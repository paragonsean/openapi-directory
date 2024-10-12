

# FundDestination


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalData** | **Map&lt;String, String&gt;** | a map of name/value pairs for passing in additional/industry-specific data |  [optional] |
|**billingAddress** | [**Address**](Address.md) | The address where to send the invoice. |  [optional] |
|**card** | [**Card**](Card.md) | Credit card data.  Optional if &#x60;shopperReference&#x60; and &#x60;selectedRecurringDetailReference&#x60; are provided. |  [optional] |
|**selectedRecurringDetailReference** | **String** | The &#x60;recurringDetailReference&#x60; you want to use for this payment. The value &#x60;LATEST&#x60; can be used to select the most recently stored recurring detail. |  [optional] |
|**shopperEmail** | **String** | the email address of the person |  [optional] |
|**shopperName** | [**Name**](Name.md) | the name of the person |  [optional] |
|**shopperReference** | **String** | Required for recurring payments.  Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. &gt; Your reference must not include personally identifiable information (PII), for example name or email address. |  [optional] |
|**subMerchant** | [**SubMerchant**](SubMerchant.md) | Required for Back-to-Back/ purchase driven load in Wallet transactions. Contains the final merchant who will be receiving the money, also known as subMerchant, information. |  [optional] |
|**telephoneNumber** | **String** | the telephone number of the person |  [optional] |



