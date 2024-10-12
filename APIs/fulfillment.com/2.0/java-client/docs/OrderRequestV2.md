

# OrderRequestV2


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**integrator** | [**IntegratorEnum**](#IntegratorEnum) | Use of this property requires special permission and must be discussed with your account executive; values are restricted while custom values need to be accepted by your AE. |  [optional] |
|**items** | [**List&lt;OrderRequestV2ItemsInner&gt;**](OrderRequestV2ItemsInner.md) |  |  |
|**merchantId** | **Integer** | Necessary if you have a multitenancy account, otherwise we will associate the order with your account |  [optional] |
|**merchantOrderId** | **String** | Unique ID provided by the merchant |  |
|**notes** | **String** |  |  [optional] |
|**recipient** | [**ConsigneeNewV2**](ConsigneeNewV2.md) |  |  |
|**shippingMethod** | **String** | Custom for you, it will be mapped to an actual method within the OMS UI |  |
|**warehouse** | [**OrderRequestV2Warehouse**](OrderRequestV2Warehouse.md) |  |  [optional] |



## Enum: IntegratorEnum

| Name | Value |
|---- | -----|
| _1_SHOPPING_CART | &quot;1ShoppingCart&quot; |
| _3D_CART | &quot;3dCart&quot; |
| ADOBE_BC | &quot;AdobeBC&quot; |
| AMAZON_AU | &quot;AmazonAU&quot; |
| AMAZON_EU | &quot;AmazonEU&quot; |
| AMAZON_NA | &quot;AmazonNA&quot; |
| BIG_COMMERCE | &quot;BigCommerce&quot; |
| BRAND_BOOM | &quot;BrandBoom&quot; |
| BRIGHT_PEARL | &quot;BrightPearl&quot; |
| BUY_GOODS | &quot;BuyGoods&quot; |
| CELERY | &quot;Celery&quot; |
| CHANNEL_ADVISOR | &quot;ChannelAdvisor&quot; |
| CLICKBANK | &quot;Clickbank&quot; |
| COMMERCE_HUB | &quot;CommerceHub&quot; |
| CUSTOM | &quot;Custom&quot; |
| DEMANDWARE | &quot;Demandware&quot; |
| EBAY | &quot;Ebay&quot; |
| ECWID | &quot;Ecwid&quot; |
| ETSY | &quot;Etsy&quot; |
| FOXY_CART | &quot;FoxyCart&quot; |
| GOODSIE | &quot;Goodsie&quot; |
| INFUSIONSOFT | &quot;Infusionsoft&quot; |
| KONNEKTIVE | &quot;Konnektive&quot; |
| LIME_LIGHT | &quot;LimeLight&quot; |
| LINIO | &quot;Linio&quot; |
| LINNWORKS | &quot;Linnworks&quot; |
| MAGENTO | &quot;Magento&quot; |
| NETSUITE | &quot;Netsuite&quot; |
| NEW_EGG | &quot;NewEgg&quot; |
| NEXTERNAL | &quot;Nexternal&quot; |
| NU_ORDER | &quot;NuOrder&quot; |
| OPENCART | &quot;Opencart&quot; |
| ORDER_WAVE | &quot;OrderWave&quot; |
| OS_COMMERCE1 | &quot;osCommerce1&quot; |
| OVERSTOCK | &quot;Overstock&quot; |
| PAY_PAL | &quot;PayPal&quot; |
| PRESTA_SHOP | &quot;PrestaShop&quot; |
| PRICEFALLS | &quot;Pricefalls&quot; |
| QUICKBOOKS | &quot;Quickbooks&quot; |
| RAKUTEN | &quot;Rakuten&quot; |
| SEARS | &quot;Sears&quot; |
| SELLBRITE | &quot;Sellbrite&quot; |
| SELLER_CLOUD | &quot;SellerCloud&quot; |
| SHIPSTATION | &quot;Shipstation&quot; |
| SHOPIFY | &quot;Shopify&quot; |
| SKUBANA | &quot;Skubana&quot; |
| SOLID_COMMERCE | &quot;SolidCommerce&quot; |
| SPARK_PAY | &quot;SparkPay&quot; |
| SPREE_COMMERCE | &quot;SpreeCommerce&quot; |
| SPS_COMMERCE | &quot;spsCommerce&quot; |
| STITCH_LABS | &quot;StitchLabs&quot; |
| STONE_EDGE | &quot;StoneEdge&quot; |
| TRADE_GECKO | &quot;TradeGecko&quot; |
| ULTRA_CART | &quot;UltraCart&quot; |
| VOLUSION | &quot;Volusion&quot; |
| VTEX | &quot;VTEX&quot; |
| WALMART | &quot;Walmart&quot; |
| WOO_COMMERCE | &quot;WooCommerce&quot; |
| YAHOO | &quot;Yahoo&quot; |



