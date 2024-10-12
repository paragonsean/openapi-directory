# DevTestLabsClient.UserIdentity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appId** | **String** | Set to the app Id of the client JWT making the request. | [optional] 
**objectId** | **String** | Set to the object Id of the client JWT making the request. Not all users have object Id. For CSP (reseller) scenarios for example, object Id is not available. | [optional] 
**principalId** | **String** | Set to the principal Id of the client JWT making the request. Service principal will not have the principal Id. | [optional] 
**principalName** | **String** | Set to the principal name / UPN of the client JWT making the request. | [optional] 
**tenantId** | **String** | Set to the tenant ID of the client JWT making the request. | [optional] 


