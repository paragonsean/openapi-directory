# TokenApi

All URIs are relative to *https://ob.nordigen.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jWTObtain**](TokenApi.md#jWTObtain) | **POST** /api/v2/token/new/ |  |
| [**jWTRefresh**](TokenApi.md#jWTRefresh) | **POST** /api/v2/token/refresh/ |  |


<a id="jWTObtain"></a>
# **jWTObtain**
> SpectacularJWTObtain jWTObtain(jwTObtainPairRequest)



Obtain JWT pair

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    TokenApi apiInstance = new TokenApi(defaultClient);
    JWTObtainPairRequest jwTObtainPairRequest = new JWTObtainPairRequest(); // JWTObtainPairRequest | 
    try {
      SpectacularJWTObtain result = apiInstance.jWTObtain(jwTObtainPairRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokenApi#jWTObtain");
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
| **jwTObtainPairRequest** | [**JWTObtainPairRequest**](JWTObtainPairRequest.md)|  | |

### Return type

[**SpectacularJWTObtain**](SpectacularJWTObtain.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Obtain JWT response. |  -  |
| **401** | Authentication failed |  -  |
| **403** | IP Access denied |  -  |
| **429** | Nordigen rate limit exceeded |  -  |

<a id="jWTRefresh"></a>
# **jWTRefresh**
> SpectacularJWTRefresh jWTRefresh(jwTRefreshRequest)



Refresh access token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    TokenApi apiInstance = new TokenApi(defaultClient);
    JWTRefreshRequest jwTRefreshRequest = new JWTRefreshRequest(); // JWTRefreshRequest | 
    try {
      SpectacularJWTRefresh result = apiInstance.jWTRefresh(jwTRefreshRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokenApi#jWTRefresh");
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
| **jwTRefreshRequest** | [**JWTRefreshRequest**](JWTRefreshRequest.md)|  | |

### Return type

[**SpectacularJWTRefresh**](SpectacularJWTRefresh.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Refresh access token. |  -  |
| **401** | Invalid token |  -  |
| **403** | IP Access denied |  -  |
| **429** | Nordigen rate limit exceeded |  -  |

