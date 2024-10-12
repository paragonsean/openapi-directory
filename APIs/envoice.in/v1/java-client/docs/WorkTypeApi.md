# WorkTypeApi

All URIs are relative to *https://www.envoice.in*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workTypeApiAll**](WorkTypeApi.md#workTypeApiAll) | **GET** /api/worktype/all | Return all work types for the account |
| [**workTypeApiDelete**](WorkTypeApi.md#workTypeApiDelete) | **POST** /api/worktype/delete | Delete an existing work type |
| [**workTypeApiDetails**](WorkTypeApi.md#workTypeApiDetails) | **GET** /api/worktype/details | Return work type details |
| [**workTypeApiNew**](WorkTypeApi.md#workTypeApiNew) | **POST** /api/worktype/new | Create a work type |
| [**workTypeApiSearch**](WorkTypeApi.md#workTypeApiSearch) | **GET** /api/worktype/search | Return all work types for the account that match the query param |
| [**workTypeApiUpdate**](WorkTypeApi.md#workTypeApiUpdate) | **POST** /api/worktype/update | Update an existing work type |


<a id="workTypeApiAll"></a>
# **workTypeApiAll**
> List&lt;WorkTypeDetailsApiModel&gt; workTypeApiAll(xAuthKey, xAuthSecret)

Return all work types for the account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    WorkTypeApi apiInstance = new WorkTypeApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    try {
      List<WorkTypeDetailsApiModel> result = apiInstance.workTypeApiAll(xAuthKey, xAuthSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkTypeApi#workTypeApiAll");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |

### Return type

[**List&lt;WorkTypeDetailsApiModel&gt;**](WorkTypeDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="workTypeApiDelete"></a>
# **workTypeApiDelete**
> Integer workTypeApiDelete(xAuthKey, xAuthSecret, workTypeDeleteApiModel)

Delete an existing work type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    WorkTypeApi apiInstance = new WorkTypeApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    WorkTypeDeleteApiModel workTypeDeleteApiModel = new WorkTypeDeleteApiModel(); // WorkTypeDeleteApiModel | 
    try {
      Integer result = apiInstance.workTypeApiDelete(xAuthKey, xAuthSecret, workTypeDeleteApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkTypeApi#workTypeApiDelete");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **workTypeDeleteApiModel** | [**WorkTypeDeleteApiModel**](WorkTypeDeleteApiModel.md)|  | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="workTypeApiDetails"></a>
# **workTypeApiDetails**
> WorkTypeDetailsApiModel workTypeApiDetails(workTypeId, xAuthKey, xAuthSecret)

Return work type details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    WorkTypeApi apiInstance = new WorkTypeApi(defaultClient);
    Integer workTypeId = 56; // Integer | 
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    try {
      WorkTypeDetailsApiModel result = apiInstance.workTypeApiDetails(workTypeId, xAuthKey, xAuthSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkTypeApi#workTypeApiDetails");
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
| **workTypeId** | **Integer**|  | |
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |

### Return type

[**WorkTypeDetailsApiModel**](WorkTypeDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="workTypeApiNew"></a>
# **workTypeApiNew**
> Integer workTypeApiNew(xAuthKey, xAuthSecret, workTypeCreateApiModel)

Create a work type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    WorkTypeApi apiInstance = new WorkTypeApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    WorkTypeCreateApiModel workTypeCreateApiModel = new WorkTypeCreateApiModel(); // WorkTypeCreateApiModel | 
    try {
      Integer result = apiInstance.workTypeApiNew(xAuthKey, xAuthSecret, workTypeCreateApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkTypeApi#workTypeApiNew");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **workTypeCreateApiModel** | [**WorkTypeCreateApiModel**](WorkTypeCreateApiModel.md)|  | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="workTypeApiSearch"></a>
# **workTypeApiSearch**
> List&lt;WorkTypeDetailsApiModel&gt; workTypeApiSearch(xAuthKey, xAuthSecret, queryOptionsQuery, queryOptionsOrderBy, queryOptionsOrder, queryOptionsPage, queryOptionsPageSize)

Return all work types for the account that match the query param

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    WorkTypeApi apiInstance = new WorkTypeApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    String queryOptionsQuery = "queryOptionsQuery_example"; // String | 
    String queryOptionsOrderBy = "queryOptionsOrderBy_example"; // String | 
    String queryOptionsOrder = "None"; // String | 
    Integer queryOptionsPage = 56; // Integer | 
    Integer queryOptionsPageSize = 56; // Integer | 
    try {
      List<WorkTypeDetailsApiModel> result = apiInstance.workTypeApiSearch(xAuthKey, xAuthSecret, queryOptionsQuery, queryOptionsOrderBy, queryOptionsOrder, queryOptionsPage, queryOptionsPageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkTypeApi#workTypeApiSearch");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **queryOptionsQuery** | **String**|  | [optional] |
| **queryOptionsOrderBy** | **String**|  | [optional] |
| **queryOptionsOrder** | **String**|  | [optional] [enum: None, Asc, Desc] |
| **queryOptionsPage** | **Integer**|  | [optional] |
| **queryOptionsPageSize** | **Integer**|  | [optional] |

### Return type

[**List&lt;WorkTypeDetailsApiModel&gt;**](WorkTypeDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="workTypeApiUpdate"></a>
# **workTypeApiUpdate**
> workTypeApiUpdate(xAuthKey, xAuthSecret, workTypeUpdateApiModel)

Update an existing work type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    WorkTypeApi apiInstance = new WorkTypeApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    WorkTypeUpdateApiModel workTypeUpdateApiModel = new WorkTypeUpdateApiModel(); // WorkTypeUpdateApiModel | 
    try {
      apiInstance.workTypeApiUpdate(xAuthKey, xAuthSecret, workTypeUpdateApiModel);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkTypeApi#workTypeApiUpdate");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **workTypeUpdateApiModel** | [**WorkTypeUpdateApiModel**](WorkTypeUpdateApiModel.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

