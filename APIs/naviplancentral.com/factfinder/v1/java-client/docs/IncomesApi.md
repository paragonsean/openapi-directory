# IncomesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**incomesDeleteById**](IncomesApi.md#incomesDeleteById) | **DELETE** /api/Incomes/{id} |  |
| [**incomesGetById**](IncomesApi.md#incomesGetById) | **GET** /api/Incomes/{id} |  |
| [**incomesGetIncomesByFactFinderIdByFactfinderid**](IncomesApi.md#incomesGetIncomesByFactFinderIdByFactfinderid) | **GET** /api/Incomes |  |
| [**incomesPostByModel**](IncomesApi.md#incomesPostByModel) | **POST** /api/Incomes |  |
| [**incomesPutByIdModel**](IncomesApi.md#incomesPutByIdModel) | **PUT** /api/Incomes/{id} |  |


<a id="incomesDeleteById"></a>
# **incomesDeleteById**
> incomesDeleteById(id)



Description: The operation removes an Income tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of an Income from a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncomesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    IncomesApi apiInstance = new IncomesApi(defaultClient);
    Integer id = 56; // Integer | The Income ID used to identify which Income to remove
    try {
      apiInstance.incomesDeleteById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncomesApi#incomesDeleteById");
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
| **id** | **Integer**| The Income ID used to identify which Income to remove | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Deleted |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Income data access. |  -  |
| **403** | Request is restricted for access to Income. |  -  |
| **404** | Income not found. |  -  |

<a id="incomesGetById"></a>
# **incomesGetById**
> IncomeWithIdModel incomesGetById(id)



Description: This operation retrieves a single Income for the specified Income ID.&lt;br /&gt;                Purpose: Provides access to the Income including annual amount and start date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncomesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    IncomesApi apiInstance = new IncomesApi(defaultClient);
    Integer id = 56; // Integer | The ID of the Income used to retreive the Income
    try {
      IncomeWithIdModel result = apiInstance.incomesGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncomesApi#incomesGetById");
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
| **id** | **Integer**| The ID of the Income used to retreive the Income | |

### Return type

[**IncomeWithIdModel**](IncomeWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Income data access. |  -  |
| **403** | Request is restricted for access to Income. |  -  |
| **404** | Income not found. |  -  |

<a id="incomesGetIncomesByFactFinderIdByFactfinderid"></a>
# **incomesGetIncomesByFactFinderIdByFactfinderid**
> IncomesModel incomesGetIncomesByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Incomes for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Incomes including annual amount and start date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncomesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    IncomesApi apiInstance = new IncomesApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Incomes
    try {
      IncomesModel result = apiInstance.incomesGetIncomesByFactFinderIdByFactfinderid(factFinderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncomesApi#incomesGetIncomesByFactFinderIdByFactfinderid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve Incomes | |

### Return type

[**IncomesModel**](IncomesModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Income data access. |  -  |
| **403** | Request is restricted for access to Income. |  -  |
| **404** | Income not found. |  -  |

<a id="incomesPostByModel"></a>
# **incomesPostByModel**
> IncomeWithIdModel incomesPostByModel(model)



Description: The operation creates an Income.&lt;br /&gt;                Purpose: Allows for creation of Incomes on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncomesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    IncomesApi apiInstance = new IncomesApi(defaultClient);
    IncomeModel model = new IncomeModel(); // IncomeModel | The Income to be added to the Fact Finder
    try {
      IncomeWithIdModel result = apiInstance.incomesPostByModel(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncomesApi#incomesPostByModel");
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
| **model** | [**IncomeModel**](IncomeModel.md)| The Income to be added to the Fact Finder | |

### Return type

[**IncomeWithIdModel**](IncomeWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Income data access. |  -  |
| **403** | Request is restricted for access to Income. |  -  |
| **404** | Income not found. |  -  |

<a id="incomesPutByIdModel"></a>
# **incomesPutByIdModel**
> IncomeWithIdModel incomesPutByIdModel(id, model)



Description: The operation updates an Income.&lt;br /&gt;                Purpose: Allows for complete replacement of an Income on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncomesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    IncomesApi apiInstance = new IncomesApi(defaultClient);
    Integer id = 56; // Integer | The existing Income ID used to identify which Income to update
    IncomeModel model = new IncomeModel(); // IncomeModel | The Income to be updated on a Fact Finder
    try {
      IncomeWithIdModel result = apiInstance.incomesPutByIdModel(id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncomesApi#incomesPutByIdModel");
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
| **id** | **Integer**| The existing Income ID used to identify which Income to update | |
| **model** | [**IncomeModel**](IncomeModel.md)| The Income to be updated on a Fact Finder | |

### Return type

[**IncomeWithIdModel**](IncomeWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Income data access. |  -  |
| **403** | Request is restricted for access to Income. |  -  |
| **404** | Income not found. |  -  |

