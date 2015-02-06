import logging

from zipkin.models import Endpoint
from zipkin.client import Client

log = logging.getLogger(__name__)


def configure(name, settings, prefix='zipkin.',
              use_requests=True, use_celery=True):
    """ Include the zipkin definitions """

    endpoint = Endpoint(name)
    Client.configure(settings, prefix=prefix)

    # Install in libs here
    if use_requests:
        from zipkin.binding.requests import bind as bind_requests
        bind_requests()

    if use_celery:
        from zipkin.binding.celery import bind as bind_celery
        bind_celery(endpoint)

    return endpoint
