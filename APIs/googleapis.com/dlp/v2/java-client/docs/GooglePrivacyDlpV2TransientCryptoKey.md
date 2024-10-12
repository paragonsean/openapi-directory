

# GooglePrivacyDlpV2TransientCryptoKey

Use this to have a random data crypto key generated. It will be discarded after the request finishes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Required. Name of the key. This is an arbitrary string used to differentiate different keys. A unique key is generated per name: two separate &#x60;TransientCryptoKey&#x60; protos share the same generated key if their names are the same. When the data crypto key is generated, this name is not used in any way (repeating the api call will result in a different key being generated). |  [optional] |



