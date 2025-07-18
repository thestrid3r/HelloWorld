FROM python:3.8-alpine

# Create a non-root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

# Copy requirements and install with no cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . .

# Set permissions (optional if you're not writing to disk)
RUN chown -R appuser:appgroup /app

# Switch to non-root user
USER appuser

EXPOSE 8080

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=8080" ]
