# CloudRunAdminApi.SecretKeySelector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **String** | A Cloud Secret Manager secret version. Must be &#39;latest&#39; for the latest version or an integer for a specific version. The key of the secret to select from. Must be a valid secret key. | [optional] 
**localObjectReference** | [**LocalObjectReference**](LocalObjectReference.md) |  | [optional] 
**name** | **String** | The name of the secret in Cloud Secret Manager. By default, the secret is assumed to be in the same project. If the secret is in another project, you must define an alias. An alias definition has the form: :projects//secrets/. If multiple alias definitions are needed, they must be separated by commas. The alias definitions must be set on the run.googleapis.com/secrets annotation. The name of the secret in the pod&#39;s namespace to select from. | [optional] 
**optional** | **Boolean** | (Optional) Specify whether the Secret or its key must be defined | [optional] 


