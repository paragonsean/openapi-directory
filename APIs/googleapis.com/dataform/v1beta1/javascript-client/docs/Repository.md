# DataformApi.Repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The timestamp of when the repository was created. | [optional] [readonly] 
**displayName** | **String** | Optional. The repository&#39;s user-friendly name. | [optional] 
**gitRemoteSettings** | [**GitRemoteSettings**](GitRemoteSettings.md) |  | [optional] 
**labels** | **{String: String}** | Optional. Repository user labels. | [optional] 
**name** | **String** | Output only. The repository&#39;s name. | [optional] [readonly] 
**npmrcEnvironmentVariablesSecretVersion** | **String** | Optional. The name of the Secret Manager secret version to be used to interpolate variables into the .npmrc file for package installation operations. Must be in the format &#x60;projects/_*_/secrets/_*_/versions/_*&#x60;. The file itself must be in a JSON format. | [optional] 
**serviceAccount** | **String** | Optional. The service account to run workflow invocations under. | [optional] 
**setAuthenticatedUserAdmin** | **Boolean** | Optional. Input only. If set to true, the authenticated user will be granted the roles/dataform.admin role on the created repository. To modify access to the created repository later apply setIamPolicy from https://cloud.google.com/dataform/reference/rest#rest-resource:-v1beta1.projects.locations.repositories | [optional] 
**workspaceCompilationOverrides** | [**WorkspaceCompilationOverrides**](WorkspaceCompilationOverrides.md) |  | [optional] 


