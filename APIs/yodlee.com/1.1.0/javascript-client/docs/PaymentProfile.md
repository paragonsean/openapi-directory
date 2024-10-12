# YodleeCoreApis.PaymentProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**[AccountAddress]**](AccountAddress.md) | The address of the lender to which the monthly payments or the loan payoff amount should be paid. &lt;br&gt;&lt;b&gt;Additional Details:&lt;/b&gt;The address field applies only to the student loan account type.&lt;br&gt;&lt;b&gt;Account Type&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: loan&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;br&gt;&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**identifier** | [**PaymentIdentifier**](PaymentIdentifier.md) |  | [optional] 
**paymentBankTransferCode** | [**PaymentBankTransferCode**](PaymentBankTransferCode.md) |  | [optional] 


