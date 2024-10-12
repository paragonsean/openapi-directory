# AppScreenshotSetsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appScreenshotSetsAppScreenshotsGetToManyRelated**](AppScreenshotSetsApi.md#appScreenshotSetsAppScreenshotsGetToManyRelated) | **GET** /v1/appScreenshotSets/{id}/appScreenshots |  |
| [**appScreenshotSetsAppScreenshotsGetToManyRelationship**](AppScreenshotSetsApi.md#appScreenshotSetsAppScreenshotsGetToManyRelationship) | **GET** /v1/appScreenshotSets/{id}/relationships/appScreenshots |  |
| [**appScreenshotSetsAppScreenshotsReplaceToManyRelationship**](AppScreenshotSetsApi.md#appScreenshotSetsAppScreenshotsReplaceToManyRelationship) | **PATCH** /v1/appScreenshotSets/{id}/relationships/appScreenshots |  |
| [**appScreenshotSetsCreateInstance**](AppScreenshotSetsApi.md#appScreenshotSetsCreateInstance) | **POST** /v1/appScreenshotSets |  |
| [**appScreenshotSetsDeleteInstance**](AppScreenshotSetsApi.md#appScreenshotSetsDeleteInstance) | **DELETE** /v1/appScreenshotSets/{id} |  |
| [**appScreenshotSetsGetInstance**](AppScreenshotSetsApi.md#appScreenshotSetsGetInstance) | **GET** /v1/appScreenshotSets/{id} |  |


<a id="appScreenshotSetsAppScreenshotsGetToManyRelated"></a>
# **appScreenshotSetsAppScreenshotsGetToManyRelated**
> AppScreenshotsResponse appScreenshotSetsAppScreenshotsGetToManyRelated(id, fieldsAppScreenshotSets, fieldsAppScreenshots, limit, include)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppScreenshotSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppScreenshotSetsApi apiInstance = new AppScreenshotSetsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppScreenshotSets = Arrays.asList(); // List<String> | the fields to include for returned resources of type appScreenshotSets
    List<String> fieldsAppScreenshots = Arrays.asList(); // List<String> | the fields to include for returned resources of type appScreenshots
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    try {
      AppScreenshotsResponse result = apiInstance.appScreenshotSetsAppScreenshotsGetToManyRelated(id, fieldsAppScreenshotSets, fieldsAppScreenshots, limit, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppScreenshotSetsApi#appScreenshotSetsAppScreenshotsGetToManyRelated");
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
| **fieldsAppScreenshotSets** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appScreenshotSets | [optional] [enum: appScreenshots, appStoreVersionLocalization, screenshotDisplayType] |
| **fieldsAppScreenshots** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appScreenshots | [optional] [enum: appScreenshotSet, assetDeliveryState, assetToken, assetType, fileName, fileSize, imageAsset, sourceFileChecksum, uploadOperations, uploaded] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: appScreenshotSet] |

### Return type

[**AppScreenshotsResponse**](AppScreenshotsResponse.md)

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

<a id="appScreenshotSetsAppScreenshotsGetToManyRelationship"></a>
# **appScreenshotSetsAppScreenshotsGetToManyRelationship**
> AppScreenshotSetAppScreenshotsLinkagesResponse appScreenshotSetsAppScreenshotsGetToManyRelationship(id, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppScreenshotSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppScreenshotSetsApi apiInstance = new AppScreenshotSetsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    Integer limit = 56; // Integer | maximum resources per page
    try {
      AppScreenshotSetAppScreenshotsLinkagesResponse result = apiInstance.appScreenshotSetsAppScreenshotsGetToManyRelationship(id, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppScreenshotSetsApi#appScreenshotSetsAppScreenshotsGetToManyRelationship");
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
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**AppScreenshotSetAppScreenshotsLinkagesResponse**](AppScreenshotSetAppScreenshotsLinkagesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of related linkages |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appScreenshotSetsAppScreenshotsReplaceToManyRelationship"></a>
# **appScreenshotSetsAppScreenshotsReplaceToManyRelationship**
> appScreenshotSetsAppScreenshotsReplaceToManyRelationship(id, appScreenshotSetAppScreenshotsLinkagesRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppScreenshotSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppScreenshotSetsApi apiInstance = new AppScreenshotSetsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    AppScreenshotSetAppScreenshotsLinkagesRequest appScreenshotSetAppScreenshotsLinkagesRequest = new AppScreenshotSetAppScreenshotsLinkagesRequest(); // AppScreenshotSetAppScreenshotsLinkagesRequest | List of related linkages
    try {
      apiInstance.appScreenshotSetsAppScreenshotsReplaceToManyRelationship(id, appScreenshotSetAppScreenshotsLinkagesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppScreenshotSetsApi#appScreenshotSetsAppScreenshotsReplaceToManyRelationship");
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
| **appScreenshotSetAppScreenshotsLinkagesRequest** | [**AppScreenshotSetAppScreenshotsLinkagesRequest**](AppScreenshotSetAppScreenshotsLinkagesRequest.md)| List of related linkages | |

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success (no content) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="appScreenshotSetsCreateInstance"></a>
# **appScreenshotSetsCreateInstance**
> AppScreenshotSetResponse appScreenshotSetsCreateInstance(appScreenshotSetCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppScreenshotSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppScreenshotSetsApi apiInstance = new AppScreenshotSetsApi(defaultClient);
    AppScreenshotSetCreateRequest appScreenshotSetCreateRequest = new AppScreenshotSetCreateRequest(); // AppScreenshotSetCreateRequest | AppScreenshotSet representation
    try {
      AppScreenshotSetResponse result = apiInstance.appScreenshotSetsCreateInstance(appScreenshotSetCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppScreenshotSetsApi#appScreenshotSetsCreateInstance");
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
| **appScreenshotSetCreateRequest** | [**AppScreenshotSetCreateRequest**](AppScreenshotSetCreateRequest.md)| AppScreenshotSet representation | |

### Return type

[**AppScreenshotSetResponse**](AppScreenshotSetResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single AppScreenshotSet |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="appScreenshotSetsDeleteInstance"></a>
# **appScreenshotSetsDeleteInstance**
> appScreenshotSetsDeleteInstance(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppScreenshotSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppScreenshotSetsApi apiInstance = new AppScreenshotSetsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    try {
      apiInstance.appScreenshotSetsDeleteInstance(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppScreenshotSetsApi#appScreenshotSetsDeleteInstance");
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

<a id="appScreenshotSetsGetInstance"></a>
# **appScreenshotSetsGetInstance**
> AppScreenshotSetResponse appScreenshotSetsGetInstance(id, fieldsAppScreenshotSets, include, fieldsAppScreenshots, limitAppScreenshots)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppScreenshotSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppScreenshotSetsApi apiInstance = new AppScreenshotSetsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppScreenshotSets = Arrays.asList(); // List<String> | the fields to include for returned resources of type appScreenshotSets
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsAppScreenshots = Arrays.asList(); // List<String> | the fields to include for returned resources of type appScreenshots
    Integer limitAppScreenshots = 56; // Integer | maximum number of related appScreenshots returned (when they are included)
    try {
      AppScreenshotSetResponse result = apiInstance.appScreenshotSetsGetInstance(id, fieldsAppScreenshotSets, include, fieldsAppScreenshots, limitAppScreenshots);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppScreenshotSetsApi#appScreenshotSetsGetInstance");
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
| **fieldsAppScreenshotSets** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appScreenshotSets | [optional] [enum: appScreenshots, appStoreVersionLocalization, screenshotDisplayType] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: appScreenshots, appStoreVersionLocalization] |
| **fieldsAppScreenshots** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appScreenshots | [optional] [enum: appScreenshotSet, assetDeliveryState, assetToken, assetType, fileName, fileSize, imageAsset, sourceFileChecksum, uploadOperations, uploaded] |
| **limitAppScreenshots** | **Integer**| maximum number of related appScreenshots returned (when they are included) | [optional] |

### Return type

[**AppScreenshotSetResponse**](AppScreenshotSetResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single AppScreenshotSet |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

