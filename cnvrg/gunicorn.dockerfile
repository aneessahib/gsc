From ubuntu:22.04

WORKDIR /cnvrg

COPY cnvrg/files/main.py ./
COPY cnvrg/files/predict.py ./
COPY cnvrg/files/caller.py ./

RUN apt-get update \
&& apt install -y \
gunicorn \
python3 \
python3-pip \
python3-flask \
&& pip3 install joblib==1.1.0 \
numpy==1.19.5 \
scikit-learn==0.24.2 \
scipy==1.5.4 \
sklearn==0.0 \
threadpoolctl==3.1.0 \
cycler==0.11.0 \
kiwisolver==1.3.1 \
matplotlib==3.3.4 \
Pillow==8.4.0 \
pyparsing==3.0.9 \
python-dateutil==2.8.2 \
plotly==5.8.2 \
tenacity==8.0.1 \
transformers \
torch \
pandas==1.1.5 \
pytz==2022.1 \
cnvrg==0.7.54 \
cnvrgv2==1.0.17

RUN rm -rf /usr/lib/python3/dist-packages/OpenSSL \
&& pip3 install pyopenssl \
&& pip3 install pyopenssl --upgrade

ENTRYPOINT ["gunicorn"]
