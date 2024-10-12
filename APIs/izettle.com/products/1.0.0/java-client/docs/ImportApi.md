# ImportApi

All URIs are relative to *https://products.izettle.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLatestImportStatus**](ImportApi.md#getLatestImportStatus) | **GET** /organizations/{organizationUuid}/import/status | Get status for latest import |
| [**getStatusByUuid**](ImportApi.md#getStatusByUuid) | **GET** /organizations/{organizationUuid}/import/status/{importUuid} | Get status for an import |
| [**importLibraryV2**](ImportApi.md#importLibraryV2) | **POST** /organizations/{organizationUuid}/import/v2 | Import library items |


<a id="getLatestImportStatus"></a>
# **getLatestImportStatus**
> ImportResponse getLatestImportStatus(organizationUuid)

Get status for latest import

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    ImportApi apiInstance = new ImportApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    try {
      ImportResponse result = apiInstance.getLatestImportStatus(organizationUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportApi#getLatestImportStatus");
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

[**ImportResponse**](ImportResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Import status |  -  |
| **404** | Organization or import not found |  -  |

<a id="getStatusByUuid"></a>
# **getStatusByUuid**
> ImportResponse getStatusByUuid(organizationUuid, importUuid)

Get status for an import

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    ImportApi apiInstance = new ImportApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    UUID importUuid = UUID.randomUUID(); // UUID | 
    try {
      ImportResponse result = apiInstance.getStatusByUuid(organizationUuid, importUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportApi#getStatusByUuid");
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
| **importUuid** | **UUID**|  | |

### Return type

[**ImportResponse**](ImportResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Import status |  -  |
| **404** | Organization or import not found |  -  |

<a id="importLibraryV2"></a>
# **importLibraryV2**
> ImportResponse importLibraryV2(organizationUuid, bulkImportRequest)

Import library items

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    ImportApi apiInstance = new ImportApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    BulkImportRequest bulkImportRequest = new BulkImportRequest(); // BulkImportRequest | 
    try {
      ImportResponse result = apiInstance.importLibraryV2(organizationUuid, bulkImportRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportApi#importLibraryV2");
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
| **bulkImportRequest** | [**BulkImportRequest**](BulkImportRequest.md)|  | |

### Return type

[**ImportResponse**](ImportResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Import status |  -  |
| **400** | Invalid request body |  -  |

