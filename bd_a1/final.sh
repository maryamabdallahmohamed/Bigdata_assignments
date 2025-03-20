CONTAINER_ID="c373825a7db226ad80e82ef6c471783bab1b477e8110777d79bbe7b2c3aa6a8b" 
LOCAL_DEST="bd-a1/service-result"  

mkdir -p "$LOCAL_DEST"

echo "Copying output files from container to local machine..."

docker cp "$CONTAINER_ID:/home/doc-bd-a1/dpre.py" "$LOCAL_DEST/"
echo "Copied dpre.py"

docker cp "$CONTAINER_ID:/home/doc-bd-a1/eda.py" "$LOCAL_DEST/"
echo "Copied eda.py"

docker cp "$CONTAINER_ID:/home/doc-bd-a1/vis.py" "$LOCAL_DEST/"
echo "Copied vis.py"

docker cp "$CONTAINER_ID:/home/doc-bd-a1/model.py" "$LOCAL_DEST/"
echo "Copied model.py"

docker cp "$CONTAINER_ID:/home/doc-bd-a1/load.py" "$LOCAL_DEST/"
echo "Copied load.py"

docker cp "$CONTAINER_ID:/home/doc-bd-a1/eda-in-1.txt" "$LOCAL_DEST/"
echo "Copied eda-in-1.txt"

docker cp "$CONTAINER_ID:/home/doc-bd-a1/eda-in-2.txt" "$LOCAL_DEST/"
echo "Copied eda-in-2.txt"

docker cp "$CONTAINER_ID:/home/doc-bd-a1/eda-in-3.txt" "$LOCAL_DEST/"
echo "Copied eda-in-3.txt"

docker cp "$CONTAINER_ID:/home/doc-bd-a1/k.txt" "$LOCAL_DEST/"
echo "Copied k.txt"


docker cp "$CONTAINER_ID:/home/doc-bd-a1/vis.png" "$LOCAL_DEST/"
echo "Copied vis.png"

docker cp "$CONTAINER_ID:/home/doc-bd-a1/vis2.png" "$LOCAL_DEST/"
echo "Copied vis2.png"

docker cp "$CONTAINER_ID:/home/doc-bd-a1/res_dpre.csv" "$LOCAL_DEST/"
echo "Copied res_dpre.csv"

docker cp "$CONTAINER_ID:/home/doc-bd-a1/res_dpre.csv" "$LOCAL_DEST/"
echo "Copied res_dpre.csv"


docker cp "$CONTAINER_ID:/home/doc-bd-a1/Markdown.md" "$LOCAL_DEST/"
echo "Copied Markdown.md"


echo "Stopping container $CONTAINER_ID..."
docker stop "$CONTAINER_ID"

echo "Process completed. Files copied to $LOCAL_DEST and container stopped."