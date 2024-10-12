# UserApi

All URIs are relative to *https://ibl.api.bbci.co.uk/ibl/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getUserStorePurchases**](UserApi.md#getUserStorePurchases) | **GET** /user/purchases | Get user store purchases |
| [**getUserStoreRecommendations**](UserApi.md#getUserStoreRecommendations) | **GET** /user/recommendations | Get user store recommendations |
| [**getUserWatching**](UserApi.md#getUserWatching) | **GET** /user/watching | Get user watching |


<a id="getUserStorePurchases"></a>
# **getUserStorePurchases**
> Object getUserStorePurchases(identityCookie)

Get user store purchases

Get user store purchases

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");
    
    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    UserApi apiInstance = new UserApi(defaultClient);
    Double identityCookie = 3.4D; // Double | The BBC-id cookie value
    try {
      Object result = apiInstance.getUserStorePurchases(identityCookie);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#getUserStorePurchases");
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
| **identityCookie** | **Double**| The BBC-id cookie value | |

### Return type

**Object**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="getUserStoreRecommendations"></a>
# **getUserStoreRecommendations**
> Object getUserStoreRecommendations(identityCookie)

Get user store recommendations

Get user store recommendations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    UserApi apiInstance = new UserApi(defaultClient);
    Double identityCookie = 3.4D; // Double | The BBC-id cookie value
    try {
      Object result = apiInstance.getUserStoreRecommendations(identityCookie);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#getUserStoreRecommendations");
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
| **identityCookie** | **Double**| The BBC-id cookie value | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="getUserWatching"></a>
# **getUserWatching**
> Object getUserWatching(identityCookie)

Get user watching

Get user watching

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    UserApi apiInstance = new UserApi(defaultClient);
    Double identityCookie = 3.4D; // Double | The BBC-id cookie value
    try {
      Object result = apiInstance.getUserWatching(identityCookie);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#getUserWatching");
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
| **identityCookie** | **Double**| The BBC-id cookie value | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

