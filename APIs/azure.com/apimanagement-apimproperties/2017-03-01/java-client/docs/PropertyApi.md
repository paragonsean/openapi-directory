# PropertyApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**propertyCreateOrUpdate**](PropertyApi.md#propertyCreateOrUpdate) | **PUT** /properties/{propId} |  |
| [**propertyDelete**](PropertyApi.md#propertyDelete) | **DELETE** /properties/{propId} |  |
| [**propertyGet**](PropertyApi.md#propertyGet) | **GET** /properties/{propId} |  |
| [**propertyList**](PropertyApi.md#propertyList) | **GET** /properties |  |
| [**propertyUpdate**](PropertyApi.md#propertyUpdate) | **PATCH** /properties/{propId} |  |


<a id="propertyCreateOrUpdate"></a>
# **propertyCreateOrUpdate**
> PropertyContract propertyCreateOrUpdate(propId, apiVersion, parameters)



Creates or updates a property.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    PropertyApi apiInstance = new PropertyApi(defaultClient);
    String propId = "propId_example"; // String | Identifier of the property.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    PropertyContract parameters = new PropertyContract(); // PropertyContract | Create parameters.
    try {
      PropertyContract result = apiInstance.propertyCreateOrUpdate(propId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertyApi#propertyCreateOrUpdate");
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
| **propId** | **String**| Identifier of the property. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **parameters** | [**PropertyContract**](PropertyContract.md)| Create parameters. | |

### Return type

[**PropertyContract**](PropertyContract.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Property was successfully updated. |  -  |
| **201** | Property was successfully created. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="propertyDelete"></a>
# **propertyDelete**
> propertyDelete(propId, ifMatch, apiVersion)



Deletes specific property from the API Management service instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    PropertyApi apiInstance = new PropertyApi(defaultClient);
    String propId = "propId_example"; // String | Identifier of the property.
    String ifMatch = "ifMatch_example"; // String | The entity state (Etag) version of the property to delete. A value of \"*\" can be used for If-Match to unconditionally apply the operation.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      apiInstance.propertyDelete(propId, ifMatch, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertyApi#propertyDelete");
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
| **propId** | **String**| Identifier of the property. | |
| **ifMatch** | **String**| The entity state (Etag) version of the property to delete. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Property was successfully deleted. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="propertyGet"></a>
# **propertyGet**
> PropertyContract propertyGet(propId, apiVersion)



Gets the details of the property specified by its identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    PropertyApi apiInstance = new PropertyApi(defaultClient);
    String propId = "propId_example"; // String | Identifier of the property.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      PropertyContract result = apiInstance.propertyGet(propId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertyApi#propertyGet");
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
| **propId** | **String**| Identifier of the property. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**PropertyContract**](PropertyContract.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body contains the specified Property entity. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="propertyList"></a>
# **propertyList**
> PropertyCollection propertyList(apiVersion, $filter, $top, $skip)



Lists a collection of properties defined within a service instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    PropertyApi apiInstance = new PropertyApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | | Field | Supported operators    | Supported functions                                   | |-------|------------------------|-------------------------------------------------------| | tags  | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith, any, all | | name  | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith           |
    Integer $top = 56; // Integer | Number of records to return.
    Integer $skip = 56; // Integer | Number of records to skip.
    try {
      PropertyCollection result = apiInstance.propertyList(apiVersion, $filter, $top, $skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertyApi#propertyList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **$filter** | **String**| | Field | Supported operators    | Supported functions                                   | |-------|------------------------|-------------------------------------------------------| | tags  | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith, any, all | | name  | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith           | | [optional] |
| **$top** | **Integer**| Number of records to return. | [optional] |
| **$skip** | **Integer**| Number of records to skip. | [optional] |

### Return type

[**PropertyCollection**](PropertyCollection.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A Collection of the Property entities for the specified API Management service instance. |  -  |

<a id="propertyUpdate"></a>
# **propertyUpdate**
> propertyUpdate(propId, ifMatch, apiVersion, parameters)



Updates the specific property.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    PropertyApi apiInstance = new PropertyApi(defaultClient);
    String propId = "propId_example"; // String | Identifier of the property.
    String ifMatch = "ifMatch_example"; // String | The entity state (Etag) version of the property to update. A value of \"*\" can be used for If-Match to unconditionally apply the operation.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    PropertyUpdateParameters parameters = new PropertyUpdateParameters(); // PropertyUpdateParameters | Update parameters.
    try {
      apiInstance.propertyUpdate(propId, ifMatch, apiVersion, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertyApi#propertyUpdate");
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
| **propId** | **String**| Identifier of the property. | |
| **ifMatch** | **String**| The entity state (Etag) version of the property to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **parameters** | [**PropertyUpdateParameters**](PropertyUpdateParameters.md)| Update parameters. | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Property was successfully updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

