

# ForceReply

Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice [privacy mode](/bots#privacy-mode).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**forceReply** | **Boolean** | Shows reply interface to the user, as if they manually selected the bot&#39;s message and tapped &#39;Reply&#39; |  |
|**selective** | **Boolean** | *Optional*. Use this parameter if you want to force reply from specific users only. Targets: 1) users that are @mentioned in the *text* of the [Message](https://core.telegram.org/bots/api/#message) object; 2) if the bot&#39;s message is a reply (has *reply\\_to\\_message\\_id*), sender of the original message. |  [optional] |



