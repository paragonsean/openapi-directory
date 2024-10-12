# GdprApi

All URIs are relative to *https://api.appcenter.ms*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dataSubjectRightCancelDeleteRequest**](GdprApi.md#dataSubjectRightCancelDeleteRequest) | **POST** /v0.1/user/dsr/delete/{token}/cancel |  |
| [**dataSubjectRightCancelExportRequest**](GdprApi.md#dataSubjectRightCancelExportRequest) | **POST** /v0.1/user/dsr/export/{token}/cancel |  |
| [**dataSubjectRightDeleteRequest**](GdprApi.md#dataSubjectRightDeleteRequest) | **POST** /v0.1/user/dsr/delete |  |
| [**dataSubjectRightDeleteStatusRequest**](GdprApi.md#dataSubjectRightDeleteStatusRequest) | **GET** /v0.1/user/dsr/delete/{token} |  |
| [**dataSubjectRightExportRequest**](GdprApi.md#dataSubjectRightExportRequest) | **POST** /v0.1/user/dsr/export |  |
| [**dataSubjectRightExportStatusRequest**](GdprApi.md#dataSubjectRightExportStatusRequest) | **GET** /v0.1/user/dsr/export/{token} |  |


<a id="dataSubjectRightCancelDeleteRequest"></a>
# **dataSubjectRightCancelDeleteRequest**
> DataSubjectRightDeleteRequest202Response dataSubjectRightCancelDeleteRequest(token, dataSubjectRightCancelDeleteRequestRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GdprApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    GdprApi apiInstance = new GdprApi(defaultClient);
    UUID token = UUID.randomUUID(); // UUID | Unique request ID (GUID)
    DataSubjectRightCancelDeleteRequestRequest dataSubjectRightCancelDeleteRequestRequest = new DataSubjectRightCancelDeleteRequestRequest(); // DataSubjectRightCancelDeleteRequestRequest | 
    try {
      DataSubjectRightDeleteRequest202Response result = apiInstance.dataSubjectRightCancelDeleteRequest(token, dataSubjectRightCancelDeleteRequestRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GdprApi#dataSubjectRightCancelDeleteRequest");
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
| **token** | **UUID**| Unique request ID (GUID) | |
| **dataSubjectRightCancelDeleteRequestRequest** | [**DataSubjectRightCancelDeleteRequestRequest**](DataSubjectRightCancelDeleteRequestRequest.md)|  | [optional] |

### Return type

[**DataSubjectRightDeleteRequest202Response**](DataSubjectRightDeleteRequest202Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Data subject right cancel delete request has been accepted. |  * Location - Link to get details about the cancel export. <br>  |
| **503** | Cancel delete request cannot be processed yet. |  -  |
| **0** | Error code with reason |  -  |

<a id="dataSubjectRightCancelExportRequest"></a>
# **dataSubjectRightCancelExportRequest**
> DataSubjectRightDeleteRequest202Response dataSubjectRightCancelExportRequest(token)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GdprApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    GdprApi apiInstance = new GdprApi(defaultClient);
    UUID token = UUID.randomUUID(); // UUID | Unique request ID (GUID)
    try {
      DataSubjectRightDeleteRequest202Response result = apiInstance.dataSubjectRightCancelExportRequest(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GdprApi#dataSubjectRightCancelExportRequest");
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
| **token** | **UUID**| Unique request ID (GUID) | |

### Return type

[**DataSubjectRightDeleteRequest202Response**](DataSubjectRightDeleteRequest202Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Data subject right cancel export request has been accepted. |  * Location - Link to get details about the cancel export. <br>  |
| **503** | Cancel export request cannot be processed yet. |  -  |
| **0** | Error code with reason |  -  |

<a id="dataSubjectRightDeleteRequest"></a>
# **dataSubjectRightDeleteRequest**
> DataSubjectRightDeleteRequest202Response dataSubjectRightDeleteRequest()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GdprApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    GdprApi apiInstance = new GdprApi(defaultClient);
    try {
      DataSubjectRightDeleteRequest202Response result = apiInstance.dataSubjectRightDeleteRequest();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GdprApi#dataSubjectRightDeleteRequest");
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

[**DataSubjectRightDeleteRequest202Response**](DataSubjectRightDeleteRequest202Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Data subject right delete request has been accepted. |  * Location - Link to get details about the cancel export. <br>  |
| **0** | Error code with reason |  -  |

<a id="dataSubjectRightDeleteStatusRequest"></a>
# **dataSubjectRightDeleteStatusRequest**
> DataSubjectRightDeleteStatusRequest200Response dataSubjectRightDeleteStatusRequest(token, email)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GdprApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    GdprApi apiInstance = new GdprApi(defaultClient);
    UUID token = UUID.randomUUID(); // UUID | Unique request ID (GUID)
    String email = "email_example"; // String | Email used for delete with x-authz-bypass headers
    try {
      DataSubjectRightDeleteStatusRequest200Response result = apiInstance.dataSubjectRightDeleteStatusRequest(token, email);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GdprApi#dataSubjectRightDeleteStatusRequest");
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
| **token** | **UUID**| Unique request ID (GUID) | |
| **email** | **String**| Email used for delete with x-authz-bypass headers | |

### Return type

[**DataSubjectRightDeleteStatusRequest200Response**](DataSubjectRightDeleteStatusRequest200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data subject right delete request status successfully retrieved. |  -  |
| **0** | Error code with reason |  -  |

<a id="dataSubjectRightExportRequest"></a>
# **dataSubjectRightExportRequest**
> DataSubjectRightDeleteRequest202Response dataSubjectRightExportRequest()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GdprApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    GdprApi apiInstance = new GdprApi(defaultClient);
    try {
      DataSubjectRightDeleteRequest202Response result = apiInstance.dataSubjectRightExportRequest();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GdprApi#dataSubjectRightExportRequest");
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

[**DataSubjectRightDeleteRequest202Response**](DataSubjectRightDeleteRequest202Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Data subject right export request has been accepted. |  * Location - Link to get details about the cancel export. <br>  |
| **0** | Error code with reason |  -  |

<a id="dataSubjectRightExportStatusRequest"></a>
# **dataSubjectRightExportStatusRequest**
> DataSubjectRightDeleteStatusRequest200Response dataSubjectRightExportStatusRequest(token)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GdprApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    GdprApi apiInstance = new GdprApi(defaultClient);
    UUID token = UUID.randomUUID(); // UUID | Unique request ID (GUID)
    try {
      DataSubjectRightDeleteStatusRequest200Response result = apiInstance.dataSubjectRightExportStatusRequest(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GdprApi#dataSubjectRightExportStatusRequest");
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
| **token** | **UUID**| Unique request ID (GUID) | |

### Return type

[**DataSubjectRightDeleteStatusRequest200Response**](DataSubjectRightDeleteStatusRequest200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data subject right export request status successfully retrieved. |  -  |
| **0** | Error code with reason |  -  |

