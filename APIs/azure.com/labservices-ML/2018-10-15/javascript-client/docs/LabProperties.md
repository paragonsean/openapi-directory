# ManagedLabsClient.LabProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdByObjectId** | **String** | Object id of the user that created the lab. | [optional] [readonly] 
**createdByUserPrincipalName** | **String** | Lab creator name | [optional] [readonly] 
**createdDate** | **Date** | Creation date for the lab | [optional] [readonly] 
**invitationCode** | **String** | Invitation code that users can use to join a lab. | [optional] [readonly] 
**latestOperationResult** | [**LatestOperationResult**](LatestOperationResult.md) |  | [optional] 
**maxUsersInLab** | **Number** | Maximum number of users allowed in the lab. | [optional] 
**provisioningState** | **String** | The provisioning status of the resource. | [optional] 
**uniqueIdentifier** | **String** | The unique immutable identifier of a resource (Guid). | [optional] 
**usageQuota** | **String** | Maximum duration a user can use an environment for in the lab. | [optional] 
**userAccessMode** | **String** | Lab user access mode (open to all vs. restricted to those listed on the lab). | [optional] 
**userQuota** | **Number** | Maximum value MaxUsersInLab can be set to, as specified by the service | [optional] [readonly] 



## Enum: UserAccessModeEnum


* `Restricted` (value: `"Restricted"`)

* `Open` (value: `"Open"`)




