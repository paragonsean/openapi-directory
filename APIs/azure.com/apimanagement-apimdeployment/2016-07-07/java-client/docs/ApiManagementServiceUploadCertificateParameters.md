

# ApiManagementServiceUploadCertificateParameters

Parameters supplied to the Upload SSL certificate for an API Management service operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificate** | **String** | Base64 Encoded certificate. |  |
|**certificatePassword** | **String** | Certificate password. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Hostname type. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PROXY | &quot;Proxy&quot; |
| PORTAL | &quot;Portal&quot; |
| MANAGEMENT | &quot;Management&quot; |
| SCM | &quot;Scm&quot; |



