

# OtherLink

An individual link from a list of links

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**href** | **URI** | The link to be followed |  |
|**contentType** | [**ContentTypeEnum**](#ContentTypeEnum) | The MIME type of the response of this link; note that the enumerated list of possible values is not exhaustive and other MIME types could occur. The list should be treated as examples, rather than absolutes. |  |
|**linkText** | **String** | Text recommended to accompany the link. For example, &#39;Read Story&#39; with a full story link, or &#39;Read Transcript&#39; with a transcript link. |  [optional] |
|**pollInterval** | **Integer** | When present, the recommended number of seconds between requests to the given URL |  [optional] |



## Enum: ContentTypeEnum

| Name | Value |
|---- | -----|
| APPLICATION_JSON | &quot;application/json&quot; |
| APPLICATION_XML | &quot;application/xml&quot; |
| TEXT_HTML | &quot;text/html&quot; |



