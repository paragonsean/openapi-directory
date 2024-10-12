# TestApi

All URIs are relative to *https://api.appcenter.ms*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**testArchiveTestRun**](TestApi.md#testArchiveTestRun) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id} |  |
| [**testCreateDeviceSelection**](TestApi.md#testCreateDeviceSelection) | **POST** /v0.1/apps/{owner_name}/{app_name}/device_selection |  |
| [**testCreateDeviceSetOfOwner**](TestApi.md#testCreateDeviceSetOfOwner) | **POST** /v0.1/apps/{owner_name}/{app_name}/owner/device_sets |  |
| [**testCreateDeviceSetOfUser**](TestApi.md#testCreateDeviceSetOfUser) | **POST** /v0.1/apps/{owner_name}/{app_name}/user/device_sets |  |
| [**testCreateSubscription**](TestApi.md#testCreateSubscription) | **POST** /v0.1/apps/{owner_name}/{app_name}/subscriptions |  |
| [**testCreateTestRun**](TestApi.md#testCreateTestRun) | **POST** /v0.1/apps/{owner_name}/{app_name}/test_runs |  |
| [**testCreateTestSeries**](TestApi.md#testCreateTestSeries) | **POST** /v0.1/apps/{owner_name}/{app_name}/test_series |  |
| [**testDeleteDeviceSetOfOwner**](TestApi.md#testDeleteDeviceSetOfOwner) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/owner/device_sets/{id} |  |
| [**testDeleteDeviceSetOfUser**](TestApi.md#testDeleteDeviceSetOfUser) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/user/device_sets/{id} |  |
| [**testDeleteTestSeries**](TestApi.md#testDeleteTestSeries) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/test_series/{test_series_slug} |  |
| [**testGdprExportAccount**](TestApi.md#testGdprExportAccount) | **GET** /v0.1/account/test/export/accounts |  |
| [**testGdprExportAccounts**](TestApi.md#testGdprExportAccounts) | **GET** /v0.1/account/test/export |  |
| [**testGdprExportApp**](TestApi.md#testGdprExportApp) | **GET** /v0.1/apps/{owner_name}/{app_name}/test/export/apps |  |
| [**testGdprExportApps**](TestApi.md#testGdprExportApps) | **GET** /v0.1/apps/{owner_name}/{app_name}/test/export |  |
| [**testGdprExportFeatureFlag**](TestApi.md#testGdprExportFeatureFlag) | **GET** /v0.1/account/test/export/featureFlags |  |
| [**testGdprExportFileSetFile**](TestApi.md#testGdprExportFileSetFile) | **GET** /v0.1/apps/{owner_name}/{app_name}/test/export/fileSetFiles |  |
| [**testGdprExportHashFile**](TestApi.md#testGdprExportHashFile) | **GET** /v0.1/apps/{owner_name}/{app_name}/test/export/hashFiles |  |
| [**testGdprExportPipelineTest**](TestApi.md#testGdprExportPipelineTest) | **GET** /v0.1/apps/{owner_name}/{app_name}/test/export/pipelineTests |  |
| [**testGdprExportTestRun**](TestApi.md#testGdprExportTestRun) | **GET** /v0.1/apps/{owner_name}/{app_name}/test/export/testRuns |  |
| [**testGetAllTestRunsForSeries**](TestApi.md#testGetAllTestRunsForSeries) | **GET** /v0.1/apps/{owner_name}/{app_name}/test_series/{test_series_slug}/test_runs |  |
| [**testGetAllTestSeries**](TestApi.md#testGetAllTestSeries) | **GET** /v0.1/apps/{owner_name}/{app_name}/test_series |  |
| [**testGetDeviceConfigurations**](TestApi.md#testGetDeviceConfigurations) | **GET** /v0.1/apps/{owner_name}/{app_name}/device_configurations |  |
| [**testGetDeviceSetOfOwner**](TestApi.md#testGetDeviceSetOfOwner) | **GET** /v0.1/apps/{owner_name}/{app_name}/owner/device_sets/{id} |  |
| [**testGetDeviceSetOfUser**](TestApi.md#testGetDeviceSetOfUser) | **GET** /v0.1/apps/{owner_name}/{app_name}/user/device_sets/{id} |  |
| [**testGetSubscriptions**](TestApi.md#testGetSubscriptions) | **GET** /v0.1/apps/{owner_name}/{app_name}/subscriptions |  |
| [**testGetTestReport**](TestApi.md#testGetTestReport) | **GET** /v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}/report |  |
| [**testGetTestRun**](TestApi.md#testGetTestRun) | **GET** /v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id} |  |
| [**testGetTestRunState**](TestApi.md#testGetTestRunState) | **GET** /v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}/state |  |
| [**testGetTestRuns**](TestApi.md#testGetTestRuns) | **GET** /v0.1/apps/{owner_name}/{app_name}/test_runs |  |
| [**testListDeviceSetsOfOwner**](TestApi.md#testListDeviceSetsOfOwner) | **GET** /v0.1/apps/{owner_name}/{app_name}/owner/device_sets |  |
| [**testListDeviceSetsOfUser**](TestApi.md#testListDeviceSetsOfUser) | **GET** /v0.1/apps/{owner_name}/{app_name}/user/device_sets |  |
| [**testPatchTestSeries**](TestApi.md#testPatchTestSeries) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/test_series/{test_series_slug} |  |
| [**testStartTestRun**](TestApi.md#testStartTestRun) | **POST** /v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}/start |  |
| [**testStartUploadingFile**](TestApi.md#testStartUploadingFile) | **POST** /v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}/files |  |
| [**testStopTestRun**](TestApi.md#testStopTestRun) | **PUT** /v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}/stop |  |
| [**testUpdateDeviceSetOfOwner**](TestApi.md#testUpdateDeviceSetOfOwner) | **PUT** /v0.1/apps/{owner_name}/{app_name}/owner/device_sets/{id} |  |
| [**testUpdateDeviceSetOfUser**](TestApi.md#testUpdateDeviceSetOfUser) | **PUT** /v0.1/apps/{owner_name}/{app_name}/user/device_sets/{id} |  |
| [**testUploadHash**](TestApi.md#testUploadHash) | **POST** /v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}/hashes |  |
| [**testUploadHashesBatch**](TestApi.md#testUploadHashesBatch) | **POST** /v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}/hashes/batch |  |


<a id="testArchiveTestRun"></a>
# **testArchiveTestRun**
> TestRun testArchiveTestRun(testRunId, ownerName, appName)



Logically deletes a test run

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    UUID testRunId = UUID.randomUUID(); // UUID | The ID of the test run
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      TestRun result = apiInstance.testArchiveTestRun(testRunId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testArchiveTestRun");
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
| **testRunId** | **UUID**| The ID of the test run | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**TestRun**](TestRun.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Test run with the given ID was not found |  -  |

<a id="testCreateDeviceSelection"></a>
# **testCreateDeviceSelection**
> DeviceSelection testCreateDeviceSelection(ownerName, appName, deviceList)



Creates a short ID for a list of devices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    DeviceList deviceList = new DeviceList(); // DeviceList | 
    try {
      DeviceSelection result = apiInstance.testCreateDeviceSelection(ownerName, appName, deviceList);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testCreateDeviceSelection");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **deviceList** | [**DeviceList**](DeviceList.md)|  | |

### Return type

[**DeviceSelection**](DeviceSelection.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **400** | Invalid list of device IDs |  -  |

<a id="testCreateDeviceSetOfOwner"></a>
# **testCreateDeviceSetOfOwner**
> DeviceSet testCreateDeviceSetOfOwner(ownerName, appName, deviceSetUpdateInformation)



Creates a device set belonging to the owner

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    DeviceSetUpdateInformation deviceSetUpdateInformation = new DeviceSetUpdateInformation(); // DeviceSetUpdateInformation | 
    try {
      DeviceSet result = apiInstance.testCreateDeviceSetOfOwner(ownerName, appName, deviceSetUpdateInformation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testCreateDeviceSetOfOwner");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **deviceSetUpdateInformation** | [**DeviceSetUpdateInformation**](DeviceSetUpdateInformation.md)|  | |

### Return type

[**DeviceSet**](DeviceSet.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **400** | Invalid list of device IDs or conflicting name |  -  |

<a id="testCreateDeviceSetOfUser"></a>
# **testCreateDeviceSetOfUser**
> DeviceSet testCreateDeviceSetOfUser(ownerName, appName, deviceSetUpdateInformation)



Creates a device set belonging to the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    DeviceSetUpdateInformation deviceSetUpdateInformation = new DeviceSetUpdateInformation(); // DeviceSetUpdateInformation | 
    try {
      DeviceSet result = apiInstance.testCreateDeviceSetOfUser(ownerName, appName, deviceSetUpdateInformation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testCreateDeviceSetOfUser");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **deviceSetUpdateInformation** | [**DeviceSetUpdateInformation**](DeviceSetUpdateInformation.md)|  | |

### Return type

[**DeviceSet**](DeviceSet.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **400** | Invalid list of device IDs or conflicting name |  -  |

<a id="testCreateSubscription"></a>
# **testCreateSubscription**
> Subscription1 testCreateSubscription(ownerName, appName)



Accept a free trial subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      Subscription1 result = apiInstance.testCreateSubscription(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testCreateSubscription");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**Subscription1**](Subscription1.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |

<a id="testCreateTestRun"></a>
# **testCreateTestRun**
> testCreateTestRun(ownerName, appName)



Creates a new test run

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      apiInstance.testCreateTestRun(ownerName, appName);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testCreateTestRun");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  * Location - Link to get details about the cancel export. <br>  |

<a id="testCreateTestSeries"></a>
# **testCreateTestSeries**
> TestSeries testCreateTestSeries(ownerName, appName, nameOfTheTestSeries)



Creates new test series for an application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    NameOfTheTestSeries nameOfTheTestSeries = new NameOfTheTestSeries(); // NameOfTheTestSeries | 
    try {
      TestSeries result = apiInstance.testCreateTestSeries(ownerName, appName, nameOfTheTestSeries);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testCreateTestSeries");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **nameOfTheTestSeries** | [**NameOfTheTestSeries**](NameOfTheTestSeries.md)|  | |

### Return type

[**TestSeries**](TestSeries.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Invalid test series name |  -  |

<a id="testDeleteDeviceSetOfOwner"></a>
# **testDeleteDeviceSetOfOwner**
> testDeleteDeviceSetOfOwner(id, ownerName, appName)



Deletes a device set belonging to the owner

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | The UUID of the device set
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      apiInstance.testDeleteDeviceSetOfOwner(id, ownerName, appName);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testDeleteDeviceSetOfOwner");
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
| **id** | **UUID**| The UUID of the device set | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Device set with the given ID was not found |  -  |

<a id="testDeleteDeviceSetOfUser"></a>
# **testDeleteDeviceSetOfUser**
> testDeleteDeviceSetOfUser(id, ownerName, appName)



Deletes a device set belonging to the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | The UUID of the device set
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      apiInstance.testDeleteDeviceSetOfUser(id, ownerName, appName);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testDeleteDeviceSetOfUser");
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
| **id** | **UUID**| The UUID of the device set | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Device set with the given ID was not found |  -  |

<a id="testDeleteTestSeries"></a>
# **testDeleteTestSeries**
> testDeleteTestSeries(testSeriesSlug, ownerName, appName)



Deletes a single test series

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String testSeriesSlug = "testSeriesSlug_example"; // String | The slug of the test series
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      apiInstance.testDeleteTestSeries(testSeriesSlug, ownerName, appName);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testDeleteTestSeries");
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
| **testSeriesSlug** | **String**| The slug of the test series | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Test series was successfully removed |  -  |
| **404** | The test series was not found |  -  |

<a id="testGdprExportAccount"></a>
# **testGdprExportAccount**
> TestGdprExportAccount200Response testGdprExportAccount()



Lists account data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    try {
      TestGdprExportAccount200Response result = apiInstance.testGdprExportAccount();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGdprExportAccount");
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

[**TestGdprExportAccount200Response**](TestGdprExportAccount200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testGdprExportAccounts"></a>
# **testGdprExportAccounts**
> TestGdprExportAccounts200Response testGdprExportAccounts()



Lists all the endpoints available for Test accounts data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    try {
      TestGdprExportAccounts200Response result = apiInstance.testGdprExportAccounts();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGdprExportAccounts");
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

[**TestGdprExportAccounts200Response**](TestGdprExportAccounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testGdprExportApp"></a>
# **testGdprExportApp**
> TestGdprExportApp200Response testGdprExportApp(ownerName, appName)



Lists app data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      TestGdprExportApp200Response result = apiInstance.testGdprExportApp(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGdprExportApp");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**TestGdprExportApp200Response**](TestGdprExportApp200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testGdprExportApps"></a>
# **testGdprExportApps**
> TestGdprExportAccounts200Response testGdprExportApps(ownerName, appName)



Lists all the endpoints available for Test apps data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      TestGdprExportAccounts200Response result = apiInstance.testGdprExportApps(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGdprExportApps");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**TestGdprExportAccounts200Response**](TestGdprExportAccounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testGdprExportFeatureFlag"></a>
# **testGdprExportFeatureFlag**
> TestGdprExportFeatureFlag200Response testGdprExportFeatureFlag()



Lists feature flag data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    try {
      TestGdprExportFeatureFlag200Response result = apiInstance.testGdprExportFeatureFlag();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGdprExportFeatureFlag");
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

[**TestGdprExportFeatureFlag200Response**](TestGdprExportFeatureFlag200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testGdprExportFileSetFile"></a>
# **testGdprExportFileSetFile**
> TestGdprExportFileSetFile200Response testGdprExportFileSetFile(ownerName, appName)



Lists file set file data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      TestGdprExportFileSetFile200Response result = apiInstance.testGdprExportFileSetFile(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGdprExportFileSetFile");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**TestGdprExportFileSetFile200Response**](TestGdprExportFileSetFile200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testGdprExportHashFile"></a>
# **testGdprExportHashFile**
> TestGdprExportHashFile200Response testGdprExportHashFile(ownerName, appName)



Lists hash file data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      TestGdprExportHashFile200Response result = apiInstance.testGdprExportHashFile(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGdprExportHashFile");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**TestGdprExportHashFile200Response**](TestGdprExportHashFile200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testGdprExportPipelineTest"></a>
# **testGdprExportPipelineTest**
> TestGdprExportPipelineTest200Response testGdprExportPipelineTest(ownerName, appName)



Lists pipeline test data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      TestGdprExportPipelineTest200Response result = apiInstance.testGdprExportPipelineTest(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGdprExportPipelineTest");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**TestGdprExportPipelineTest200Response**](TestGdprExportPipelineTest200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testGdprExportTestRun"></a>
# **testGdprExportTestRun**
> TestGdprExportTestRun200Response testGdprExportTestRun(ownerName, appName)



Lists test run data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      TestGdprExportTestRun200Response result = apiInstance.testGdprExportTestRun(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGdprExportTestRun");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**TestGdprExportTestRun200Response**](TestGdprExportTestRun200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testGetAllTestRunsForSeries"></a>
# **testGetAllTestRunsForSeries**
> List&lt;TestRun&gt; testGetAllTestRunsForSeries(testSeriesSlug, ownerName, appName)



Returns list of all test runs for a given test series

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String testSeriesSlug = "testSeriesSlug_example"; // String | The slug of the test series
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<TestRun> result = apiInstance.testGetAllTestRunsForSeries(testSeriesSlug, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGetAllTestRunsForSeries");
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
| **testSeriesSlug** | **String**| The slug of the test series | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;TestRun&gt;**](TestRun.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testGetAllTestSeries"></a>
# **testGetAllTestSeries**
> List&lt;TestSeries&gt; testGetAllTestSeries(ownerName, appName, query)



Returns list of all test series for an application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String query = "query_example"; // String | A query string to filter test series
    try {
      List<TestSeries> result = apiInstance.testGetAllTestSeries(ownerName, appName, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGetAllTestSeries");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **query** | **String**| A query string to filter test series | [optional] |

### Return type

[**List&lt;TestSeries&gt;**](TestSeries.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testGetDeviceConfigurations"></a>
# **testGetDeviceConfigurations**
> List&lt;TestGetDeviceConfigurations200ResponseInner&gt; testGetDeviceConfigurations(ownerName, appName, appUploadId)



Returns a list of available devices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    UUID appUploadId = UUID.randomUUID(); // UUID | The ID of the test run
    try {
      List<TestGetDeviceConfigurations200ResponseInner> result = apiInstance.testGetDeviceConfigurations(ownerName, appName, appUploadId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGetDeviceConfigurations");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **appUploadId** | **UUID**| The ID of the test run | [optional] |

### Return type

[**List&lt;TestGetDeviceConfigurations200ResponseInner&gt;**](TestGetDeviceConfigurations200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testGetDeviceSetOfOwner"></a>
# **testGetDeviceSetOfOwner**
> DeviceSet testGetDeviceSetOfOwner(id, ownerName, appName)



Gets a device set belonging to the owner

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | The UUID of the device set
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      DeviceSet result = apiInstance.testGetDeviceSetOfOwner(id, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGetDeviceSetOfOwner");
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
| **id** | **UUID**| The UUID of the device set | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**DeviceSet**](DeviceSet.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Device set with the given ID was not found |  -  |

<a id="testGetDeviceSetOfUser"></a>
# **testGetDeviceSetOfUser**
> DeviceSet testGetDeviceSetOfUser(id, ownerName, appName)



Gets a device set belonging to the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | The UUID of the device set
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      DeviceSet result = apiInstance.testGetDeviceSetOfUser(id, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGetDeviceSetOfUser");
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
| **id** | **UUID**| The UUID of the device set | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**DeviceSet**](DeviceSet.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Device set with the given ID was not found |  -  |

<a id="testGetSubscriptions"></a>
# **testGetSubscriptions**
> Subscription1 testGetSubscriptions(ownerName, appName)



Get information about the currently active subscriptions, if any

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      Subscription1 result = apiInstance.testGetSubscriptions(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGetSubscriptions");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**Subscription1**](Subscription1.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testGetTestReport"></a>
# **testGetTestReport**
> TestGetTestReport200Response testGetTestReport(testRunId, ownerName, appName)



Returns a single test report

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    UUID testRunId = UUID.randomUUID(); // UUID | The ID of the test run
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      TestGetTestReport200Response result = apiInstance.testGetTestReport(testRunId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGetTestReport");
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
| **testRunId** | **UUID**| The ID of the test run | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**TestGetTestReport200Response**](TestGetTestReport200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testGetTestRun"></a>
# **testGetTestRun**
> TestRun testGetTestRun(testRunId, ownerName, appName)



Returns a single test runs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    UUID testRunId = UUID.randomUUID(); // UUID | The ID of the test run
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      TestRun result = apiInstance.testGetTestRun(testRunId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGetTestRun");
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
| **testRunId** | **UUID**| The ID of the test run | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**TestRun**](TestRun.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testGetTestRunState"></a>
# **testGetTestRunState**
> TestRunState testGetTestRunState(testRunId, ownerName, appName)



Gets state of the test run

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String testRunId = "testRunId_example"; // String | The ID of the test run
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      TestRunState result = apiInstance.testGetTestRunState(testRunId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGetTestRunState");
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
| **testRunId** | **String**| The ID of the test run | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**TestRunState**](TestRunState.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testGetTestRuns"></a>
# **testGetTestRuns**
> List&lt;TestRun&gt; testGetTestRuns(ownerName, appName)



Returns a list of test runs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<TestRun> result = apiInstance.testGetTestRuns(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGetTestRuns");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;TestRun&gt;**](TestRun.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testListDeviceSetsOfOwner"></a>
# **testListDeviceSetsOfOwner**
> List&lt;DeviceSet&gt; testListDeviceSetsOfOwner(ownerName, appName)



Lists device sets belonging to the owner

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<DeviceSet> result = apiInstance.testListDeviceSetsOfOwner(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testListDeviceSetsOfOwner");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;DeviceSet&gt;**](DeviceSet.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testListDeviceSetsOfUser"></a>
# **testListDeviceSetsOfUser**
> List&lt;DeviceSet&gt; testListDeviceSetsOfUser(ownerName, appName)



Lists device sets belonging to the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<DeviceSet> result = apiInstance.testListDeviceSetsOfUser(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testListDeviceSetsOfUser");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;DeviceSet&gt;**](DeviceSet.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testPatchTestSeries"></a>
# **testPatchTestSeries**
> TestSeries testPatchTestSeries(testSeriesSlug, ownerName, appName, nameOfTheTestSeries)



Updates name and slug of a test series

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String testSeriesSlug = "testSeriesSlug_example"; // String | The slug of the test series
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    NameOfTheTestSeries nameOfTheTestSeries = new NameOfTheTestSeries(); // NameOfTheTestSeries | 
    try {
      TestSeries result = apiInstance.testPatchTestSeries(testSeriesSlug, ownerName, appName, nameOfTheTestSeries);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testPatchTestSeries");
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
| **testSeriesSlug** | **String**| The slug of the test series | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **nameOfTheTestSeries** | [**NameOfTheTestSeries**](NameOfTheTestSeries.md)|  | |

### Return type

[**TestSeries**](TestSeries.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Test series was successfully patched |  -  |
| **400** | The new test series name is incorrect |  -  |
| **404** | Test series with the given slug name was not found |  -  |

<a id="testStartTestRun"></a>
# **testStartTestRun**
> TestCloudTestRunStartResult testStartTestRun(testRunId, ownerName, appName, testCloudStartTestRunOptions)



Starts test run

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String testRunId = "testRunId_example"; // String | The ID of the test run
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    TestCloudStartTestRunOptions testCloudStartTestRunOptions = new TestCloudStartTestRunOptions(); // TestCloudStartTestRunOptions | Option required to start the test run
    try {
      TestCloudTestRunStartResult result = apiInstance.testStartTestRun(testRunId, ownerName, appName, testCloudStartTestRunOptions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testStartTestRun");
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
| **testRunId** | **String**| The ID of the test run | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **testCloudStartTestRunOptions** | [**TestCloudStartTestRunOptions**](TestCloudStartTestRunOptions.md)| Option required to start the test run | |

### Return type

[**TestCloudTestRunStartResult**](TestCloudTestRunStartResult.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testStartUploadingFile"></a>
# **testStartUploadingFile**
> testStartUploadingFile(testRunId, ownerName, appName)



Uploads file for a test run

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String testRunId = "testRunId_example"; // String | The ID of the test run
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      apiInstance.testStartUploadingFile(testRunId, ownerName, appName);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testStartUploadingFile");
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
| **testRunId** | **String**| The ID of the test run | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File was created and can be uploaded |  * Location - Link to get details about the cancel export. <br>  |
| **400** | Bad request |  -  |

<a id="testStopTestRun"></a>
# **testStopTestRun**
> TestRun testStopTestRun(testRunId, ownerName, appName)



Stop a test run execution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String testRunId = "testRunId_example"; // String | The ID of the test run to be stopped
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      TestRun result = apiInstance.testStopTestRun(testRunId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testStopTestRun");
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
| **testRunId** | **String**| The ID of the test run to be stopped | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**TestRun**](TestRun.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Test run with the given ID was not found |  -  |

<a id="testUpdateDeviceSetOfOwner"></a>
# **testUpdateDeviceSetOfOwner**
> DeviceSet testUpdateDeviceSetOfOwner(id, ownerName, appName, deviceSetUpdateInformation)



Updates a device set belonging to the owner

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | The UUID of the device set
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    DeviceSetUpdateInformation deviceSetUpdateInformation = new DeviceSetUpdateInformation(); // DeviceSetUpdateInformation | 
    try {
      DeviceSet result = apiInstance.testUpdateDeviceSetOfOwner(id, ownerName, appName, deviceSetUpdateInformation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testUpdateDeviceSetOfOwner");
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
| **id** | **UUID**| The UUID of the device set | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **deviceSetUpdateInformation** | [**DeviceSetUpdateInformation**](DeviceSetUpdateInformation.md)|  | |

### Return type

[**DeviceSet**](DeviceSet.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Invalid list of device IDs or conflicting name |  -  |
| **404** | Device set with the given ID was not found |  -  |

<a id="testUpdateDeviceSetOfUser"></a>
# **testUpdateDeviceSetOfUser**
> DeviceSet testUpdateDeviceSetOfUser(id, ownerName, appName, deviceSetUpdateInformation)



Updates a device set belonging to the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | The UUID of the device set
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    DeviceSetUpdateInformation deviceSetUpdateInformation = new DeviceSetUpdateInformation(); // DeviceSetUpdateInformation | 
    try {
      DeviceSet result = apiInstance.testUpdateDeviceSetOfUser(id, ownerName, appName, deviceSetUpdateInformation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testUpdateDeviceSetOfUser");
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
| **id** | **UUID**| The UUID of the device set | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **deviceSetUpdateInformation** | [**DeviceSetUpdateInformation**](DeviceSetUpdateInformation.md)|  | |

### Return type

[**DeviceSet**](DeviceSet.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Invalid list of device IDs or conflicting name |  -  |
| **404** | Device set with the given ID was not found |  -  |

<a id="testUploadHash"></a>
# **testUploadHash**
> testUploadHash(testRunId, ownerName, appName, testCloudFileHash)



Adds file with the given hash to a test run

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String testRunId = "testRunId_example"; // String | The ID of the test run
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    TestCloudFileHash testCloudFileHash = new TestCloudFileHash(); // TestCloudFileHash | File hash information
    try {
      apiInstance.testUploadHash(testRunId, ownerName, appName, testCloudFileHash);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testUploadHash");
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
| **testRunId** | **String**| The ID of the test run | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **testCloudFileHash** | [**TestCloudFileHash**](TestCloudFileHash.md)| File hash information | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **401** | Byte range verification required for given SHA256 hash |  * X-Challenge-Bytes - Byte range required to authenticate the request <br>  |
| **412** | File with given SHA256 hash doesn&#39;t exist and must be uploaded |  -  |

<a id="testUploadHashesBatch"></a>
# **testUploadHashesBatch**
> List&lt;TestCloudFileHashResponse&gt; testUploadHashesBatch(testRunId, ownerName, appName, testCloudFileHash1)



Adds file with the given hash to a test run

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    String testRunId = "testRunId_example"; // String | The ID of the test run
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    List<TestCloudFileHash1> testCloudFileHash1 = Arrays.asList(); // List<TestCloudFileHash1> | File hash information
    try {
      List<TestCloudFileHashResponse> result = apiInstance.testUploadHashesBatch(testRunId, ownerName, appName, testCloudFileHash1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testUploadHashesBatch");
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
| **testRunId** | **String**| The ID of the test run | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **testCloudFileHash1** | [**List&lt;TestCloudFileHash1&gt;**](TestCloudFileHash1.md)| File hash information | |

### Return type

[**List&lt;TestCloudFileHashResponse&gt;**](TestCloudFileHashResponse.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

