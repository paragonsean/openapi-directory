# AccountApi.InternationalReturnOverrideType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**returnMethod** | **String** | This field sets/indicates if the seller offers replacement items to the buyer in the case of an international return. The buyer must be willing to accept a replacement item; otherwise, the seller will need to issue a refund for a return. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/account/types/api:ReturnMethodEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**returnPeriod** | [**TimeDuration**](TimeDuration.md) |  | [optional] 
**returnShippingCostPayer** | **String** | This field indicates who is responsible for paying for the shipping charges for returned items. The field can be set to either &lt;code&gt;BUYER&lt;/code&gt; or &lt;code&gt;SELLER&lt;/code&gt;.  &lt;br/&gt;&lt;br/&gt;Depending on the return policy and specifics of the return, either the buyer or the seller can be responsible for the return shipping costs. Note that the seller is always responsible for return shipping costs for &#39;significantly not as described&#39; (SNAD) issues.  &lt;br/&gt;&lt;br/&gt;This field is conditionally required if the &lt;b&gt;internationalOverride.returnsAccepted&lt;/b&gt; field is set to &lt;code&gt;true&lt;/code&gt;. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/account/types/api:ReturnShippingCostPayerEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**returnsAccepted** | **Boolean** | If set to &lt;code&gt;true&lt;/code&gt;, the seller accepts international returns. If set to &lt;code&gt;false&lt;/code&gt;, the seller does not accept international returns.  &lt;br/&gt;&lt;br/&gt;This field is conditionally required if the seller chooses to have a separate international return policy. | [optional] 


