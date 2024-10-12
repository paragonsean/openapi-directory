# RetirementGoalsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**retirementGoalsDeleteById**](RetirementGoalsApi.md#retirementGoalsDeleteById) | **DELETE** /api/RetirementGoals/{id} |  |
| [**retirementGoalsDeleteByRetirementgoalidId**](RetirementGoalsApi.md#retirementGoalsDeleteByRetirementgoalidId) | **DELETE** /api/RetirementGoals/{retirementGoalId}/Expenses/{id} |  |
| [**retirementGoalsGetById**](RetirementGoalsApi.md#retirementGoalsGetById) | **GET** /api/RetirementGoals/{id} |  |
| [**retirementGoalsGetRetirementExpenseByRetirementgoalidId**](RetirementGoalsApi.md#retirementGoalsGetRetirementExpenseByRetirementgoalidId) | **GET** /api/RetirementGoals/{retirementGoalId}/Expenses/{id} |  |
| [**retirementGoalsGetRetirementExpensesByRetirementGoalIdByRetirementgoalid**](RetirementGoalsApi.md#retirementGoalsGetRetirementExpensesByRetirementGoalIdByRetirementgoalid) | **GET** /api/RetirementGoals/{retirementGoalId}/Expenses |  |
| [**retirementGoalsGetRetirementGoalsByFactFinderIdByFactfinderid**](RetirementGoalsApi.md#retirementGoalsGetRetirementGoalsByFactFinderIdByFactfinderid) | **GET** /api/RetirementGoals |  |
| [**retirementGoalsPostByModel**](RetirementGoalsApi.md#retirementGoalsPostByModel) | **POST** /api/RetirementGoals |  |
| [**retirementGoalsPostByRetirementgoalidModel**](RetirementGoalsApi.md#retirementGoalsPostByRetirementgoalidModel) | **POST** /api/RetirementGoals/{retirementGoalId}/Expenses |  |
| [**retirementGoalsPutByIdModel**](RetirementGoalsApi.md#retirementGoalsPutByIdModel) | **PUT** /api/RetirementGoals/{id} |  |
| [**retirementGoalsPutByRetirementgoalidIdModel**](RetirementGoalsApi.md#retirementGoalsPutByRetirementgoalidIdModel) | **PUT** /api/RetirementGoals/{retirementGoalId}/Expenses/{id} |  |


<a id="retirementGoalsDeleteById"></a>
# **retirementGoalsDeleteById**
> retirementGoalsDeleteById(id)



Description: The operation removes a Retirement Goal tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Retirement Goal from a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetirementGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    RetirementGoalsApi apiInstance = new RetirementGoalsApi(defaultClient);
    Integer id = 56; // Integer | The Retirement Goal ID used to identify which Retirement Goal to remove
    try {
      apiInstance.retirementGoalsDeleteById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetirementGoalsApi#retirementGoalsDeleteById");
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
| **id** | **Integer**| The Retirement Goal ID used to identify which Retirement Goal to remove | |

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
| **401** | Unauthorized for Retirement Goal data access. |  -  |
| **403** | Request is restricted for access to Retirement Goal. |  -  |
| **404** | Retirement Goal not found. |  -  |

<a id="retirementGoalsDeleteByRetirementgoalidId"></a>
# **retirementGoalsDeleteByRetirementgoalidId**
> retirementGoalsDeleteByRetirementgoalidId(retirementGoalId, id)



Description: The operation removes a Retirement Goal Expense tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Retirement Goal Expense from a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetirementGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    RetirementGoalsApi apiInstance = new RetirementGoalsApi(defaultClient);
    Integer retirementGoalId = 56; // Integer | The Retirement Goal ID used to locate the Goal to delete the Retirement Goal Expense under
    Integer id = 56; // Integer | The Retirement Goal Expense ID used to identify which Retirement Goal Expense to remove
    try {
      apiInstance.retirementGoalsDeleteByRetirementgoalidId(retirementGoalId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetirementGoalsApi#retirementGoalsDeleteByRetirementgoalidId");
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
| **retirementGoalId** | **Integer**| The Retirement Goal ID used to locate the Goal to delete the Retirement Goal Expense under | |
| **id** | **Integer**| The Retirement Goal Expense ID used to identify which Retirement Goal Expense to remove | |

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
| **401** | Unauthorized for Retirement Goal Expense data access. |  -  |
| **403** | Request is restricted for access to Retirement Goal Expense. |  -  |
| **404** | Retirement Goal Expense not found. |  -  |

<a id="retirementGoalsGetById"></a>
# **retirementGoalsGetById**
> RetirementGoalWithIdModel retirementGoalsGetById(id)



Description: This operation retrieves a single Retirement Goal for the specified Retirement Goal ID.&lt;br /&gt;                Purpose: Provides access to the Retirement Goal including retirement date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetirementGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    RetirementGoalsApi apiInstance = new RetirementGoalsApi(defaultClient);
    Integer id = 56; // Integer | The ID of the Retirement Goal used to retreive the Retirement Goal
    try {
      RetirementGoalWithIdModel result = apiInstance.retirementGoalsGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetirementGoalsApi#retirementGoalsGetById");
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
| **id** | **Integer**| The ID of the Retirement Goal used to retreive the Retirement Goal | |

### Return type

[**RetirementGoalWithIdModel**](RetirementGoalWithIdModel.md)

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
| **401** | Unauthorized for Retirement Goal data access. |  -  |
| **403** | Request is restricted for access to Retirement Goal. |  -  |
| **404** | Retirement Goal not found. |  -  |

<a id="retirementGoalsGetRetirementExpenseByRetirementgoalidId"></a>
# **retirementGoalsGetRetirementExpenseByRetirementgoalidId**
> RetirementExpenseWithIdModel retirementGoalsGetRetirementExpenseByRetirementgoalidId(retirementGoalId, id)



Description: This operation retrieves a single Retirement Goal Expense for the specified Retirement Goal Expense ID.&lt;br /&gt;                Purpose: Provides access to the Retirement Goal Expense including description and amount.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetirementGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    RetirementGoalsApi apiInstance = new RetirementGoalsApi(defaultClient);
    Integer retirementGoalId = 56; // Integer | The ID of the Retirement Goal used to retrieve the Retirement Goal Expense
    Integer id = 56; // Integer | The ID of the Retirement Goal Expense used to retreive the Retirement Goal Expense
    try {
      RetirementExpenseWithIdModel result = apiInstance.retirementGoalsGetRetirementExpenseByRetirementgoalidId(retirementGoalId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetirementGoalsApi#retirementGoalsGetRetirementExpenseByRetirementgoalidId");
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
| **retirementGoalId** | **Integer**| The ID of the Retirement Goal used to retrieve the Retirement Goal Expense | |
| **id** | **Integer**| The ID of the Retirement Goal Expense used to retreive the Retirement Goal Expense | |

### Return type

[**RetirementExpenseWithIdModel**](RetirementExpenseWithIdModel.md)

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
| **401** | Unauthorized for Retirement Goal Expense data access. |  -  |
| **403** | Request is restricted for access to Retirement Goal Expense. |  -  |
| **404** | Retirement Goal Expense not found. |  -  |

<a id="retirementGoalsGetRetirementExpensesByRetirementGoalIdByRetirementgoalid"></a>
# **retirementGoalsGetRetirementExpensesByRetirementGoalIdByRetirementgoalid**
> RetirementExpensesModel retirementGoalsGetRetirementExpensesByRetirementGoalIdByRetirementgoalid(retirementGoalId)



Description: This operation retrieves all Retirement Goal Expenses for the specified Retirement Goal ID.&lt;br /&gt;                Purpose: Provides access to the Retirement Goal Expenses including description and amount.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetirementGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    RetirementGoalsApi apiInstance = new RetirementGoalsApi(defaultClient);
    Integer retirementGoalId = 56; // Integer | The ID of the Retirement Goal used to retrieve Retirement Goal Expenses
    try {
      RetirementExpensesModel result = apiInstance.retirementGoalsGetRetirementExpensesByRetirementGoalIdByRetirementgoalid(retirementGoalId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetirementGoalsApi#retirementGoalsGetRetirementExpensesByRetirementGoalIdByRetirementgoalid");
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
| **retirementGoalId** | **Integer**| The ID of the Retirement Goal used to retrieve Retirement Goal Expenses | |

### Return type

[**RetirementExpensesModel**](RetirementExpensesModel.md)

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
| **401** | Unauthorized for Retirement Goal Expense data access. |  -  |
| **403** | Request is restricted for access to Retirement Goal Expense. |  -  |
| **404** | Retirement Goal Expense not found. |  -  |

<a id="retirementGoalsGetRetirementGoalsByFactFinderIdByFactfinderid"></a>
# **retirementGoalsGetRetirementGoalsByFactFinderIdByFactfinderid**
> RetirementGoalsModel retirementGoalsGetRetirementGoalsByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Retirement Goals for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Retirement Goals including retirement date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetirementGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    RetirementGoalsApi apiInstance = new RetirementGoalsApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Retirement Goals
    try {
      RetirementGoalsModel result = apiInstance.retirementGoalsGetRetirementGoalsByFactFinderIdByFactfinderid(factFinderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetirementGoalsApi#retirementGoalsGetRetirementGoalsByFactFinderIdByFactfinderid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve Retirement Goals | |

### Return type

[**RetirementGoalsModel**](RetirementGoalsModel.md)

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
| **401** | Unauthorized for Retirement Goal data access. |  -  |
| **403** | Request is restricted for access to Retirement Goal. |  -  |
| **404** | Retirement Goal not found. |  -  |

<a id="retirementGoalsPostByModel"></a>
# **retirementGoalsPostByModel**
> RetirementGoalWithIdModel retirementGoalsPostByModel(model)



Description: The operation creates a Retirement Goal.&lt;br /&gt;                Purpose: Allows for creation of Retirement Goals on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetirementGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    RetirementGoalsApi apiInstance = new RetirementGoalsApi(defaultClient);
    RetirementGoalModel model = new RetirementGoalModel(); // RetirementGoalModel | The Retirement Goal to be added to the Fact Finder
    try {
      RetirementGoalWithIdModel result = apiInstance.retirementGoalsPostByModel(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetirementGoalsApi#retirementGoalsPostByModel");
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
| **model** | [**RetirementGoalModel**](RetirementGoalModel.md)| The Retirement Goal to be added to the Fact Finder | |

### Return type

[**RetirementGoalWithIdModel**](RetirementGoalWithIdModel.md)

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
| **401** | Unauthorized for Retirement Goal data access. |  -  |
| **403** | Request is restricted for access to Retirement Goal. |  -  |
| **404** | Retirement Goal not found. |  -  |

<a id="retirementGoalsPostByRetirementgoalidModel"></a>
# **retirementGoalsPostByRetirementgoalidModel**
> RetirementExpenseWithIdModel retirementGoalsPostByRetirementgoalidModel(retirementGoalId, model)



Description: The operation creates a Retirement Goal Expense.&lt;br /&gt;                Purpose: Allows for creation of Retirement Goal Expenses on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetirementGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    RetirementGoalsApi apiInstance = new RetirementGoalsApi(defaultClient);
    Integer retirementGoalId = 56; // Integer | The ID of the Retirement Goal to add the Retirement Goal Expense to
    RetirementExpenseModel model = new RetirementExpenseModel(); // RetirementExpenseModel | The Retirement Goal Expense to be added to the Fact Finder
    try {
      RetirementExpenseWithIdModel result = apiInstance.retirementGoalsPostByRetirementgoalidModel(retirementGoalId, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetirementGoalsApi#retirementGoalsPostByRetirementgoalidModel");
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
| **retirementGoalId** | **Integer**| The ID of the Retirement Goal to add the Retirement Goal Expense to | |
| **model** | [**RetirementExpenseModel**](RetirementExpenseModel.md)| The Retirement Goal Expense to be added to the Fact Finder | |

### Return type

[**RetirementExpenseWithIdModel**](RetirementExpenseWithIdModel.md)

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
| **401** | Unauthorized for Retirement Goal Expense data access. |  -  |
| **403** | Request is restricted for access to Retirement Goal Expense. |  -  |
| **404** | Retirement Goal Expense not found. |  -  |

<a id="retirementGoalsPutByIdModel"></a>
# **retirementGoalsPutByIdModel**
> RetirementGoalWithIdModel retirementGoalsPutByIdModel(id, model)



Description: The operation updates a Retirement Goal.&lt;br /&gt;                Purpose: Allows for complete replacement of a Retirement Goal on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetirementGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    RetirementGoalsApi apiInstance = new RetirementGoalsApi(defaultClient);
    Integer id = 56; // Integer | The existing Retirement Goal ID used to identify which Retirement Goal to update
    RetirementGoalModel model = new RetirementGoalModel(); // RetirementGoalModel | The Retirement Goal to be updated on a Fact Finder
    try {
      RetirementGoalWithIdModel result = apiInstance.retirementGoalsPutByIdModel(id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetirementGoalsApi#retirementGoalsPutByIdModel");
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
| **id** | **Integer**| The existing Retirement Goal ID used to identify which Retirement Goal to update | |
| **model** | [**RetirementGoalModel**](RetirementGoalModel.md)| The Retirement Goal to be updated on a Fact Finder | |

### Return type

[**RetirementGoalWithIdModel**](RetirementGoalWithIdModel.md)

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
| **401** | Unauthorized for Retirement Goal data access. |  -  |
| **403** | Request is restricted for access to Retirement Goal. |  -  |
| **404** | Retirement Goal not found. |  -  |

<a id="retirementGoalsPutByRetirementgoalidIdModel"></a>
# **retirementGoalsPutByRetirementgoalidIdModel**
> RetirementExpenseWithIdModel retirementGoalsPutByRetirementgoalidIdModel(retirementGoalId, id, model)



Description: The operation updates a Retirement Goal Expense.&lt;br /&gt;                Purpose: Allows for complete replacement of a Retirement Goal Expense on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetirementGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    RetirementGoalsApi apiInstance = new RetirementGoalsApi(defaultClient);
    Integer retirementGoalId = 56; // Integer | The Retirement Goal ID used to locate the Goal to update the Retirement Goal Expense under
    Integer id = 56; // Integer | The existing Retirement Goal Expense ID used to identify which Retirement Goal Expense to update
    RetirementExpenseModel model = new RetirementExpenseModel(); // RetirementExpenseModel | The Retirement Goal Expense to be updated on a Fact Finder
    try {
      RetirementExpenseWithIdModel result = apiInstance.retirementGoalsPutByRetirementgoalidIdModel(retirementGoalId, id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetirementGoalsApi#retirementGoalsPutByRetirementgoalidIdModel");
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
| **retirementGoalId** | **Integer**| The Retirement Goal ID used to locate the Goal to update the Retirement Goal Expense under | |
| **id** | **Integer**| The existing Retirement Goal Expense ID used to identify which Retirement Goal Expense to update | |
| **model** | [**RetirementExpenseModel**](RetirementExpenseModel.md)| The Retirement Goal Expense to be updated on a Fact Finder | |

### Return type

[**RetirementExpenseWithIdModel**](RetirementExpenseWithIdModel.md)

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
| **401** | Unauthorized for Retirement Goal Expense data access. |  -  |
| **403** | Request is restricted for access to Retirement Goal Expense. |  -  |
| **404** | Retirement Goal Expense not found. |  -  |

