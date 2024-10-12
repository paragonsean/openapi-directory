

# OrderAdd


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminComment** | **String** | Specifies admin&#39;s order comment |  [optional] |
|**adminPrivateComment** | **String** | Specifies private admin&#39;s order comment |  [optional] |
|**billAddress1** | **String** | Specifies first billing address |  |
|**billAddress2** | **String** | Specifies second billing address |  [optional] |
|**billCity** | **String** | Specifies billing city |  |
|**billCompany** | **String** | Specifies billing company |  [optional] |
|**billCountry** | **String** | Specifies billing country code |  |
|**billFax** | **String** | Specifies billing fax |  [optional] |
|**billFirstName** | **String** | Specifies billing first name |  |
|**billLastName** | **String** | Specifies billing last name |  |
|**billPhone** | **String** | Specifies billing phone |  [optional] |
|**billPostcode** | **String** | Specifies billing postcode |  |
|**billState** | **String** | Specifies billing state code |  |
|**channelId** | **String** | Channel ID |  [optional] |
|**clearCache** | **Boolean** | Is cache clear required |  [optional] |
|**comment** | **String** | Specifies order comment |  [optional] |
|**couponDiscount** | **BigDecimal** | Specifies order&#39;s coupon discount |  [optional] |
|**coupons** | **List&lt;String&gt;** | Coupons that will be applied to order |  [optional] |
|**createInvoice** | **Boolean** | Defines whether the invoice is created automatically along with the order |  [optional] |
|**currency** | **String** | Currency code of order |  [optional] |
|**customerBirthday** | **String** | Specifies customer’s birthday |  [optional] |
|**customerEmail** | **String** | Defines the customer specified by email for whom order has to be created |  |
|**customerFax** | **String** | Specifies customer’s fax |  [optional] |
|**customerFirstName** | **String** | Specifies customer&#39;s first name |  [optional] |
|**customerLastName** | **String** | Specifies customer’s last name |  [optional] |
|**customerPhone** | **String** | Specifies customer’s phone |  [optional] |
|**date** | **String** | Specifies an order creation date in format Y-m-d H:i:s |  [optional] |
|**dateFinished** | **String** | Specifies order&#39;s  finished date |  [optional] |
|**dateModified** | **String** | Specifies order&#39;s  modification date |  [optional] |
|**discount** | **BigDecimal** | Specifies order&#39;s discount |  [optional] |
|**externalSource** | **String** | Identifying the system used to generate the order |  [optional] |
|**financialStatus** | **String** | Create order with financial status |  [optional] |
|**fulfillmentStatus** | **String** | Create order with fulfillment status |  [optional] |
|**giftCertificateDiscount** | **BigDecimal** | Discounts for order with gift certificates |  [optional] |
|**id** | **String** | Defines order&#39;s id |  [optional] |
|**inventoryBehaviour** | **String** | The behaviour to use when updating inventory.&lt;hr&gt;&lt;div style&#x3D;\&quot;font-style:normal\&quot;&gt;Values description:&lt;div style&#x3D;\&quot;margin-left: 2%; padding-top: 2%\&quot;&gt;&lt;div style&#x3D;\&quot;font-size:85%\&quot;&gt;&lt;b&gt;bypass&lt;/b&gt; &#x3D; Do not claim inventory &lt;/br&gt;&lt;/br&gt;&lt;b&gt;decrement_ignoring_policy&lt;/b&gt; &#x3D; Ignore the product&#39;s &lt;/br&gt; inventory policy and claim amounts&lt;/br&gt;&lt;/br&gt;&lt;b&gt;decrement_obeying_policy&lt;/b&gt; &#x3D;  Obey the product&#39;s &lt;/br&gt; inventory policy.&lt;/br&gt;&lt;/br&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt; |  [optional] |
|**noteAttributes** | [**List&lt;OrderAddNoteAttributesInner&gt;**](OrderAddNoteAttributesInner.md) | Defines note attributes |  [optional] |
|**orderId** | **String** | Defines the order id if it is supported by the cart |  [optional] |
|**orderItem** | [**List&lt;OrderAddOrderItemInner&gt;**](OrderAddOrderItemInner.md) |  |  |
|**orderPaymentMethod** | **String** | Defines order payment method.&lt;br/&gt;Setting order_payment_method on Shopify will also change financial_status field value to &#39;paid&#39; |  [optional] |
|**orderShippingMethod** | **String** | Defines order shipping method |  [optional] |
|**orderStatus** | **String** | Defines order status. |  |
|**pricesIncTax** | **Boolean** | Indicates whether prices and subtotal includes tax. |  [optional] |
|**sendAdminNotifications** | **Boolean** | Notify admin when new order was created. |  [optional] |
|**sendNotifications** | **Boolean** | Send notifications to customer after order was created |  [optional] |
|**shippAddress1** | **String** | Specifies first shipping address |  [optional] |
|**shippAddress2** | **String** | Specifies second address line of a shipping street address |  [optional] |
|**shippCity** | **String** | Specifies shipping city |  [optional] |
|**shippCompany** | **String** | Specifies shipping company |  [optional] |
|**shippCountry** | **String** | Specifies shipping country code |  [optional] |
|**shippFax** | **String** | Specifies shipping fax |  [optional] |
|**shippFirstName** | **String** | Specifies shipping first name |  [optional] |
|**shippLastName** | **String** | Specifies shipping last name |  [optional] |
|**shippPhone** | **String** | Specifies shipping phone |  [optional] |
|**shippPostcode** | **String** | Specifies shipping postcode |  [optional] |
|**shippState** | **String** | Specifies shipping state code |  [optional] |
|**shippingPrice** | **BigDecimal** | Specifies order&#39;s shipping price |  [optional] |
|**shippingTax** | **BigDecimal** | Specifies order&#39;s shipping price tax |  [optional] |
|**storeId** | **String** | Defines store id where the order should be assigned |  [optional] |
|**subtotalPrice** | **BigDecimal** | Total price of all ordered products multiplied by their number, excluding tax, shipping price and discounts |  [optional] |
|**tags** | **String** | Order tags |  [optional] |
|**taxPrice** | **BigDecimal** | The value of tax cost for order |  [optional] |
|**totalPaid** | **BigDecimal** | Defines total paid amount for the order |  [optional] |
|**totalPrice** | **BigDecimal** | Defines order&#39;s total price |  [optional] |
|**totalWeight** | **Integer** | Defines the sum of all line item weights in grams for the order |  [optional] |
|**transactionId** | **String** | Payment transaction id |  [optional] |



