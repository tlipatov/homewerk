FROM python:3.6

COPY src/ /badsec
WORKDIR /badsec
RUN pip install /badsec

ENTRYPOINT ["badsec"]
CMD ["-h"]
