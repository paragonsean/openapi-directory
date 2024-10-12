# CloudFunctionsApi.SecretEnvVar

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **String** | Name of the environment variable. | [optional] 
**projectId** | **String** | Project identifier (preferrably project number but can also be the project ID) of the project that contains the secret. If not set, it will be populated with the function&#39;s project assuming that the secret exists in the same project as of the function. | [optional] 
**secret** | **String** | Name of the secret in secret manager (not the full resource name). | [optional] 
**version** | **String** | Version of the secret (version number or the string &#39;latest&#39;). It is recommended to use a numeric version for secret environment variables as any updates to the secret value is not reflected until new instances start. | [optional] 


