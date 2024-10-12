# AlerterSystemApi.MediaObjectJsonldGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**AlertLogJsonldGetContext**](AlertLogJsonldGetContext.md) |  | [optional] 
**id** | **String** |  | [optional] [readonly] 
**type** | **String** |  | [optional] [readonly] 
**contentUrl** | **String** | Where the media file can be accessed. | [optional] 
**createdAt** | **Date** | When the resource instance was created. This date-time is in the UTC timezone. | [optional] [readonly] 
**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. | [optional] 
**fileSize** | **Number** | The size of the media file. | [optional] 
**id** | **String** | The unique identifier of the resource instance. | [optional] [readonly] 
**keywords** | **String** | A string of keywords that can be used to search for a resource. Max 100 characters. | [optional] 
**mimeType** | **String** | The mime type of the media file. | [optional] 
**originalName** | **String** | The original name of the media file. | [optional] 
**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. | 
**resourceOwner** | **String** | The name of the person who owns this resource. | [optional] 


