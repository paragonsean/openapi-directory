# TravelsWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**projectTravelExpensesPatchProjectTravelExpense**](TravelsWriteApi.md#projectTravelExpensesPatchProjectTravelExpense) | **PATCH** /v1/projecttravelexpenses/{guid} | Update (Patch) a project travel expense or a part of it. |
| [**projectTravelExpensesPostProjectTravelExpense**](TravelsWriteApi.md#projectTravelExpensesPostProjectTravelExpense) | **POST** /v1/projecttravelexpenses | Insert a project travel expense. |
| [**travelReimbursementsPatchTravelReimbursement**](TravelsWriteApi.md#travelReimbursementsPatchTravelReimbursement) | **PATCH** /v1/travelreimbursements/{guid} | Update (Patch) a travel reimbursement |
| [**travelReimbursementsPostTravelReimbursement**](TravelsWriteApi.md#travelReimbursementsPostTravelReimbursement) | **POST** /v1/travelreimbursements | Add a travel reimbursement |


<a id="projectTravelExpensesPatchProjectTravelExpense"></a>
# **projectTravelExpensesPatchProjectTravelExpense**
> List&lt;ProjectTravelExpenseOutputModel&gt; projectTravelExpensesPatchProjectTravelExpense(guid, patchOperation)

Update (Patch) a project travel expense or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TravelsWriteApi;

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

    TravelsWriteApi apiInstance = new TravelsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the project travel expense.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of ProjectTravelExpenseInputModel.
    try {
      List<ProjectTravelExpenseOutputModel> result = apiInstance.projectTravelExpensesPatchProjectTravelExpense(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TravelsWriteApi#projectTravelExpensesPatchProjectTravelExpense");
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
| **guid** | **String**| ID of the project travel expense. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of ProjectTravelExpenseInputModel. | [optional] |

### Return type

[**List&lt;ProjectTravelExpenseOutputModel&gt;**](ProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated project travel expenses. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectTravelExpensesPostProjectTravelExpense"></a>
# **projectTravelExpensesPostProjectTravelExpense**
> ProjectTravelExpenseOutputModel projectTravelExpensesPostProjectTravelExpense(projectTravelExpenseInputModel)

Insert a project travel expense.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TravelsWriteApi;

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

    TravelsWriteApi apiInstance = new TravelsWriteApi(defaultClient);
    ProjectTravelExpenseInputModel projectTravelExpenseInputModel = new ProjectTravelExpenseInputModel(); // ProjectTravelExpenseInputModel | ProjectTravelExpenseInputModel.
    try {
      ProjectTravelExpenseOutputModel result = apiInstance.projectTravelExpensesPostProjectTravelExpense(projectTravelExpenseInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TravelsWriteApi#projectTravelExpensesPostProjectTravelExpense");
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
| **projectTravelExpenseInputModel** | [**ProjectTravelExpenseInputModel**](ProjectTravelExpenseInputModel.md)| ProjectTravelExpenseInputModel. | [optional] |

### Return type

[**ProjectTravelExpenseOutputModel**](ProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created project travel expense. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="travelReimbursementsPatchTravelReimbursement"></a>
# **travelReimbursementsPatchTravelReimbursement**
> List&lt;TravelReimbursementOutputModel&gt; travelReimbursementsPatchTravelReimbursement(guid, patchOperation)

Update (Patch) a travel reimbursement

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TravelsWriteApi;

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

    TravelsWriteApi apiInstance = new TravelsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the travel reimbursement
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document
    try {
      List<TravelReimbursementOutputModel> result = apiInstance.travelReimbursementsPatchTravelReimbursement(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TravelsWriteApi#travelReimbursementsPatchTravelReimbursement");
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
| **guid** | **String**| ID of the travel reimbursement | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document | [optional] |

### Return type

[**List&lt;TravelReimbursementOutputModel&gt;**](TravelReimbursementOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated travel reimbursement |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="travelReimbursementsPostTravelReimbursement"></a>
# **travelReimbursementsPostTravelReimbursement**
> TravelReimbursementOutputModel travelReimbursementsPostTravelReimbursement(addAllUnreimbursedTravelExpenses, includedProjectTravelExpenses, travelReimbursementInputModel)

Add a travel reimbursement

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TravelsWriteApi;

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

    TravelsWriteApi apiInstance = new TravelsWriteApi(defaultClient);
    Boolean addAllUnreimbursedTravelExpenses = true; // Boolean | Optional: Add all of user's unreimbursed travel expenses to reimbursement. Default is true. If TravelExpenseReimbursementStartDate is given in organization settings, travel expenses are added from that date onwards. If value is false then expenses from includedProjectTravelExpenses list are added.
    List<String> includedProjectTravelExpenses = Arrays.asList(); // List<String> | Optional: A list of included projectTravelExpense GUIDs belonging to the user. If addAllUnreimbursedTravelExpenses is true then this list is ignored.
    TravelReimbursementInputModel travelReimbursementInputModel = new TravelReimbursementInputModel(); // TravelReimbursementInputModel | TravelReimbursementModel
    try {
      TravelReimbursementOutputModel result = apiInstance.travelReimbursementsPostTravelReimbursement(addAllUnreimbursedTravelExpenses, includedProjectTravelExpenses, travelReimbursementInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TravelsWriteApi#travelReimbursementsPostTravelReimbursement");
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
| **addAllUnreimbursedTravelExpenses** | **Boolean**| Optional: Add all of user&#39;s unreimbursed travel expenses to reimbursement. Default is true. If TravelExpenseReimbursementStartDate is given in organization settings, travel expenses are added from that date onwards. If value is false then expenses from includedProjectTravelExpenses list are added. | [optional] [default to true] |
| **includedProjectTravelExpenses** | [**List&lt;String&gt;**](String.md)| Optional: A list of included projectTravelExpense GUIDs belonging to the user. If addAllUnreimbursedTravelExpenses is true then this list is ignored. | [optional] |
| **travelReimbursementInputModel** | [**TravelReimbursementInputModel**](TravelReimbursementInputModel.md)| TravelReimbursementModel | [optional] |

### Return type

[**TravelReimbursementOutputModel**](TravelReimbursementOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Added travel reimbursement |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

