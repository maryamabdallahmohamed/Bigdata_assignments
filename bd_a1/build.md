# Sleep Health Analysis Docker Container

## Build the container
```bash
docker build -t sleep_health:latest .
```

## Run the container
```bash
docker run -it -v $(pwd):/home/doc-bd-a1 sleep_health:latest
```
```
## Activate virtual enviroment
/opt/venv/bin/python /home/doc-bd-a1/load.py