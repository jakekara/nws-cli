# Docker usage

Docker is used for dev purposes but might be a preferred way
for some users to install this tool. This documentation will 
assume plenty of Docker experience. There isn't any benefit
to using Docker if you're not already familiar with it.

## Build the image

This is mostly just to test that package builds and installs
properly.

Run:

```shell
sh scripts/docker/build.sh
```

This will build an image called `nws`.

## Run the app in docker

When you run the app in docker, it will create a `.nws.weather.config`
file in your current directory on the host machine, so any configs
you set inside the container using the `wizard` subcommand will be 
persisted to that file.

```shell
sh scripts/docker/run.sh ARGS
```

The entrypoint is the `nws` script so the args start at the 
subcommand you wish to run. For example:

```shell
sh scripts/docker/run.sh wizard
```

The usage is the same as using the app from a Python environment,
but instead of running `nws wizard` you run `sh scripts/docker/run.sh
wizard`.

Since the config file is persisted with a volume mount (see the 
bash script for more), you won't lose your config between executions.