FROM python
WORKDIR /db
COPY dB.py .
COPY requirementsdB.txt .
RUN pip3 install -r requirementsdB.txt
EXPOSE 500
CMD ["python3", "dB.py"]
