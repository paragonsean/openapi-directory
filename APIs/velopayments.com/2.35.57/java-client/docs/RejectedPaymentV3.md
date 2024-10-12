

# RejectedPaymentV3


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | The amount of the payment in minor units |  |
|**currencyType** | **String** | Valid ISO 4217 3 letter currency code. See the &lt;a href&#x3D;\&quot;https://www.iso.org/iso-4217-currency-codes.html\&quot; target&#x3D;\&quot;_blank\&quot; a&gt;ISO specification&lt;/a&gt; for details. |  |
|**lineNumber** | **Integer** | If the payment was submitted in a csv payout then this will be the line number of the payment in the file |  [optional] |
|**message** | **String** | A more general rejection message than the reason property |  [optional] |
|**paymentMetadata** | **String** | &lt;p&gt;Metadata about the payment that may be relevant to the specific rails or remote system making the payout&lt;/p&gt; &lt;p&gt;The structure of the data will be dictated by the requirements of the payment rails&lt;/p&gt;  |  [optional] |
|**payorPaymentId** | **String** | A reference identifier for the payor for the given payee payment |  |
|**reason** | **String** | The reason for the payment being rejected |  |
|**reasonCode** | **String** | The reason code as determined by Velo |  [optional] |
|**remoteId** | **String** | The remoteId supplied by the payor that identifies the payee |  |
|**remoteSystemId** | **String** | &lt;p&gt;The identifier for the remote payments system if not Velo&lt;/p&gt;  |  [optional] |
|**sourceAccountName** | **String** | The identifier of the source account to debit the payment from |  |



