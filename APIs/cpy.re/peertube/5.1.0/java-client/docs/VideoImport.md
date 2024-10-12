

# VideoImport


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**error** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**magnetUri** | **URI** | magnet URI allowing to resolve the import&#39;s source video |  [optional] |
|**state** | [**VideoImportStateConstant**](VideoImportStateConstant.md) |  |  [optional] [readonly] |
|**targetUrl** | **String** | remote URL where to find the import&#39;s source video |  [optional] |
|**torrentName** | **String** |  |  [optional] [readonly] |
|**torrentfile** | **File** | Torrent file containing only the video file |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**video** | [**Video**](Video.md) |  |  [optional] [readonly] |



