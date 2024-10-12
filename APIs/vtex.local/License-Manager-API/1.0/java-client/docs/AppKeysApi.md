# AppKeysApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createnewappkey**](AppKeysApi.md#createnewappkey) | **POST** /api/vlm/appkeys | Create new appkey |
| [**getappkeysfromaccount**](AppKeysApi.md#getappkeysfromaccount) | **GET** /api/vlm/appkeys | Get appKeys from account |
| [**updateappkey**](AppKeysApi.md#updateappkey) | **PUT** /api/vlm/appkeys/{id} | Update appkey |


<a id="createnewappkey"></a>
# **createnewappkey**
> CreatenewappkeyResponse createnewappkey(createnewappkeyRequest)

Create new appkey

Creates a new pair of &#x60;appKey&#x60; and &#x60;appToken&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppKeysApi;

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

    AppKeysApi apiInstance = new AppKeysApi(defaultClient);
    CreatenewappkeyRequest createnewappkeyRequest = new CreatenewappkeyRequest(); // CreatenewappkeyRequest | 
    try {
      CreatenewappkeyResponse result = apiInstance.createnewappkey(createnewappkeyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppKeysApi#createnewappkey");
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
| **createnewappkeyRequest** | [**CreatenewappkeyRequest**](CreatenewappkeyRequest.md)|  | |

### Return type

[**CreatenewappkeyResponse**](CreatenewappkeyResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getappkeysfromaccount"></a>
# **getappkeysfromaccount**
> List&lt;Getappkeysfromaccount&gt; getappkeysfromaccount(contentType)

Get appKeys from account

Gets all application keys from an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppKeysApi;

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

    AppKeysApi apiInstance = new AppKeysApi(defaultClient);
    String contentType = "application/json"; // String | The media type of the body of the request. Default value for license manager protocol is application/json
    try {
      List<Getappkeysfromaccount> result = apiInstance.getappkeysfromaccount(contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppKeysApi#getappkeysfromaccount");
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
| **contentType** | **String**| The media type of the body of the request. Default value for license manager protocol is application/json | |

### Return type

[**List&lt;Getappkeysfromaccount&gt;**](Getappkeysfromaccount.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="updateappkey"></a>
# **updateappkey**
> updateappkey(id, updateappkeyRequest)

Update appkey

Activates or deactivates an &#x60;appKey&#x60; by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppKeysApi;

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

    AppKeysApi apiInstance = new AppKeysApi(defaultClient);
    String id = "id_example"; // String | ID from the appKey which will be updated
    UpdateappkeyRequest updateappkeyRequest = new UpdateappkeyRequest(); // UpdateappkeyRequest | Request body for updating AppKeys
    try {
      apiInstance.updateappkey(id, updateappkeyRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppKeysApi#updateappkey");
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
| **id** | **String**| ID from the appKey which will be updated | |
| **updateappkeyRequest** | [**UpdateappkeyRequest**](UpdateappkeyRequest.md)| Request body for updating AppKeys | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

