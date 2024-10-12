# ThePlaidApi.ProductStatusBreakdown

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorInstitution** | **Number** | The percentage of logins that are failing due to an issue in the institution&#39;s system, expressed as a decimal. | 
**errorPlaid** | **Number** | The percentage of logins that are failing due to an internal Plaid issue, expressed as a decimal.  | 
**refreshInterval** | **String** | The &#x60;refresh_interval&#x60; may be &#x60;DELAYED&#x60; or &#x60;STOPPED&#x60; even when the success rate is high. This value is only returned for Transactions status breakdowns. | [optional] 
**success** | **Number** | The percentage of login attempts that are successful, expressed as a decimal. | 



## Enum: RefreshIntervalEnum


* `NORMAL` (value: `"NORMAL"`)

* `DELAYED` (value: `"DELAYED"`)

* `STOPPED` (value: `"STOPPED"`)




