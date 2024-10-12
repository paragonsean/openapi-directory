

# DealerDBModelsVoucher

A voucher for EDT activation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdDate** | **OffsetDateTime** | Read-Only. The date the voucher was created. |  [optional] |
|**dealerCode** | **String** | The dealer code the voucher is assigned to.  Required for commercial and right to repair vouchers. |  [optional] |
|**deleted** | **Boolean** | Read-Only. True if voucher has been deleted. |  [optional] |
|**email** | **String** | Required for internal vouchers. |  [optional] |
|**expirationDate** | **OffsetDateTime** | The expiration date of the voucher. Required for Temporary and Right to Repair Vouchers. |  [optional] |
|**licenseTo** | **String** | Required for Internal Vouchers |  [optional] |
|**modifiedBy** | **String** | Read-Only. The user that made the last modification to the voucher. |  [optional] |
|**orderNumber** | **String** | The order number of a license. Required for Commercial and Right To Repair Vouchers. Not supported for other Vouchers. |  [optional] |
|**punched** | **Boolean** | True if voucher has aleady been used.  False if the voucher has not been used. |  [optional] |
|**punchedDate** | **OffsetDateTime** | Read-Only. The date the voucher was punched. |  [optional] |
|**purpose** | **String** | Required for Internal Vouchers. Not supported for other Vouchers. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of voucher. Commercial is the default if not specified. |  [optional] |
|**voucherCode** | **String** | The voucher code. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| COMMERCIAL | &quot;Commercial&quot; |
| INTERNAL | &quot;Internal&quot; |
| TEMPORARY | &quot;Temporary&quot; |
| RIGHT_TO_REPAIR | &quot;RightToRepair&quot; |



