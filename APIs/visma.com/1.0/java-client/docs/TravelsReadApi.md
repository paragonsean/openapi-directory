# TravelsReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**projectTravelExpensesGetDeletedProjectTravelExpenses**](TravelsReadApi.md#projectTravelExpensesGetDeletedProjectTravelExpenses) | **GET** /v1/deletedprojecttravelexpenses | Get the deleted project travel expenses. |
| [**projectTravelExpensesGetProjectTravelExpense**](TravelsReadApi.md#projectTravelExpensesGetProjectTravelExpense) | **GET** /v1/projecttravelexpenses/{guid} | Get project travel expense by ID. |
| [**projectTravelExpensesGetProjectTravelExpenses**](TravelsReadApi.md#projectTravelExpensesGetProjectTravelExpenses) | **GET** /v1/projecttravelexpenses | Get the project travel expenses. |
| [**projectTravelExpensesGetProjectTravelExpensesForProject**](TravelsReadApi.md#projectTravelExpensesGetProjectTravelExpensesForProject) | **GET** /v1/projects/{projectGuid}/projecttravelexpenses | Get all the project travel expenses for a project |
| [**projectTravelExpensesGetProjectTravelExpensesForTravelReimbursement**](TravelsReadApi.md#projectTravelExpensesGetProjectTravelExpensesForTravelReimbursement) | **GET** /v1/travelreimbursements/{travelReimbursementGuid}/projecttravelexpenses | Get all the project travel expenses for a travel reimbursement |
| [**projectTravelExpensesGetProjectTravelExpensesForUser**](TravelsReadApi.md#projectTravelExpensesGetProjectTravelExpensesForUser) | **GET** /v1/users/{userGuid}/projecttravelexpenses | Get all the project travel expenses for a user |
| [**travelReimbursementsGetTravelReimbursement**](TravelsReadApi.md#travelReimbursementsGetTravelReimbursement) | **GET** /v1/travelreimbursements/{guid} | Get travel reimbursement by ID |
| [**travelReimbursementsGetTravelReimbursements**](TravelsReadApi.md#travelReimbursementsGetTravelReimbursements) | **GET** /v1/travelreimbursements | Get travel reimbursements. |


<a id="projectTravelExpensesGetDeletedProjectTravelExpenses"></a>
# **projectTravelExpensesGetDeletedProjectTravelExpenses**
> List&lt;DeletedProjectTravelExpenseModel&gt; projectTravelExpensesGetDeletedProjectTravelExpenses(pageToken, rowCount, projectGuid, userGuid, deletedSince)

Get the deleted project travel expenses.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TravelsReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    TravelsReadApi apiInstance = new TravelsReadApi(defaultClient);
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    List<String> projectGuid = Arrays.asList(); // List<String> | Optional: ID of the project for the deleted project travel expenses to be fetched. If not provided, returns for all projects. Default all.
    List<String> userGuid = Arrays.asList(); // List<String> | Optional: ID of the user. If not provided, returns for all users. Default all.
    OffsetDateTime deletedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get project travel expenses that have been deleted after this date time (greater or equal).
    try {
      List<DeletedProjectTravelExpenseModel> result = apiInstance.projectTravelExpensesGetDeletedProjectTravelExpenses(pageToken, rowCount, projectGuid, userGuid, deletedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TravelsReadApi#projectTravelExpensesGetDeletedProjectTravelExpenses");
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
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **projectGuid** | [**List&lt;String&gt;**](String.md)| Optional: ID of the project for the deleted project travel expenses to be fetched. If not provided, returns for all projects. Default all. | [optional] |
| **userGuid** | [**List&lt;String&gt;**](String.md)| Optional: ID of the user. If not provided, returns for all users. Default all. | [optional] |
| **deletedSince** | **OffsetDateTime**| Optional: Get project travel expenses that have been deleted after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;DeletedProjectTravelExpenseModel&gt;**](DeletedProjectTravelExpenseModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectTravelExpensesGetProjectTravelExpense"></a>
# **projectTravelExpensesGetProjectTravelExpense**
> ProjectTravelExpenseOutputModel projectTravelExpensesGetProjectTravelExpense(guid)

Get project travel expense by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TravelsReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    TravelsReadApi apiInstance = new TravelsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the project travel expense.
    try {
      ProjectTravelExpenseOutputModel result = apiInstance.projectTravelExpensesGetProjectTravelExpense(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TravelsReadApi#projectTravelExpensesGetProjectTravelExpense");
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
| **guid** | **String**| Id used to get the project travel expense. | |

### Return type

[**ProjectTravelExpenseOutputModel**](ProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProjectTravelExpenseOutputModel. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectTravelExpensesGetProjectTravelExpenses"></a>
# **projectTravelExpensesGetProjectTravelExpenses**
> List&lt;ProjectTravelExpenseOutputModel&gt; projectTravelExpensesGetProjectTravelExpenses(pageToken, rowCount, changedSince)

Get the project travel expenses.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TravelsReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    TravelsReadApi apiInstance = new TravelsReadApi(defaultClient);
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get project travel expenses that have been added or changed after this date time (greater or equal).
    try {
      List<ProjectTravelExpenseOutputModel> result = apiInstance.projectTravelExpensesGetProjectTravelExpenses(pageToken, rowCount, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TravelsReadApi#projectTravelExpensesGetProjectTravelExpenses");
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
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get project travel expenses that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;ProjectTravelExpenseOutputModel&gt;**](ProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProjectTravelExpenseOutputModel |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectTravelExpensesGetProjectTravelExpensesForProject"></a>
# **projectTravelExpensesGetProjectTravelExpensesForProject**
> List&lt;ProjectTravelExpenseOutputModel&gt; projectTravelExpensesGetProjectTravelExpensesForProject(projectGuid, isBillable, isBilled, invoiceableDate, pageToken, rowCount, isBillablePeriodInFuture, expenseClass)

Get all the project travel expenses for a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TravelsReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    TravelsReadApi apiInstance = new TravelsReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | ID of the project.
    Boolean isBillable = true; // Boolean | Optional: Filter the travel expenses. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null.
    Boolean isBilled = true; // Boolean | Optional: Filter the travel expenses. If true/false, only the ones that are/are not invoiced are returned. If null, all are returned. Default is null.
    OffsetDateTime invoiceableDate = OffsetDateTime.now(); // OffsetDateTime | Optional: Filter the project fees. When given, only the ones that are invoiceable before or on the given date are returned. Default is null.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    Boolean isBillablePeriodInFuture = true; // Boolean | Optional. Filter the project travel expenses. If true/false, only the ones that will be billable in the future are returned. If null, all are returned. Default is false.
    ExpensesClass expenseClass = ExpensesClass.fromValue("Mileage"); // ExpensesClass | Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense
    try {
      List<ProjectTravelExpenseOutputModel> result = apiInstance.projectTravelExpensesGetProjectTravelExpensesForProject(projectGuid, isBillable, isBilled, invoiceableDate, pageToken, rowCount, isBillablePeriodInFuture, expenseClass);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TravelsReadApi#projectTravelExpensesGetProjectTravelExpensesForProject");
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
| **projectGuid** | **String**| ID of the project. | |
| **isBillable** | **Boolean**| Optional: Filter the travel expenses. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null. | [optional] |
| **isBilled** | **Boolean**| Optional: Filter the travel expenses. If true/false, only the ones that are/are not invoiced are returned. If null, all are returned. Default is null. | [optional] |
| **invoiceableDate** | **OffsetDateTime**| Optional: Filter the project fees. When given, only the ones that are invoiceable before or on the given date are returned. Default is null. | [optional] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **isBillablePeriodInFuture** | **Boolean**| Optional. Filter the project travel expenses. If true/false, only the ones that will be billable in the future are returned. If null, all are returned. Default is false. | [optional] |
| **expenseClass** | [**ExpensesClass**](.md)| Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense | [optional] [enum: Mileage, DailyAllowance, OtherTravelExpense] |

### Return type

[**List&lt;ProjectTravelExpenseOutputModel&gt;**](ProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProjectTravelExpenseOutputModel |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectTravelExpensesGetProjectTravelExpensesForTravelReimbursement"></a>
# **projectTravelExpensesGetProjectTravelExpensesForTravelReimbursement**
> List&lt;ProjectTravelExpenseOutputModel&gt; projectTravelExpensesGetProjectTravelExpensesForTravelReimbursement(travelReimbursementGuid, pageToken, rowCount, expenseClass)

Get all the project travel expenses for a travel reimbursement

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TravelsReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    TravelsReadApi apiInstance = new TravelsReadApi(defaultClient);
    String travelReimbursementGuid = "travelReimbursementGuid_example"; // String | Optional: ID of the travel reimbursement
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    ExpensesClass expenseClass = ExpensesClass.fromValue("Mileage"); // ExpensesClass | Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense
    try {
      List<ProjectTravelExpenseOutputModel> result = apiInstance.projectTravelExpensesGetProjectTravelExpensesForTravelReimbursement(travelReimbursementGuid, pageToken, rowCount, expenseClass);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TravelsReadApi#projectTravelExpensesGetProjectTravelExpensesForTravelReimbursement");
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
| **travelReimbursementGuid** | **String**| Optional: ID of the travel reimbursement | |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **expenseClass** | [**ExpensesClass**](.md)| Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense | [optional] [enum: Mileage, DailyAllowance, OtherTravelExpense] |

### Return type

[**List&lt;ProjectTravelExpenseOutputModel&gt;**](ProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProjectTravelExpenseOutputModel |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectTravelExpensesGetProjectTravelExpensesForUser"></a>
# **projectTravelExpensesGetProjectTravelExpensesForUser**
> List&lt;ProjectTravelExpenseOutputModel&gt; projectTravelExpensesGetProjectTravelExpensesForUser(userGuid, startDate, endDate, pageToken, rowCount, expenseClass, isReimbursed, isTravelReimbursementRequired, travelReimbursementGuid, costCurrencyGuid)

Get all the project travel expenses for a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TravelsReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    TravelsReadApi apiInstance = new TravelsReadApi(defaultClient);
    String userGuid = "userGuid_example"; // String | ID of the user.
    LocalDate startDate = LocalDate.now(); // LocalDate | Optional: starting date from which to get the travel expenses. Default all.
    LocalDate endDate = LocalDate.now(); // LocalDate | Optional: starting date to which to get the travel expenses. Default all.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    ExpensesClass expenseClass = ExpensesClass.fromValue("Mileage"); // ExpensesClass | Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense
    Boolean isReimbursed = true; // Boolean | Optional. Filter the project travel expenses. If true/false, only the ones that are reimbursed are returned. If null, all are returned. Default is null.
    Boolean isTravelReimbursementRequired = true; // Boolean | Optional: Filter the project travel expenses by whether or not the reimbursement is required. Default all.
    String travelReimbursementGuid = "travelReimbursementGuid_example"; // String | Optional: ID of the travel reimbursement
    String costCurrencyGuid = "costCurrencyGuid_example"; // String | Optional: ID of the cost currency.
    try {
      List<ProjectTravelExpenseOutputModel> result = apiInstance.projectTravelExpensesGetProjectTravelExpensesForUser(userGuid, startDate, endDate, pageToken, rowCount, expenseClass, isReimbursed, isTravelReimbursementRequired, travelReimbursementGuid, costCurrencyGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TravelsReadApi#projectTravelExpensesGetProjectTravelExpensesForUser");
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
| **userGuid** | **String**| ID of the user. | |
| **startDate** | **LocalDate**| Optional: starting date from which to get the travel expenses. Default all. | [optional] |
| **endDate** | **LocalDate**| Optional: starting date to which to get the travel expenses. Default all. | [optional] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **expenseClass** | [**ExpensesClass**](.md)| Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense | [optional] [enum: Mileage, DailyAllowance, OtherTravelExpense] |
| **isReimbursed** | **Boolean**| Optional. Filter the project travel expenses. If true/false, only the ones that are reimbursed are returned. If null, all are returned. Default is null. | [optional] |
| **isTravelReimbursementRequired** | **Boolean**| Optional: Filter the project travel expenses by whether or not the reimbursement is required. Default all. | [optional] |
| **travelReimbursementGuid** | **String**| Optional: ID of the travel reimbursement | [optional] |
| **costCurrencyGuid** | **String**| Optional: ID of the cost currency. | [optional] |

### Return type

[**List&lt;ProjectTravelExpenseOutputModel&gt;**](ProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProjectTravelExpenseOutputModel |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="travelReimbursementsGetTravelReimbursement"></a>
# **travelReimbursementsGetTravelReimbursement**
> TravelReimbursementOutputModel travelReimbursementsGetTravelReimbursement(guid)

Get travel reimbursement by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TravelsReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    TravelsReadApi apiInstance = new TravelsReadApi(defaultClient);
    String guid = "guid_example"; // String | ID of travel reimbursement
    try {
      TravelReimbursementOutputModel result = apiInstance.travelReimbursementsGetTravelReimbursement(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TravelsReadApi#travelReimbursementsGetTravelReimbursement");
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
| **guid** | **String**| ID of travel reimbursement | |

### Return type

[**TravelReimbursementOutputModel**](TravelReimbursementOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="travelReimbursementsGetTravelReimbursements"></a>
# **travelReimbursementsGetTravelReimbursements**
> List&lt;TravelReimbursementOutputModel&gt; travelReimbursementsGetTravelReimbursements(pageToken, rowCount, changedSince, travelReimbursementStatusGuids)

Get travel reimbursements.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TravelsReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    TravelsReadApi apiInstance = new TravelsReadApi(defaultClient);
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get travel reimbursements that have been added or changed after this date time (greater or equal).
    List<String> travelReimbursementStatusGuids = Arrays.asList(); // List<String> | Optional: List of travel reimbursement status ids.
    try {
      List<TravelReimbursementOutputModel> result = apiInstance.travelReimbursementsGetTravelReimbursements(pageToken, rowCount, changedSince, travelReimbursementStatusGuids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TravelsReadApi#travelReimbursementsGetTravelReimbursements");
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
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get travel reimbursements that have been added or changed after this date time (greater or equal). | [optional] |
| **travelReimbursementStatusGuids** | [**List&lt;String&gt;**](String.md)| Optional: List of travel reimbursement status ids. | [optional] |

### Return type

[**List&lt;TravelReimbursementOutputModel&gt;**](TravelReimbursementOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

