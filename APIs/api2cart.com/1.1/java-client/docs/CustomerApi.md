# CustomerApi

All URIs are relative to *https://api.api2cart.com/v1.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerAdd**](CustomerApi.md#customerAdd) | **POST** /customer.add.json |  |
| [**customerAttributeList**](CustomerApi.md#customerAttributeList) | **GET** /customer.attribute.list.json |  |
| [**customerCount**](CustomerApi.md#customerCount) | **GET** /customer.count.json |  |
| [**customerFind**](CustomerApi.md#customerFind) | **GET** /customer.find.json |  |
| [**customerGroupAdd**](CustomerApi.md#customerGroupAdd) | **POST** /customer.group.add.json |  |
| [**customerGroupList**](CustomerApi.md#customerGroupList) | **GET** /customer.group.list.json |  |
| [**customerInfo**](CustomerApi.md#customerInfo) | **GET** /customer.info.json |  |
| [**customerList**](CustomerApi.md#customerList) | **GET** /customer.list.json |  |
| [**customerUpdate**](CustomerApi.md#customerUpdate) | **PUT** /customer.update.json |  |
| [**customerWishlistList**](CustomerApi.md#customerWishlistList) | **GET** /customer.wishlist.list.json |  |


<a id="customerAdd"></a>
# **customerAdd**
> CustomerAdd200Response customerAdd(customerAdd)



Add customer into store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerApi;

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

    CustomerApi apiInstance = new CustomerApi(defaultClient);
    CustomerAdd customerAdd = new CustomerAdd(); // CustomerAdd | 
    try {
      CustomerAdd200Response result = apiInstance.customerAdd(customerAdd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerApi#customerAdd");
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
| **customerAdd** | [**CustomerAdd**](CustomerAdd.md)|  | |

### Return type

[**CustomerAdd200Response**](CustomerAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="customerAttributeList"></a>
# **customerAttributeList**
> ModelResponseCustomerAttributeList customerAttributeList(customerId, count, pageCursor, storeId, langId, params, exclude, responseFields)



Get attributes for specific customer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerApi;

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

    CustomerApi apiInstance = new CustomerApi(defaultClient);
    String customerId = "customerId_example"; // String | Retrieves orders specified by customer id
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String pageCursor = "pageCursor_example"; // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
    String storeId = "storeId_example"; // String | Store Id
    String langId = "langId_example"; // String | Language id
    String params = "force_all"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    try {
      ModelResponseCustomerAttributeList result = apiInstance.customerAttributeList(customerId, count, pageCursor, storeId, langId, params, exclude, responseFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerApi#customerAttributeList");
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
| **customerId** | **String**| Retrieves orders specified by customer id | |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] |
| **storeId** | **String**| Store Id | [optional] |
| **langId** | **String**| Language id | [optional] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to force_all] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |

### Return type

[**ModelResponseCustomerAttributeList**](ModelResponseCustomerAttributeList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="customerCount"></a>
# **customerCount**
> CustomerCount200Response customerCount(groupId, createdFrom, createdTo, modifiedFrom, modifiedTo, storeId, customerListId, avail)



Get number of customers from store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerApi;

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

    CustomerApi apiInstance = new CustomerApi(defaultClient);
    String groupId = "groupId_example"; // String | Customer group_id
    String createdFrom = "createdFrom_example"; // String | Retrieve entities from their creation date
    String createdTo = "createdTo_example"; // String | Retrieve entities to their creation date
    String modifiedFrom = "modifiedFrom_example"; // String | Retrieve entities from their modification date
    String modifiedTo = "modifiedTo_example"; // String | Retrieve entities to their modification date
    String storeId = "storeId_example"; // String | Counts customer specified by store id
    String customerListId = "customerListId_example"; // String | The numeric ID of the customer list in Demandware.
    Boolean avail = true; // Boolean | Defines category's visibility status
    try {
      CustomerCount200Response result = apiInstance.customerCount(groupId, createdFrom, createdTo, modifiedFrom, modifiedTo, storeId, customerListId, avail);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerApi#customerCount");
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
| **groupId** | **String**| Customer group_id | [optional] |
| **createdFrom** | **String**| Retrieve entities from their creation date | [optional] |
| **createdTo** | **String**| Retrieve entities to their creation date | [optional] |
| **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] |
| **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] |
| **storeId** | **String**| Counts customer specified by store id | [optional] |
| **customerListId** | **String**| The numeric ID of the customer list in Demandware. | [optional] |
| **avail** | **Boolean**| Defines category&#39;s visibility status | [optional] [default to true] |

### Return type

[**CustomerCount200Response**](CustomerCount200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="customerFind"></a>
# **customerFind**
> CustomerFind200Response customerFind(findValue, findWhere, findParams, storeId)



Find customers in store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerApi;

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

    CustomerApi apiInstance = new CustomerApi(defaultClient);
    String findValue = "findValue_example"; // String | Entity search that is specified by some value
    String findWhere = "email"; // String | Entity search that is specified by the comma-separated unique fields
    String findParams = "whole_words"; // String | Entity search that is specified by comma-separated parameters
    String storeId = "storeId_example"; // String | Store Id
    try {
      CustomerFind200Response result = apiInstance.customerFind(findValue, findWhere, findParams, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerApi#customerFind");
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
| **findWhere** | **String**| Entity search that is specified by the comma-separated unique fields | [optional] [default to email] |
| **findParams** | **String**| Entity search that is specified by comma-separated parameters | [optional] [default to whole_words] |
| **storeId** | **String**| Store Id | [optional] |

### Return type

[**CustomerFind200Response**](CustomerFind200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="customerGroupAdd"></a>
# **customerGroupAdd**
> CustomerGroupAdd200Response customerGroupAdd(name, storeId, storesIds)



Create customer group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerApi;

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

    CustomerApi apiInstance = new CustomerApi(defaultClient);
    String name = "name_example"; // String | Customer group name
    String storeId = "storeId_example"; // String | Store Id
    String storesIds = "storesIds_example"; // String | Assign customer group to the stores that is specified by comma-separated stores' id
    try {
      CustomerGroupAdd200Response result = apiInstance.customerGroupAdd(name, storeId, storesIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerApi#customerGroupAdd");
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
| **name** | **String**| Customer group name | |
| **storeId** | **String**| Store Id | [optional] |
| **storesIds** | **String**| Assign customer group to the stores that is specified by comma-separated stores&#39; id | [optional] |

### Return type

[**CustomerGroupAdd200Response**](CustomerGroupAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="customerGroupList"></a>
# **customerGroupList**
> ModelResponseCustomerGroupList customerGroupList(pageCursor, start, count, storeId, langId, groupIds, params, exclude, responseFields)



Get list of customers groups.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerApi;

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

    CustomerApi apiInstance = new CustomerApi(defaultClient);
    String pageCursor = "pageCursor_example"; // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String storeId = "storeId_example"; // String | Store Id
    String langId = "langId_example"; // String | Language id
    String groupIds = "groupIds_example"; // String | Groups that will be assigned to a customer
    String params = "id,name,additional_fields"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    try {
      ModelResponseCustomerGroupList result = apiInstance.customerGroupList(pageCursor, start, count, storeId, langId, groupIds, params, exclude, responseFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerApi#customerGroupList");
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
| **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] |
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **storeId** | **String**| Store Id | [optional] |
| **langId** | **String**| Language id | [optional] |
| **groupIds** | **String**| Groups that will be assigned to a customer | [optional] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,name,additional_fields] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |

### Return type

[**ModelResponseCustomerGroupList**](ModelResponseCustomerGroupList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="customerInfo"></a>
# **customerInfo**
> CustomerInfo200Response customerInfo(id, params, responseFields, exclude, storeId)



Get customers&#39; details from store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerApi;

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

    CustomerApi apiInstance = new CustomerApi(defaultClient);
    String id = "id_example"; // String | Retrieves customer's info specified by customer id
    String params = "id,email,first_name,last_name"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String storeId = "storeId_example"; // String | Retrieves customer info specified by store id
    try {
      CustomerInfo200Response result = apiInstance.customerInfo(id, params, responseFields, exclude, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerApi#customerInfo");
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
| **id** | **String**| Retrieves customer&#39;s info specified by customer id | |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,email,first_name,last_name] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **storeId** | **String**| Retrieves customer info specified by store id | [optional] |

### Return type

[**CustomerInfo200Response**](CustomerInfo200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="customerList"></a>
# **customerList**
> ModelResponseCustomerList customerList(pageCursor, start, count, createdFrom, createdTo, modifiedFrom, modifiedTo, params, responseFields, exclude, groupId, storeId, customerListId, avail)



Get list of customers from store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerApi;

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

    CustomerApi apiInstance = new CustomerApi(defaultClient);
    String pageCursor = "pageCursor_example"; // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String createdFrom = "createdFrom_example"; // String | Retrieve entities from their creation date
    String createdTo = "createdTo_example"; // String | Retrieve entities to their creation date
    String modifiedFrom = "modifiedFrom_example"; // String | Retrieve entities from their modification date
    String modifiedTo = "modifiedTo_example"; // String | Retrieve entities to their modification date
    String params = "id,email,first_name,last_name"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String groupId = "groupId_example"; // String | Customer group_id
    String storeId = "storeId_example"; // String | Retrieves customers specified by store id
    String customerListId = "customerListId_example"; // String | The numeric ID of the customer list in Demandware.
    Boolean avail = true; // Boolean | Defines category's visibility status
    try {
      ModelResponseCustomerList result = apiInstance.customerList(pageCursor, start, count, createdFrom, createdTo, modifiedFrom, modifiedTo, params, responseFields, exclude, groupId, storeId, customerListId, avail);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerApi#customerList");
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
| **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] |
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **createdFrom** | **String**| Retrieve entities from their creation date | [optional] |
| **createdTo** | **String**| Retrieve entities to their creation date | [optional] |
| **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] |
| **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,email,first_name,last_name] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **groupId** | **String**| Customer group_id | [optional] |
| **storeId** | **String**| Retrieves customers specified by store id | [optional] |
| **customerListId** | **String**| The numeric ID of the customer list in Demandware. | [optional] |
| **avail** | **Boolean**| Defines category&#39;s visibility status | [optional] [default to true] |

### Return type

[**ModelResponseCustomerList**](ModelResponseCustomerList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="customerUpdate"></a>
# **customerUpdate**
> CustomerUpdate200Response customerUpdate(customerUpdate)



Update information of customer in store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerApi;

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

    CustomerApi apiInstance = new CustomerApi(defaultClient);
    CustomerUpdate customerUpdate = new CustomerUpdate(); // CustomerUpdate | 
    try {
      CustomerUpdate200Response result = apiInstance.customerUpdate(customerUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerApi#customerUpdate");
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
| **customerUpdate** | [**CustomerUpdate**](CustomerUpdate.md)|  | |

### Return type

[**CustomerUpdate200Response**](CustomerUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="customerWishlistList"></a>
# **customerWishlistList**
> CustomerWishlistList200Response customerWishlistList(customerId, id, storeId, start, count, pageCursor, responseFields)



Get a Wish List of customer from the store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerApi;

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

    CustomerApi apiInstance = new CustomerApi(defaultClient);
    String customerId = "customerId_example"; // String | Retrieves orders specified by customer id
    String id = "id_example"; // String | Entity id
    String storeId = "storeId_example"; // String | Store Id
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String pageCursor = "pageCursor_example"; // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
    String responseFields = "{return_code,return_message,pagination,result}"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    try {
      CustomerWishlistList200Response result = apiInstance.customerWishlistList(customerId, id, storeId, start, count, pageCursor, responseFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerApi#customerWishlistList");
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
| **customerId** | **String**| Retrieves orders specified by customer id | |
| **id** | **String**| Entity id | [optional] |
| **storeId** | **String**| Store Id | [optional] |
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to {return_code,return_message,pagination,result}] |

### Return type

[**CustomerWishlistList200Response**](CustomerWishlistList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

