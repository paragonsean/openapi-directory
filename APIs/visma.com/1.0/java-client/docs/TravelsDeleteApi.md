# TravelsDeleteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**projectTravelExpensesDeleteProjectTravelExpense**](TravelsDeleteApi.md#projectTravelExpensesDeleteProjectTravelExpense) | **DELETE** /v1/projecttravelexpenses/{guid} | Deletes a project travel expense. |
| [**travelReimbursementsDeleteTravelReimbursement**](TravelsDeleteApi.md#travelReimbursementsDeleteTravelReimbursement) | **DELETE** /v1/travelreimbursements/{guid} | Delete a travel reimbursement |


<a id="projectTravelExpensesDeleteProjectTravelExpense"></a>
# **projectTravelExpensesDeleteProjectTravelExpense**
> projectTravelExpensesDeleteProjectTravelExpense(guid)

Deletes a project travel expense.

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TravelsDeleteApi;

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

    TravelsDeleteApi apiInstance = new TravelsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the project travel expense.
    try {
      apiInstance.projectTravelExpensesDeleteProjectTravelExpense(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling TravelsDeleteApi#projectTravelExpensesDeleteProjectTravelExpense");
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
| **guid** | **String**| GUID used to delete the project travel expense. | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="travelReimbursementsDeleteTravelReimbursement"></a>
# **travelReimbursementsDeleteTravelReimbursement**
> travelReimbursementsDeleteTravelReimbursement(guid)

Delete a travel reimbursement

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TravelsDeleteApi;

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

    TravelsDeleteApi apiInstance = new TravelsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID of travel reimbursement
    try {
      apiInstance.travelReimbursementsDeleteTravelReimbursement(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling TravelsDeleteApi#travelReimbursementsDeleteTravelReimbursement");
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
| **guid** | **String**| GUID of travel reimbursement | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content (204) if succeeded. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

