

# V1PaymentItemization

Payment include an` itemizations` field that lists the items purchased, along with associated fees, modifiers, and discounts. Each itemization has an `itemization_type` field that indicates which of the following the itemization represents:  <ul> <li>An item variation from the merchant's item library</li> <li>A custom monetary amount</li> <li> An action performed on a Square gift card, such as activating or reloading it. </li> </ul>  *Note**: itemization information included in a `Payment` object reflects details collected **at the time of the payment**. Details such as the name or price of items might have changed since the payment was processed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**discountMoney** | [**V1Money**](V1Money.md) |  |  [optional] |
|**discounts** | [**List&lt;V1PaymentDiscount&gt;**](V1PaymentDiscount.md) | All discounts applied to this itemization. |  [optional] |
|**grossSalesMoney** | [**V1Money**](V1Money.md) |  |  [optional] |
|**itemDetail** | [**V1PaymentItemDetail**](V1PaymentItemDetail.md) |  |  [optional] |
|**itemVariationName** | **String** | The name of the item variation purchased, if any. |  [optional] |
|**itemizationType** | **String** | The type of purchase that the itemization represents, such as an ITEM or CUSTOM_AMOUNT |  [optional] |
|**modifiers** | [**List&lt;V1PaymentModifier&gt;**](V1PaymentModifier.md) | All modifier options applied to this itemization. |  [optional] |
|**name** | **String** | The item&#39;s name. |  [optional] |
|**netSalesMoney** | [**V1Money**](V1Money.md) |  |  [optional] |
|**notes** | **String** | Notes entered by the merchant about the item at the time of payment, if any. |  [optional] |
|**quantity** | **BigDecimal** | The quantity of the item purchased. This can be a decimal value. |  [optional] |
|**singleQuantityMoney** | [**V1Money**](V1Money.md) |  |  [optional] |
|**taxes** | [**List&lt;V1PaymentTax&gt;**](V1PaymentTax.md) | All taxes applied to this itemization. |  [optional] |
|**totalMoney** | [**V1Money**](V1Money.md) |  |  [optional] |



