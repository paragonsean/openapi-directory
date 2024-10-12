# UtilityApi

All URIs are relative to *https://go.netlicensing.io/core/v2/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**licenseTypes**](UtilityApi.md#licenseTypes) | **GET** /utility/licenseTypes | List License Types |
| [**licensingModels**](UtilityApi.md#licensingModels) | **GET** /utility/licensingModels | List Licensing Models |


<a id="licenseTypes"></a>
# **licenseTypes**
> Netlicensing licenseTypes()

List License Types

Return a list of all License Types supported by the service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    UtilityApi apiInstance = new UtilityApi(defaultClient);
    try {
      Netlicensing result = apiInstance.licenseTypes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilityApi#licenseTypes");
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

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

<a id="licensingModels"></a>
# **licensingModels**
> Netlicensing licensingModels()

List Licensing Models

Return a list of all licensing models supported by the service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    UtilityApi apiInstance = new UtilityApi(defaultClient);
    try {
      Netlicensing result = apiInstance.licensingModels();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilityApi#licensingModels");
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

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

