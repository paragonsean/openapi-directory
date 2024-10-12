# RestApiVersion2.SpaceItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **String** | The Status of this item | [optional] 
**attachments** | [**[SpaceAttachment]**](SpaceAttachment.md) | The list of attachments | [optional] 
**complex** | **Boolean** | Is this item complex | [optional] 
**content** | **String** | The content of this item | [optional] 
**creationTime** | **Number** | The time this item got created | [optional] 
**creatorId** | **String** | The Id of the creator | [optional] 
**deletedBy** | **String** | Incase this item got deleted, the id of the deletor | [optional] 
**externalAttachments** | [**[SpaceExternalAttachment]**](SpaceExternalAttachment.md) | A list of external attachments | [optional] 
**formMetaData** | **String** | Incase there is FormMetaData | [optional] 
**itemId** | **String** | the Id of this item | [optional] 
**mentionedUsers** | **[String]** | A list of userIds who have been mentioned in this item | [optional] 
**modificationTime** | **Number** | the time this item got modified | [optional] 
**numberOfLikes** | **Number** | The number of likes | [optional] 
**previews** | [**[SpaceItemPreview]**](SpaceItemPreview.md) | A list of previews | [optional] 
**sharedItems** | [**[SharedItem]**](SharedItem.md) | missing documentation | [optional] 
**spaceId** | **String** | the Id of the space containing this item | [optional] 
**tenantId** | **String** | the Id of the tenant | [optional] 


