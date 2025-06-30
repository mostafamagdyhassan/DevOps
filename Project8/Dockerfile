FROM python:3.10-slim
WORKDIR /app
COPY sensor_emulator.py .
RUN pip install requests
CMD ["python", "sensor_emulator.py"]
