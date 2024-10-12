

# ListVolumeRestoresResponse

Response message for ListVolumeRestores.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token which may be sent as page_token in a subsequent &#x60;ListVolumeRestores&#x60; call to retrieve the next page of results. If this field is omitted or empty, then there are no more results to return. |  [optional] |
|**volumeRestores** | [**List&lt;VolumeRestore&gt;**](VolumeRestore.md) | The list of VolumeRestores matching the given criteria. |  [optional] |



