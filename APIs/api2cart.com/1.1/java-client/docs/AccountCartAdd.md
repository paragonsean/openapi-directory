

# AccountCartAdd


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_3dcartAccessToken** | **String** | 3DCart Token |  [optional] |
|**_3dcartPrivateKey** | **String** | 3DCart Private Key |  [optional] |
|**_3dcartapiApiKey** | **String** | 3DCart API Key |  [optional] |
|**amazonAccessKeyId** | **String** | Amazon Secret Key Id |  [optional] |
|**amazonAccessToken** | **String** | MWS Auth Token. Access token authorizing the app to access resources on behalf of a user |  [optional] |
|**amazonMarketplacesIds** | **String** | Amazon Marketplace IDs comma separated string |  [optional] |
|**amazonSecretKey** | **String** | Amazon Secret Key |  [optional] |
|**amazonSellerId** | **String** | Amazon Seller ID (Merchant token) |  [optional] |
|**amazonSpApiEnvironment** | **String** | Amazon SP API environment |  [optional] |
|**amazonSpAwsRegion** | [**AmazonSpAwsRegionEnum**](#AmazonSpAwsRegionEnum) | Amazon AWS Region |  |
|**amazonSpAwsRoleArn** | **String** | Amazon AWS Role ARN |  |
|**amazonSpAwsUserKeyId** | **String** | Amazon AWS user access key ID |  |
|**amazonSpAwsUserSecret** | **String** | Amazon AWS user secret access key |  |
|**amazonSpClientId** | **String** | Amazon SP API app client id |  |
|**amazonSpClientSecret** | **String** | Amazon SP API app client secret |  |
|**amazonSpRefreshToken** | **String** | Amazon SP API OAuth refresh token |  |
|**aspdotnetstorefrontApiPass** | **String** | AspDotNetStorefront API Password |  [optional] |
|**aspdotnetstorefrontApiUser** | **String** | It&#39;s a AspDotNetStorefront account for which API is available |  [optional] |
|**bigcommerceapiAccessToken** | **String** | Access token authorizing the app to access resources on behalf of a user |  [optional] |
|**bigcommerceapiAdminAccount** | **String** | It&#39;s a BigCommerce account for which API is enabled |  [optional] |
|**bigcommerceapiApiKey** | **String** | Bigcommerce API Key |  [optional] |
|**bigcommerceapiApiPath** | **String** | BigCommerce API URL |  [optional] |
|**bigcommerceapiClientId** | **String** | Client ID of the requesting app |  [optional] |
|**bigcommerceapiContext** | **String** | API Path section unique to the store |  [optional] |
|**bridgeUrl** | **String** | This parameter allows to set up store with custom bridge url (also you must use store_root parameter if a bridge folder is not in the root folder of the store) |  [optional] |
|**cartId** | [**CartIdEnum**](#CartIdEnum) | Store’s identifier which you can get from cart_list method |  |
|**commercehqApiKey** | **String** | CommerceHQ api key |  [optional] |
|**commercehqApiPassword** | **String** | CommerceHQ api password |  [optional] |
|**dbTablesPrefix** | **String** | DB tables prefix |  [optional] |
|**demandwareApiPassword** | **String** | Demandware api password |  [optional] |
|**demandwareClientId** | **String** | Demandware client id |  [optional] |
|**demandwareUserName** | **String** | Demandware user name |  [optional] |
|**demandwareUserPassword** | **String** | Demandware user password |  [optional] |
|**ebayAccessToken** | **String** | Used to authenticate API requests. |  [optional] |
|**ebayClientId** | **String** | Application ID (AppID). |  [optional] |
|**ebayClientSecret** | **String** | Shared Secret from eBay application |  [optional] |
|**ebayEnvironment** | **String** | eBay environment |  [optional] |
|**ebayRefreshToken** | **String** | Used to renew the access token. |  [optional] |
|**ebayRuname** | **String** | The RuName value that eBay assigns to your application. |  [optional] |
|**ebaySiteId** | **Integer** | eBay global ID |  [optional] |
|**ecwidAcessToken** | **String** | Access token authorizing the app to access resources on behalf of a user |  [optional] |
|**ecwidStoreId** | **String** | Store Id |  [optional] |
|**etsyAccessToken** | **String** | Access token authorizing the app to access resources on behalf of a user |  [optional] |
|**etsyClientId** | **String** | Etsy Client Id |  |
|**etsyKeystring** | **String** | Etsy keystring |  [optional] |
|**etsyRefreshToken** | **String** | Etsy Refresh token |  |
|**etsySharedSecret** | **String** | Etsy shared secret |  [optional] |
|**etsyTokenSecret** | **String** | Secret token authorizing the app to access resources on behalf of a user |  [optional] |
|**ftpHost** | **String** | FTP connection host |  [optional] |
|**ftpPassword** | **String** | FTP Password |  [optional] |
|**ftpPort** | **Integer** | FTP Port |  [optional] |
|**ftpStoreDir** | **String** | FTP Store dir |  [optional] |
|**ftpUser** | **String** | FTP User |  [optional] |
|**hybrisClientId** | **String** | Omni Commerce Connector Client ID |  [optional] |
|**hybrisClientSecret** | **String** | Omni Commerce Connector Client Secret |  [optional] |
|**hybrisPassword** | **String** | User password |  [optional] |
|**hybrisUsername** | **String** | User Name |  [optional] |
|**hybrisWebsites** | [**List&lt;AccountCartAddHybrisWebsitesInner&gt;**](AccountCartAddHybrisWebsitesInner.md) | Websites to stores mapping data |  [optional] |
|**lightspeedApiKey** | **String** | LightSpeed api key |  [optional] |
|**lightspeedApiSecret** | **String** | LightSpeed api secret |  [optional] |
|**magentoAccessToken** | **String** | Magento Access Token |  [optional] |
|**magentoConsumerKey** | **String** | Magento Consumer Key |  [optional] |
|**magentoConsumerSecret** | **String** | Magento Consumer Secret |  [optional] |
|**magentoTokenSecret** | **String** | Magento Token Secret |  [optional] |
|**mercadoLibreAppId** | **String** | Mercado Libre App ID |  [optional] |
|**mercadoLibreAppSecretKey** | **String** | Mercado Libre App Secret Key |  [optional] |
|**mercadoLibreRefreshToken** | **String** | Mercado Libre Refresh Token |  [optional] |
|**netoApiKey** | **String** | Neto API Key |  [optional] |
|**netoApiUsername** | **String** | Neto User Name |  [optional] |
|**prestashopWebserviceKey** | **String** | Prestashop webservice key |  [optional] |
|**shopifyAccessToken** | **String** | Access token authorizing the app to access resources on behalf of a user |  [optional] |
|**shopifyApiKey** | **String** | Shopify API Key |  [optional] |
|**shopifyApiPassword** | **String** | Shopify API Password |  [optional] |
|**shopifySharedSecret** | **String** | Shared secret |  [optional] |
|**shopwareAccessKey** | **String** | Shopware access key |  [optional] |
|**shopwareApiKey** | **String** | Shopware api key |  [optional] |
|**shopwareApiSecret** | **String** | Shopware client secret access key |  [optional] |
|**squarespaceApiKey** | **String** | Squarespace API Key |  [optional] |
|**storeKey** | **String** | Set this parameter if bridge is already uploaded to store |  [optional] |
|**storeRoot** | **String** | Absolute path to the store root directory (used with \&quot;bridge_url\&quot; parameter) |  [optional] |
|**storeUrl** | **String** | A web address of a store that you would like to connect to API2Cart |  |
|**validateVersion** | **Boolean** | Specify if api2cart should validate cart version |  [optional] |
|**verify** | **Boolean** | Enables or disables cart&#39;s verification |  [optional] |
|**volusionLogin** | **String** | It&#39;s a Volusion account for which API is enabled |  [optional] |
|**volusionPassword** | **String** | Volusion API Password |  [optional] |
|**walmartChannelType** | **String** | Walmart WM_CONSUMER.CHANNEL.TYPE header |  [optional] |
|**walmartClientId** | **String** | Walmart client ID |  [optional] |
|**walmartClientSecret** | **String** | Walmart client secret |  [optional] |
|**walmartEnvironment** | **String** | Walmart environment |  [optional] |
|**wcConsumerKey** | **String** | Woocommerce consumer key |  [optional] |
|**wcConsumerSecret** | **String** | Woocommerce consumer secret |  [optional] |
|**wixAppId** | **String** | Wix App ID |  [optional] |
|**wixAppSecretKey** | **String** | Wix App Secret Key |  [optional] |
|**wixRefreshToken** | **String** | Wix refresh token |  [optional] |
|**zidAccessToken** | **String** | Zid Access Token |  [optional] |
|**zidAuthorization** | **String** | Zid Authorization |  [optional] |
|**zidClientId** | **Integer** | Zid Client ID |  [optional] |
|**zidClientSecret** | **String** | Zid Client Secret |  [optional] |
|**zidRefreshToken** | **String** | Zid refresh token |  [optional] |



## Enum: AmazonSpAwsRegionEnum

| Name | Value |
|---- | -----|
| EU_WEST_1 | &quot;eu-west-1&quot; |
| US_EAST_1 | &quot;us-east-1&quot; |
| US_WEST_2 | &quot;us-west-2&quot; |



## Enum: CartIdEnum

| Name | Value |
|---- | -----|
| _3_D_CART | &quot;3DCart&quot; |
| _3_D_CART_API | &quot;3DCartApi&quot; |
| ACE_SHOP | &quot;AceShop&quot; |
| AMAZON_SP | &quot;AmazonSP&quot; |
| AMAZON | &quot;Amazon&quot; |
| ASP_DOT_NET_STOREFRONT | &quot;AspDotNetStorefront&quot; |
| BIGCOMMERCE_API | &quot;BigcommerceApi&quot; |
| CRELOADED | &quot;Creloaded&quot; |
| COMMERCE_HQ | &quot;CommerceHQ&quot; |
| CSCART | &quot;Cscart&quot; |
| CUBECART | &quot;Cubecart&quot; |
| DEMANDWARE | &quot;Demandware&quot; |
| E_BAY | &quot;EBay&quot; |
| ECWID | &quot;Ecwid&quot; |
| ETSY | &quot;Etsy&quot; |
| ETSY_APIV3 | &quot;EtsyAPIv3&quot; |
| GAMBIO | &quot;Gambio&quot; |
| JOO_CART | &quot;JooCart&quot; |
| MAGENTO1212 | &quot;Magento1212&quot; |
| MAGENTO2_API | &quot;Magento2Api&quot; |
| MIJO_SHOP | &quot;MijoShop&quot; |
| NETO | &quot;Neto&quot; |
| OPENCART14 | &quot;Opencart14&quot; |
| LIGHT_SPEED | &quot;LightSpeed&quot; |
| OSCMAX2 | &quot;Oscmax2&quot; |
| OSCOMMERCE22MS2 | &quot;Oscommerce22ms2&quot; |
| OXID | &quot;Oxid&quot; |
| PINNACLE | &quot;Pinnacle&quot; |
| PRESTASHOP | &quot;Prestashop&quot; |
| PRESTASHOP_API | &quot;PrestashopApi&quot; |
| SS_PREMIUM | &quot;SSPremium&quot; |
| SHOPIFY | &quot;Shopify&quot; |
| SQUARESPACE | &quot;Squarespace&quot; |
| SHOPWARE | &quot;Shopware&quot; |
| SHOPWARE_API | &quot;ShopwareApi&quot; |
| TOMATOCART | &quot;Tomatocart&quot; |
| UBERCART | &quot;Ubercart&quot; |
| VIRTUEMART | &quot;Virtuemart&quot; |
| VOLUSION | &quot;Volusion&quot; |
| W_PECOMMERCE | &quot;WPecommerce&quot; |
| WALMART | &quot;Walmart&quot; |
| WEB_ASYST | &quot;WebAsyst&quot; |
| WOOCOMMERCE | &quot;Woocommerce&quot; |
| WOOCOMMERCE_API | &quot;WoocommerceApi&quot; |
| WIX | &quot;Wix&quot; |
| XCART | &quot;Xcart&quot; |
| XTCOMMERCE | &quot;Xtcommerce&quot; |
| XTCOMMERCE_VEYTON | &quot;XtcommerceVeyton&quot; |
| ZENCART137 | &quot;Zencart137&quot; |
| HYBRIS | &quot;Hybris&quot; |
| MERCADO_LIBRE | &quot;MercadoLibre&quot; |
| ZID | &quot;Zid&quot; |
| ZOEY | &quot;Zoey&quot; |



