# AlerterSystemApi.TransportPagerTreeJsonldGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**AlertLogJsonldGetContext**](AlertLogJsonldGetContext.md) |  | [optional] 
**id** | **String** |  | [optional] [readonly] 
**type** | **String** |  | [optional] [readonly] 
**createdAt** | **Date** | When the resource instance was created. This date-time is in the UTC timezone. | [optional] 
**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. | [optional] 
**id** | **String** | The unique identifier of the resource instance. | [optional] [readonly] 
**pagerTreeAccessToken** | **String** | The access token for the Pager Tree service. Stored in encrypted format. | 
**pagerTreeAccountUserId** | **String** | The account user ID for the Pager Tree service. (Must supply either team ID, router ID or account user ID.) | [optional] 
**pagerTreeRouterId** | **String** | The router ID for the Pager Tree service. (Must supply either team ID, router ID or account user ID.) | [optional] 
**pagerTreeTeamId** | **String** | The team ID for the Pager Tree service. (Must supply either team ID, router ID or account user ID.) | [optional] 
**pagerTreeUrgency** | **String** | The urgency for the Pager Tree service. | 
**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. | 
**resourceOwner** | **String** | The name of the person who owns this resource. | [optional] 
**transportName** | **String** | The name of the transport. | 


