

# MediaItem

A single media item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attribution** | [**Attribution**](Attribution.md) |  |  [optional] |
|**createTime** | **String** | Output only. Creation time of this media item. |  [optional] |
|**dataRef** | [**MediaItemDataRef**](MediaItemDataRef.md) |  |  [optional] |
|**description** | **String** | Description for this media item. Descriptions cannot be modified through the Google My Business API, but can be set when creating a new media item that is not a cover photo. |  [optional] |
|**dimensions** | [**Dimensions**](Dimensions.md) |  |  [optional] |
|**googleUrl** | **String** | Output only. Google-hosted URL for this media item. This URL is not static since it may change over time. For video this will be a preview image with an overlaid play icon. |  [optional] |
|**insights** | [**MediaInsights**](MediaInsights.md) |  |  [optional] |
|**locationAssociation** | [**LocationAssociation**](LocationAssociation.md) |  |  [optional] |
|**mediaFormat** | [**MediaFormatEnum**](#MediaFormatEnum) | The format of this media item. Must be set when the media item is created, and is read-only on all other requests. Cannot be updated. |  [optional] |
|**name** | **String** | The resource name for this media item. &#x60;accounts/{account_id}/locations/{location_id}/media/{media_key}&#x60; |  [optional] |
|**sourceUrl** | **String** | A publicly accessible URL where the media item can be retrieved from. When creating one of this or data_ref must be set to specify the source of the media item. If &#x60;source_url&#x60; was used when creating a media item, it will be populated with that source URL when the media item is retrieved. This field cannot be updated. |  [optional] |
|**thumbnailUrl** | **String** | Output only. Where provided, the URL of a thumbnail image for this media item. |  [optional] |



## Enum: MediaFormatEnum

| Name | Value |
|---- | -----|
| MEDIA_FORMAT_UNSPECIFIED | &quot;MEDIA_FORMAT_UNSPECIFIED&quot; |
| PHOTO | &quot;PHOTO&quot; |
| VIDEO | &quot;VIDEO&quot; |



