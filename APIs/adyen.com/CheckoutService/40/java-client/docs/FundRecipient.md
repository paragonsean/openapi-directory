

# FundRecipient


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAddress** | [**Address**](Address.md) | The address where to send the invoice. |  [optional] |
|**paymentMethod** | [**CardDetails**](CardDetails.md) | the used paymentMetohd |  [optional] |
|**shopperEmail** | **String** | the email address of the person |  [optional] |
|**shopperName** | [**Name**](Name.md) | the name of the person |  [optional] |
|**shopperReference** | **String** | Required for recurring payments.  Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. &gt; Your reference must not include personally identifiable information (PII), for example name or email address. |  [optional] |
|**storedPaymentMethodId** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**subMerchant** | [**SubMerchant**](SubMerchant.md) | Required for Back-to-Back/ purchase driven load in Wallet transactions. Contains the final merchant who will be receiving the money, also known as subMerchant, information. |  [optional] |
|**telephoneNumber** | **String** | the telephone number of the person |  [optional] |
|**walletIdentifier** | **String** | indicates where the money is going |  [optional] |
|**walletOwnerTaxId** | **String** | indicates the tax identifier of the fund recepient |  [optional] |



