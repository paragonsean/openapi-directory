# ProjectsDeleteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**keywordsDeleteProjectKeyword**](ProjectsDeleteApi.md#keywordsDeleteProjectKeyword) | **DELETE** /v1/projects/{projectGuid}/keywords/{guid} | Delete a keyword from the project |
| [**phaseMembersDeletePhaseMember**](ProjectsDeleteApi.md#phaseMembersDeletePhaseMember) | **DELETE** /v1/phasemembers/{userGuid} | Deletes a phase member |
| [**phasesDeletePhase**](ProjectsDeleteApi.md#phasesDeletePhase) | **DELETE** /v1/phases/{guid} | Deletes a phase |
| [**projectCustomValuesDeleteProjectCustomValue**](ProjectsDeleteApi.md#projectCustomValuesDeleteProjectCustomValue) | **DELETE** /v1/projects/customvalues/{guid} | Deletes a project custom value. |
| [**projectForecastsDeleteForecast**](ProjectsDeleteApi.md#projectForecastsDeleteForecast) | **DELETE** /v1/projectforecasts/{guid} | Delete a project forecast |
| [**projectForecastsDeleteForecasts**](ProjectsDeleteApi.md#projectForecastsDeleteForecasts) | **DELETE** /v1/projects/{projectGuid}/projectforecasts | Delete the project forecasts from a month onward, including the given month. |
| [**projectInvoiceSettingsDeleteProjectInvoiceSettings_0**](ProjectsDeleteApi.md#projectInvoiceSettingsDeleteProjectInvoiceSettings_0) | **DELETE** /v1/projectinvoicesettings/{guid} | Delete an project invoice settings. |
| [**projectProductsDeleteAllProjectProducts**](ProjectsDeleteApi.md#projectProductsDeleteAllProjectProducts) | **DELETE** /v1/projects/{projectGuid}/projectproducts | Deletes all project products of a project. |
| [**projectProductsDeleteProjectProduct**](ProjectsDeleteApi.md#projectProductsDeleteProjectProduct) | **DELETE** /v1/projectproducts/{guid} | Deletes a project product. |
| [**projectWorkHourPricesDeleteProjectWorkHourPrice**](ProjectsDeleteApi.md#projectWorkHourPricesDeleteProjectWorkHourPrice) | **DELETE** /v1/projectworkhourprices/{guid} | Deletes a work hour price |
| [**projectWorkTypesDeleteProjectWorktype**](ProjectsDeleteApi.md#projectWorkTypesDeleteProjectWorktype) | **DELETE** /v1/projectworktypes/{guid} | Deletes a project work type. |
| [**projectsDeleteProject**](ProjectsDeleteApi.md#projectsDeleteProject) | **DELETE** /v1/projects/{guid} | Delete a project |
| [**proposalFeesDeleteProposalFee**](ProjectsDeleteApi.md#proposalFeesDeleteProposalFee) | **DELETE** /v1/proposalfeerows/{guid} | Delete a proposal fee row |
| [**proposalSubtotalsDeleteProposalSubtotal**](ProjectsDeleteApi.md#proposalSubtotalsDeleteProposalSubtotal) | **DELETE** /v1/proposalsubtotals/{guid} | Delete a proposal subtotal |
| [**proposalWorkhoursDeleteProposalWorkhour**](ProjectsDeleteApi.md#proposalWorkhoursDeleteProposalWorkhour) | **DELETE** /v1/proposalworkrows/{guid} | Delete a proposal work row. |
| [**proposalsDeleteProposal**](ProjectsDeleteApi.md#proposalsDeleteProposal) | **DELETE** /v1/proposals/{guid} | Delete a proposal |
| [**salesNotesDeleteProjectSalesNote**](ProjectsDeleteApi.md#salesNotesDeleteProjectSalesNote) | **DELETE** /v1/projectsalesnotes/{guid} | Deletes a project sales note. |


<a id="keywordsDeleteProjectKeyword"></a>
# **keywordsDeleteProjectKeyword**
> keywordsDeleteProjectKeyword(projectGuid, guid)

Delete a keyword from the project

Returns: No Content (204) if succeeded. Not found (404) if the keyword or the link can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsDeleteApi;

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

    ProjectsDeleteApi apiInstance = new ProjectsDeleteApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | 
    String guid = "guid_example"; // String | 
    try {
      apiInstance.keywordsDeleteProjectKeyword(projectGuid, guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsDeleteApi#keywordsDeleteProjectKeyword");
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
| **projectGuid** | **String**|  | |
| **guid** | **String**|  | |

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

<a id="phaseMembersDeletePhaseMember"></a>
# **phaseMembersDeletePhaseMember**
> phaseMembersDeletePhaseMember(userGuid, resourceAllocationAction, transferToUserGuid, phaseMemberModel)

Deletes a phase member

Returns: No Content (204) if succeeded. Only one of transferToRoleGuid and transferToUserGuid can be provided. Use root phase to delete a project member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsDeleteApi;

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

    ProjectsDeleteApi apiInstance = new ProjectsDeleteApi(defaultClient);
    String userGuid = "userGuid_example"; // String | GUID of the phase member to remove
    ResourceAllocationAction resourceAllocationAction = ResourceAllocationAction.fromValue("None"); // ResourceAllocationAction | Optional: The action to be applied to the user's resource allocations
    String transferToUserGuid = "transferToUserGuid_example"; // String | Optional: GUID of the user to whom the resource allocations are transferred.
    PhaseMemberModel phaseMemberModel = new PhaseMemberModel(); // PhaseMemberModel | 
    try {
      apiInstance.phaseMembersDeletePhaseMember(userGuid, resourceAllocationAction, transferToUserGuid, phaseMemberModel);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsDeleteApi#phaseMembersDeletePhaseMember");
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
| **userGuid** | **String**| GUID of the phase member to remove | |
| **resourceAllocationAction** | [**ResourceAllocationAction**](.md)| Optional: The action to be applied to the user&#39;s resource allocations | [optional] [enum: None, Delete, Transfer] |
| **transferToUserGuid** | **String**| Optional: GUID of the user to whom the resource allocations are transferred. | [optional] |
| **phaseMemberModel** | [**PhaseMemberModel**](PhaseMemberModel.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="phasesDeletePhase"></a>
# **phasesDeletePhase**
> phasesDeletePhase(guid)

Deletes a phase

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsDeleteApi;

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

    ProjectsDeleteApi apiInstance = new ProjectsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the phase.
    try {
      apiInstance.phasesDeletePhase(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsDeleteApi#phasesDeletePhase");
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
| **guid** | **String**| GUID used to delete the phase. | |

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

<a id="projectCustomValuesDeleteProjectCustomValue"></a>
# **projectCustomValuesDeleteProjectCustomValue**
> projectCustomValuesDeleteProjectCustomValue(guid)

Deletes a project custom value.

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsDeleteApi;

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

    ProjectsDeleteApi apiInstance = new ProjectsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the project custom value.
    try {
      apiInstance.projectCustomValuesDeleteProjectCustomValue(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsDeleteApi#projectCustomValuesDeleteProjectCustomValue");
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
| **guid** | **String**| GUID used to delete the project custom value. | |

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
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectForecastsDeleteForecast"></a>
# **projectForecastsDeleteForecast**
> projectForecastsDeleteForecast(guid)

Delete a project forecast

Returns: No Content (204) if succeeded. Not found (404) if product can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsDeleteApi;

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

    ProjectsDeleteApi apiInstance = new ProjectsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the project forecast to delete
    try {
      apiInstance.projectForecastsDeleteForecast(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsDeleteApi#projectForecastsDeleteForecast");
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
| **guid** | **String**| ID for the project forecast to delete | |

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

<a id="projectForecastsDeleteForecasts"></a>
# **projectForecastsDeleteForecasts**
> projectForecastsDeleteForecasts(projectGuid, year, month)

Delete the project forecasts from a month onward, including the given month.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsDeleteApi;

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

    ProjectsDeleteApi apiInstance = new ProjectsDeleteApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | Project for the forecasts to delete
    Integer year = 56; // Integer | Year where to start deleting the forecasts
    Integer month = 56; // Integer | Month where to start deleting the forecasts
    try {
      apiInstance.projectForecastsDeleteForecasts(projectGuid, year, month);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsDeleteApi#projectForecastsDeleteForecasts");
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
| **projectGuid** | **String**| Project for the forecasts to delete | |
| **year** | **Integer**| Year where to start deleting the forecasts | [optional] |
| **month** | **Integer**| Month where to start deleting the forecasts | [optional] |

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
| **204** | List of project forecasts. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectInvoiceSettingsDeleteProjectInvoiceSettings_0"></a>
# **projectInvoiceSettingsDeleteProjectInvoiceSettings_0**
> projectInvoiceSettingsDeleteProjectInvoiceSettings_0(guid)

Delete an project invoice settings.

Returns: No Content (204) if succeeded. Not found (404) if project invoice settings can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsDeleteApi;

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

    ProjectsDeleteApi apiInstance = new ProjectsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the project invoice settings to delete.
    try {
      apiInstance.projectInvoiceSettingsDeleteProjectInvoiceSettings_0(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsDeleteApi#projectInvoiceSettingsDeleteProjectInvoiceSettings_0");
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
| **guid** | **String**| ID for the project invoice settings to delete. | |

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

<a id="projectProductsDeleteAllProjectProducts"></a>
# **projectProductsDeleteAllProjectProducts**
> projectProductsDeleteAllProjectProducts(projectGuid)

Deletes all project products of a project.

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsDeleteApi;

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

    ProjectsDeleteApi apiInstance = new ProjectsDeleteApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | GUID of the project from where project products to remove.
    try {
      apiInstance.projectProductsDeleteAllProjectProducts(projectGuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsDeleteApi#projectProductsDeleteAllProjectProducts");
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
| **projectGuid** | **String**| GUID of the project from where project products to remove. | |

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

<a id="projectProductsDeleteProjectProduct"></a>
# **projectProductsDeleteProjectProduct**
> projectProductsDeleteProjectProduct(guid)

Deletes a project product.

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsDeleteApi;

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

    ProjectsDeleteApi apiInstance = new ProjectsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID of the project product to remove.
    try {
      apiInstance.projectProductsDeleteProjectProduct(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsDeleteApi#projectProductsDeleteProjectProduct");
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
| **guid** | **String**| GUID of the project product to remove. | |

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

<a id="projectWorkHourPricesDeleteProjectWorkHourPrice"></a>
# **projectWorkHourPricesDeleteProjectWorkHourPrice**
> projectWorkHourPricesDeleteProjectWorkHourPrice(guid)

Deletes a work hour price

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsDeleteApi;

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

    ProjectsDeleteApi apiInstance = new ProjectsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the work hour price.
    try {
      apiInstance.projectWorkHourPricesDeleteProjectWorkHourPrice(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsDeleteApi#projectWorkHourPricesDeleteProjectWorkHourPrice");
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
| **guid** | **String**| GUID used to delete the work hour price. | |

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

<a id="projectWorkTypesDeleteProjectWorktype"></a>
# **projectWorkTypesDeleteProjectWorktype**
> projectWorkTypesDeleteProjectWorktype(guid)

Deletes a project work type.

Returns: No Content (204) if succeeded. The \&quot;UseWorktypesFromSetting\&quot; flag for the Project should be false (the project should not use the organization list of work types).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsDeleteApi;

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

    ProjectsDeleteApi apiInstance = new ProjectsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID of the project work type to remove.
    try {
      apiInstance.projectWorkTypesDeleteProjectWorktype(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsDeleteApi#projectWorkTypesDeleteProjectWorktype");
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
| **guid** | **String**| GUID of the project work type to remove. | |

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

<a id="projectsDeleteProject"></a>
# **projectsDeleteProject**
> projectsDeleteProject(guid)

Delete a project

Returns: No Content (204) if succeeded. Not found (404) if project can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsDeleteApi;

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

    ProjectsDeleteApi apiInstance = new ProjectsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the project to delete
    try {
      apiInstance.projectsDeleteProject(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsDeleteApi#projectsDeleteProject");
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
| **guid** | **String**| ID for the project to delete | |

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

<a id="proposalFeesDeleteProposalFee"></a>
# **proposalFeesDeleteProposalFee**
> proposalFeesDeleteProposalFee(guid)

Delete a proposal fee row

Returns: No Content (204) if succeeded. Not found (404) if proposal fee row can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsDeleteApi;

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

    ProjectsDeleteApi apiInstance = new ProjectsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the proposal fee row to delete
    try {
      apiInstance.proposalFeesDeleteProposalFee(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsDeleteApi#proposalFeesDeleteProposalFee");
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
| **guid** | **String**| ID for the proposal fee row to delete | |

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
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalSubtotalsDeleteProposalSubtotal"></a>
# **proposalSubtotalsDeleteProposalSubtotal**
> proposalSubtotalsDeleteProposalSubtotal(guid)

Delete a proposal subtotal

Returns: No Content (204) if succeeded. Not found (404) if proposal subtotal can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsDeleteApi;

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

    ProjectsDeleteApi apiInstance = new ProjectsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the proposal subtotal to delete.
    try {
      apiInstance.proposalSubtotalsDeleteProposalSubtotal(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsDeleteApi#proposalSubtotalsDeleteProposalSubtotal");
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
| **guid** | **String**| ID for the proposal subtotal to delete. | |

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
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalWorkhoursDeleteProposalWorkhour"></a>
# **proposalWorkhoursDeleteProposalWorkhour**
> proposalWorkhoursDeleteProposalWorkhour(guid)

Delete a proposal work row.

Returns: No Content (204) if succeeded. Not found (404) if proposal work row can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsDeleteApi;

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

    ProjectsDeleteApi apiInstance = new ProjectsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the proposal work row to delete.
    try {
      apiInstance.proposalWorkhoursDeleteProposalWorkhour(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsDeleteApi#proposalWorkhoursDeleteProposalWorkhour");
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
| **guid** | **String**| ID for the proposal work row to delete. | |

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
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalsDeleteProposal"></a>
# **proposalsDeleteProposal**
> proposalsDeleteProposal(guid)

Delete a proposal

Returns: No Content (204) if succeeded. Not found (404) if proposal can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsDeleteApi;

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

    ProjectsDeleteApi apiInstance = new ProjectsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | Guid for the proposal to delete
    try {
      apiInstance.proposalsDeleteProposal(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsDeleteApi#proposalsDeleteProposal");
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
| **guid** | **String**| Guid for the proposal to delete | |

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

<a id="salesNotesDeleteProjectSalesNote"></a>
# **salesNotesDeleteProjectSalesNote**
> salesNotesDeleteProjectSalesNote(guid)

Deletes a project sales note.

Returns: No Content (204) if succeeded. OK (200) if note has child notes and can&#39;t be deleted. It is marked as IsDeleted &#x3D; true. Not found (404) if note can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsDeleteApi;

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

    ProjectsDeleteApi apiInstance = new ProjectsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the project sales note.
    try {
      apiInstance.salesNotesDeleteProjectSalesNote(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsDeleteApi#salesNotesDeleteProjectSalesNote");
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
| **guid** | **String**| GUID used to delete the project sales note. | |

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

