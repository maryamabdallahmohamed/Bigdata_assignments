#!/bin/bash

CONTAINER_ID="9371a18fdaf5cb5ba133e9dfa641bbccf1ebb70136e4be12a0700e42a33351ca"  # Replace with your actual container ID
LOCAL_DEST="bd-a1/service-result"  

# Create the destination directory if it doesn't exist
mkdir -p "$LOCAL_DEST"

# Copy output files from the container to local machine
echo "Copying output files from container to local machine..."
# Copy Python scripts
docker cp "$CONTAINER_ID:dpre.py" "$LOCAL_DEST/"
echo "Copied dpre.py"

docker cp "$CONTAINER_ID:eda.py" "$LOCAL_DEST/"
echo "Copied eda.py"

docker cp "$CONTAINER_ID:vis.py" "$LOCAL_DEST/"
echo "Copied vis.py"

docker cp "$CONTAINER_ID:model.py" "$LOCAL_DEST/"
echo "Copied model.py"

docker cp "$CONTAINER_ID:load.py" "$LOCAL_DEST/"
echo "Copied load.py"

# Copy text files
docker cp "$CONTAINER_ID:eda-in-1.txt" "$LOCAL_DEST/"
echo "Copied eda-in-1.txt"

docker cp "$CONTAINER_ID:eda-in-2.txt" "$LOCAL_DEST/"
echo "Copied eda-in-2.txt"

docker cp "$CONTAINER_ID:eda-in-3.txt" "$LOCAL_DEST/"
echo "Copied eda-in-3.txt"

docker cp "$CONTAINER_ID:k.txt" "$LOCAL_DEST/"
echo "Copied k.txt"

# Copy visualization files
docker cp "$CONTAINER_ID:vis.png" "$LOCAL_DEST/"
echo "Copied vis.png"

docker cp "$CONTAINER_ID:vis2.png" "$LOCAL_DEST/"
echo "Copied vis2.png"

# Copy CSV files
docker cp "$CONTAINER_ID:res_dpre.csv" "$LOCAL_DEST/"
echo "Copied res_dpre.csv"



# Stop the container
echo "Stopping container $CONTAINER_ID..."
docker stop "$CONTAINER_ID"

echo "Process completed. Files copied to $LOCAL_DEST and container stopped."