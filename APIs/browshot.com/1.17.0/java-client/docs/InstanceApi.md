# InstanceApi

All URIs are relative to *https://api.browshot.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getInstanceInfo**](InstanceApi.md#getInstanceInfo) | **GET** /instance/info | Get information about an instance |
| [**getInstancesInfo**](InstanceApi.md#getInstancesInfo) | **GET** /instance/list | Get all instances |


<a id="getInstanceInfo"></a>
# **getInstanceInfo**
> Instance getInstanceInfo(id)

Get information about an instance

Get information about an instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.browshot.com/api/v1");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    InstanceApi apiInstance = new InstanceApi(defaultClient);
    Integer id = 56; // Integer | instance ID
    try {
      Instance result = apiInstance.getInstanceInfo(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceApi#getInstanceInfo");
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
| **id** | **Integer**| instance ID | |

### Return type

[**Instance**](Instance.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Instance information |  -  |
| **0** | Account not found |  -  |

<a id="getInstancesInfo"></a>
# **getInstancesInfo**
> InstanceList getInstancesInfo()

Get all instances

Get all instances.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.browshot.com/api/v1");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    InstanceApi apiInstance = new InstanceApi(defaultClient);
    try {
      InstanceList result = apiInstance.getInstancesInfo();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceApi#getInstancesInfo");
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

[**InstanceList**](InstanceList.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Instance information |  -  |
| **0** | Account not found |  -  |

