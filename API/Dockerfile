FROM python
WORKDIR /api
COPY api.py .
COPY requirementsApi.txt .
RUN pip3 install -r requirementsApi.txt
EXPOSE 5000
CMD ["python3", "api.py"]
