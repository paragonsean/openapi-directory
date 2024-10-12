# CloudFirestoreApi.BitSequence

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bitmap** | **Blob** | The bytes that encode the bit sequence. May have a length of zero. | [optional] 
**padding** | **Number** | The number of bits of the last byte in &#x60;bitmap&#x60; to ignore as \&quot;padding\&quot;. If the length of &#x60;bitmap&#x60; is zero, then this value must be &#x60;0&#x60;. Otherwise, this value must be between 0 and 7, inclusive. | [optional] 


