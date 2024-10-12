

# CreateRefundIn


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **BigDecimal** | Amount (without tax) to be refunded. Either amount or total amount is required. In case of line key and custom id missing, only total_amount can be used. |  [optional] |
|**customId** | **String** | Line custom identifier. If neither line key or custom id is provided, the refund amount will be assigned to lines in order. |  [optional] |
|**lineKey** | **String** | Line identifier. If neither line key or custom id is provided, the refund amount will be assigned to lines in order. |  [optional] |
|**refundReason** | **String** | Refund reason, displayed on the credit note. |  [optional] |
|**totalAmount** | **BigDecimal** | Total amount, including tax, to be refunded. Either amount or total amount is required. In case of line key and custom id missing, only total_amount can be used. |  [optional] |



