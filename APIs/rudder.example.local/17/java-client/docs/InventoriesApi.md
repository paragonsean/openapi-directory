# InventoriesApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fileWatcherRestart**](InventoriesApi.md#fileWatcherRestart) | **POST** /inventories/watcher/restart | Restart inventory watcher |
| [**fileWatcherStart**](InventoriesApi.md#fileWatcherStart) | **POST** /inventories/watcher/start | Start inventory watcher |
| [**fileWatcherStop**](InventoriesApi.md#fileWatcherStop) | **POST** /inventories/watcher/stop | Stop inventory watcher |
| [**queueInformation**](InventoriesApi.md#queueInformation) | **GET** /inventories/info | Get information about inventory processing queue |
| [**uploadInventory**](InventoriesApi.md#uploadInventory) | **POST** /inventories/upload | Upload an inventory for processing |


<a id="fileWatcherRestart"></a>
# **fileWatcherRestart**
> FileWatcherRestart200Response fileWatcherRestart()

Restart inventory watcher

Restart the inventory watcher if necessary

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    InventoriesApi apiInstance = new InventoriesApi(defaultClient);
    try {
      FileWatcherRestart200Response result = apiInstance.fileWatcherRestart();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoriesApi#fileWatcherRestart");
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

[**FileWatcherRestart200Response**](FileWatcherRestart200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Started |  -  |

<a id="fileWatcherStart"></a>
# **fileWatcherStart**
> FileWatcherStart200Response fileWatcherStart()

Start inventory watcher

Start the inventory watcher if necessary

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    InventoriesApi apiInstance = new InventoriesApi(defaultClient);
    try {
      FileWatcherStart200Response result = apiInstance.fileWatcherStart();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoriesApi#fileWatcherStart");
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

[**FileWatcherStart200Response**](FileWatcherStart200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Started |  -  |

<a id="fileWatcherStop"></a>
# **fileWatcherStop**
> FileWatcherStop200Response fileWatcherStop()

Stop inventory watcher

Stop the inventory watcher if necessary

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    InventoriesApi apiInstance = new InventoriesApi(defaultClient);
    try {
      FileWatcherStop200Response result = apiInstance.fileWatcherStop();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoriesApi#fileWatcherStop");
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

[**FileWatcherStop200Response**](FileWatcherStop200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stopped |  -  |

<a id="queueInformation"></a>
# **queueInformation**
> QueueInformation200Response queueInformation()

Get information about inventory processing queue

Provide information about the current state of the inventory processor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    InventoriesApi apiInstance = new InventoriesApi(defaultClient);
    try {
      QueueInformation200Response result = apiInstance.queueInformation();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoriesApi#queueInformation");
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

[**QueueInformation200Response**](QueueInformation200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Inventories information |  -  |

<a id="uploadInventory"></a>
# **uploadInventory**
> UploadInventory200Response uploadInventory(_file, signature)

Upload an inventory for processing

Upload an inventory to the web application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    InventoriesApi apiInstance = new InventoriesApi(defaultClient);
    File _file = new File("/path/to/file"); // File | The inventory file. The original file name is used to check extension, that should be .xml[.gz] or .ocs[.gz]
    File signature = new File("/path/to/file"); // File | The signature file. The original file name is used to check extension, that should be ${originalInventoryFileName}.sign[.gz]
    try {
      UploadInventory200Response result = apiInstance.uploadInventory(_file, signature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoriesApi#uploadInventory");
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
| **_file** | **File**| The inventory file. The original file name is used to check extension, that should be .xml[.gz] or .ocs[.gz] | [optional] |
| **signature** | **File**| The signature file. The original file name is used to check extension, that should be ${originalInventoryFileName}.sign[.gz] | [optional] |

### Return type

[**UploadInventory200Response**](UploadInventory200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Inventory uploaded |  -  |

