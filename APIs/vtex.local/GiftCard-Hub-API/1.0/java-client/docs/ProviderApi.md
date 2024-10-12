# ProviderApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createUpdateGiftCardProviderbyID**](ProviderApi.md#createUpdateGiftCardProviderbyID) | **PUT** /giftcardproviders/{giftCardProviderID} | Create/Update GiftCard Provider by ID |
| [**deleteGiftCardProviderbyID**](ProviderApi.md#deleteGiftCardProviderbyID) | **DELETE** /giftcardproviders/{giftCardProviderID} | Delete GiftCard Provider by ID |
| [**getGiftCardProviderbyID**](ProviderApi.md#getGiftCardProviderbyID) | **GET** /giftcardproviders/{giftCardProviderId} | Get GiftCard Provider by ID |
| [**listAllGiftCardProviders**](ProviderApi.md#listAllGiftCardProviders) | **GET** /giftcardproviders | List All GiftCard Providers |


<a id="createUpdateGiftCardProviderbyID"></a>
# **createUpdateGiftCardProviderbyID**
> Object createUpdateGiftCardProviderbyID(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, giftCardProviderID, createUpdateGiftCardProviderbyIDRequest)

Create/Update GiftCard Provider by ID

Create or update a giftcard provider from a store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProviderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ProviderApi apiInstance = new ProviderApi(defaultClient);
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json.
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    String xVTEXAPIAppKey = "{{X-VTEX-API-AppKey}}"; // String | VTEX API AppKey
    String xVTEXAPIAppToken = "{{X-VTEX-API-AppToken}}"; // String | VTEX API AppToken
    String giftCardProviderID = "insert identifier here"; // String | Gift Card provider's ID.
    CreateUpdateGiftCardProviderbyIDRequest createUpdateGiftCardProviderbyIDRequest = new CreateUpdateGiftCardProviderbyIDRequest(); // CreateUpdateGiftCardProviderbyIDRequest | 
    try {
      Object result = apiInstance.createUpdateGiftCardProviderbyID(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, giftCardProviderID, createUpdateGiftCardProviderbyIDRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProviderApi#createUpdateGiftCardProviderbyID");
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
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json. | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **xVTEXAPIAppKey** | **String**| VTEX API AppKey | [default to {{X-VTEX-API-AppKey}}] |
| **xVTEXAPIAppToken** | **String**| VTEX API AppToken | [default to {{X-VTEX-API-AppToken}}] |
| **giftCardProviderID** | **String**| Gift Card provider&#39;s ID. | [default to insert identifier here] |
| **createUpdateGiftCardProviderbyIDRequest** | [**CreateUpdateGiftCardProviderbyIDRequest**](CreateUpdateGiftCardProviderbyIDRequest.md)|  | |

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/vnd.vtex.giftcardproviders.v1+json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="deleteGiftCardProviderbyID"></a>
# **deleteGiftCardProviderbyID**
> Object deleteGiftCardProviderbyID(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, giftCardProviderID)

Delete GiftCard Provider by ID

Delete a giftcard provider from a store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProviderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ProviderApi apiInstance = new ProviderApi(defaultClient);
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json.
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json.
    String xVTEXAPIAppKey = "{{X-VTEX-API-AppKey}}"; // String | VTEX API AppKey
    String xVTEXAPIAppToken = "{{X-VTEX-API-AppToken}}"; // String | VTEX API AppToken
    String giftCardProviderID = "insert identifier here"; // String | Gift Card provider's ID.
    try {
      Object result = apiInstance.deleteGiftCardProviderbyID(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, giftCardProviderID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProviderApi#deleteGiftCardProviderbyID");
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
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json. | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json. | [default to application/json] |
| **xVTEXAPIAppKey** | **String**| VTEX API AppKey | [default to {{X-VTEX-API-AppKey}}] |
| **xVTEXAPIAppToken** | **String**| VTEX API AppToken | [default to {{X-VTEX-API-AppToken}}] |
| **giftCardProviderID** | **String**| Gift Card provider&#39;s ID. | [default to insert identifier here] |

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | O provider não existe.  |  -  |

<a id="getGiftCardProviderbyID"></a>
# **getGiftCardProviderbyID**
> Object getGiftCardProviderbyID(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, giftCardProviderId)

Get GiftCard Provider by ID

Returns a giftcard provider from a store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProviderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ProviderApi apiInstance = new ProviderApi(defaultClient);
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json.
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json.
    String xVTEXAPIAppKey = "{{X-VTEX-API-AppKey}}"; // String | VTEX API AppKey
    String xVTEXAPIAppToken = "{{X-VTEX-API-AppToken}}"; // String | VTEX API AppToken
    String giftCardProviderId = "insert identifier here"; // String | Gift Card provider's ID.
    try {
      Object result = apiInstance.getGiftCardProviderbyID(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, giftCardProviderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProviderApi#getGiftCardProviderbyID");
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
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json. | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json. | [default to application/json] |
| **xVTEXAPIAppKey** | **String**| VTEX API AppKey | [default to {{X-VTEX-API-AppKey}}] |
| **xVTEXAPIAppToken** | **String**| VTEX API AppToken | [default to {{X-VTEX-API-AppToken}}] |
| **giftCardProviderId** | **String**| Gift Card provider&#39;s ID. | [default to insert identifier here] |

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | O provider não existe.  |  -  |

<a id="listAllGiftCardProviders"></a>
# **listAllGiftCardProviders**
> Object listAllGiftCardProviders(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, reSTRange)

List All GiftCard Providers

Returns a collection of giftcard providers from a store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProviderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    ProviderApi apiInstance = new ProviderApi(defaultClient);
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json.
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json.
    String xVTEXAPIAppKey = "{{X-VTEX-API-AppKey}}"; // String | VTEX API AppKey
    String xVTEXAPIAppToken = "{{X-VTEX-API-AppToken}}"; // String | VTEX API AppToken
    String reSTRange = "resources=0-49"; // String | Pagination control. This query variable must follow the format _resources={from}-{to}_.
    try {
      Object result = apiInstance.listAllGiftCardProviders(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, reSTRange);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProviderApi#listAllGiftCardProviders");
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
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json. | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json. | [default to application/json] |
| **xVTEXAPIAppKey** | **String**| VTEX API AppKey | [default to {{X-VTEX-API-AppKey}}] |
| **xVTEXAPIAppToken** | **String**| VTEX API AppToken | [default to {{X-VTEX-API-AppToken}}] |
| **reSTRange** | **String**| Pagination control. This query variable must follow the format _resources&#x3D;{from}-{to}_. | [optional] [default to resources&#x3D;0-49] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

