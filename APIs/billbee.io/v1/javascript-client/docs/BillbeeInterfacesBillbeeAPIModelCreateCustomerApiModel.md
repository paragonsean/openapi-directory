# BillbeeApi.BillbeeInterfacesBillbeeAPIModelCreateCustomerApiModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md) |  | [optional] 
**archivedAt** | **Date** | If set, the customer was already archived at the given date. Further modification is disabled. | [optional] 
**defaultCommercialMailAddress** | [**BillbeeInterfacesBillbeeAPIModelsCustomerMetaDataApiModel**](BillbeeInterfacesBillbeeAPIModelsCustomerMetaDataApiModel.md) |  | [optional] 
**defaultFax** | [**BillbeeInterfacesBillbeeAPIModelsCustomerMetaDataApiModel**](BillbeeInterfacesBillbeeAPIModelsCustomerMetaDataApiModel.md) |  | [optional] 
**defaultMailAddress** | [**BillbeeInterfacesBillbeeAPIModelsCustomerMetaDataApiModel**](BillbeeInterfacesBillbeeAPIModelsCustomerMetaDataApiModel.md) |  | [optional] 
**defaultPhone1** | [**BillbeeInterfacesBillbeeAPIModelsCustomerMetaDataApiModel**](BillbeeInterfacesBillbeeAPIModelsCustomerMetaDataApiModel.md) |  | [optional] 
**defaultPhone2** | [**BillbeeInterfacesBillbeeAPIModelsCustomerMetaDataApiModel**](BillbeeInterfacesBillbeeAPIModelsCustomerMetaDataApiModel.md) |  | [optional] 
**defaultStatusUpdatesMailAddress** | [**BillbeeInterfacesBillbeeAPIModelsCustomerMetaDataApiModel**](BillbeeInterfacesBillbeeAPIModelsCustomerMetaDataApiModel.md) |  | [optional] 
**email** | **String** |  | [optional] 
**id** | **Number** | The Billbee Id of the customer | [optional] 
**languageId** | **Number** |  | [optional] 
**metaData** | [**[BillbeeInterfacesBillbeeAPIModelsCustomerMetaDataApiModel]**](BillbeeInterfacesBillbeeAPIModelsCustomerMetaDataApiModel.md) |  | [optional] 
**name** | **String** |  | [optional] 
**number** | **Number** |  | [optional] 
**priceGroupId** | **Number** |  | [optional] 
**restoredAt** | **Date** | If set, the customer was restored from the archive at the given date. | [optional] 
**tel1** | **String** |  | [optional] 
**tel2** | **String** |  | [optional] 
**type** | **Number** | Customer Type | [optional] 
**vatId** | **String** | The vat-id, that should be saved at the customer. Only used if CustomerVatId is not set on the order. | [optional] 


