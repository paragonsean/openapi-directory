

# PostInstructFxInfo

FX details relating to a payout that was executed or is still waiting to be executed

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fxMode** | **String** | The mode by which the FX rate is to be determined (MANUAL or AUTO) |  |
|**fxStatus** | **String** | The state to which the Post-Instruct FX process has reached (INITIATED or COMPLETED) |  |
|**fxStatusUpdatedAt** | **OffsetDateTime** | The date-time at which the most recent fxStatus was determined. |  |
|**fxTransactionReference** | **String** | The reference assigned to the FX funding that will fulfil this payment. |  [optional] |



