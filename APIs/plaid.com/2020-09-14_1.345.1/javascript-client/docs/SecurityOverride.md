# ThePlaidApi.SecurityOverride

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **String** | Either a valid &#x60;iso_currency_code&#x60; or &#x60;unofficial_currency_code&#x60; | [optional] 
**cusip** | **String** | 9-character CUSIP, an identifier assigned to North American securities. Please note that Plaid&#39;s customers must hold a license directly from CUSIP Global Services to receive CUSIP &amp; ISIN data. This field will be null by default for new customers. For existing customers, this field will be null by default starting on Sept 15, 2023. If you would like access to this field, please contact your Plaid Account Manager or reach out to investments-vendors@plaid.com. | [optional] 
**isin** | **String** | 12-character ISIN, a globally unique securities identifier. Please note that Plaid&#39;s customers must hold a license directly from CUSIP Global Services to receive CUSIP &amp; ISIN data. This field will be null by default for new customers. For existing customers, this field will be null by default starting on Sept 15, 2023. If you would like access to this field, please contact your Plaid Account Manager or reach out to investments-vendors@plaid.com. | [optional] 
**name** | **String** | A descriptive name for the security, suitable for display. | [optional] 
**sedol** | **String** | 7-character SEDOL, an identifier assigned to securities in the UK. | [optional] 
**tickerSymbol** | **String** | The security’s trading symbol for publicly traded securities, and otherwise a short identifier if available. | [optional] 


