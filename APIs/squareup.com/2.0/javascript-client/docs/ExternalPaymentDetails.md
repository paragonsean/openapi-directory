# SquareConnectApi.ExternalPaymentDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **String** | A description of the external payment source. For example,  \&quot;Food Delivery Service\&quot;. | 
**sourceFeeMoney** | [**Money**](Money.md) |  | [optional] 
**sourceId** | **String** | An ID to associate the payment to its originating source. | [optional] 
**type** | **String** | The type of external payment the seller received. It can be one of the following: - CHECK - Paid using a physical check. - BANK_TRANSFER - Paid using external bank transfer. - OTHER\\_GIFT\\_CARD - Paid using a non-Square gift card. - CRYPTO - Paid using a crypto currency. - SQUARE_CASH - Paid using Square Cash App. - SOCIAL - Paid using peer-to-peer payment applications. - EXTERNAL - A third-party application gathered this payment outside of Square. - EMONEY - Paid using an E-money provider. - CARD - A credit or debit card that Square does not support. - STORED_BALANCE - Use for house accounts, store credit, and so forth. - FOOD_VOUCHER - Restaurant voucher provided by employers to employees to pay for meals - OTHER - A type not listed here. | 


