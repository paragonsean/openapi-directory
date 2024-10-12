# BillbeeApi.BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autosubtractReservedAmount** | **Boolean** | Automatically reduce the NewQuantity by the currently not fulfilled amount | [optional] 
**billbeeId** | **Number** | Optional the ID of the Billbee product to update | [optional] 
**deltaQuantity** | **Number** | This parameter is currently ignored | [optional] 
**forceSendStockToShops** | **Boolean** | If true, every sent stockchange is stored and transmitted to the connected shop, even if the value has not changed | [optional] 
**newQuantity** | **Number** | The new absolute stock quantity for the product you want to set | [optional] 
**oldQuantity** | **Number** | This parameter is currently ignored | [optional] 
**reason** | **String** | Optional a reason text for the stock update | [optional] 
**sku** | **String** | The SKU of the product to update | [optional] 
**stockId** | **Number** | Optional the stock id if the feature multi stock is activated | [optional] 


