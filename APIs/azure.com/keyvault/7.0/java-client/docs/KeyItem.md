

# KeyItem

The key item containing key metadata.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**KeyAttributes**](KeyAttributes.md) |  |  [optional] |
|**kid** | **String** | Key identifier. |  [optional] |
|**managed** | **Boolean** | True if the key&#39;s lifetime is managed by key vault. If this is a key backing a certificate, then managed will be true. |  [optional] [readonly] |
|**tags** | **Map&lt;String, String&gt;** | Application specific metadata in the form of key-value pairs. |  [optional] |



