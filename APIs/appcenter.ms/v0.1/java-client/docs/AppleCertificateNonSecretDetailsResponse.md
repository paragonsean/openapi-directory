

# AppleCertificateNonSecretDetailsResponse

Apple certificate non-secret details

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**Object**](Object.md) | apple certificate non-secret details |  |
|**credentialType** | [**CredentialTypeEnum**](#CredentialTypeEnum) | the type of the credential |  [optional] |
|**displayName** | **String** | display name of shared connection |  |
|**serviceType** | [**ServiceTypeEnum**](#ServiceTypeEnum) | service type of shared connection can be apple|gitlab|googleplay|jira |  |



## Enum: CredentialTypeEnum

| Name | Value |
|---- | -----|
| CREDENTIALS | &quot;credentials&quot; |
| CERTIFICATE | &quot;certificate&quot; |
| KEY | &quot;key&quot; |



## Enum: ServiceTypeEnum

| Name | Value |
|---- | -----|
| APPLE | &quot;apple&quot; |
| JIRA | &quot;jira&quot; |
| GOOGLEPLAY | &quot;googleplay&quot; |
| GITLAB | &quot;gitlab&quot; |



