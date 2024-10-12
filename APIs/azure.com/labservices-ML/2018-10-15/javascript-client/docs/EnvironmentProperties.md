# ManagedLabsClient.EnvironmentProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claimedByUserName** | **String** | The name or email address of the user who has claimed the environment | [optional] [readonly] 
**claimedByUserObjectId** | **String** | The AAD object Id of the user who has claimed the environment | [optional] [readonly] 
**claimedByUserPrincipalId** | **String** | The user principal Id of the user who has claimed the environment | [optional] [readonly] 
**isClaimed** | **Boolean** | Is the environment claimed or not | [optional] [readonly] 
**lastKnownPowerState** | **String** | Last known power state of the environment | [optional] [readonly] 
**latestOperationResult** | [**LatestOperationResult**](LatestOperationResult.md) |  | [optional] 
**networkInterface** | [**NetworkInterface**](NetworkInterface.md) |  | [optional] 
**passwordLastReset** | **Date** | When the password was last reset on the environment. | [optional] [readonly] 
**provisioningState** | **String** | The provisioning status of the resource. | [optional] 
**resourceSets** | [**ResourceSet**](ResourceSet.md) |  | [optional] 
**totalUsage** | **String** | How long the environment has been used by a lab user | [optional] [readonly] 
**uniqueIdentifier** | **String** | The unique immutable identifier of a resource (Guid). | [optional] 


