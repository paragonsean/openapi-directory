# TaskManagerApiApi

All URIs are relative to *https://api.tradematic.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**taskmanagerTasksGet**](TaskManagerApiApi.md#taskmanagerTasksGet) | **GET** /taskmanager/tasks | Get tasks list |
| [**taskmanagerTasksPost**](TaskManagerApiApi.md#taskmanagerTasksPost) | **POST** /taskmanager/tasks | Create a new task |
| [**taskmanagerTasksTaskidBymonthsGet**](TaskManagerApiApi.md#taskmanagerTasksTaskidBymonthsGet) | **GET** /taskmanager/tasks/{taskid}/bymonths | Get backtest data for equity chart, grouped by months |
| [**taskmanagerTasksTaskidByquartersGet**](TaskManagerApiApi.md#taskmanagerTasksTaskidByquartersGet) | **GET** /taskmanager/tasks/{taskid}/byquarters | Get backtest data for equity chart, grouped by quarters |
| [**taskmanagerTasksTaskidByyearsGet**](TaskManagerApiApi.md#taskmanagerTasksTaskidByyearsGet) | **GET** /taskmanager/tasks/{taskid}/byyears | Get backtest data for equity chart, grouped by years |
| [**taskmanagerTasksTaskidContributionGet**](TaskManagerApiApi.md#taskmanagerTasksTaskidContributionGet) | **GET** /taskmanager/tasks/{taskid}/contribution | Get backtest symbol contribution data |
| [**taskmanagerTasksTaskidDrawdownGet**](TaskManagerApiApi.md#taskmanagerTasksTaskidDrawdownGet) | **GET** /taskmanager/tasks/{taskid}/drawdown | Get data for drawdown chart |
| [**taskmanagerTasksTaskidEquityGet**](TaskManagerApiApi.md#taskmanagerTasksTaskidEquityGet) | **GET** /taskmanager/tasks/{taskid}/equity | Get data for equity chart |
| [**taskmanagerTasksTaskidEquitypctGet**](TaskManagerApiApi.md#taskmanagerTasksTaskidEquitypctGet) | **GET** /taskmanager/tasks/{taskid}/equitypct | Get data for equity chart (%) |
| [**taskmanagerTasksTaskidEquitypctsmGet**](TaskManagerApiApi.md#taskmanagerTasksTaskidEquitypctsmGet) | **GET** /taskmanager/tasks/{taskid}/equitypctsm | Get spared data for equity chart (%) |
| [**taskmanagerTasksTaskidFolderGet**](TaskManagerApiApi.md#taskmanagerTasksTaskidFolderGet) | **GET** /taskmanager/tasks/{taskid}/folder | Get task result folder name |
| [**taskmanagerTasksTaskidGet**](TaskManagerApiApi.md#taskmanagerTasksTaskidGet) | **GET** /taskmanager/tasks/{taskid} | Get task by ID |
| [**taskmanagerTasksTaskidPerformanceGet**](TaskManagerApiApi.md#taskmanagerTasksTaskidPerformanceGet) | **GET** /taskmanager/tasks/{taskid}/performance | Get backtest statistics |
| [**taskmanagerTasksTaskidResult2Get**](TaskManagerApiApi.md#taskmanagerTasksTaskidResult2Get) | **GET** /taskmanager/tasks/{taskid}/result2 | Get task result (version 2) |
| [**taskmanagerTasksTaskidResultGet**](TaskManagerApiApi.md#taskmanagerTasksTaskidResultGet) | **GET** /taskmanager/tasks/{taskid}/result | Get task result |
| [**taskmanagerTasksTaskidStatusGet**](TaskManagerApiApi.md#taskmanagerTasksTaskidStatusGet) | **GET** /taskmanager/tasks/{taskid}/status | Get task status |
| [**taskmanagerTasksTaskidTradesGet**](TaskManagerApiApi.md#taskmanagerTasksTaskidTradesGet) | **GET** /taskmanager/tasks/{taskid}/trades | Get backtest trades list |


<a id="taskmanagerTasksGet"></a>
# **taskmanagerTasksGet**
> List&lt;Task&gt; taskmanagerTasksGet()

Get tasks list

Get tasks list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskManagerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    TaskManagerApiApi apiInstance = new TaskManagerApiApi(defaultClient);
    try {
      List<Task> result = apiInstance.taskmanagerTasksGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskManagerApiApi#taskmanagerTasksGet");
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

[**List&lt;Task&gt;**](Task.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="taskmanagerTasksPost"></a>
# **taskmanagerTasksPost**
> TaskmanagerTasksPost202Response taskmanagerTasksPost(body)

Create a new task

Create a new task

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskManagerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    TaskManagerApiApi apiInstance = new TaskManagerApiApi(defaultClient);
    TaskmanagerTasksPostRequest body = new TaskmanagerTasksPostRequest(); // TaskmanagerTasksPostRequest | 
    try {
      TaskmanagerTasksPost202Response result = apiInstance.taskmanagerTasksPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskManagerApiApi#taskmanagerTasksPost");
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
| **body** | [**TaskmanagerTasksPostRequest**](TaskmanagerTasksPostRequest.md)|  | |

### Return type

[**TaskmanagerTasksPost202Response**](TaskmanagerTasksPost202Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="taskmanagerTasksTaskidBymonthsGet"></a>
# **taskmanagerTasksTaskidBymonthsGet**
> List&lt;ByMonths&gt; taskmanagerTasksTaskidBymonthsGet(taskid)

Get backtest data for equity chart, grouped by months

Get backtest data for equity chart, grouped by months

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskManagerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    TaskManagerApiApi apiInstance = new TaskManagerApiApi(defaultClient);
    Long taskid = 56L; // Long | 
    try {
      List<ByMonths> result = apiInstance.taskmanagerTasksTaskidBymonthsGet(taskid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskManagerApiApi#taskmanagerTasksTaskidBymonthsGet");
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
| **taskid** | **Long**|  | |

### Return type

[**List&lt;ByMonths&gt;**](ByMonths.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="taskmanagerTasksTaskidByquartersGet"></a>
# **taskmanagerTasksTaskidByquartersGet**
> List&lt;ByQuarters&gt; taskmanagerTasksTaskidByquartersGet(taskid)

Get backtest data for equity chart, grouped by quarters

Get backtest data for equity chart, grouped by quarters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskManagerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    TaskManagerApiApi apiInstance = new TaskManagerApiApi(defaultClient);
    Long taskid = 56L; // Long | 
    try {
      List<ByQuarters> result = apiInstance.taskmanagerTasksTaskidByquartersGet(taskid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskManagerApiApi#taskmanagerTasksTaskidByquartersGet");
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
| **taskid** | **Long**|  | |

### Return type

[**List&lt;ByQuarters&gt;**](ByQuarters.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="taskmanagerTasksTaskidByyearsGet"></a>
# **taskmanagerTasksTaskidByyearsGet**
> List&lt;ByYears&gt; taskmanagerTasksTaskidByyearsGet(taskid)

Get backtest data for equity chart, grouped by years

Get backtest data for equity chart, grouped by years

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskManagerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    TaskManagerApiApi apiInstance = new TaskManagerApiApi(defaultClient);
    Long taskid = 56L; // Long | 
    try {
      List<ByYears> result = apiInstance.taskmanagerTasksTaskidByyearsGet(taskid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskManagerApiApi#taskmanagerTasksTaskidByyearsGet");
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
| **taskid** | **Long**|  | |

### Return type

[**List&lt;ByYears&gt;**](ByYears.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="taskmanagerTasksTaskidContributionGet"></a>
# **taskmanagerTasksTaskidContributionGet**
> List&lt;Contribution&gt; taskmanagerTasksTaskidContributionGet(taskid)

Get backtest symbol contribution data

Get backtest symbol contribution data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskManagerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    TaskManagerApiApi apiInstance = new TaskManagerApiApi(defaultClient);
    Long taskid = 56L; // Long | 
    try {
      List<Contribution> result = apiInstance.taskmanagerTasksTaskidContributionGet(taskid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskManagerApiApi#taskmanagerTasksTaskidContributionGet");
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
| **taskid** | **Long**|  | |

### Return type

[**List&lt;Contribution&gt;**](Contribution.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="taskmanagerTasksTaskidDrawdownGet"></a>
# **taskmanagerTasksTaskidDrawdownGet**
> List&lt;DrawdownItem&gt; taskmanagerTasksTaskidDrawdownGet(taskid)

Get data for drawdown chart

Get data for drawdown chart

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskManagerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    TaskManagerApiApi apiInstance = new TaskManagerApiApi(defaultClient);
    Long taskid = 56L; // Long | 
    try {
      List<DrawdownItem> result = apiInstance.taskmanagerTasksTaskidDrawdownGet(taskid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskManagerApiApi#taskmanagerTasksTaskidDrawdownGet");
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
| **taskid** | **Long**|  | |

### Return type

[**List&lt;DrawdownItem&gt;**](DrawdownItem.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="taskmanagerTasksTaskidEquityGet"></a>
# **taskmanagerTasksTaskidEquityGet**
> List&lt;EquityItem&gt; taskmanagerTasksTaskidEquityGet(taskid)

Get data for equity chart

Get data for equity chart

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskManagerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    TaskManagerApiApi apiInstance = new TaskManagerApiApi(defaultClient);
    Long taskid = 56L; // Long | 
    try {
      List<EquityItem> result = apiInstance.taskmanagerTasksTaskidEquityGet(taskid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskManagerApiApi#taskmanagerTasksTaskidEquityGet");
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
| **taskid** | **Long**|  | |

### Return type

[**List&lt;EquityItem&gt;**](EquityItem.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="taskmanagerTasksTaskidEquitypctGet"></a>
# **taskmanagerTasksTaskidEquitypctGet**
> List&lt;EquityPctItem&gt; taskmanagerTasksTaskidEquitypctGet(taskid)

Get data for equity chart (%)

Get data for equity chart (%)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskManagerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    TaskManagerApiApi apiInstance = new TaskManagerApiApi(defaultClient);
    Long taskid = 56L; // Long | 
    try {
      List<EquityPctItem> result = apiInstance.taskmanagerTasksTaskidEquitypctGet(taskid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskManagerApiApi#taskmanagerTasksTaskidEquitypctGet");
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
| **taskid** | **Long**|  | |

### Return type

[**List&lt;EquityPctItem&gt;**](EquityPctItem.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="taskmanagerTasksTaskidEquitypctsmGet"></a>
# **taskmanagerTasksTaskidEquitypctsmGet**
> List&lt;EquityPctSmItem&gt; taskmanagerTasksTaskidEquitypctsmGet(taskid)

Get spared data for equity chart (%)

Get spared data for equity chart (%)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskManagerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    TaskManagerApiApi apiInstance = new TaskManagerApiApi(defaultClient);
    Long taskid = 56L; // Long | 
    try {
      List<EquityPctSmItem> result = apiInstance.taskmanagerTasksTaskidEquitypctsmGet(taskid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskManagerApiApi#taskmanagerTasksTaskidEquitypctsmGet");
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
| **taskid** | **Long**|  | |

### Return type

[**List&lt;EquityPctSmItem&gt;**](EquityPctSmItem.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="taskmanagerTasksTaskidFolderGet"></a>
# **taskmanagerTasksTaskidFolderGet**
> TaskmanagerTasksTaskidFolderGet200Response taskmanagerTasksTaskidFolderGet(taskid)

Get task result folder name

Get task result folder name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskManagerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    TaskManagerApiApi apiInstance = new TaskManagerApiApi(defaultClient);
    Long taskid = 56L; // Long | 
    try {
      TaskmanagerTasksTaskidFolderGet200Response result = apiInstance.taskmanagerTasksTaskidFolderGet(taskid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskManagerApiApi#taskmanagerTasksTaskidFolderGet");
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
| **taskid** | **Long**|  | |

### Return type

[**TaskmanagerTasksTaskidFolderGet200Response**](TaskmanagerTasksTaskidFolderGet200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="taskmanagerTasksTaskidGet"></a>
# **taskmanagerTasksTaskidGet**
> Task taskmanagerTasksTaskidGet(taskid)

Get task by ID

Get task by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskManagerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    TaskManagerApiApi apiInstance = new TaskManagerApiApi(defaultClient);
    Long taskid = 56L; // Long | 
    try {
      Task result = apiInstance.taskmanagerTasksTaskidGet(taskid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskManagerApiApi#taskmanagerTasksTaskidGet");
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
| **taskid** | **Long**|  | |

### Return type

[**Task**](Task.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="taskmanagerTasksTaskidPerformanceGet"></a>
# **taskmanagerTasksTaskidPerformanceGet**
> TaskmanagerTasksTaskidPerformanceGet200Response taskmanagerTasksTaskidPerformanceGet(taskid)

Get backtest statistics

Get backtest statistics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskManagerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    TaskManagerApiApi apiInstance = new TaskManagerApiApi(defaultClient);
    Long taskid = 56L; // Long | 
    try {
      TaskmanagerTasksTaskidPerformanceGet200Response result = apiInstance.taskmanagerTasksTaskidPerformanceGet(taskid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskManagerApiApi#taskmanagerTasksTaskidPerformanceGet");
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
| **taskid** | **Long**|  | |

### Return type

[**TaskmanagerTasksTaskidPerformanceGet200Response**](TaskmanagerTasksTaskidPerformanceGet200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="taskmanagerTasksTaskidResult2Get"></a>
# **taskmanagerTasksTaskidResult2Get**
> TaskmanagerTasksTaskidResult2Get200Response taskmanagerTasksTaskidResult2Get(taskid)

Get task result (version 2)

Get task result (version 2)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskManagerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    TaskManagerApiApi apiInstance = new TaskManagerApiApi(defaultClient);
    Long taskid = 56L; // Long | 
    try {
      TaskmanagerTasksTaskidResult2Get200Response result = apiInstance.taskmanagerTasksTaskidResult2Get(taskid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskManagerApiApi#taskmanagerTasksTaskidResult2Get");
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
| **taskid** | **Long**|  | |

### Return type

[**TaskmanagerTasksTaskidResult2Get200Response**](TaskmanagerTasksTaskidResult2Get200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="taskmanagerTasksTaskidResultGet"></a>
# **taskmanagerTasksTaskidResultGet**
> TaskmanagerTasksTaskidResultGet200Response taskmanagerTasksTaskidResultGet(taskid)

Get task result

Get task result

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskManagerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    TaskManagerApiApi apiInstance = new TaskManagerApiApi(defaultClient);
    Long taskid = 56L; // Long | 
    try {
      TaskmanagerTasksTaskidResultGet200Response result = apiInstance.taskmanagerTasksTaskidResultGet(taskid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskManagerApiApi#taskmanagerTasksTaskidResultGet");
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
| **taskid** | **Long**|  | |

### Return type

[**TaskmanagerTasksTaskidResultGet200Response**](TaskmanagerTasksTaskidResultGet200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="taskmanagerTasksTaskidStatusGet"></a>
# **taskmanagerTasksTaskidStatusGet**
> TaskmanagerTasksTaskidStatusGet200Response taskmanagerTasksTaskidStatusGet(taskid)

Get task status

Get task status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskManagerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    TaskManagerApiApi apiInstance = new TaskManagerApiApi(defaultClient);
    Long taskid = 56L; // Long | 
    try {
      TaskmanagerTasksTaskidStatusGet200Response result = apiInstance.taskmanagerTasksTaskidStatusGet(taskid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskManagerApiApi#taskmanagerTasksTaskidStatusGet");
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
| **taskid** | **Long**|  | |

### Return type

[**TaskmanagerTasksTaskidStatusGet200Response**](TaskmanagerTasksTaskidStatusGet200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

<a id="taskmanagerTasksTaskidTradesGet"></a>
# **taskmanagerTasksTaskidTradesGet**
> List&lt;BacktestTrade&gt; taskmanagerTasksTaskidTradesGet(taskid)

Get backtest trades list

Get backtest trades list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskManagerApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tradematic.com");
    
    // Configure API key authorization: Secured
    ApiKeyAuth Secured = (ApiKeyAuth) defaultClient.getAuthentication("Secured");
    Secured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Secured.setApiKeyPrefix("Token");

    TaskManagerApiApi apiInstance = new TaskManagerApiApi(defaultClient);
    Long taskid = 56L; // Long | 
    try {
      List<BacktestTrade> result = apiInstance.taskmanagerTasksTaskidTradesGet(taskid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskManagerApiApi#taskmanagerTasksTaskidTradesGet");
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
| **taskid** | **Long**|  | |

### Return type

[**List&lt;BacktestTrade&gt;**](BacktestTrade.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **500** | Error |  -  |

