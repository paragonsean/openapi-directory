# SnykApi.ProvisionAUserToTheOrganizationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **String** | The email of the user. | 
**role** | **String** | Deprecated. Name of the role to grant this user. Must be one of &#x60;ADMIN&#x60;, &#x60;COLLABORATOR&#x60;, or &#x60;RESTRICTED_COLLABORATOR&#x60;. This field is invalid if &#x60;rolePublicId&#x60; is supplied with the request. | [optional] 
**rolePublicId** | **String** | ID of the role to grant this user. | [optional] 


