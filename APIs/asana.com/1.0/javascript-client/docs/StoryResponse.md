# Asana.StoryResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **String** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resourceType** | **String** | The base type of this resource. | [optional] [readonly] 
**createdAt** | **Date** | The time at which this resource was created. | [optional] [readonly] 
**htmlText** | **String** | [Opt In](/docs/input-output-options). HTML formatted text for a comment. This will not include the name of the creator. | [optional] 
**isPinned** | **Boolean** | *Conditional*. Whether the story should be pinned on the resource. | [optional] 
**resourceSubtype** | **String** | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. | [optional] [readonly] 
**stickerName** | **String** | The name of the sticker in this story. &#x60;null&#x60; if there is no sticker. | [optional] 
**text** | **String** | The plain text of the comment to add. Cannot be used with html_text. | [optional] 
**assignee** | [**UserCompact**](UserCompact.md) |  | [optional] 
**createdBy** | [**UserCompact**](UserCompact.md) |  | [optional] 
**customField** | [**CustomFieldCompact**](CustomFieldCompact.md) |  | [optional] 
**dependency** | [**TaskCompact**](TaskCompact.md) |  | [optional] 
**duplicateOf** | [**TaskCompact**](TaskCompact.md) |  | [optional] 
**duplicatedFrom** | [**TaskCompact**](TaskCompact.md) |  | [optional] 
**follower** | [**UserCompact**](UserCompact.md) |  | [optional] 
**hearted** | **Boolean** | *Deprecated - please use likes instead* *Conditional*. True if the story is hearted by the authorized user, false if not. | [optional] [readonly] 
**hearts** | [**[Like]**](Like.md) | *Deprecated - please use likes instead*  *Conditional*. Array of likes for users who have hearted this story. | [optional] [readonly] 
**isEditable** | **Boolean** | *Conditional*. Whether the text of the story can be edited after creation. | [optional] [readonly] 
**isEdited** | **Boolean** | *Conditional*. Whether the text of the story has been edited after creation. | [optional] [readonly] 
**liked** | **Boolean** | *Conditional*. True if the story is liked by the authorized user, false if not. | [optional] [readonly] 
**likes** | [**[Like]**](Like.md) | *Conditional*. Array of likes for users who have liked this story. | [optional] [readonly] 
**newApprovalStatus** | **String** | *Conditional*. The new value of approval status. | [optional] [readonly] 
**newDateValue** | [**StoryResponseAllOfNewDateValue**](StoryResponseAllOfNewDateValue.md) |  | [optional] 
**newDates** | [**StoryResponseDates**](StoryResponseDates.md) |  | [optional] 
**newEnumValue** | [**EnumOption**](EnumOption.md) |  | [optional] 
**newMultiEnumValues** | [**[EnumOption]**](EnumOption.md) | *Conditional*. The new value of a multi-enum custom field story. | [optional] [readonly] 
**newName** | **String** | *Conditional* | [optional] [readonly] 
**newNumberValue** | **Number** | *Conditional* | [optional] [readonly] 
**newPeopleValue** | [**[UserCompact]**](UserCompact.md) | *Conditional*. The new value of a people custom field story. | [optional] [readonly] 
**newResourceSubtype** | **String** | *Conditional* | [optional] [readonly] 
**newSection** | [**SectionCompact**](SectionCompact.md) |  | [optional] 
**newTextValue** | **String** | *Conditional* | [optional] [readonly] 
**numHearts** | **Number** | *Deprecated - please use likes instead*  *Conditional*. The number of users who have hearted this story. | [optional] [readonly] 
**numLikes** | **Number** | *Conditional*. The number of users who have liked this story. | [optional] [readonly] 
**oldApprovalStatus** | **String** | *Conditional*. The old value of approval status. | [optional] [readonly] 
**oldDateValue** | [**StoryResponseAllOfOldDateValue**](StoryResponseAllOfOldDateValue.md) |  | [optional] 
**oldDates** | [**StoryResponseDates**](StoryResponseDates.md) |  | [optional] 
**oldEnumValue** | [**EnumOption**](EnumOption.md) |  | [optional] 
**oldMultiEnumValues** | [**[EnumOption]**](EnumOption.md) | *Conditional*. The old value of a multi-enum custom field story. | [optional] [readonly] 
**oldName** | **String** | *Conditional*&#39; | [optional] 
**oldNumberValue** | **Number** | *Conditional* | [optional] [readonly] 
**oldPeopleValue** | [**[UserCompact]**](UserCompact.md) | *Conditional*. The old value of a people custom field story. | [optional] [readonly] 
**oldResourceSubtype** | **String** | *Conditional* | [optional] [readonly] 
**oldSection** | [**SectionCompact**](SectionCompact.md) |  | [optional] 
**oldTextValue** | **String** | *Conditional* | [optional] [readonly] 
**previews** | [**[Preview]**](Preview.md) | *Conditional*. A collection of previews to be displayed in the story.  *Note: This property only exists for comment stories.* | [optional] [readonly] 
**project** | [**ProjectCompact**](ProjectCompact.md) |  | [optional] 
**source** | **String** | The component of the Asana product the user used to trigger the story. | [optional] [readonly] 
**story** | [**StoryCompact**](StoryCompact.md) |  | [optional] 
**tag** | [**TagCompact**](TagCompact.md) |  | [optional] 
**target** | [**StoryResponseAllOfTarget**](StoryResponseAllOfTarget.md) |  | [optional] 
**task** | [**TaskCompact**](TaskCompact.md) |  | [optional] 
**type** | **String** |  | [optional] [readonly] 



## Enum: StickerNameEnum


* `green_checkmark` (value: `"green_checkmark"`)

* `people_dancing` (value: `"people_dancing"`)

* `dancing_unicorn` (value: `"dancing_unicorn"`)

* `heart` (value: `"heart"`)

* `party_popper` (value: `"party_popper"`)

* `people_waving_flags` (value: `"people_waving_flags"`)

* `splashing_narwhal` (value: `"splashing_narwhal"`)

* `trophy` (value: `"trophy"`)

* `yeti_riding_unicorn` (value: `"yeti_riding_unicorn"`)

* `celebrating_people` (value: `"celebrating_people"`)

* `determined_climbers` (value: `"determined_climbers"`)

* `phoenix_spreading_love` (value: `"phoenix_spreading_love"`)





## Enum: SourceEnum


* `web` (value: `"web"`)

* `email` (value: `"email"`)

* `mobile` (value: `"mobile"`)

* `api` (value: `"api"`)

* `unknown` (value: `"unknown"`)





## Enum: TypeEnum


* `comment` (value: `"comment"`)

* `system` (value: `"system"`)




