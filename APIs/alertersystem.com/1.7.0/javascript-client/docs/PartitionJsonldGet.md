# AlerterSystemApi.PartitionJsonldGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**AlertLogJsonldGetContext**](AlertLogJsonldGetContext.md) |  | [optional] 
**id** | **String** |  | [optional] [readonly] 
**type** | **String** |  | [optional] [readonly] 
**alertServices** | **[String]** | The alert services that are related to this resource. | [optional] 
**createdAt** | **Date** | When the resource instance was created. This date-time is in the UTC timezone. | [optional] [readonly] 
**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. | [optional] 
**id** | **String** | The unique identifier of the resource instance. | [optional] [readonly] 
**monitors** | **[String]** | The monitors that are associated with this partition. | [optional] 
**partitionName** | **String** | The name of the partition. Max 255 characters. | 
**partitionNotes** | **String** | Notes about the partition. Max 10,000 characters. Formatting using Markdown is allowed. HTML will be removed. | [optional] 
**resourceOwner** | **String** | The name of the person who owns this resource. | [optional] 
**teamInvitations** | **[String]** | The team invitations that are related to this resource. | [optional] 
**teamMembers** | **[String]** | The team members of this resource. | [optional] 


