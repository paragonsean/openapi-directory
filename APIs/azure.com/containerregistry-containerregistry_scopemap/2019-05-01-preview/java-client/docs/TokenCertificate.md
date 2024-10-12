

# TokenCertificate

The properties of a certificate used for authenticating a token.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encodedPemCertificate** | **String** | Base 64 encoded string of the public certificate1 in PEM format that will be used for authenticating the token. |  [optional] |
|**expiry** | **OffsetDateTime** | The expiry datetime of the certificate. |  [optional] |
|**name** | [**NameEnum**](#NameEnum) |  |  [optional] |
|**thumbprint** | **String** | The thumbprint of the certificate. |  [optional] |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| CERTIFICATE1 | &quot;certificate1&quot; |
| CERTIFICATE2 | &quot;certificate2&quot; |



