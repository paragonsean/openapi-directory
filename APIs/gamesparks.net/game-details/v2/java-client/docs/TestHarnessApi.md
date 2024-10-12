# TestHarnessApi

All URIs are relative to *http://config2.gamesparks.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTestHarnessScenarioUsingPOST**](TestHarnessApi.md#createTestHarnessScenarioUsingPOST) | **POST** /restv2/game/{apiKey}/admin/testHarness/scenarios | createTestHarnessScenario |
| [**deleteTestHarnessScenarioUsingDELETE**](TestHarnessApi.md#deleteTestHarnessScenarioUsingDELETE) | **DELETE** /restv2/game/{apiKey}/admin/testHarness/scenarios/{scenarioName} | deleteTestHarnessScenario |
| [**getTestHarnessScenarioUsingGET**](TestHarnessApi.md#getTestHarnessScenarioUsingGET) | **GET** /restv2/game/{apiKey}/admin/testHarness/scenarios/{scenarioName} | getTestHarnessScenario |
| [**getTestHarnessScenariosUsingGET**](TestHarnessApi.md#getTestHarnessScenariosUsingGET) | **GET** /restv2/game/{apiKey}/admin/testHarness/scenarios | getTestHarnessScenarios |
| [**updateTestHarnessScenarioUsingPUT**](TestHarnessApi.md#updateTestHarnessScenarioUsingPUT) | **PUT** /restv2/game/{apiKey}/admin/testHarness/scenarios/{scenarioName} | updateTestHarnessScenario |


<a id="createTestHarnessScenarioUsingPOST"></a>
# **createTestHarnessScenarioUsingPOST**
> TestHarnessScenarioModel createTestHarnessScenarioUsingPOST(apiKey, testHarnessScenarioModel)

createTestHarnessScenario

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestHarnessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    TestHarnessApi apiInstance = new TestHarnessApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    TestHarnessScenarioModel testHarnessScenarioModel = new TestHarnessScenarioModel(); // TestHarnessScenarioModel | testHarnessScenarioDTO
    try {
      TestHarnessScenarioModel result = apiInstance.createTestHarnessScenarioUsingPOST(apiKey, testHarnessScenarioModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestHarnessApi#createTestHarnessScenarioUsingPOST");
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
| **testHarnessScenarioModel** | [**TestHarnessScenarioModel**](TestHarnessScenarioModel.md)| testHarnessScenarioDTO | |

### Return type

[**TestHarnessScenarioModel**](TestHarnessScenarioModel.md)

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

<a id="deleteTestHarnessScenarioUsingDELETE"></a>
# **deleteTestHarnessScenarioUsingDELETE**
> MessageModel deleteTestHarnessScenarioUsingDELETE(apiKey, scenarioName)

deleteTestHarnessScenario

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestHarnessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    TestHarnessApi apiInstance = new TestHarnessApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String scenarioName = "scenarioName_example"; // String | scenarioName
    try {
      MessageModel result = apiInstance.deleteTestHarnessScenarioUsingDELETE(apiKey, scenarioName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestHarnessApi#deleteTestHarnessScenarioUsingDELETE");
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
| **scenarioName** | **String**| scenarioName | |

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

<a id="getTestHarnessScenarioUsingGET"></a>
# **getTestHarnessScenarioUsingGET**
> TestHarnessScenarioModel getTestHarnessScenarioUsingGET(apiKey, scenarioName)

getTestHarnessScenario

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestHarnessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    TestHarnessApi apiInstance = new TestHarnessApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String scenarioName = "scenarioName_example"; // String | scenarioName
    try {
      TestHarnessScenarioModel result = apiInstance.getTestHarnessScenarioUsingGET(apiKey, scenarioName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestHarnessApi#getTestHarnessScenarioUsingGET");
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
| **scenarioName** | **String**| scenarioName | |

### Return type

[**TestHarnessScenarioModel**](TestHarnessScenarioModel.md)

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

<a id="getTestHarnessScenariosUsingGET"></a>
# **getTestHarnessScenariosUsingGET**
> List&lt;TestHarnessScenarioModel&gt; getTestHarnessScenariosUsingGET(apiKey)

getTestHarnessScenarios

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestHarnessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    TestHarnessApi apiInstance = new TestHarnessApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    try {
      List<TestHarnessScenarioModel> result = apiInstance.getTestHarnessScenariosUsingGET(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestHarnessApi#getTestHarnessScenariosUsingGET");
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

[**List&lt;TestHarnessScenarioModel&gt;**](TestHarnessScenarioModel.md)

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

<a id="updateTestHarnessScenarioUsingPUT"></a>
# **updateTestHarnessScenarioUsingPUT**
> TestHarnessScenarioModel updateTestHarnessScenarioUsingPUT(apiKey, scenarioName, testHarnessScenarioModel)

updateTestHarnessScenario

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestHarnessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    TestHarnessApi apiInstance = new TestHarnessApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String scenarioName = "scenarioName_example"; // String | scenarioName
    TestHarnessScenarioModel testHarnessScenarioModel = new TestHarnessScenarioModel(); // TestHarnessScenarioModel | testHarnessScenarioDTO
    try {
      TestHarnessScenarioModel result = apiInstance.updateTestHarnessScenarioUsingPUT(apiKey, scenarioName, testHarnessScenarioModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestHarnessApi#updateTestHarnessScenarioUsingPUT");
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
| **scenarioName** | **String**| scenarioName | |
| **testHarnessScenarioModel** | [**TestHarnessScenarioModel**](TestHarnessScenarioModel.md)| testHarnessScenarioDTO | |

### Return type

[**TestHarnessScenarioModel**](TestHarnessScenarioModel.md)

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

