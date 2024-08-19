# BrowserApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**browseCSV**](BrowserApi.md#browseCSV) | **GET** /browser/csv | Searches for data (ie. customer, task, etc) and returns it in a CSV form. |
| [**browseJSON**](BrowserApi.md#browseJSON) | **GET** /browser | Searches for data (ie. customer, task, etc) and returns it in a tabular form. |
| [**create**](BrowserApi.md#create) | **POST** /browser/views/for/{className} | Creates view for given class. |
| [**delete**](BrowserApi.md#delete) | **DELETE** /browser/views/{viewId} | Removes a view. |
| [**deleteColumn**](BrowserApi.md#deleteColumn) | **DELETE** /browser/views/{viewId}/columns/{columnName} | Deletes a single column from view. |
| [**get**](BrowserApi.md#get) | **GET** /browser/views/{viewId} | Returns all view&#39;s information. |
| [**getColumnSettings**](BrowserApi.md#getColumnSettings) | **GET** /browser/views/{viewId}/columns/{columnName}/settings | Returns column&#39;s specific settings. |
| [**getColumns**](BrowserApi.md#getColumns) | **GET** /browser/views/{viewId}/columns | Returns columns defined in view. |
| [**getCurrentViewDetails**](BrowserApi.md#getCurrentViewDetails) | **GET** /browser/views/details/for/{className} | Returns current view&#39;s detailed information, suitable for browser. |
| [**getFilter**](BrowserApi.md#getFilter) | **GET** /browser/views/{viewId}/filter | Returns view&#39;s filter. |
| [**getLocalSettings**](BrowserApi.md#getLocalSettings) | **GET** /browser/views/{viewId}/settings/local | Returns view&#39;s local settings (for current user). |
| [**getOrder**](BrowserApi.md#getOrder) | **GET** /browser/views/{viewId}/order | Returns view&#39;s order settings. |
| [**getPermissions**](BrowserApi.md#getPermissions) | **GET** /browser/views/{viewId}/permissions | Returns view&#39;s permissions. |
| [**getSettings**](BrowserApi.md#getSettings) | **GET** /browser/views/{viewId}/settings | Returns view&#39;s settings. |
| [**getViewDetails**](BrowserApi.md#getViewDetails) | **GET** /browser/views/details/for/{className}/{viewId} | Returns view&#39;s detailed information, suitable for browser. |
| [**getViewsBrief**](BrowserApi.md#getViewsBrief) | **GET** /browser/views/for/{className} | Returns views&#39; brief. |
| [**selectViewAndGetItsDetails**](BrowserApi.md#selectViewAndGetItsDetails) | **POST** /browser/views/details/for/{className}/{viewId} | Selects given view as current and returns its detailed information, suitable for browser. |
| [**update**](BrowserApi.md#update) | **PUT** /browser/views/{viewId} | Updates all view&#39;s information. |
| [**updateColumnSettings**](BrowserApi.md#updateColumnSettings) | **PUT** /browser/views/{viewId}/columns/{columnName}/settings | Updates column&#39;s specific settings. |
| [**updateColumns**](BrowserApi.md#updateColumns) | **PUT** /browser/views/{viewId}/columns | Updates columns in view. |
| [**updateFilter**](BrowserApi.md#updateFilter) | **PUT** /browser/views/{viewId}/filter | Updates view&#39;s filter. |
| [**updateFilterProperty**](BrowserApi.md#updateFilterProperty) | **PUT** /browser/views/{viewId}/filter/{filterProperty} | Updates view&#39;s filter property. |
| [**updateLocalSettings**](BrowserApi.md#updateLocalSettings) | **PUT** /browser/views/{viewId}/settings/local | Updates view&#39;s local settings (for current user). |
| [**updateOrder**](BrowserApi.md#updateOrder) | **PUT** /browser/views/{viewId}/order | Updates view&#39;s order settings. |
| [**updatePermissions**](BrowserApi.md#updatePermissions) | **PUT** /browser/views/{viewId}/permissions | Updates view&#39;s permissions. |
| [**updateSettings**](BrowserApi.md#updateSettings) | **PUT** /browser/views/{viewId}/settings | Updates view&#39;s settings. |


<a id="browseCSV"></a>
# **browseCSV**
> Object browseCSV(viewId, separator, secondarySeparator, additionalOrder)

Searches for data (ie. customer, task, etc) and returns it in a CSV form.

Searches for data (ie. customer, task, etc) and returns it in a CSV form.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Long viewId = 56L; // Long | view's identifier
    String separator = "separator_example"; // String | csv field separator
    String secondarySeparator = "secondarySeparator_example"; // String | secondary csv field separator
    String additionalOrder = "additionalOrder_example"; // String | 
    try {
      Object result = apiInstance.browseCSV(viewId, separator, secondarySeparator, additionalOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#browseCSV");
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
| **viewId** | **Long**| view&#39;s identifier | [optional] |
| **separator** | **String**| csv field separator | [optional] |
| **secondarySeparator** | **String**| secondary csv field separator | [optional] |
| **additionalOrder** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="browseJSON"></a>
# **browseJSON**
> Object browseJSON(viewId, page, additionalOrder, useDeferredColumns, maxRows)

Searches for data (ie. customer, task, etc) and returns it in a tabular form.

Searches for data (ie. customer, task, etc) and returns it in a tabular form.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Long viewId = 56L; // Long | view's identifier
    Integer page = 0; // Integer | 
    String additionalOrder = "additionalOrder_example"; // String | 
    String useDeferredColumns = "useDeferredColumns_example"; // String | 
    Integer maxRows = 0; // Integer | overrides view's default rows limit, supported values 10 to 1000
    try {
      Object result = apiInstance.browseJSON(viewId, page, additionalOrder, useDeferredColumns, maxRows);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#browseJSON");
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
| **viewId** | **Long**| view&#39;s identifier | [optional] |
| **page** | **Integer**|  | [optional] [default to 0] |
| **additionalOrder** | **String**|  | [optional] |
| **useDeferredColumns** | **String**|  | [optional] |
| **maxRows** | **Integer**| overrides view&#39;s default rows limit, supported values 10 to 1000 | [optional] [default to 0] |

### Return type

**Object**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="create"></a>
# **create**
> ViewWithIdDTO create(className, viewDTO)

Creates view for given class.

Creates view for given class.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    String className = "className_example"; // String | view's class name
    ViewDTO viewDTO = new ViewDTO(); // ViewDTO | Created view for given class.
    try {
      ViewWithIdDTO result = apiInstance.create(className, viewDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#create");
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
| **className** | **String**| view&#39;s class name | |
| **viewDTO** | [**ViewDTO**](ViewDTO.md)| Created view for given class. | |

### Return type

[**ViewWithIdDTO**](ViewWithIdDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="delete"></a>
# **delete**
> delete(viewId)

Removes a view.

Removes a view. No content is returned upon success (204).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Long viewId = 56L; // Long | view's internal identifier
    try {
      apiInstance.delete(viewId);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#delete");
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
| **viewId** | **Long**| view&#39;s internal identifier | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="deleteColumn"></a>
# **deleteColumn**
> List&lt;ColumnDTO&gt; deleteColumn(viewId, columnName)

Deletes a single column from view.

Deletes a single column from view.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Long viewId = 56L; // Long | view's identifier
    String columnName = "columnName_example"; // String | column's name
    try {
      List<ColumnDTO> result = apiInstance.deleteColumn(viewId, columnName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#deleteColumn");
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
| **viewId** | **Long**| view&#39;s identifier | |
| **columnName** | **String**| column&#39;s name | |

### Return type

[**List&lt;ColumnDTO&gt;**](ColumnDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="get"></a>
# **get**
> ViewDTO get(viewId)

Returns all view&#39;s information.

Returns all view&#39;s information (ie. name, columns, filters, etc).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Long viewId = 56L; // Long | view's identifier
    try {
      ViewDTO result = apiInstance.get(viewId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#get");
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
| **viewId** | **Long**| view&#39;s identifier | |

### Return type

[**ViewDTO**](ViewDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getColumnSettings"></a>
# **getColumnSettings**
> Object getColumnSettings(viewId, columnName)

Returns column&#39;s specific settings.

Returns column&#39;s specific settings. For example when column describes money amount we can decide whether it should display currency or not.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Long viewId = 56L; // Long | view's identifier
    String columnName = "columnName_example"; // String | column's name
    try {
      Object result = apiInstance.getColumnSettings(viewId, columnName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#getColumnSettings");
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
| **viewId** | **Long**| view&#39;s identifier | |
| **columnName** | **String**| column&#39;s name | |

### Return type

**Object**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getColumns"></a>
# **getColumns**
> List&lt;ColumnDTO&gt; getColumns(viewId)

Returns columns defined in view.

Returns columns defined in view.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Long viewId = 56L; // Long | view's identifier
    try {
      List<ColumnDTO> result = apiInstance.getColumns(viewId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#getColumns");
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
| **viewId** | **Long**| view&#39;s identifier | |

### Return type

[**List&lt;ColumnDTO&gt;**](ColumnDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getCurrentViewDetails"></a>
# **getCurrentViewDetails**
> ViewDetailsDTO getCurrentViewDetails(className, placeName)

Returns current view&#39;s detailed information, suitable for browser.

Returns current view&#39;s detailed information, suitable for browser.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    String className = "className_example"; // String | views' class name
    String placeName = "default"; // String | place name (denotes specific place in system with the table)
    try {
      ViewDetailsDTO result = apiInstance.getCurrentViewDetails(className, placeName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#getCurrentViewDetails");
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
| **className** | **String**| views&#39; class name | |
| **placeName** | **String**| place name (denotes specific place in system with the table) | [optional] [default to default] |

### Return type

[**ViewDetailsDTO**](ViewDetailsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getFilter"></a>
# **getFilter**
> FilterDTO getFilter(viewId)

Returns view&#39;s filter.

Returns view&#39;s filter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Long viewId = 56L; // Long | view's identifier
    try {
      FilterDTO result = apiInstance.getFilter(viewId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#getFilter");
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
| **viewId** | **Long**| view&#39;s identifier | |

### Return type

[**FilterDTO**](FilterDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getLocalSettings"></a>
# **getLocalSettings**
> LocalSettingsDTO getLocalSettings(viewId)

Returns view&#39;s local settings (for current user).

Returns view&#39;s local settings (for current user).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Long viewId = 56L; // Long | view's identifier
    try {
      LocalSettingsDTO result = apiInstance.getLocalSettings(viewId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#getLocalSettings");
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
| **viewId** | **Long**| view&#39;s identifier | |

### Return type

[**LocalSettingsDTO**](LocalSettingsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getOrder"></a>
# **getOrder**
> OrderDTO getOrder(viewId)

Returns view&#39;s order settings.

Returns view&#39;s order settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Long viewId = 56L; // Long | view's identifier
    try {
      OrderDTO result = apiInstance.getOrder(viewId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#getOrder");
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
| **viewId** | **Long**| view&#39;s identifier | |

### Return type

[**OrderDTO**](OrderDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getPermissions"></a>
# **getPermissions**
> PermissionsDTO getPermissions(viewId)

Returns view&#39;s permissions.

Returns view&#39;s permissions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Long viewId = 56L; // Long | view's identifier
    try {
      PermissionsDTO result = apiInstance.getPermissions(viewId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#getPermissions");
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
| **viewId** | **Long**| view&#39;s identifier | |

### Return type

[**PermissionsDTO**](PermissionsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getSettings"></a>
# **getSettings**
> SettingsDTO getSettings(viewId)

Returns view&#39;s settings.

Returns view&#39;s settings (ie. name).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Long viewId = 56L; // Long | view's identifier
    try {
      SettingsDTO result = apiInstance.getSettings(viewId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#getSettings");
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
| **viewId** | **Long**| view&#39;s identifier | |

### Return type

[**SettingsDTO**](SettingsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getViewDetails"></a>
# **getViewDetails**
> ViewDetailsDTO getViewDetails(className, viewId, placeName)

Returns view&#39;s detailed information, suitable for browser.

Returns view&#39;s detailed information, suitable for browser.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    String className = "className_example"; // String | views' class name
    Long viewId = 56L; // Long | 
    String placeName = "default"; // String | place name (denotes specific place in system with the table)
    try {
      ViewDetailsDTO result = apiInstance.getViewDetails(className, viewId, placeName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#getViewDetails");
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
| **className** | **String**| views&#39; class name | |
| **viewId** | **Long**|  | |
| **placeName** | **String**| place name (denotes specific place in system with the table) | [optional] [default to default] |

### Return type

[**ViewDetailsDTO**](ViewDetailsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getViewsBrief"></a>
# **getViewsBrief**
> ViewsBriefDTO getViewsBrief(className, placeName)

Returns views&#39; brief.

Returns views&#39; brief.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    String className = "className_example"; // String | views' class name
    String placeName = "default"; // String | place name (denotes specific place in system with the table)
    try {
      ViewsBriefDTO result = apiInstance.getViewsBrief(className, placeName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#getViewsBrief");
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
| **className** | **String**| views&#39; class name | |
| **placeName** | **String**| place name (denotes specific place in system with the table) | [optional] [default to default] |

### Return type

[**ViewsBriefDTO**](ViewsBriefDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="selectViewAndGetItsDetails"></a>
# **selectViewAndGetItsDetails**
> ViewDetailsDTO selectViewAndGetItsDetails(className, viewId, placeNameDenotesSpecificPlaceInSystemWithTheTable)

Selects given view as current and returns its detailed information, suitable for browser.

Selects given view as current and returns its detailed information, suitable for browser.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    String className = "className_example"; // String | views' class name
    Long viewId = 56L; // Long | 
    String placeNameDenotesSpecificPlaceInSystemWithTheTable = "default"; // String | 
    try {
      ViewDetailsDTO result = apiInstance.selectViewAndGetItsDetails(className, viewId, placeNameDenotesSpecificPlaceInSystemWithTheTable);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#selectViewAndGetItsDetails");
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
| **className** | **String**| views&#39; class name | |
| **viewId** | **Long**|  | |
| **placeNameDenotesSpecificPlaceInSystemWithTheTable** | **String**|  | [optional] [default to default] |

### Return type

[**ViewDetailsDTO**](ViewDetailsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="update"></a>
# **update**
> ViewDTO update(viewId, viewDTO)

Updates all view&#39;s information.

Updates all view&#39;s information (ie. name, columns, filters, etc).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Long viewId = 56L; // Long | view's identifier
    ViewDTO viewDTO = new ViewDTO(); // ViewDTO | Updated all view's information.
    try {
      ViewDTO result = apiInstance.update(viewId, viewDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#update");
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
| **viewId** | **Long**| view&#39;s identifier | |
| **viewDTO** | [**ViewDTO**](ViewDTO.md)| Updated all view&#39;s information. | |

### Return type

[**ViewDTO**](ViewDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="updateColumnSettings"></a>
# **updateColumnSettings**
> Object updateColumnSettings(viewId, columnName, body)

Updates column&#39;s specific settings.

Updates column&#39;s specific settings. For example when column describes money amount we can decide whether it should display currency or not.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Long viewId = 56L; // Long | view's identifier
    String columnName = "columnName_example"; // String | column's name
    Object body = /home-api/assets/examples/browsers/views/updateColumnSettings.json#requestBody; // Object | Updated column's specific settings.
    try {
      Object result = apiInstance.updateColumnSettings(viewId, columnName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#updateColumnSettings");
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
| **viewId** | **Long**| view&#39;s identifier | |
| **columnName** | **String**| column&#39;s name | |
| **body** | **Object**| Updated column&#39;s specific settings. | |

### Return type

**Object**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="updateColumns"></a>
# **updateColumns**
> List&lt;ColumnDTO&gt; updateColumns(viewId, columnDTO)

Updates columns in view.

Updates columns in view.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Long viewId = 56L; // Long | view's identifier
    List<ColumnDTO> columnDTO = Arrays.asList(); // List<ColumnDTO> | Updated columns in view.
    try {
      List<ColumnDTO> result = apiInstance.updateColumns(viewId, columnDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#updateColumns");
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
| **viewId** | **Long**| view&#39;s identifier | |
| **columnDTO** | [**List&lt;ColumnDTO&gt;**](ColumnDTO.md)| Updated columns in view. | |

### Return type

[**List&lt;ColumnDTO&gt;**](ColumnDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="updateFilter"></a>
# **updateFilter**
> FilterDTO updateFilter(viewId, filterPropertyDTO)

Updates view&#39;s filter.

Updates view&#39;s filter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Long viewId = 56L; // Long | view's identifier
    List<FilterPropertyDTO> filterPropertyDTO = Arrays.asList(); // List<FilterPropertyDTO> | Updated view's filter.
    try {
      FilterDTO result = apiInstance.updateFilter(viewId, filterPropertyDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#updateFilter");
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
| **viewId** | **Long**| view&#39;s identifier | |
| **filterPropertyDTO** | [**List&lt;FilterPropertyDTO&gt;**](FilterPropertyDTO.md)| Updated view&#39;s filter. | |

### Return type

[**FilterDTO**](FilterDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="updateFilterProperty"></a>
# **updateFilterProperty**
> Object updateFilterProperty(viewId, filterProperty, filterPropertyDTO)

Updates view&#39;s filter property.

Updates view&#39;s filter property.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Long viewId = 56L; // Long | view's identifier
    String filterProperty = "filterProperty_example"; // String | view's filter property name
    FilterPropertyDTO filterPropertyDTO = new FilterPropertyDTO(); // FilterPropertyDTO | Updated view's filter property.
    try {
      Object result = apiInstance.updateFilterProperty(viewId, filterProperty, filterPropertyDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#updateFilterProperty");
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
| **viewId** | **Long**| view&#39;s identifier | |
| **filterProperty** | **String**| view&#39;s filter property name | |
| **filterPropertyDTO** | [**FilterPropertyDTO**](FilterPropertyDTO.md)| Updated view&#39;s filter property. | |

### Return type

**Object**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="updateLocalSettings"></a>
# **updateLocalSettings**
> LocalSettingsDTO updateLocalSettings(viewId, localSettingsDTO)

Updates view&#39;s local settings (for current user).

Updates view&#39;s local settings (for current user).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Long viewId = 56L; // Long | view's identifier
    LocalSettingsDTO localSettingsDTO = new LocalSettingsDTO(); // LocalSettingsDTO | Updated view's local settings (for current user).
    try {
      LocalSettingsDTO result = apiInstance.updateLocalSettings(viewId, localSettingsDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#updateLocalSettings");
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
| **viewId** | **Long**| view&#39;s identifier | |
| **localSettingsDTO** | [**LocalSettingsDTO**](LocalSettingsDTO.md)| Updated view&#39;s local settings (for current user). | |

### Return type

[**LocalSettingsDTO**](LocalSettingsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="updateOrder"></a>
# **updateOrder**
> OrderDTO updateOrder(viewId, orderDTO)

Updates view&#39;s order settings.

Updates view&#39;s order settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Long viewId = 56L; // Long | view's identifier
    OrderDTO orderDTO = new OrderDTO(); // OrderDTO | Updated view's order settings.
    try {
      OrderDTO result = apiInstance.updateOrder(viewId, orderDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#updateOrder");
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
| **viewId** | **Long**| view&#39;s identifier | |
| **orderDTO** | [**OrderDTO**](OrderDTO.md)| Updated view&#39;s order settings. | |

### Return type

[**OrderDTO**](OrderDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="updatePermissions"></a>
# **updatePermissions**
> PermissionsDTO updatePermissions(viewId, permissionsDTO)

Updates view&#39;s permissions.

Updates view&#39;s permissions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Long viewId = 56L; // Long | view's identifier
    PermissionsDTO permissionsDTO = new PermissionsDTO(); // PermissionsDTO | Updated view's permissions.
    try {
      PermissionsDTO result = apiInstance.updatePermissions(viewId, permissionsDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#updatePermissions");
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
| **viewId** | **Long**| view&#39;s identifier | |
| **permissionsDTO** | [**PermissionsDTO**](PermissionsDTO.md)| Updated view&#39;s permissions. | |

### Return type

[**PermissionsDTO**](PermissionsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="updateSettings"></a>
# **updateSettings**
> SettingsDTO updateSettings(viewId, settingsDTO)

Updates view&#39;s settings.

Updates view&#39;s settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Long viewId = 56L; // Long | view's identifier
    SettingsDTO settingsDTO = new SettingsDTO(); // SettingsDTO | Updated view's settings.
    try {
      SettingsDTO result = apiInstance.updateSettings(viewId, settingsDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#updateSettings");
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
| **viewId** | **Long**| view&#39;s identifier | |
| **settingsDTO** | [**SettingsDTO**](SettingsDTO.md)| Updated view&#39;s settings. | |

### Return type

[**SettingsDTO**](SettingsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

