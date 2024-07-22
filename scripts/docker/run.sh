docker run --rm -it \
    -v "$(pwd)"/.nws.weather.config:/root/.nws.weather.config \
    nws $@