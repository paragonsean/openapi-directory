

# NotificationRequest159

Contains the details of the request message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalMessage** | **String** | Message a financial institution will associate to the transfer and may display |  [optional] |
|**mastercardAssignedId** | **String** | Mastercard Assigned ID for tiered interchange calculations. Length: 6. Applicable only for P2M and MRF notifications. |  [optional] |
|**merchantCategoryCode** | **String** | Merchant category code |  [optional] |
|**paymentFacilitatorId** | **String** | Contains the Payment Facilitator ID. Length: 11. Applicable only for P2M and MRF notifications. |  [optional] |
|**paymentType** | **String** | P2M: Person to Merchant, ACO: Agent Cash Out |  |
|**recipient** | [**Recipient161**](Recipient161.md) |  |  [optional] |
|**recipientAccountUri** | **String** | Recepient Account uri . Only accept format: pan:[16 digit] |  |
|**transactionAmount** | [**TransactionAmount160**](TransactionAmount160.md) |  |  [optional] |
|**transferStatus** | **String** | APPROVED or DECLINED |  |



