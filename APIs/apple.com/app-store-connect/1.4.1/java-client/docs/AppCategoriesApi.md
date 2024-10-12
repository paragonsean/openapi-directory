# AppCategoriesApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appCategoriesGetCollection**](AppCategoriesApi.md#appCategoriesGetCollection) | **GET** /v1/appCategories |  |
| [**appCategoriesGetInstance**](AppCategoriesApi.md#appCategoriesGetInstance) | **GET** /v1/appCategories/{id} |  |
| [**appCategoriesParentGetToOneRelated**](AppCategoriesApi.md#appCategoriesParentGetToOneRelated) | **GET** /v1/appCategories/{id}/parent |  |
| [**appCategoriesSubcategoriesGetToManyRelated**](AppCategoriesApi.md#appCategoriesSubcategoriesGetToManyRelated) | **GET** /v1/appCategories/{id}/subcategories |  |


<a id="appCategoriesGetCollection"></a>
# **appCategoriesGetCollection**
> AppCategoriesResponse appCategoriesGetCollection(filterPlatforms, existsParent, fieldsAppCategories, limit, include, limitSubcategories)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppCategoriesApi apiInstance = new AppCategoriesApi(defaultClient);
    List<String> filterPlatforms = Arrays.asList(); // List<String> | filter by attribute 'platforms'
    List<String> existsParent = Arrays.asList(); // List<String> | filter by existence or non-existence of related 'parent'
    List<String> fieldsAppCategories = Arrays.asList(); // List<String> | the fields to include for returned resources of type appCategories
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    Integer limitSubcategories = 56; // Integer | maximum number of related subcategories returned (when they are included)
    try {
      AppCategoriesResponse result = apiInstance.appCategoriesGetCollection(filterPlatforms, existsParent, fieldsAppCategories, limit, include, limitSubcategories);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppCategoriesApi#appCategoriesGetCollection");
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
| **filterPlatforms** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;platforms&#39; | [optional] [enum: IOS, MAC_OS, TV_OS] |
| **existsParent** | [**List&lt;String&gt;**](String.md)| filter by existence or non-existence of related &#39;parent&#39; | [optional] |
| **fieldsAppCategories** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appCategories | [optional] [enum: parent, platforms, subcategories] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: parent, subcategories] |
| **limitSubcategories** | **Integer**| maximum number of related subcategories returned (when they are included) | [optional] |

### Return type

[**AppCategoriesResponse**](AppCategoriesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of AppCategories |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |

<a id="appCategoriesGetInstance"></a>
# **appCategoriesGetInstance**
> AppCategoryResponse appCategoriesGetInstance(id, fieldsAppCategories, include, limitSubcategories)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppCategoriesApi apiInstance = new AppCategoriesApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppCategories = Arrays.asList(); // List<String> | the fields to include for returned resources of type appCategories
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    Integer limitSubcategories = 56; // Integer | maximum number of related subcategories returned (when they are included)
    try {
      AppCategoryResponse result = apiInstance.appCategoriesGetInstance(id, fieldsAppCategories, include, limitSubcategories);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppCategoriesApi#appCategoriesGetInstance");
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
| **fieldsAppCategories** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appCategories | [optional] [enum: parent, platforms, subcategories] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: parent, subcategories] |
| **limitSubcategories** | **Integer**| maximum number of related subcategories returned (when they are included) | [optional] |

### Return type

[**AppCategoryResponse**](AppCategoryResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single AppCategory |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appCategoriesParentGetToOneRelated"></a>
# **appCategoriesParentGetToOneRelated**
> AppCategoryResponse appCategoriesParentGetToOneRelated(id, fieldsAppCategories)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppCategoriesApi apiInstance = new AppCategoriesApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppCategories = Arrays.asList(); // List<String> | the fields to include for returned resources of type appCategories
    try {
      AppCategoryResponse result = apiInstance.appCategoriesParentGetToOneRelated(id, fieldsAppCategories);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppCategoriesApi#appCategoriesParentGetToOneRelated");
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
| **fieldsAppCategories** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appCategories | [optional] [enum: parent, platforms, subcategories] |

### Return type

[**AppCategoryResponse**](AppCategoryResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Related resource |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appCategoriesSubcategoriesGetToManyRelated"></a>
# **appCategoriesSubcategoriesGetToManyRelated**
> AppCategoriesResponse appCategoriesSubcategoriesGetToManyRelated(id, fieldsAppCategories, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppCategoriesApi apiInstance = new AppCategoriesApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppCategories = Arrays.asList(); // List<String> | the fields to include for returned resources of type appCategories
    Integer limit = 56; // Integer | maximum resources per page
    try {
      AppCategoriesResponse result = apiInstance.appCategoriesSubcategoriesGetToManyRelated(id, fieldsAppCategories, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppCategoriesApi#appCategoriesSubcategoriesGetToManyRelated");
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
| **fieldsAppCategories** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appCategories | [optional] [enum: parent, platforms, subcategories] |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**AppCategoriesResponse**](AppCategoriesResponse.md)

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

