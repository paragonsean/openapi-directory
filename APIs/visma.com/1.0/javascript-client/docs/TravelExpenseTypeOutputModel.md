# SeveraPublicRestApiDocumentation.TravelExpenseTypeOutputModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** |  | [optional] 
**costAccount** | [**TravelExpenseCostAccountSubModel**](TravelExpenseCostAccountSubModel.md) |  | [optional] 
**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**createdDateTime** | **Date** |  | [optional] [readonly] 
**expenseClass** | [**ExpensesClass**](ExpensesClass.md) |  | [optional] 
**guid** | **String** |  | [optional] [readonly] 
**includeTime** | **Boolean** |  | [optional] 
**isActive** | **Boolean** |  | [optional] [default to true]
**isDailyAllowance** | **Boolean** |  | [optional] 
**isMileage** | **Boolean** |  | [optional] 
**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**lastUpdatedDateTime** | **Date** |  | [optional] [readonly] 
**measurementUnit** | **String** |  | [optional] 
**name** | **String** |  | 
**productCategory** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**purchaseVatRate** | **Number** |  | [optional] 
**salesAccount** | [**ProductSalesAccountSubModel2**](ProductSalesAccountSubModel2.md) |  | [optional] 
**unitCost** | [**MoneyOutputModel**](MoneyOutputModel.md) |  | [optional] 
**vatRate** | **Number** |  | [optional] 


