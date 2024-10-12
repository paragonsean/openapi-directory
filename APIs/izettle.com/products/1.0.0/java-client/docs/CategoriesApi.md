# CategoriesApi

All URIs are relative to *https://products.izettle.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCategories**](CategoriesApi.md#createCategories) | **POST** /organizations/{organizationUuid}/categories/v2 | Create a new category |
| [**deleteCategory**](CategoriesApi.md#deleteCategory) | **DELETE** /organizations/{organizationUuid}/categories/v2/{categoryUuid} | Delete a category |
| [**getProductTypes**](CategoriesApi.md#getProductTypes) | **GET** /organizations/{organizationUuid}/categories/v2 | Retrieve all categories |
| [**renameCategory**](CategoriesApi.md#renameCategory) | **PATCH** /organizations/{organizationUuid}/categories/v2/{categoryUuid} | Rename a category |


<a id="createCategories"></a>
# **createCategories**
> createCategories(organizationUuid, createCategoriesRequest)

Create a new category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    CreateCategoriesRequest createCategoriesRequest = new CreateCategoriesRequest(); // CreateCategoriesRequest | 
    try {
      apiInstance.createCategories(organizationUuid, createCategoriesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#createCategories");
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
| **organizationUuid** | **UUID**|  | |
| **createCategoriesRequest** | [**CreateCategoriesRequest**](CreateCategoriesRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Category created |  -  |
| **400** | Category already exists |  -  |
| **404** | Organization not found |  -  |

<a id="deleteCategory"></a>
# **deleteCategory**
> deleteCategory(organizationUuid, categoryUuid)

Delete a category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    UUID categoryUuid = UUID.randomUUID(); // UUID | 
    try {
      apiInstance.deleteCategory(organizationUuid, categoryUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#deleteCategory");
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
| **organizationUuid** | **UUID**|  | |
| **categoryUuid** | **UUID**|  | |

### Return type

null (empty response body)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Category deleted |  -  |
| **404** | Organization not found |  -  |

<a id="getProductTypes"></a>
# **getProductTypes**
> CategoryResponse getProductTypes(organizationUuid)

Retrieve all categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    try {
      CategoryResponse result = apiInstance.getProductTypes(organizationUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#getProductTypes");
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
| **organizationUuid** | **UUID**|  | |

### Return type

[**CategoryResponse**](CategoryResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of all categories |  -  |

<a id="renameCategory"></a>
# **renameCategory**
> renameCategory(organizationUuid, categoryUuid, renameCategoryRequest)

Rename a category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    UUID categoryUuid = UUID.randomUUID(); // UUID | 
    RenameCategoryRequest renameCategoryRequest = new RenameCategoryRequest(); // RenameCategoryRequest | 
    try {
      apiInstance.renameCategory(organizationUuid, categoryUuid, renameCategoryRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#renameCategory");
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
| **organizationUuid** | **UUID**|  | |
| **categoryUuid** | **UUID**|  | |
| **renameCategoryRequest** | [**RenameCategoryRequest**](RenameCategoryRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Category renamed |  -  |
| **400** | Category already exists |  -  |
| **404** | Organization not found |  -  |

