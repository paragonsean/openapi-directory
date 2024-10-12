# DefaultApi

All URIs are relative to *http://microcks.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getResource**](DefaultApi.md#getResource) | **GET** /resources/{name} | Get Resource |
| [**getResourcesByService**](DefaultApi.md#getResourcesByService) | **GET** /resources/service/{serviceId} | Get Resources by Service |


<a id="getResource"></a>
# **getResource**
> Resource getResource(name)

Get Resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | Unique name/business identifier of the Service or API resource
    try {
      Resource result = apiInstance.getResource(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getResource");
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
| **name** | **String**| Unique name/business identifier of the Service or API resource | |

### Return type

[**Resource**](Resource.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieve the resource having this name |  -  |

<a id="getResourcesByService"></a>
# **getResourcesByService**
> List&lt;Resource&gt; getResourcesByService(serviceId)

Get Resources by Service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String serviceId = "serviceId_example"; // String | Unique identifier of the Service or API the resources are attached to
    try {
      List<Resource> result = apiInstance.getResourcesByService(serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getResourcesByService");
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
| **serviceId** | **String**| Unique identifier of the Service or API the resources are attached to | |

### Return type

[**List&lt;Resource&gt;**](Resource.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List the resources attached to a Service or API |  -  |

