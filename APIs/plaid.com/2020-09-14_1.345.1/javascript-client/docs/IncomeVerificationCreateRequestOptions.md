# ThePlaidApi.IncomeVerificationCreateRequestOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessTokens** | **[String]** | An array of access tokens corresponding to the Items that will be cross-referenced with the product data. Plaid will attempt to correlate transaction history from these Items with data from the user&#39;s paystub, such as date and amount. The &#x60;verification&#x60; status of the paystub as returned by &#x60;/income/verification/paystubs/get&#x60; will indicate if the verification status was successful, or, if not, why it failed. If the &#x60;transactions&#x60; product was not initialized for the Items during Link, it will be initialized after this Link session. | [optional] 


