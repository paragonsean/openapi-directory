

# ProposalOutputModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAddress** | [**ProposalBillingAddressSubModel**](ProposalBillingAddressSubModel.md) |  |  [optional] |
|**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**createdDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**culture** | [**FormattingCultureSubModel**](FormattingCultureSubModel.md) |  |  [optional] |
|**customer** | [**ProposalCustomerSubModel**](ProposalCustomerSubModel.md) |  |  [optional] |
|**customerContactPerson** | [**CustomerContactPersonSubModel**](CustomerContactPersonSubModel.md) |  |  [optional] |
|**freeText1** | [**FreeTextModel2**](FreeTextModel2.md) |  |  [optional] |
|**freeText2** | [**FreeTextModel2**](FreeTextModel2.md) |  |  [optional] |
|**guid** | **String** |  |  [optional] [readonly] |
|**language** | [**ProposalLanguageSubModel**](ProposalLanguageSubModel.md) |  |  [optional] |
|**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**lastUpdatedDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**name** | **String** |  |  [optional] |
|**number** | **String** |  |  [optional] |
|**pricelist** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**project** | [**ProposalProjectSubModel**](ProposalProjectSubModel.md) |  |  [optional] |
|**proposalDate** | **LocalDate** |  |  [optional] |
|**proposalStatus** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**totalExcludingVat** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**totalIncludingVat** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |



