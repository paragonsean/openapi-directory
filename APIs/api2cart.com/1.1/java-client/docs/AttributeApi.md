# AttributeApi

All URIs are relative to *https://api.api2cart.com/v1.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**attributeAdd**](AttributeApi.md#attributeAdd) | **POST** /attribute.add.json |  |
| [**attributeAssignGroup**](AttributeApi.md#attributeAssignGroup) | **POST** /attribute.assign.group.json |  |
| [**attributeAssignSet**](AttributeApi.md#attributeAssignSet) | **POST** /attribute.assign.set.json |  |
| [**attributeAttributesetList**](AttributeApi.md#attributeAttributesetList) | **GET** /attribute.attributeset.list.json |  |
| [**attributeCount**](AttributeApi.md#attributeCount) | **GET** /attribute.count.json |  |
| [**attributeDelete**](AttributeApi.md#attributeDelete) | **DELETE** /attribute.delete.json |  |
| [**attributeGroupList**](AttributeApi.md#attributeGroupList) | **GET** /attribute.group.list.json |  |
| [**attributeInfo**](AttributeApi.md#attributeInfo) | **GET** /attribute.info.json |  |
| [**attributeList**](AttributeApi.md#attributeList) | **GET** /attribute.list.json |  |
| [**attributeTypeList**](AttributeApi.md#attributeTypeList) | **GET** /attribute.type.list.json |  |
| [**attributeUnassignGroup**](AttributeApi.md#attributeUnassignGroup) | **POST** /attribute.unassign.group.json |  |
| [**attributeUnassignSet**](AttributeApi.md#attributeUnassignSet) | **POST** /attribute.unassign.set.json |  |
| [**attributeUpdate**](AttributeApi.md#attributeUpdate) | **POST** /attribute.update.json |  |


<a id="attributeAdd"></a>
# **attributeAdd**
> AttributeAdd200Response attributeAdd(type, name, code, storeId, langId, visible, required, position, attributeGroupId, isGlobal, isSearchable, isFilterable, isComparable, isHtmlAllowedOnFront, isFilterableInSearch, isConfigurable, isVisibleInAdvancedSearch, isUsedForPromoRules, usedInProductListing, usedForSortBy, applyTo)



Add new attribute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

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

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String type = "text"; // String | Defines attribute's type
    String name = "name_example"; // String | Defines attributes's name
    String code = "code_example"; // String | Entity code
    String storeId = "storeId_example"; // String | Store Id
    String langId = "langId_example"; // String | Language id
    Boolean visible = false; // Boolean | Set visibility status
    Boolean required = false; // Boolean | Defines if the option is required
    Integer position = 0; // Integer | Attribute`s position
    String attributeGroupId = "attributeGroupId_example"; // String | Filter by attribute_group_id
    String isGlobal = "Store"; // String | Attribute saving scope
    Boolean isSearchable = false; // Boolean | Use attribute in Quick Search
    String isFilterable = "false"; // String | Use In Layered Navigation
    Boolean isComparable = false; // Boolean | Comparable on Front-end
    Boolean isHtmlAllowedOnFront = false; // Boolean | Allow HTML Tags on Frontend
    Boolean isFilterableInSearch = false; // Boolean | Use In Search Results Layered Navigation
    Boolean isConfigurable = false; // Boolean | Use To Create Configurable Product
    Boolean isVisibleInAdvancedSearch = false; // Boolean | Use in Advanced Search
    Boolean isUsedForPromoRules = false; // Boolean | Use for Promo Rule Conditions
    Boolean usedInProductListing = false; // Boolean | Used in Product Listing
    Boolean usedForSortBy = false; // Boolean | Used for Sorting in Product Listing
    String applyTo = "all_types"; // String | Types of products which can have this attribute
    try {
      AttributeAdd200Response result = apiInstance.attributeAdd(type, name, code, storeId, langId, visible, required, position, attributeGroupId, isGlobal, isSearchable, isFilterable, isComparable, isHtmlAllowedOnFront, isFilterableInSearch, isConfigurable, isVisibleInAdvancedSearch, isUsedForPromoRules, usedInProductListing, usedForSortBy, applyTo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeAdd");
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
| **type** | **String**| Defines attribute&#39;s type | [enum: text, select, textarea, date, price, multiselect, boolean] |
| **name** | **String**| Defines attributes&#39;s name | |
| **code** | **String**| Entity code | [optional] |
| **storeId** | **String**| Store Id | [optional] |
| **langId** | **String**| Language id | [optional] |
| **visible** | **Boolean**| Set visibility status | [optional] [default to false] |
| **required** | **Boolean**| Defines if the option is required | [optional] [default to false] |
| **position** | **Integer**| Attribute&#x60;s position | [optional] [default to 0] |
| **attributeGroupId** | **String**| Filter by attribute_group_id | [optional] |
| **isGlobal** | **String**| Attribute saving scope | [optional] [default to Store] |
| **isSearchable** | **Boolean**| Use attribute in Quick Search | [optional] [default to false] |
| **isFilterable** | **String**| Use In Layered Navigation | [optional] [default to false] |
| **isComparable** | **Boolean**| Comparable on Front-end | [optional] [default to false] |
| **isHtmlAllowedOnFront** | **Boolean**| Allow HTML Tags on Frontend | [optional] [default to false] |
| **isFilterableInSearch** | **Boolean**| Use In Search Results Layered Navigation | [optional] [default to false] |
| **isConfigurable** | **Boolean**| Use To Create Configurable Product | [optional] [default to false] |
| **isVisibleInAdvancedSearch** | **Boolean**| Use in Advanced Search | [optional] [default to false] |
| **isUsedForPromoRules** | **Boolean**| Use for Promo Rule Conditions | [optional] [default to false] |
| **usedInProductListing** | **Boolean**| Used in Product Listing | [optional] [default to false] |
| **usedForSortBy** | **Boolean**| Used for Sorting in Product Listing | [optional] [default to false] |
| **applyTo** | **String**| Types of products which can have this attribute | [optional] [default to all_types] |

### Return type

[**AttributeAdd200Response**](AttributeAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="attributeAssignGroup"></a>
# **attributeAssignGroup**
> AttributeAssignGroup200Response attributeAssignGroup(id, groupId, attributeSetId)



Assign attribute to the group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

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

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String id = "id_example"; // String | Entity id
    String groupId = "groupId_example"; // String | Attribute group_id
    String attributeSetId = "attributeSetId_example"; // String | Attribute set id
    try {
      AttributeAssignGroup200Response result = apiInstance.attributeAssignGroup(id, groupId, attributeSetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeAssignGroup");
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
| **id** | **String**| Entity id | |
| **groupId** | **String**| Attribute group_id | |
| **attributeSetId** | **String**| Attribute set id | [optional] |

### Return type

[**AttributeAssignGroup200Response**](AttributeAssignGroup200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="attributeAssignSet"></a>
# **attributeAssignSet**
> AttributeAssignGroup200Response attributeAssignSet(id, attributeSetId, groupId)



Assign attribute to the attribute set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

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

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String id = "id_example"; // String | Entity id
    String attributeSetId = "attributeSetId_example"; // String | Attribute set id
    String groupId = "groupId_example"; // String | Attribute group_id
    try {
      AttributeAssignGroup200Response result = apiInstance.attributeAssignSet(id, attributeSetId, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeAssignSet");
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
| **id** | **String**| Entity id | |
| **attributeSetId** | **String**| Attribute set id | |
| **groupId** | **String**| Attribute group_id | [optional] |

### Return type

[**AttributeAssignGroup200Response**](AttributeAssignGroup200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="attributeAttributesetList"></a>
# **attributeAttributesetList**
> AttributeAttributesetList200Response attributeAttributesetList(start, count, params, exclude, responseFields)



Get attribute_set list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

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

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String params = "id,name"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    try {
      AttributeAttributesetList200Response result = apiInstance.attributeAttributesetList(start, count, params, exclude, responseFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeAttributesetList");
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
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |

### Return type

[**AttributeAttributesetList200Response**](AttributeAttributesetList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="attributeCount"></a>
# **attributeCount**
> AttributeCount200Response attributeCount(type, storeId, langId, visible, required, system)



Get attributes count

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

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

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String type = "type_example"; // String | Defines attribute's type
    String storeId = "storeId_example"; // String | Store Id
    String langId = "langId_example"; // String | Language id
    Boolean visible = true; // Boolean | Filter items by visibility status
    Boolean required = true; // Boolean | Defines if the option is required
    Boolean system = true; // Boolean | True if attribute is system
    try {
      AttributeCount200Response result = apiInstance.attributeCount(type, storeId, langId, visible, required, system);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeCount");
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
| **type** | **String**| Defines attribute&#39;s type | [optional] |
| **storeId** | **String**| Store Id | [optional] |
| **langId** | **String**| Language id | [optional] |
| **visible** | **Boolean**| Filter items by visibility status | [optional] |
| **required** | **Boolean**| Defines if the option is required | [optional] |
| **system** | **Boolean**| True if attribute is system | [optional] |

### Return type

[**AttributeCount200Response**](AttributeCount200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="attributeDelete"></a>
# **attributeDelete**
> AttributeDelete200Response attributeDelete(id, storeId)



Delete attribute from store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

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

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String id = "id_example"; // String | Entity id
    String storeId = "storeId_example"; // String | Store Id
    try {
      AttributeDelete200Response result = apiInstance.attributeDelete(id, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeDelete");
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
| **id** | **String**| Entity id | |
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

<a id="attributeGroupList"></a>
# **attributeGroupList**
> AttributeAttributesetList200Response attributeGroupList(start, count, langId, params, exclude, responseFields, attributeSetId)



Get attribute group list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

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

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String langId = "langId_example"; // String | Language id
    String params = "id,name"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String attributeSetId = "attributeSetId_example"; // String | Attribute set id
    try {
      AttributeAttributesetList200Response result = apiInstance.attributeGroupList(start, count, langId, params, exclude, responseFields, attributeSetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeGroupList");
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
| **langId** | **String**| Language id | [optional] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **attributeSetId** | **String**| Attribute set id | [optional] |

### Return type

[**AttributeAttributesetList200Response**](AttributeAttributesetList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="attributeInfo"></a>
# **attributeInfo**
> AttributeInfo200Response attributeInfo(id, storeId, langId, params, exclude, responseFields)



Get attribute info

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

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

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String id = "id_example"; // String | Entity id
    String storeId = "storeId_example"; // String | Store Id
    String langId = "langId_example"; // String | Language id
    String params = "force_all"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    try {
      AttributeInfo200Response result = apiInstance.attributeInfo(id, storeId, langId, params, exclude, responseFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeInfo");
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
| **id** | **String**| Entity id | |
| **storeId** | **String**| Store Id | [optional] |
| **langId** | **String**| Language id | [optional] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to force_all] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |

### Return type

[**AttributeInfo200Response**](AttributeInfo200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="attributeList"></a>
# **attributeList**
> ModelResponseAttributeList attributeList(start, count, type, attributeIds, storeId, langId, params, exclude, responseFields, visible, required, system)



Get attributes list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

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

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String type = "type_example"; // String | Defines attribute's type
    String attributeIds = "attributeIds_example"; // String | Filter attributes by ids
    String storeId = "storeId_example"; // String | Store Id
    String langId = "langId_example"; // String | Retrieves attributes on specified language id
    String params = "id,name,code,type"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    Boolean visible = true; // Boolean | Filter items by visibility status
    Boolean required = true; // Boolean | Defines if the option is required
    Boolean system = true; // Boolean | True if attribute is system
    try {
      ModelResponseAttributeList result = apiInstance.attributeList(start, count, type, attributeIds, storeId, langId, params, exclude, responseFields, visible, required, system);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeList");
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
| **type** | **String**| Defines attribute&#39;s type | [optional] |
| **attributeIds** | **String**| Filter attributes by ids | [optional] |
| **storeId** | **String**| Store Id | [optional] |
| **langId** | **String**| Retrieves attributes on specified language id | [optional] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name,code,type] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **visible** | **Boolean**| Filter items by visibility status | [optional] |
| **required** | **Boolean**| Defines if the option is required | [optional] |
| **system** | **Boolean**| True if attribute is system | [optional] |

### Return type

[**ModelResponseAttributeList**](ModelResponseAttributeList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="attributeTypeList"></a>
# **attributeTypeList**
> AttributeTypeList200Response attributeTypeList()



Get list of supported attributes types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

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

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    try {
      AttributeTypeList200Response result = apiInstance.attributeTypeList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeTypeList");
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

[**AttributeTypeList200Response**](AttributeTypeList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="attributeUnassignGroup"></a>
# **attributeUnassignGroup**
> AttributeUnassignGroup200Response attributeUnassignGroup(id, groupId)



Unassign attribute from group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

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

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String id = "id_example"; // String | Entity id
    String groupId = "groupId_example"; // String | Customer group_id
    try {
      AttributeUnassignGroup200Response result = apiInstance.attributeUnassignGroup(id, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeUnassignGroup");
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
| **id** | **String**| Entity id | |
| **groupId** | **String**| Customer group_id | |

### Return type

[**AttributeUnassignGroup200Response**](AttributeUnassignGroup200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="attributeUnassignSet"></a>
# **attributeUnassignSet**
> AttributeUnassignGroup200Response attributeUnassignSet(id, attributeSetId)



Unassign attribute from attribute set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

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

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String id = "id_example"; // String | Entity id
    String attributeSetId = "attributeSetId_example"; // String | Attribute set id
    try {
      AttributeUnassignGroup200Response result = apiInstance.attributeUnassignSet(id, attributeSetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeUnassignSet");
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
| **id** | **String**| Entity id | |
| **attributeSetId** | **String**| Attribute set id | |

### Return type

[**AttributeUnassignGroup200Response**](AttributeUnassignGroup200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="attributeUpdate"></a>
# **attributeUpdate**
> AttributeUpdate200Response attributeUpdate(id, name, storeId, langId)



Update attribute data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributeApi;

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

    AttributeApi apiInstance = new AttributeApi(defaultClient);
    String id = "id_example"; // String | Entity id
    String name = "name_example"; // String | Defines new attributes's name
    String storeId = "storeId_example"; // String | Store Id
    String langId = "langId_example"; // String | Language id
    try {
      AttributeUpdate200Response result = apiInstance.attributeUpdate(id, name, storeId, langId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributeApi#attributeUpdate");
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
| **id** | **String**| Entity id | |
| **name** | **String**| Defines new attributes&#39;s name | |
| **storeId** | **String**| Store Id | [optional] |
| **langId** | **String**| Language id | [optional] |

### Return type

[**AttributeUpdate200Response**](AttributeUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

