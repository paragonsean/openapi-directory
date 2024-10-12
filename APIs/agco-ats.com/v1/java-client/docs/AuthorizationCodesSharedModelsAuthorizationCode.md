

# AuthorizationCodesSharedModelsAuthorizationCode

Represents the model containing an authorization code used to unlock a feature in machines and EDT

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | The code to enter to unlock a feature. Read only. |  [optional] |
|**createdByUserID** | **Integer** | The ID of the user that created this authorization code. Read only. |  [optional] |
|**createdDate** | **OffsetDateTime** | A timestamp of when this code was created. Read only. |  [optional] |
|**dataParameters** | [**List&lt;AuthorizationCodesSharedModelsParameter&gt;**](AuthorizationCodesSharedModelsParameter.md) | The parameters and values contained as data in this authorization code. May not be updated. |  [optional] |
|**definitionID** | **String** | The id of the definition for this authorization code. May not be updated. |  [optional] |
|**deletedByUserID** | **Integer** | The ID of the user that deleted this authorization code. Read only. |  [optional] |
|**deletedDate** | **OffsetDateTime** | A timestamp of when this authorization code was deleted. Read only. |  [optional] |
|**effectiveDate** | **OffsetDateTime** | A date at which this code should begin being valid. Optional. Set on create only. |  [optional] |
|**ID** | **Integer** | The identifier for the authorization code. Read only. |  [optional] |
|**isDeleted** | **Boolean** | Indicates whether this code is deleted. |  [optional] |
|**validationParameters** | [**List&lt;AuthorizationCodesSharedModelsParameter&gt;**](AuthorizationCodesSharedModelsParameter.md) | The parameters and values used to validate this authorization code. May not be updated. |  [optional] |



