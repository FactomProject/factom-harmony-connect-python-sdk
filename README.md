Table of Contents
===============
[INTRODUCTION](#Introduction)
- [About This Document](#about)
- [SDK Architecture Overview](#architecture)

[GETTING STARTED](#gettingstarted)
 - [System Requirements](#requirements)
 - [Installation](#installation)
 - [Usage](#usage)
 - [License](#license)

[METHODS](#methods)

[SAMPLE APPLICATION](#sampleapplication)
- [Overview](#overview)
- [Installation](#appinstallation)
- [Usage](#appusage)

<a name="Introduction"></a>INTRODUCTION
============

<a name="about"></a>About This Document
-------------------

This documentation is written for developers with a basic level of
coding knowledge and familiarity of the Python programming language.

Readers can find guidelines to quickly get started with building and
using the Python SDK for Factom Harmony Connect.

You can learn more about Factom Harmony Connect
[here](https://docs.harmony.factom.com/).

This SDK is open source and can be accessed on Github
[here](https://github.com/FactomProject/factom-harmony-connect-python-sdk).

<a name="architecture"></a>SDK Architecture Overview
-------------------------

![architecture](documentation/pictures/architecture.jpg?raw=true)

**FactomSDK Class:** Manages SDK constructor, product connection and
provides access to other layers.

**Utilities:** Contain functions shared between core components.

**Core:** Contains main components that interact with Connect API.

**Request/Response Handler:** Handles all requests/responses (HTTP /
HTTPS) from Connect API before passing them to other components.

<a name="gettingstarted"></a>GETTING STARTED
===============

This section contains a summary of the steps required to get started
with Python Connect SDK installation.

<a name="requirements"></a>System Requirements
-------------------

In order to use this Python SDK, you will need the following tool:

-  Python version >= 3.5


<a name="installation"></a>Installation
-------------
**Published package**

`pip install factom-harmony-connect`

**Open-source package**

- Clone the repo
- Setup a virtual environment (optional)
- Install dependencies
  - `pip install -r requirements.txt`

To use the SDK, you have to import: `from factom_sdk import FactomClient`


<a name="usage"></a>Usage
-----


For more details of a specific module, please refer to the
[**Methods**](#METHODS) section.

If you want to understand how the SDK works in practice, refer to the
[**Sample Application**](#sampleapplication) section.

Below is an example of how to use the SDK. Before executing any
requests, you will need to instantiate an instance of the SDK. The
required parameters include details about the application you will be
using to authenticate your requests. If you do not have an application
yet, you can get one
[here](https://account.factom.com).

```python
factom_client = FactomClient("YOUR_BASE_URL", "YOUR_APP_ID","YOUR_APP_KEY")
```


When the Factom SDK is initialized, there will be an optional
`automatic_signing` param, which defaults to `true`.

-   When this initial config is set to `true` as default, all chain
    and entry POST methods require passing the params:
    `signer_private_key` and `signer_chain_id` which will be used to create signed chains and entries,
    as per the [Factom Signing Standard](https://docs.harmony.factom.com/docs/factom-signing-standard).

-   When this initial config is set to `false`, the FactomSDK will not sign the chains and entries that are
    created and therefore it does not require the params: `signer_private_key` and `signer_chain_id`.

The primary benefit of `automatic_signing` param is to encourage you to
create chains and entries with unique signatures. Later on, you can
validate that the chains or entries were created by you or that a
certain user/device/ organization/etc. actually signed and published a
certain message that you see in your chain.

Now that you have initialized the SDK, you can use the SDK's Methods,
which will execute the necessary REST API calls on your behalf.

**Note:** The SDK requires to pass all optional parameters with `**kwargs` added as final arguments. Please refer to [**Methods**](#METHODS) section to get the correct parameter names.

Patterns to utilize the Factom SDK:
```python
# Return a JSON chain object as is from the API.
chain = factom_client.chains.get('5dc94c605769d8e9dac1423048f8e5a1182e575aab6d923207a3a8d15771ad63')

# Return JSON entries array as is from API.
entries = factom_client.chains.entries.list('5dc94c605769d8e9dac1423048f8e5a1182e575aab6d923207a3a8d15771ad63')

# Return a JSON single entry object as is from the API.
entry = factom_client.chains.entries.get('5dc94c605769d8e9dac1423048f8e5a1182e575aab6d923207a3a8d15771ad63',
                                         'e0e2b7f7920ce25c20cf98c13ae454566e7cda7bb815b8a9ca568320d7bdeb93')
```

**Note:** The SDK allows for override values that were set in the instatiation of the SDK on a per-method call basis. To override desired parameters that were set in the instantiated SDK class, you may specify any of the following properties in the calls where these properties apply:

- `app_id`
- `app_key`
- `base_url`
- `automatic_signing`

Example:

```python
# Create a chain with automatic_signing turned off for one call
 create_chain_response = factom_client.chains.create(
   'TestOverrides',
   external_ids = ['TestOverrides', 'CustomerChain', 'cust123'],
   automatic_signing = False
 )

# Return a JSON chain object as is from the API with new app_id, app_key and base_url.
chain = factom_client.chains.get('5dc94c605769d8e9dac1423048f8e5a1182e575aab6d923207a3a8d15771ad63',
  base_url = 'https://ephemeral.api.factom.com/v1',
  app_id = '4db6b007',
  app_key = 'ec0c88e3c5bb57cd7303d070ad838260'
)

# Return JSON entries array as is from API with new app_id, app_key and base_url.
entries = factom_client.chains.entries.list('5dc94c605769d8e9dac1423048f8e5a1182e575aab6d923207a3a8d15771ad63',
  base_url = 'https://ephemeral.api.factom.com/v1',
  app_id = '4db6b007',
  app_key = 'ec0c88e3c5bb57cd7303d070ad838260'
)

# Return a JSON single entry object as is from the API with new app_id, app_key and base_url.
entry = factom_client.chains.entries.get('5dc94c605769d8e9dac1423048f8e5a1182e575aab6d923207a3a8d15771ad63',
  'e0e2b7f7920ce25c20cf98c13ae454566e7cda7bb815b8a9ca568320d7bdeb93',
  base_url = 'https://ephemeral.api.factom.com/v1',
  app_id = '4db6b007',
  app_key = 'ec0c88e3c5bb57cd7303d070ad838260'
)
```



<a name="license"></a>License
-------

The Harmony Connect SDK is provided with an [MIT License](LICENSE).

# <a name="methods"></a> METHODS

<a name="utils"></a>[utils](documentation/utils.md)
 - <a name="generate_key_pair"></a>[generate_key_pair](documentation/utils.md#generate_key_pair)
 - <a name="convert_raw_to_key_pair"></a>[convert_raw_to_key_pair](documentation/utils.md#convert_raw_to_key_pair)
 - <a name="convert_to_raw"></a>[convert_to_raw](documentation/utils.md#convert_to_raw)

<a name="identities"></a>[identities](documentation/identities.md)
  - <a name="identities_create"></a>[create](documentation/identities.md#identities_create)
  - <a name="identities_get"></a>[get](documentation/identities.md#identities_get)
  - <a name="identities_keys"></a>[keys](documentation/identities.md#identities_keys)
     - <a name="keys_list"></a>[list](documentation/identities.md#keys_list)
     - <a name="keys_get"></a>[get](documentation/identities.md#keys_get)
     - <a name="keys_replace"></a>[replace](documentation/identities.md#keys_replace)

<a name="api_info"></a>[api_info](documentation/api_info.md)
  - <a name="info_get"></a>[get](documentation/api_info.md#info_get)

<a name="chains"></a>[chains](documentation/chains.md)
  - <a name="chains_get"></a>[get](documentation/chains.md#chains_get)
  - <a name="chains_create"></a>[create](documentation/chains.md#chains_create)
  - <a name="chains_list"></a>[list](documentation/chains.md#chains_list)
  - <a name="chains_search"></a>[search](documentation/chains.md#chains_search)
  - <a name="chains_entries"></a>[entries](documentation/chains.md#chains_entries)
     - <a name="entries_get"></a>[get](documentation/chains.md#entries_get)
     - <a name="entries_create"></a>[create](documentation/chains.md#entries_create)
     - <a name="entries_list"></a>[list](documentation/chains.md#entries_list)
     - <a name="entries_first"></a>[get_first](documentation/chains.md#entries_first)
     - <a name="entries_last"></a>[get_last](documentation/chains.md#entries_last)
     - <a name="entries_search"></a>[search](documentation/chains.md#entries_search)

<a name="anchors"></a>[anchors](documentation/chains.md)
  - <a name="anchors_get"></a>[get](documentation/anchors.md#anchors_get)

<a name="receipts"></a>[receipts](documentation/receipts.md)
  - <a name="receipts_get"></a>[get](documentation/receipts.md#receipts_get)

# <a name="sampleapplication"></a> SAMPLE APPLICATION


<a name="overview"></a> Overview
--------
![architecture](documentation/pictures/sample-app-1.jpg?raw=true)

This Sample App is created to illustrate some of the core methods of this SDK and a real-world
business scenario of how it can be used.

Since the application is built as a standalone application with a backend SDK process,
the reader should review the commented code [here](https://github.com/FactomProject/factom-harmony-connect-python-sdk/blob/master/sample_app/simulate_notary.py).

The concept of the Sample App is a simple Notary service with a business flow as follows:


-   **A Notary service begins using Factom Harmony:** To use Harmony, there should be at least 1 identity used when signing written data. So, to start, the app creates an identity’s chain for the Notary service.

-   **The first customer purchases the Notary service’s new “Blockchain authentication” service tier:** To track the customer’s documents, the app creates a signed chain for them, allowing easy retrieval for that customer’s records.


-   **The customer requests notarization of the first document:** The app creates a signed entry within the customer’s chain containing a hashed version of the document. At this time, the notary service should also be storing the document in a secure location.

-   **The customer returns at a later date and the clerk retrieves the past work for this customer:** The app searches the blockchain for the customer’s chain, and with that data, retrieves the chain. The SDK automatically validates the authenticity of this chain, which ensures that the Notary’s systems have not been tampered with and the blockchain data was submitted by the Notary service.

-   **The customer requests the document that was notarized:** The app searches for an entry in the chain validated in the step above and gets that entry info, then validates the authenticity of the signature used to sign that entry.


-   **The document’s authenticity is validated:** The app pulls out the document’s hash from the entry’s content and compares it against a freshly generated hash of a stored document.
    -   **Note:** It is recommended that in a real-world scenario, scheduled tasks are run to validate the data for proactive validation.

-   **A developer who had access to one of the keys leaves employment with the Notary company, so they carry out proactive security:** The app replaces the old key pair that the employee had access to.


<a name="appinstallation"></a>Installation
------------

1.  Checkout the repository.
2.  Run `pip install -r requirements.txt`.
3.  Navigate to folder `cd ./sample_app`.
5.  Open `configure.py`.
6.  Change configuration settings with your BASE_URL, APP_ID and APP_KEY, which can be found or generated at <https://account.factom.com>.
7.  Run `python route.py`.
8.  Open localhost:8080 on your browser.

<a name="appusage"></a>Usage
-----

**Starting screen:** The app comes with a starting page where the user
clicks the "Run Notary Simulation" button to run the app.

![architecture](documentation/pictures/sample-app-2.jpg?raw=true)

**Simulating screen:** Then the system will take some time to generate all responses by calling the Harmony Connect API through the Python Connect SDK in Python backend.

![architecture](documentation/pictures/sample-app-3.jpg?raw=true)

**Response screen:** After the loading process is finished, the app will display relevant data with regard to this business flow.

![architecture](documentation/pictures/sample-app-4.jpg?raw=true)
