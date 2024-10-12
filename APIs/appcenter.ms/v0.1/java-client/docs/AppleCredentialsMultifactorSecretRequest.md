

# AppleCredentialsMultifactorSecretRequest

Apple connection secrets

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**Object**](Object.md) | apple secret details |  |
|**credentialType** | [**CredentialTypeEnum**](#CredentialTypeEnum) | credential type of the shared connection. Values can be credentials|certificate |  [optional] |
|**displayName** | **String** | display name of shared connection |  [optional] |
|**serviceType** | [**ServiceTypeEnum**](#ServiceTypeEnum) | service type of shared connection can be apple|gitlab|googleplay|jira|applecertificate |  |



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



