Testing
=======

Requirements:

* Ansible >= 1.6
* Vagrant >= 1.6
* Tox

Execute unit tests:

.. code-block:: bash

	$ make

Manually Testing
================

In one window.  Publish an initial message, and create the topic:

.. code-block:: bash

	$ curl -d 'hello world 1' 'http://192.168.90.12:4151/put?topic=test'

In the same window, start the client:

.. code-block:: bash

	nsq_to_file --topic=test --output-dir=/tmp --lookupd-http-address=192.168.90.12:4161

In another window, publish more messages:
 
.. code-block:: bash

	curl -d 'hello world 2' 'http://192.168.90.12:4151/put?topic=test'
