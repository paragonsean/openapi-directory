

# V1beta1ServiceAccount

A service account in the Identity and Access Management API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** | The email address of the service account. |  [optional] |
|**iamAccountName** | **String** | Deprecated. See b/136209818. |  [optional] |
|**name** | **String** | P4 SA resource name. An example name would be: &#x60;services/serviceconsumermanagement.googleapis.com/projects/123/serviceAccounts/default&#x60; |  [optional] |
|**tag** | **String** | The P4 SA configuration tag. This must be defined in activation_grants. If not specified when creating the account, the tag is set to \&quot;default\&quot;. |  [optional] |
|**uniqueId** | **String** | The unique and stable id of the service account. |  [optional] |



