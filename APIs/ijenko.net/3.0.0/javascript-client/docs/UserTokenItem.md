# IoEIoTApiToCreateEndUserApplications.UserTokenItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appName** | **String** | Application name | 
**id** | **String** |  | 
**lastUse** | **Date** | Time of last use of the token to access the API. Updated at most every 15 minutes. If absent, the token has never been used. | [optional] 
**places** | [**[PlaceItem]**](PlaceItem.md) | List of Places to which the User has access. If absent, it means any Place of the account are allowed. | [optional] 
**refreshTokenExpires** | **Date** | If absent, infinite validity. | [optional] 
**self** | **Boolean** | True if this token is the one used for this API request | [optional] 
**user** | [**UserItem**](UserItem.md) |  | 


