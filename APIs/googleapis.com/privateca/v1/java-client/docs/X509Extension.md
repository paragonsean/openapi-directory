

# X509Extension

An X509Extension specifies an X.509 extension, which may be used in different parts of X.509 objects like certificates, CSRs, and CRLs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**critical** | **Boolean** | Optional. Indicates whether or not this extension is critical (i.e., if the client does not know how to handle this extension, the client should consider this to be an error). |  [optional] |
|**objectId** | [**ObjectId**](ObjectId.md) |  |  [optional] |
|**value** | **byte[]** | Required. The value of this X.509 extension. |  [optional] |



