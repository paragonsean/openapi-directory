

# CardWithId

A [card](https://developers.google.com/chat/api/reference/rest/v1/cards) in a Google Chat message. Only Chat apps can create cards. If your Chat app [authenticates as a user](https://developers.google.com/chat/api/guides/auth/users), the message can't contain cards. [Card builder](https://addons.gsuite.google.com/uikit/builder)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**card** | [**GoogleAppsCardV1Card**](GoogleAppsCardV1Card.md) |  |  [optional] |
|**cardId** | **String** | Required if the message contains multiple cards. A unique identifier for a card in a message. |  [optional] |



