# SeveraPublicRestApiDocumentation.ProductOutputModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** |  | [optional] 
**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**createdDateTime** | **Date** |  | [optional] [readonly] 
**guid** | **String** |  | [optional] [readonly] 
**isActive** | **Boolean** |  | [optional] [default to true]
**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**lastUpdatedDateTime** | **Date** |  | [optional] [readonly] 
**measurementUnit** | **String** |  | [optional] 
**name** | **String** |  | 
**productCategory** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**proposalDescription** | **String** |  | [optional] 
**salesAccount** | [**ProductSalesAccountSubModel**](ProductSalesAccountSubModel.md) |  | [optional] 
**type** | [**ProductType**](ProductType.md) |  | [optional] 
**unitCost** | [**MoneyOutputModel**](MoneyOutputModel.md) |  | [optional] 
**unitPrice** | [**MoneyOutputModel**](MoneyOutputModel.md) |  | [optional] 
**vatRate** | **Number** |  | [optional] 


