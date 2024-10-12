

# LiveChatGiftMembershipReceivedDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**associatedMembershipGiftingMessageId** | **String** | The ID of the membership gifting message that is related to this gift membership. This ID will always refer to a message whose type is &#39;membershipGiftingEvent&#39;. |  [optional] |
|**gifterChannelId** | **String** | The ID of the user that made the membership gifting purchase. This matches the &#x60;snippet.authorChannelId&#x60; of the associated membership gifting message. |  [optional] |
|**memberLevelName** | **String** | The name of the Level at which the viewer is a member. This matches the &#x60;snippet.membershipGiftingDetails.giftMembershipsLevelName&#x60; of the associated membership gifting message. The Level names are defined by the YouTube channel offering the Membership. In some situations this field isn&#39;t filled. |  [optional] |



