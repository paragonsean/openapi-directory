# BungieNetApi.ContentContentItemPublicContract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowComments** | **Boolean** |  | [optional] 
**author** | [**UserGeneralUser**](UserGeneralUser.md) |  | [optional] 
**autoEnglishPropertyFallback** | **Boolean** |  | [optional] 
**cType** | **String** |  | [optional] 
**cmsPath** | **String** |  | [optional] 
**commentSummary** | [**ContentCommentSummary**](ContentCommentSummary.md) |  | [optional] 
**contentId** | **Number** |  | [optional] 
**creationDate** | **Date** |  | [optional] 
**hasAgeGate** | **Boolean** |  | [optional] 
**minimumAge** | **Number** |  | [optional] 
**modifyDate** | **Date** |  | [optional] 
**properties** | **{String: Object}** | Firehose content is really a collection of metadata and \&quot;properties\&quot;, which are the potentially-but-not-strictly localizable data that comprises the meat of whatever content is being shown.  As Cole Porter would have crooned, \&quot;Anything Goes\&quot; with Firehose properties. They are most often strings, but they can theoretically be anything. They are JSON encoded, and could be JSON structures, simple strings, numbers etc... The Content Type of the item (cType) will describe the properties, and thus how they ought to be deserialized. | [optional] 
**ratingImagePath** | **String** |  | [optional] 
**representations** | [**[ContentContentRepresentation]**](ContentContentRepresentation.md) |  | [optional] 
**tags** | **[String]** | NOTE: Tags will always be lower case. | [optional] 


