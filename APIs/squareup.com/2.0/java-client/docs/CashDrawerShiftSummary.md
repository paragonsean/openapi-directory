

# CashDrawerShiftSummary

The summary of a closed cash drawer shift. This model contains only the money counted to start a cash drawer shift, counted at the end of the shift, and the amount that should be in the drawer at shift end based on summing all cash drawer shift events.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**closedAt** | **String** | The shift close time in ISO 8601 format. |  [optional] |
|**closedCashMoney** | [**Money**](Money.md) |  |  [optional] |
|**description** | **String** | An employee free-text description of a cash drawer shift. |  [optional] |
|**endedAt** | **String** | The shift end time in ISO 8601 format. |  [optional] |
|**expectedCashMoney** | [**Money**](Money.md) |  |  [optional] |
|**id** | **String** | The shift unique ID. |  [optional] |
|**openedAt** | **String** | The shift start time in ISO 8601 format. |  [optional] |
|**openedCashMoney** | [**Money**](Money.md) |  |  [optional] |
|**state** | **String** | The shift current state. |  [optional] |



