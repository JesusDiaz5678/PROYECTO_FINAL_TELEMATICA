FROM python
WORKDIR /front
COPY front.py .
COPY requirementsFront.txt .
RUN pip3 install -r requirementsFront.txt
EXPOSE 5010
CMD ["python3", "front.py"]
