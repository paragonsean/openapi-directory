

# UserSettings


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountantEmail** | **String** |  |  [optional] |
|**address** | **String** |  |  [optional] |
|**apiKey** | **String** |  |  [optional] |
|**apiSecret** | **String** |  |  [optional] |
|**backgroundImage** | **String** |  |  [optional] |
|**bank** | **String** |  |  [optional] |
|**bankAccount** | **String** |  |  [optional] |
|**cname** | **String** |  |  [optional] |
|**companyRegistrationNumber** | **String** |  |  [optional] |
|**country** | [**Country**](Country.md) |  |  [optional] |
|**countryId** | **Integer** |  |  [optional] |
|**currency** | [**Currency**](Currency.md) |  |  [optional] |
|**currencyId** | **Integer** |  |  [optional] |
|**currencySymbol** | **String** |  |  [optional] |
|**defaultDateFormat** | **String** |  |  [optional] |
|**defaultDueDateInDays** | **Integer** |  |  [optional] |
|**doNotTrack** | **Boolean** |  |  [optional] |
|**enableClientPortal** | **Boolean** |  |  [optional] |
|**enablePredictiveInvoicing** | **Boolean** |  |  [optional] |
|**enableRecurringInvoicing** | **Boolean** |  |  [optional] |
|**hasInvoiceLogo** | **Boolean** |  |  [optional] |
|**iban** | **String** |  |  [optional] |
|**id** | **Integer** |  |  [optional] |
|**invoiceTemplate** | [**InvoiceTemplateEnum**](#InvoiceTemplateEnum) |  |  [optional] |
|**invoiceTemplateColorHex** | **String** |  |  [optional] |
|**phoneNumber** | **String** |  |  [optional] |
|**profession** | [**ProfessionEnum**](#ProfessionEnum) |  |  [optional] |
|**receiveSmsNotifications** | **Boolean** |  |  [optional] |
|**referralProgram** | [**ReferralProgramEnum**](#ReferralProgramEnum) |  |  [optional] |
|**storeCheckoutFields** | [**StoreCheckoutFieldsEnum**](#StoreCheckoutFieldsEnum) |  |  [optional] |
|**storeColorHex** | **String** |  |  [optional] |
|**storeCurrency** | [**Currency**](Currency.md) |  |  [optional] |
|**storeCurrencyId** | **Integer** |  |  [optional] |
|**storeCustomJavaScript** | **String** |  |  [optional] |
|**storeDescription** | **String** |  |  [optional] |
|**storeEmail** | **String** |  |  [optional] |
|**storeLanguage** | [**UiLanguage**](UiLanguage.md) |  |  [optional] |
|**storeLanguageId** | **Integer** |  |  [optional] |
|**storeName** | **String** |  |  [optional] |
|**storePurchaseEmailMessage** | **String** |  |  [optional] |
|**storePurchaseThankYouMessage** | **String** |  |  [optional] |
|**storeTextColorHex** | **String** |  |  [optional] |
|**storeUrl** | **String** |  |  [optional] |
|**subscribeToProductEmails** | **Boolean** |  |  [optional] |
|**swift** | **String** |  |  [optional] |
|**terms** | **String** |  |  [optional] |
|**userId** | **Integer** |  |  [optional] |
|**userSignature** | **String** |  |  [optional] |
|**vatNumber** | **String** |  |  [optional] |
|**yearsOfExperience** | **Integer** |  |  [optional] |



## Enum: InvoiceTemplateEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;Default&quot; |
| TEMPLATE1 | &quot;Template1&quot; |
| TEMPLATE2 | &quot;Template2&quot; |



## Enum: ProfessionEnum

| Name | Value |
|---- | -----|
| OTHER | &quot;Other&quot; |
| DESIGN_AND_CREATIVE | &quot;DesignAndCreative&quot; |
| SOFTWARE_DEVELOPMENT | &quot;SoftwareDevelopment&quot; |
| CONTENT_WRITING_AND_MARKETING | &quot;ContentWritingAndMarketing&quot; |
| FREELANCERS | &quot;Freelancers&quot; |
| CONSULTANTS | &quot;Consultants&quot; |
| SMES | &quot;Smes&quot; |
| ENTERPRISE | &quot;Enterprise&quot; |
| E_COMMERCE | &quot;ECommerce&quot; |
| INDIVIDUAL | &quot;Individual&quot; |



## Enum: ReferralProgramEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: StoreCheckoutFieldsEnum

| Name | Value |
|---- | -----|
| SHOW_MINIMUM_REQUIRED_FIELDS | &quot;ShowMinimumRequiredFields&quot; |
| SHOW_ALL_FIELDS | &quot;ShowAllFields&quot; |



