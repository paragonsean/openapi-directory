

# DialogAction

Describes the next action that the bot should take in its interaction with the user and provides information about the context in which the action takes place. Use the <code>DialogAction</code> data type to set the interaction to a specific state, or to return the interaction to a previous state.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**DialogActionType**](DialogActionType.md) |  |  |
|**intentName** | [**String**](String.md) |  |  [optional] |
|**slots** | [**Map**](Map.md) |  |  [optional] |
|**slotToElicit** | [**String**](String.md) |  |  [optional] |
|**fulfillmentState** | [**FulfillmentState**](FulfillmentState.md) |  |  [optional] |
|**message** | [**String**](String.md) |  |  [optional] |
|**messageFormat** | [**MessageFormatType**](MessageFormatType.md) |  |  [optional] |



