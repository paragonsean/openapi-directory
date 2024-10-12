# ServiceControlApi.AuthenticationInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authoritySelector** | **String** | The authority selector specified by the requestor, if any. It is not guaranteed that the principal was allowed to use this authority. | [optional] 
**principalEmail** | **String** | The email address of the authenticated user (or service account on behalf of third party principal) making the request. For third party identity callers, the &#x60;principal_subject&#x60; field is populated instead of this field. For privacy reasons, the principal email address is sometimes redacted. For more information, see [Caller identities in audit logs](https://cloud.google.com/logging/docs/audit#user-id). | [optional] 
**principalSubject** | **String** | String representation of identity of requesting party. Populated for both first and third party identities. | [optional] 
**serviceAccountDelegationInfo** | [**[ServiceAccountDelegationInfo]**](ServiceAccountDelegationInfo.md) | Identity delegation history of an authenticated service account that makes the request. It contains information on the real authorities that try to access GCP resources by delegating on a service account. When multiple authorities present, they are guaranteed to be sorted based on the original ordering of the identity delegation events. | [optional] 
**serviceAccountKeyName** | **String** | The name of the service account key used to create or exchange credentials for authenticating the service account making the request. This is a scheme-less URI full resource name. For example: \&quot;//iam.googleapis.com/projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}/keys/{key}\&quot; | [optional] 
**serviceDelegationHistory** | [**ServiceDelegationHistory**](ServiceDelegationHistory.md) |  | [optional] 
**thirdPartyPrincipal** | **{String: Object}** | The third party identification (if any) of the authenticated user making the request. When the JSON object represented here has a proto equivalent, the proto name will be indicated in the &#x60;@type&#x60; property. | [optional] 


