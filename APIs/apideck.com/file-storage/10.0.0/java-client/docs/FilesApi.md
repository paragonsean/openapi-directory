# FilesApi

All URIs are relative to *https://unify.apideck.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**filesAll**](FilesApi.md#filesAll) | **GET** /file-storage/files | List Files |
| [**filesDelete**](FilesApi.md#filesDelete) | **DELETE** /file-storage/files/{id} | Delete File |
| [**filesDownload**](FilesApi.md#filesDownload) | **GET** /file-storage/files/{id}/download | Download File |
| [**filesExport**](FilesApi.md#filesExport) | **GET** /file-storage/files/{id}/export | Export File |
| [**filesOne**](FilesApi.md#filesOne) | **GET** /file-storage/files/{id} | Get File |
| [**filesSearch**](FilesApi.md#filesSearch) | **POST** /file-storage/files/search | Search Files |
| [**filesUpdate**](FilesApi.md#filesUpdate) | **PATCH** /file-storage/files/{id} | Rename or move File |
| [**filesUpload**](FilesApi.md#filesUpload) | **POST** /file-storage/files | Upload file |


<a id="filesAll"></a>
# **filesAll**
> GetFilesResponse filesAll(xApideckConsumerId, xApideckAppId, raw, xApideckServiceId, cursor, limit, filter, sort, passThrough, fields)

List Files

List Files

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    Boolean raw = false; // Boolean | Include raw response. Mostly used for debugging purposes
    String xApideckServiceId = "xApideckServiceId_example"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    String cursor = "cursor_example"; // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    Integer limit = 20; // Integer | Number of results to return. Minimum 1, Maximum 200, Default 20
    FilesFilter filter = new FilesFilter(); // FilesFilter | Apply filters
    FilesSort sort = new FilesSort(); // FilesSort | Apply sorting
    PassThroughQuery passThrough = null; // PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads
    String fields = "id,updated_at"; // String | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded.
    try {
      GetFilesResponse result = apiInstance.filesAll(xApideckConsumerId, xApideckAppId, raw, xApideckServiceId, cursor, limit, filter, sort, passThrough, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesAll");
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
| **filter** | [**FilesFilter**](.md)| Apply filters | [optional] |
| **sort** | [**FilesSort**](.md)| Apply sorting | [optional] |
| **passThrough** | [**PassThroughQuery**](Object.md)| Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads | [optional] |
| **fields** | **String**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional] |

### Return type

[**GetFilesResponse**](GetFilesResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Files |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **422** | Unprocessable |  -  |
| **0** | Unexpected error |  -  |

<a id="filesDelete"></a>
# **filesDelete**
> DeleteFileResponse filesDelete(id, xApideckConsumerId, xApideckAppId, xApideckServiceId, raw)

Delete File

Delete File

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String id = "id_example"; // String | ID of the record you are acting upon.
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    String xApideckServiceId = "xApideckServiceId_example"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    Boolean raw = false; // Boolean | Include raw response. Mostly used for debugging purposes
    try {
      DeleteFileResponse result = apiInstance.filesDelete(id, xApideckConsumerId, xApideckAppId, xApideckServiceId, raw);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesDelete");
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

[**DeleteFileResponse**](DeleteFileResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Files |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **422** | Unprocessable |  -  |
| **0** | Unexpected error |  -  |

<a id="filesDownload"></a>
# **filesDownload**
> File filesDownload(id, xApideckConsumerId, xApideckAppId, xApideckServiceId, fields)

Download File

Download File

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String id = "id_example"; // String | ID of the record you are acting upon.
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    String xApideckServiceId = "xApideckServiceId_example"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    String fields = "id,updated_at"; // String | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded.
    try {
      File result = apiInstance.filesDownload(id, xApideckConsumerId, xApideckAppId, xApideckServiceId, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesDownload");
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
| **fields** | **String**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional] |

### Return type

[**File**](File.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File Download |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **422** | Unprocessable |  -  |
| **0** | Unexpected error |  -  |

<a id="filesExport"></a>
# **filesExport**
> File filesExport(id, xApideckConsumerId, xApideckAppId, format, xApideckServiceId, fields)

Export File

Export File

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String id = "id_example"; // String | ID of the record you are acting upon.
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    String format = "pdf"; // String | File format to export this file to. A list of available file formats for the current file is available as `export_formats` on the File resource.
    String xApideckServiceId = "xApideckServiceId_example"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    String fields = "id,updated_at"; // String | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded.
    try {
      File result = apiInstance.filesExport(id, xApideckConsumerId, xApideckAppId, format, xApideckServiceId, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesExport");
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
| **format** | **String**| File format to export this file to. A list of available file formats for the current file is available as &#x60;export_formats&#x60; on the File resource. | |
| **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] |
| **fields** | **String**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional] |

### Return type

[**File**](File.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File Download |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **422** | Unprocessable |  -  |
| **0** | Unexpected error |  -  |

<a id="filesOne"></a>
# **filesOne**
> GetFileResponse filesOne(id, xApideckConsumerId, xApideckAppId, xApideckServiceId, raw, fields)

Get File

Get File

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String id = "id_example"; // String | ID of the record you are acting upon.
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    String xApideckServiceId = "xApideckServiceId_example"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    Boolean raw = false; // Boolean | Include raw response. Mostly used for debugging purposes
    String fields = "id,updated_at"; // String | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded.
    try {
      GetFileResponse result = apiInstance.filesOne(id, xApideckConsumerId, xApideckAppId, xApideckServiceId, raw, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesOne");
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

[**GetFileResponse**](GetFileResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **422** | Unprocessable |  -  |
| **0** | Unexpected error |  -  |

<a id="filesSearch"></a>
# **filesSearch**
> GetFilesResponse filesSearch(xApideckConsumerId, xApideckAppId, filesSearch, xApideckServiceId, passThrough, fields, cursor, limit)

Search Files

Search Files

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    FilesSearch filesSearch = new FilesSearch(); // FilesSearch | 
    String xApideckServiceId = "xApideckServiceId_example"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    PassThroughQuery passThrough = null; // PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads
    String fields = "id,updated_at"; // String | The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields \"name\", \"email\" and \"addresses.city\". If any other fields are available, they will be excluded.
    String cursor = "cursor_example"; // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    Integer limit = 20; // Integer | Number of results to return. Minimum 1, Maximum 200, Default 20
    try {
      GetFilesResponse result = apiInstance.filesSearch(xApideckConsumerId, xApideckAppId, filesSearch, xApideckServiceId, passThrough, fields, cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesSearch");
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
| **filesSearch** | [**FilesSearch**](FilesSearch.md)|  | |
| **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] |
| **passThrough** | [**PassThroughQuery**](Object.md)| Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads | [optional] |
| **fields** | **String**| The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded. | [optional] |
| **cursor** | **String**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional] |
| **limit** | **Integer**| Number of results to return. Minimum 1, Maximum 200, Default 20 | [optional] [default to 20] |

### Return type

[**GetFilesResponse**](GetFilesResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Files |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **422** | Unprocessable |  -  |
| **0** | Unexpected error |  -  |

<a id="filesUpdate"></a>
# **filesUpdate**
> UpdateFileResponse filesUpdate(id, xApideckConsumerId, xApideckAppId, updateFileRequest, xApideckServiceId, raw)

Rename or move File

Rename or move File

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String id = "id_example"; // String | ID of the record you are acting upon.
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    UpdateFileRequest updateFileRequest = new UpdateFileRequest(); // UpdateFileRequest | 
    String xApideckServiceId = "xApideckServiceId_example"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    Boolean raw = false; // Boolean | Include raw response. Mostly used for debugging purposes
    try {
      UpdateFileResponse result = apiInstance.filesUpdate(id, xApideckConsumerId, xApideckAppId, updateFileRequest, xApideckServiceId, raw);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesUpdate");
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
| **updateFileRequest** | [**UpdateFileRequest**](UpdateFileRequest.md)|  | |
| **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] |
| **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false] |

### Return type

[**UpdateFileResponse**](UpdateFileResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Files |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **422** | Unprocessable |  -  |
| **0** | Unexpected error |  -  |

<a id="filesUpload"></a>
# **filesUpload**
> CreateFileResponse filesUpload(xApideckMetadata, xApideckConsumerId, xApideckAppId, raw, xApideckServiceId, body)

Upload file

Upload file (max 100MB). Please use the [Upload Sessions API](#operation/uploadSessionsStart) to upload bigger files. For more information on uploads, refer to the [file upload guide](/guides/file-upload).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    CreateFileRequest xApideckMetadata = new CreateFileRequest(); // CreateFileRequest | Metadata to attach to the file
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    Boolean raw = false; // Boolean | Include raw response. Mostly used for debugging purposes
    String xApideckServiceId = "xApideckServiceId_example"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    File body = new File("/path/to/file"); // File | 
    try {
      CreateFileResponse result = apiInstance.filesUpload(xApideckMetadata, xApideckConsumerId, xApideckAppId, raw, xApideckServiceId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#filesUpload");
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
| **xApideckMetadata** | [**CreateFileRequest**](.md)| Metadata to attach to the file | |
| **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | |
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false] |
| **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] |
| **body** | **File**|  | [optional] |

### Return type

[**CreateFileResponse**](CreateFileResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Files |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **422** | Unprocessable |  -  |
| **0** | Unexpected error |  -  |

