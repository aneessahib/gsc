FROM ubuntu:20.04

WORKDIR /files
RUN apt-get update 
RUN apt-get install -y build-essential
COPY sealed_test.c .
#COPY inp_files/plain_text.txt .
RUN mkdir inp_files
RUN gcc sealed_test.c -o seal.out
RUN mkdir tmp_enc
RUN cp seal.out /usr/bin/
ENTRYPOINT ["seal.out"]
