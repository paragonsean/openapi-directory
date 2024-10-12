

# Review

A single review in a VR Listing. NEXT ID: 10

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**author** | **String** | The author of the review. |  [optional] |
|**body** | **String** | The body of the review. |  [optional] |
|**languageCode** | **String** | Language of the review, such as \&quot;en\&quot;, \&quot;de\&quot;, etc. |  [optional] |
|**link** | **String** | The url of the review. |  [optional] |
|**rating** | [**List&lt;Rating&gt;**](Rating.md) | Any ratings associated with this review. This is repeated because reviews can include ratings on different aspects of a listing, e.g. location, cleanliness, etc. |  [optional] |
|**reviewTime** | **String** | Unix timestamp (in seconds) of the review, in UTC+0. |  [optional] |
|**title** | **String** | The title of the review, for example: Great three bedrooms. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the review. |  [optional] |
|**visitTime** | **String** | Unix timestamp (in seconds) of when the stay was, in UTC+0. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| EDITORIAL | &quot;EDITORIAL&quot; |
| USER | &quot;USER&quot; |



