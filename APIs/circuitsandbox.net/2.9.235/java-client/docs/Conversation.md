

# Conversation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**avatar** | **String** | The URL of the small avatar image of the conversation |  [optional] |
|**avatarLarge** | **String** | The URL of the large avatar image of the conversation |  [optional] |
|**convId** | **String** | The ID of the conversation |  [optional] |
|**creationTime** | **BigDecimal** | UTC timestamp when the conversation was created |  [optional] |
|**creatorId** | **String** | The ID of the user who created the conversation |  [optional] |
|**creatorTenantId** | **String** | The ID of the Circuit domain (tenant) where the creator of the conversation belongs to |  [optional] |
|**description** | **String** | The description of the conversation. This field is available only for conversations with type COMMUNITY |  [optional] |
|**isGuestAccessDisabled** | **Boolean** | Indicates whether guest access to the conversation is disabled or not |  [optional] |
|**isModerated** | **Boolean** | Indicates whether the conversation is moderated or not. In a moderated conversation only participants who have been assigned the role of a moderator are allowed to add or remove participants into the conversation |  [optional] |
|**modificationTime** | **BigDecimal** | UTC timestamp when the conversation was modified. A conversation is modified when any of the conversation object fields change but not when conversation items are added or edited |  [optional] |
|**participants** | **List&lt;String&gt;** | Array of active participants |  [optional] |
|**topic** | **String** | The title of the conversation. Conversations of type DIRECT cannot have a title |  [optional] |
|**topicPlaceholder** | **String** | The title of the conversation. Conversations of type DIRECT cannot have a title |  [optional] |
|**type** | **String** | The type of the conversation. It can be one of the following: DIRECT, GROUP, COMMUNITY or LARGE |  [optional] |



