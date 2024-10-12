# ExperimentsApi

All URIs are relative to *http://config2.gamesparks.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createExperimentUsingPOST**](ExperimentsApi.md#createExperimentUsingPOST) | **POST** /restv2/game/{apiKey}/manage/experiments | createExperiment |
| [**deleteExperimentUsingDELETE**](ExperimentsApi.md#deleteExperimentUsingDELETE) | **DELETE** /restv2/game/{apiKey}/manage/experiments/{id} | deleteExperiment |
| [**doActionExperimentUsingPOST**](ExperimentsApi.md#doActionExperimentUsingPOST) | **POST** /restv2/game/{apiKey}/manage/experiments/{id}/{action} | doActionExperiment |
| [**getExperimentUsingGET**](ExperimentsApi.md#getExperimentUsingGET) | **GET** /restv2/game/{apiKey}/manage/experiments/{id} | getExperiment |
| [**getExperimentsUsingGET**](ExperimentsApi.md#getExperimentsUsingGET) | **GET** /restv2/game/{apiKey}/manage/experiments | getExperiments |
| [**updateExperimentUsingPUT**](ExperimentsApi.md#updateExperimentUsingPUT) | **PUT** /restv2/game/{apiKey}/manage/experiments/{id} | updateExperiment |


<a id="createExperimentUsingPOST"></a>
# **createExperimentUsingPOST**
> ExperimentModel createExperimentUsingPOST(apiKey, experimentModel)

createExperiment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExperimentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ExperimentsApi apiInstance = new ExperimentsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    ExperimentModel experimentModel = new ExperimentModel(); // ExperimentModel | input
    try {
      ExperimentModel result = apiInstance.createExperimentUsingPOST(apiKey, experimentModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExperimentsApi#createExperimentUsingPOST");
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
| **experimentModel** | [**ExperimentModel**](ExperimentModel.md)| input | |

### Return type

[**ExperimentModel**](ExperimentModel.md)

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

<a id="deleteExperimentUsingDELETE"></a>
# **deleteExperimentUsingDELETE**
> MessageModel deleteExperimentUsingDELETE(apiKey, id)

deleteExperiment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExperimentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ExperimentsApi apiInstance = new ExperimentsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    Long id = 56L; // Long | id
    try {
      MessageModel result = apiInstance.deleteExperimentUsingDELETE(apiKey, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExperimentsApi#deleteExperimentUsingDELETE");
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
| **id** | **Long**| id | |

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

<a id="doActionExperimentUsingPOST"></a>
# **doActionExperimentUsingPOST**
> ExperimentModel doActionExperimentUsingPOST(apiKey, id, action)

doActionExperiment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExperimentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ExperimentsApi apiInstance = new ExperimentsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    Long id = 56L; // Long | id
    String action = "start"; // String | action
    try {
      ExperimentModel result = apiInstance.doActionExperimentUsingPOST(apiKey, id, action);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExperimentsApi#doActionExperimentUsingPOST");
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
| **id** | **Long**| id | |
| **action** | **String**| action | [enum: start, stop, publish, unpublish] |

### Return type

[**ExperimentModel**](ExperimentModel.md)

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

<a id="getExperimentUsingGET"></a>
# **getExperimentUsingGET**
> ExperimentModel getExperimentUsingGET(apiKey, id)

getExperiment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExperimentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ExperimentsApi apiInstance = new ExperimentsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    Long id = 56L; // Long | id
    try {
      ExperimentModel result = apiInstance.getExperimentUsingGET(apiKey, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExperimentsApi#getExperimentUsingGET");
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
| **id** | **Long**| id | |

### Return type

[**ExperimentModel**](ExperimentModel.md)

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

<a id="getExperimentsUsingGET"></a>
# **getExperimentsUsingGET**
> List&lt;ExperimentModel&gt; getExperimentsUsingGET(apiKey)

getExperiments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExperimentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ExperimentsApi apiInstance = new ExperimentsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    try {
      List<ExperimentModel> result = apiInstance.getExperimentsUsingGET(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExperimentsApi#getExperimentsUsingGET");
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

[**List&lt;ExperimentModel&gt;**](ExperimentModel.md)

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

<a id="updateExperimentUsingPUT"></a>
# **updateExperimentUsingPUT**
> ExperimentModel updateExperimentUsingPUT(apiKey, id, experimentModel)

updateExperiment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExperimentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    ExperimentsApi apiInstance = new ExperimentsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    Long id = 56L; // Long | id
    ExperimentModel experimentModel = new ExperimentModel(); // ExperimentModel | input
    try {
      ExperimentModel result = apiInstance.updateExperimentUsingPUT(apiKey, id, experimentModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExperimentsApi#updateExperimentUsingPUT");
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
| **id** | **Long**| id | |
| **experimentModel** | [**ExperimentModel**](ExperimentModel.md)| input | |

### Return type

[**ExperimentModel**](ExperimentModel.md)

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

