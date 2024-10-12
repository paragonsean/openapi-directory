# SwaggerApi2Cart.AccountApi

All URIs are relative to *https://api.api2cart.com/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountCartAdd**](AccountApi.md#accountCartAdd) | **POST** /account.cart.add.json | 
[**accountCartList**](AccountApi.md#accountCartList) | **GET** /account.cart.list.json | 
[**accountConfigUpdate**](AccountApi.md#accountConfigUpdate) | **PUT** /account.config.update.json | 
[**accountFailedWebhooks**](AccountApi.md#accountFailedWebhooks) | **GET** /account.failed_webhooks.json | 
[**accountSupportedPlatforms**](AccountApi.md#accountSupportedPlatforms) | **GET** /account.supported_platforms.json | 



## accountCartAdd

> AccountCartAdd200Response accountCartAdd(accountCartAdd)



Add store to the account

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.AccountApi();
let accountCartAdd = new SwaggerApi2Cart.AccountCartAdd(); // AccountCartAdd | 
apiInstance.accountCartAdd(accountCartAdd, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountCartAdd** | [**AccountCartAdd**](AccountCartAdd.md)|  | 

### Return type

[**AccountCartAdd200Response**](AccountCartAdd200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accountCartList

> AccountCartList200Response accountCartList(opts)



Get list of carts.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.AccountApi();
let opts = {
  'params': "'force_all'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'requestFromDate': "requestFromDate_example", // String | Retrieve entities from their creation date
  'requestToDate': "requestToDate_example", // String | Retrieve entities to their creation date
  'storeUrl': "storeUrl_example", // String | A web address of a store
  'storeKey': "storeKey_example" // String | Find store by store key
};
apiInstance.accountCartList(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;force_all&#39;]
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **requestFromDate** | **String**| Retrieve entities from their creation date | [optional] 
 **requestToDate** | **String**| Retrieve entities to their creation date | [optional] 
 **storeUrl** | **String**| A web address of a store | [optional] 
 **storeKey** | **String**| Find store by store key | [optional] 

### Return type

[**AccountCartList200Response**](AccountCartList200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountConfigUpdate

> AccountConfigUpdate200Response accountConfigUpdate(opts)



Update configs in the API2Cart database.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.AccountApi();
let opts = {
  'newStoreKey': "newStoreKey_example", // String | Update store key
  'bridgeUrl': "bridgeUrl_example", // String | This parameter allows to set up store with custom bridge url (also you must use store_root parameter if a bridge folder is not in the root folder of the store)
  'storeRoot': "storeRoot_example", // String | Absolute path to the store root directory (used with \"bridge_url\" parameter)
  'dbTablesPrefix': "dbTablesPrefix_example", // String | DB tables prefix
  '_3dcartPrivateKey': "_3dcartPrivateKey_example", // String | 3DCart Private Key
  '_3dcartAccessToken': "_3dcartAccessToken_example", // String | 3DCart Token
  '_3dcartapiApiKey': "_3dcartapiApiKey_example", // String | 3DCart API Key
  'amazonSpClientId': "amazonSpClientId_example", // String | Amazon SP API app client id
  'amazonSpClientSecret': "amazonSpClientSecret_example", // String | Amazon SP API app client secret
  'amazonSpAwsUserKeyId': "amazonSpAwsUserKeyId_example", // String | Amazon AWS user access key ID
  'amazonSpAwsUserSecret': "amazonSpAwsUserSecret_example", // String | Amazon AWS user secret access key
  'amazonSpAwsRegion': "amazonSpAwsRegion_example", // String | Amazon AWS Region
  'amazonSpAwsRoleArn': "amazonSpAwsRoleArn_example", // String | Amazon AWS Role ARN
  'amazonSpRefreshToken': "amazonSpRefreshToken_example", // String | Amazon SP API OAuth refresh token
  'amazonSpApiEnvironment': "'production'", // String | Amazon SP API environment
  'amazonAccessToken': "amazonAccessToken_example", // String | MWS Auth Token. Access token authorizing the app to access resources on behalf of a user
  'amazonSellerId': "amazonSellerId_example", // String | Amazon Seller ID (Merchant token)
  'amazonMarketplacesIds': "amazonMarketplacesIds_example", // String | Amazon Marketplace IDs comma separated string
  'amazonSecretKey': "amazonSecretKey_example", // String | Amazon Secret Key
  'amazonAccessKeyId': "amazonAccessKeyId_example", // String | Amazon Secret Key Id
  'aspdotnetstorefrontApiUser': "aspdotnetstorefrontApiUser_example", // String | It's a AspDotNetStorefront account for which API is available
  'aspdotnetstorefrontApiPass': "aspdotnetstorefrontApiPass_example", // String | AspDotNetStorefront API Password
  'bigcommerceapiAdminAccount': "bigcommerceapiAdminAccount_example", // String | It's a BigCommerce account for which API is enabled
  'bigcommerceapiApiPath': "bigcommerceapiApiPath_example", // String | BigCommerce API URL
  'bigcommerceapiApiKey': "bigcommerceapiApiKey_example", // String | Bigcommerce API Key
  'bigcommerceapiClientId': "bigcommerceapiClientId_example", // String | Client ID of the requesting app
  'bigcommerceapiAccessToken': "bigcommerceapiAccessToken_example", // String | Access token authorizing the app to access resources on behalf of a user
  'bigcommerceapiContext': "bigcommerceapiContext_example", // String | API Path section unique to the store
  'demandwareClientId': "demandwareClientId_example", // String | Demandware client id
  'demandwareApiPassword': "demandwareApiPassword_example", // String | Demandware api password
  'demandwareUserName': "demandwareUserName_example", // String | Demandware user name
  'demandwareUserPassword': "demandwareUserPassword_example", // String | Demandware user password
  'ebayClientId': "ebayClientId_example", // String | Application ID (AppID).
  'ebayClientSecret': "ebayClientSecret_example", // String | Shared Secret from eBay application
  'ebayRuname': "ebayRuname_example", // String | The RuName value that eBay assigns to your application.
  'ebayAccessToken': "ebayAccessToken_example", // String | Used to authenticate API requests.
  'ebayRefreshToken': "ebayRefreshToken_example", // String | Used to renew the access token.
  'ebayEnvironment': "ebayEnvironment_example", // String | eBay environment
  'ebaySiteId': 0, // Number | eBay global ID
  'ecwidAcessToken': "ecwidAcessToken_example", // String | Access token authorizing the app to access resources on behalf of a user
  'ecwidStoreId': "ecwidStoreId_example", // String | Store Id
  'etsyKeystring': "etsyKeystring_example", // String | Etsy keystring
  'etsySharedSecret': "etsySharedSecret_example", // String | Etsy shared secret
  'etsyAccessToken': "etsyAccessToken_example", // String | Access token authorizing the app to access resources on behalf of a user
  'etsyTokenSecret': "etsyTokenSecret_example", // String | Secret token authorizing the app to access resources on behalf of a user
  'etsyClientId': "etsyClientId_example", // String | Etsy Client Id
  'etsyRefreshToken': "etsyRefreshToken_example", // String | Etsy Refresh token
  'netoApiKey': "netoApiKey_example", // String | Neto API Key
  'netoApiUsername': "netoApiUsername_example", // String | Neto User Name
  'shopifyApiKey': "shopifyApiKey_example", // String | Shopify API Key
  'shopifyApiPassword': "shopifyApiPassword_example", // String | Shopify API Password
  'shopifySharedSecret': "shopifySharedSecret_example", // String | Shared secret
  'shopifyAccessToken': "shopifyAccessToken_example", // String | Access token authorizing the app to access resources on behalf of a user
  'shopwareAccessKey': "shopwareAccessKey_example", // String | Shopware access key
  'shopwareApiKey': "shopwareApiKey_example", // String | Shopware api key
  'shopwareApiSecret': "shopwareApiSecret_example", // String | Shopware client secret access key
  'volusionLogin': "volusionLogin_example", // String | It's a Volusion account for which API is enabled
  'volusionPassword': "volusionPassword_example", // String | Volusion API Password
  'walmartClientId': "walmartClientId_example", // String | Walmart client ID
  'walmartClientSecret': "walmartClientSecret_example", // String | Walmart client secret
  'walmartEnvironment': "'production'", // String | Walmart environment
  'walmartChannelType': "walmartChannelType_example", // String | Walmart WM_CONSUMER.CHANNEL.TYPE header
  'squarespaceApiKey': "squarespaceApiKey_example", // String | Squarespace API Key
  'hybrisClientId': "hybrisClientId_example", // String | Omni Commerce Connector Client ID
  'hybrisClientSecret': "hybrisClientSecret_example", // String | Omni Commerce Connector Client Secret
  'hybrisUsername': "hybrisUsername_example", // String | User Name
  'hybrisPassword': "hybrisPassword_example", // String | User password
  'hybrisWebsites': ["null"], // [String] | Websites to stores mapping data
  'lightspeedApiKey': "lightspeedApiKey_example", // String | LightSpeed api key
  'lightspeedApiSecret': "lightspeedApiSecret_example", // String | LightSpeed api secret
  'commercehqApiKey': "commercehqApiKey_example", // String | CommerceHQ api key
  'commercehqApiPassword': "commercehqApiPassword_example", // String | CommerceHQ api password
  'wcConsumerKey': "wcConsumerKey_example", // String | Woocommerce consumer key
  'wcConsumerSecret': "wcConsumerSecret_example", // String | Woocommerce consumer secret
  'magentoConsumerKey': "magentoConsumerKey_example", // String | Magento Consumer Key
  'magentoConsumerSecret': "magentoConsumerSecret_example", // String | Magento Consumer Secret
  'magentoAccessToken': "magentoAccessToken_example", // String | Magento Access Token
  'magentoTokenSecret': "magentoTokenSecret_example", // String | Magento Token Secret
  'prestashopWebserviceKey': "prestashopWebserviceKey_example", // String | Prestashop webservice key
  'wixAppId': "wixAppId_example", // String | Wix App ID
  'wixAppSecretKey': "wixAppSecretKey_example", // String | Wix App Secret Key
  'wixRefreshToken': "wixRefreshToken_example", // String | Wix refresh token
  'mercadoLibreAppId': "mercadoLibreAppId_example", // String | Mercado Libre App ID
  'mercadoLibreAppSecretKey': "mercadoLibreAppSecretKey_example", // String | Mercado Libre App Secret Key
  'mercadoLibreRefreshToken': "mercadoLibreRefreshToken_example", // String | Mercado Libre Refresh Token
  'zidClientId': 56, // Number | Zid Client ID
  'zidClientSecret': "zidClientSecret_example", // String | Zid Client Secret
  'zidAccessToken': "zidAccessToken_example", // String | Zid Access Token
  'zidAuthorization': "zidAuthorization_example", // String | Zid Authorization
  'zidRefreshToken': "zidRefreshToken_example" // String | Zid refresh token
};
apiInstance.accountConfigUpdate(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **newStoreKey** | **String**| Update store key | [optional] 
 **bridgeUrl** | **String**| This parameter allows to set up store with custom bridge url (also you must use store_root parameter if a bridge folder is not in the root folder of the store) | [optional] 
 **storeRoot** | **String**| Absolute path to the store root directory (used with \&quot;bridge_url\&quot; parameter) | [optional] 
 **dbTablesPrefix** | **String**| DB tables prefix | [optional] 
 **_3dcartPrivateKey** | **String**| 3DCart Private Key | [optional] 
 **_3dcartAccessToken** | **String**| 3DCart Token | [optional] 
 **_3dcartapiApiKey** | **String**| 3DCart API Key | [optional] 
 **amazonSpClientId** | **String**| Amazon SP API app client id | [optional] 
 **amazonSpClientSecret** | **String**| Amazon SP API app client secret | [optional] 
 **amazonSpAwsUserKeyId** | **String**| Amazon AWS user access key ID | [optional] 
 **amazonSpAwsUserSecret** | **String**| Amazon AWS user secret access key | [optional] 
 **amazonSpAwsRegion** | **String**| Amazon AWS Region | [optional] 
 **amazonSpAwsRoleArn** | **String**| Amazon AWS Role ARN | [optional] 
 **amazonSpRefreshToken** | **String**| Amazon SP API OAuth refresh token | [optional] 
 **amazonSpApiEnvironment** | **String**| Amazon SP API environment | [optional] [default to &#39;production&#39;]
 **amazonAccessToken** | **String**| MWS Auth Token. Access token authorizing the app to access resources on behalf of a user | [optional] 
 **amazonSellerId** | **String**| Amazon Seller ID (Merchant token) | [optional] 
 **amazonMarketplacesIds** | **String**| Amazon Marketplace IDs comma separated string | [optional] 
 **amazonSecretKey** | **String**| Amazon Secret Key | [optional] 
 **amazonAccessKeyId** | **String**| Amazon Secret Key Id | [optional] 
 **aspdotnetstorefrontApiUser** | **String**| It&#39;s a AspDotNetStorefront account for which API is available | [optional] 
 **aspdotnetstorefrontApiPass** | **String**| AspDotNetStorefront API Password | [optional] 
 **bigcommerceapiAdminAccount** | **String**| It&#39;s a BigCommerce account for which API is enabled | [optional] 
 **bigcommerceapiApiPath** | **String**| BigCommerce API URL | [optional] 
 **bigcommerceapiApiKey** | **String**| Bigcommerce API Key | [optional] 
 **bigcommerceapiClientId** | **String**| Client ID of the requesting app | [optional] 
 **bigcommerceapiAccessToken** | **String**| Access token authorizing the app to access resources on behalf of a user | [optional] 
 **bigcommerceapiContext** | **String**| API Path section unique to the store | [optional] 
 **demandwareClientId** | **String**| Demandware client id | [optional] 
 **demandwareApiPassword** | **String**| Demandware api password | [optional] 
 **demandwareUserName** | **String**| Demandware user name | [optional] 
 **demandwareUserPassword** | **String**| Demandware user password | [optional] 
 **ebayClientId** | **String**| Application ID (AppID). | [optional] 
 **ebayClientSecret** | **String**| Shared Secret from eBay application | [optional] 
 **ebayRuname** | **String**| The RuName value that eBay assigns to your application. | [optional] 
 **ebayAccessToken** | **String**| Used to authenticate API requests. | [optional] 
 **ebayRefreshToken** | **String**| Used to renew the access token. | [optional] 
 **ebayEnvironment** | **String**| eBay environment | [optional] 
 **ebaySiteId** | **Number**| eBay global ID | [optional] [default to 0]
 **ecwidAcessToken** | **String**| Access token authorizing the app to access resources on behalf of a user | [optional] 
 **ecwidStoreId** | **String**| Store Id | [optional] 
 **etsyKeystring** | **String**| Etsy keystring | [optional] 
 **etsySharedSecret** | **String**| Etsy shared secret | [optional] 
 **etsyAccessToken** | **String**| Access token authorizing the app to access resources on behalf of a user | [optional] 
 **etsyTokenSecret** | **String**| Secret token authorizing the app to access resources on behalf of a user | [optional] 
 **etsyClientId** | **String**| Etsy Client Id | [optional] 
 **etsyRefreshToken** | **String**| Etsy Refresh token | [optional] 
 **netoApiKey** | **String**| Neto API Key | [optional] 
 **netoApiUsername** | **String**| Neto User Name | [optional] 
 **shopifyApiKey** | **String**| Shopify API Key | [optional] 
 **shopifyApiPassword** | **String**| Shopify API Password | [optional] 
 **shopifySharedSecret** | **String**| Shared secret | [optional] 
 **shopifyAccessToken** | **String**| Access token authorizing the app to access resources on behalf of a user | [optional] 
 **shopwareAccessKey** | **String**| Shopware access key | [optional] 
 **shopwareApiKey** | **String**| Shopware api key | [optional] 
 **shopwareApiSecret** | **String**| Shopware client secret access key | [optional] 
 **volusionLogin** | **String**| It&#39;s a Volusion account for which API is enabled | [optional] 
 **volusionPassword** | **String**| Volusion API Password | [optional] 
 **walmartClientId** | **String**| Walmart client ID | [optional] 
 **walmartClientSecret** | **String**| Walmart client secret | [optional] 
 **walmartEnvironment** | **String**| Walmart environment | [optional] [default to &#39;production&#39;]
 **walmartChannelType** | **String**| Walmart WM_CONSUMER.CHANNEL.TYPE header | [optional] 
 **squarespaceApiKey** | **String**| Squarespace API Key | [optional] 
 **hybrisClientId** | **String**| Omni Commerce Connector Client ID | [optional] 
 **hybrisClientSecret** | **String**| Omni Commerce Connector Client Secret | [optional] 
 **hybrisUsername** | **String**| User Name | [optional] 
 **hybrisPassword** | **String**| User password | [optional] 
 **hybrisWebsites** | [**[String]**](String.md)| Websites to stores mapping data | [optional] 
 **lightspeedApiKey** | **String**| LightSpeed api key | [optional] 
 **lightspeedApiSecret** | **String**| LightSpeed api secret | [optional] 
 **commercehqApiKey** | **String**| CommerceHQ api key | [optional] 
 **commercehqApiPassword** | **String**| CommerceHQ api password | [optional] 
 **wcConsumerKey** | **String**| Woocommerce consumer key | [optional] 
 **wcConsumerSecret** | **String**| Woocommerce consumer secret | [optional] 
 **magentoConsumerKey** | **String**| Magento Consumer Key | [optional] 
 **magentoConsumerSecret** | **String**| Magento Consumer Secret | [optional] 
 **magentoAccessToken** | **String**| Magento Access Token | [optional] 
 **magentoTokenSecret** | **String**| Magento Token Secret | [optional] 
 **prestashopWebserviceKey** | **String**| Prestashop webservice key | [optional] 
 **wixAppId** | **String**| Wix App ID | [optional] 
 **wixAppSecretKey** | **String**| Wix App Secret Key | [optional] 
 **wixRefreshToken** | **String**| Wix refresh token | [optional] 
 **mercadoLibreAppId** | **String**| Mercado Libre App ID | [optional] 
 **mercadoLibreAppSecretKey** | **String**| Mercado Libre App Secret Key | [optional] 
 **mercadoLibreRefreshToken** | **String**| Mercado Libre Refresh Token | [optional] 
 **zidClientId** | **Number**| Zid Client ID | [optional] 
 **zidClientSecret** | **String**| Zid Client Secret | [optional] 
 **zidAccessToken** | **String**| Zid Access Token | [optional] 
 **zidAuthorization** | **String**| Zid Authorization | [optional] 
 **zidRefreshToken** | **String**| Zid refresh token | [optional] 

### Return type

[**AccountConfigUpdate200Response**](AccountConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountFailedWebhooks

> AccountFailedWebhooks200Response accountFailedWebhooks(opts)



List webhooks that was not delivered to the callback.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.AccountApi();
let opts = {
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'ids': "ids_example" // String | List of сomma-separated webhook ids
};
apiInstance.accountFailedWebhooks(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **ids** | **String**| List of сomma-separated webhook ids | [optional] 

### Return type

[**AccountFailedWebhooks200Response**](AccountFailedWebhooks200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountSupportedPlatforms

> AccountSupportedPlatforms200Response accountSupportedPlatforms()



Get list of supported platforms

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.AccountApi();
apiInstance.accountSupportedPlatforms((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountSupportedPlatforms200Response**](AccountSupportedPlatforms200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

