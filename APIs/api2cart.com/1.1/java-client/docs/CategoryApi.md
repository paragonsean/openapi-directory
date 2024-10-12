# CategoryApi

All URIs are relative to *https://api.api2cart.com/v1.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**categoryAdd**](CategoryApi.md#categoryAdd) | **POST** /category.add.json |  |
| [**categoryAssign**](CategoryApi.md#categoryAssign) | **POST** /category.assign.json |  |
| [**categoryCount**](CategoryApi.md#categoryCount) | **GET** /category.count.json |  |
| [**categoryDelete**](CategoryApi.md#categoryDelete) | **DELETE** /category.delete.json |  |
| [**categoryFind**](CategoryApi.md#categoryFind) | **GET** /category.find.json |  |
| [**categoryImageAdd**](CategoryApi.md#categoryImageAdd) | **POST** /category.image.add.json |  |
| [**categoryImageDelete**](CategoryApi.md#categoryImageDelete) | **DELETE** /category.image.delete.json |  |
| [**categoryInfo**](CategoryApi.md#categoryInfo) | **GET** /category.info.json |  |
| [**categoryList**](CategoryApi.md#categoryList) | **GET** /category.list.json |  |
| [**categoryUnassign**](CategoryApi.md#categoryUnassign) | **POST** /category.unassign.json |  |
| [**categoryUpdate**](CategoryApi.md#categoryUpdate) | **PUT** /category.update.json |  |


<a id="categoryAdd"></a>
# **categoryAdd**
> CategoryAdd200Response categoryAdd(name, parentId, storesIds, storeId, langId, avail, sortOrder, createdTime, modifiedTime, description, metaTitle, metaDescription, metaKeywords, seoUrl)



Add new category in store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String name = "name_example"; // String | Defines category's name that has to be added
    String parentId = "parentId_example"; // String | Adds categories specified by parent id
    String storesIds = "0"; // String | Create category in the stores that is specified by comma-separated stores' id
    String storeId = "storeId_example"; // String | Store Id
    String langId = "langId_example"; // String | Language id
    Boolean avail = true; // Boolean | Defines category's visibility status
    Integer sortOrder = 0; // Integer | Sort number in the list
    String createdTime = "createdTime_example"; // String | Entity's date creation
    String modifiedTime = "modifiedTime_example"; // String | Entity's date modification
    String description = "description_example"; // String | Defines category's description
    String metaTitle = "metaTitle_example"; // String | Defines unique meta title for each entity
    String metaDescription = "metaDescription_example"; // String | Defines unique meta description of a entity
    String metaKeywords = "metaKeywords_example"; // String | Defines unique meta keywords for each entity
    String seoUrl = "seoUrl_example"; // String | Defines unique category's URL for SEO
    try {
      CategoryAdd200Response result = apiInstance.categoryAdd(name, parentId, storesIds, storeId, langId, avail, sortOrder, createdTime, modifiedTime, description, metaTitle, metaDescription, metaKeywords, seoUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#categoryAdd");
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
| **name** | **String**| Defines category&#39;s name that has to be added | |
| **parentId** | **String**| Adds categories specified by parent id | [optional] |
| **storesIds** | **String**| Create category in the stores that is specified by comma-separated stores&#39; id | [optional] [default to 0] |
| **storeId** | **String**| Store Id | [optional] |
| **langId** | **String**| Language id | [optional] |
| **avail** | **Boolean**| Defines category&#39;s visibility status | [optional] [default to true] |
| **sortOrder** | **Integer**| Sort number in the list | [optional] [default to 0] |
| **createdTime** | **String**| Entity&#39;s date creation | [optional] |
| **modifiedTime** | **String**| Entity&#39;s date modification | [optional] |
| **description** | **String**| Defines category&#39;s description | [optional] |
| **metaTitle** | **String**| Defines unique meta title for each entity | [optional] |
| **metaDescription** | **String**| Defines unique meta description of a entity | [optional] |
| **metaKeywords** | **String**| Defines unique meta keywords for each entity | [optional] |
| **seoUrl** | **String**| Defines unique category&#39;s URL for SEO | [optional] |

### Return type

[**CategoryAdd200Response**](CategoryAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="categoryAssign"></a>
# **categoryAssign**
> CartConfigUpdate200Response categoryAssign(productId, categoryId, storeId)



Assign category to product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String productId = "productId_example"; // String | Defines category assign to the product, specified by product id
    String categoryId = "categoryId_example"; // String | Defines category assign, specified by category id
    String storeId = "storeId_example"; // String | Store Id
    try {
      CartConfigUpdate200Response result = apiInstance.categoryAssign(productId, categoryId, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#categoryAssign");
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
| **productId** | **String**| Defines category assign to the product, specified by product id | |
| **categoryId** | **String**| Defines category assign, specified by category id | |
| **storeId** | **String**| Store Id | [optional] |

### Return type

[**CartConfigUpdate200Response**](CartConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="categoryCount"></a>
# **categoryCount**
> CategoryCount200Response categoryCount(parentId, storeId, langId, createdFrom, createdTo, modifiedFrom, modifiedTo, avail)



Count categories in store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String parentId = "parentId_example"; // String | Counts categories specified by parent id
    String storeId = "storeId_example"; // String | Counts category specified by store id
    String langId = "langId_example"; // String | Counts category specified by language id
    String createdFrom = "createdFrom_example"; // String | Retrieve entities from their creation date
    String createdTo = "createdTo_example"; // String | Retrieve entities to their creation date
    String modifiedFrom = "modifiedFrom_example"; // String | Retrieve entities from their modification date
    String modifiedTo = "modifiedTo_example"; // String | Retrieve entities to their modification date
    Boolean avail = true; // Boolean | Defines category's visibility status
    try {
      CategoryCount200Response result = apiInstance.categoryCount(parentId, storeId, langId, createdFrom, createdTo, modifiedFrom, modifiedTo, avail);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#categoryCount");
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
| **parentId** | **String**| Counts categories specified by parent id | [optional] |
| **storeId** | **String**| Counts category specified by store id | [optional] |
| **langId** | **String**| Counts category specified by language id | [optional] |
| **createdFrom** | **String**| Retrieve entities from their creation date | [optional] |
| **createdTo** | **String**| Retrieve entities to their creation date | [optional] |
| **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] |
| **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] |
| **avail** | **Boolean**| Defines category&#39;s visibility status | [optional] [default to true] |

### Return type

[**CategoryCount200Response**](CategoryCount200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="categoryDelete"></a>
# **categoryDelete**
> BridgeDelete200Response categoryDelete(id)



Delete category in store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String id = "id_example"; // String | Defines category removal, specified by category id
    try {
      BridgeDelete200Response result = apiInstance.categoryDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#categoryDelete");
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
| **id** | **String**| Defines category removal, specified by category id | |

### Return type

[**BridgeDelete200Response**](BridgeDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="categoryFind"></a>
# **categoryFind**
> CategoryFind200Response categoryFind(findValue, findWhere, findParams, storeId, langId)



Search category in store. \&quot;Laptop\&quot; is specified here by default.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String findValue = "findValue_example"; // String | Entity search that is specified by some value
    String findWhere = "name"; // String | Entity search that is specified by the comma-separated unique fields
    String findParams = "whole_words"; // String | Entity search that is specified by comma-separated parameters
    String storeId = "storeId_example"; // String | Store Id
    String langId = "langId_example"; // String | Language id
    try {
      CategoryFind200Response result = apiInstance.categoryFind(findValue, findWhere, findParams, storeId, langId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#categoryFind");
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
| **findValue** | **String**| Entity search that is specified by some value | |
| **findWhere** | **String**| Entity search that is specified by the comma-separated unique fields | [optional] [default to name] |
| **findParams** | **String**| Entity search that is specified by comma-separated parameters | [optional] [default to whole_words] |
| **storeId** | **String**| Store Id | [optional] |
| **langId** | **String**| Language id | [optional] |

### Return type

[**CategoryFind200Response**](CategoryFind200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="categoryImageAdd"></a>
# **categoryImageAdd**
> CategoryImageAdd200Response categoryImageAdd(categoryId, imageName, url, type, label, mime, position, storeId)



Add image to category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String categoryId = "categoryId_example"; // String | Defines category id where the image should be added
    String imageName = "imageName_example"; // String | Defines image's name
    String url = "url_example"; // String | Defines URL of the image that has to be added
    String type = "base"; // String | Defines image's types that are specified by comma-separated list
    String label = "label_example"; // String | Defines alternative text that has to be attached to the picture
    String mime = "mime_example"; // String | Mime type of image http://en.wikipedia.org/wiki/Internet_media_type.
    Integer position = 0; // Integer | Defines image’s position in the list
    String storeId = "storeId_example"; // String | Store Id
    try {
      CategoryImageAdd200Response result = apiInstance.categoryImageAdd(categoryId, imageName, url, type, label, mime, position, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#categoryImageAdd");
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
| **categoryId** | **String**| Defines category id where the image should be added | |
| **imageName** | **String**| Defines image&#39;s name | |
| **url** | **String**| Defines URL of the image that has to be added | |
| **type** | **String**| Defines image&#39;s types that are specified by comma-separated list | [enum: base, thumbnail] |
| **label** | **String**| Defines alternative text that has to be attached to the picture | [optional] |
| **mime** | **String**| Mime type of image http://en.wikipedia.org/wiki/Internet_media_type. | [optional] |
| **position** | **Integer**| Defines image’s position in the list | [optional] [default to 0] |
| **storeId** | **String**| Store Id | [optional] |

### Return type

[**CategoryImageAdd200Response**](CategoryImageAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="categoryImageDelete"></a>
# **categoryImageDelete**
> AttributeDelete200Response categoryImageDelete(categoryId, imageId, storeId)



Delete image

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String categoryId = "categoryId_example"; // String | Defines category id where the image should be deleted
    String imageId = "imageId_example"; // String | Define image id
    String storeId = "storeId_example"; // String | Store Id
    try {
      AttributeDelete200Response result = apiInstance.categoryImageDelete(categoryId, imageId, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#categoryImageDelete");
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
| **categoryId** | **String**| Defines category id where the image should be deleted | |
| **imageId** | **String**| Define image id | |
| **storeId** | **String**| Store Id | [optional] |

### Return type

[**AttributeDelete200Response**](AttributeDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="categoryInfo"></a>
# **categoryInfo**
> CategoryInfo200Response categoryInfo(id, params, responseFields, exclude, storeId, langId)



Get category info about category ID*** or specify other category ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String id = "id_example"; // String | Retrieves category's info specified by category id
    String params = "id,parent_id,name,description"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String storeId = "storeId_example"; // String | Retrieves category info  specified by store id
    String langId = "langId_example"; // String | Retrieves category info  specified by language id
    try {
      CategoryInfo200Response result = apiInstance.categoryInfo(id, params, responseFields, exclude, storeId, langId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#categoryInfo");
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
| **id** | **String**| Retrieves category&#39;s info specified by category id | |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,parent_id,name,description] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **storeId** | **String**| Retrieves category info  specified by store id | [optional] |
| **langId** | **String**| Retrieves category info  specified by language id | [optional] |

### Return type

[**CategoryInfo200Response**](CategoryInfo200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="categoryList"></a>
# **categoryList**
> ModelResponseCategoryList categoryList(start, count, pageCursor, parentId, params, responseFields, exclude, storeId, langId, createdFrom, createdTo, modifiedFrom, modifiedTo, avail)



Get list of categories from store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String pageCursor = "pageCursor_example"; // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
    String parentId = "parentId_example"; // String | Retrieves categories specified by parent id
    String params = "id,parent_id,name,description"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String storeId = "storeId_example"; // String | Retrieves categories specified by store id
    String langId = "langId_example"; // String | Retrieves categorys specified by language id
    String createdFrom = "createdFrom_example"; // String | Retrieve entities from their creation date
    String createdTo = "createdTo_example"; // String | Retrieve entities to their creation date
    String modifiedFrom = "modifiedFrom_example"; // String | Retrieve entities from their modification date
    String modifiedTo = "modifiedTo_example"; // String | Retrieve entities to their modification date
    Boolean avail = true; // Boolean | Defines category's visibility status
    try {
      ModelResponseCategoryList result = apiInstance.categoryList(start, count, pageCursor, parentId, params, responseFields, exclude, storeId, langId, createdFrom, createdTo, modifiedFrom, modifiedTo, avail);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#categoryList");
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
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] |
| **parentId** | **String**| Retrieves categories specified by parent id | [optional] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,parent_id,name,description] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **storeId** | **String**| Retrieves categories specified by store id | [optional] |
| **langId** | **String**| Retrieves categorys specified by language id | [optional] |
| **createdFrom** | **String**| Retrieve entities from their creation date | [optional] |
| **createdTo** | **String**| Retrieve entities to their creation date | [optional] |
| **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] |
| **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] |
| **avail** | **Boolean**| Defines category&#39;s visibility status | [optional] [default to true] |

### Return type

[**ModelResponseCategoryList**](ModelResponseCategoryList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="categoryUnassign"></a>
# **categoryUnassign**
> CartConfigUpdate200Response categoryUnassign(categoryId, productId, storeId)



Unassign category to product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String categoryId = "categoryId_example"; // String | Defines category unassign, specified by category id
    String productId = "productId_example"; // String | Defines category unassign to the product, specified by product id
    String storeId = "storeId_example"; // String | Store Id
    try {
      CartConfigUpdate200Response result = apiInstance.categoryUnassign(categoryId, productId, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#categoryUnassign");
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
| **categoryId** | **String**| Defines category unassign, specified by category id | |
| **productId** | **String**| Defines category unassign to the product, specified by product id | |
| **storeId** | **String**| Store Id | [optional] |

### Return type

[**CartConfigUpdate200Response**](CartConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="categoryUpdate"></a>
# **categoryUpdate**
> AccountConfigUpdate200Response categoryUpdate(id, name, parentId, storesIds, avail, sortOrder, modifiedTime, description, metaTitle, metaDescription, metaKeywords, seoUrl, langId, storeId)



Update category in store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String id = "id_example"; // String | Defines category update specified by category id
    String name = "name_example"; // String | Defines new category’s name
    String parentId = "parentId_example"; // String | Defines new parent category id
    String storesIds = "0"; // String | Update category in the stores that is specified by comma-separated stores' id
    Boolean avail = true; // Boolean | Defines category's visibility status
    Integer sortOrder = 56; // Integer | Sort number in the list
    String modifiedTime = "modifiedTime_example"; // String | Entity's date modification
    String description = "description_example"; // String | Defines new category's description
    String metaTitle = "metaTitle_example"; // String | Defines unique meta title for each entity
    String metaDescription = "metaDescription_example"; // String | Defines unique meta description of a entity
    String metaKeywords = "metaKeywords_example"; // String | Defines unique meta keywords for each entity
    String seoUrl = "seoUrl_example"; // String | Defines unique category's URL for SEO
    String langId = "langId_example"; // String | Language id
    String storeId = "storeId_example"; // String | Store Id
    try {
      AccountConfigUpdate200Response result = apiInstance.categoryUpdate(id, name, parentId, storesIds, avail, sortOrder, modifiedTime, description, metaTitle, metaDescription, metaKeywords, seoUrl, langId, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#categoryUpdate");
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
| **id** | **String**| Defines category update specified by category id | |
| **name** | **String**| Defines new category’s name | [optional] |
| **parentId** | **String**| Defines new parent category id | [optional] |
| **storesIds** | **String**| Update category in the stores that is specified by comma-separated stores&#39; id | [optional] [default to 0] |
| **avail** | **Boolean**| Defines category&#39;s visibility status | [optional] |
| **sortOrder** | **Integer**| Sort number in the list | [optional] |
| **modifiedTime** | **String**| Entity&#39;s date modification | [optional] |
| **description** | **String**| Defines new category&#39;s description | [optional] |
| **metaTitle** | **String**| Defines unique meta title for each entity | [optional] |
| **metaDescription** | **String**| Defines unique meta description of a entity | [optional] |
| **metaKeywords** | **String**| Defines unique meta keywords for each entity | [optional] |
| **seoUrl** | **String**| Defines unique category&#39;s URL for SEO | [optional] |
| **langId** | **String**| Language id | [optional] |
| **storeId** | **String**| Store Id | [optional] |

### Return type

[**AccountConfigUpdate200Response**](AccountConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

