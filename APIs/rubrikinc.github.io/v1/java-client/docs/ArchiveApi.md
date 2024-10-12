# ArchiveApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**disableArchivalLocation**](ArchiveApi.md#disableArchivalLocation) | **POST** /archive/location/{id}/owner/disable | Disable location for archival and modification operations |
| [**enableArchivalLocation**](ArchiveApi.md#enableArchivalLocation) | **POST** /archive/location/{id}/owner/enable | Enable archival location for archival and modification operations |
| [**getAwsAccountId**](ArchiveApi.md#getAwsAccountId) | **GET** /archive/aws/s3/{id}/account_id | Get the AWS account ID of an AWS S3 archival location |
| [**refreshArchivalLocationDataSources**](ArchiveApi.md#refreshArchivalLocationDataSources) | **POST** /archive/location/{location_id}/reader/refresh/data_sources | Refresh archive information for a list of data sources |


<a id="disableArchivalLocation"></a>
# **disableArchivalLocation**
> disableArchivalLocation(id)

Disable location for archival and modification operations

Disables archiving and any changes to the data for the specified archival location. This operation disables snapshot upload, snapshot expiration, consolidation, and garbage collection operations on the archival location. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArchiveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ArchiveApi apiInstance = new ArchiveApi(defaultClient);
    String id = "id_example"; // String | ID assigned to an archival location object.
    try {
      apiInstance.disableArchivalLocation(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArchiveApi#disableArchivalLocation");
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
| **id** | **String**| ID assigned to an archival location object. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Archival location successfully disabled.  |  -  |

<a id="enableArchivalLocation"></a>
# **enableArchivalLocation**
> enableArchivalLocation(id)

Enable archival location for archival and modification operations

Enable archiving and other operations that were previously disabled on the specified archival location. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArchiveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ArchiveApi apiInstance = new ArchiveApi(defaultClient);
    String id = "id_example"; // String | ID assigned to an archival location object.
    try {
      apiInstance.enableArchivalLocation(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArchiveApi#enableArchivalLocation");
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
| **id** | **String**| ID assigned to an archival location object. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Archival location successfully enabled.  |  -  |

<a id="getAwsAccountId"></a>
# **getAwsAccountId**
> StringResponse getAwsAccountId(id)

Get the AWS account ID of an AWS S3 archival location

Get the AWS account ID of an AWS S3 archival location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArchiveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ArchiveApi apiInstance = new ArchiveApi(defaultClient);
    String id = "id_example"; // String | ID of an AWS archival location that uses the S3 protocol.
    try {
      StringResponse result = apiInstance.getAwsAccountId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArchiveApi#getAwsAccountId");
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
| **id** | **String**| ID of an AWS archival location that uses the S3 protocol. | |

### Return type

[**StringResponse**](StringResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account ID of the AWS account of the archival location. |  -  |

<a id="refreshArchivalLocationDataSources"></a>
# **refreshArchivalLocationDataSources**
> AsyncRequestStatus refreshArchivalLocationDataSources(locationId, readerRefreshDataSourcesRequest)

Refresh archive information for a list of data sources

Update the current Rubrik CDM cluster with information about the changes made to a list of data sources in an archival location by the Rubrik CDM cluster that owns the archival location. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArchiveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ArchiveApi apiInstance = new ArchiveApi(defaultClient);
    String locationId = "locationId_example"; // String | ID assigned to an archival location object.
    ReaderRefreshDataSourcesRequest readerRefreshDataSourcesRequest = new ReaderRefreshDataSourcesRequest(); // ReaderRefreshDataSourcesRequest | A set of local and archival IDs for data sources to refresh. For a data source, either a local or archival data source ID should be specified. The operation will fail if `none` is specified. 
    try {
      AsyncRequestStatus result = apiInstance.refreshArchivalLocationDataSources(locationId, readerRefreshDataSourcesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArchiveApi#refreshArchivalLocationDataSources");
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
| **locationId** | **String**| ID assigned to an archival location object. | |
| **readerRefreshDataSourcesRequest** | [**ReaderRefreshDataSourcesRequest**](ReaderRefreshDataSourcesRequest.md)| A set of local and archival IDs for data sources to refresh. For a data source, either a local or archival data source ID should be specified. The operation will fail if &#x60;none&#x60; is specified.  | |

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The request ID for an asynchronous request to refresh archival information.  |  -  |

