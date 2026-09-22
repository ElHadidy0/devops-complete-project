import os
from flask import Flask, jsonify
import redis
import psycopg2
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# تفعيل الـ Prometheus Metrics أوتوماتيك على الـ API
metrics = PrometheusMetrics(app)

# ميكروفون ثابت للـ App Info في الـ Metrics
metrics.info('app_info', 'Application Info', version='1.0.0')

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "shop_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Enterprise E-Commerce DevOps API with Prometheus & Grafana!",
        "status": "Running smoothly"
    })

@app.route("/check-db")
def check_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD
        )
        conn.close()
        return jsonify({"database_status": "Connected successfully to PostgreSQL! 🟢"})
    except Exception as e:
        return jsonify({"database_status": f"Connection failed: {str(e)} 🔴"}), 500

@app.route("/check-redis")
def check_redis():
    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        r.ping()
        return jsonify({"redis_status": "Connected successfully to Redis! 🟢"})
    except Exception as e:
        return jsonify({"redis_status": f"Connection failed: {str(e)} 🔴"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
