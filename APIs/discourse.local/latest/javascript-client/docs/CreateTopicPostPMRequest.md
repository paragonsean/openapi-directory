# DiscourseApiDocumentation.CreateTopicPostPMRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archetype** | **String** | Required for new private message. | [optional] 
**category** | **Number** | Optional if creating a new topic, and ignored if creating a new post. | [optional] 
**createdAt** | **String** |  | [optional] 
**embedUrl** | **String** | Provide a URL from a remote system to associate a forum topic with that URL, typically for using Discourse as a comments system for an external blog. | [optional] 
**externalId** | **String** | Provide an external_id from a remote system to associate a forum topic with that id. | [optional] 
**raw** | **String** |  | 
**targetRecipients** | **String** | Required for private message, comma separated. | [optional] 
**targetUsernames** | **String** | Deprecated. Use target_recipients instead. | [optional] 
**title** | **String** | Required if creating a new topic or new private message. | [optional] 
**topicId** | **Number** | Required if creating a new post. | [optional] 


