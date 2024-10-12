# CloudTraceApi.TruncatableString

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**truncatedByteCount** | **Number** | The number of bytes removed from the original string. If this value is 0, then the string was not shortened. | [optional] 
**value** | **String** | The shortened string. For example, if the original string is 500 bytes long and the limit of the string is 128 bytes, then &#x60;value&#x60; contains the first 128 bytes of the 500-byte string. Truncation always happens on a UTF8 character boundary. If there are multi-byte characters in the string, then the length of the shortened string might be less than the size limit. | [optional] 


