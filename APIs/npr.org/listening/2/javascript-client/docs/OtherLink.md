# NprListeningService.OtherLink

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **String** | The link to be followed | 
**contentType** | **String** | The MIME type of the response of this link; note that the enumerated list of possible values is not exhaustive and other MIME types could occur. The list should be treated as examples, rather than absolutes. | [default to &#39;application/json&#39;]
**linkText** | **String** | Text recommended to accompany the link. For example, &#39;Read Story&#39; with a full story link, or &#39;Read Transcript&#39; with a transcript link. | [optional] 
**pollInterval** | **Number** | When present, the recommended number of seconds between requests to the given URL | [optional] 



## Enum: ContentTypeEnum


* `application/json` (value: `"application/json"`)

* `application/xml` (value: `"application/xml"`)

* `text/html` (value: `"text/html"`)




