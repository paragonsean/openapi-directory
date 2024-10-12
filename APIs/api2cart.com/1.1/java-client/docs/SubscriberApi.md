# SubscriberApi

All URIs are relative to *https://api.api2cart.com/v1.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**subscriberList**](SubscriberApi.md#subscriberList) | **GET** /subscriber.list.json |  |


<a id="subscriberList"></a>
# **subscriberList**
> SubscriberList200Response subscriberList(start, count, subscribed, storeId, email, params, exclude, createdFrom, createdTo, modifiedFrom, modifiedTo, pageCursor, responseFields)



Get subscribers list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriberApi;

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

    SubscriberApi apiInstance = new SubscriberApi(defaultClient);
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    Boolean subscribed = true; // Boolean | Filter by subscription status
    String storeId = "storeId_example"; // String | Store Id
    String email = "email_example"; // String | Filter subscribers by email
    String params = "force_all"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String createdFrom = "createdFrom_example"; // String | Retrieve entities from their creation date
    String createdTo = "createdTo_example"; // String | Retrieve entities to their creation date
    String modifiedFrom = "modifiedFrom_example"; // String | Retrieve entities from their modification date
    String modifiedTo = "modifiedTo_example"; // String | Retrieve entities to their modification date
    String pageCursor = "pageCursor_example"; // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    try {
      SubscriberList200Response result = apiInstance.subscriberList(start, count, subscribed, storeId, email, params, exclude, createdFrom, createdTo, modifiedFrom, modifiedTo, pageCursor, responseFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriberApi#subscriberList");
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
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **subscribed** | **Boolean**| Filter by subscription status | [optional] |
| **storeId** | **String**| Store Id | [optional] |
| **email** | **String**| Filter subscribers by email | [optional] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to force_all] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **createdFrom** | **String**| Retrieve entities from their creation date | [optional] |
| **createdTo** | **String**| Retrieve entities to their creation date | [optional] |
| **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] |
| **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] |
| **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |

### Return type

[**SubscriberList200Response**](SubscriberList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

