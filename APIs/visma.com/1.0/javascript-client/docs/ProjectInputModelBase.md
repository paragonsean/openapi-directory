# SeveraPublicRestApiDocumentation.ProjectInputModelBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingContact** | [**SimpleInputModel**](SimpleInputModel.md) |  | [optional] 
**businessUnit** | [**SimpleInputRequiredModel**](SimpleInputRequiredModel.md) |  | [optional] 
**completionEstimatePercentage** | **Number** |  | [optional] 
**costCenter** | [**SimpleInputModel**](SimpleInputModel.md) |  | [optional] 
**currency** | [**SimpleInputRequiredModel**](SimpleInputRequiredModel.md) |  | [optional] 
**customer** | [**SimpleInputRequiredModel**](SimpleInputRequiredModel.md) |  | 
**customerContact** | [**SimpleInputModel**](SimpleInputModel.md) |  | [optional] 
**deadline** | **Date** |  | [optional] 
**description** | **String** |  | [optional] 
**expectedOrderDate** | **Date** |  | [optional] 
**expectedValue** | [**MoneyInputModelWithNullableAmount**](MoneyInputModelWithNullableAmount.md) |  | [optional] 
**internalName** | **String** |  | [optional] 
**invoiceNotes** | **String** |  | [optional] 
**invoiceTemplate** | [**InvoiceTemplateSubModel**](InvoiceTemplateSubModel.md) |  | [optional] 
**isClosed** | **Boolean** |  | [optional] 
**isInternal** | **Boolean** |  | [optional] 
**isJoiningAllowed** | **Boolean** |  | [optional] [default to true]
**leadSource** | [**SimpleInputModel**](SimpleInputModel.md) |  | [optional] 
**name** | **String** |  | 
**number** | **Number** |  | [optional] 
**orderNumber** | **String** |  | [optional] 
**ourReference** | **String** |  | [optional] 
**paymentTerm** | **Number** |  | [optional] 
**probability** | **Number** |  | [optional] 
**projectOwner** | [**SimpleInputModel**](SimpleInputModel.md) |  | 
**projectStatus** | [**SimpleProjectStatusInputModel**](SimpleProjectStatusInputModel.md) |  | [optional] 
**salesPerson** | [**SimpleInputModel**](SimpleInputModel.md) |  | [optional] 
**salesStatus** | [**SimpleSalesStatusInputModel**](SimpleSalesStatusInputModel.md) |  | [optional] 
**startDate** | **Date** |  | [optional] 
**useOvertimeMultipliers** | **Boolean** |  | [optional] [default to true]
**useProductsFromSetting** | **Boolean** |  | [optional] [default to true]
**useWorktypesFromSetting** | **Boolean** |  | [optional] [default to true]
**yourReference** | **String** |  | [optional] 


