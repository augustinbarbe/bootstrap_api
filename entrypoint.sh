#!/bin/bash
set -e

case "$1" in
        api)
            echo "starting api"
	          gunicorn -c ./config/gunicorn_conf.py --log-config config/logging.conf "customers:app"
            ;;
esac
