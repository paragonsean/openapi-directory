# AppStoreReviewAttachmentsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appStoreReviewAttachmentsCreateInstance**](AppStoreReviewAttachmentsApi.md#appStoreReviewAttachmentsCreateInstance) | **POST** /v1/appStoreReviewAttachments |  |
| [**appStoreReviewAttachmentsDeleteInstance**](AppStoreReviewAttachmentsApi.md#appStoreReviewAttachmentsDeleteInstance) | **DELETE** /v1/appStoreReviewAttachments/{id} |  |
| [**appStoreReviewAttachmentsGetInstance**](AppStoreReviewAttachmentsApi.md#appStoreReviewAttachmentsGetInstance) | **GET** /v1/appStoreReviewAttachments/{id} |  |
| [**appStoreReviewAttachmentsUpdateInstance**](AppStoreReviewAttachmentsApi.md#appStoreReviewAttachmentsUpdateInstance) | **PATCH** /v1/appStoreReviewAttachments/{id} |  |


<a id="appStoreReviewAttachmentsCreateInstance"></a>
# **appStoreReviewAttachmentsCreateInstance**
> AppStoreReviewAttachmentResponse appStoreReviewAttachmentsCreateInstance(appStoreReviewAttachmentCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreReviewAttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreReviewAttachmentsApi apiInstance = new AppStoreReviewAttachmentsApi(defaultClient);
    AppStoreReviewAttachmentCreateRequest appStoreReviewAttachmentCreateRequest = new AppStoreReviewAttachmentCreateRequest(); // AppStoreReviewAttachmentCreateRequest | AppStoreReviewAttachment representation
    try {
      AppStoreReviewAttachmentResponse result = apiInstance.appStoreReviewAttachmentsCreateInstance(appStoreReviewAttachmentCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreReviewAttachmentsApi#appStoreReviewAttachmentsCreateInstance");
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
| **appStoreReviewAttachmentCreateRequest** | [**AppStoreReviewAttachmentCreateRequest**](AppStoreReviewAttachmentCreateRequest.md)| AppStoreReviewAttachment representation | |

### Return type

[**AppStoreReviewAttachmentResponse**](AppStoreReviewAttachmentResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single AppStoreReviewAttachment |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="appStoreReviewAttachmentsDeleteInstance"></a>
# **appStoreReviewAttachmentsDeleteInstance**
> appStoreReviewAttachmentsDeleteInstance(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreReviewAttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreReviewAttachmentsApi apiInstance = new AppStoreReviewAttachmentsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    try {
      apiInstance.appStoreReviewAttachmentsDeleteInstance(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreReviewAttachmentsApi#appStoreReviewAttachmentsDeleteInstance");
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

<a id="appStoreReviewAttachmentsGetInstance"></a>
# **appStoreReviewAttachmentsGetInstance**
> AppStoreReviewAttachmentResponse appStoreReviewAttachmentsGetInstance(id, fieldsAppStoreReviewAttachments, include)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreReviewAttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreReviewAttachmentsApi apiInstance = new AppStoreReviewAttachmentsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppStoreReviewAttachments = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreReviewAttachments
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    try {
      AppStoreReviewAttachmentResponse result = apiInstance.appStoreReviewAttachmentsGetInstance(id, fieldsAppStoreReviewAttachments, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreReviewAttachmentsApi#appStoreReviewAttachmentsGetInstance");
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
| **fieldsAppStoreReviewAttachments** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreReviewAttachments | [optional] [enum: appStoreReviewDetail, assetDeliveryState, fileName, fileSize, sourceFileChecksum, uploadOperations, uploaded] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: appStoreReviewDetail] |

### Return type

[**AppStoreReviewAttachmentResponse**](AppStoreReviewAttachmentResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single AppStoreReviewAttachment |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appStoreReviewAttachmentsUpdateInstance"></a>
# **appStoreReviewAttachmentsUpdateInstance**
> AppStoreReviewAttachmentResponse appStoreReviewAttachmentsUpdateInstance(id, appStoreReviewAttachmentUpdateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreReviewAttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreReviewAttachmentsApi apiInstance = new AppStoreReviewAttachmentsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    AppStoreReviewAttachmentUpdateRequest appStoreReviewAttachmentUpdateRequest = new AppStoreReviewAttachmentUpdateRequest(); // AppStoreReviewAttachmentUpdateRequest | AppStoreReviewAttachment representation
    try {
      AppStoreReviewAttachmentResponse result = apiInstance.appStoreReviewAttachmentsUpdateInstance(id, appStoreReviewAttachmentUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreReviewAttachmentsApi#appStoreReviewAttachmentsUpdateInstance");
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
| **appStoreReviewAttachmentUpdateRequest** | [**AppStoreReviewAttachmentUpdateRequest**](AppStoreReviewAttachmentUpdateRequest.md)| AppStoreReviewAttachment representation | |

### Return type

[**AppStoreReviewAttachmentResponse**](AppStoreReviewAttachmentResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single AppStoreReviewAttachment |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

