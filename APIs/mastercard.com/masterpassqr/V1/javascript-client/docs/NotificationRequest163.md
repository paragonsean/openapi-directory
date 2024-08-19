# SendPersonToMerchant.NotificationRequest163

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalMessage** | **String** | Message a financial institution will associate to the transfer and may display | [optional] 
**mastercardAssignedId** | **String** | Mastercard Assigned ID for tiered interchange calculations. Length: 6. Applicable only for P2M and MRF notifications.  | [optional] 
**merchantCategoryCode** | **String** | Merchant category code | [optional] 
**paymentFacilitatorId** | **String** | Contains the Payment Facilitator ID. Length: 11. Applicable only for P2M and MRF notifications. | [optional] 
**paymentType** | **String** | MRF: Merchant Refund | 
**recipient** | [**Recipient165**](Recipient165.md) |  | [optional] 
**recipientAccountUri** | **String** | Recepient Account uri . Only accept format: pan:[16 digit] | 
**transactionAmount** | [**TransactionAmount164**](TransactionAmount164.md) |  | [optional] 
**transferStatus** | **String** | APPROVED or DECLINED | 


