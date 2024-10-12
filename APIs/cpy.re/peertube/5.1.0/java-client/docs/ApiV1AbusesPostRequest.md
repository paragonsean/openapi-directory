

# ApiV1AbusesPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | [**ApiV1AbusesPostRequestAccount**](ApiV1AbusesPostRequestAccount.md) |  |  [optional] |
|**comment** | [**ApiV1AbusesPostRequestComment**](ApiV1AbusesPostRequestComment.md) |  |  [optional] |
|**predefinedReasons** | [**List&lt;PredefinedReasonsEnum&gt;**](#List&lt;PredefinedReasonsEnum&gt;) | Reason categories that help triage reports |  [optional] |
|**reason** | **String** | Reason why the user reports this video |  |
|**video** | [**ApiV1AbusesPostRequestVideo**](ApiV1AbusesPostRequestVideo.md) |  |  [optional] |



## Enum: List&lt;PredefinedReasonsEnum&gt;

| Name | Value |
|---- | -----|
| VIOLENT_OR_ABUSIVE | &quot;violentOrAbusive&quot; |
| HATEFUL_OR_ABUSIVE | &quot;hatefulOrAbusive&quot; |
| SPAM_OR_MISLEADING | &quot;spamOrMisleading&quot; |
| PRIVACY | &quot;privacy&quot; |
| RIGHTS | &quot;rights&quot; |
| SERVER_RULES | &quot;serverRules&quot; |
| THUMBNAILS | &quot;thumbnails&quot; |
| CAPTIONS | &quot;captions&quot; |



