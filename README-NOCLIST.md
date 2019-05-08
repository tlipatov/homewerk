# Retrieve the NOC List Homework

Simple application to retrieve the NOC list and print in JSON formatted list to STDOUT

## Building

The application is packaged into a docker container for simpler installation

Application source is in `src/badsec/main.py`


### Prerequisites

 - docker installed
 - make installed

### Create container

This will create a docker container `badsec:latest` with the application
 ```shell
cd noclist
make
```

### Run the application
If accessing a server running on a localhost, use `--net=host` flag

#### Print  help

```shell
docker run -it --net=host --rm badsec

==>
usage: badsec [-h] [-D] [-U URL]

BadSec homewerk

optional arguments:
  -h, --help         show this help message and exit
  -D, --debug        Enable debug

required arguments:
  -U URL, --url URL  NOC List Server URL http://host:port
```

### Run

```shell
docker run -it --net=host --rm badsec -U http://localhost:8888 | jq

==>
["18207056982152612516", "7692335473348482352", "6944230214351225668", "3628386513825310392",....]
```
