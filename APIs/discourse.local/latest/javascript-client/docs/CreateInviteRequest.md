# DiscourseApiDocumentation.CreateInviteRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customMessage** | **String** | optional, for email invites | [optional] 
**email** | **String** | required for email invites only | [optional] 
**expiresAt** | **String** | optional, if not supplied, the invite_expiry_days site setting is used | [optional] 
**groupId** | **Number** | optional, either this or &#x60;group_names&#x60; | [optional] 
**groupNames** | **String** | optional, either this or &#x60;group_id&#x60; | [optional] 
**maxRedemptionsAllowed** | **Number** | optional, for link invites | [optional] [default to 1]
**skipEmail** | **Boolean** |  | [optional] [default to false]
**topicId** | **Number** |  | [optional] 


