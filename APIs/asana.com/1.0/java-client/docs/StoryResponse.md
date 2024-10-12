

# StoryResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gid** | **String** | Globally unique identifier of the resource, as a string. |  [optional] [readonly] |
|**resourceType** | **String** | The base type of this resource. |  [optional] [readonly] |
|**createdAt** | **OffsetDateTime** | The time at which this resource was created. |  [optional] [readonly] |
|**htmlText** | **String** | [Opt In](/docs/input-output-options). HTML formatted text for a comment. This will not include the name of the creator. |  [optional] |
|**isPinned** | **Boolean** | *Conditional*. Whether the story should be pinned on the resource. |  [optional] |
|**resourceSubtype** | **String** | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. |  [optional] [readonly] |
|**stickerName** | [**StickerNameEnum**](#StickerNameEnum) | The name of the sticker in this story. &#x60;null&#x60; if there is no sticker. |  [optional] |
|**text** | **String** | The plain text of the comment to add. Cannot be used with html_text. |  [optional] |
|**assignee** | [**UserCompact**](UserCompact.md) |  |  [optional] |
|**createdBy** | [**UserCompact**](UserCompact.md) |  |  [optional] |
|**customField** | [**CustomFieldCompact**](CustomFieldCompact.md) |  |  [optional] |
|**dependency** | [**TaskCompact**](TaskCompact.md) |  |  [optional] |
|**duplicateOf** | [**TaskCompact**](TaskCompact.md) |  |  [optional] |
|**duplicatedFrom** | [**TaskCompact**](TaskCompact.md) |  |  [optional] |
|**follower** | [**UserCompact**](UserCompact.md) |  |  [optional] |
|**hearted** | **Boolean** | *Deprecated - please use likes instead* *Conditional*. True if the story is hearted by the authorized user, false if not. |  [optional] [readonly] |
|**hearts** | [**List&lt;Like&gt;**](Like.md) | *Deprecated - please use likes instead*  *Conditional*. Array of likes for users who have hearted this story. |  [optional] [readonly] |
|**isEditable** | **Boolean** | *Conditional*. Whether the text of the story can be edited after creation. |  [optional] [readonly] |
|**isEdited** | **Boolean** | *Conditional*. Whether the text of the story has been edited after creation. |  [optional] [readonly] |
|**liked** | **Boolean** | *Conditional*. True if the story is liked by the authorized user, false if not. |  [optional] [readonly] |
|**likes** | [**List&lt;Like&gt;**](Like.md) | *Conditional*. Array of likes for users who have liked this story. |  [optional] [readonly] |
|**newApprovalStatus** | **String** | *Conditional*. The new value of approval status. |  [optional] [readonly] |
|**newDateValue** | [**StoryResponseAllOfNewDateValue**](StoryResponseAllOfNewDateValue.md) |  |  [optional] |
|**newDates** | [**StoryResponseDates**](StoryResponseDates.md) |  |  [optional] |
|**newEnumValue** | [**EnumOption**](EnumOption.md) |  |  [optional] |
|**newMultiEnumValues** | [**List&lt;EnumOption&gt;**](EnumOption.md) | *Conditional*. The new value of a multi-enum custom field story. |  [optional] [readonly] |
|**newName** | **String** | *Conditional* |  [optional] [readonly] |
|**newNumberValue** | **Integer** | *Conditional* |  [optional] [readonly] |
|**newPeopleValue** | [**List&lt;UserCompact&gt;**](UserCompact.md) | *Conditional*. The new value of a people custom field story. |  [optional] [readonly] |
|**newResourceSubtype** | **String** | *Conditional* |  [optional] [readonly] |
|**newSection** | [**SectionCompact**](SectionCompact.md) |  |  [optional] |
|**newTextValue** | **String** | *Conditional* |  [optional] [readonly] |
|**numHearts** | **Integer** | *Deprecated - please use likes instead*  *Conditional*. The number of users who have hearted this story. |  [optional] [readonly] |
|**numLikes** | **Integer** | *Conditional*. The number of users who have liked this story. |  [optional] [readonly] |
|**oldApprovalStatus** | **String** | *Conditional*. The old value of approval status. |  [optional] [readonly] |
|**oldDateValue** | [**StoryResponseAllOfOldDateValue**](StoryResponseAllOfOldDateValue.md) |  |  [optional] |
|**oldDates** | [**StoryResponseDates**](StoryResponseDates.md) |  |  [optional] |
|**oldEnumValue** | [**EnumOption**](EnumOption.md) |  |  [optional] |
|**oldMultiEnumValues** | [**List&lt;EnumOption&gt;**](EnumOption.md) | *Conditional*. The old value of a multi-enum custom field story. |  [optional] [readonly] |
|**oldName** | **String** | *Conditional*&#39; |  [optional] |
|**oldNumberValue** | **Integer** | *Conditional* |  [optional] [readonly] |
|**oldPeopleValue** | [**List&lt;UserCompact&gt;**](UserCompact.md) | *Conditional*. The old value of a people custom field story. |  [optional] [readonly] |
|**oldResourceSubtype** | **String** | *Conditional* |  [optional] [readonly] |
|**oldSection** | [**SectionCompact**](SectionCompact.md) |  |  [optional] |
|**oldTextValue** | **String** | *Conditional* |  [optional] [readonly] |
|**previews** | [**List&lt;Preview&gt;**](Preview.md) | *Conditional*. A collection of previews to be displayed in the story.  *Note: This property only exists for comment stories.* |  [optional] [readonly] |
|**project** | [**ProjectCompact**](ProjectCompact.md) |  |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) | The component of the Asana product the user used to trigger the story. |  [optional] [readonly] |
|**story** | [**StoryCompact**](StoryCompact.md) |  |  [optional] |
|**tag** | [**TagCompact**](TagCompact.md) |  |  [optional] |
|**target** | [**StoryResponseAllOfTarget**](StoryResponseAllOfTarget.md) |  |  [optional] |
|**task** | [**TaskCompact**](TaskCompact.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] [readonly] |



## Enum: StickerNameEnum

| Name | Value |
|---- | -----|
| GREEN_CHECKMARK | &quot;green_checkmark&quot; |
| PEOPLE_DANCING | &quot;people_dancing&quot; |
| DANCING_UNICORN | &quot;dancing_unicorn&quot; |
| HEART | &quot;heart&quot; |
| PARTY_POPPER | &quot;party_popper&quot; |
| PEOPLE_WAVING_FLAGS | &quot;people_waving_flags&quot; |
| SPLASHING_NARWHAL | &quot;splashing_narwhal&quot; |
| TROPHY | &quot;trophy&quot; |
| YETI_RIDING_UNICORN | &quot;yeti_riding_unicorn&quot; |
| CELEBRATING_PEOPLE | &quot;celebrating_people&quot; |
| DETERMINED_CLIMBERS | &quot;determined_climbers&quot; |
| PHOENIX_SPREADING_LOVE | &quot;phoenix_spreading_love&quot; |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| WEB | &quot;web&quot; |
| EMAIL | &quot;email&quot; |
| MOBILE | &quot;mobile&quot; |
| API | &quot;api&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| COMMENT | &quot;comment&quot; |
| SYSTEM | &quot;system&quot; |



