# AppStoreVersionLocalizationsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appStoreVersionLocalizationsAppPreviewSetsGetToManyRelated**](AppStoreVersionLocalizationsApi.md#appStoreVersionLocalizationsAppPreviewSetsGetToManyRelated) | **GET** /v1/appStoreVersionLocalizations/{id}/appPreviewSets |  |
| [**appStoreVersionLocalizationsAppScreenshotSetsGetToManyRelated**](AppStoreVersionLocalizationsApi.md#appStoreVersionLocalizationsAppScreenshotSetsGetToManyRelated) | **GET** /v1/appStoreVersionLocalizations/{id}/appScreenshotSets |  |
| [**appStoreVersionLocalizationsCreateInstance**](AppStoreVersionLocalizationsApi.md#appStoreVersionLocalizationsCreateInstance) | **POST** /v1/appStoreVersionLocalizations |  |
| [**appStoreVersionLocalizationsDeleteInstance**](AppStoreVersionLocalizationsApi.md#appStoreVersionLocalizationsDeleteInstance) | **DELETE** /v1/appStoreVersionLocalizations/{id} |  |
| [**appStoreVersionLocalizationsGetInstance**](AppStoreVersionLocalizationsApi.md#appStoreVersionLocalizationsGetInstance) | **GET** /v1/appStoreVersionLocalizations/{id} |  |
| [**appStoreVersionLocalizationsUpdateInstance**](AppStoreVersionLocalizationsApi.md#appStoreVersionLocalizationsUpdateInstance) | **PATCH** /v1/appStoreVersionLocalizations/{id} |  |


<a id="appStoreVersionLocalizationsAppPreviewSetsGetToManyRelated"></a>
# **appStoreVersionLocalizationsAppPreviewSetsGetToManyRelated**
> AppPreviewSetsResponse appStoreVersionLocalizationsAppPreviewSetsGetToManyRelated(id, filterPreviewType, fieldsAppStoreVersionLocalizations, fieldsAppPreviews, fieldsAppPreviewSets, limit, include)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionLocalizationsApi apiInstance = new AppStoreVersionLocalizationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> filterPreviewType = Arrays.asList(); // List<String> | filter by attribute 'previewType'
    List<String> fieldsAppStoreVersionLocalizations = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreVersionLocalizations
    List<String> fieldsAppPreviews = Arrays.asList(); // List<String> | the fields to include for returned resources of type appPreviews
    List<String> fieldsAppPreviewSets = Arrays.asList(); // List<String> | the fields to include for returned resources of type appPreviewSets
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    try {
      AppPreviewSetsResponse result = apiInstance.appStoreVersionLocalizationsAppPreviewSetsGetToManyRelated(id, filterPreviewType, fieldsAppStoreVersionLocalizations, fieldsAppPreviews, fieldsAppPreviewSets, limit, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionLocalizationsApi#appStoreVersionLocalizationsAppPreviewSetsGetToManyRelated");
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
| **filterPreviewType** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;previewType&#39; | [optional] [enum: IPHONE_65, IPHONE_58, IPHONE_55, IPHONE_47, IPHONE_40, IPHONE_35, IPAD_PRO_3GEN_129, IPAD_PRO_3GEN_11, IPAD_PRO_129, IPAD_105, IPAD_97, DESKTOP, WATCH_SERIES_4, WATCH_SERIES_3, APPLE_TV] |
| **fieldsAppStoreVersionLocalizations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreVersionLocalizations | [optional] [enum: appPreviewSets, appScreenshotSets, appStoreVersion, description, keywords, locale, marketingUrl, promotionalText, supportUrl, whatsNew] |
| **fieldsAppPreviews** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appPreviews | [optional] [enum: appPreviewSet, assetDeliveryState, fileName, fileSize, mimeType, previewFrameTimeCode, previewImage, sourceFileChecksum, uploadOperations, uploaded, videoUrl] |
| **fieldsAppPreviewSets** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appPreviewSets | [optional] [enum: appPreviews, appStoreVersionLocalization, previewType] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: appPreviews, appStoreVersionLocalization] |

### Return type

[**AppPreviewSetsResponse**](AppPreviewSetsResponse.md)

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

<a id="appStoreVersionLocalizationsAppScreenshotSetsGetToManyRelated"></a>
# **appStoreVersionLocalizationsAppScreenshotSetsGetToManyRelated**
> AppScreenshotSetsResponse appStoreVersionLocalizationsAppScreenshotSetsGetToManyRelated(id, filterScreenshotDisplayType, fieldsAppStoreVersionLocalizations, fieldsAppScreenshotSets, fieldsAppScreenshots, limit, include)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionLocalizationsApi apiInstance = new AppStoreVersionLocalizationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> filterScreenshotDisplayType = Arrays.asList(); // List<String> | filter by attribute 'screenshotDisplayType'
    List<String> fieldsAppStoreVersionLocalizations = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreVersionLocalizations
    List<String> fieldsAppScreenshotSets = Arrays.asList(); // List<String> | the fields to include for returned resources of type appScreenshotSets
    List<String> fieldsAppScreenshots = Arrays.asList(); // List<String> | the fields to include for returned resources of type appScreenshots
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    try {
      AppScreenshotSetsResponse result = apiInstance.appStoreVersionLocalizationsAppScreenshotSetsGetToManyRelated(id, filterScreenshotDisplayType, fieldsAppStoreVersionLocalizations, fieldsAppScreenshotSets, fieldsAppScreenshots, limit, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionLocalizationsApi#appStoreVersionLocalizationsAppScreenshotSetsGetToManyRelated");
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
| **filterScreenshotDisplayType** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;screenshotDisplayType&#39; | [optional] [enum: APP_IPHONE_65, APP_IPHONE_58, APP_IPHONE_55, APP_IPHONE_47, APP_IPHONE_40, APP_IPHONE_35, APP_IPAD_PRO_3GEN_129, APP_IPAD_PRO_3GEN_11, APP_IPAD_PRO_129, APP_IPAD_105, APP_IPAD_97, APP_DESKTOP, APP_WATCH_SERIES_4, APP_WATCH_SERIES_3, APP_APPLE_TV, IMESSAGE_APP_IPHONE_65, IMESSAGE_APP_IPHONE_58, IMESSAGE_APP_IPHONE_55, IMESSAGE_APP_IPHONE_47, IMESSAGE_APP_IPHONE_40, IMESSAGE_APP_IPAD_PRO_3GEN_129, IMESSAGE_APP_IPAD_PRO_3GEN_11, IMESSAGE_APP_IPAD_PRO_129, IMESSAGE_APP_IPAD_105, IMESSAGE_APP_IPAD_97] |
| **fieldsAppStoreVersionLocalizations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreVersionLocalizations | [optional] [enum: appPreviewSets, appScreenshotSets, appStoreVersion, description, keywords, locale, marketingUrl, promotionalText, supportUrl, whatsNew] |
| **fieldsAppScreenshotSets** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appScreenshotSets | [optional] [enum: appScreenshots, appStoreVersionLocalization, screenshotDisplayType] |
| **fieldsAppScreenshots** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appScreenshots | [optional] [enum: appScreenshotSet, assetDeliveryState, assetToken, assetType, fileName, fileSize, imageAsset, sourceFileChecksum, uploadOperations, uploaded] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: appScreenshots, appStoreVersionLocalization] |

### Return type

[**AppScreenshotSetsResponse**](AppScreenshotSetsResponse.md)

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

<a id="appStoreVersionLocalizationsCreateInstance"></a>
# **appStoreVersionLocalizationsCreateInstance**
> AppStoreVersionLocalizationResponse appStoreVersionLocalizationsCreateInstance(appStoreVersionLocalizationCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionLocalizationsApi apiInstance = new AppStoreVersionLocalizationsApi(defaultClient);
    AppStoreVersionLocalizationCreateRequest appStoreVersionLocalizationCreateRequest = new AppStoreVersionLocalizationCreateRequest(); // AppStoreVersionLocalizationCreateRequest | AppStoreVersionLocalization representation
    try {
      AppStoreVersionLocalizationResponse result = apiInstance.appStoreVersionLocalizationsCreateInstance(appStoreVersionLocalizationCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionLocalizationsApi#appStoreVersionLocalizationsCreateInstance");
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
| **appStoreVersionLocalizationCreateRequest** | [**AppStoreVersionLocalizationCreateRequest**](AppStoreVersionLocalizationCreateRequest.md)| AppStoreVersionLocalization representation | |

### Return type

[**AppStoreVersionLocalizationResponse**](AppStoreVersionLocalizationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single AppStoreVersionLocalization |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="appStoreVersionLocalizationsDeleteInstance"></a>
# **appStoreVersionLocalizationsDeleteInstance**
> appStoreVersionLocalizationsDeleteInstance(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionLocalizationsApi apiInstance = new AppStoreVersionLocalizationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    try {
      apiInstance.appStoreVersionLocalizationsDeleteInstance(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionLocalizationsApi#appStoreVersionLocalizationsDeleteInstance");
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

<a id="appStoreVersionLocalizationsGetInstance"></a>
# **appStoreVersionLocalizationsGetInstance**
> AppStoreVersionLocalizationResponse appStoreVersionLocalizationsGetInstance(id, fieldsAppStoreVersionLocalizations, include, fieldsAppScreenshotSets, fieldsAppPreviewSets, limitAppPreviewSets, limitAppScreenshotSets)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionLocalizationsApi apiInstance = new AppStoreVersionLocalizationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppStoreVersionLocalizations = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreVersionLocalizations
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsAppScreenshotSets = Arrays.asList(); // List<String> | the fields to include for returned resources of type appScreenshotSets
    List<String> fieldsAppPreviewSets = Arrays.asList(); // List<String> | the fields to include for returned resources of type appPreviewSets
    Integer limitAppPreviewSets = 56; // Integer | maximum number of related appPreviewSets returned (when they are included)
    Integer limitAppScreenshotSets = 56; // Integer | maximum number of related appScreenshotSets returned (when they are included)
    try {
      AppStoreVersionLocalizationResponse result = apiInstance.appStoreVersionLocalizationsGetInstance(id, fieldsAppStoreVersionLocalizations, include, fieldsAppScreenshotSets, fieldsAppPreviewSets, limitAppPreviewSets, limitAppScreenshotSets);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionLocalizationsApi#appStoreVersionLocalizationsGetInstance");
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
| **fieldsAppStoreVersionLocalizations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreVersionLocalizations | [optional] [enum: appPreviewSets, appScreenshotSets, appStoreVersion, description, keywords, locale, marketingUrl, promotionalText, supportUrl, whatsNew] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: appPreviewSets, appScreenshotSets, appStoreVersion] |
| **fieldsAppScreenshotSets** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appScreenshotSets | [optional] [enum: appScreenshots, appStoreVersionLocalization, screenshotDisplayType] |
| **fieldsAppPreviewSets** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appPreviewSets | [optional] [enum: appPreviews, appStoreVersionLocalization, previewType] |
| **limitAppPreviewSets** | **Integer**| maximum number of related appPreviewSets returned (when they are included) | [optional] |
| **limitAppScreenshotSets** | **Integer**| maximum number of related appScreenshotSets returned (when they are included) | [optional] |

### Return type

[**AppStoreVersionLocalizationResponse**](AppStoreVersionLocalizationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single AppStoreVersionLocalization |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appStoreVersionLocalizationsUpdateInstance"></a>
# **appStoreVersionLocalizationsUpdateInstance**
> AppStoreVersionLocalizationResponse appStoreVersionLocalizationsUpdateInstance(id, appStoreVersionLocalizationUpdateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionLocalizationsApi apiInstance = new AppStoreVersionLocalizationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    AppStoreVersionLocalizationUpdateRequest appStoreVersionLocalizationUpdateRequest = new AppStoreVersionLocalizationUpdateRequest(); // AppStoreVersionLocalizationUpdateRequest | AppStoreVersionLocalization representation
    try {
      AppStoreVersionLocalizationResponse result = apiInstance.appStoreVersionLocalizationsUpdateInstance(id, appStoreVersionLocalizationUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionLocalizationsApi#appStoreVersionLocalizationsUpdateInstance");
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
| **appStoreVersionLocalizationUpdateRequest** | [**AppStoreVersionLocalizationUpdateRequest**](AppStoreVersionLocalizationUpdateRequest.md)| AppStoreVersionLocalization representation | |

### Return type

[**AppStoreVersionLocalizationResponse**](AppStoreVersionLocalizationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single AppStoreVersionLocalization |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

