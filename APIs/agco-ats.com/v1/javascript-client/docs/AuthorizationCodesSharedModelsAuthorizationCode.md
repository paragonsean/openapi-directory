# AgcoApi.AuthorizationCodesSharedModelsAuthorizationCode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | The code to enter to unlock a feature. Read only. | [optional] 
**createdByUserID** | **Number** | The ID of the user that created this authorization code. Read only. | [optional] 
**createdDate** | **Date** | A timestamp of when this code was created. Read only. | [optional] 
**dataParameters** | [**[AuthorizationCodesSharedModelsParameter]**](AuthorizationCodesSharedModelsParameter.md) | The parameters and values contained as data in this authorization code. May not be updated. | [optional] 
**definitionID** | **String** | The id of the definition for this authorization code. May not be updated. | [optional] 
**deletedByUserID** | **Number** | The ID of the user that deleted this authorization code. Read only. | [optional] 
**deletedDate** | **Date** | A timestamp of when this authorization code was deleted. Read only. | [optional] 
**effectiveDate** | **Date** | A date at which this code should begin being valid. Optional. Set on create only. | [optional] 
**ID** | **Number** | The identifier for the authorization code. Read only. | [optional] 
**isDeleted** | **Boolean** | Indicates whether this code is deleted. | [optional] 
**validationParameters** | [**[AuthorizationCodesSharedModelsParameter]**](AuthorizationCodesSharedModelsParameter.md) | The parameters and values used to validate this authorization code. May not be updated. | [optional] 


