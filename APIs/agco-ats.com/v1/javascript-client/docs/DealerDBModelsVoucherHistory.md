# AgcoApi.DealerDBModelsVoucherHistory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changedDate** | **Date** |  | [optional] 
**createdDate** | **Date** | Read-Only. The date the voucher was created. | [optional] 
**dealerCode** | **String** | The dealer code the voucher is assigned to.  Required for commercial vouchers. | [optional] 
**deleted** | **Boolean** | Read-Only. True if voucher has been deleted. | [optional] 
**email** | **String** | The email address. Required for Internal Vouchers | [optional] 
**expirationDate** | **Date** | The expiration date of the voucher. Required for Temporary Vouchers. | [optional] 
**ID** | **Number** | The id of the voucher history item | [optional] 
**licenseTo** | **String** | Required for Internal Vouchers | [optional] 
**modifiedBy** | **String** | Read-Only. The user that made the last modification to the voucher. | [optional] 
**orderNumber** | **String** | The order number of a commercial license. Required for Commercial Vouchers. Not supported for other Vouchers. | [optional] 
**punched** | **Boolean** | True if voucher has aleady been used.  False if the voucher has not been used. | [optional] 
**punchedDate** | **Date** | Read-Only. The date the voucher was punched. | [optional] 
**purpose** | **String** | Required for Internal Vouchers | [optional] 
**type** | **String** | The type of voucher. | [optional] 
**voucherCode** | **String** | The voucher code. | [optional] 



## Enum: TypeEnum


* `Commercial` (value: `"Commercial"`)

* `Internal` (value: `"Internal"`)

* `Temporary` (value: `"Temporary"`)

* `RightToRepair` (value: `"RightToRepair"`)




