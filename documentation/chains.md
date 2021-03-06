chains
------

### Table of Contents

- [get](#chains_get)
- [create](#chains_create)
- [list](#chains_list)
- [search](#chains_search)
- [entries](#chains_entries)
	- [get](#entries_get)
	- [create](#entries_create)
	- [list](#entries_list)
	- [get_first](#entries_first)
	- [get_last](#entries_last)
	- [search](#entries_search)

### <a name="chains_get"></a>get

Gets information about a specific chain from Connect.

**Sample**
```python
factom_client.chains.get('4b9532c79d53ab22b85951b4a5853f81c2682132b3c810a95128c30401cd1e58')
```

**Parameters**

| **Name**                     | **Type** | **Description**                                                                                                                                                                                                                                                                       | **SDK Error Message & Description**       <img width=400/>                        |
|------------------------------|----------|------------------------------------------------------------------------------|---------------------------------------------------------------------|
| `chain_id`                   | required | string </br> The unique identifier created for each chain.                                                                                                                                                                                                                            | **chain_id is required** </br> `chain_id` parameter was not provided. |
| `signature_validation`       | optional | boolean (`True`/`False`/`custom function`) </br> Default value is `True`. Indicates whether the SDK automatically validates that the chain was signed based on our signing standard. </br> `custom function`: allows for validating the chain's signature  based on custom logic. |
| `app_id`            | optional | string </br> This is the override parameter that allows user to specify a different API Application ID (which you can see by clicking on any of the applications in the application list that you see upon logging into  https://account.factom.com).               |
| `app_key`           | optional | string </br> This is the override parameter that allows user to specify a different API Application Key (which you can see by clicking on any of the applications in the application list that you see upon logging into  https://account.factom.com).              |
| `base_url`          | optional | string </br> This is the override parameter that allows user to specify a different API Base URL for your application (which you can see by clicking on any of the applications in the application list the you see upon logging into  https://account.factom.com). |



**Returns**

**Response:** OK
-   **data:** object
    -   **data.chain_id:** string </br> The unique identifier created for each chain.
    -   **data.content:** string </br> The data that was stored in the first entry of this chain.
    -   **data.external_ids:** array of strings </br> Tags that have been used to identify the first entry of this chain.
    -   **data.stage:** string </br> The immutability stage that this chain has reached.
    -   **data.entries:** object
        -   **data.entries.href:** string </br> An API link to all of the entries in this chain.
    -   **data.eblock:** object </br> Represents the Entry Block that contains the first entry of this chain. This will be null if the chain is not at least at the `factom` immutability stage.
	    -   **data.eblock.keymr:** string </br> The Key Merkle Root for this entry block.
	    -   **data.eblock.href:** string </br> An API link to retrieve all information about this entry block.
	-   **data.dblock:** object </br> Represents the Directory Block that relates to this chain. This will be null if the chain is not at least at the `factom` immutability stage.
		-   **data.dblock.keymr:** string </br> The Key Merkle Root for this directory block.
		-   **data.dblock.height:** integer </br> The Factom blockchain height of this directory block.
		-   **data.dblock.href:** string </br> An API link to retrieve all information about this directory block.
	-   **data.created_at:** string </br> The time at which the chain was created. Sent in [ISO 8601 Format](https://en.wikipedia.org/wiki/ISO_8601). For example: `YYYY-MM-DDThh:mm:ss.ssssssZ`. This will be null if the chain is not at least at the `factom` immutability stage.
-   **status:** string </br> The result of signature validation.</br>
Displays an empty string ("") when `signature_validation` is set to `False`.
</br> Or displays a function's result when `signature_validation` is set to `custom function`.
</br> In case `signature_validation` is set to `True` then one of the following values will be returned based on an automatic comparison of the expected SignedChain structure outlined in our signing standard.
    -   **not_signed/invalid_chain_format:** A chain that was not signed or did not conform to the SignedChain structure.
    -   **invalid_signature:** A chain was created in the proper SignedChain structure, but the signature does not match the attached key.
    -   **retired_height:** A chain that conformed to the SignedChain structure and the signature was verified with the listed key, but
    that key was retired for the signer identity at a height lower than when this chain reached the `factom` immutability stage.
    -   **key_not_found:** A chain that conformed to the SignedChain structure but the signer public key does not belong to the signer identity chain.
    -   **valid_signature:** A chain that conformed to the SignedChain structure and the signature was verified with the listed key. That key was also active for the signer identity at the height when this chain reached the `factom` immutability stage.

 ```python
 {
   'chain':{
      'data':{
         'stage':'replicated',
         'external_ids':[
            'SignedChain',
            '0x01',
            'd22fd62b2c64061d48121d24bfa4e57826caaf532df1524da6eb243da3daa84f',
            'idpub25ZVKWA7BqTM7VmBtWK5DYNQwusqMpxbWABigfvqqQVNcd2Fr6',
            '2a0ebd83a34fef6e38049815d199398eb4e5ed34a32e8f9f1fa6184d2ec6015e7be601d0fb75679e62575c3cdd7779f52a84a9853f8725932e3a92143d2b3c05',
            '2019-03-15T03:43:22.200505',
            'NotarySimulation',
            'CustomerChain',
            'cust123'
         ],
         'entries':{
            'href':'/v1/chains/4b9532c79d53ab22b85951b4a5853f81c2682132b3c810a95128c30401cd1e58/entries'
         },
         'eblock':None,
         'dblock':None,
         'created_at':None,
         'content':"This chain represents a notary service's customer in the NotarySimulation, a sample implementation provided as part of the Factom Harmony SDKs. Learn more here: https://docs.harmony.factom.com/docs/sdks-clients",
         'chain_id':'4b9532c79d53ab22b85951b4a5853f81c2682132b3c810a95128c30401cd1e58'
      }
   },
   'status':'valid_signature'
}
 ```

### <a name="chains_create"></a>create

Creates a new chain with or without signature:

-   When the Factom SDK is initialized, if `automatic_signing` =  `True`; in order to create a signed chain, you need to pass:
    -   `signer_chain_id`
    -   `signer_private_key`
-   When the Factom SDK is initialized, if `automatic_signing` = `False`, SDK creates an unsigned chain and therefore it does not require these parameters.

**Sample**
```python
factom_client.chains.create(
    "This chain represents a notary service's customer in the NotarySimulation, a sample implementation provided as"
    " part of the Factom Harmony SDKs. Learn more here: https://docs.harmony.factom.com/docs/sdks-clients",
    signer_chain_id='d22fd62b2c64061d48121d24bfa4e57826caaf532df1524da6eb243da3daa84f',
    external_ids=["NotarySimulation", "CustomerChain", "cust123"],
    signer_private_key='idsec2rY42dadPcytBLEx9sanpCJk3PHqLnVwMYuPF7jcmDULVRySH2'
)
```

**Parameters**


| **Name**                  | **Type**                               | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                      | **SDK Error Message & Description**       <img width=1500/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `external_ids`            | required </br> or </br> optional </br> | array of strings</br> Tags that can be used to identify your chain. You can search for records that contain a particular `external_ids` using Connect.</br>  **Note:** Since the Connect API requires each array element to be Base64 encoded, the SDK will do so before making the API request. This parameter is only required for creating an unsigned chain (`automatic_signing` is set to `False`). | **at least 1 external_id is required.** </br> `external_ids` parameter was not provided when `automatic_signing` was set to `False`. </br></br>**external_ids must be an array.**</br>  An invalid `external_ids` format was provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `content`                 | required                               | string </br>  This is the data that will make up the first entry in your new chain. It is customary to use this space to describe the entries that are to follow in the chain.</br> **Note:** Since the Connect API requires the `content` to be Base64 encoded, the SDK will do so before making the API request.                                                                                | **content is required.**</br>    `content` parameter was not provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `signer_chain_id`         | required </br> or </br> optional </br> | string </br> The chain id of the signer identity.</br> **Note:** This parameter is optional for creating an unsigned chain. However, if `signer_private_key` is inputted then `signer_chain_id` must also be inputted.                                                                                                                                                                                | In case of creating a signed chain: </br>**signer_chain_id is required.** </br> `signer_chain_id` parameter was not provided. </br></br>In case of creating an unsigned chain:</br>**signer_chain_id is required when passing a signer_private_key.**</br> `signer_private_key` parameter was provided but lacking `signer_chain_id` parameter.                                                                                                                                                                                                                                                                                                                                       |
| `signer_private_key`      | required </br> or </br> optional </br> | base58 string in Idsec format</br> The private key signer would like to sign with. In fact, private key is used to generate the public key, which is included as an external ID on the created signed entry. </br> **Note:** This parameter is optional for creating an unsigned chain. However, if `signer_chain_id` is inputted then `signer_private_key` must also be inputted.                                     | In case of creating a signed chain:</br>**signer_private_key is required.**</br> `signer_private_key` parameter was not provided.</br></br>  **signer_private_key is invalid.** </br> An invalid `signer_private_key` parameter was provided or key’s byte length is not equal to 41. </br></br> In case of creating an unsigned chain: </br> **signer_private_key is required when passing a signer_chain_id.** </br>   `signer_chain_id` parameter was provided but lacking `signer_private_key` parameter.  </br></br>  **signer_private_key is invalid.**  </br> `signer_chain_id` was provided but either an invalid `signer_private_key` parameter was also provided or key’s byte length is not equal to 41. |
| `callback_url`            | optional                               | string </br> The URL where you would like to receive the callback from Connect. </br> **Note:** If this is not specified, callbacks will not be activated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | **callback_url is an invalid url format.** </br> An invalid `callback_url` format was provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `callback_stages`         | optional                               | array of strings </br> The immutability stages you would like to be notified about. This list can include any or all of the three stages: `replicated`, `factom`, and `anchored`. For example, when you would like to trigger the callback from Connect at `replicated` and `factom` stage, you would send them in the format: [‘replicated’, ‘factom’]. </br> **Note:** For this field to matter, the URL must be provided. If callbacks are activated (URL has been specified) and this field is not sent, it will default to `factom` and `anchored`. | **callback_stages must be an array.** </br> An invalid `callback_stages` format was provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `app_id`            | optional | string</br>  This is the override parameter that allows user to specify a different API Application ID (which you can see by clicking on any of the applications in the application list that you see upon logging into  https://account.factom.com).               |
| `app_key`           | optional | string </br> This is the override parameter that allows user to specify a different API Application Key (which you can see by clicking on any of the applications in the application list that you see upon logging into  https://account.factom.com).              |
| `base_url`          | optional | string </br> This is the override parameter that allows user to specify a different API Base URL for your application (which you can see by clicking on any of the applications in the application list the you see upon logging into  https://account.factom.com). |
| `automatic_signing` | optional | boolean</br>  Setting this property to false allows user to create an unsigned entry, or implement their own way of signing the entry (it is set to  true by default in the SDK class that gets instantiated).                                                      |

**Returns**

**Response:** Accepted

-   **chain_id:** string </br> This is the unique identifier created for each chain.  </br>**Note:** Chain ID is a hash based on the external IDs you choose. External IDs must be unique or else the chain creation will fail.
-   **entry_hash:** string </br> The SHA256 Hash of the first entry of this new chain.
-   **stage:** string </br> The immutability stage that this chain has reached.

```python
{
   'stage':'replicated',
   'entry_hash':'e76e92550fb49634f83bea791345c138e2f081da0053f0a2e19c03da98036a36',
   'chain_id':'4b9532c79d53ab22b85951b4a5853f81c2682132b3c810a95128c30401cd1e58'
}
```

### <a name="chains_list"></a>list

Gets all of the chains on Factom.

**Sample**
```python
factom_client.chains.list()
```

**Parameters**

| **Name**        | **Type** | **Description**                                                                                                                                                                                                                                                                                                                                                                                | **SDK Error Message & Description**             <img width=1300/>                                  |
|-----------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| `limit`  | optional | integer </br>  The number of items you would like to return back in each stage. The default value is 15.                                                                                                                                                                                                                                                                          | **limit must be an integer.**</br>   An invalid `limit` format was provided.  |
| `offset` | optional | integer </br>  The offset parameter allows you to select which item you would like to start from when a list is returned from Connect. For example, if you have already seen the first 15 items and you would like the next set, you would send an offset of 15. `offset=0` starts from the first item of the set and is the default position.   | **offset must be an integer.**  </br>  An invalid `offset` format was provided. |
| `stages` | optional | array of strings </br>  The immutability stages you want to restrict results to. You can choose any from `replicated`, `factom`, and `anchored`. The default value are these three stages: `replicated`, `factom`, and `anchored`. </br>  **Note**: If you would like to search among multiple stages, you would send them in the format: [‘replicated’, ‘factom’]. | **stages must be an array.**</br>  An invalid `stages` format was provided.   |
| `app_id`            | optional | string</br>  This is the override parameter that allows user to specify a different API Application ID (which you can see by clicking on any of the applications in the application list that you see upon logging into  https://account.factom.com).               |
| `app_key`           | optional | string </br> This is the override parameter that allows user to specify a different API Application Key (which you can see by clicking on any of the applications in the application list that you see upon logging into  https://account.factom.com).              |
| `base_url`          | optional | string </br> This is the override parameter that allows user to specify a different API Base URL for your application (which you can see by clicking on any of the applications in the application list the you see upon logging into  https://account.factom.com). |

**Returns**

**Response:** OK
-   **data:** array of objects </br> An array that contains the chains on this page.
    -   **data[].chain_id:** string </br> The ID for this chain on the Factom blockchain.
    -   **data[].external_ids:** array of strings </br> The external IDs attached to this chain on the Factom blockchain.
    -   **data[].href:** string </br> An API link to retrieve all information about this chain.
    -   **data[].stage:** string </br> The immutability stage that this chain has reached.
    -   **data[].created_at:** string </br> The time when the chain was created. Sent in [ISO 8601 Format](https://en.wikipedia.org/wiki/ISO_8601). For example: `YYYY-MM-DDThh:mm:ss.ssssssZ`. This will be null if the chain is not at least at the `factom` immutability stage.
-   **offset:** integer </br> The index of the first chain returned from the total set, which starts from 0.
-   **limit:** integer </br> The number of chains returned.
-   **count:** integer </br> The total number of chains seen.

```python
{
   'offset':0,
   'limit':1,
   'data':[
      {
         'stage':'replicated',
         'href':'/v1/chains/e8ac011c4b0f6a5539e835811da7404442fcbbe6c26ce5feaa8b702dbd99209e',
         'external_ids':[
            'SignedChain',
            '0x01',
            '7cdd5333033b4bb6a6c73b4b239257516793b3b83ea6c698d9b9db9764717704',
            'idpub2174LhCanGnM6dHiin6hkzVD7x2M18ChiQShJAohMc9yzP79R9',
	    'c12700993e2764ed3786f910a6d7038326a628966b5ea861b4522a76257c362b8bbdfd1a73f239a7aaa20737b579d60f1905879fff1e7b7f2edcc5e73c6bd601',
            '2019-03-15T03:51:57.383862',
            'NotarySimulation',
            'CustomerChain',
            'cust123'
         ],
         'created_at':None,
         'chain_id':'e8ac011c4b0f6a5539e835811da7404442fcbbe6c26ce5feaa8b702dbd99209e'
      }
   ],
   'count':1298
}
```

### <a name="chains_search"></a>search

Finds all of the chains with `external_ids` that match what you entered.

**Sample**
```python
factom_client.chains.search(["TestFunction", "CustomerChain", "cust123"])
```

**Parameters**

| **Name**             | **Type** | **Description**                                                                                                                                                                                                                                                                                                                                                                            | **SDK Error Message & Description**          <img width=1300/>                                                                                                                                                 |
|----------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `external_ids` | required | array of strings </br>  A list of external IDs associated with the chains user would like to search by.                                                                                                                                                                                                                                                                              | **at least 1 external_ids is required.**</br>  `external_ids` parameter was not provided.</br>   **external_ids must be an array.** </br>  An invalid `external_ids` format was provided. |
| `limit`       | optional | integer </br> The number of items you would like to return back in each stage. The default value is 15.                                                                                                                                                                                                                                                                             | **limit must be an integer.** </br> An invalid `limit` format was provided.                                                                                                          |
| `offset`      | optional | integer </br>  The offset parameter allows you to select which item you would like to start from when a list is returned from Connect. For example, if you have already seen the first 15 items and you would like the next set, you would send an offset of 15. `offset=0` starts from the first item of the set and is the default position. | **offset must be an integer.**</br>  An invalid `offset` format was provided.                                                                                                       |
| `app_id`            | optional | string</br>  This is the override parameter that allows user to specify a different API Application ID (which you can see by clicking on any of the applications in the application list that you see upon logging into  https://account.factom.com).               |
| `app_key`           | optional | string </br> This is the override parameter that allows user to specify a different API Application Key (which you can see by clicking on any of the applications in the application list that you see upon logging into  https://account.factom.com).              |
| `base_url`          | optional | string </br> This is the override parameter that allows user to specify a different API Base URL for your application (which you can see by clicking on any of the applications in the application list the you see upon logging into  https://account.factom.com). |

**Returns**

**Response:** OK
-   **data:** array of objects </br> An array that contains the chains on this page.
    -   **data[].chain_id:** string </br> The ID for this chain on the Factom blockchain.
    -   **data[].external_ids:** array of strings </br> The external IDs attached to this chain on the Factom blockchain.
    -   **data[].href:** string </br> An API link to retrieve all information about this chain.
    -   **data[].stage:** string </br> The level of immutability that this chain has reached.
    -   **data[].created_at:** string </br> The time at which this chain was created. Sent in [ISO 8601 Format](https://en.wikipedia.org/wiki/ISO_8601). For example: `YYYY-MM-DDThh:mm:ss.ssssssZ`. This will be null if the chain is not at least at the `factom` immutability stage.
-   **offset:** integer </br> The index of the first chain returned from the total set, which starts from 0.
-   **limit:** integer </br> The number of chains returned.
-   **count:** integer </br> The total number of chains seen.

```python
{
   'offset':0,
   'limit':1,
   'data':[
      {
         'stage':'factom',
         'href':'/v1/chains/75f40155d87c1da402c4e9e8e0ee6b8915aa5db98e32e6f4d1649ca495e7f225',
         'external_ids':[
            'SignedChain',
            '0x01',
            '33f4a13b69c91b0f6a13e940bcd83831cb1fefd4a26a956e1ec456b02d553fa3',
            'idpub2qSXVg7Tw2o3FUu7vz6j96FrS3BTVjvhM4mMLoAvmyK5t2VDXG',
            '9aae05eb4c164f416fa1f2b7911c0a278dd9f10b5714781e4b14c579c70041fb937dfdc039c9f9b9a04d075915312c66c54a0e3ebecc5bd726ed14b12a4dc708',
            '2019-03-04T04:29:54.222Z',
            'TestFunction',
            'CustomerChain',
            'cust123'
         ],
         'created_at':'2019-03-04T04:30:00.000000Z',
         'chain_id':'75f40155d87c1da402c4e9e8e0ee6b8915aa5db98e32e6f4d1649ca495e7f225'
      }
   ],
   'count':19
}
```

### <a name="chains_entries"></a>entries

##### <a name="entries_get"></a>get

Gets information about a specific entry on Connect.

**Sample**
```python
factom_client.chains.entries.get('c15f9e51781a8a4c520c15fd135e761b922b709217ebea974537e8689c74d0c2',
				 'cccf02ac98c9e04f556508aa4dc9e277d44e8ce2006a244ebec082e0bed36efc')
```

**Parameters**

| **Name**                     | **Type** | **Description**                                                                                                                                                                                                                                                                                                        | **SDK Error Message & Description**    <img width=400/>                                           |
|------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| `chain_id`             | required | string </br>  The chain identifier.                                                                                                                                                                                                                                                                                    | **chain_id is required.**</br>  `chain_id` parameter was not provided.   |
| `entry_hash`           | required | string </br> The SHA256 hash of the entry.                                                                                                                                                                                                                                                                             | **entry_hash is required.** </br> `entry_hash` parameter was not provided. |
| `signature_validation` | optional | boolean (`True`/`False`/`custom function`) </br>  The default value is `True`. Indicates whether the SDK automatically validates that the entry was signed based on our signing standard. </br> `custom function`: allows for validating the entry's signature based on custom logic.|                                                                                |
| `app_id`            | optional | string</br>  This is the override parameter that allows user to specify a different API Application ID (which you can see by clicking on any of the applications in the application list that you see upon logging into  https://account.factom.com).               |
| `app_key`           | optional | string </br> This is the override parameter that allows user to specify a different API Application Key (which you can see by clicking on any of the applications in the application list that you see upon logging into  https://account.factom.com).              |
| `base_url`          | optional | string </br> This is the override parameter that allows user to specify a different API Base URL for your application (which you can see by clicking on any of the applications in the application list the you see upon logging into  https://account.factom.com). |

**Returns**

**Response:** OK
-   **data:** object
    -   **data.entry_hash:** string </br> The SHA256 Hash of this entry.
    -   **data.chain:** object </br> An object that contains the Chain Hash (ID) as well as a URL for the chain.
        -   **data.chain.chain_id:** string </br> The ID for this chain on the Factom blockchain.
        -   **data.chain.href:** string </br> An API link to retrieve all information about this chain.
    -   **data.created_at:** string </br> The time when this entry was created. Sent in [ISO 8601 Format](https://en.wikipedia.org/wiki/ISO_8601). For example: `YYYY-MM-DDThh:mm:ssssssZ`.
    -   **data.external_ids:** array of strings </br> Tags that can be used to identify your entry. You can search for records that contain a particular external ID using Connect.</br> **Note**: Since the Connect API Base64 encodes these values for transport, each array element will be decoded for you by the SDK.
    -   **data.content:** string </br> This is the data that is stored by the entry.</br>  **Note**: Since the Connect API Base64 encodes these values for transport, `content` will be decoded for you by the SDK.
    -   **data.stage:** string </br> The level of immutability that this entry has reached.
    -   **data.dblock:** object </br> Represents the Directory Block that relates to this entry. This will be null if the chain is not at least at the `factom` immutability stage.
		-   **data.dblock.keymr:** string </br> The Key Merkle Root for this directory block.
		-   **data.dblock.height:** integer </br> The Factom blockchain height of this directory block.
		-   **data.dblock.href:** string </br> An API link to retrieve all information about this directory block.
	-   **data.eblock:** object </br> Represents the Entry Block that contains the entry. This will be null if the entry is not at least at the `factom` immutability stage.
		- **data.eblock.keymr:** string</br> The Key Merkle Root for this entry block.
		- **data.eblock.href:** string</br> An API link to retrieve all information about this entry block.
-   **status:** string </br> The result of signature validation.</br>
Displays an empty string ("") when `signature_validation` is set to `False`.</br>
Or displays a function's result when `signature_validation` is set to `custom function`.</br>
In case `signature_validation` is set to `True` then one of the following values will be returned based on an automatic comparison of the expected SignedEntry structure outlined in our signing standard.
    - **not_signed/invalid_entry_format:** An entry that was not signed or did not conform to the SignedEntry structure.
    - **invalid_signature:** An entry was created in the proper SignedEntry structure, but the signature does not match the attached key.
    - **retired_height:** An entry that conformed to the SignedEntry structure and the signature was verified with the listed key, but that key was retired for the signer identity at a height lower than when this entry reached the `factom` immutability stage.
    -   **key_not_found:** An entry that conformed to the SignedEntry structure but the signer public key does not belong to the signer identity chain.
    - **valid_signature:** An entry that conformed to the SignedEntry structure and the signature was verified with the listed key. That key was also active for the signer identity at the height when this entry reached the `factom` immutability stage.

```python
{
   'entry':{
      'data':{
         'stage':'replicated',
         'external_ids':[
            'SignedEntry',
            '0x01',
            '8c33e7432cdfd3933beb6de5ccbc3706ac21458ed53352e02658daf2dce8f27c',
            'idpub3D92p9aiSFo6ad4UbkvcPDE7cFcGqQky2yMk1gjKCfWwh9zfpq',
            '116ef1cdcbb6b047729dd5cba77aeb2ef61a764af847a2c85c6aee531545aa678ef220ec35e36d13ee9b82779bef1106d5fb7f97b1640a6991cc645c67d6ee0e',
            '2019-03-15T03:58:31.259724',
            'NotarySimulation',
            'DocumentEntry',
            'doc987'
         ],
         'entry_hash':'cccf02ac98c9e04f556508aa4dc9e277d44e8ce2006a244ebec082e0bed36efc',
         'eblock':None,
         'dblock':None,
         'created_at':None,
         'content':'{"document_hash": "98e8447527dd18fd054ff76371d4885972887481b1499dad02ac3c39748a4012", "hash_type": "sha256"}',
         'chain':{
            'href':'/v1/chains/c15f9e51781a8a4c520c15fd135e761b922b709217ebea974537e8689c74d0c2',
            'chain_id':'c15f9e51781a8a4c520c15fd135e761b922b709217ebea974537e8689c74d0c2'
         }
      }
   },
   'status':'valid_signature'
}
```
##### <a name="entries_create"></a>create

Creates a new entry for the selected chain with or without signature:

-   When the Factom SDK is initialized, if `automatic_signing` = `True`; in order to create a signed entry, you need to pass:
    -   `signer_chain_id`
    -   `signer_private_key`
-   When the Factom SDK is initialized, if `automatic_signing` =
    `False`, SDK creates an unsigned entry and therefore it does
    not require these parameters.

**Sample**
```python
factom_client.chains.entries.create(chain_id='c15f9e51781a8a4c520c15fd135e761b922b709217ebea974537e8689c74d0c2',
                                    signer_private_key='idsec1xbKD6tkgLPMBuNQbTnHPr6mFoeF7iQV4ybTN63sKdFg7h1uWH',
                                    signer_chain_id='8c33e7432cdfd3933beb6de5ccbc3706ac21458ed53352e02658daf2dce8f27c',
                                    external_ids=["NotarySimulation","DocumentEntry","doc987"],
                                    content='Abc123')
```

**Parameters**

| **Name**                  | **Type**                         | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | **SDK Error Message & Description**     <img width=1500/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `chain_id`          | required                         | string </br>  The chain identifier.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **chain_id is required.**</br>  `chain_id` parameter was not provided.</br>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `external_ids`      | required</br>  or</br>  optional | array of strings </br> Tags that can be used to identify your entry. You can search for records that contain a particular external ID using Connect.</br>  **Note:** Since the Connect API requires each array element to be Base64 encoded, the SDK will do so before making the API request. This parameter is only required for creating an unsigned entry (`automatic_signing` is set to `False`).                                                                                                                                                       | **at least 1 external_id is required.**</br> `external_ids` parameter was not provided when `automatic_signing` is set to `False`.</br></br>  **external_ids must be an array.**</br>  An invalid `external_ids` format was provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `content`          | required                         | string</br> This is the data that will be stored directly on the blockchain. Please be sure that no private information is entered here.</br> **Note:** The value in `content` parameter will be encoded in Base64 format by Connect SDK.                                                                                                                                                                                                                                                                                                                                                        | **content is required.**</br> `content` parameter was not provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `signer_chain_id`    | required</br> or</br> optional   | string</br> The chain ID of the signer identity.</br>  **Note:** This parameter is optional for creating an unsigned entry. However, if `signer_private_key` is inputted then `signer_chain_id` must also be inputted.                                                                                                                                                                                                                                                                                                                                                                                       | In case of creating a signed entry:</br> **signer_chain_id is required.**</br> `signer_chain_id` parameter was not provided.</br></br>  In case of creating an unsigned entry:</br>  **signer_chain_id is required when passing a signer_private_key.**</br> `signer_private_key` was provided but lacking `signer_chain_id` parameter.                                                                                                                                                                                                                                                                                                                                                                                                   |
| `signer_private_key` | required</br>  or</br>  optional | a base58 string in Idsec format</br> The private key signer would like to sign with. In fact, private key is used to generate the public key, which is included as an external ID on the created signed entry.</br>   **Note:** This parameter is optional for creating an unsigned entry. However, if `signer_chain_id` is inputted then `signer_private_key` must also be inputted.                                                                                                                                                                                               | In case of creating a signed entry:</br> **signer_private_key is required.**</br> `signer_private_key` parameter was not provided.</br></br>  **signer_private_key is invalid.**</br> An invalid `signer_private_key` parameter was provided or key's byte length is not equal to 41. </br></br>  In case of creating an unsigned entry:</br>  **signer_private_key is required when passing a signer_chain_id.**</br> `signer_chain_id` was provided but lacking `signer_private_key` parameter.</br></br>  **signer_private_key is invalid.**</br>  `signer_chain_id` was provided but an invalid `signer_private_key` parameter was provided or key's byte length is not equal to 41.  |
| `callback_url`      | optional                         | string</br> the URL you would like the callbacks to be sent to </br> **Note:** If this is not specified, callbacks will not be activated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | **callback_url is an invalid url format.**</br> An invalid `callback_url` format was provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `callback_stages`   | optional                         | array of strings</br>  The immutability stages you would like to be notified about. This list can include any or all of these three stages: `replicated`, `factom`, and `anchored`. For example, when you would like to trigger the callback from Connect from `replicated` and `factom` then you would send them in the format: ['replicated', 'factom'].</br> **Note:** For this field to matter, the URL must be provided. If callbacks are activated (URL has been specified) and this field is not sent, it will default to `factom` and `anchored`. | **callback_stages must be an array.**</br> An invalid `callback_stages` format was provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `app_id`            | optional | string</br>  This is the override parameter that allows user to specify a different API Application ID (which you can see by clicking on any of the applications in the application list that you see upon logging into  https://account.factom.com).               |
| `app_key`           | optional | string </br> This is the override parameter that allows user to specify a different API Application Key (which you can see by clicking on any of the applications in the application list that you see upon logging into  https://account.factom.com).              |
| `base_url`          | optional | string </br> This is the override parameter that allows user to specify a different API Base URL for your application (which you can see by clicking on any of the applications in the application list the you see upon logging into  https://account.factom.com). |
| `automatic_signing` | optional | boolean</br>  Setting this property to false allows user to create an unsigned entry, or implement their own way of signing the entry (it is set to  true by default in the SDK class that gets instantiated).                                                      |

**Returns**

**Response:** Accepted
-   **entry_hash** string </br>
    The SHA256 Hash of the entry you just created. You can use this hash
    to reference this entry in the future.
-   **stage:** string </br> The current immutability stage of the new entry.

```python
{
   'stage':'replicated',
   'entry_hash':'cccf02ac98c9e04f556508aa4dc9e277d44e8ce2006a244ebec082e0bed36efc'
}
```

##### <a name="entries_list"></a>list

Gets list of all entries contained on a specified chain.

**Sample**
```python
factom_client.chains.entries.list('c15f9e51781a8a4c520c15fd135e761b922b709217ebea974537e8689c74d0c2')
```

**Parameters**

| **Name**         | **Type** | **Description**                                                                                                                                                                                                                                                                                                                                                                            | **SDK Error Message & Description**  <img width=1300/>                                                     |
|------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| `chain_id` | required | string </br>  The chain identifier.                                                                                                                                                                                                                                                                                                                                                        | **chain_id is required.**</br>  `chain_id` parameter was not provided.</br>              |
| `limit`   | optional | integer </br> The number of items you would like back in each page. The default value is 15.                                                                                                                                                                                                                                                                                        | **limit must ben an integer.**</br> An invalid `limit` format was provided.</br>  |
| `offset`  | optional | integer</br> The offset parameter allows you to select which item you would like to start from when a list is returned from Connect. For example, if you have already seen the first 15 items and you would like the next set, you would send an offset of 15. `offset=0` starts from the first item of the set and is the default position. | **offset must be an integer.**</br> An invalid `offset` format was provided.|
| `stages`  | optional | array of strings</br> The immutability stages you want to restrict results to. You can choose any from `replicated`, `factom`, and `anchored`. The default value are these three stages: `replicated`, `factom` and `anchored`.</br>  **Note:** If you would like to search among multiple stages, you would send them in the format ['replicated', 'factom'].  | **stages must be an array.**</br>  An invalid `stages` format was provided. |
| `app_id`            | optional | string</br>  This is the override parameter that allows user to specify a different API Application ID (which you can see by clicking on any of the applications in the application list that you see upon logging into  https://account.factom.com).               |
| `app_key`           | optional | string </br> This is the override parameter that allows user to specify a different API Application Key (which you can see by clicking on any of the applications in the application list that you see upon logging into  https://account.factom.com).              |
| `base_url`          | optional | string </br> This is the override parameter that allows user to specify a different API Base URL for your application (which you can see by clicking on any of the applications in the application list the you see upon logging into  https://account.factom.com). |

**Returns**

**Response:** OK

-   **data:** array of objects </br> An array that contains the entries on this page.
    -   **data[].entry_hash:** string </br> The SHA256 Hash of this entry.
    -   **data[].chain:** object </br> An object that contains the Chain Hash (ID) as well as a URL for the chain.
        -   **data[].chain.chain_id:** string </br> The ID for this chain on the Factom blockchain.
        -   **data[].chain.href:** string </br> An API link to retrieve all information about this chain.
    -   **data[].created_at:** string </br> The time at which this entry was created. Sent in [ISO 8601 Format](https://en.wikipedia.org/wiki/ISO_8601). For example: `YYYY-MM-DDThh:mm:ssssssZ`.
    -   **data[].href:** string </br>  An API link to retrieve all information about this entry.
-   **offset:** integer </br> The index of the first entry returned from the total set starting from 0.
-   **limit:** integer </br> The number of entries returned per page.
-   **count:** integer </br> The total number of entries seen.

```python
{
   'offset':0,
   'limit':15,
   'data':[
      {
         'stage':'replicated',
         'href':'/v1/chains/c15f9e51781a8a4c520c15fd135e761b922b709217ebea974537e8689c74d0c2/entries/bcf9ce3beba20007408319a3965a6dde2ad23eb45a20f0d61827b8dc3c584ced',
         'entry_hash':'bcf9ce3beba20007408319a3965a6dde2
ad23eb45a20f0d61827b8dc3c584ced',
         'created_at':None,
         'chain':{
            'href':'/v1/chains/c15f9e51781a8a4c520c15fd135e761b922b709217ebea974537e8689c74d0c2',
            'chain_id':'c15f9e51781a8a4c520c15fd135e761b922b709217ebea974537e8689c74d0c2'
         }
      },
      {
         'stage':'replicated',
         'href':'/v1/chains/c15f9e51781a8a4c520c15fd135e761b922b709217ebea974537e8689c74d0c2/entries/cccf02ac98c9e04f556508aa4dc9e277d44e8ce2006a244ebec082e0bed36efc',
         'entry_hash':'cccf02ac98c9e04f556508aa4dc9e277d44e8ce2006a244ebec082e0bed36efc',
         'created_at':None,
         'chain':{
            'href':'/v1/chains/c15f9e51781a8a4c520c15fd135e761b922b709217ebea974537e8689c74d0c2',
            'chain_id':'c15f9e51781a8a4c520c15fd135e761b922b709217ebea974537e8689c74d0c2'
         }
      }
   ],
   'count':2
}
```

##### <a name="entries_first"></a>get_first

Retrieves the first entry that has been saved to this chain.

**Sample**
```python
factom_client.chains.entries.get_first('c15f9e51781a8a4c520c15fd135e761b922b709217ebea974537e8689c74d0c2')
```

**Parameters**

| **Name**                     | **Type** | **Description**                                                                                                                                                                                                                                                                                                   | **SDK Error Message & Description**      <img width=400/>                                    |
|------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| `chain_id`             | required | string </br>  The chain identifier.                                                                                                                                                                                                                                                                               | **chain_id is required.**</br>  `chain_id` parameter was not provided.</br> |
| `signature_validation` | optional | boolean (`True`/`False`/`custom function`)</br> Default value is `True`.</br>  Indicates whether the SDK automatically validates that the entry was signed based on our signing standard.</br>   `custom function`: allows for validating the entry's signature based on custom logic. |
| `app_id`            | optional | string</br>  This is the override parameter that allows user to specify a different API Application ID (which you can see by clicking on any of the applications in the application list that you see upon logging into  https://account.factom.com).               |
| `app_key`           | optional | string </br> This is the override parameter that allows user to specify a different API Application Key (which you can see by clicking on any of the applications in the application list that you see upon logging into  https://account.factom.com).              |
| `base_url`          | optional | string </br> This is the override parameter that allows user to specify a different API Base URL for your application (which you can see by clicking on any of the applications in the application list the you see upon logging into  https://account.factom.com). |

**Returns**

**Response:** OK

-   **data:** object
    -   **data.entry_hash:** string </br> The SHA256 Hash of this entry.
    -   **data.chain:** object </br> An object that contains the Chain Hash (ID) as well as a URL for the chain.
        -   **data.chain.chain_id:** string </br> The ID for this chain on the Factom blockchain.
        -   **data.chain.href:**: string </br> An API link to retrieve all information about this chain.
    -   **data.created_at:** string </br> The time at which this entry was created. Sent in [ISO 8601 Format](https://en.wikipedia.org/wiki/ISO_8601). For example: `YYYY-MM-DDThh:mm:ssssssZ`.
    -   **data.external_ids:** array of strings </br> Tags that can be used to identify your entry. You can search for records that contain a particular external ID using Connect. </br> **Note:** Since the Connect API Base64 encodes these values for transport, each array element will be decoded for you by the SDK.
    -   **data.content:** string </br> This is the data that is stored by the entry. </br> **Note:** Since the Connect API Base64 encodes these values for transport, `content` will be decoded for you by the SDK.
    -   **data.stage:** string </br> The level of immutability that this entry has reached.
    -   **data.dblock:** object </br> Represents the Directory Block that relates to this entry. This will be null if the chain is not at least at the `factom` immutability stage.
		-   **data.dblock.keymr:** string </br> The Key Merkle Root for this directory block.
		-   **data.dblock.height:** integer </br> The Factom blockchain height of this directory block.
		-   **data.dblock.href: :** string </br> An API link to retrieve all information about this directory block.
	-   **data.eblock**: object </br> Represents the Entry Block that contains the entry. This will be null if the entry is not at least at the `factom` immutability stage.
		-   **data.eblock.keymr:** string </br> The Key Merkle Root for this entry block.
		-   **data.eblock.href**: string </br> An API link to retrieve all information about this entry block.
-   **status:** string </br> The result of signature validation.</br>
Displays an empty string ("") when `signature_validation` is set to `False`.</br>
Or displays a function's result when `signature_validation` is set to `custom function`.</br>
In case `signature_validation` is set to `True` then one of the following values will be returned based on an automatic comparison of the expected SignedEntry structure outlined in our signing standard.
    - **not_signed/invalid_entry_format:** An entry that was not signed or did not conform to the SignedEntry structure.
    - **invalid_signature:** An entry was created in the proper SignedEntry structure, but the signature does not match the attached key.
    - **retired_height:** An entry that conformed to the SignedEntry structure and the signature was verified with the listed key, but that key was retired for the signer identity at a height lower than when this entry reached the `factom` immutability stage.
    -   **key_not_found:** An entry that conformed to the SignedEntry structure but the signer public key does not belong to the signer identity chain.
    - **valid_signature:** An entry that conformed to the SignedEntry structure and the signature was verified with the listed key. That key was also active for the signer identity at the height when this entry reached the `factom` immutability stage.

```python
{
   'entry':{
      'data':{
         'stage':'replicated',
         'external_ids':[
            'SignedChain',
            '0x01',
            '8c33e7432cdfd3933beb6de5ccbc3706ac21458ed53352e02658daf2dce8f27c',
            'idpub3D92p9aiSFo6ad4UbkvcPDE7cFcGqQky2yMk1gjKCfWwh9zfpq',
            '54d5c4771f70bc197a8f6a347ce3a921425e3db4957918cc7bc305d694d59566989bf0be29843e805cc958ad0eed81b9a766c7b54602f474cc503c908729010d',
            '2019-03-15T03:58:28.544972',
            'NotarySimulation',
            'CustomerChain',
            'cust123'
         ],
         'entry_hash':'bcf9ce3beba20007408319a3965a6dde2ad23eb45a20f0d61827b8dc3c584ced',
         'eblock':None,
         'dblock':None,
         '
created_at':None,
         'content':"This chain represents a notary service's customer in the NotarySimulation, a sample implementation provided as part of the Factom Harmony SDKs. Learn more here: https://docs.harmony.factom.com/docs/sdks-clients",
         'chain':{
            'href':'/v1/chains/c15f9e51781a8a4c520c15fd135e761b922b709217ebea974537e8689c74d0c2',
            'chain_id':'c15f9e51781a8a4c520c15fd135e761b922b709217ebea974537e8689c74d0c2'
         }
      }
   },
   'status':'not_signed/invalid_entry_format'
}
```

##### <a name="entries_last"></a>get_last

Gets the last entry that has been saved to this chain.

**Sample**
```python
factom_client.chains.entries.get_last('c15f9e51781a8a4c520c15fd135e761b922b709217ebea974537e8689c74d0c2')
```

**Parameters**

| **Name**                     | **Type** | **Description**                                                                                                                                                                                                                                                                                                   | **SDK Error Message & Description**                 <img width=400/>                         |
|------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| `chain_id`             | required | string </br>  The chain identifier.                                                                                                                                                                                                                                                                               | **chain_id is required.**</br>  `chain_id` parameter was not provided.</br> |
| `signature_validation` | optional | boolean (`True`/`False`/`custom function`)</br> Default value is `True`.</br> Indicates whether the SDK automatically validates that the entry was signed based on our signing standard.</br> `custom function`: allows for validating the entry's signature based on custom logic. |                                                                           |
| `app_id`            | optional | string</br>  This is the override parameter that allows user to specify a different API Application ID (which you can see by clicking on any of the applications in the application list that you see upon logging into  https://account.factom.com).               |
| `app_key`           | optional | string </br> This is the override parameter that allows user to specify a different API Application Key (which you can see by clicking on any of the applications in the application list that you see upon logging into  https://account.factom.com).              |
| `base_url`          | optional | string </br> This is the override parameter that allows user to specify a different API Base URL for your application (which you can see by clicking on any of the applications in the application list the you see upon logging into  https://account.factom.com). |

**Returns**

**Response:** OK

-   **data:** object
    -   **data.entry_hash:** string </br> The SHA256 Hash of this entry.
    -   **data.chain:** object </br> An object that contains the Chain Hash (ID) as well as a URL for the chain.
        -   **data.chain.chain_id:** string </br> The ID for this chain on the Factom blockchain.
        -   **data.chain.href:**: string </br> An API link to retrieve all information about this chain.
    -   **data.created_at:** string </br> The time at which this entry was created. Sent in [ISO 8601 Format](https://en.wikipedia.org/wiki/ISO_8601). For example: `YYYY-MM-DDThh:mm:ssssssZ`.
    -   **data.external_ids:** array of strings </br> Tags that can be used to identify your entry. You can search for records that contain a particular external ID using Connect. </br> **Note:** Since the Connect API Base64 encodes these values for transport, each array element will be decoded for you by the SDK.
    -   **data.content:** string </br> This is the data that is stored by the entry. </br> **Note:** Since the Connect API Base64 encodes these values for transport, `content` will be decoded for you by the SDK.
    -   **data.stage:** string </br> The level of immutability that this entry has reached.
    -   **data.dblock:** object </br> Represents the Directory Block that relates to this entry. This will be null if the chain is not at least at the `factom` immutability stage.
		-   **data.dblock.keymr:** string </br> The Key Merkle Root for this directory block.
		-   **data.dblock.height:** integer </br> The Factom blockchain height of this directory block.
		-   **data.dblock.href: :** string </br> An API link to retrieve all information about this directory block.
	-   **data.eblock**: object </br> Represents the Entry Block that contains the entry. This will be null if the entry is not at least at the `factom` immutability stage.
		-   **data.eblock.keymr:** string </br> The Key Merkle Root for this entry block.
		-   **data.eblock.href**: string </br> An API link to retrieve all information about this entry block.
-   **status:** string </br> The result of signature validation.</br>
Displays an empty string ("") when `signature_validation` is set to `False`.</br>
Or displays a function's result when `signature_validation` is set to `custom function`.</br>
In case `signature_validation` is set to `True` then one of the following values will be returned based on an automatic comparison of the expected SignedEntry structure outlined in our signing standard.
    - **not_signed/invalid_entry_format:** An entry that was not signed or did not conform to the SignedEntry structure.
    - **invalid_signature:** An entry was created in the proper SignedEntry structure, but the signature does not match the attached key.
    - **retired_height:** An entry that conformed to the SignedEntry structure and the signature was verified with the listed key, but that key was retired for the signer identity at a height lower than when this entry reached the `factom` immutability stage.
    -   **key_not_found:** An entry that conformed to the SignedEntry structure but the signer public key does not belong to the signer identity chain.
    - **valid_signature:** An entry that conformed to the SignedEntry structure and the signature was verified with the listed key. That key was also active for the signer identity at the height when this entry reached the `factom` immutability stage.

```python
{
   'entry':{
      'data':{
         'stage':'replicated',
         'external_ids':[
            'SignedChain',
            '0x01',
            '8c33e7432cdfd3933beb6de5ccbc3706ac21458ed53352e02658daf2dce8f27c',
            'idpub3D92p9aiSFo6ad4UbkvcPDE7cFcGqQky2yMk1gjKCfWwh9zfpq',
            '54d5c4771f70bc197a8f6a347ce3a921425e3db4957918cc7bc305d694d59566989bf0be29843e805cc958ad0eed81b9a766c7b54602f474cc503c908729010d',
            '2019-03-15T03:58:28.544972',
            'NotarySimulation',
            'CustomerChain',
            'cust123'
         ],
         'entry_hash':'bcf9ce3beba20007408319a3965a6dde2ad23eb45a20f0d61827b8dc3c584ced',
         'eblock':None,
         'dblock':None,
         'created_at':None,
         'content':"This chain represents a notary service's customer in the NotarySimulation, a sample implementation provided as part of the Factom Harmony SDKs. Learn more here: https://docs.harmony.factom.com/docs/sdks-clients",
         'chain':{
            'href':'/v1/chains/c15f9e51781a8a4c520c15fd135e761b922b709217ebea974537e8689c74d0c2',
            'chain_id':'c15f9e51781a8a4c520c15fd135e761b922b709217ebea974537e8689c74d0c2'
         }
      }
   },
   'status':'not_signed/invalid_entry_format'
}
```
##### <a name="entries_search"></a>search

Finds all of the entries with `external_ids` that match what you entered.

**Sample**
```python
factom_client.chains.entries.search('c15f9e51781a8a4c520c15fd135e761b922b709217ebea974537e8689c74d0c2',
				    ["NotarySimulation","DocumentEntry","doc987"])
```

**Parameters**

| **Name**             | **Type** | **Description**                                                                                                                                                                                                                                                                                                                                                                            | **SDK Error Message & Description**    <img width=1300/>                                                                                                                                                |
|----------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `chain_id`     | required | string </br>  The chain identifier.                                                                                                                                                                                                                                                                                                                                                        | **chain_id is required.**</br>  `chain_id` parameter was not provided.</br>                                                                                                           |
| `external_ids` | required | array of strings</br> A list of external IDs.</br> **Note:** Since the Connect API requires each array element to be Base64 encoded, the SDK will do so before making the API request.                                                                                                                                                                                   | **at least 1 external_id is required.**</br> `external_ids` parameter was not provided. </br>  **external_ids must be an array.**</br> An invalid `external_ids`parameter was provided. |
| `limit`       | optional | integer</br> The number of items you would like to return back in each page. The default value is  15.                                                                                                                                                                                                                                                                              | **limit must be an integer.**</br> An invalid `limit` format was provided.</br>                                                                                                      |
| `offset`      | optional | integer</br> The offset parameter allows you to select which item you would like to start from when a list is returned from Connect. For example, if you have already seen the first 15 items and you would like the next set, you would send an offset of 15. `offset=0` starts from the first item of the set and is the default position. | **offset must be an integer.**</br> An invalid `offset` format was provided.                                                                                              |
| `app_id`            | optional | string</br>  This is the override parameter that allows user to specify a different API Application ID (which you can see by clicking on any of the applications in the application list that you see upon logging into  https://account.factom.com).               |
| `app_key`           | optional | string </br> This is the override parameter that allows user to specify a different API Application Key (which you can see by clicking on any of the applications in the application list that you see upon logging into  https://account.factom.com).              |
| `base_url`          | optional | string </br> This is the override parameter that allows user to specify a different API Base URL for your application (which you can see by clicking on any of the applications in the application list the you see upon logging into  https://account.factom.com). |

**Returns**

**Response:** OK

-   **data:** array of objects
	-   **data[].entry_hash:** string </br> The SHA256 Hash of this entry.
    -   **data[].external_ids:** array of strings </br> Tags that can be used to identify your entry.</br> **Note:** Since the Connect API Base64 encodes these values for transport, each array element will be decoded for you by the SDK.
    -   **data[].stage:** string </br> The level of immutability that this entry has reached.
    -   **data[].href:** string </br> An API link to retrieve all information about this entry.
-   **offset:** integer </br> The index of the first item returned from the total set, which starts from 0.
-   **limit:** integer </br> The number of entries returned per page.
-   **count:** integer </br> The total number of entries seen.

```python
{
   'offset':0,
   'limit':15,
   'data':[
      {
         'stage':'replicated',
         'href':'/v1/chains/c15f9e51781a8a4c520c15fd135e761b922b709217ebea974537e8689c74d0c2/entries/cccf02ac98c9e04f556508aa4dc9e277d44e8ce2006a244ebec082e0bed36efc',
         'external_ids':[
            'SignedEntry',
            '0x01',
            '8c33e7432cdfd3933beb6de5ccbc3706ac21458ed53352e02658daf2dce8f27c',
            'idpub3D92p9aiSFo6ad4UbkvcPDE7cFcGqQky2yMk1gjKCfWwh9zfpq',
            '116ef1cdcbb6b047729dd5cba77aeb2ef61a764af847a2c85c6aee531545aa678ef220ec35e36d13ee9b82779bef1106d5fb7f97b1640a6991cc645c67d6ee0e',
            '2019-03-15T03:58:31.259724',
            'NotarySimulation',
            'DocumentEntry',
            'doc987'
         ],
         'entry_hash':'cccf02ac98c9e04f556508aa4dc9e277d44e8ce2006a244ebec082e0bed36efc'
      }
   ],
   'count':1
}
```
