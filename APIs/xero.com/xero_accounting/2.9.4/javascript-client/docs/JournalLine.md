# XeroAccountingApi.JournalLine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountCode** | **String** | See Accounts | [optional] 
**accountID** | **String** | See Accounts | [optional] 
**accountName** | **String** | See AccountCodes | [optional] 
**accountType** | [**AccountType**](AccountType.md) |  | [optional] 
**description** | **String** | The description from the source transaction line item. Only returned if populated. | [optional] 
**grossAmount** | **Number** | Gross amount of journal line (NetAmount + TaxAmount). | [optional] 
**journalLineID** | **String** | Xero identifier for Journal | [optional] 
**netAmount** | **Number** | Net amount of journal line. This will be a positive value for a debit and negative for a credit | [optional] 
**taxAmount** | **Number** | Total tax on a journal line | [optional] [readonly] 
**taxName** | **String** | see TaxRates | [optional] 
**taxType** | **String** | The tax type from TaxRates | [optional] 
**trackingCategories** | [**[TrackingCategory]**](TrackingCategory.md) | Optional Tracking Category – see Tracking. Any JournalLine can have a maximum of 2 &lt;TrackingCategory&gt; elements. | [optional] 


