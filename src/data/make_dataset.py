import pandas as pd
import os

def prepare_expedia_data(input_path='data/raw/train.csv', 
                         output_path='data/processed/train_bookings_sample.csv'):
    """
    Filters the massive Expedia dataset to include only booking events.
    This creates a manageable and consistent data foundation for the team.
    """
    
    print(f"🚀 Starting data processing from {input_path}...")
    
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Define chunk size to prevent memory exhaustion (approx 500k rows at a time)
    chunk_size = 500000
    first_chunk = True
    total_rows = 0
    
    try:
        # Initialize the TextFileReader to process the file in segments
        reader = pd.read_csv(input_path, chunksize=chunk_size)
        
        for i, chunk in enumerate(reader):
            # FILTER: Keep only rows where a booking actually occurred
            # This reduces the data from ~37M rows to ~3M rows
            filtered_chunk = chunk[chunk['is_booking'] == 1]
            
            # Save: Write new file for the first chunk, then append (mode='a')
            if first_chunk:
                filtered_chunk.to_csv(output_path, index=False)
                first_chunk = False
            else:
                filtered_chunk.to_csv(output_path, index=False, mode='a', header=False)
            
            total_rows += len(filtered_chunk)
            if (i + 1) % 10 == 0:
                print(f"   Processed { (i+1) * chunk_size } rows...")

        print(f"✅ Success! Processed dataset saved at: {output_path}")
        print(f"📊 Final row count: {total_rows} (approx. 3M bookings)")

    except FileNotFoundError:
        print(f"❌ Error: The file {input_path} was not found.")
        print("💡 Action required: Download the data from Kaggle and place it in the 'data/raw/' folder.")

if __name__ == "__main__":
    prepare_expedia_data()