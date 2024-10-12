

# RuntimeHints

<p>You can provide Amazon Lex with hints to the phrases that a customer is likely to use for a slot. When a slot with hints is resolved, the phrases in the runtime hints are preferred in the resolution. You can provide hints for a maximum of 100 intents. You can provide a maximum of 100 slots.</p> <p>Before you can use runtime hints with an existing bot, you must first rebuild the bot.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/using-hints.html\">Using runtime hints to improve recognition of slot values</a>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**slotHints** | [**Map**](Map.md) |  |  [optional] |



