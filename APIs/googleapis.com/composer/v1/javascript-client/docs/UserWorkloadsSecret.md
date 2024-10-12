# CloudComposerApi.UserWorkloadsSecret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **{String: String}** | Optional. The \&quot;data\&quot; field of Kubernetes Secret, organized in key-value pairs, which can contain sensitive values such as a password, a token, or a key. The values for all keys have to be base64-encoded strings. For details see: https://kubernetes.io/docs/concepts/configuration/secret/ | [optional] 
**name** | **String** | Identifier. The resource name of the Secret, in the form: \&quot;projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}\&quot; | [optional] 


