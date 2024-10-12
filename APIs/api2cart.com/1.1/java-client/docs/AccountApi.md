# AccountApi

All URIs are relative to *https://api.api2cart.com/v1.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountCartAdd**](AccountApi.md#accountCartAdd) | **POST** /account.cart.add.json |  |
| [**accountCartList**](AccountApi.md#accountCartList) | **GET** /account.cart.list.json |  |
| [**accountConfigUpdate**](AccountApi.md#accountConfigUpdate) | **PUT** /account.config.update.json |  |
| [**accountFailedWebhooks**](AccountApi.md#accountFailedWebhooks) | **GET** /account.failed_webhooks.json |  |
| [**accountSupportedPlatforms**](AccountApi.md#accountSupportedPlatforms) | **GET** /account.supported_platforms.json |  |


<a id="accountCartAdd"></a>
# **accountCartAdd**
> AccountCartAdd200Response accountCartAdd(accountCartAdd)



Add store to the account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    AccountCartAdd accountCartAdd = new AccountCartAdd(); // AccountCartAdd | 
    try {
      AccountCartAdd200Response result = apiInstance.accountCartAdd(accountCartAdd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountCartAdd");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountCartAdd** | [**AccountCartAdd**](AccountCartAdd.md)|  | |

### Return type

[**AccountCartAdd200Response**](AccountCartAdd200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="accountCartList"></a>
# **accountCartList**
> AccountCartList200Response accountCartList(params, exclude, requestFromDate, requestToDate, storeUrl, storeKey)



Get list of carts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String params = "force_all"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String requestFromDate = "requestFromDate_example"; // String | Retrieve entities from their creation date
    String requestToDate = "requestToDate_example"; // String | Retrieve entities to their creation date
    String storeUrl = "storeUrl_example"; // String | A web address of a store
    String storeKey = "storeKey_example"; // String | Find store by store key
    try {
      AccountCartList200Response result = apiInstance.accountCartList(params, exclude, requestFromDate, requestToDate, storeUrl, storeKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountCartList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to force_all] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **requestFromDate** | **String**| Retrieve entities from their creation date | [optional] |
| **requestToDate** | **String**| Retrieve entities to their creation date | [optional] |
| **storeUrl** | **String**| A web address of a store | [optional] |
| **storeKey** | **String**| Find store by store key | [optional] |

### Return type

[**AccountCartList200Response**](AccountCartList200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="accountConfigUpdate"></a>
# **accountConfigUpdate**
> AccountConfigUpdate200Response accountConfigUpdate(newStoreKey, bridgeUrl, storeRoot, dbTablesPrefix, _3dcartPrivateKey, _3dcartAccessToken, _3dcartapiApiKey, amazonSpClientId, amazonSpClientSecret, amazonSpAwsUserKeyId, amazonSpAwsUserSecret, amazonSpAwsRegion, amazonSpAwsRoleArn, amazonSpRefreshToken, amazonSpApiEnvironment, amazonAccessToken, amazonSellerId, amazonMarketplacesIds, amazonSecretKey, amazonAccessKeyId, aspdotnetstorefrontApiUser, aspdotnetstorefrontApiPass, bigcommerceapiAdminAccount, bigcommerceapiApiPath, bigcommerceapiApiKey, bigcommerceapiClientId, bigcommerceapiAccessToken, bigcommerceapiContext, demandwareClientId, demandwareApiPassword, demandwareUserName, demandwareUserPassword, ebayClientId, ebayClientSecret, ebayRuname, ebayAccessToken, ebayRefreshToken, ebayEnvironment, ebaySiteId, ecwidAcessToken, ecwidStoreId, etsyKeystring, etsySharedSecret, etsyAccessToken, etsyTokenSecret, etsyClientId, etsyRefreshToken, netoApiKey, netoApiUsername, shopifyApiKey, shopifyApiPassword, shopifySharedSecret, shopifyAccessToken, shopwareAccessKey, shopwareApiKey, shopwareApiSecret, volusionLogin, volusionPassword, walmartClientId, walmartClientSecret, walmartEnvironment, walmartChannelType, squarespaceApiKey, hybrisClientId, hybrisClientSecret, hybrisUsername, hybrisPassword, hybrisWebsites, lightspeedApiKey, lightspeedApiSecret, commercehqApiKey, commercehqApiPassword, wcConsumerKey, wcConsumerSecret, magentoConsumerKey, magentoConsumerSecret, magentoAccessToken, magentoTokenSecret, prestashopWebserviceKey, wixAppId, wixAppSecretKey, wixRefreshToken, mercadoLibreAppId, mercadoLibreAppSecretKey, mercadoLibreRefreshToken, zidClientId, zidClientSecret, zidAccessToken, zidAuthorization, zidRefreshToken)



Update configs in the API2Cart database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String newStoreKey = "newStoreKey_example"; // String | Update store key
    String bridgeUrl = "bridgeUrl_example"; // String | This parameter allows to set up store with custom bridge url (also you must use store_root parameter if a bridge folder is not in the root folder of the store)
    String storeRoot = "storeRoot_example"; // String | Absolute path to the store root directory (used with \"bridge_url\" parameter)
    String dbTablesPrefix = "dbTablesPrefix_example"; // String | DB tables prefix
    String _3dcartPrivateKey = "_3dcartPrivateKey_example"; // String | 3DCart Private Key
    String _3dcartAccessToken = "_3dcartAccessToken_example"; // String | 3DCart Token
    String _3dcartapiApiKey = "_3dcartapiApiKey_example"; // String | 3DCart API Key
    String amazonSpClientId = "amazonSpClientId_example"; // String | Amazon SP API app client id
    String amazonSpClientSecret = "amazonSpClientSecret_example"; // String | Amazon SP API app client secret
    String amazonSpAwsUserKeyId = "amazonSpAwsUserKeyId_example"; // String | Amazon AWS user access key ID
    String amazonSpAwsUserSecret = "amazonSpAwsUserSecret_example"; // String | Amazon AWS user secret access key
    String amazonSpAwsRegion = "amazonSpAwsRegion_example"; // String | Amazon AWS Region
    String amazonSpAwsRoleArn = "amazonSpAwsRoleArn_example"; // String | Amazon AWS Role ARN
    String amazonSpRefreshToken = "amazonSpRefreshToken_example"; // String | Amazon SP API OAuth refresh token
    String amazonSpApiEnvironment = "production"; // String | Amazon SP API environment
    String amazonAccessToken = "amazonAccessToken_example"; // String | MWS Auth Token. Access token authorizing the app to access resources on behalf of a user
    String amazonSellerId = "amazonSellerId_example"; // String | Amazon Seller ID (Merchant token)
    String amazonMarketplacesIds = "amazonMarketplacesIds_example"; // String | Amazon Marketplace IDs comma separated string
    String amazonSecretKey = "amazonSecretKey_example"; // String | Amazon Secret Key
    String amazonAccessKeyId = "amazonAccessKeyId_example"; // String | Amazon Secret Key Id
    String aspdotnetstorefrontApiUser = "aspdotnetstorefrontApiUser_example"; // String | It's a AspDotNetStorefront account for which API is available
    String aspdotnetstorefrontApiPass = "aspdotnetstorefrontApiPass_example"; // String | AspDotNetStorefront API Password
    String bigcommerceapiAdminAccount = "bigcommerceapiAdminAccount_example"; // String | It's a BigCommerce account for which API is enabled
    String bigcommerceapiApiPath = "bigcommerceapiApiPath_example"; // String | BigCommerce API URL
    String bigcommerceapiApiKey = "bigcommerceapiApiKey_example"; // String | Bigcommerce API Key
    String bigcommerceapiClientId = "bigcommerceapiClientId_example"; // String | Client ID of the requesting app
    String bigcommerceapiAccessToken = "bigcommerceapiAccessToken_example"; // String | Access token authorizing the app to access resources on behalf of a user
    String bigcommerceapiContext = "bigcommerceapiContext_example"; // String | API Path section unique to the store
    String demandwareClientId = "demandwareClientId_example"; // String | Demandware client id
    String demandwareApiPassword = "demandwareApiPassword_example"; // String | Demandware api password
    String demandwareUserName = "demandwareUserName_example"; // String | Demandware user name
    String demandwareUserPassword = "demandwareUserPassword_example"; // String | Demandware user password
    String ebayClientId = "ebayClientId_example"; // String | Application ID (AppID).
    String ebayClientSecret = "ebayClientSecret_example"; // String | Shared Secret from eBay application
    String ebayRuname = "ebayRuname_example"; // String | The RuName value that eBay assigns to your application.
    String ebayAccessToken = "ebayAccessToken_example"; // String | Used to authenticate API requests.
    String ebayRefreshToken = "ebayRefreshToken_example"; // String | Used to renew the access token.
    String ebayEnvironment = "ebayEnvironment_example"; // String | eBay environment
    Integer ebaySiteId = 0; // Integer | eBay global ID
    String ecwidAcessToken = "ecwidAcessToken_example"; // String | Access token authorizing the app to access resources on behalf of a user
    String ecwidStoreId = "ecwidStoreId_example"; // String | Store Id
    String etsyKeystring = "etsyKeystring_example"; // String | Etsy keystring
    String etsySharedSecret = "etsySharedSecret_example"; // String | Etsy shared secret
    String etsyAccessToken = "etsyAccessToken_example"; // String | Access token authorizing the app to access resources on behalf of a user
    String etsyTokenSecret = "etsyTokenSecret_example"; // String | Secret token authorizing the app to access resources on behalf of a user
    String etsyClientId = "etsyClientId_example"; // String | Etsy Client Id
    String etsyRefreshToken = "etsyRefreshToken_example"; // String | Etsy Refresh token
    String netoApiKey = "netoApiKey_example"; // String | Neto API Key
    String netoApiUsername = "netoApiUsername_example"; // String | Neto User Name
    String shopifyApiKey = "shopifyApiKey_example"; // String | Shopify API Key
    String shopifyApiPassword = "shopifyApiPassword_example"; // String | Shopify API Password
    String shopifySharedSecret = "shopifySharedSecret_example"; // String | Shared secret
    String shopifyAccessToken = "shopifyAccessToken_example"; // String | Access token authorizing the app to access resources on behalf of a user
    String shopwareAccessKey = "shopwareAccessKey_example"; // String | Shopware access key
    String shopwareApiKey = "shopwareApiKey_example"; // String | Shopware api key
    String shopwareApiSecret = "shopwareApiSecret_example"; // String | Shopware client secret access key
    String volusionLogin = "volusionLogin_example"; // String | It's a Volusion account for which API is enabled
    String volusionPassword = "volusionPassword_example"; // String | Volusion API Password
    String walmartClientId = "walmartClientId_example"; // String | Walmart client ID
    String walmartClientSecret = "walmartClientSecret_example"; // String | Walmart client secret
    String walmartEnvironment = "production"; // String | Walmart environment
    String walmartChannelType = "walmartChannelType_example"; // String | Walmart WM_CONSUMER.CHANNEL.TYPE header
    String squarespaceApiKey = "squarespaceApiKey_example"; // String | Squarespace API Key
    String hybrisClientId = "hybrisClientId_example"; // String | Omni Commerce Connector Client ID
    String hybrisClientSecret = "hybrisClientSecret_example"; // String | Omni Commerce Connector Client Secret
    String hybrisUsername = "hybrisUsername_example"; // String | User Name
    String hybrisPassword = "hybrisPassword_example"; // String | User password
    List<String> hybrisWebsites = Arrays.asList(); // List<String> | Websites to stores mapping data
    String lightspeedApiKey = "lightspeedApiKey_example"; // String | LightSpeed api key
    String lightspeedApiSecret = "lightspeedApiSecret_example"; // String | LightSpeed api secret
    String commercehqApiKey = "commercehqApiKey_example"; // String | CommerceHQ api key
    String commercehqApiPassword = "commercehqApiPassword_example"; // String | CommerceHQ api password
    String wcConsumerKey = "wcConsumerKey_example"; // String | Woocommerce consumer key
    String wcConsumerSecret = "wcConsumerSecret_example"; // String | Woocommerce consumer secret
    String magentoConsumerKey = "magentoConsumerKey_example"; // String | Magento Consumer Key
    String magentoConsumerSecret = "magentoConsumerSecret_example"; // String | Magento Consumer Secret
    String magentoAccessToken = "magentoAccessToken_example"; // String | Magento Access Token
    String magentoTokenSecret = "magentoTokenSecret_example"; // String | Magento Token Secret
    String prestashopWebserviceKey = "prestashopWebserviceKey_example"; // String | Prestashop webservice key
    String wixAppId = "wixAppId_example"; // String | Wix App ID
    String wixAppSecretKey = "wixAppSecretKey_example"; // String | Wix App Secret Key
    String wixRefreshToken = "wixRefreshToken_example"; // String | Wix refresh token
    String mercadoLibreAppId = "mercadoLibreAppId_example"; // String | Mercado Libre App ID
    String mercadoLibreAppSecretKey = "mercadoLibreAppSecretKey_example"; // String | Mercado Libre App Secret Key
    String mercadoLibreRefreshToken = "mercadoLibreRefreshToken_example"; // String | Mercado Libre Refresh Token
    Integer zidClientId = 56; // Integer | Zid Client ID
    String zidClientSecret = "zidClientSecret_example"; // String | Zid Client Secret
    String zidAccessToken = "zidAccessToken_example"; // String | Zid Access Token
    String zidAuthorization = "zidAuthorization_example"; // String | Zid Authorization
    String zidRefreshToken = "zidRefreshToken_example"; // String | Zid refresh token
    try {
      AccountConfigUpdate200Response result = apiInstance.accountConfigUpdate(newStoreKey, bridgeUrl, storeRoot, dbTablesPrefix, _3dcartPrivateKey, _3dcartAccessToken, _3dcartapiApiKey, amazonSpClientId, amazonSpClientSecret, amazonSpAwsUserKeyId, amazonSpAwsUserSecret, amazonSpAwsRegion, amazonSpAwsRoleArn, amazonSpRefreshToken, amazonSpApiEnvironment, amazonAccessToken, amazonSellerId, amazonMarketplacesIds, amazonSecretKey, amazonAccessKeyId, aspdotnetstorefrontApiUser, aspdotnetstorefrontApiPass, bigcommerceapiAdminAccount, bigcommerceapiApiPath, bigcommerceapiApiKey, bigcommerceapiClientId, bigcommerceapiAccessToken, bigcommerceapiContext, demandwareClientId, demandwareApiPassword, demandwareUserName, demandwareUserPassword, ebayClientId, ebayClientSecret, ebayRuname, ebayAccessToken, ebayRefreshToken, ebayEnvironment, ebaySiteId, ecwidAcessToken, ecwidStoreId, etsyKeystring, etsySharedSecret, etsyAccessToken, etsyTokenSecret, etsyClientId, etsyRefreshToken, netoApiKey, netoApiUsername, shopifyApiKey, shopifyApiPassword, shopifySharedSecret, shopifyAccessToken, shopwareAccessKey, shopwareApiKey, shopwareApiSecret, volusionLogin, volusionPassword, walmartClientId, walmartClientSecret, walmartEnvironment, walmartChannelType, squarespaceApiKey, hybrisClientId, hybrisClientSecret, hybrisUsername, hybrisPassword, hybrisWebsites, lightspeedApiKey, lightspeedApiSecret, commercehqApiKey, commercehqApiPassword, wcConsumerKey, wcConsumerSecret, magentoConsumerKey, magentoConsumerSecret, magentoAccessToken, magentoTokenSecret, prestashopWebserviceKey, wixAppId, wixAppSecretKey, wixRefreshToken, mercadoLibreAppId, mercadoLibreAppSecretKey, mercadoLibreRefreshToken, zidClientId, zidClientSecret, zidAccessToken, zidAuthorization, zidRefreshToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountConfigUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **newStoreKey** | **String**| Update store key | [optional] |
| **bridgeUrl** | **String**| This parameter allows to set up store with custom bridge url (also you must use store_root parameter if a bridge folder is not in the root folder of the store) | [optional] |
| **storeRoot** | **String**| Absolute path to the store root directory (used with \&quot;bridge_url\&quot; parameter) | [optional] |
| **dbTablesPrefix** | **String**| DB tables prefix | [optional] |
| **_3dcartPrivateKey** | **String**| 3DCart Private Key | [optional] |
| **_3dcartAccessToken** | **String**| 3DCart Token | [optional] |
| **_3dcartapiApiKey** | **String**| 3DCart API Key | [optional] |
| **amazonSpClientId** | **String**| Amazon SP API app client id | [optional] |
| **amazonSpClientSecret** | **String**| Amazon SP API app client secret | [optional] |
| **amazonSpAwsUserKeyId** | **String**| Amazon AWS user access key ID | [optional] |
| **amazonSpAwsUserSecret** | **String**| Amazon AWS user secret access key | [optional] |
| **amazonSpAwsRegion** | **String**| Amazon AWS Region | [optional] |
| **amazonSpAwsRoleArn** | **String**| Amazon AWS Role ARN | [optional] |
| **amazonSpRefreshToken** | **String**| Amazon SP API OAuth refresh token | [optional] |
| **amazonSpApiEnvironment** | **String**| Amazon SP API environment | [optional] [default to production] |
| **amazonAccessToken** | **String**| MWS Auth Token. Access token authorizing the app to access resources on behalf of a user | [optional] |
| **amazonSellerId** | **String**| Amazon Seller ID (Merchant token) | [optional] |
| **amazonMarketplacesIds** | **String**| Amazon Marketplace IDs comma separated string | [optional] |
| **amazonSecretKey** | **String**| Amazon Secret Key | [optional] |
| **amazonAccessKeyId** | **String**| Amazon Secret Key Id | [optional] |
| **aspdotnetstorefrontApiUser** | **String**| It&#39;s a AspDotNetStorefront account for which API is available | [optional] |
| **aspdotnetstorefrontApiPass** | **String**| AspDotNetStorefront API Password | [optional] |
| **bigcommerceapiAdminAccount** | **String**| It&#39;s a BigCommerce account for which API is enabled | [optional] |
| **bigcommerceapiApiPath** | **String**| BigCommerce API URL | [optional] |
| **bigcommerceapiApiKey** | **String**| Bigcommerce API Key | [optional] |
| **bigcommerceapiClientId** | **String**| Client ID of the requesting app | [optional] |
| **bigcommerceapiAccessToken** | **String**| Access token authorizing the app to access resources on behalf of a user | [optional] |
| **bigcommerceapiContext** | **String**| API Path section unique to the store | [optional] |
| **demandwareClientId** | **String**| Demandware client id | [optional] |
| **demandwareApiPassword** | **String**| Demandware api password | [optional] |
| **demandwareUserName** | **String**| Demandware user name | [optional] |
| **demandwareUserPassword** | **String**| Demandware user password | [optional] |
| **ebayClientId** | **String**| Application ID (AppID). | [optional] |
| **ebayClientSecret** | **String**| Shared Secret from eBay application | [optional] |
| **ebayRuname** | **String**| The RuName value that eBay assigns to your application. | [optional] |
| **ebayAccessToken** | **String**| Used to authenticate API requests. | [optional] |
| **ebayRefreshToken** | **String**| Used to renew the access token. | [optional] |
| **ebayEnvironment** | **String**| eBay environment | [optional] |
| **ebaySiteId** | **Integer**| eBay global ID | [optional] [default to 0] |
| **ecwidAcessToken** | **String**| Access token authorizing the app to access resources on behalf of a user | [optional] |
| **ecwidStoreId** | **String**| Store Id | [optional] |
| **etsyKeystring** | **String**| Etsy keystring | [optional] |
| **etsySharedSecret** | **String**| Etsy shared secret | [optional] |
| **etsyAccessToken** | **String**| Access token authorizing the app to access resources on behalf of a user | [optional] |
| **etsyTokenSecret** | **String**| Secret token authorizing the app to access resources on behalf of a user | [optional] |
| **etsyClientId** | **String**| Etsy Client Id | [optional] |
| **etsyRefreshToken** | **String**| Etsy Refresh token | [optional] |
| **netoApiKey** | **String**| Neto API Key | [optional] |
| **netoApiUsername** | **String**| Neto User Name | [optional] |
| **shopifyApiKey** | **String**| Shopify API Key | [optional] |
| **shopifyApiPassword** | **String**| Shopify API Password | [optional] |
| **shopifySharedSecret** | **String**| Shared secret | [optional] |
| **shopifyAccessToken** | **String**| Access token authorizing the app to access resources on behalf of a user | [optional] |
| **shopwareAccessKey** | **String**| Shopware access key | [optional] |
| **shopwareApiKey** | **String**| Shopware api key | [optional] |
| **shopwareApiSecret** | **String**| Shopware client secret access key | [optional] |
| **volusionLogin** | **String**| It&#39;s a Volusion account for which API is enabled | [optional] |
| **volusionPassword** | **String**| Volusion API Password | [optional] |
| **walmartClientId** | **String**| Walmart client ID | [optional] |
| **walmartClientSecret** | **String**| Walmart client secret | [optional] |
| **walmartEnvironment** | **String**| Walmart environment | [optional] [default to production] |
| **walmartChannelType** | **String**| Walmart WM_CONSUMER.CHANNEL.TYPE header | [optional] |
| **squarespaceApiKey** | **String**| Squarespace API Key | [optional] |
| **hybrisClientId** | **String**| Omni Commerce Connector Client ID | [optional] |
| **hybrisClientSecret** | **String**| Omni Commerce Connector Client Secret | [optional] |
| **hybrisUsername** | **String**| User Name | [optional] |
| **hybrisPassword** | **String**| User password | [optional] |
| **hybrisWebsites** | [**List&lt;String&gt;**](String.md)| Websites to stores mapping data | [optional] |
| **lightspeedApiKey** | **String**| LightSpeed api key | [optional] |
| **lightspeedApiSecret** | **String**| LightSpeed api secret | [optional] |
| **commercehqApiKey** | **String**| CommerceHQ api key | [optional] |
| **commercehqApiPassword** | **String**| CommerceHQ api password | [optional] |
| **wcConsumerKey** | **String**| Woocommerce consumer key | [optional] |
| **wcConsumerSecret** | **String**| Woocommerce consumer secret | [optional] |
| **magentoConsumerKey** | **String**| Magento Consumer Key | [optional] |
| **magentoConsumerSecret** | **String**| Magento Consumer Secret | [optional] |
| **magentoAccessToken** | **String**| Magento Access Token | [optional] |
| **magentoTokenSecret** | **String**| Magento Token Secret | [optional] |
| **prestashopWebserviceKey** | **String**| Prestashop webservice key | [optional] |
| **wixAppId** | **String**| Wix App ID | [optional] |
| **wixAppSecretKey** | **String**| Wix App Secret Key | [optional] |
| **wixRefreshToken** | **String**| Wix refresh token | [optional] |
| **mercadoLibreAppId** | **String**| Mercado Libre App ID | [optional] |
| **mercadoLibreAppSecretKey** | **String**| Mercado Libre App Secret Key | [optional] |
| **mercadoLibreRefreshToken** | **String**| Mercado Libre Refresh Token | [optional] |
| **zidClientId** | **Integer**| Zid Client ID | [optional] |
| **zidClientSecret** | **String**| Zid Client Secret | [optional] |
| **zidAccessToken** | **String**| Zid Access Token | [optional] |
| **zidAuthorization** | **String**| Zid Authorization | [optional] |
| **zidRefreshToken** | **String**| Zid refresh token | [optional] |

### Return type

[**AccountConfigUpdate200Response**](AccountConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="accountFailedWebhooks"></a>
# **accountFailedWebhooks**
> AccountFailedWebhooks200Response accountFailedWebhooks(count, start, ids)



List webhooks that was not delivered to the callback.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    String ids = "ids_example"; // String | List of сomma-separated webhook ids
    try {
      AccountFailedWebhooks200Response result = apiInstance.accountFailedWebhooks(count, start, ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountFailedWebhooks");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **ids** | **String**| List of сomma-separated webhook ids | [optional] |

### Return type

[**AccountFailedWebhooks200Response**](AccountFailedWebhooks200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="accountSupportedPlatforms"></a>
# **accountSupportedPlatforms**
> AccountSupportedPlatforms200Response accountSupportedPlatforms()



Get list of supported platforms

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      AccountSupportedPlatforms200Response result = apiInstance.accountSupportedPlatforms();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountSupportedPlatforms");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

