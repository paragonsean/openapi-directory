# LocationsApi

All URIs are relative to *https://unify.apideck.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**locationsAdd**](LocationsApi.md#locationsAdd) | **POST** /pos/locations | Create Location |
| [**locationsAll**](LocationsApi.md#locationsAll) | **GET** /pos/locations | List Locations |
| [**locationsDelete**](LocationsApi.md#locationsDelete) | **DELETE** /pos/locations/{id} | Delete Location |
| [**locationsOne**](LocationsApi.md#locationsOne) | **GET** /pos/locations/{id} | Get Location |
| [**locationsUpdate**](LocationsApi.md#locationsUpdate) | **PATCH** /pos/locations/{id} | Update Location |


<a id="locationsAdd"></a>
# **locationsAdd**
> CreateLocationResponse locationsAdd(xApideckConsumerId, xApideckAppId, location, raw, xApideckServiceId)

Create Location

Create Location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    Location location = new Location(); // Location | 
    Boolean raw = false; // Boolean | Include raw response. Mostly used for debugging purposes
    String xApideckServiceId = "xApideckServiceId_example"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    try {
      CreateLocationResponse result = apiInstance.locationsAdd(xApideckConsumerId, xApideckAppId, location, raw, xApideckServiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#locationsAdd");
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
| **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | |
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **location** | [**Location**](Location.md)|  | |
| **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false] |
| **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] |

### Return type

[**CreateLocationResponse**](CreateLocationResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Locations |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **422** | Unprocessable |  -  |
| **0** | Unexpected error |  -  |

<a id="locationsAll"></a>
# **locationsAll**
> GetLocationsResponse locationsAll(xApideckConsumerId, xApideckAppId, raw, xApideckServiceId, cursor, limit, fields)

List Locations

List Locations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    Boolean raw = false; // Boolean | Include raw response. Mostly used for debugging purposes
    String xApideckServiceId = "xApideckServiceId_example"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    String cursor = "cursor_example"; // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    Integer limit = 20; // Integer | Number of results to return. Minimum 1, Maximum 200, Default 20
    String fields = "id,updated_at"; // String | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded.
    try {
      GetLocationsResponse result = apiInstance.locationsAll(xApideckConsumerId, xApideckAppId, raw, xApideckServiceId, cursor, limit, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#locationsAll");
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
| **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | |
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false] |
| **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] |
| **cursor** | **String**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional] |
| **limit** | **Integer**| Number of results to return. Minimum 1, Maximum 200, Default 20 | [optional] [default to 20] |
| **fields** | **String**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional] |

### Return type

[**GetLocationsResponse**](GetLocationsResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Locations |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **422** | Unprocessable |  -  |
| **0** | Unexpected error |  -  |

<a id="locationsDelete"></a>
# **locationsDelete**
> DeleteLocationResponse locationsDelete(id, xApideckConsumerId, xApideckAppId, xApideckServiceId, raw)

Delete Location

Delete Location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | ID of the record you are acting upon.
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    String xApideckServiceId = "xApideckServiceId_example"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    Boolean raw = false; // Boolean | Include raw response. Mostly used for debugging purposes
    try {
      DeleteLocationResponse result = apiInstance.locationsDelete(id, xApideckConsumerId, xApideckAppId, xApideckServiceId, raw);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#locationsDelete");
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
| **id** | **String**| ID of the record you are acting upon. | |
| **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | |
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] |
| **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false] |

### Return type

[**DeleteLocationResponse**](DeleteLocationResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Locations |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **422** | Unprocessable |  -  |
| **0** | Unexpected error |  -  |

<a id="locationsOne"></a>
# **locationsOne**
> GetLocationResponse locationsOne(id, xApideckConsumerId, xApideckAppId, xApideckServiceId, raw, fields)

Get Location

Get Location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | ID of the record you are acting upon.
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    String xApideckServiceId = "xApideckServiceId_example"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    Boolean raw = false; // Boolean | Include raw response. Mostly used for debugging purposes
    String fields = "id,updated_at"; // String | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded.
    try {
      GetLocationResponse result = apiInstance.locationsOne(id, xApideckConsumerId, xApideckAppId, xApideckServiceId, raw, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#locationsOne");
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
| **id** | **String**| ID of the record you are acting upon. | |
| **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | |
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] |
| **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false] |
| **fields** | **String**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional] |

### Return type

[**GetLocationResponse**](GetLocationResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Locations |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **422** | Unprocessable |  -  |
| **0** | Unexpected error |  -  |

<a id="locationsUpdate"></a>
# **locationsUpdate**
> UpdateLocationResponse locationsUpdate(id, xApideckConsumerId, xApideckAppId, location, xApideckServiceId, raw)

Update Location

Update Location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | ID of the record you are acting upon.
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    Location location = new Location(); // Location | 
    String xApideckServiceId = "xApideckServiceId_example"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    Boolean raw = false; // Boolean | Include raw response. Mostly used for debugging purposes
    try {
      UpdateLocationResponse result = apiInstance.locationsUpdate(id, xApideckConsumerId, xApideckAppId, location, xApideckServiceId, raw);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#locationsUpdate");
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
| **id** | **String**| ID of the record you are acting upon. | |
| **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | |
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **location** | [**Location**](Location.md)|  | |
| **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] |
| **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false] |

### Return type

[**UpdateLocationResponse**](UpdateLocationResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Locations |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **422** | Unprocessable |  -  |
| **0** | Unexpected error |  -  |

