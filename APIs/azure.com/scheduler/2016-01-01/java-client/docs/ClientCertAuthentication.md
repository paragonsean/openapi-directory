

# ClientCertAuthentication


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateExpirationDate** | **OffsetDateTime** | Gets or sets the certificate expiration date. |  [optional] |
|**certificateSubjectName** | **String** | Gets or sets the certificate subject name. |  [optional] |
|**certificateThumbprint** | **String** | Gets or sets the certificate thumbprint. |  [optional] |
|**password** | **String** | Gets or sets the password. |  [optional] |
|**pfx** | **String** | Gets or sets the pfx. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Gets or sets the http authentication type. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NOT_SPECIFIED | &quot;NotSpecified&quot; |
| CLIENT_CERTIFICATE | &quot;ClientCertificate&quot; |
| ACTIVE_DIRECTORY_O_AUTH | &quot;ActiveDirectoryOAuth&quot; |
| BASIC | &quot;Basic&quot; |



