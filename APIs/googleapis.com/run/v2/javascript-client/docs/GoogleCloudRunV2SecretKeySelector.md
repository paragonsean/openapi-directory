# CloudRunAdminApi.GoogleCloudRunV2SecretKeySelector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **String** | Required. The name of the secret in Cloud Secret Manager. Format: {secret_name} if the secret is in the same project. projects/{project}/secrets/{secret_name} if the secret is in a different project. | [optional] 
**version** | **String** | The Cloud Secret Manager secret version. Can be &#39;latest&#39; for the latest version, an integer for a specific version, or a version alias. | [optional] 


