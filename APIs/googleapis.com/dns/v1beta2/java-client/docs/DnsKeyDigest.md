

# DnsKeyDigest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**digest** | **String** | The base-16 encoded bytes of this digest. Suitable for use in a DS resource record. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Specifies the algorithm used to calculate this digest. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SHA1 | &quot;sha1&quot; |
| SHA256 | &quot;sha256&quot; |
| SHA384 | &quot;sha384&quot; |



