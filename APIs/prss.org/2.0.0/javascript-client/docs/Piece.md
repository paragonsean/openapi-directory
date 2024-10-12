# ContentDepot.Piece

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contributor** | **String** | The artist or contributor name. | [optional] 
**createdDate** | **Date** | The date the piece was created. Generated at creation. | [optional] [readonly] 
**description** | **String** | The short description of the piece. | [optional] 
**episodeId** | **Number** | The ID of the episode that owns the piece. | 
**fullDescription** | **String** | The long description of the piece. | [optional] 
**id** | **Number** | The unique ID of the piece. Generated at creation. | [optional] [readonly] 
**imageCdDriveUri** | **String** | The URI to the piece image content in CD Drive. Format should be &#39;cddrive:id:{value}&#39; or &#39;cddrive://{path}&#39;. This property is only used on modification and is not returned. | [optional] 
**imageFileName** | **String** | The name of the piece image file. Generated at creation. | [optional] 
**imageFileSize** | **Number** | The size of the piece image file in bytes. Generated at creation. | [optional] 
**imageOriginalFileName** | **String** | The user&#39;s original name of the piece image file. | [optional] 
**lastModifiedDate** | **Date** | The date the piece was last modified/updated. Automatically updated on any write operation. | [optional] [readonly] 
**relativeEndTime** | **Number** | Seconds relative to the start of the episode. | 
**relativeStartTime** | **Number** | Seconds relative to the start of the episode. | 
**segmentNumber** | **Number** | The number of the segment that this piece is in, starting with 1. This is an optional field but it can be used to provide more detail by linking the piece to a specific audio segment. | [optional] 
**title** | **String** | The human readable title of the piece that is normally displayed on an end user&#39;s device. | 


