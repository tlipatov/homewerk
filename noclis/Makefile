NAME=$(shell cat src/setup.py  | grep name | cut -f 2 -d '"')
VERSION=$(shell cat src/setup.py  | grep version | cut -f 2 -d '"')
IMAGE=badsec

all: docker_build

docker_build:
	docker build -t $(IMAGE):$(VERSION) .
	docker tag $(IMAGE):$(VERSION) $(IMAGE):latest
