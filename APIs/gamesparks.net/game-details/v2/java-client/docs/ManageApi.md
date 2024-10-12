# ManageApi

All URIs are relative to *http://config2.gamesparks.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**copySnapshotToExistingGameUsingPOST**](ManageApi.md#copySnapshotToExistingGameUsingPOST) | **POST** /restv2/game/{apiKey}/manage/snapshots/{snapshotId}/copy/to/{targetApiKey} | copySnapshotToExistingGame |
| [**createQueryUsingPOST**](ManageApi.md#createQueryUsingPOST) | **POST** /restv2/game/{apiKey}/manage/queries | createQuery |
| [**createScreenUsingPOST**](ManageApi.md#createScreenUsingPOST) | **POST** /restv2/game/{apiKey}/manage/screens | createScreen |
| [**createSnapshotUsingPOST**](ManageApi.md#createSnapshotUsingPOST) | **POST** /restv2/game/{apiKey}/manage/snapshots | createSnapshot |
| [**createSnippetUsingPOST**](ManageApi.md#createSnippetUsingPOST) | **POST** /restv2/game/{apiKey}/manage/snippets | createSnippet |
| [**deleteQueryUsingDELETE**](ManageApi.md#deleteQueryUsingDELETE) | **DELETE** /restv2/game/{apiKey}/manage/queries/{shortCode} | deleteQuery |
| [**deleteScreenUsingDELETE**](ManageApi.md#deleteScreenUsingDELETE) | **DELETE** /restv2/game/{apiKey}/manage/screens/{shortCode} | deleteScreen |
| [**deleteSnapshotUsingDELETE**](ManageApi.md#deleteSnapshotUsingDELETE) | **DELETE** /restv2/game/{apiKey}/manage/snapshots/{snapshotId} | deleteSnapshot |
| [**deleteSnippetUsingDELETE**](ManageApi.md#deleteSnippetUsingDELETE) | **DELETE** /restv2/game/{apiKey}/manage/snippets/{shortCode} | deleteSnippet |
| [**getQueryUsingGET**](ManageApi.md#getQueryUsingGET) | **GET** /restv2/game/{apiKey}/manage/queries/{shortCode} | getQuery |
| [**getScreenUsingGET**](ManageApi.md#getScreenUsingGET) | **GET** /restv2/game/{apiKey}/manage/screens/{shortCode} | getScreen |
| [**getSnippetUsingGET**](ManageApi.md#getSnippetUsingGET) | **GET** /restv2/game/{apiKey}/manage/snippets/{shortCode} | getSnippet |
| [**listExecutableScreensUsingGET**](ManageApi.md#listExecutableScreensUsingGET) | **GET** /restv2/game/{apiKey}/manage/screens/executable | listExecutableScreens |
| [**listQueriesUsingGET**](ManageApi.md#listQueriesUsingGET) | **GET** /restv2/game/{apiKey}/manage/queries | listQueries |
| [**listScreensUsingGET**](ManageApi.md#listScreensUsingGET) | **GET** /restv2/game/{apiKey}/manage/screens | listScreens |
| [**listSnapshotsUsingGET**](ManageApi.md#listSnapshotsUsingGET) | **GET** /restv2/game/{apiKey}/manage/snapshots | listSnapshots |
| [**listSnippetsUsingGET**](ManageApi.md#listSnippetsUsingGET) | **GET** /restv2/game/{apiKey}/manage/snippets | listSnippets |
| [**publishSnapshotUsingPOST**](ManageApi.md#publishSnapshotUsingPOST) | **POST** /restv2/game/{apiKey}/manage/snapshots/{snapshotId}/publish | publishSnapshot |
| [**revertSnapshotUsingPOST**](ManageApi.md#revertSnapshotUsingPOST) | **POST** /restv2/game/{apiKey}/manage/snapshots/{snapshotId}/revert | revertSnapshot |
| [**updateQueryUsingPUT**](ManageApi.md#updateQueryUsingPUT) | **PUT** /restv2/game/{apiKey}/manage/queries/{shortCode} | updateQuery |
| [**updateScreenUsingPUT**](ManageApi.md#updateScreenUsingPUT) | **PUT** /restv2/game/{apiKey}/manage/screens/{shortCode} | updateScreen |
| [**updateSnippetUsingPUT**](ManageApi.md#updateSnippetUsingPUT) | **PUT** /restv2/game/{apiKey}/manage/snippets/{shortCode} | updateSnippet |


<a id="copySnapshotToExistingGameUsingPOST"></a>
# **copySnapshotToExistingGameUsingPOST**
> ManageResult copySnapshotToExistingGameUsingPOST(apiKey, snapshotId, targetApiKey)

copySnapshotToExistingGame

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String snapshotId = "snapshotId_example"; // String | snapshotId
    String targetApiKey = "targetApiKey_example"; // String | targetApiKey
    try {
      ManageResult result = apiInstance.copySnapshotToExistingGameUsingPOST(apiKey, snapshotId, targetApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#copySnapshotToExistingGameUsingPOST");
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
| **snapshotId** | **String**| snapshotId | |
| **targetApiKey** | **String**| targetApiKey | |

### Return type

[**ManageResult**](ManageResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="createQueryUsingPOST"></a>
# **createQueryUsingPOST**
> ManageQuery createQueryUsingPOST(apiKey, manageQuery)

createQuery

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    ManageQuery manageQuery = new ManageQuery(); // ManageQuery | query
    try {
      ManageQuery result = apiInstance.createQueryUsingPOST(apiKey, manageQuery);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#createQueryUsingPOST");
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
| **manageQuery** | [**ManageQuery**](ManageQuery.md)| query | |

### Return type

[**ManageQuery**](ManageQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="createScreenUsingPOST"></a>
# **createScreenUsingPOST**
> ManageScreen createScreenUsingPOST(apiKey, manageScreen)

createScreen

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    ManageScreen manageScreen = new ManageScreen(); // ManageScreen | screen
    try {
      ManageScreen result = apiInstance.createScreenUsingPOST(apiKey, manageScreen);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#createScreenUsingPOST");
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
| **manageScreen** | [**ManageScreen**](ManageScreen.md)| screen | |

### Return type

[**ManageScreen**](ManageScreen.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="createSnapshotUsingPOST"></a>
# **createSnapshotUsingPOST**
> ManageSnapshot createSnapshotUsingPOST(apiKey, snapshotCreationModel)

createSnapshot

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    SnapshotCreationModel snapshotCreationModel = new SnapshotCreationModel(); // SnapshotCreationModel | model
    try {
      ManageSnapshot result = apiInstance.createSnapshotUsingPOST(apiKey, snapshotCreationModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#createSnapshotUsingPOST");
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
| **snapshotCreationModel** | [**SnapshotCreationModel**](SnapshotCreationModel.md)| model | |

### Return type

[**ManageSnapshot**](ManageSnapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="createSnippetUsingPOST"></a>
# **createSnippetUsingPOST**
> ManageSnippet createSnippetUsingPOST(apiKey, manageSnippet)

createSnippet

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    ManageSnippet manageSnippet = new ManageSnippet(); // ManageSnippet | snippet
    try {
      ManageSnippet result = apiInstance.createSnippetUsingPOST(apiKey, manageSnippet);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#createSnippetUsingPOST");
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
| **manageSnippet** | [**ManageSnippet**](ManageSnippet.md)| snippet | |

### Return type

[**ManageSnippet**](ManageSnippet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="deleteQueryUsingDELETE"></a>
# **deleteQueryUsingDELETE**
> ManageResult deleteQueryUsingDELETE(apiKey, shortCode)

deleteQuery

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String shortCode = "shortCode_example"; // String | shortCode
    try {
      ManageResult result = apiInstance.deleteQueryUsingDELETE(apiKey, shortCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#deleteQueryUsingDELETE");
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
| **shortCode** | **String**| shortCode | |

### Return type

[**ManageResult**](ManageResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="deleteScreenUsingDELETE"></a>
# **deleteScreenUsingDELETE**
> ManageResult deleteScreenUsingDELETE(apiKey, shortCode)

deleteScreen

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String shortCode = "shortCode_example"; // String | shortCode
    try {
      ManageResult result = apiInstance.deleteScreenUsingDELETE(apiKey, shortCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#deleteScreenUsingDELETE");
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
| **shortCode** | **String**| shortCode | |

### Return type

[**ManageResult**](ManageResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="deleteSnapshotUsingDELETE"></a>
# **deleteSnapshotUsingDELETE**
> deleteSnapshotUsingDELETE(apiKey, snapshotId)

deleteSnapshot

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String snapshotId = "snapshotId_example"; // String | snapshotId
    try {
      apiInstance.deleteSnapshotUsingDELETE(apiKey, snapshotId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#deleteSnapshotUsingDELETE");
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
| **snapshotId** | **String**| snapshotId | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **201** | Created |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="deleteSnippetUsingDELETE"></a>
# **deleteSnippetUsingDELETE**
> ManageResult deleteSnippetUsingDELETE(apiKey, shortCode)

deleteSnippet

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String shortCode = "shortCode_example"; // String | shortCode
    try {
      ManageResult result = apiInstance.deleteSnippetUsingDELETE(apiKey, shortCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#deleteSnippetUsingDELETE");
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
| **shortCode** | **String**| shortCode | |

### Return type

[**ManageResult**](ManageResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="getQueryUsingGET"></a>
# **getQueryUsingGET**
> ManageQuery getQueryUsingGET(apiKey, shortCode)

getQuery

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String shortCode = "shortCode_example"; // String | shortCode
    try {
      ManageQuery result = apiInstance.getQueryUsingGET(apiKey, shortCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#getQueryUsingGET");
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
| **shortCode** | **String**| shortCode | |

### Return type

[**ManageQuery**](ManageQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="getScreenUsingGET"></a>
# **getScreenUsingGET**
> ManageScreen getScreenUsingGET(apiKey, shortCode)

getScreen

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String shortCode = "shortCode_example"; // String | shortCode
    try {
      ManageScreen result = apiInstance.getScreenUsingGET(apiKey, shortCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#getScreenUsingGET");
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
| **shortCode** | **String**| shortCode | |

### Return type

[**ManageScreen**](ManageScreen.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="getSnippetUsingGET"></a>
# **getSnippetUsingGET**
> ManageSnippet getSnippetUsingGET(apiKey, shortCode)

getSnippet

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String shortCode = "shortCode_example"; // String | shortCode
    try {
      ManageSnippet result = apiInstance.getSnippetUsingGET(apiKey, shortCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#getSnippetUsingGET");
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
| **shortCode** | **String**| shortCode | |

### Return type

[**ManageSnippet**](ManageSnippet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="listExecutableScreensUsingGET"></a>
# **listExecutableScreensUsingGET**
> List&lt;ManageItemSummary&gt; listExecutableScreensUsingGET(apiKey)

listExecutableScreens

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    try {
      List<ManageItemSummary> result = apiInstance.listExecutableScreensUsingGET(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#listExecutableScreensUsingGET");
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

[**List&lt;ManageItemSummary&gt;**](ManageItemSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="listQueriesUsingGET"></a>
# **listQueriesUsingGET**
> List&lt;ManageItemSummary&gt; listQueriesUsingGET(apiKey)

listQueries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    try {
      List<ManageItemSummary> result = apiInstance.listQueriesUsingGET(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#listQueriesUsingGET");
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

[**List&lt;ManageItemSummary&gt;**](ManageItemSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="listScreensUsingGET"></a>
# **listScreensUsingGET**
> List&lt;ManageItemSummary&gt; listScreensUsingGET(apiKey)

listScreens

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    try {
      List<ManageItemSummary> result = apiInstance.listScreensUsingGET(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#listScreensUsingGET");
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

[**List&lt;ManageItemSummary&gt;**](ManageItemSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="listSnapshotsUsingGET"></a>
# **listSnapshotsUsingGET**
> List&lt;ManageSnapshot&gt; listSnapshotsUsingGET(apiKey)

listSnapshots

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    try {
      List<ManageSnapshot> result = apiInstance.listSnapshotsUsingGET(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#listSnapshotsUsingGET");
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

[**List&lt;ManageSnapshot&gt;**](ManageSnapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="listSnippetsUsingGET"></a>
# **listSnippetsUsingGET**
> List&lt;ManageItemSummary&gt; listSnippetsUsingGET(apiKey)

listSnippets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    try {
      List<ManageItemSummary> result = apiInstance.listSnippetsUsingGET(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#listSnippetsUsingGET");
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

[**List&lt;ManageItemSummary&gt;**](ManageItemSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="publishSnapshotUsingPOST"></a>
# **publishSnapshotUsingPOST**
> ManageResult publishSnapshotUsingPOST(apiKey, snapshotId)

publishSnapshot

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String snapshotId = "snapshotId_example"; // String | snapshotId
    try {
      ManageResult result = apiInstance.publishSnapshotUsingPOST(apiKey, snapshotId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#publishSnapshotUsingPOST");
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
| **snapshotId** | **String**| snapshotId | |

### Return type

[**ManageResult**](ManageResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="revertSnapshotUsingPOST"></a>
# **revertSnapshotUsingPOST**
> ManageResult revertSnapshotUsingPOST(apiKey, snapshotId)

revertSnapshot

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String snapshotId = "snapshotId_example"; // String | snapshotId
    try {
      ManageResult result = apiInstance.revertSnapshotUsingPOST(apiKey, snapshotId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#revertSnapshotUsingPOST");
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
| **snapshotId** | **String**| snapshotId | |

### Return type

[**ManageResult**](ManageResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="updateQueryUsingPUT"></a>
# **updateQueryUsingPUT**
> ManageQuery updateQueryUsingPUT(apiKey, shortCode, manageQuery)

updateQuery

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String shortCode = "shortCode_example"; // String | shortCode
    ManageQuery manageQuery = new ManageQuery(); // ManageQuery | query
    try {
      ManageQuery result = apiInstance.updateQueryUsingPUT(apiKey, shortCode, manageQuery);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#updateQueryUsingPUT");
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
| **shortCode** | **String**| shortCode | |
| **manageQuery** | [**ManageQuery**](ManageQuery.md)| query | |

### Return type

[**ManageQuery**](ManageQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="updateScreenUsingPUT"></a>
# **updateScreenUsingPUT**
> ManageScreen updateScreenUsingPUT(apiKey, shortCode, manageScreen)

updateScreen

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String shortCode = "shortCode_example"; // String | shortCode
    ManageScreen manageScreen = new ManageScreen(); // ManageScreen | screen
    try {
      ManageScreen result = apiInstance.updateScreenUsingPUT(apiKey, shortCode, manageScreen);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#updateScreenUsingPUT");
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
| **shortCode** | **String**| shortCode | |
| **manageScreen** | [**ManageScreen**](ManageScreen.md)| screen | |

### Return type

[**ManageScreen**](ManageScreen.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="updateSnippetUsingPUT"></a>
# **updateSnippetUsingPUT**
> ManageSnippet updateSnippetUsingPUT(apiKey, shortCode, manageSnippet)

updateSnippet

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String shortCode = "shortCode_example"; // String | shortCode
    ManageSnippet manageSnippet = new ManageSnippet(); // ManageSnippet | snippet
    try {
      ManageSnippet result = apiInstance.updateSnippetUsingPUT(apiKey, shortCode, manageSnippet);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#updateSnippetUsingPUT");
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
| **shortCode** | **String**| shortCode | |
| **manageSnippet** | [**ManageSnippet**](ManageSnippet.md)| snippet | |

### Return type

[**ManageSnippet**](ManageSnippet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

