# SnapshotsApi

All URIs are relative to *http://config2.gamesparks.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**copySnapshotToExistingGameUsingPOST1**](SnapshotsApi.md#copySnapshotToExistingGameUsingPOST1) | **POST** /restv2/game/{apiKey}/admin/snapshots/{snapshotId}/copy/to/{targetApiKey} | copySnapshotToExistingGame |
| [**copySnapshotToNewGameUsingPOST**](SnapshotsApi.md#copySnapshotToNewGameUsingPOST) | **POST** /restv2/game/{apiKey}/admin/snapshots/{snapshotId}/copy | copySnapshotToNewGame |
| [**createSnapshotsUsingPOST**](SnapshotsApi.md#createSnapshotsUsingPOST) | **POST** /restv2/game/{apiKey}/admin/snapshots | createSnapshots |
| [**deleteSnapshotUsingDELETE1**](SnapshotsApi.md#deleteSnapshotUsingDELETE1) | **DELETE** /restv2/game/{apiKey}/admin/snapshots/{snapshotId} | deleteSnapshot |
| [**getLiveSnapshotIdUsingGET**](SnapshotsApi.md#getLiveSnapshotIdUsingGET) | **GET** /restv2/game/{apiKey}/admin/snapshots/liveSnapshotId | getLiveSnapshotId |
| [**getSnapshotUsingGET**](SnapshotsApi.md#getSnapshotUsingGET) | **GET** /restv2/game/{apiKey}/admin/snapshots/{snapshotId} | getSnapshot |
| [**getSnapshotsUsingGET**](SnapshotsApi.md#getSnapshotsUsingGET) | **GET** /restv2/game/{apiKey}/admin/snapshots/page/{page} | getSnapshots |
| [**getSnapshotsUsingGET1**](SnapshotsApi.md#getSnapshotsUsingGET1) | **GET** /restv2/game/{apiKey}/admin/snapshots | getSnapshots |
| [**publishSnapshotUsingPOST1**](SnapshotsApi.md#publishSnapshotUsingPOST1) | **POST** /restv2/game/{apiKey}/admin/snapshots/{snapshotId}/publish | publishSnapshot |
| [**revertToSnapshotUsingPOST**](SnapshotsApi.md#revertToSnapshotUsingPOST) | **POST** /restv2/game/{apiKey}/admin/snapshots/revert/to/{snapshotId} | revertToSnapshot |
| [**unpublishSnapshotUsingPOST**](SnapshotsApi.md#unpublishSnapshotUsingPOST) | **POST** /restv2/game/{apiKey}/admin/snapshots/{snapshotId}/unpublish | unpublishSnapshot |


<a id="copySnapshotToExistingGameUsingPOST1"></a>
# **copySnapshotToExistingGameUsingPOST1**
> SnapshotCreationSuccessModel copySnapshotToExistingGameUsingPOST1(apiKey, snapshotId, targetApiKey, includeGameConfig, includeMetadata, includeBinaries, includeCollaborators)

copySnapshotToExistingGame

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String snapshotId = "snapshotId_example"; // String | snapshotId
    String targetApiKey = "targetApiKey_example"; // String | targetApiKey
    Boolean includeGameConfig = true; // Boolean | includeGameConfig
    Boolean includeMetadata = true; // Boolean | includeMetadata
    Boolean includeBinaries = true; // Boolean | includeBinaries
    Boolean includeCollaborators = true; // Boolean | includeCollaborators
    try {
      SnapshotCreationSuccessModel result = apiInstance.copySnapshotToExistingGameUsingPOST1(apiKey, snapshotId, targetApiKey, includeGameConfig, includeMetadata, includeBinaries, includeCollaborators);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#copySnapshotToExistingGameUsingPOST1");
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
| **includeGameConfig** | **Boolean**| includeGameConfig | [optional] [default to true] |
| **includeMetadata** | **Boolean**| includeMetadata | [optional] [default to true] |
| **includeBinaries** | **Boolean**| includeBinaries | [optional] [default to true] |
| **includeCollaborators** | **Boolean**| includeCollaborators | [optional] [default to true] |

### Return type

[**SnapshotCreationSuccessModel**](SnapshotCreationSuccessModel.md)

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

<a id="copySnapshotToNewGameUsingPOST"></a>
# **copySnapshotToNewGameUsingPOST**
> SnapshotCreationSuccessModel copySnapshotToNewGameUsingPOST(apiKey, snapshotId, includeGameConfig, includeMetadata, includeBinaries, includeCollaborators)

copySnapshotToNewGame

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String snapshotId = "snapshotId_example"; // String | snapshotId
    Boolean includeGameConfig = true; // Boolean | includeGameConfig
    Boolean includeMetadata = true; // Boolean | includeMetadata
    Boolean includeBinaries = true; // Boolean | includeBinaries
    Boolean includeCollaborators = true; // Boolean | includeCollaborators
    try {
      SnapshotCreationSuccessModel result = apiInstance.copySnapshotToNewGameUsingPOST(apiKey, snapshotId, includeGameConfig, includeMetadata, includeBinaries, includeCollaborators);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#copySnapshotToNewGameUsingPOST");
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
| **includeGameConfig** | **Boolean**| includeGameConfig | [optional] [default to true] |
| **includeMetadata** | **Boolean**| includeMetadata | [optional] [default to true] |
| **includeBinaries** | **Boolean**| includeBinaries | [optional] [default to true] |
| **includeCollaborators** | **Boolean**| includeCollaborators | [optional] [default to true] |

### Return type

[**SnapshotCreationSuccessModel**](SnapshotCreationSuccessModel.md)

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

<a id="createSnapshotsUsingPOST"></a>
# **createSnapshotsUsingPOST**
> SnapshotModel createSnapshotsUsingPOST(apiKey, snapshotCreationModel)

createSnapshots

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    SnapshotCreationModel snapshotCreationModel = new SnapshotCreationModel(); // SnapshotCreationModel | description
    try {
      SnapshotModel result = apiInstance.createSnapshotsUsingPOST(apiKey, snapshotCreationModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#createSnapshotsUsingPOST");
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
| **snapshotCreationModel** | [**SnapshotCreationModel**](SnapshotCreationModel.md)| description | |

### Return type

[**SnapshotModel**](SnapshotModel.md)

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

<a id="deleteSnapshotUsingDELETE1"></a>
# **deleteSnapshotUsingDELETE1**
> MessageModel deleteSnapshotUsingDELETE1(apiKey, snapshotId)

deleteSnapshot

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String snapshotId = "snapshotId_example"; // String | snapshotId
    try {
      MessageModel result = apiInstance.deleteSnapshotUsingDELETE1(apiKey, snapshotId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#deleteSnapshotUsingDELETE1");
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

[**MessageModel**](MessageModel.md)

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

<a id="getLiveSnapshotIdUsingGET"></a>
# **getLiveSnapshotIdUsingGET**
> MessageModel getLiveSnapshotIdUsingGET(apiKey)

getLiveSnapshotId

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    try {
      MessageModel result = apiInstance.getLiveSnapshotIdUsingGET(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#getLiveSnapshotIdUsingGET");
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

[**MessageModel**](MessageModel.md)

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

<a id="getSnapshotUsingGET"></a>
# **getSnapshotUsingGET**
> SnapshotModel getSnapshotUsingGET(apiKey, snapshotId)

getSnapshot

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String snapshotId = "snapshotId_example"; // String | snapshotId
    try {
      SnapshotModel result = apiInstance.getSnapshotUsingGET(apiKey, snapshotId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#getSnapshotUsingGET");
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

[**SnapshotModel**](SnapshotModel.md)

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

<a id="getSnapshotsUsingGET"></a>
# **getSnapshotsUsingGET**
> List&lt;SnapshotModel&gt; getSnapshotsUsingGET(apiKey, page, pageSize)

getSnapshots

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    Integer page = 56; // Integer | page
    Integer pageSize = 20; // Integer | pageSize
    try {
      List<SnapshotModel> result = apiInstance.getSnapshotsUsingGET(apiKey, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#getSnapshotsUsingGET");
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
| **pageSize** | **Integer**| pageSize | [optional] [default to 20] |

### Return type

[**List&lt;SnapshotModel&gt;**](SnapshotModel.md)

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

<a id="getSnapshotsUsingGET1"></a>
# **getSnapshotsUsingGET1**
> List&lt;SnapshotModel&gt; getSnapshotsUsingGET1(apiKey, pageSize)

getSnapshots

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    Integer pageSize = 20; // Integer | pageSize
    try {
      List<SnapshotModel> result = apiInstance.getSnapshotsUsingGET1(apiKey, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#getSnapshotsUsingGET1");
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
| **pageSize** | **Integer**| pageSize | [optional] [default to 20] |

### Return type

[**List&lt;SnapshotModel&gt;**](SnapshotModel.md)

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

<a id="publishSnapshotUsingPOST1"></a>
# **publishSnapshotUsingPOST1**
> publishSnapshotUsingPOST1(apiKey, snapshotId)

publishSnapshot

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String snapshotId = "snapshotId_example"; // String | snapshotId
    try {
      apiInstance.publishSnapshotUsingPOST1(apiKey, snapshotId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#publishSnapshotUsingPOST1");
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
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="revertToSnapshotUsingPOST"></a>
# **revertToSnapshotUsingPOST**
> MessageModel revertToSnapshotUsingPOST(apiKey, snapshotId)

revertToSnapshot

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String snapshotId = "snapshotId_example"; // String | snapshotId
    try {
      MessageModel result = apiInstance.revertToSnapshotUsingPOST(apiKey, snapshotId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#revertToSnapshotUsingPOST");
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

[**MessageModel**](MessageModel.md)

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

<a id="unpublishSnapshotUsingPOST"></a>
# **unpublishSnapshotUsingPOST**
> MessageModel unpublishSnapshotUsingPOST(apiKey, snapshotId)

unpublishSnapshot

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String snapshotId = "snapshotId_example"; // String | snapshotId
    try {
      MessageModel result = apiInstance.unpublishSnapshotUsingPOST(apiKey, snapshotId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#unpublishSnapshotUsingPOST");
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

[**MessageModel**](MessageModel.md)

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

