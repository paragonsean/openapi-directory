

# UpsertSellerRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**csCIdentification** | **String** | SKU Seller Identification |  |
|**account** | **String** | Seller&#39;s account name |  |
|**allowHybridPayments** | **Boolean** | Flag that allows customers to use gift cards from the seller to buy their products on the marketplace. It identifies purchases made with a gift card so that only the final price (with discounts applied) is paid to the seller. |  |
|**availableSalesChannels** | [**List&lt;AvailableSalesChannel&gt;**](AvailableSalesChannel.md) | Sales channel (or [trade policy](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV#master-data)) available. |  |
|**catalogSystemEndpoint** | **String** | URL of the endpoint of the seller&#39;s catalog. This field will only be displayed if the seller type is VTEX Store. The field format will be as follows: &#x60;https://{sellerName}.vtexcommercestable.com.br/api/catalog_system/.&#x60; |  |
|**channel** | **String** | Channel&#39;s name. |  |
|**deliveryPolicy** | **String** | Text describing the delivery policy previously agreed between the marketplace and the seller. |  |
|**description** | **String** | String describing the seller |  |
|**email** | **String** | email of the admin responsible for the seller. |  |
|**exchangeReturnPolicy** | **String** | Text describing the exchange and return policy previously agreed between the marketplace and the seller. |  |
|**fulfillmentEndpoint** | **String** | URL of the endpoint for fulfillment of seller&#39;s orders, which the marketplace will use to communicate with the seller.   For **external sellers**, please include the URL of the seller&#39;s endpoint. External sellers have different endpoint standards. The seller must inform this endpoint to the marketplace so that the marketplace can complete the configuration process.   For **VTEX Stores**, the field format will be as follows: &#x60;https://{SellerName}.vtexcommercestable.com.br/api/fulfillment?&amp;sc&#x3D;{TradePolicyID}&#x60;.   The value &#x60;SellerName&#x60; corresponds to the store name if the seller is a VTEX store.   The value &#x60;TradePolicyID&#x60; corresponds to the [trade policy](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV#master-data) created by the seller in their own VTEX environment. The seller must inform this ID to the marketplace so that the marketplace can complete the configuration process.   The value &#x60;AffiliateID&#x60; corresponds to the 3-digit affiliate identification code created by the seller. The seller must inform this ID to the marketplace so that the marketplace can complete the configuration process.   To configure the [Multilevel Omnichannel Inventory](https://developers.vtex.com/vtex-rest-api/docs/multilevel-omnichannel-inventory) feature, fill in this field with the checkout endpoint following this example: &#x60;https://{{sellerAccount}}.vtexcommercestable.com.br/api/checkout?affiliateid&#x3D;{{affiliateId}}&amp;sc&#x3D;{{salesChannel&#x60; |  |
|**fulfillmentSellerId** | **String** |  Identification code of the seller responsible for fulfilling the order. This is an optional field used when a seller sells SKUs from another seller. If the seller sells their own SKUs, it must be nulled. |  |
|**groups** | [**List&lt;Groups&gt;**](Groups.md) | Array of groups attached to the seller. Groups are defined by key-words that group sellers into categories defined by the marketplace when adding a new seller through the [Configure Seller Account](https://developers.vtex.com/vtex-rest-api/reference/sellers#putupsertseller) endpoint. It is possible to filter sellers by group in the Seller Management page in your VTEX Admin. Know more about groups through our [Seller Management](https://help.vtex.com/en/tutorial/gerenciamento-de-sellers-beta--6eEiOISwxuAWJ8w6MtK7iv#groups) documentation. |  [optional] |
|**id** | **String** | Seller ID assigned by the marketplace. We recommend filling it in with the seller&#39;s account name. |  |
|**isActive** | **Boolean** | Whether the seller is active on the marketplace or not. |  |
|**isBetterScope** | **Boolean** | Flag used by the VTEX Checkout to simmulate shopping carts, products and shipping only in sellers with the boolean set as &#x60;true&#x60;, avoiding performance issues. |  |
|**isVtex** | **Boolean** | Flag determining whether the seller configured is a VTEX store or not. |  |
|**name** | **String** | Name of the seller&#39;s store, configured in the seller&#39;s environment. |  |
|**password** | **String** | User password, if you are using a hub to integrate with the external seller. |  |
|**salesChannel** | **String** | Sales channel (or [trade policy](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV)) associated to the seller account created. If no value is specified, the system will automatically use the sales channel configured in the seller&#39;s [affiliate](https://help.vtex.com/en/tutorial/configuring-affiliates--tutorials_187) ID. |  |
|**score** | **BigDecimal** | Score attributed to this seller. |  |
|**securityPrivacyPolicy** | **String** |  Text describing the security policy previously agreed between the marketplace and the seller. |  |
|**sellerCommissionConfiguration** | [**List&lt;SellerCommissionConfiguration&gt;**](SellerCommissionConfiguration.md) |  |  |
|**sellerType** | **Integer** | Type of seller, including:   &#x60;1&#x60;: regular seller   &#x60;2&#x60;: whitelabel seller |  |
|**taxCode** | **String** | This code is the Identity Number for the legal entity and is linked to information in its base country. |  |
|**trustPolicy** | **String** |  the marketplace must first allow VTEX to share clients’ email addresses with the seller. To do so, it is necessary to set &#39;AllowEmailSharing&#39; as the value for the TrustPolicy field |  |
|**user** | **String** | Username, if you are using a hub to integrate with the external seller. |  |



