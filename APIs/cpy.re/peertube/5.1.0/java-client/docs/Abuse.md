

# Abuse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**id** | **Integer** |  |  [optional] |
|**moderationComment** | **String** |  |  [optional] |
|**predefinedReasons** | [**List&lt;PredefinedReasonsEnum&gt;**](#List&lt;PredefinedReasonsEnum&gt;) |  |  [optional] |
|**reason** | **String** |  |  [optional] |
|**reporterAccount** | [**Account**](Account.md) |  |  [optional] |
|**state** | [**AbuseStateConstant**](AbuseStateConstant.md) |  |  [optional] |
|**video** | [**VideoInfo**](VideoInfo.md) |  |  [optional] |



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



