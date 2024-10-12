# AppStoreReviewDetailsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appStoreReviewDetailsAppStoreReviewAttachmentsGetToManyRelated**](AppStoreReviewDetailsApi.md#appStoreReviewDetailsAppStoreReviewAttachmentsGetToManyRelated) | **GET** /v1/appStoreReviewDetails/{id}/appStoreReviewAttachments |  |
| [**appStoreReviewDetailsCreateInstance**](AppStoreReviewDetailsApi.md#appStoreReviewDetailsCreateInstance) | **POST** /v1/appStoreReviewDetails |  |
| [**appStoreReviewDetailsGetInstance**](AppStoreReviewDetailsApi.md#appStoreReviewDetailsGetInstance) | **GET** /v1/appStoreReviewDetails/{id} |  |
| [**appStoreReviewDetailsUpdateInstance**](AppStoreReviewDetailsApi.md#appStoreReviewDetailsUpdateInstance) | **PATCH** /v1/appStoreReviewDetails/{id} |  |


<a id="appStoreReviewDetailsAppStoreReviewAttachmentsGetToManyRelated"></a>
# **appStoreReviewDetailsAppStoreReviewAttachmentsGetToManyRelated**
> AppStoreReviewAttachmentsResponse appStoreReviewDetailsAppStoreReviewAttachmentsGetToManyRelated(id, fieldsAppStoreReviewDetails, fieldsAppStoreReviewAttachments, limit, include)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreReviewDetailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreReviewDetailsApi apiInstance = new AppStoreReviewDetailsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppStoreReviewDetails = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreReviewDetails
    List<String> fieldsAppStoreReviewAttachments = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreReviewAttachments
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    try {
      AppStoreReviewAttachmentsResponse result = apiInstance.appStoreReviewDetailsAppStoreReviewAttachmentsGetToManyRelated(id, fieldsAppStoreReviewDetails, fieldsAppStoreReviewAttachments, limit, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreReviewDetailsApi#appStoreReviewDetailsAppStoreReviewAttachmentsGetToManyRelated");
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
| **fieldsAppStoreReviewDetails** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreReviewDetails | [optional] [enum: appStoreReviewAttachments, appStoreVersion, contactEmail, contactFirstName, contactLastName, contactPhone, demoAccountName, demoAccountPassword, demoAccountRequired, notes] |
| **fieldsAppStoreReviewAttachments** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreReviewAttachments | [optional] [enum: appStoreReviewDetail, assetDeliveryState, fileName, fileSize, sourceFileChecksum, uploadOperations, uploaded] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: appStoreReviewDetail] |

### Return type

[**AppStoreReviewAttachmentsResponse**](AppStoreReviewAttachmentsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of related resources |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appStoreReviewDetailsCreateInstance"></a>
# **appStoreReviewDetailsCreateInstance**
> AppStoreReviewDetailResponse appStoreReviewDetailsCreateInstance(appStoreReviewDetailCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreReviewDetailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreReviewDetailsApi apiInstance = new AppStoreReviewDetailsApi(defaultClient);
    AppStoreReviewDetailCreateRequest appStoreReviewDetailCreateRequest = new AppStoreReviewDetailCreateRequest(); // AppStoreReviewDetailCreateRequest | AppStoreReviewDetail representation
    try {
      AppStoreReviewDetailResponse result = apiInstance.appStoreReviewDetailsCreateInstance(appStoreReviewDetailCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreReviewDetailsApi#appStoreReviewDetailsCreateInstance");
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
| **appStoreReviewDetailCreateRequest** | [**AppStoreReviewDetailCreateRequest**](AppStoreReviewDetailCreateRequest.md)| AppStoreReviewDetail representation | |

### Return type

[**AppStoreReviewDetailResponse**](AppStoreReviewDetailResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single AppStoreReviewDetail |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="appStoreReviewDetailsGetInstance"></a>
# **appStoreReviewDetailsGetInstance**
> AppStoreReviewDetailResponse appStoreReviewDetailsGetInstance(id, fieldsAppStoreReviewDetails, include, fieldsAppStoreReviewAttachments, limitAppStoreReviewAttachments)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreReviewDetailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreReviewDetailsApi apiInstance = new AppStoreReviewDetailsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppStoreReviewDetails = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreReviewDetails
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsAppStoreReviewAttachments = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreReviewAttachments
    Integer limitAppStoreReviewAttachments = 56; // Integer | maximum number of related appStoreReviewAttachments returned (when they are included)
    try {
      AppStoreReviewDetailResponse result = apiInstance.appStoreReviewDetailsGetInstance(id, fieldsAppStoreReviewDetails, include, fieldsAppStoreReviewAttachments, limitAppStoreReviewAttachments);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreReviewDetailsApi#appStoreReviewDetailsGetInstance");
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
| **fieldsAppStoreReviewDetails** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreReviewDetails | [optional] [enum: appStoreReviewAttachments, appStoreVersion, contactEmail, contactFirstName, contactLastName, contactPhone, demoAccountName, demoAccountPassword, demoAccountRequired, notes] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: appStoreReviewAttachments, appStoreVersion] |
| **fieldsAppStoreReviewAttachments** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreReviewAttachments | [optional] [enum: appStoreReviewDetail, assetDeliveryState, fileName, fileSize, sourceFileChecksum, uploadOperations, uploaded] |
| **limitAppStoreReviewAttachments** | **Integer**| maximum number of related appStoreReviewAttachments returned (when they are included) | [optional] |

### Return type

[**AppStoreReviewDetailResponse**](AppStoreReviewDetailResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single AppStoreReviewDetail |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appStoreReviewDetailsUpdateInstance"></a>
# **appStoreReviewDetailsUpdateInstance**
> AppStoreReviewDetailResponse appStoreReviewDetailsUpdateInstance(id, appStoreReviewDetailUpdateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreReviewDetailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreReviewDetailsApi apiInstance = new AppStoreReviewDetailsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    AppStoreReviewDetailUpdateRequest appStoreReviewDetailUpdateRequest = new AppStoreReviewDetailUpdateRequest(); // AppStoreReviewDetailUpdateRequest | AppStoreReviewDetail representation
    try {
      AppStoreReviewDetailResponse result = apiInstance.appStoreReviewDetailsUpdateInstance(id, appStoreReviewDetailUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreReviewDetailsApi#appStoreReviewDetailsUpdateInstance");
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
| **appStoreReviewDetailUpdateRequest** | [**AppStoreReviewDetailUpdateRequest**](AppStoreReviewDetailUpdateRequest.md)| AppStoreReviewDetail representation | |

### Return type

[**AppStoreReviewDetailResponse**](AppStoreReviewDetailResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single AppStoreReviewDetail |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

