

# PaymentPolicy

This type is used by the <b>paymentPolicy</b> response container, a container which defines a seller's payment business policy for a specific marketplace.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categoryTypes** | [**List&lt;CategoryType&gt;**](CategoryType.md) | This container indicates whether the fulfillment policy applies to motor vehicle listings, or if it applies to non-motor vehicle listings. |  [optional] |
|**deposit** | [**Deposit**](Deposit.md) |  |  [optional] |
|**description** | **String** | A seller-defined description of the payment policy. This description is only for the seller&#39;s use, and is not exposed on any eBay pages.  &lt;br/&gt;&lt;br/&gt;&lt;b&gt;Max length&lt;/b&gt;: 250 |  [optional] |
|**fullPaymentDueIn** | [**TimeDuration**](TimeDuration.md) |  |  [optional] |
|**immediatePay** | **Boolean** | If this field is returned as &lt;code&gt;true&lt;/code&gt;, immediate payment is required from the buyer for: &lt;ul&gt;&lt;li&gt;A fixed-price item&lt;/li&gt;&lt;li&gt;An auction item where the buyer uses the &#39;Buy it Now&#39; option&lt;/li&gt;&lt;li&gt;A deposit for a motor vehicle listing&lt;/li&gt;&lt;/ul&gt;&lt;br /&gt;It is possible for the seller to set this field as &lt;code&gt;true&lt;/code&gt; in the payment business policy, but it will not apply in some scenarios. For example, immediate payment is not applicable for auction listings that have a winning bidder, for buyer purchases that involve the Best Offer feature, or for transactions that happen offline between the buyer and seller. |  [optional] |
|**marketplaceId** | **String** | The ID of the eBay marketplace to which the payment business policy applies. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum&#39;&gt;eBay API documentation&lt;/a&gt; |  [optional] |
|**name** | **String** | A seller-defined name for this fulfillment policy. Names must be unique for policies assigned to the same marketplace. &lt;br/&gt;&lt;br/&gt;&lt;b&gt;Max length&lt;/b&gt;: 64 |  [optional] |
|**paymentInstructions** | **String** | Although this field may be returned for some older payment business policies, payment instructions are no longer supported by payment business policies. If this field is returned, it can be ignored and these payment instructions will not appear in any listings that use the corresponding business policy. &lt;br/&gt;&lt;br/&gt;&lt;b&gt;Max length&lt;/b&gt;: 1000 |  [optional] |
|**paymentMethods** | [**List&lt;PaymentMethod&gt;**](PaymentMethod.md) | This container is returned to show the payment methods that are accepted for the payment business policy.  &lt;br&gt;&lt;br&gt;Sellers do not have to specify any electronic payment methods for listings, so this array will often be returned empty unless the payment business policy is intended for motor vehicle listings or other items in categories where offline payments are required or supported.  |  [optional] |
|**paymentPolicyId** | **String** | A unique eBay-assigned ID for a payment business policy. This ID is generated when the policy is created. |  [optional] |



