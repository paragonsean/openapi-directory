# CloudSpannerApi.KeySet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **Boolean** | For convenience &#x60;all&#x60; can be set to &#x60;true&#x60; to indicate that this &#x60;KeySet&#x60; matches all keys in the table or index. Note that any keys specified in &#x60;keys&#x60; or &#x60;ranges&#x60; are only yielded once. | [optional] 
**keys** | **[[Object]]** | A list of specific keys. Entries in &#x60;keys&#x60; should have exactly as many elements as there are columns in the primary or index key with which this &#x60;KeySet&#x60; is used. Individual key values are encoded as described here. | [optional] 
**ranges** | [**[KeyRange]**](KeyRange.md) | A list of key ranges. See KeyRange for more information about key range specifications. | [optional] 


