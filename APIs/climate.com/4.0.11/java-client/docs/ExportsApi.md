# ExportsApi

All URIs are relative to *https://platform.climate.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchExportContentsById**](ExportsApi.md#fetchExportContentsById) | **GET** /v4/exports/{exportId}/contents | Retrieve the binary contents of a processed export request. |
| [**fetchExportStatusById**](ExportsApi.md#fetchExportStatusById) | **GET** /v4/exports/{exportId}/status | Retrieve the status of an Export. |
| [**postExport**](ExportsApi.md#postExport) | **POST** /v4/exports | Initiate a new export request. |


<a id="fetchExportContentsById"></a>
# **fetchExportContentsById**
> fetchExportContentsById(accept, exportId, range)

Retrieve the binary contents of a processed export request.

Downloads larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) in size must be downloaded in chunks no larger than &#x60;5MiB&#x60; (&#x60;5242880 bytes&#x60;) and no smaller than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;). The last chunk could be less than &#x60;1MiB&#x60; (&#x60;1048576 bytes&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    ExportsApi apiInstance = new ExportsApi(defaultClient);
    String accept = "accept_example"; // String | Must be either \\*_/_* or application/octet-stream,application/json
    UUID exportId = UUID.randomUUID(); // UUID | Unique identifier of an Export.
    String range = "range_example"; // String | Byte range `bytes=start-end` (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes=0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB.
    try {
      apiInstance.fetchExportContentsById(accept, exportId, range);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportsApi#fetchExportContentsById");
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
| **accept** | **String**| Must be either \\*_/_* or application/octet-stream,application/json | |
| **exportId** | **UUID**| Unique identifier of an Export. | |
| **range** | **String**| Byte range &#x60;bytes&#x3D;start-end&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes&#x3D;0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **206** | Partial Result |  * Content-Range - Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes). <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **304** | Not Modified |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **401** | Unauthorized |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **403** | Forbidden |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **404** | Not Found |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **409** | Conflict (Report generation is still in progress) |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **410** | Gone (Report is expired) |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **416** | Range Not Satisfiable |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **429** | Too Many Requests |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **500** | Internal Server Error |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **503** | Server Busy |  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

<a id="fetchExportStatusById"></a>
# **fetchExportStatusById**
> ExportStatus fetchExportStatusById(exportId)

Retrieve the status of an Export.

Check the status of an **Export** by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    ExportsApi apiInstance = new ExportsApi(defaultClient);
    UUID exportId = UUID.randomUUID(); // UUID | Unique identifier of an Export.
    try {
      ExportStatus result = apiInstance.fetchExportStatusById(exportId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportsApi#fetchExportStatusById");
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
| **exportId** | **UUID**| Unique identifier of an Export. | |

### Return type

[**ExportStatus**](ExportStatus.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **401** | Unauthorized |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **403** | Forbidden |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **404** | Not Found |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **429** | Too Many Requests |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **500** | Internal Server Error |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **503** | Server Busy |  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

<a id="postExport"></a>
# **postExport**
> CreatedExport postExport(export)

Initiate a new export request.

Step one in requesting a data product. The method will return an **Export** ID which the caller will use in subsequent &#x60;GET&#x60; requests. The following &#x60;contentTypes&#x60; may be requested:   * __application/vnd.climate.acrsi.geojson__ (Beta)      Exports the planting activities accessible by the authenticated user and optionally filtered by resource owner      as a [GeoJSON Feature Collection](https://tools.ietf.org/html/rfc7946#page-12).       The export request definition must contain the following properties:        * plantingStartDate        * plantingEndDate        * resourceOwnerId       Requires &#x60;exports:read&#x60; and &#x60;plantingActivitySummary:read&#x60; scope.      * __application/vnd.climate.harvest.geojson__      Exports the harvesting activities accessible by the authenticated user and optionally filtered by resource owner      as a [GeoJSON Feature Collection](https://tools.ietf.org/html/rfc7946#page-12).       The export request definition must contain the following properties:        * harvestStartDate        * harvestEndDate        * resourceOwnerId       Requires &#x60;exports:read&#x60; and &#x60;plantingActivitySummary:read&#x60; scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    ExportsApi apiInstance = new ExportsApi(defaultClient);
    Export export = new Export(); // Export | 
    try {
      CreatedExport result = apiInstance.postExport(export);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportsApi#postExport");
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
| **export** | [**Export**](Export.md)|  | [optional] |

### Return type

[**CreatedExport**](CreatedExport.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **401** | Unauthorized |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **403** | Forbidden |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **429** | Too Many Requests |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **500** | Internal Server Error |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **503** | Server Busy |  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

