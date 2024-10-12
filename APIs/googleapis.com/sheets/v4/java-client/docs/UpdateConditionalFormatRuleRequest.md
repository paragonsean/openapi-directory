

# UpdateConditionalFormatRuleRequest

Updates a conditional format rule at the given index, or moves a conditional format rule to another index.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**index** | **Integer** | The zero-based index of the rule that should be replaced or moved. |  [optional] |
|**newIndex** | **Integer** | The zero-based new index the rule should end up at. |  [optional] |
|**rule** | [**ConditionalFormatRule**](ConditionalFormatRule.md) |  |  [optional] |
|**sheetId** | **Integer** | The sheet of the rule to move. Required if new_index is set, unused otherwise. |  [optional] |



