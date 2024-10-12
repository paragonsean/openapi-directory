# OpenApiApi

All URIs are relative to *http://superset.apache.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**openapiVersionOpenapiGet**](OpenApiApi.md#openapiVersionOpenapiGet) | **GET** /openapi/{version}/_openapi |  |


<a id="openapiVersionOpenapiGet"></a>
# **openapiVersionOpenapiGet**
> Object openapiVersionOpenapiGet(version)



Get the OpenAPI spec for a specific API version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    OpenApiApi apiInstance = new OpenApiApi(defaultClient);
    String version = "version_example"; // String | 
    try {
      Object result = apiInstance.openapiVersionOpenapiGet(version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenApiApi#openapiVersionOpenapiGet");
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
| **version** | **String**|  | |

### Return type

**Object**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The OpenAPI spec |  -  |
| **404** | Not found |  -  |
| **500** | Fatal error |  -  |

