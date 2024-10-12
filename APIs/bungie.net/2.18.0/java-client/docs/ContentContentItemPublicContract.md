

# ContentContentItemPublicContract


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowComments** | **Boolean** |  |  [optional] |
|**author** | [**UserGeneralUser**](UserGeneralUser.md) |  |  [optional] |
|**autoEnglishPropertyFallback** | **Boolean** |  |  [optional] |
|**cType** | **String** |  |  [optional] |
|**cmsPath** | **String** |  |  [optional] |
|**commentSummary** | [**ContentCommentSummary**](ContentCommentSummary.md) |  |  [optional] |
|**contentId** | **Long** |  |  [optional] |
|**creationDate** | **OffsetDateTime** |  |  [optional] |
|**hasAgeGate** | **Boolean** |  |  [optional] |
|**minimumAge** | **Integer** |  |  [optional] |
|**modifyDate** | **OffsetDateTime** |  |  [optional] |
|**properties** | **Map&lt;String, Object&gt;** | Firehose content is really a collection of metadata and \&quot;properties\&quot;, which are the potentially-but-not-strictly localizable data that comprises the meat of whatever content is being shown.  As Cole Porter would have crooned, \&quot;Anything Goes\&quot; with Firehose properties. They are most often strings, but they can theoretically be anything. They are JSON encoded, and could be JSON structures, simple strings, numbers etc... The Content Type of the item (cType) will describe the properties, and thus how they ought to be deserialized. |  [optional] |
|**ratingImagePath** | **String** |  |  [optional] |
|**representations** | [**List&lt;ContentContentRepresentation&gt;**](ContentContentRepresentation.md) |  |  [optional] |
|**tags** | **List&lt;String&gt;** | NOTE: Tags will always be lower case. |  [optional] |



