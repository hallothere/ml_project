import pandas as pd
import os
from pathlib import Path

def make_dataset():
    """
    Creates a consolidated dataset by merging booking events with destination data,
    applying memory optimizations (chunking, float32 casting), and saving as Parquet.
    """
    # Define paths using Pathlib
    PROJECT_ROOT = Path(".")
    DATA_DIR = PROJECT_ROOT / "data"
    raw_train_path = DATA_DIR / "raw" / "train.csv"
    raw_dest_path = DATA_DIR / "raw" / "destinations.csv"
    processed_path = DATA_DIR / "processed" / "df_model.parquet"
    
    # 1. Load destinations and prepare index (Nils' logic)
    print("Loading destinations...")
    df_dest = pd.read_csv(raw_dest_path).set_index("srch_destination_id")
    dest_cols = df_dest.columns.tolist()
    
    # Initialize chunking process
    chunk_size = 500000
    all_processed_chunks = []
    
    print("Starting chunking, merging and cleaning...")
    
    # 2. Process train.csv in chunks to prevent memory overflow
    for chunk in pd.read_csv(raw_train_path, chunksize=chunk_size):
        
        # A. Filter for successful bookings only
        chunk = chunk[chunk['is_booking'] == 1].copy()
        
        # B. Merge with destination data (Left join on destination ID)
        chunk = chunk.merge(
            df_dest,
            how="left",
            left_on="srch_destination_id",
            right_index=True
        )
        
        # C. Remove records with missing destination signals (12,516 records expected to drop)
        chunk = chunk.dropna(subset=dest_cols)
        
        # D. Optimize memory: Cast destination features to float32
        chunk[dest_cols] = chunk[dest_cols].astype("float32")
        
        # Collect processed chunks in memory
        all_processed_chunks.append(chunk)
        print(f"Processed chunk... current total rows: {sum(len(c) for c in all_processed_chunks)}")

    # 3. Concatenate all processed chunks and save as high-performance Parquet
    print("Consolidating data and saving to Parquet...")
    df_final = pd.concat(all_processed_chunks, ignore_index=True)
    
    # Ensure the directory exists
    os.makedirs(DATA_DIR / "processed", exist_ok=True)
    
    df_final.to_parquet(processed_path, index=False)
    
    print(f"Done! Final dataset saved to {processed_path}")
    print(f"Final shape: {df_final.shape}") # Target shape: (2,988,177, 173)

if __name__ == "__main__":
    make_dataset()