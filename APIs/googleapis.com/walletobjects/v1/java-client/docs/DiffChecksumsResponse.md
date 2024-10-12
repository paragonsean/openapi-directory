

# DiffChecksumsResponse

Backend response for a Diff get checksums response. For details on the Scotty Diff protocol, visit http://go/scotty-diff-protocol.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checksumsLocation** | [**CompositeMedia**](CompositeMedia.md) |  |  [optional] |
|**chunkSizeBytes** | **String** | The chunk size of checksums. Must be a multiple of 256KB. |  [optional] |
|**objectLocation** | [**CompositeMedia**](CompositeMedia.md) |  |  [optional] |
|**objectSizeBytes** | **String** | The total size of the server object. |  [optional] |
|**objectVersion** | **String** | The object version of the object the checksums are being returned for. |  [optional] |



