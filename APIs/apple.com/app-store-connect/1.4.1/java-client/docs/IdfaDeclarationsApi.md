# IdfaDeclarationsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**idfaDeclarationsCreateInstance**](IdfaDeclarationsApi.md#idfaDeclarationsCreateInstance) | **POST** /v1/idfaDeclarations |  |
| [**idfaDeclarationsDeleteInstance**](IdfaDeclarationsApi.md#idfaDeclarationsDeleteInstance) | **DELETE** /v1/idfaDeclarations/{id} |  |
| [**idfaDeclarationsUpdateInstance**](IdfaDeclarationsApi.md#idfaDeclarationsUpdateInstance) | **PATCH** /v1/idfaDeclarations/{id} |  |


<a id="idfaDeclarationsCreateInstance"></a>
# **idfaDeclarationsCreateInstance**
> IdfaDeclarationResponse idfaDeclarationsCreateInstance(idfaDeclarationCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdfaDeclarationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    IdfaDeclarationsApi apiInstance = new IdfaDeclarationsApi(defaultClient);
    IdfaDeclarationCreateRequest idfaDeclarationCreateRequest = new IdfaDeclarationCreateRequest(); // IdfaDeclarationCreateRequest | IdfaDeclaration representation
    try {
      IdfaDeclarationResponse result = apiInstance.idfaDeclarationsCreateInstance(idfaDeclarationCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdfaDeclarationsApi#idfaDeclarationsCreateInstance");
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
| **idfaDeclarationCreateRequest** | [**IdfaDeclarationCreateRequest**](IdfaDeclarationCreateRequest.md)| IdfaDeclaration representation | |

### Return type

[**IdfaDeclarationResponse**](IdfaDeclarationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single IdfaDeclaration |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="idfaDeclarationsDeleteInstance"></a>
# **idfaDeclarationsDeleteInstance**
> idfaDeclarationsDeleteInstance(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdfaDeclarationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    IdfaDeclarationsApi apiInstance = new IdfaDeclarationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    try {
      apiInstance.idfaDeclarationsDeleteInstance(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdfaDeclarationsApi#idfaDeclarationsDeleteInstance");
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
| **id** | **String**| the id of the requested resource | |

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success (no content) |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="idfaDeclarationsUpdateInstance"></a>
# **idfaDeclarationsUpdateInstance**
> IdfaDeclarationResponse idfaDeclarationsUpdateInstance(id, idfaDeclarationUpdateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdfaDeclarationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    IdfaDeclarationsApi apiInstance = new IdfaDeclarationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    IdfaDeclarationUpdateRequest idfaDeclarationUpdateRequest = new IdfaDeclarationUpdateRequest(); // IdfaDeclarationUpdateRequest | IdfaDeclaration representation
    try {
      IdfaDeclarationResponse result = apiInstance.idfaDeclarationsUpdateInstance(id, idfaDeclarationUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdfaDeclarationsApi#idfaDeclarationsUpdateInstance");
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
| **id** | **String**| the id of the requested resource | |
| **idfaDeclarationUpdateRequest** | [**IdfaDeclarationUpdateRequest**](IdfaDeclarationUpdateRequest.md)| IdfaDeclaration representation | |

### Return type

[**IdfaDeclarationResponse**](IdfaDeclarationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single IdfaDeclaration |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

