

# PrivateAppleCertificateSecretResponse

private Apple connection secrets response

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**Object**](Object.md) | apple secret details |  |
|**displayName** | **String** | display name of shared connection |  [optional] |
|**id** | **String** | id of the shared connection |  |
|**is2FA** | **Boolean** | if the account is a 2FA account or not |  [optional] |
|**isValid** | **Boolean** | whether the credentials are valid or not |  [optional] |
|**serviceType** | [**ServiceTypeEnum**](#ServiceTypeEnum) | service type of shared connection can be apple|gitlab|googleplay|jira|applecertificate |  |



## Enum: ServiceTypeEnum

| Name | Value |
|---- | -----|
| APPLE | &quot;apple&quot; |
| JIRA | &quot;jira&quot; |
| GOOGLEPLAY | &quot;googleplay&quot; |
| GITLAB | &quot;gitlab&quot; |



