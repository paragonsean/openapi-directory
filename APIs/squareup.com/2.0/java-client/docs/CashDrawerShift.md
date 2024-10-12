

# CashDrawerShift

This model gives the details of a cash drawer shift. The cash_payment_money, cash_refund_money, cash_paid_in_money, and cash_paid_out_money fields are all computed by summing their respective event types.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cashPaidInMoney** | [**Money**](Money.md) |  |  [optional] |
|**cashPaidOutMoney** | [**Money**](Money.md) |  |  [optional] |
|**cashPaymentMoney** | [**Money**](Money.md) |  |  [optional] |
|**cashRefundsMoney** | [**Money**](Money.md) |  |  [optional] |
|**closedAt** | **String** | The time when the shift was closed, in ISO 8601 format. |  [optional] |
|**closedCashMoney** | [**Money**](Money.md) |  |  [optional] |
|**closingEmployeeId** | **String** | The ID of the employee that closed the cash drawer shift by auditing the cash drawer contents. |  [optional] |
|**description** | **String** | The free-form text description of a cash drawer by an employee. |  [optional] |
|**device** | [**CashDrawerDevice**](CashDrawerDevice.md) |  |  [optional] |
|**employeeIds** | **List&lt;String&gt;** | The IDs of all employees that were logged into Square Point of Sale at any point while the cash drawer shift was open. |  [optional] |
|**endedAt** | **String** | The time when the shift ended, in ISO 8601 format. |  [optional] |
|**endingEmployeeId** | **String** | The ID of the employee that ended the cash drawer shift. |  [optional] |
|**expectedCashMoney** | [**Money**](Money.md) |  |  [optional] |
|**id** | **String** | The shift unique ID. |  [optional] |
|**openedAt** | **String** | The time when the shift began, in ISO 8601 format. |  [optional] |
|**openedCashMoney** | [**Money**](Money.md) |  |  [optional] |
|**openingEmployeeId** | **String** | The ID of the employee that started the cash drawer shift. |  [optional] |
|**state** | **String** | The shift current state. |  [optional] |



