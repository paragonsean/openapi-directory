# AppCenterClient.SharedConnectionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentialType** | **String** | credential type of the shared connection. Values can be credentials|certificate | [optional] [default to &#39;credentials&#39;]
**data** | [**AppleConnectionSecretRequestAllOfData**](AppleConnectionSecretRequestAllOfData.md) |  | [optional] 
**displayName** | **String** | display name of shared connection | [optional] 
**serviceType** | **String** | service type of shared connection can be apple|gitlab|googleplay|jira|applecertificate | 



## Enum: CredentialTypeEnum


* `credentials` (value: `"credentials"`)

* `certificate` (value: `"certificate"`)

* `key` (value: `"key"`)





## Enum: ServiceTypeEnum


* `apple` (value: `"apple"`)

* `jira` (value: `"jira"`)

* `googleplay` (value: `"googleplay"`)

* `gitlab` (value: `"gitlab"`)




