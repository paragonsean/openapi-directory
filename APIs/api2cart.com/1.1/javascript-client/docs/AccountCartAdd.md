# SwaggerApi2Cart.AccountCartAdd

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_3dcartAccessToken** | **String** | 3DCart Token | [optional] 
**_3dcartPrivateKey** | **String** | 3DCart Private Key | [optional] 
**_3dcartapiApiKey** | **String** | 3DCart API Key | [optional] 
**amazonAccessKeyId** | **String** | Amazon Secret Key Id | [optional] 
**amazonAccessToken** | **String** | MWS Auth Token. Access token authorizing the app to access resources on behalf of a user | [optional] 
**amazonMarketplacesIds** | **String** | Amazon Marketplace IDs comma separated string | [optional] 
**amazonSecretKey** | **String** | Amazon Secret Key | [optional] 
**amazonSellerId** | **String** | Amazon Seller ID (Merchant token) | [optional] 
**amazonSpApiEnvironment** | **String** | Amazon SP API environment | [optional] [default to &#39;production&#39;]
**amazonSpAwsRegion** | **String** | Amazon AWS Region | 
**amazonSpAwsRoleArn** | **String** | Amazon AWS Role ARN | 
**amazonSpAwsUserKeyId** | **String** | Amazon AWS user access key ID | 
**amazonSpAwsUserSecret** | **String** | Amazon AWS user secret access key | 
**amazonSpClientId** | **String** | Amazon SP API app client id | 
**amazonSpClientSecret** | **String** | Amazon SP API app client secret | 
**amazonSpRefreshToken** | **String** | Amazon SP API OAuth refresh token | 
**aspdotnetstorefrontApiPass** | **String** | AspDotNetStorefront API Password | [optional] 
**aspdotnetstorefrontApiUser** | **String** | It&#39;s a AspDotNetStorefront account for which API is available | [optional] 
**bigcommerceapiAccessToken** | **String** | Access token authorizing the app to access resources on behalf of a user | [optional] 
**bigcommerceapiAdminAccount** | **String** | It&#39;s a BigCommerce account for which API is enabled | [optional] 
**bigcommerceapiApiKey** | **String** | Bigcommerce API Key | [optional] 
**bigcommerceapiApiPath** | **String** | BigCommerce API URL | [optional] 
**bigcommerceapiClientId** | **String** | Client ID of the requesting app | [optional] 
**bigcommerceapiContext** | **String** | API Path section unique to the store | [optional] 
**bridgeUrl** | **String** | This parameter allows to set up store with custom bridge url (also you must use store_root parameter if a bridge folder is not in the root folder of the store) | [optional] 
**cartId** | **String** | Store’s identifier which you can get from cart_list method | 
**commercehqApiKey** | **String** | CommerceHQ api key | [optional] 
**commercehqApiPassword** | **String** | CommerceHQ api password | [optional] 
**dbTablesPrefix** | **String** | DB tables prefix | [optional] 
**demandwareApiPassword** | **String** | Demandware api password | [optional] 
**demandwareClientId** | **String** | Demandware client id | [optional] 
**demandwareUserName** | **String** | Demandware user name | [optional] 
**demandwareUserPassword** | **String** | Demandware user password | [optional] 
**ebayAccessToken** | **String** | Used to authenticate API requests. | [optional] 
**ebayClientId** | **String** | Application ID (AppID). | [optional] 
**ebayClientSecret** | **String** | Shared Secret from eBay application | [optional] 
**ebayEnvironment** | **String** | eBay environment | [optional] [default to &#39;production&#39;]
**ebayRefreshToken** | **String** | Used to renew the access token. | [optional] 
**ebayRuname** | **String** | The RuName value that eBay assigns to your application. | [optional] 
**ebaySiteId** | **Number** | eBay global ID | [optional] [default to 0]
**ecwidAcessToken** | **String** | Access token authorizing the app to access resources on behalf of a user | [optional] 
**ecwidStoreId** | **String** | Store Id | [optional] 
**etsyAccessToken** | **String** | Access token authorizing the app to access resources on behalf of a user | [optional] 
**etsyClientId** | **String** | Etsy Client Id | 
**etsyKeystring** | **String** | Etsy keystring | [optional] 
**etsyRefreshToken** | **String** | Etsy Refresh token | 
**etsySharedSecret** | **String** | Etsy shared secret | [optional] 
**etsyTokenSecret** | **String** | Secret token authorizing the app to access resources on behalf of a user | [optional] 
**ftpHost** | **String** | FTP connection host | [optional] 
**ftpPassword** | **String** | FTP Password | [optional] 
**ftpPort** | **Number** | FTP Port | [optional] 
**ftpStoreDir** | **String** | FTP Store dir | [optional] 
**ftpUser** | **String** | FTP User | [optional] 
**hybrisClientId** | **String** | Omni Commerce Connector Client ID | [optional] 
**hybrisClientSecret** | **String** | Omni Commerce Connector Client Secret | [optional] 
**hybrisPassword** | **String** | User password | [optional] 
**hybrisUsername** | **String** | User Name | [optional] 
**hybrisWebsites** | [**[AccountCartAddHybrisWebsitesInner]**](AccountCartAddHybrisWebsitesInner.md) | Websites to stores mapping data | [optional] 
**lightspeedApiKey** | **String** | LightSpeed api key | [optional] 
**lightspeedApiSecret** | **String** | LightSpeed api secret | [optional] 
**magentoAccessToken** | **String** | Magento Access Token | [optional] 
**magentoConsumerKey** | **String** | Magento Consumer Key | [optional] 
**magentoConsumerSecret** | **String** | Magento Consumer Secret | [optional] 
**magentoTokenSecret** | **String** | Magento Token Secret | [optional] 
**mercadoLibreAppId** | **String** | Mercado Libre App ID | [optional] 
**mercadoLibreAppSecretKey** | **String** | Mercado Libre App Secret Key | [optional] 
**mercadoLibreRefreshToken** | **String** | Mercado Libre Refresh Token | [optional] 
**netoApiKey** | **String** | Neto API Key | [optional] 
**netoApiUsername** | **String** | Neto User Name | [optional] 
**prestashopWebserviceKey** | **String** | Prestashop webservice key | [optional] 
**shopifyAccessToken** | **String** | Access token authorizing the app to access resources on behalf of a user | [optional] 
**shopifyApiKey** | **String** | Shopify API Key | [optional] 
**shopifyApiPassword** | **String** | Shopify API Password | [optional] 
**shopifySharedSecret** | **String** | Shared secret | [optional] 
**shopwareAccessKey** | **String** | Shopware access key | [optional] 
**shopwareApiKey** | **String** | Shopware api key | [optional] 
**shopwareApiSecret** | **String** | Shopware client secret access key | [optional] 
**squarespaceApiKey** | **String** | Squarespace API Key | [optional] 
**storeKey** | **String** | Set this parameter if bridge is already uploaded to store | [optional] 
**storeRoot** | **String** | Absolute path to the store root directory (used with \&quot;bridge_url\&quot; parameter) | [optional] 
**storeUrl** | **String** | A web address of a store that you would like to connect to API2Cart | 
**validateVersion** | **Boolean** | Specify if api2cart should validate cart version | [optional] [default to false]
**verify** | **Boolean** | Enables or disables cart&#39;s verification | [optional] [default to true]
**volusionLogin** | **String** | It&#39;s a Volusion account for which API is enabled | [optional] 
**volusionPassword** | **String** | Volusion API Password | [optional] 
**walmartChannelType** | **String** | Walmart WM_CONSUMER.CHANNEL.TYPE header | [optional] 
**walmartClientId** | **String** | Walmart client ID | [optional] 
**walmartClientSecret** | **String** | Walmart client secret | [optional] 
**walmartEnvironment** | **String** | Walmart environment | [optional] [default to &#39;production&#39;]
**wcConsumerKey** | **String** | Woocommerce consumer key | [optional] 
**wcConsumerSecret** | **String** | Woocommerce consumer secret | [optional] 
**wixAppId** | **String** | Wix App ID | [optional] 
**wixAppSecretKey** | **String** | Wix App Secret Key | [optional] 
**wixRefreshToken** | **String** | Wix refresh token | [optional] 
**zidAccessToken** | **String** | Zid Access Token | [optional] 
**zidAuthorization** | **String** | Zid Authorization | [optional] 
**zidClientId** | **Number** | Zid Client ID | [optional] 
**zidClientSecret** | **String** | Zid Client Secret | [optional] 
**zidRefreshToken** | **String** | Zid refresh token | [optional] 



## Enum: AmazonSpAwsRegionEnum


* `eu-west-1` (value: `"eu-west-1"`)

* `us-east-1` (value: `"us-east-1"`)

* `us-west-2` (value: `"us-west-2"`)





## Enum: CartIdEnum


* `3DCart` (value: `"3DCart"`)

* `3DCartApi` (value: `"3DCartApi"`)

* `AceShop` (value: `"AceShop"`)

* `AmazonSP` (value: `"AmazonSP"`)

* `Amazon` (value: `"Amazon"`)

* `AspDotNetStorefront` (value: `"AspDotNetStorefront"`)

* `BigcommerceApi` (value: `"BigcommerceApi"`)

* `Creloaded` (value: `"Creloaded"`)

* `CommerceHQ` (value: `"CommerceHQ"`)

* `Cscart` (value: `"Cscart"`)

* `Cubecart` (value: `"Cubecart"`)

* `Demandware` (value: `"Demandware"`)

* `EBay` (value: `"EBay"`)

* `Ecwid` (value: `"Ecwid"`)

* `Etsy` (value: `"Etsy"`)

* `EtsyAPIv3` (value: `"EtsyAPIv3"`)

* `Gambio` (value: `"Gambio"`)

* `JooCart` (value: `"JooCart"`)

* `Magento1212` (value: `"Magento1212"`)

* `Magento2Api` (value: `"Magento2Api"`)

* `MijoShop` (value: `"MijoShop"`)

* `Neto` (value: `"Neto"`)

* `Opencart14` (value: `"Opencart14"`)

* `LightSpeed` (value: `"LightSpeed"`)

* `Oscmax2` (value: `"Oscmax2"`)

* `Oscommerce22ms2` (value: `"Oscommerce22ms2"`)

* `Oxid` (value: `"Oxid"`)

* `Pinnacle` (value: `"Pinnacle"`)

* `Prestashop` (value: `"Prestashop"`)

* `PrestashopApi` (value: `"PrestashopApi"`)

* `SSPremium` (value: `"SSPremium"`)

* `Shopify` (value: `"Shopify"`)

* `Squarespace` (value: `"Squarespace"`)

* `Shopware` (value: `"Shopware"`)

* `ShopwareApi` (value: `"ShopwareApi"`)

* `Tomatocart` (value: `"Tomatocart"`)

* `Ubercart` (value: `"Ubercart"`)

* `Virtuemart` (value: `"Virtuemart"`)

* `Volusion` (value: `"Volusion"`)

* `WPecommerce` (value: `"WPecommerce"`)

* `Walmart` (value: `"Walmart"`)

* `WebAsyst` (value: `"WebAsyst"`)

* `Woocommerce` (value: `"Woocommerce"`)

* `WoocommerceApi` (value: `"WoocommerceApi"`)

* `Wix` (value: `"Wix"`)

* `Xcart` (value: `"Xcart"`)

* `Xtcommerce` (value: `"Xtcommerce"`)

* `XtcommerceVeyton` (value: `"XtcommerceVeyton"`)

* `Zencart137` (value: `"Zencart137"`)

* `Hybris` (value: `"Hybris"`)

* `MercadoLibre` (value: `"MercadoLibre"`)

* `Zid` (value: `"Zid"`)

* `Zoey` (value: `"Zoey"`)




