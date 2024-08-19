

# OrganizationSettingsModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currencyRoundingType** | **TotalRoundingType** |  |  [optional] |
|**defaultFooterColumn1** | [**FreeTextModel**](FreeTextModel.md) |  |  [optional] |
|**defaultFooterColumn2** | [**FreeTextModel**](FreeTextModel.md) |  |  [optional] |
|**defaultFooterColumn3** | [**FreeTextModel**](FreeTextModel.md) |  |  [optional] |
|**displayProjectNumber** | **Boolean** |  |  [optional] |
|**flextimeCalculationStartDate** | **LocalDate** |  |  [optional] |
|**isAddingNewKeywordsFromProjectAllowed** | **Boolean** |  |  [optional] |
|**isCustomerSearchAllowed** | **Boolean** |  |  [optional] |
|**isEnteringHourPlannedInvoiceQuantityAllowed** | **Boolean** |  |  [optional] |
|**isIdenticalPhaseCodesAllowed** | **Boolean** |  |  [optional] |
|**isTravelExpenseImmediatelyInvoiceable** | **Boolean** |  |  [optional] |
|**isWorkHourDescriptionMandatory** | **Boolean** |  |  [optional] |
|**lastCustomerNumber** | **Long** |  |  [optional] [readonly] |
|**lastFlextimeCalculationEndTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**lastFlextimeCalculationUser** | [**UserWithFirstNameLastNameModel**](UserWithFirstNameLastNameModel.md) |  |  [optional] |
|**lastInvoiceNumber** | **Long** |  |  [optional] [readonly] |
|**lastProjectNumber** | **Long** |  |  [optional] [readonly] |
|**lastPurchaseOrderNumber** | **Long** |  |  [optional] [readonly] |
|**lastTravelReimbursementNumber** | **Long** |  |  [optional] [readonly] |
|**maxFlextimeBalanceLimit** | **Double** |  |  [optional] |
|**minFlextimeBalanceLimit** | **Double** |  |  [optional] |
|**nextCustomerNumber** | **Long** |  |  [optional] |
|**nextInvoiceNumber** | **Integer** |  |  [optional] |
|**nextProjectNumber** | **Long** |  |  [optional] |
|**nextPurchaseOrderNumber** | **Integer** |  |  [optional] |
|**nextTravelReimbursementNumber** | **Integer** |  |  [optional] |
|**overdueInterest** | **Double** |  |  [optional] |
|**paymentReferenceNumberDisplaySetting** | **ReferenceNumberDisplay** |  |  [optional] |
|**paymentTerm** | **Integer** |  |  [optional] [readonly] |
|**projectNameDisplayFormatSetting** | **ProjectNameDisplayFormatOptions** |  |  [optional] |
|**projectNameDisplaySetting** | **ProjectNameDisplayOptions** |  |  [optional] |
|**purchaseOrderNumberPrefix** | **String** |  |  [optional] |
|**quickSearchSetting** | **QuickSearchOptions** |  |  [optional] |
|**setCreditNoteInvoiceNumber** | **Boolean** |  |  [optional] |
|**travelEntryClosingDate** | **LocalDate** |  |  [optional] |
|**travelExpenseReimbursementStartDate** | **LocalDate** |  |  [optional] |
|**travelReimbursementInstructions** | **String** |  |  [optional] [readonly] |
|**uniqueIdentifierForProductsAndWorktypes** | **Boolean** |  |  [optional] |
|**workHourApprovalMode** | **WorkHourApprovalMode** |  |  [optional] |
|**workHourEntryFormat** | **EntryFormat** |  |  [optional] |
|**workWeek** | **List&lt;Workweek&gt;** |  |  |
|**worktimeEntryClosingDate** | **LocalDate** |  |  [optional] |



