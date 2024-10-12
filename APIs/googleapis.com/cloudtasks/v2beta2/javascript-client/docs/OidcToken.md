# CloudTasksApi.OidcToken

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **String** | Audience to be used when generating OIDC token. If not specified, the URI specified in target will be used. | [optional] 
**serviceAccountEmail** | **String** | [Service account email](https://cloud.google.com/iam/docs/service-accounts) to be used for generating OIDC token. The service account must be within the same project as the queue. The caller must have iam.serviceAccounts.actAs permission for the service account. | [optional] 


