# MaintenanceModeApi

All URIs are relative to *https://api.victorops.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPublicV1MaintenancemodeGet**](MaintenanceModeApi.md#apiPublicV1MaintenancemodeGet) | **GET** /api-public/v1/maintenancemode | Get an organization&#39;s current maintenance mode state |
| [**apiPublicV1MaintenancemodeMaintenancemodeidEndPut**](MaintenanceModeApi.md#apiPublicV1MaintenancemodeMaintenancemodeidEndPut) | **PUT** /api-public/v1/maintenancemode/{maintenancemodeid}/end | End maintenance mode for routing keys |
| [**apiPublicV1MaintenancemodeStartPost**](MaintenanceModeApi.md#apiPublicV1MaintenancemodeStartPost) | **POST** /api-public/v1/maintenancemode/start | Start maintenance mode for routing keys |


<a id="apiPublicV1MaintenancemodeGet"></a>
# **apiPublicV1MaintenancemodeGet**
> MaintenanceModeState apiPublicV1MaintenancemodeGet(xVOApiId, xVOApiKey)

Get an organization&#39;s current maintenance mode state

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MaintenanceModeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    MaintenanceModeApi apiInstance = new MaintenanceModeApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    try {
      MaintenanceModeState result = apiInstance.apiPublicV1MaintenancemodeGet(xVOApiId, xVOApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MaintenanceModeApi#apiPublicV1MaintenancemodeGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |

### Return type

[**MaintenanceModeState**](MaintenanceModeState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | maintenance mode state |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1MaintenancemodeMaintenancemodeidEndPut"></a>
# **apiPublicV1MaintenancemodeMaintenancemodeidEndPut**
> MaintenanceModeState apiPublicV1MaintenancemodeMaintenancemodeidEndPut(xVOApiId, xVOApiKey, maintenancemodeid)

End maintenance mode for routing keys

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MaintenanceModeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    MaintenanceModeApi apiInstance = new MaintenanceModeApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String maintenancemodeid = "maintenancemodeid_example"; // String | The id of the maintenance mode found in the active maintenance mode object
    try {
      MaintenanceModeState result = apiInstance.apiPublicV1MaintenancemodeMaintenancemodeidEndPut(xVOApiId, xVOApiKey, maintenancemodeid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MaintenanceModeApi#apiPublicV1MaintenancemodeMaintenancemodeidEndPut");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **maintenancemodeid** | **String**| The id of the maintenance mode found in the active maintenance mode object | |

### Return type

[**MaintenanceModeState**](MaintenanceModeState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | maintenance mode state |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1MaintenancemodeStartPost"></a>
# **apiPublicV1MaintenancemodeStartPost**
> MaintenanceModeState apiPublicV1MaintenancemodeStartPost(xVOApiId, xVOApiKey, body)

Start maintenance mode for routing keys

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MaintenanceModeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    MaintenanceModeApi apiInstance = new MaintenanceModeApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    ApiPublicV1MaintenancemodeStartPostRequest body = new ApiPublicV1MaintenancemodeStartPostRequest(); // ApiPublicV1MaintenancemodeStartPostRequest | the definition of the maintenance mode you want to start
    try {
      MaintenanceModeState result = apiInstance.apiPublicV1MaintenancemodeStartPost(xVOApiId, xVOApiKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MaintenanceModeApi#apiPublicV1MaintenancemodeStartPost");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **body** | [**ApiPublicV1MaintenancemodeStartPostRequest**](ApiPublicV1MaintenancemodeStartPostRequest.md)| the definition of the maintenance mode you want to start | |

### Return type

[**MaintenanceModeState**](MaintenanceModeState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | maintenance mode state |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **409** | You have an active global maintanance mode and are attempting to start a second. You may only have a single Global maintenance mode at a time |  -  |
| **420** | You have reached the limit of allowed active maintenance modes |  -  |
| **500** | Internal Server Error |  -  |

