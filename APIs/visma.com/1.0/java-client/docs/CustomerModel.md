

# CustomerModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annualRevenue** | **Long** |  |  [optional] |
|**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**createdDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**currency** | [**CustomerCurrency**](CustomerCurrency.md) |  |  [optional] |
|**eInvoiceAddress** | **String** |  |  [optional] |
|**eInvoiceOperator** | **String** |  |  [optional] |
|**email** | **String** |  |  [optional] |
|**guid** | **String** |  |  [optional] [readonly] |
|**headquarterAddress** | [**CustomerHeadquarterAddress**](CustomerHeadquarterAddress.md) |  |  [optional] |
|**industry** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**invoiceTemplate** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**invoicingVat** | [**CustomerInvoicingVat**](CustomerInvoicingVat.md) |  |  [optional] |
|**isActive** | **Boolean** |  |  [optional] |
|**isInternal** | **Boolean** |  |  [optional] [readonly] |
|**kvkNumber** | **String** |  |  [optional] |
|**language** | [**CustomerLanguage**](CustomerLanguage.md) |  |  [optional] |
|**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**lastUpdatedDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**name** | **String** |  |  |
|**notes** | **String** |  |  [optional] |
|**number** | **Long** |  |  [optional] |
|**numberOfEmployees** | **Integer** |  |  [optional] |
|**overdueInterest** | **Double** |  |  [optional] |
|**owner** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**paymentTerm** | **Integer** |  |  [optional] |
|**pricelist** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**timezone** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**vatNumber** | **String** |  |  [optional] |
|**website** | **String** |  |  [optional] |



