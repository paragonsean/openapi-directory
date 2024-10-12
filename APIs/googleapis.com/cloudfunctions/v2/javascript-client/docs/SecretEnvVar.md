# CloudFunctionsApi.SecretEnvVar

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **String** | Name of the environment variable. | [optional] 
**projectId** | **String** | Project identifier (preferably project number but can also be the project ID) of the project that contains the secret. If not set, it is assumed that the secret is in the same project as the function. | [optional] 
**secret** | **String** | Name of the secret in secret manager (not the full resource name). | [optional] 
**version** | **String** | Version of the secret (version number or the string &#39;latest&#39;). It is recommended to use a numeric version for secret environment variables as any updates to the secret value is not reflected until new instances start. | [optional] 


