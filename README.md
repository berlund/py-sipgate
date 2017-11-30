# Sipgate REST API client

This is a API client for the Sipgate REST API, available at [https://developer.sipgate.io](https://developer.sipgate.io).

Minimum Python version 3 is recommended.

## Supported operations
Currently supported operations are:

* GET `devices/`
* GET `devices/{device_id}`

## Supported authentication schemes

Basic Authentication is the only supported mechanism.

## Usage

```python
from sipgate import Client

c = Client(USERNAME, PASSWORD)

# Gets all registered Sipgate devices
devices = c.devices()

# Gets one specific device
device = c.device_by_id(devices[0].id)

```
