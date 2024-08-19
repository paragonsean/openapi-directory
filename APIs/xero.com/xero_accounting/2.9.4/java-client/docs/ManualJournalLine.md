

# ManualJournalLine


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountCode** | **String** | See Accounts |  [optional] |
|**accountID** | **UUID** | See Accounts |  [optional] |
|**description** | **String** | Description for journal line |  [optional] |
|**isBlank** | **Boolean** | is the line blank |  [optional] |
|**lineAmount** | **Double** | total for line. Debits are positive, credits are negative value |  [optional] |
|**taxAmount** | **Double** | The calculated tax amount based on the TaxType and LineAmount |  [optional] [readonly] |
|**taxType** | **String** | The tax type from TaxRates |  [optional] |
|**tracking** | [**List&lt;TrackingCategory&gt;**](TrackingCategory.md) | Optional Tracking Category – see Tracking. Any JournalLine can have a maximum of 2 &lt;TrackingCategory&gt; elements. |  [optional] |



