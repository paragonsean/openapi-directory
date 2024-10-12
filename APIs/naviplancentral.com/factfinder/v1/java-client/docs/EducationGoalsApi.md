# EducationGoalsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**educationGoalsDeleteByEducationgoalidId**](EducationGoalsApi.md#educationGoalsDeleteByEducationgoalidId) | **DELETE** /api/EducationGoals/{educationGoalId}/Expenses/{id} |  |
| [**educationGoalsDeleteById**](EducationGoalsApi.md#educationGoalsDeleteById) | **DELETE** /api/EducationGoals/{id} |  |
| [**educationGoalsGetById**](EducationGoalsApi.md#educationGoalsGetById) | **GET** /api/EducationGoals/{id} |  |
| [**educationGoalsGetEducationExpenseByEducationgoalidId**](EducationGoalsApi.md#educationGoalsGetEducationExpenseByEducationgoalidId) | **GET** /api/EducationGoals/{educationGoalId}/Expenses/{id} |  |
| [**educationGoalsGetEducationExpensesByEducationGoalIdByEducationgoalid**](EducationGoalsApi.md#educationGoalsGetEducationExpensesByEducationGoalIdByEducationgoalid) | **GET** /api/EducationGoals/{educationGoalId}/Expenses |  |
| [**educationGoalsGetEducationGoalsByFactFinderIdByFactfinderid**](EducationGoalsApi.md#educationGoalsGetEducationGoalsByFactFinderIdByFactfinderid) | **GET** /api/EducationGoals |  |
| [**educationGoalsPostByEducationgoalidModel**](EducationGoalsApi.md#educationGoalsPostByEducationgoalidModel) | **POST** /api/EducationGoals/{educationGoalId}/Expenses |  |
| [**educationGoalsPostByModel**](EducationGoalsApi.md#educationGoalsPostByModel) | **POST** /api/EducationGoals |  |
| [**educationGoalsPutByEducationgoalidIdModel**](EducationGoalsApi.md#educationGoalsPutByEducationgoalidIdModel) | **PUT** /api/EducationGoals/{educationGoalId}/Expenses/{id} |  |
| [**educationGoalsPutByIdModel**](EducationGoalsApi.md#educationGoalsPutByIdModel) | **PUT** /api/EducationGoals/{id} |  |


<a id="educationGoalsDeleteByEducationgoalidId"></a>
# **educationGoalsDeleteByEducationgoalidId**
> educationGoalsDeleteByEducationgoalidId(educationGoalId, id)



Description: The operation removes an Education Goal Expense tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of an Education Goal Expense from a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EducationGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    EducationGoalsApi apiInstance = new EducationGoalsApi(defaultClient);
    Integer educationGoalId = 56; // Integer | The Education Goal ID used to locate the Goal to delete the Expense under
    Integer id = 56; // Integer | The Education Goal Expense ID used to identify which Education Goal Expense to remove
    try {
      apiInstance.educationGoalsDeleteByEducationgoalidId(educationGoalId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling EducationGoalsApi#educationGoalsDeleteByEducationgoalidId");
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
| **educationGoalId** | **Integer**| The Education Goal ID used to locate the Goal to delete the Expense under | |
| **id** | **Integer**| The Education Goal Expense ID used to identify which Education Goal Expense to remove | |

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
| **401** | Unauthorized for Education Goal Expense data access. |  -  |
| **403** | Request is restricted for access to Education Goal Expense. |  -  |
| **404** | Education Goal Expense not found. |  -  |

<a id="educationGoalsDeleteById"></a>
# **educationGoalsDeleteById**
> educationGoalsDeleteById(id)



Description: The operation removes an Education Goal tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of an Education Goal from a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EducationGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    EducationGoalsApi apiInstance = new EducationGoalsApi(defaultClient);
    Integer id = 56; // Integer | The Education Goal ID used to identify which Education Goal to remove
    try {
      apiInstance.educationGoalsDeleteById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling EducationGoalsApi#educationGoalsDeleteById");
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
| **id** | **Integer**| The Education Goal ID used to identify which Education Goal to remove | |

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
| **401** | Unauthorized for Education Goal data access. |  -  |
| **403** | Request is restricted for access to Education Goal. |  -  |
| **404** | Education Goal not found. |  -  |

<a id="educationGoalsGetById"></a>
# **educationGoalsGetById**
> EducationGoalWithIdModel educationGoalsGetById(id)



Description: This operation retrieves a single Education Goal for the specified Education Goal ID.&lt;br /&gt;                Purpose: Provides access to the Education Goal including description and projected cost.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EducationGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    EducationGoalsApi apiInstance = new EducationGoalsApi(defaultClient);
    Integer id = 56; // Integer | The ID of the Education Goal used to retreive the Education Goal
    try {
      EducationGoalWithIdModel result = apiInstance.educationGoalsGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EducationGoalsApi#educationGoalsGetById");
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
| **id** | **Integer**| The ID of the Education Goal used to retreive the Education Goal | |

### Return type

[**EducationGoalWithIdModel**](EducationGoalWithIdModel.md)

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
| **401** | Unauthorized for Education Goal data access. |  -  |
| **403** | Request is restricted for access to Education Goal. |  -  |
| **404** | Education Goal not found. |  -  |

<a id="educationGoalsGetEducationExpenseByEducationgoalidId"></a>
# **educationGoalsGetEducationExpenseByEducationgoalidId**
> EducationExpenseWithIdModel educationGoalsGetEducationExpenseByEducationgoalidId(educationGoalId, id)



Description: This operation retrieves a single Education Goal Expense for the specified Education Goal Expense ID.&lt;br /&gt;                Purpose: Provides access to the Education Goal Expense including description and annual cost.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EducationGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    EducationGoalsApi apiInstance = new EducationGoalsApi(defaultClient);
    Integer educationGoalId = 56; // Integer | The ID of the Education Goal used to retrieve Education Goal Expenses
    Integer id = 56; // Integer | The ID of the Education Goal Expense used to retreive the Education Goal Expense
    try {
      EducationExpenseWithIdModel result = apiInstance.educationGoalsGetEducationExpenseByEducationgoalidId(educationGoalId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EducationGoalsApi#educationGoalsGetEducationExpenseByEducationgoalidId");
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
| **educationGoalId** | **Integer**| The ID of the Education Goal used to retrieve Education Goal Expenses | |
| **id** | **Integer**| The ID of the Education Goal Expense used to retreive the Education Goal Expense | |

### Return type

[**EducationExpenseWithIdModel**](EducationExpenseWithIdModel.md)

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
| **401** | Unauthorized for Education Goal Expense data access. |  -  |
| **403** | Request is restricted for access to Education Goal Expense. |  -  |
| **404** | Education Goal Expense not found. |  -  |

<a id="educationGoalsGetEducationExpensesByEducationGoalIdByEducationgoalid"></a>
# **educationGoalsGetEducationExpensesByEducationGoalIdByEducationgoalid**
> EducationExpensesModel educationGoalsGetEducationExpensesByEducationGoalIdByEducationgoalid(educationGoalId)



Description: This operation retrieves all Education Goal Expenses for the specified Education Goal ID.&lt;br /&gt;                Purpose: Provides access to the Education Goal Expenses including description and annual cost.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EducationGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    EducationGoalsApi apiInstance = new EducationGoalsApi(defaultClient);
    Integer educationGoalId = 56; // Integer | The ID of the Education Goal used to retrieve Education Goal Expenses
    try {
      EducationExpensesModel result = apiInstance.educationGoalsGetEducationExpensesByEducationGoalIdByEducationgoalid(educationGoalId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EducationGoalsApi#educationGoalsGetEducationExpensesByEducationGoalIdByEducationgoalid");
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
| **educationGoalId** | **Integer**| The ID of the Education Goal used to retrieve Education Goal Expenses | |

### Return type

[**EducationExpensesModel**](EducationExpensesModel.md)

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
| **401** | Unauthorized for Education Goal Expense data access. |  -  |
| **403** | Request is restricted for access to Education Goal Expense. |  -  |
| **404** | Education Goal Expense not found. |  -  |

<a id="educationGoalsGetEducationGoalsByFactFinderIdByFactfinderid"></a>
# **educationGoalsGetEducationGoalsByFactFinderIdByFactfinderid**
> EducationGoalsModel educationGoalsGetEducationGoalsByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Education Goals for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Education Goals including description and projected cost.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EducationGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    EducationGoalsApi apiInstance = new EducationGoalsApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Education Goals
    try {
      EducationGoalsModel result = apiInstance.educationGoalsGetEducationGoalsByFactFinderIdByFactfinderid(factFinderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EducationGoalsApi#educationGoalsGetEducationGoalsByFactFinderIdByFactfinderid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve Education Goals | |

### Return type

[**EducationGoalsModel**](EducationGoalsModel.md)

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
| **401** | Unauthorized for Education Goal data access. |  -  |
| **403** | Request is restricted for access to Education Goal. |  -  |
| **404** | Education Goal not found. |  -  |

<a id="educationGoalsPostByEducationgoalidModel"></a>
# **educationGoalsPostByEducationgoalidModel**
> EducationExpenseWithIdModel educationGoalsPostByEducationgoalidModel(educationGoalId, model)



Description: The operation creates an Education Goal Expense.&lt;br /&gt;                Purpose: Allows for creation of Education Goal Expenses on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EducationGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    EducationGoalsApi apiInstance = new EducationGoalsApi(defaultClient);
    Integer educationGoalId = 56; // Integer | The Education Goal ID used to locate the Goal to add the expense to
    EducationExpenseModel model = new EducationExpenseModel(); // EducationExpenseModel | The Education Goal Expense to be added to the Fact Finder
    try {
      EducationExpenseWithIdModel result = apiInstance.educationGoalsPostByEducationgoalidModel(educationGoalId, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EducationGoalsApi#educationGoalsPostByEducationgoalidModel");
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
| **educationGoalId** | **Integer**| The Education Goal ID used to locate the Goal to add the expense to | |
| **model** | [**EducationExpenseModel**](EducationExpenseModel.md)| The Education Goal Expense to be added to the Fact Finder | |

### Return type

[**EducationExpenseWithIdModel**](EducationExpenseWithIdModel.md)

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
| **401** | Unauthorized for Education Goal Expense data access. |  -  |
| **403** | Request is restricted for access to Education Goal Expense. |  -  |
| **404** | Education Goal Expense not found. |  -  |

<a id="educationGoalsPostByModel"></a>
# **educationGoalsPostByModel**
> EducationGoalWithIdModel educationGoalsPostByModel(model)



Description: The operation creates an Education Goal.&lt;br /&gt;                Purpose: Allows for creation of Education Goals on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EducationGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    EducationGoalsApi apiInstance = new EducationGoalsApi(defaultClient);
    EducationGoalModel model = new EducationGoalModel(); // EducationGoalModel | The Education Goal to be added to the Fact Finder
    try {
      EducationGoalWithIdModel result = apiInstance.educationGoalsPostByModel(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EducationGoalsApi#educationGoalsPostByModel");
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
| **model** | [**EducationGoalModel**](EducationGoalModel.md)| The Education Goal to be added to the Fact Finder | |

### Return type

[**EducationGoalWithIdModel**](EducationGoalWithIdModel.md)

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
| **401** | Unauthorized for Education Goal data access. |  -  |
| **403** | Request is restricted for access to Education Goal. |  -  |
| **404** | Education Goal not found. |  -  |

<a id="educationGoalsPutByEducationgoalidIdModel"></a>
# **educationGoalsPutByEducationgoalidIdModel**
> EducationExpenseWithIdModel educationGoalsPutByEducationgoalidIdModel(educationGoalId, id, model)



Description: The operation updates an Education Goal Expense.&lt;br /&gt;                Purpose: Allows for complete replacement of an Education Goal Expense on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EducationGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    EducationGoalsApi apiInstance = new EducationGoalsApi(defaultClient);
    Integer educationGoalId = 56; // Integer | The Education Goal ID used to locate the Goal to update the Expense under
    Integer id = 56; // Integer | The existing Education Goal Expense ID used to identify which Education Goal Expense to update
    EducationExpenseModel model = new EducationExpenseModel(); // EducationExpenseModel | The Education Goal Expense to be added to the Fact Finder
    try {
      EducationExpenseWithIdModel result = apiInstance.educationGoalsPutByEducationgoalidIdModel(educationGoalId, id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EducationGoalsApi#educationGoalsPutByEducationgoalidIdModel");
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
| **educationGoalId** | **Integer**| The Education Goal ID used to locate the Goal to update the Expense under | |
| **id** | **Integer**| The existing Education Goal Expense ID used to identify which Education Goal Expense to update | |
| **model** | [**EducationExpenseModel**](EducationExpenseModel.md)| The Education Goal Expense to be added to the Fact Finder | |

### Return type

[**EducationExpenseWithIdModel**](EducationExpenseWithIdModel.md)

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
| **401** | Unauthorized for Education Goal Expense data access. |  -  |
| **403** | Request is restricted for access to Education Goal Expense. |  -  |
| **404** | Education Goal Expense not found. |  -  |

<a id="educationGoalsPutByIdModel"></a>
# **educationGoalsPutByIdModel**
> EducationGoalWithIdModel educationGoalsPutByIdModel(id, model)



Description: The operation creates an Education Goal Expense.&lt;br /&gt;                Purpose: Allows for creation of Education Goal Expenses on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EducationGoalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    EducationGoalsApi apiInstance = new EducationGoalsApi(defaultClient);
    Integer id = 56; // Integer | The Education Goal ID used to locate the Goal to add the Expense to
    EducationGoalModel model = new EducationGoalModel(); // EducationGoalModel | The Education Goal Expense to be added to the Fact Finder
    try {
      EducationGoalWithIdModel result = apiInstance.educationGoalsPutByIdModel(id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EducationGoalsApi#educationGoalsPutByIdModel");
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
| **id** | **Integer**| The Education Goal ID used to locate the Goal to add the Expense to | |
| **model** | [**EducationGoalModel**](EducationGoalModel.md)| The Education Goal Expense to be added to the Fact Finder | |

### Return type

[**EducationGoalWithIdModel**](EducationGoalWithIdModel.md)

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
| **401** | Unauthorized for Education Goal Expense data access. |  -  |
| **403** | Request is restricted for access to Education Goal Expense. |  -  |
| **404** | Education Goal Expense not found. |  -  |

