# ScriptsApi

All URIs are relative to *http://config2.gamesparks.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**exportZipUsingGET**](ScriptsApi.md#exportZipUsingGET) | **GET** /restv2/game/{apiKey}/admin/scripts/export | exportZip |
| [**getScriptDifferencesUsingGET**](ScriptsApi.md#getScriptDifferencesUsingGET) | **GET** /restv2/game/{apiKey}/admin/scripts/differences/{snapshotId1}/{snapshotId2} | getScriptDifferences |
| [**getScriptVersionsUsingGET**](ScriptsApi.md#getScriptVersionsUsingGET) | **GET** /restv2/game/{apiKey}/admin/scripts/versions/{page} | getScriptVersions |
| [**getScriptVersionsUsingGET1**](ScriptsApi.md#getScriptVersionsUsingGET1) | **GET** /restv2/game/{apiKey}/admin/scripts/versions | getScriptVersions |
| [**importAcceptUsingPOST**](ScriptsApi.md#importAcceptUsingPOST) | **POST** /restv2/game/{apiKey}/admin/scripts/import/accept | importAccept |
| [**importZipUsingPOST**](ScriptsApi.md#importZipUsingPOST) | **POST** /restv2/game/{apiKey}/admin/scripts/import/preview | importZip |


<a id="exportZipUsingGET"></a>
# **exportZipUsingGET**
> exportZipUsingGET(apiKey)

exportZip

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ScriptsApi apiInstance = new ScriptsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    try {
      apiInstance.exportZipUsingGET(apiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptsApi#exportZipUsingGET");
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
| **apiKey** | **String**| apiKey | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="getScriptDifferencesUsingGET"></a>
# **getScriptDifferencesUsingGET**
> ScriptsDifferenceListModel getScriptDifferencesUsingGET(apiKey, snapshotId1, snapshotId2)

getScriptDifferences

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ScriptsApi apiInstance = new ScriptsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String snapshotId1 = "snapshotId1_example"; // String | snapshotId1
    String snapshotId2 = "snapshotId2_example"; // String | snapshotId2
    try {
      ScriptsDifferenceListModel result = apiInstance.getScriptDifferencesUsingGET(apiKey, snapshotId1, snapshotId2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptsApi#getScriptDifferencesUsingGET");
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
| **apiKey** | **String**| apiKey | |
| **snapshotId1** | **String**| snapshotId1 | |
| **snapshotId2** | **String**| snapshotId2 | |

### Return type

[**ScriptsDifferenceListModel**](ScriptsDifferenceListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="getScriptVersionsUsingGET"></a>
# **getScriptVersionsUsingGET**
> SnapshotScriptVersionListModel getScriptVersionsUsingGET(apiKey, page, pageSize)

getScriptVersions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ScriptsApi apiInstance = new ScriptsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    Integer page = 56; // Integer | page
    Integer pageSize = 100; // Integer | pageSize
    try {
      SnapshotScriptVersionListModel result = apiInstance.getScriptVersionsUsingGET(apiKey, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptsApi#getScriptVersionsUsingGET");
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
| **apiKey** | **String**| apiKey | |
| **page** | **Integer**| page | |
| **pageSize** | **Integer**| pageSize | [optional] [default to 100] |

### Return type

[**SnapshotScriptVersionListModel**](SnapshotScriptVersionListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="getScriptVersionsUsingGET1"></a>
# **getScriptVersionsUsingGET1**
> SnapshotScriptVersionListModel getScriptVersionsUsingGET1(apiKey, pageSize)

getScriptVersions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ScriptsApi apiInstance = new ScriptsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    Integer pageSize = 100; // Integer | pageSize
    try {
      SnapshotScriptVersionListModel result = apiInstance.getScriptVersionsUsingGET1(apiKey, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptsApi#getScriptVersionsUsingGET1");
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
| **apiKey** | **String**| apiKey | |
| **pageSize** | **Integer**| pageSize | [optional] [default to 100] |

### Return type

[**SnapshotScriptVersionListModel**](SnapshotScriptVersionListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="importAcceptUsingPOST"></a>
# **importAcceptUsingPOST**
> MessageModel importAcceptUsingPOST(apiKey, body, _file)

importAccept

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ScriptsApi apiInstance = new ScriptsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String body = "body_example"; // String | body
    File _file = new File("/path/to/file"); // File | file
    try {
      MessageModel result = apiInstance.importAcceptUsingPOST(apiKey, body, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptsApi#importAcceptUsingPOST");
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
| **apiKey** | **String**| apiKey | |
| **body** | **String**| body | |
| **_file** | **File**| file | |

### Return type

[**MessageModel**](MessageModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="importZipUsingPOST"></a>
# **importZipUsingPOST**
> ScriptsDifferenceListModel importZipUsingPOST(apiKey, _file)

importZip

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ScriptsApi apiInstance = new ScriptsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    File _file = new File("/path/to/file"); // File | file
    try {
      ScriptsDifferenceListModel result = apiInstance.importZipUsingPOST(apiKey, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptsApi#importZipUsingPOST");
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
| **apiKey** | **String**| apiKey | |
| **_file** | **File**| file | |

### Return type

[**ScriptsDifferenceListModel**](ScriptsDifferenceListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

