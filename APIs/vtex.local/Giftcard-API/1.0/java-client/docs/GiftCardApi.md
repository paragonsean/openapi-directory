# GiftCardApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createGiftCard**](GiftCardApi.md#createGiftCard) | **POST** /giftcards | Create GiftCard |
| [**getGiftCardbyID**](GiftCardApi.md#getGiftCardbyID) | **GET** /giftcards/{giftCardID} | Get GiftCard by ID |
| [**getGiftCardusingJSON**](GiftCardApi.md#getGiftCardusingJSON) | **POST** /giftcards/_search | Get GiftCard using JSON |


<a id="createGiftCard"></a>
# **createGiftCard**
> Response createGiftCard(contentType, accept, xVTEXAPIAppKey, xVTEXAPIAppToken, createGiftCardRequest)

Create GiftCard

Creates a GiftCard for a specific user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GiftCardApi;

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

    GiftCardApi apiInstance = new GiftCardApi(defaultClient);
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String xVTEXAPIAppKey = "{{X-VTEX-API-AppKey}}"; // String | The AppKey configured by the merchant
    String xVTEXAPIAppToken = "{{X-VTEX-API-AppToken}}"; // String | The AppToken configured by the merchant
    CreateGiftCardRequest createGiftCardRequest = new CreateGiftCardRequest(); // CreateGiftCardRequest | 
    try {
      Response result = apiInstance.createGiftCard(contentType, accept, xVTEXAPIAppKey, xVTEXAPIAppToken, createGiftCardRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GiftCardApi#createGiftCard");
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
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **xVTEXAPIAppKey** | **String**| The AppKey configured by the merchant | [default to {{X-VTEX-API-AppKey}}] |
| **xVTEXAPIAppToken** | **String**| The AppToken configured by the merchant | [default to {{X-VTEX-API-AppToken}}] |
| **createGiftCardRequest** | [**CreateGiftCardRequest**](CreateGiftCardRequest.md)|  | |

### Return type

[**Response**](Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/vnd.vtex.giftcard.v1+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getGiftCardbyID"></a>
# **getGiftCardbyID**
> Response getGiftCardbyID(accept, contentType, giftCardID)

Get GiftCard by ID

Returns associated data for a specified giftcardId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GiftCardApi;

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

    GiftCardApi apiInstance = new GiftCardApi(defaultClient);
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    String giftCardID = "2"; // String | 
    try {
      Response result = apiInstance.getGiftCardbyID(accept, contentType, giftCardID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GiftCardApi#getGiftCardbyID");
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
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **giftCardID** | **String**|  | [default to 2] |

### Return type

[**Response**](Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getGiftCardusingJSON"></a>
# **getGiftCardusingJSON**
> Response2 getGiftCardusingJSON(accept, contentType, getGiftCardusingJSONRequest, reSTRange)

Get GiftCard using JSON

Returns the giftcards based on the cart data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GiftCardApi;

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

    GiftCardApi apiInstance = new GiftCardApi(defaultClient);
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    GetGiftCardusingJSONRequest getGiftCardusingJSONRequest = new GetGiftCardusingJSONRequest(); // GetGiftCardusingJSONRequest | 
    String reSTRange = "giftcard=0-49"; // String | PaginationB control.B ThisB queryB variableB mustB followB theB formatB _resources={from}-{to}_.
    try {
      Response2 result = apiInstance.getGiftCardusingJSON(accept, contentType, getGiftCardusingJSONRequest, reSTRange);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GiftCardApi#getGiftCardusingJSON");
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
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **getGiftCardusingJSONRequest** | [**GetGiftCardusingJSONRequest**](GetGiftCardusingJSONRequest.md)|  | |
| **reSTRange** | **String**| PaginationB control.B ThisB queryB variableB mustB followB theB formatB _resources&#x3D;{from}-{to}_. | [optional] [default to giftcard&#x3D;0-49] |

### Return type

[**Response2**](Response2.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

