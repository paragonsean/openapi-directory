

# SendKeys

The Send Keys action simulates real user input of key by key into a given string. It mimics real user behavior, such as the inability to type into invisible or read-only DOM elements. This action is useful for cases where explicit keystroke events are required, like auto-completing combo boxes. Unlike a similar 'input' action, which forces a specified value directly into an input selector, this action does not overwrite existing content.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ignoreIfNotPresent** | **Boolean** |  |  [optional] |
|**selector** | **String** | Must be a valid CSS Selector |  [optional] |
|**value** | **String** | Sequence of keys to send. Keys can include keystrokes such as ALT+A, ENTER, BACKSPACE, etc. |  [optional] |



