

# Asset

A single asset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | **String** | The asset content. For uploaded assets, the content is the serving path. |  [optional] |
|**mediaId** | **String** | Media ID of the uploaded asset. This is a unique identifier for the asset. This ID can be passed to other API calls, e.g. CreateCreative to associate the asset with a creative. The Media ID space updated on **April 5, 2023**. Update media IDs cached before **April 5, 2023** by retrieving the new media ID from associated creative resources or re-uploading the asset. |  [optional] |



