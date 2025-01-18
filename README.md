# EdaWithKafkaAndDjango

## Overview

This project demonstrates an event-driven architecture (EDA) implementation using Django and Kafka. It includes producers and consumers for handling events, integrated with Celery for asynchronous task management.

## Features
- Kafka integration for real-time message streaming.
- Django-based API for managing orders.
- Celery for handling background tasks.
- Docker support for containerized deployment.

## Project Structure
```
EdaWithKafkaAndDjango-main/
├── .gitignore
├── docker-compose.yml
├── dockerfile
├── dockerfile.celery
├── manage.py
├── requirements.txt
├── EdaWithKafkaAndDjango/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── consumer/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── celery.py
│   ├── kafka_consumer.py
│   ├── models.py
│   ├── tasks.py
│   ├── tests.py
│   ├── views.py
│   ├── migrations/
│       └── __init__.py
├── order/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── kafka_producer.py
│   ├── models.py
│   ├── tasks.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│       ├── 0001_initial.py
│       ├── 0002_remove_order_order_id_alter_order_order_date.py
│       └── __init__.py
```

## Requirements

- Docker
- Python 3.9+
- Kafka server

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/EdaWithKafkaAndDjango.git
   cd EdaWithKafkaAndDjango
   ```

2. **Build and Run Containers**:
   ```bash
   docker-compose up --build
   ```

3. **Apply Migrations**:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. **Start Kafka** (if not already running):
   Ensure that Kafka broker and Zookeeper are running before testing.

5. **Run the Development Server**:
   ```bash
   docker-compose exec web python manage.py runserver
   ```

## Usage

- **Producer**:
  The `order` app produces Kafka messages when an order is created or updated.

- **Consumer**:
  The `consumer` app listens to Kafka topics and processes events accordingly.

- **API**:
  Endpoints for managing orders are available under the `order` app's views.

  You can send an order by making a request to the following URL:
   ```
   localhost:8000
   ```

  You can start consuming messages by making a request to the following URL:
  ```
  localhost:8000/run_consumer
  ```


## Remote Debugging

You can use the following  vscode launch configurations for remote debugging in your IDE:

```jsonc
{
   "version": "0.2.0",
   "configurations": [
      {
            "name": "Main App",
            "type": "python",
            "request": "attach",
            "host": "localhost",
            "port": 5679,
            "pathMappings": [
               {
                  "localRoot": "${workspaceFolder}",
                  "remoteRoot": "/app"
               }
            ]
      },
   ]
}
```





## Important Files

- `docker-compose.yml`: Defines services for Django, Kafka, and Celery.
- `consumer/kafka_consumer.py`: Kafka consumer logic.
- `order/kafka_producer.py`: Kafka producer logic.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Developed with ❤️ using Django and Kafka.
