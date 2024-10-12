

# ImageReference

A summary of an image identity, including digest, id (if available), and any tags known to have ever been mapped to the digest

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**analyzedAt** | **String** | Timestamp, in rfc3339 format, indicating when the image state became &#39;analyzed&#39; in Anchore Engine. |  [optional] |
|**digest** | **String** | The image digest |  [optional] |
|**id** | **String** | The image id if available |  [optional] |
|**tagHistory** | [**List&lt;TagEntry&gt;**](TagEntry.md) |  |  [optional] |



