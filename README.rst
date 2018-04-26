.. image:: https://travis-ci.org/urbanairship/reach-python-library.svg?branch=master
    :target: https://travis-ci.org/urbanairship/reach-python-library

About
=====

The Urban Airship ``uareach`` (formerly known as ``wallet``) library is a Python library for
using the `Urban Airship Reach <http://urbanairship.com/>`__ web service API.

Version 0.1.0 is a beta release.  Please visit `Urban Airship Support
<https://support.urbanairship.com/>`_ with questions or comments.

Requirements
============

As of version 0.1.0, Python 2.7 is required.

Development
=============

Install development dependencies:

    $ pip install -r requirements.txt

Install the library in editable mode:

    $ pip install --editable .

Run tests with:

    $ nosetests

Usage
=====

To get started, simply import the library and set up a client:

.. sourcecode:: python

   import uareach as ua


   client = ua.Reach('email', 'wallet_key')


   # Example: getting a pass
   my_pass = ua.get_pass(client, pass_id=12345)

For more details on using the library, please see the `full documentation
<http://docs.urbanairship.com/reference/libraries>`__, as well as the
`Urban Airship API Documentation <http://docs.urbanairship.com/api/wallet.html>`__.
