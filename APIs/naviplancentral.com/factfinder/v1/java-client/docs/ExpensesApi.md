# ExpensesApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expensesDeleteById**](ExpensesApi.md#expensesDeleteById) | **DELETE** /api/Expenses/{id} |  |
| [**expensesGetById**](ExpensesApi.md#expensesGetById) | **GET** /api/Expenses/{id} |  |
| [**expensesGetExpensesByFactFinderIdByFactfinderid**](ExpensesApi.md#expensesGetExpensesByFactFinderIdByFactfinderid) | **GET** /api/Expenses |  |
| [**expensesPostByModel**](ExpensesApi.md#expensesPostByModel) | **POST** /api/Expenses |  |
| [**expensesPutByIdModel**](ExpensesApi.md#expensesPutByIdModel) | **PUT** /api/Expenses/{id} |  |


<a id="expensesDeleteById"></a>
# **expensesDeleteById**
> expensesDeleteById(id)



Description: The operation removes an Expense tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of an Expense from a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    ExpensesApi apiInstance = new ExpensesApi(defaultClient);
    Integer id = 56; // Integer | The Expense ID used to identify which Expense to remove
    try {
      apiInstance.expensesDeleteById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpensesApi#expensesDeleteById");
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
| **id** | **Integer**| The Expense ID used to identify which Expense to remove | |

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
| **401** | Unauthorized for Expense data access. |  -  |
| **403** | Request is restricted for access to Expense. |  -  |
| **404** | Expense not found. |  -  |

<a id="expensesGetById"></a>
# **expensesGetById**
> ExpenseWithIdModel expensesGetById(id)



Description: This operation retrieves a single Expense for the specified Expense ID.&lt;br /&gt;                Purpose: Provides access to the Expense including description and Expense type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    ExpensesApi apiInstance = new ExpensesApi(defaultClient);
    Integer id = 56; // Integer | The ID of the Expense used to retreive the Expense
    try {
      ExpenseWithIdModel result = apiInstance.expensesGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpensesApi#expensesGetById");
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
| **id** | **Integer**| The ID of the Expense used to retreive the Expense | |

### Return type

[**ExpenseWithIdModel**](ExpenseWithIdModel.md)

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
| **401** | Unauthorized for Expense data access. |  -  |
| **403** | Request is restricted for access to Expense. |  -  |
| **404** | Expense not found. |  -  |

<a id="expensesGetExpensesByFactFinderIdByFactfinderid"></a>
# **expensesGetExpensesByFactFinderIdByFactfinderid**
> ExpensesModel expensesGetExpensesByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Expenses for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Expenses including description and Expense type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    ExpensesApi apiInstance = new ExpensesApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Expenses
    try {
      ExpensesModel result = apiInstance.expensesGetExpensesByFactFinderIdByFactfinderid(factFinderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpensesApi#expensesGetExpensesByFactFinderIdByFactfinderid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve Expenses | |

### Return type

[**ExpensesModel**](ExpensesModel.md)

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
| **401** | Unauthorized for Expense data access. |  -  |
| **403** | Request is restricted for access to Expense. |  -  |
| **404** | Expense not found. |  -  |

<a id="expensesPostByModel"></a>
# **expensesPostByModel**
> ExpenseWithIdModel expensesPostByModel(model)



Description: The operation creates an Expense.&lt;br /&gt;                Purpose: Allows for creation of Expenses on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    ExpensesApi apiInstance = new ExpensesApi(defaultClient);
    ExpenseModel model = new ExpenseModel(); // ExpenseModel | The Expense to be added to the Fact Finder
    try {
      ExpenseWithIdModel result = apiInstance.expensesPostByModel(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpensesApi#expensesPostByModel");
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
| **model** | [**ExpenseModel**](ExpenseModel.md)| The Expense to be added to the Fact Finder | |

### Return type

[**ExpenseWithIdModel**](ExpenseWithIdModel.md)

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
| **401** | Unauthorized for Expense data access. |  -  |
| **403** | Request is restricted for access to Expense. |  -  |
| **404** | Expense not found. |  -  |

<a id="expensesPutByIdModel"></a>
# **expensesPutByIdModel**
> ExpenseWithIdModel expensesPutByIdModel(id, model)



Description: The operation updates an Expense.&lt;br /&gt;                Purpose: Allows for complete replacement of an Expense on a Fact Finder. &lt;br /&gt;&lt;br /&gt;                Note: Expense type cannot be changed for expenses prepopulated from NaviPlan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpensesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    ExpensesApi apiInstance = new ExpensesApi(defaultClient);
    Integer id = 56; // Integer | The existing Expense ID used to identify which Expense to update
    ExpenseModel model = new ExpenseModel(); // ExpenseModel | The Expense to be updated on a Fact Finder
    try {
      ExpenseWithIdModel result = apiInstance.expensesPutByIdModel(id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpensesApi#expensesPutByIdModel");
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
| **id** | **Integer**| The existing Expense ID used to identify which Expense to update | |
| **model** | [**ExpenseModel**](ExpenseModel.md)| The Expense to be updated on a Fact Finder | |

### Return type

[**ExpenseWithIdModel**](ExpenseWithIdModel.md)

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
| **401** | Unauthorized for Expense data access. |  -  |
| **403** | Request is restricted for access to Expense. |  -  |
| **404** | Expense not found. |  -  |

