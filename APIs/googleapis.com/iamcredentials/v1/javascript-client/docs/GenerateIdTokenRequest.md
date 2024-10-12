# IamServiceAccountCredentialsApi.GenerateIdTokenRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **String** | Required. The audience for the token, such as the API or account that this token grants access to. | [optional] 
**delegates** | **[String]** | The sequence of service accounts in a delegation chain. Each service account must be granted the &#x60;roles/iam.serviceAccountTokenCreator&#x60; role on its next service account in the chain. The last service account in the chain must be granted the &#x60;roles/iam.serviceAccountTokenCreator&#x60; role on the service account that is specified in the &#x60;name&#x60; field of the request. The delegates must have the following format: &#x60;projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}&#x60;. The &#x60;-&#x60; wildcard character is required; replacing it with a project ID is invalid. | [optional] 
**includeEmail** | **Boolean** | Include the service account email in the token. If set to &#x60;true&#x60;, the token will contain &#x60;email&#x60; and &#x60;email_verified&#x60; claims. | [optional] 


