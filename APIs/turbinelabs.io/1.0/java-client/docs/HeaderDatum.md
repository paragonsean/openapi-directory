

# HeaderDatum

This describes a HTTP header that should be attached to requests. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the header that will be attached to the response sent. This is case insensitive.  |  [optional] |
|**value** | **String** | A literal value to send as the header value or a reference to some metadatum value set on the Cluster Intsance that handles a specific request. If this value is empty after looking up an Instance metadatum value no header will be sent.  |  [optional] |
|**valueIsLiteral** | **Boolean** | If true then the value attribute is treated as a literal and no attempt to resolve instance metadatum to find a value.  |  [optional] |



