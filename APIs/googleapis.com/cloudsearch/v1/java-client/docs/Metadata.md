

# Metadata

Metadata of a matched search result.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | The creation time for this document or object in the search result. |  [optional] |
|**displayOptions** | [**ResultDisplayMetadata**](ResultDisplayMetadata.md) |  |  [optional] |
|**fields** | [**List&lt;NamedProperty&gt;**](NamedProperty.md) | Indexed fields in structured data, returned as a generic named property. |  [optional] |
|**mimeType** | **String** | Mime type of the search result. |  [optional] |
|**objectType** | **String** | Object type of the search result. |  [optional] |
|**owner** | [**Person**](Person.md) |  |  [optional] |
|**source** | [**Source**](Source.md) |  |  [optional] |
|**thumbnailUrl** | **String** | The thumbnail URL of the result. |  [optional] |
|**updateTime** | **String** | The last modified date for the object in the search result. If not set in the item, the value returned here is empty. When &#x60;updateTime&#x60; is used for calculating freshness and is not set, this value defaults to 2 years from the current time. |  [optional] |



