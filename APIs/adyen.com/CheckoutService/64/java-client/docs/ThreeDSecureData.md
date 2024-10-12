

# ThreeDSecureData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authenticationResponse** | [**AuthenticationResponseEnum**](#AuthenticationResponseEnum) | In 3D Secure 1, the authentication response if the shopper was redirected.  In 3D Secure 2, this is the &#x60;transStatus&#x60; from the challenge result. If the transaction was frictionless, omit this parameter. |  [optional] |
|**cavv** | **String** | The cardholder authentication value (base64 encoded, 20 bytes in a decoded form). |  [optional] |
|**cavvAlgorithm** | **String** | The CAVV algorithm used. Include this only for 3D Secure 1. |  [optional] |
|**directoryResponse** | [**DirectoryResponseEnum**](#DirectoryResponseEnum) | In 3D Secure 1, this is the enrollment response from the 3D directory server.  In 3D Secure 2, this is the &#x60;transStatus&#x60; from the &#x60;ARes&#x60;. |  [optional] |
|**dsTransID** | **String** | Supported for 3D Secure 2. The unique transaction identifier assigned by the Directory Server (DS) to identify a single transaction. |  [optional] |
|**eci** | **String** | The electronic commerce indicator. |  [optional] |
|**threeDSVersion** | **String** | The version of the 3D Secure protocol. |  [optional] |
|**xid** | **String** | Supported for 3D Secure 1. The transaction identifier (Base64-encoded, 20 bytes in a decoded form). |  [optional] |



## Enum: AuthenticationResponseEnum

| Name | Value |
|---- | -----|
| Y | &quot;Y&quot; |
| N | &quot;N&quot; |
| U | &quot;U&quot; |
| A | &quot;A&quot; |



## Enum: DirectoryResponseEnum

| Name | Value |
|---- | -----|
| A | &quot;A&quot; |
| C | &quot;C&quot; |
| D | &quot;D&quot; |
| I | &quot;I&quot; |
| N | &quot;N&quot; |
| R | &quot;R&quot; |
| U | &quot;U&quot; |
| Y | &quot;Y&quot; |



