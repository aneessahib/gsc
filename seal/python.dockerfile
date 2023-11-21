FROM python:3.8.10 

RUN mkdir files && cd files
RUN apt-get update 
RUN apt-get install -y build-essential
COPY sealed_test.c .
COPY entrypoint.manifest.sgx .
COPY entrypoint.sig .
#COPY inp_files/plain_text.txt .
RUN mkdir inp_files
RUN gcc sealed_test.c -o seal.out
RUN mkdir tmp_enc
RUN rm sealed_test.c 
RUN cp seal.out /usr/bin/
