# ProjectsReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**keywordsGetProjectKeywords**](ProjectsReadApi.md#keywordsGetProjectKeywords) | **GET** /v1/projects/{projectGuid}/keywords | Get all the keywords for project. |
| [**overtimePricesGetOvertimePricesForProject**](ProjectsReadApi.md#overtimePricesGetOvertimePricesForProject) | **GET** /v1/projects/{projectGuid}/overtimeprices | Get all the overtimePrices for a project. |
| [**phaseMembersGetAllDeletedPhaseMembers**](ProjectsReadApi.md#phaseMembersGetAllDeletedPhaseMembers) | **GET** /v1/deletedphasemembers | Get all deleted phase members |
| [**phaseMembersGetAllPhaseMembers**](ProjectsReadApi.md#phaseMembersGetAllPhaseMembers) | **GET** /v1/phasemembers | Get all active phase members |
| [**phaseMembersGetPhaseMembers**](ProjectsReadApi.md#phaseMembersGetPhaseMembers) | **GET** /v1/phases/{phaseGuid}/phasemembers | Get phase members |
| [**phasesGetPhase**](ProjectsReadApi.md#phasesGetPhase) | **GET** /v1/phases/{guid} | Get phase by ID |
| [**phasesGetPhases**](ProjectsReadApi.md#phasesGetPhases) | **GET** /v1/phases | Get the phases. |
| [**phasesGetProjectPhases**](ProjectsReadApi.md#phasesGetProjectPhases) | **GET** /v1/projects/{guid}/phaseswithhierarchy | Get project&#39;s phases as flat list |
| [**phasesGetRootPhases**](ProjectsReadApi.md#phasesGetRootPhases) | **GET** /v1/rootphaseswithhierarchy | Get a list of root phases with information about hierarchy. |
| [**productPricesGetProductPricesForProject**](ProjectsReadApi.md#productPricesGetProductPricesForProject) | **GET** /v1/projects/{projectGuid}/productprices | Get all the productPrices for a project. |
| [**productsGetSearchedProducts**](ProjectsReadApi.md#productsGetSearchedProducts) | **GET** /v1/projects/{projectGuid}/productsforproject | Gets available products for the given project where price information comes from projects price list |
| [**projectBillingCustomersGetWorkHourPricesForProject**](ProjectsReadApi.md#projectBillingCustomersGetWorkHourPricesForProject) | **GET** /v1/projects/{projectGuid}/projectbillingcustomers | Get all the billing customers for a project |
| [**projectCustomValuesGetProjectCustomValue**](ProjectsReadApi.md#projectCustomValuesGetProjectCustomValue) | **GET** /v1/projects/customvalues/{guid} | Get project custom value by ID. |
| [**projectCustomValuesGetProjectCustomValues**](ProjectsReadApi.md#projectCustomValuesGetProjectCustomValues) | **GET** /v1/projects/{projectGuid}/customvalues | Get the project custom values. |
| [**projectForecastsGetForecast**](ProjectsReadApi.md#projectForecastsGetForecast) | **GET** /v1/projectforecasts/{guid} | Get project forecast by ID |
| [**projectForecastsGetForecasts**](ProjectsReadApi.md#projectForecastsGetForecasts) | **GET** /v1/projects/{projectGuid}/projectforecasts | Get the project forecasts |
| [**projectInvoiceSettingsGetProjectInvoiceSetting_0**](ProjectsReadApi.md#projectInvoiceSettingsGetProjectInvoiceSetting_0) | **GET** /v1/projectinvoicesettings/{guid} | Get project invoice settings by ID. |
| [**projectInvoiceSettingsGetProjectInvoiceSettings_0**](ProjectsReadApi.md#projectInvoiceSettingsGetProjectInvoiceSettings_0) | **GET** /v1/projects/{projectGuid}/projectinvoicesettings | Get project invoice settings by project ID. |
| [**projectMemberCostExceptionsGetProjectMemberCostExceptionsForProject**](ProjectsReadApi.md#projectMemberCostExceptionsGetProjectMemberCostExceptionsForProject) | **GET** /v1/projects/{projectGuid}/projectmembercostexceptions | Get all cost exceptions of project members for a project. |
| [**projectProductsGetProjectProducts**](ProjectsReadApi.md#projectProductsGetProjectProducts) | **GET** /v1/projects/{projectGuid}/projectproducts | Get project products |
| [**projectWorkHourPricesGetProjectWorkHourPrice**](ProjectsReadApi.md#projectWorkHourPricesGetProjectWorkHourPrice) | **GET** /v1/projectworkhourprices/{guid} | Get project work hour price by ID |
| [**projectWorkHourPricesGetWorkHourPricesForProject**](ProjectsReadApi.md#projectWorkHourPricesGetWorkHourPricesForProject) | **GET** /v1/projects/{projectGuid}/projectworkhourprices | Get all the work hour prices for a project |
| [**projectWorkTypesGetProjectWorktypes**](ProjectsReadApi.md#projectWorkTypesGetProjectWorktypes) | **GET** /v1/projects/{projectGuid}/projectworktypes | Get project work types. |
| [**projectsGetCustomerProjects**](ProjectsReadApi.md#projectsGetCustomerProjects) | **GET** /v1/customers/{customerGuid}/projects | Get customer&#39;s projects |
| [**projectsGetProject**](ProjectsReadApi.md#projectsGetProject) | **GET** /v1/projects/{guid} | Get project by ID |
| [**projectsGetProjects**](ProjectsReadApi.md#projectsGetProjects) | **GET** /v1/projects | Get all the projects |
| [**projectsGetSalesCases**](ProjectsReadApi.md#projectsGetSalesCases) | **GET** /v1/salescases | Gets the sales cases (sales status is in progress) |
| [**proposalFeesGetProposalFee**](ProjectsReadApi.md#proposalFeesGetProposalFee) | **GET** /v1/proposalfeerows/{guid} | Get the proposal fee rows by guid |
| [**proposalFeesGetProposalFees**](ProjectsReadApi.md#proposalFeesGetProposalFees) | **GET** /v1/proposalfeerows | Get the proposal fee rows. |
| [**proposalFeesGetProposalFeesForProposal**](ProjectsReadApi.md#proposalFeesGetProposalFeesForProposal) | **GET** /v1/proposals/{proposalGuid}/proposalfeerows | Get all the proposal fee rows for a proposal |
| [**proposalSettingsGetProposalSettings**](ProjectsReadApi.md#proposalSettingsGetProposalSettings) | **GET** /v1/proposals/{guid}/proposalsettings | Get settings for a proposal |
| [**proposalSubtotalsGetProposalSubtotal**](ProjectsReadApi.md#proposalSubtotalsGetProposalSubtotal) | **GET** /v1/proposalsubtotals/{guid} | Get Proposal subtotal by ID |
| [**proposalSubtotalsGetProposalSubtotals**](ProjectsReadApi.md#proposalSubtotalsGetProposalSubtotals) | **GET** /v1/proposalsubtotals | Get the proposal subtotals. |
| [**proposalSubtotalsGetProposalSubtotalsForProposal**](ProjectsReadApi.md#proposalSubtotalsGetProposalSubtotalsForProposal) | **GET** /v1/proposals/{proposalGuid}/proposalsubtotals | Get all the proposal subtotals for a proposal |
| [**proposalWorkhoursGetProposalWorkHours**](ProjectsReadApi.md#proposalWorkhoursGetProposalWorkHours) | **GET** /v1/proposalworkrows | Get the proposal work rows. |
| [**proposalWorkhoursGetProposalWorkHoursForProposal**](ProjectsReadApi.md#proposalWorkhoursGetProposalWorkHoursForProposal) | **GET** /v1/proposals/{proposalGuid}/proposalworkrows | Get all the proposal work rows. |
| [**proposalWorkhoursGetProposalWorkhour**](ProjectsReadApi.md#proposalWorkhoursGetProposalWorkhour) | **GET** /v1/proposalworkrows/{guid} | Get the proposal work row by guid. |
| [**proposalsGetProposal**](ProjectsReadApi.md#proposalsGetProposal) | **GET** /v1/proposals/{guid} | Get Proposal by ID |
| [**proposalsGetProposals**](ProjectsReadApi.md#proposalsGetProposals) | **GET** /v1/proposals | Get all the proposals |
| [**proposalsGetProposalsForProject**](ProjectsReadApi.md#proposalsGetProposalsForProject) | **GET** /v1/projects/{projectGuid}/proposals | Get all the proposals for a project |
| [**salesNotesGetAllCustomerSalesNotes**](ProjectsReadApi.md#salesNotesGetAllCustomerSalesNotes) | **GET** /v1/customers/{customerGuid}/salesnotes | Get the sales notes by customer guid. |
| [**salesNotesGetProjectSalesNote**](ProjectsReadApi.md#salesNotesGetProjectSalesNote) | **GET** /v1/projectsalesnotes/{guid} | Get project sales note by ID. |
| [**salesNotesGetProjectSalesNotes**](ProjectsReadApi.md#salesNotesGetProjectSalesNotes) | **GET** /v1/projects/{projectGuid}/projectsalesnotes | Get the sales notes of a case. |
| [**salesStatusHistoryGetSalesStatusHistory**](ProjectsReadApi.md#salesStatusHistoryGetSalesStatusHistory) | **GET** /v1/projects/{projectGuid}/salesstatushistory | Get the sales status history for a project |
| [**teamProductivityGetTeamProductivity**](ProjectsReadApi.md#teamProductivityGetTeamProductivity) | **GET** /v1/projects/{projectGuid}/teamproductivity | Get team productivity of a project. |
| [**travelExpenseTypesGetSearchedTravelExpenseTypes**](ProjectsReadApi.md#travelExpenseTypesGetSearchedTravelExpenseTypes) | **GET** /v1/projects/{projectGuid}/travelexpensetypes | Search active travel expense types of project by part of the name or code. |
| [**travelPricesGetTravelPricesForProject**](ProjectsReadApi.md#travelPricesGetTravelPricesForProject) | **GET** /v1/projects/{projectGuid}/travelprices | Get all the travel prices for a project. |
| [**workTypesGetPhaseWorkTypes**](ProjectsReadApi.md#workTypesGetPhaseWorkTypes) | **GET** /v1/phases/{phaseGuid}/worktypes | Get all work types that are available for a phase (for work hour entry) |
| [**workTypesGetSearchedWorktypes**](ProjectsReadApi.md#workTypesGetSearchedWorktypes) | **GET** /v1/projects/{projectGuid}/worktypesforproject | Search active work types by part of the name or code. |


<a id="keywordsGetProjectKeywords"></a>
# **keywordsGetProjectKeywords**
> List&lt;ProjectKeywordModel&gt; keywordsGetProjectKeywords(projectGuid, active, sortings)

Get all the keywords for project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | ID of the project for which keywords are requested.
    Boolean active = true; // Boolean | If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Keyword&sortings[0].value=Desc\".
    try {
      List<ProjectKeywordModel> result = apiInstance.keywordsGetProjectKeywords(projectGuid, active, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#keywordsGetProjectKeywords");
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
| **projectGuid** | **String**| ID of the project for which keywords are requested. | |
| **active** | **Boolean**| If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords. | [optional] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Keyword&amp;sortings[0].value&#x3D;Desc\&quot;. | [optional] |

### Return type

[**List&lt;ProjectKeywordModel&gt;**](ProjectKeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Keywords. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="overtimePricesGetOvertimePricesForProject"></a>
# **overtimePricesGetOvertimePricesForProject**
> List&lt;OvertimePriceModel&gt; overtimePricesGetOvertimePricesForProject(projectGuid)

Get all the overtimePrices for a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | 
    try {
      List<OvertimePriceModel> result = apiInstance.overtimePricesGetOvertimePricesForProject(projectGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#overtimePricesGetOvertimePricesForProject");
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

### Return type

[**List&lt;OvertimePriceModel&gt;**](OvertimePriceModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Projects. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="phaseMembersGetAllDeletedPhaseMembers"></a>
# **phaseMembersGetAllDeletedPhaseMembers**
> List&lt;DeletedPhaseMemberOutputModel&gt; phaseMembersGetAllDeletedPhaseMembers(deletedSince, pageToken, rowCount, isUserActive)

Get all deleted phase members

Use root phase to get project members.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    OffsetDateTime deletedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get phase members that have been added or changed after this date time (greater or equal).
    String pageToken = "pageToken_example"; // String | Optional: Page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch.
    Boolean isUserActive = true; // Boolean | Optional: Is the user active. Default nothing = all.
    try {
      List<DeletedPhaseMemberOutputModel> result = apiInstance.phaseMembersGetAllDeletedPhaseMembers(deletedSince, pageToken, rowCount, isUserActive);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#phaseMembersGetAllDeletedPhaseMembers");
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
| **deletedSince** | **OffsetDateTime**| Optional: Get phase members that have been added or changed after this date time (greater or equal). | [optional] |
| **pageToken** | **String**| Optional: Page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch. | [optional] |
| **isUserActive** | **Boolean**| Optional: Is the user active. Default nothing &#x3D; all. | [optional] |

### Return type

[**List&lt;DeletedPhaseMemberOutputModel&gt;**](DeletedPhaseMemberOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the phase members |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="phaseMembersGetAllPhaseMembers"></a>
# **phaseMembersGetAllPhaseMembers**
> List&lt;PhaseMemberOutputModel&gt; phaseMembersGetAllPhaseMembers(changedSince, pageToken, rowCount, isUserActive)

Get all active phase members

Use root phase to get project members.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get phase members that have been added or changed after this date time (greater or equal).
    String pageToken = "pageToken_example"; // String | Optional: Page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch.
    Boolean isUserActive = true; // Boolean | Optional: Is the user active. Default nothing = all.
    try {
      List<PhaseMemberOutputModel> result = apiInstance.phaseMembersGetAllPhaseMembers(changedSince, pageToken, rowCount, isUserActive);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#phaseMembersGetAllPhaseMembers");
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
| **changedSince** | **OffsetDateTime**| Optional: Get phase members that have been added or changed after this date time (greater or equal). | [optional] |
| **pageToken** | **String**| Optional: Page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch. | [optional] |
| **isUserActive** | **Boolean**| Optional: Is the user active. Default nothing &#x3D; all. | [optional] |

### Return type

[**List&lt;PhaseMemberOutputModel&gt;**](PhaseMemberOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the phase members |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="phaseMembersGetPhaseMembers"></a>
# **phaseMembersGetPhaseMembers**
> List&lt;PhaseMemberOutputModel&gt; phaseMembersGetPhaseMembers(phaseGuid, pageToken, rowCount, isActive, isUserActive)

Get phase members

Use root phase to get project members.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String phaseGuid = "phaseGuid_example"; // String | GUID of the phase.
    String pageToken = "pageToken_example"; // String | Optional: Page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch.
    Boolean isActive = true; // Boolean | Optional: Is the member active on the phase. Filters only root phase members. Default nothing = all.
    Boolean isUserActive = true; // Boolean | Optional: Is the user active. Default nothing = all.
    try {
      List<PhaseMemberOutputModel> result = apiInstance.phaseMembersGetPhaseMembers(phaseGuid, pageToken, rowCount, isActive, isUserActive);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#phaseMembersGetPhaseMembers");
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
| **phaseGuid** | **String**| GUID of the phase. | |
| **pageToken** | **String**| Optional: Page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch. | [optional] |
| **isActive** | **Boolean**| Optional: Is the member active on the phase. Filters only root phase members. Default nothing &#x3D; all. | [optional] |
| **isUserActive** | **Boolean**| Optional: Is the user active. Default nothing &#x3D; all. | [optional] |

### Return type

[**List&lt;PhaseMemberOutputModel&gt;**](PhaseMemberOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the phase members |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="phasesGetPhase"></a>
# **phasesGetPhase**
> PhaseOutputModel phasesGetPhase(guid)

Get phase by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the phase.
    try {
      PhaseOutputModel result = apiInstance.phasesGetPhase(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#phasesGetPhase");
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
| **guid** | **String**| Id used to get the phase. | |

### Return type

[**PhaseOutputModel**](PhaseOutputModel.md)

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

<a id="phasesGetPhases"></a>
# **phasesGetPhases**
> List&lt;PhaseOutputModel&gt; phasesGetPhases(pageToken, rowCount, changedSince, code, projectGuids)

Get the phases.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get phases that have been added or changed after this date time (greater or equal).
    String code = ""; // String | Optional: Code of the phase.
    List<String> projectGuids = Arrays.asList(); // List<String> | Optional: List of project ids.
    try {
      List<PhaseOutputModel> result = apiInstance.phasesGetPhases(pageToken, rowCount, changedSince, code, projectGuids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#phasesGetPhases");
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
| **changedSince** | **OffsetDateTime**| Optional: Get phases that have been added or changed after this date time (greater or equal). | [optional] |
| **code** | **String**| Optional: Code of the phase. | [optional] [default to ] |
| **projectGuids** | [**List&lt;String&gt;**](String.md)| Optional: List of project ids. | [optional] |

### Return type

[**List&lt;PhaseOutputModel&gt;**](PhaseOutputModel.md)

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

<a id="phasesGetProjectPhases"></a>
# **phasesGetProjectPhases**
> List&lt;PhaseModelWithHierarchyInfo&gt; phasesGetProjectPhases(guid)

Get project&#39;s phases as flat list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id of the project.
    try {
      List<PhaseModelWithHierarchyInfo> result = apiInstance.phasesGetProjectPhases(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#phasesGetProjectPhases");
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
| **guid** | **String**| Id of the project. | |

### Return type

[**List&lt;PhaseModelWithHierarchyInfo&gt;**](PhaseModelWithHierarchyInfo.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the phases for the project |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="phasesGetRootPhases"></a>
# **phasesGetRootPhases**
> List&lt;PhaseOutputModel&gt; phasesGetRootPhases(pageToken, rowCount, customerGuids, projectGuids, projectKeywordGuids, projectStatusTypeGuids, salesPersonGuids, projectOwnerGuids, businessUnitGuids, customerOwnerGuids, salesStatusTypeGuids, openProjects, projectMemberUserGuids)

Get a list of root phases with information about hierarchy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    List<String> customerGuids = Arrays.asList(); // List<String> | 
    List<String> projectGuids = Arrays.asList(); // List<String> | 
    List<String> projectKeywordGuids = Arrays.asList(); // List<String> | 
    List<String> projectStatusTypeGuids = Arrays.asList(); // List<String> | 
    List<String> salesPersonGuids = Arrays.asList(); // List<String> | 
    List<String> projectOwnerGuids = Arrays.asList(); // List<String> | 
    List<String> businessUnitGuids = Arrays.asList(); // List<String> | 
    List<String> customerOwnerGuids = Arrays.asList(); // List<String> | 
    List<String> salesStatusTypeGuids = Arrays.asList(); // List<String> | 
    Boolean openProjects = true; // Boolean | 
    List<String> projectMemberUserGuids = Arrays.asList(); // List<String> | 
    try {
      List<PhaseOutputModel> result = apiInstance.phasesGetRootPhases(pageToken, rowCount, customerGuids, projectGuids, projectKeywordGuids, projectStatusTypeGuids, salesPersonGuids, projectOwnerGuids, businessUnitGuids, customerOwnerGuids, salesStatusTypeGuids, openProjects, projectMemberUserGuids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#phasesGetRootPhases");
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
| **customerGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **projectGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **projectKeywordGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **projectStatusTypeGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **salesPersonGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **projectOwnerGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **businessUnitGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **customerOwnerGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **salesStatusTypeGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **openProjects** | **Boolean**|  | [optional] |
| **projectMemberUserGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |

### Return type

[**List&lt;PhaseOutputModel&gt;**](PhaseOutputModel.md)

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

<a id="productPricesGetProductPricesForProject"></a>
# **productPricesGetProductPricesForProject**
> List&lt;ProductPriceOutputModel&gt; productPricesGetProductPricesForProject(projectGuid, fromPricelistOnly, firstRow, rowCount, textToSearch, calculateRowCount, isAvailable, productCode, productGuids, isVolumePriced, productCategoryGuids, productTypes)

Get all the productPrices for a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | ID of the project.
    Boolean fromPricelistOnly = false; // Boolean | If true return only prices from the price list, if false also returns prices from the products. Default is false.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from Product name.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate the number of total rows. Default false = total row count is returned as zero.
    Boolean isAvailable = true; // Boolean | Optional: If true, returns only prices that are available for the project, false returns price that are not available. Default all.
    String productCode = ""; // String | Optional: Absolute search for products with specified product code.
    List<String> productGuids = Arrays.asList(); // List<String> | Optional: Search all product price(s) by products guid(s).
    Boolean isVolumePriced = true; // Boolean | Optional: If true, return only volume priced products. If false, return all non volume priced products. Default is null, which means return all products.
    List<String> productCategoryGuids = Arrays.asList(); // List<String> | Optional: Search product prices according to product category / categories by product category guid(s).
    List<ProductType> productTypes = Arrays.asList(); // List<ProductType> | Optional: Search product prices according to product type / types.
    try {
      List<ProductPriceOutputModel> result = apiInstance.productPricesGetProductPricesForProject(projectGuid, fromPricelistOnly, firstRow, rowCount, textToSearch, calculateRowCount, isAvailable, productCode, productGuids, isVolumePriced, productCategoryGuids, productTypes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#productPricesGetProductPricesForProject");
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
| **fromPricelistOnly** | **Boolean**| If true return only prices from the price list, if false also returns prices from the products. Default is false. | [optional] [default to false] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from Product name. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate the number of total rows. Default false &#x3D; total row count is returned as zero. | [optional] [default to false] |
| **isAvailable** | **Boolean**| Optional: If true, returns only prices that are available for the project, false returns price that are not available. Default all. | [optional] |
| **productCode** | **String**| Optional: Absolute search for products with specified product code. | [optional] [default to ] |
| **productGuids** | [**List&lt;String&gt;**](String.md)| Optional: Search all product price(s) by products guid(s). | [optional] |
| **isVolumePriced** | **Boolean**| Optional: If true, return only volume priced products. If false, return all non volume priced products. Default is null, which means return all products. | [optional] |
| **productCategoryGuids** | [**List&lt;String&gt;**](String.md)| Optional: Search product prices according to product category / categories by product category guid(s). | [optional] |
| **productTypes** | [**List&lt;ProductType&gt;**](ProductType.md)| Optional: Search product prices according to product type / types. | [optional] |

### Return type

[**List&lt;ProductPriceOutputModel&gt;**](ProductPriceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Projects. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="productsGetSearchedProducts"></a>
# **productsGetSearchedProducts**
> List&lt;ProductForProjectOutputModel&gt; productsGetSearchedProducts(projectGuid, rowCount, pageToken, type, includeProductsFromRegistry)

Gets available products for the given project where price information comes from projects price list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | Id of the project
    Integer rowCount = 56; // Integer | Optional: Number of rows to fetch
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    ProductType type = ProductType.fromValue("FixedFees"); // ProductType | Product type. if given, it filters the products by the given type
    Boolean includeProductsFromRegistry = false; // Boolean | Optional: If true returns all the products from registry with project specific prices. If false returns only products specified for the project with project specific prices. Default false.
    try {
      List<ProductForProjectOutputModel> result = apiInstance.productsGetSearchedProducts(projectGuid, rowCount, pageToken, type, includeProductsFromRegistry);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#productsGetSearchedProducts");
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
| **projectGuid** | **String**| Id of the project | |
| **rowCount** | **Integer**| Optional: Number of rows to fetch | [optional] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **type** | [**ProductType**](.md)| Product type. if given, it filters the products by the given type | [optional] [enum: FixedFees, Materials, Subcontracting] |
| **includeProductsFromRegistry** | **Boolean**| Optional: If true returns all the products from registry with project specific prices. If false returns only products specified for the project with project specific prices. Default false. | [optional] [default to false] |

### Return type

[**List&lt;ProductForProjectOutputModel&gt;**](ProductForProjectOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the Products matching search criteria |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectBillingCustomersGetWorkHourPricesForProject"></a>
# **projectBillingCustomersGetWorkHourPricesForProject**
> List&lt;ProjectBillingCustomerModel&gt; projectBillingCustomersGetWorkHourPricesForProject(projectGuid)

Get all the billing customers for a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | 
    try {
      List<ProjectBillingCustomerModel> result = apiInstance.projectBillingCustomersGetWorkHourPricesForProject(projectGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#projectBillingCustomersGetWorkHourPricesForProject");
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

### Return type

[**List&lt;ProjectBillingCustomerModel&gt;**](ProjectBillingCustomerModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Project&#39;s billing customers |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectCustomValuesGetProjectCustomValue"></a>
# **projectCustomValuesGetProjectCustomValue**
> ProjectCustomValueModel projectCustomValuesGetProjectCustomValue(guid)

Get project custom value by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the project custom value.
    try {
      ProjectCustomValueModel result = apiInstance.projectCustomValuesGetProjectCustomValue(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#projectCustomValuesGetProjectCustomValue");
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
| **guid** | **String**| Id used to get the project custom value. | |

### Return type

[**ProjectCustomValueModel**](ProjectCustomValueModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectCustomValuesGetProjectCustomValues"></a>
# **projectCustomValuesGetProjectCustomValues**
> List&lt;ProjectCustomValueModel&gt; projectCustomValuesGetProjectCustomValues(projectGuid, firstRow, rowCount, active, target, calculateRowCount, sortings)

Get the project custom values.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | ID of the project.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    Boolean active = true; // Boolean | Optional: Get only values of active or inactive project custom properties.
    List<String> target = Arrays.asList(); // List<String> | List of target for which to get the values.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc&sortings[1].key=Number&sortings[1].value=Asc\".
    try {
      List<ProjectCustomValueModel> result = apiInstance.projectCustomValuesGetProjectCustomValues(projectGuid, firstRow, rowCount, active, target, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#projectCustomValuesGetProjectCustomValues");
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
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **active** | **Boolean**| Optional: Get only values of active or inactive project custom properties. | [optional] |
| **target** | [**List&lt;String&gt;**](String.md)| List of target for which to get the values. | [optional] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc&amp;sortings[1].key&#x3D;Number&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] |

### Return type

[**List&lt;ProjectCustomValueModel&gt;**](ProjectCustomValueModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectForecastsGetForecast"></a>
# **projectForecastsGetForecast**
> ProjectForecastOutputModel projectForecastsGetForecast(guid)

Get project forecast by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the project forecast.
    try {
      ProjectForecastOutputModel result = apiInstance.projectForecastsGetForecast(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#projectForecastsGetForecast");
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
| **guid** | **String**| GUID used to get the project forecast. | |

### Return type

[**ProjectForecastOutputModel**](ProjectForecastOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Project forecast |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectForecastsGetForecasts"></a>
# **projectForecastsGetForecasts**
> List&lt;ProjectForecastOutputModel&gt; projectForecastsGetForecasts(projectGuid, startDate, endDate)

Get the project forecasts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | project for the forecasts
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Start date of the date range for the forecasts
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | End date of the date range for the forecasts
    try {
      List<ProjectForecastOutputModel> result = apiInstance.projectForecastsGetForecasts(projectGuid, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#projectForecastsGetForecasts");
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
| **projectGuid** | **String**| project for the forecasts | |
| **startDate** | **OffsetDateTime**| Start date of the date range for the forecasts | [optional] |
| **endDate** | **OffsetDateTime**| End date of the date range for the forecasts | [optional] |

### Return type

[**List&lt;ProjectForecastOutputModel&gt;**](ProjectForecastOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of project forecasts. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectInvoiceSettingsGetProjectInvoiceSetting_0"></a>
# **projectInvoiceSettingsGetProjectInvoiceSetting_0**
> ProjectInvoiceSettingsOutputModel projectInvoiceSettingsGetProjectInvoiceSetting_0(guid)

Get project invoice settings by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String guid = "guid_example"; // String | ID of the project invoice settings.
    try {
      ProjectInvoiceSettingsOutputModel result = apiInstance.projectInvoiceSettingsGetProjectInvoiceSetting_0(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#projectInvoiceSettingsGetProjectInvoiceSetting_0");
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
| **guid** | **String**| ID of the project invoice settings. | |

### Return type

[**ProjectInvoiceSettingsOutputModel**](ProjectInvoiceSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project invoice settings. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectInvoiceSettingsGetProjectInvoiceSettings_0"></a>
# **projectInvoiceSettingsGetProjectInvoiceSettings_0**
> List&lt;ProjectInvoiceSettingsOutputModel&gt; projectInvoiceSettingsGetProjectInvoiceSettings_0(projectGuid)

Get project invoice settings by project ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | ID of the project.
    try {
      List<ProjectInvoiceSettingsOutputModel> result = apiInstance.projectInvoiceSettingsGetProjectInvoiceSettings_0(projectGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#projectInvoiceSettingsGetProjectInvoiceSettings_0");
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

### Return type

[**List&lt;ProjectInvoiceSettingsOutputModel&gt;**](ProjectInvoiceSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project invoice settings. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectMemberCostExceptionsGetProjectMemberCostExceptionsForProject"></a>
# **projectMemberCostExceptionsGetProjectMemberCostExceptionsForProject**
> List&lt;ProjectMemberCostExceptionOutputModel&gt; projectMemberCostExceptionsGetProjectMemberCostExceptionsForProject(projectGuid, userGuid, firstRow, rowCount)

Get all cost exceptions of project members for a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | Guid of the project.
    String userGuid = "userGuid_example"; // String | Optional: Guid of the user.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    try {
      List<ProjectMemberCostExceptionOutputModel> result = apiInstance.projectMemberCostExceptionsGetProjectMemberCostExceptionsForProject(projectGuid, userGuid, firstRow, rowCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#projectMemberCostExceptionsGetProjectMemberCostExceptionsForProject");
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
| **projectGuid** | **String**| Guid of the project. | |
| **userGuid** | **String**| Optional: Guid of the user. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |

### Return type

[**List&lt;ProjectMemberCostExceptionOutputModel&gt;**](ProjectMemberCostExceptionOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the member cost exceptions for one project. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectProductsGetProjectProducts"></a>
# **projectProductsGetProjectProducts**
> List&lt;ProjectProductOutputModel&gt; projectProductsGetProjectProducts(projectGuid, includeProductsFromRegistry, pageToken, rowCount, active)

Get project products

This is the same as organization&#39;s list of products, unless the project has some specific products and UseProductsFromSetting in project model is set to false.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | GUID of the project.
    Boolean includeProductsFromRegistry = false; // Boolean | Optional: Includes products available from product registry
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default all.
    Boolean active = true; // Boolean | Fetch only active
    try {
      List<ProjectProductOutputModel> result = apiInstance.projectProductsGetProjectProducts(projectGuid, includeProductsFromRegistry, pageToken, rowCount, active);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#projectProductsGetProjectProducts");
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
| **projectGuid** | **String**| GUID of the project. | |
| **includeProductsFromRegistry** | **Boolean**| Optional: Includes products available from product registry | [optional] [default to false] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default all. | [optional] |
| **active** | **Boolean**| Fetch only active | [optional] |

### Return type

[**List&lt;ProjectProductOutputModel&gt;**](ProjectProductOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of products for the project. |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectWorkHourPricesGetProjectWorkHourPrice"></a>
# **projectWorkHourPricesGetProjectWorkHourPrice**
> ProjectWorkHourPriceOutputModel projectWorkHourPricesGetProjectWorkHourPrice(guid)

Get project work hour price by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the work hour price.
    try {
      ProjectWorkHourPriceOutputModel result = apiInstance.projectWorkHourPricesGetProjectWorkHourPrice(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#projectWorkHourPricesGetProjectWorkHourPrice");
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
| **guid** | **String**| Id used to get the work hour price. | |

### Return type

[**ProjectWorkHourPriceOutputModel**](ProjectWorkHourPriceOutputModel.md)

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

<a id="projectWorkHourPricesGetWorkHourPricesForProject"></a>
# **projectWorkHourPricesGetWorkHourPricesForProject**
> List&lt;ProjectWorkHourPriceOutputModel&gt; projectWorkHourPricesGetWorkHourPricesForProject(projectGuid, fromPricelistOnly, isAvailable, changedSince)

Get all the work hour prices for a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | Guid of the project.
    Boolean fromPricelistOnly = false; // Boolean | If true return only prices from the price list, if false also returns prices from the products. Default is false.
    Boolean isAvailable = true; // Boolean | Optional: If true, returns only prices that are available for the project, false returns price that are not available. Default all.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get project work hour prices that have been added or changed after this date time (greater or equal).
    try {
      List<ProjectWorkHourPriceOutputModel> result = apiInstance.projectWorkHourPricesGetWorkHourPricesForProject(projectGuid, fromPricelistOnly, isAvailable, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#projectWorkHourPricesGetWorkHourPricesForProject");
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
| **projectGuid** | **String**| Guid of the project. | |
| **fromPricelistOnly** | **Boolean**| If true return only prices from the price list, if false also returns prices from the products. Default is false. | [optional] [default to false] |
| **isAvailable** | **Boolean**| Optional: If true, returns only prices that are available for the project, false returns price that are not available. Default all. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get project work hour prices that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;ProjectWorkHourPriceOutputModel&gt;**](ProjectWorkHourPriceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Projects |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectWorkTypesGetProjectWorktypes"></a>
# **projectWorkTypesGetProjectWorktypes**
> List&lt;ProjectWorkTypeModel&gt; projectWorkTypesGetProjectWorktypes(projectGuid, includeWorktypesFromRegistry, firstRow, rowCount, active, textToSearch, changedSince)

Get project work types.

This is the same as organization&#39;s list of work types, unless the project has some specific work types and \&quot;UseWorktypesFromSetting\&quot; in project model is set to false.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | GUID of the project.
    Boolean includeWorktypesFromRegistry = false; // Boolean | Include work types also from registry. If false, returns only project specific work types. Default false.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    Boolean active = true; // Boolean | If not given, return all work types, if given as true return only active work types, if given as false returns only inactive work types.
    String textToSearch = ""; // String | Optional: Text to search from work type name.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get project work types that have been added or changed after this date time (greater or equal).
    try {
      List<ProjectWorkTypeModel> result = apiInstance.projectWorkTypesGetProjectWorktypes(projectGuid, includeWorktypesFromRegistry, firstRow, rowCount, active, textToSearch, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#projectWorkTypesGetProjectWorktypes");
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
| **projectGuid** | **String**| GUID of the project. | |
| **includeWorktypesFromRegistry** | **Boolean**| Include work types also from registry. If false, returns only project specific work types. Default false. | [optional] [default to false] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **active** | **Boolean**| If not given, return all work types, if given as true return only active work types, if given as false returns only inactive work types. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from work type name. | [optional] [default to ] |
| **changedSince** | **OffsetDateTime**| Optional: Get project work types that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;ProjectWorkTypeModel&gt;**](ProjectWorkTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of work types for the project. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectsGetCustomerProjects"></a>
# **projectsGetCustomerProjects**
> List&lt;ProjectOutputModel&gt; projectsGetCustomerProjects(customerGuid, pageToken, rowCount, isBillable, currencyGuids, projectGuids, projectKeywordGuids, projectStatusTypeGuids, salesPersonGuids, projectOwnerGuids, businessUnitGuids, minimumBillableAmount, customerOwnerGuids, invoiceableDate, marketSegmentationGuids, salesStatusTypeGuids, isClosed, hasRecurringFees, companyCurrencyGuids, projectMemberUserGuids, numbers)

Get customer&#39;s projects

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String customerGuid = "customerGuid_example"; // String | Id of the customer.
    String pageToken = "pageToken_example"; // String | 
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    Boolean isBillable = true; // Boolean | Optional: When true fetch projects that have something to bill, when false nothing to bill. Default nothing = all.
    List<String> currencyGuids = Arrays.asList(); // List<String> | 
    List<String> projectGuids = Arrays.asList(); // List<String> | 
    List<String> projectKeywordGuids = Arrays.asList(); // List<String> | 
    List<String> projectStatusTypeGuids = Arrays.asList(); // List<String> | 
    List<String> salesPersonGuids = Arrays.asList(); // List<String> | 
    List<String> projectOwnerGuids = Arrays.asList(); // List<String> | 
    List<String> businessUnitGuids = Arrays.asList(); // List<String> | 
    Double minimumBillableAmount = 3.4D; // Double | 
    List<String> customerOwnerGuids = Arrays.asList(); // List<String> | 
    OffsetDateTime invoiceableDate = OffsetDateTime.now(); // OffsetDateTime | 
    List<String> marketSegmentationGuids = Arrays.asList(); // List<String> | 
    List<String> salesStatusTypeGuids = Arrays.asList(); // List<String> | 
    Boolean isClosed = true; // Boolean | 
    Boolean hasRecurringFees = true; // Boolean | 
    List<String> companyCurrencyGuids = Arrays.asList(); // List<String> | 
    List<String> projectMemberUserGuids = Arrays.asList(); // List<String> | 
    List<Long> numbers = Arrays.asList(); // List<Long> | 
    try {
      List<ProjectOutputModel> result = apiInstance.projectsGetCustomerProjects(customerGuid, pageToken, rowCount, isBillable, currencyGuids, projectGuids, projectKeywordGuids, projectStatusTypeGuids, salesPersonGuids, projectOwnerGuids, businessUnitGuids, minimumBillableAmount, customerOwnerGuids, invoiceableDate, marketSegmentationGuids, salesStatusTypeGuids, isClosed, hasRecurringFees, companyCurrencyGuids, projectMemberUserGuids, numbers);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#projectsGetCustomerProjects");
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
| **customerGuid** | **String**| Id of the customer. | |
| **pageToken** | **String**|  | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **isBillable** | **Boolean**| Optional: When true fetch projects that have something to bill, when false nothing to bill. Default nothing &#x3D; all. | [optional] |
| **currencyGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **projectGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **projectKeywordGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **projectStatusTypeGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **salesPersonGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **projectOwnerGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **businessUnitGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **minimumBillableAmount** | **Double**|  | [optional] |
| **customerOwnerGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **invoiceableDate** | **OffsetDateTime**|  | [optional] |
| **marketSegmentationGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **salesStatusTypeGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **isClosed** | **Boolean**|  | [optional] |
| **hasRecurringFees** | **Boolean**|  | [optional] |
| **companyCurrencyGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **projectMemberUserGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **numbers** | [**List&lt;Long&gt;**](Long.md)|  | [optional] |

### Return type

[**List&lt;ProjectOutputModel&gt;**](ProjectOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the projects for the customer |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectsGetProject"></a>
# **projectsGetProject**
> ProjectOutputModel projectsGetProject(guid)

Get project by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the project.
    try {
      ProjectOutputModel result = apiInstance.projectsGetProject(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#projectsGetProject");
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
| **guid** | **String**| Id used to get the project. | |

### Return type

[**ProjectOutputModel**](ProjectOutputModel.md)

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

<a id="projectsGetProjects"></a>
# **projectsGetProjects**
> List&lt;ProjectOutputModel&gt; projectsGetProjects(pageToken, rowCount, currencyGuid, changedSince, isBillable, customerGuids, projectGuids, projectKeywordGuids, projectStatusTypeGuids, salesPersonGuids, projectOwnerGuids, businessUnitGuids, minimumBillableAmount, customerOwnerGuids, invoiceableDate, marketSegmentationGuids, salesStatusTypeGuids, isClosed, hasRecurringFees, companyCurrencyGuids, projectMemberUserGuids, numbers, internal)

Get all the projects

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String pageToken = "pageToken_example"; // String | 
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String currencyGuid = "currencyGuid_example"; // String | Optional: ID of project currency.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get projects that have been added or changed after this date time (greater or equal).
    Boolean isBillable = true; // Boolean | Optional: When true fetch projects that have something to bill, when false nothing to bill. Default nothing = all.
    List<String> customerGuids = Arrays.asList(); // List<String> | 
    List<String> projectGuids = Arrays.asList(); // List<String> | 
    List<String> projectKeywordGuids = Arrays.asList(); // List<String> | 
    List<String> projectStatusTypeGuids = Arrays.asList(); // List<String> | 
    List<String> salesPersonGuids = Arrays.asList(); // List<String> | 
    List<String> projectOwnerGuids = Arrays.asList(); // List<String> | 
    List<String> businessUnitGuids = Arrays.asList(); // List<String> | 
    Double minimumBillableAmount = 3.4D; // Double | 
    List<String> customerOwnerGuids = Arrays.asList(); // List<String> | 
    OffsetDateTime invoiceableDate = OffsetDateTime.now(); // OffsetDateTime | 
    List<String> marketSegmentationGuids = Arrays.asList(); // List<String> | 
    List<String> salesStatusTypeGuids = Arrays.asList(); // List<String> | 
    Boolean isClosed = true; // Boolean | 
    Boolean hasRecurringFees = true; // Boolean | 
    List<String> companyCurrencyGuids = Arrays.asList(); // List<String> | 
    List<String> projectMemberUserGuids = Arrays.asList(); // List<String> | 
    List<Long> numbers = Arrays.asList(); // List<Long> | 
    Boolean internal = true; // Boolean | Optional: Get internal / non-internal projects.
    try {
      List<ProjectOutputModel> result = apiInstance.projectsGetProjects(pageToken, rowCount, currencyGuid, changedSince, isBillable, customerGuids, projectGuids, projectKeywordGuids, projectStatusTypeGuids, salesPersonGuids, projectOwnerGuids, businessUnitGuids, minimumBillableAmount, customerOwnerGuids, invoiceableDate, marketSegmentationGuids, salesStatusTypeGuids, isClosed, hasRecurringFees, companyCurrencyGuids, projectMemberUserGuids, numbers, internal);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#projectsGetProjects");
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
| **pageToken** | **String**|  | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **currencyGuid** | **String**| Optional: ID of project currency. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get projects that have been added or changed after this date time (greater or equal). | [optional] |
| **isBillable** | **Boolean**| Optional: When true fetch projects that have something to bill, when false nothing to bill. Default nothing &#x3D; all. | [optional] |
| **customerGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **projectGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **projectKeywordGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **projectStatusTypeGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **salesPersonGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **projectOwnerGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **businessUnitGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **minimumBillableAmount** | **Double**|  | [optional] |
| **customerOwnerGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **invoiceableDate** | **OffsetDateTime**|  | [optional] |
| **marketSegmentationGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **salesStatusTypeGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **isClosed** | **Boolean**|  | [optional] |
| **hasRecurringFees** | **Boolean**|  | [optional] |
| **companyCurrencyGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **projectMemberUserGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **numbers** | [**List&lt;Long&gt;**](Long.md)|  | [optional] |
| **internal** | **Boolean**| Optional: Get internal / non-internal projects. | [optional] |

### Return type

[**List&lt;ProjectOutputModel&gt;**](ProjectOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Projects |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectsGetSalesCases"></a>
# **projectsGetSalesCases**
> List&lt;ProjectOutputModel&gt; projectsGetSalesCases(pageToken, rowCount, customerGuids, currencyGuids, projectGuids, projectKeywordGuids, projectStatusTypeGuids, salesPersonGuids, projectOwnerGuids, businessUnitGuids, minimumBillableAmount, customerOwnerGuids, invoiceableDate, marketSegmentationGuids, salesStatusTypeGuids, isClosed, hasRecurringFees, companyCurrencyGuids, projectMemberUserGuids, numbers)

Gets the sales cases (sales status is in progress)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String pageToken = "pageToken_example"; // String | 
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    List<String> customerGuids = Arrays.asList(); // List<String> | 
    List<String> currencyGuids = Arrays.asList(); // List<String> | 
    List<String> projectGuids = Arrays.asList(); // List<String> | 
    List<String> projectKeywordGuids = Arrays.asList(); // List<String> | 
    List<String> projectStatusTypeGuids = Arrays.asList(); // List<String> | 
    List<String> salesPersonGuids = Arrays.asList(); // List<String> | 
    List<String> projectOwnerGuids = Arrays.asList(); // List<String> | 
    List<String> businessUnitGuids = Arrays.asList(); // List<String> | 
    Double minimumBillableAmount = 3.4D; // Double | 
    List<String> customerOwnerGuids = Arrays.asList(); // List<String> | 
    OffsetDateTime invoiceableDate = OffsetDateTime.now(); // OffsetDateTime | 
    List<String> marketSegmentationGuids = Arrays.asList(); // List<String> | 
    List<String> salesStatusTypeGuids = Arrays.asList(); // List<String> | 
    Boolean isClosed = true; // Boolean | 
    Boolean hasRecurringFees = true; // Boolean | 
    List<String> companyCurrencyGuids = Arrays.asList(); // List<String> | 
    List<String> projectMemberUserGuids = Arrays.asList(); // List<String> | 
    List<Long> numbers = Arrays.asList(); // List<Long> | 
    try {
      List<ProjectOutputModel> result = apiInstance.projectsGetSalesCases(pageToken, rowCount, customerGuids, currencyGuids, projectGuids, projectKeywordGuids, projectStatusTypeGuids, salesPersonGuids, projectOwnerGuids, businessUnitGuids, minimumBillableAmount, customerOwnerGuids, invoiceableDate, marketSegmentationGuids, salesStatusTypeGuids, isClosed, hasRecurringFees, companyCurrencyGuids, projectMemberUserGuids, numbers);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#projectsGetSalesCases");
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
| **pageToken** | **String**|  | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **customerGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **currencyGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **projectGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **projectKeywordGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **projectStatusTypeGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **salesPersonGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **projectOwnerGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **businessUnitGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **minimumBillableAmount** | **Double**|  | [optional] |
| **customerOwnerGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **invoiceableDate** | **OffsetDateTime**|  | [optional] |
| **marketSegmentationGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **salesStatusTypeGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **isClosed** | **Boolean**|  | [optional] |
| **hasRecurringFees** | **Boolean**|  | [optional] |
| **companyCurrencyGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **projectMemberUserGuids** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **numbers** | [**List&lt;Long&gt;**](Long.md)|  | [optional] |

### Return type

[**List&lt;ProjectOutputModel&gt;**](ProjectOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Projects |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalFeesGetProposalFee"></a>
# **proposalFeesGetProposalFee**
> ProposalFeeRowOutputModel proposalFeesGetProposalFee(guid)

Get the proposal fee rows by guid

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String guid = "guid_example"; // String | proposal fee row id to get
    try {
      ProposalFeeRowOutputModel result = apiInstance.proposalFeesGetProposalFee(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#proposalFeesGetProposalFee");
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
| **guid** | **String**| proposal fee row id to get | |

### Return type

[**ProposalFeeRowOutputModel**](ProposalFeeRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Proposal fee |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalFeesGetProposalFees"></a>
# **proposalFeesGetProposalFees**
> List&lt;ProposalFeeRowOutputModel&gt; proposalFeesGetProposalFees(pageToken, rowCount, changedSince)

Get the proposal fee rows.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get proposal fee rows that have been added or changed after this date time (greater or equal).
    try {
      List<ProposalFeeRowOutputModel> result = apiInstance.proposalFeesGetProposalFees(pageToken, rowCount, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#proposalFeesGetProposalFees");
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
| **changedSince** | **OffsetDateTime**| Optional: Get proposal fee rows that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;ProposalFeeRowOutputModel&gt;**](ProposalFeeRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Proposal fee rows |  * NextPageToken - Page token to fetch the next page <br>  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalFeesGetProposalFeesForProposal"></a>
# **proposalFeesGetProposalFeesForProposal**
> List&lt;ProposalFeeRowOutputModel&gt; proposalFeesGetProposalFeesForProposal(proposalGuid, pageToken, rowCount)

Get all the proposal fee rows for a proposal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String proposalGuid = "proposalGuid_example"; // String | proposal id for which to get proposal fees rows.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default all.
    try {
      List<ProposalFeeRowOutputModel> result = apiInstance.proposalFeesGetProposalFeesForProposal(proposalGuid, pageToken, rowCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#proposalFeesGetProposalFeesForProposal");
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
| **proposalGuid** | **String**| proposal id for which to get proposal fees rows. | |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default all. | [optional] |

### Return type

[**List&lt;ProposalFeeRowOutputModel&gt;**](ProposalFeeRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Proposal fee rows |  * NextPageToken - Page token to fetch the next page <br>  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalSettingsGetProposalSettings"></a>
# **proposalSettingsGetProposalSettings**
> ProposalSettingsOutputModel proposalSettingsGetProposalSettings(guid)

Get settings for a proposal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the Proposal.
    try {
      ProposalSettingsOutputModel result = apiInstance.proposalSettingsGetProposalSettings(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#proposalSettingsGetProposalSettings");
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
| **guid** | **String**| GUID used to get the Proposal. | |

### Return type

[**ProposalSettingsOutputModel**](ProposalSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Proposal |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalSubtotalsGetProposalSubtotal"></a>
# **proposalSubtotalsGetProposalSubtotal**
> ProposalSubtotalOutputModel proposalSubtotalsGetProposalSubtotal(guid)

Get Proposal subtotal by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the Proposal subtotal.
    try {
      ProposalSubtotalOutputModel result = apiInstance.proposalSubtotalsGetProposalSubtotal(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#proposalSubtotalsGetProposalSubtotal");
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
| **guid** | **String**| GUID used to get the Proposal subtotal. | |

### Return type

[**ProposalSubtotalOutputModel**](ProposalSubtotalOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Proposal subtotal |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalSubtotalsGetProposalSubtotals"></a>
# **proposalSubtotalsGetProposalSubtotals**
> List&lt;ProposalSubtotalOutputModel&gt; proposalSubtotalsGetProposalSubtotals(pageToken, rowCount, changedSince)

Get the proposal subtotals.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String pageToken = "pageToken_example"; // String | Optional: Page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get proposal subtotals that have been added or changed after this date time (greater or equal).
    try {
      List<ProposalSubtotalOutputModel> result = apiInstance.proposalSubtotalsGetProposalSubtotals(pageToken, rowCount, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#proposalSubtotalsGetProposalSubtotals");
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
| **pageToken** | **String**| Optional: Page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get proposal subtotals that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;ProposalSubtotalOutputModel&gt;**](ProposalSubtotalOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * NextPageToken - Page token to fetch the next page <br>  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalSubtotalsGetProposalSubtotalsForProposal"></a>
# **proposalSubtotalsGetProposalSubtotalsForProposal**
> List&lt;ProposalSubtotalOutputModel&gt; proposalSubtotalsGetProposalSubtotalsForProposal(proposalGuid, pageToken, rowCount)

Get all the proposal subtotals for a proposal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String proposalGuid = "proposalGuid_example"; // String | proposal id for which to get proposal subtotals.
    String pageToken = "pageToken_example"; // String | Optional: Page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default all.
    try {
      List<ProposalSubtotalOutputModel> result = apiInstance.proposalSubtotalsGetProposalSubtotalsForProposal(proposalGuid, pageToken, rowCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#proposalSubtotalsGetProposalSubtotalsForProposal");
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
| **proposalGuid** | **String**| proposal id for which to get proposal subtotals. | |
| **pageToken** | **String**| Optional: Page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default all. | [optional] |

### Return type

[**List&lt;ProposalSubtotalOutputModel&gt;**](ProposalSubtotalOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Proposal |  * NextPageToken - Page token to fetch the next page <br>  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalWorkhoursGetProposalWorkHours"></a>
# **proposalWorkhoursGetProposalWorkHours**
> List&lt;ProposalWorkhourRowOutputModel&gt; proposalWorkhoursGetProposalWorkHours(pageToken, rowCount, changedSince)

Get the proposal work rows.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get proposal work rows that have been added or changed after this date time (greater or equal).
    try {
      List<ProposalWorkhourRowOutputModel> result = apiInstance.proposalWorkhoursGetProposalWorkHours(pageToken, rowCount, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#proposalWorkhoursGetProposalWorkHours");
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
| **changedSince** | **OffsetDateTime**| Optional: Get proposal work rows that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;ProposalWorkhourRowOutputModel&gt;**](ProposalWorkhourRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * NextPageToken - Page token to fetch the next page <br>  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalWorkhoursGetProposalWorkHoursForProposal"></a>
# **proposalWorkhoursGetProposalWorkHoursForProposal**
> List&lt;ProposalWorkhourRowOutputModel&gt; proposalWorkhoursGetProposalWorkHoursForProposal(proposalGuid, pageToken, rowCount)

Get all the proposal work rows.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String proposalGuid = "proposalGuid_example"; // String | proposal id for which to get proposal work rows.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default all.
    try {
      List<ProposalWorkhourRowOutputModel> result = apiInstance.proposalWorkhoursGetProposalWorkHoursForProposal(proposalGuid, pageToken, rowCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#proposalWorkhoursGetProposalWorkHoursForProposal");
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
| **proposalGuid** | **String**| proposal id for which to get proposal work rows. | |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default all. | [optional] |

### Return type

[**List&lt;ProposalWorkhourRowOutputModel&gt;**](ProposalWorkhourRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Proposal work rows. |  * NextPageToken - Page token to fetch the next page <br>  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalWorkhoursGetProposalWorkhour"></a>
# **proposalWorkhoursGetProposalWorkhour**
> ProposalWorkhourRowOutputModel proposalWorkhoursGetProposalWorkhour(guid)

Get the proposal work row by guid.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String guid = "guid_example"; // String | proposal work row id to get.
    try {
      ProposalWorkhourRowOutputModel result = apiInstance.proposalWorkhoursGetProposalWorkhour(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#proposalWorkhoursGetProposalWorkhour");
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
| **guid** | **String**| proposal work row id to get. | |

### Return type

[**ProposalWorkhourRowOutputModel**](ProposalWorkhourRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Proposal work row. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalsGetProposal"></a>
# **proposalsGetProposal**
> ProposalOutputModel proposalsGetProposal(guid)

Get Proposal by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the Proposal.
    try {
      ProposalOutputModel result = apiInstance.proposalsGetProposal(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#proposalsGetProposal");
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
| **guid** | **String**| GUID used to get the Proposal. | |

### Return type

[**ProposalOutputModel**](ProposalOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Proposal |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalsGetProposals"></a>
# **proposalsGetProposals**
> List&lt;ProposalOutputModel&gt; proposalsGetProposals(pageToken, rowCount, changedSince)

Get all the proposals

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get proposals that have been added or changed after this date time (greater or equal).
    try {
      List<ProposalOutputModel> result = apiInstance.proposalsGetProposals(pageToken, rowCount, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#proposalsGetProposals");
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
| **changedSince** | **OffsetDateTime**| Optional: Get proposals that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;ProposalOutputModel&gt;**](ProposalOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Proposal |  * NextPageToken - Page token to fetch the next page <br>  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalsGetProposalsForProject"></a>
# **proposalsGetProposalsForProject**
> List&lt;ProposalOutputModel&gt; proposalsGetProposalsForProject(projectGuid, pageToken, rowCount, changedSince)

Get all the proposals for a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | Project id for which to get proposals.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default all.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get proposals that have been added or changed after this date time (greater or equal).
    try {
      List<ProposalOutputModel> result = apiInstance.proposalsGetProposalsForProject(projectGuid, pageToken, rowCount, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#proposalsGetProposalsForProject");
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
| **projectGuid** | **String**| Project id for which to get proposals. | |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default all. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get proposals that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;ProposalOutputModel&gt;**](ProposalOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Proposal |  * NextPageToken - Page token to fetch the next page <br>  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="salesNotesGetAllCustomerSalesNotes"></a>
# **salesNotesGetAllCustomerSalesNotes**
> List&lt;SalesNoteOutputModel&gt; salesNotesGetAllCustomerSalesNotes(customerGuid, pageToken, rowCount, changedSince)

Get the sales notes by customer guid.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String customerGuid = "customerGuid_example"; // String | Customer guid used to get the notes.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get sales notes that have been added or changed after this date time (greater or equal).
    try {
      List<SalesNoteOutputModel> result = apiInstance.salesNotesGetAllCustomerSalesNotes(customerGuid, pageToken, rowCount, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#salesNotesGetAllCustomerSalesNotes");
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
| **customerGuid** | **String**| Customer guid used to get the notes. | |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get sales notes that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;SalesNoteOutputModel&gt;**](SalesNoteOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of sales notes for a customer. |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="salesNotesGetProjectSalesNote"></a>
# **salesNotesGetProjectSalesNote**
> ProjectSalesNoteOutputModel salesNotesGetProjectSalesNote(guid)

Get project sales note by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the project sales note.
    try {
      ProjectSalesNoteOutputModel result = apiInstance.salesNotesGetProjectSalesNote(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#salesNotesGetProjectSalesNote");
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
| **guid** | **String**| GUID used to get the project sales note. | |

### Return type

[**ProjectSalesNoteOutputModel**](ProjectSalesNoteOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProjectNote |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="salesNotesGetProjectSalesNotes"></a>
# **salesNotesGetProjectSalesNotes**
> List&lt;ProjectSalesNoteOutputModel&gt; salesNotesGetProjectSalesNotes(projectGuid, pageToken, rowCount, changedSince)

Get the sales notes of a case.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | Project guid used to get the notes.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get sales notes that have been added or changed after this date time (greater or equal).
    try {
      List<ProjectSalesNoteOutputModel> result = apiInstance.salesNotesGetProjectSalesNotes(projectGuid, pageToken, rowCount, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#salesNotesGetProjectSalesNotes");
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
| **projectGuid** | **String**| Project guid used to get the notes. | |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get sales notes that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;ProjectSalesNoteOutputModel&gt;**](ProjectSalesNoteOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of sales notes for a project. |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="salesStatusHistoryGetSalesStatusHistory"></a>
# **salesStatusHistoryGetSalesStatusHistory**
> List&lt;SalesStatusHistoryOutputModel&gt; salesStatusHistoryGetSalesStatusHistory(projectGuid)

Get the sales status history for a project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | The project for which the sales status history is fetched.
    try {
      List<SalesStatusHistoryOutputModel> result = apiInstance.salesStatusHistoryGetSalesStatusHistory(projectGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#salesStatusHistoryGetSalesStatusHistory");
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
| **projectGuid** | **String**| The project for which the sales status history is fetched. | |

### Return type

[**List&lt;SalesStatusHistoryOutputModel&gt;**](SalesStatusHistoryOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sales status history |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="teamProductivityGetTeamProductivity"></a>
# **teamProductivityGetTeamProductivity**
> List&lt;TeamProductivityOutputModel&gt; teamProductivityGetTeamProductivity(projectGuid)

Get team productivity of a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | GUID of the project.
    try {
      List<TeamProductivityOutputModel> result = apiInstance.teamProductivityGetTeamProductivity(projectGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#teamProductivityGetTeamProductivity");
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
| **projectGuid** | **String**| GUID of the project. | |

### Return type

[**List&lt;TeamProductivityOutputModel&gt;**](TeamProductivityOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of project members with team productivity information. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="travelExpenseTypesGetSearchedTravelExpenseTypes"></a>
# **travelExpenseTypesGetSearchedTravelExpenseTypes**
> List&lt;TravelExpenseTypeOutputModel&gt; travelExpenseTypesGetSearchedTravelExpenseTypes(projectGuid, textToSearch, firstRow, rowCount, userGuid, expenseClass)

Search active travel expense types of project by part of the name or code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | Id of the project.
    String textToSearch = ""; // String | Searched string: part of name or code.
    Integer firstRow = 56; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default all.
    String userGuid = "userGuid_example"; // String | Optional: Id of the user to fetch travels for.
    ExpensesClass expenseClass = ExpensesClass.fromValue("Mileage"); // ExpensesClass | Optional: Expense class of the travel. Mileage/DailyAllowance/OtherTravelExpense.
    try {
      List<TravelExpenseTypeOutputModel> result = apiInstance.travelExpenseTypesGetSearchedTravelExpenseTypes(projectGuid, textToSearch, firstRow, rowCount, userGuid, expenseClass);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#travelExpenseTypesGetSearchedTravelExpenseTypes");
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
| **projectGuid** | **String**| Id of the project. | |
| **textToSearch** | **String**| Searched string: part of name or code. | [optional] [default to ] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default all. | [optional] |
| **userGuid** | **String**| Optional: Id of the user to fetch travels for. | [optional] |
| **expenseClass** | [**ExpensesClass**](.md)| Optional: Expense class of the travel. Mileage/DailyAllowance/OtherTravelExpense. | [optional] [enum: Mileage, DailyAllowance, OtherTravelExpense] |

### Return type

[**List&lt;TravelExpenseTypeOutputModel&gt;**](TravelExpenseTypeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the Travel expense types matching search criteria. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="travelPricesGetTravelPricesForProject"></a>
# **travelPricesGetTravelPricesForProject**
> List&lt;TravelPriceOutputModel&gt; travelPricesGetTravelPricesForProject(projectGuid, fromPricelistOnly, expenseClasses, firstRow, rowCount, textToSearch, calculateRowCount)

Get all the travel prices for a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | ID of the project.
    Boolean fromPricelistOnly = false; // Boolean | If true return only prices from the price list, if false also returns prices from the settings. Default is false.
    List<ExpensesClass> expenseClasses = Arrays.asList(); // List<ExpensesClass> | Optional: List of expense classes to search by, defaults to all travel categories.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from Product name.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate the number of total rows. Default false = total row count is returned as zero.
    try {
      List<TravelPriceOutputModel> result = apiInstance.travelPricesGetTravelPricesForProject(projectGuid, fromPricelistOnly, expenseClasses, firstRow, rowCount, textToSearch, calculateRowCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#travelPricesGetTravelPricesForProject");
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
| **fromPricelistOnly** | **Boolean**| If true return only prices from the price list, if false also returns prices from the settings. Default is false. | [optional] [default to false] |
| **expenseClasses** | [**List&lt;ExpensesClass&gt;**](ExpensesClass.md)| Optional: List of expense classes to search by, defaults to all travel categories. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from Product name. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate the number of total rows. Default false &#x3D; total row count is returned as zero. | [optional] [default to false] |

### Return type

[**List&lt;TravelPriceOutputModel&gt;**](TravelPriceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TravelPriceModel. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workTypesGetPhaseWorkTypes"></a>
# **workTypesGetPhaseWorkTypes**
> List&lt;WorkTypeOutputModel&gt; workTypesGetPhaseWorkTypes(phaseGuid, pageToken, rowCount, userGuid)

Get all work types that are available for a phase (for work hour entry)

Only the active work types are included in the list, whether they come from organization settings or project specific work types.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String phaseGuid = "phaseGuid_example"; // String | Id of the phase.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: number of rows to fetch
    String userGuid = "userGuid_example"; // String | Id of the user for whom the work types are retrieved. Default is current user.
    try {
      List<WorkTypeOutputModel> result = apiInstance.workTypesGetPhaseWorkTypes(phaseGuid, pageToken, rowCount, userGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#workTypesGetPhaseWorkTypes");
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
| **phaseGuid** | **String**| Id of the phase. | |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: number of rows to fetch | [optional] |
| **userGuid** | **String**| Id of the user for whom the work types are retrieved. Default is current user. | [optional] |

### Return type

[**List&lt;WorkTypeOutputModel&gt;**](WorkTypeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the work types matching search criteria |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workTypesGetSearchedWorktypes"></a>
# **workTypesGetSearchedWorktypes**
> List&lt;WorktypeForProjectOutputModel&gt; workTypesGetSearchedWorktypes(projectGuid, firstRow, rowCount, textToSearch)

Search active work types by part of the name or code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsReadApi;

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

    ProjectsReadApi apiInstance = new ProjectsReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | Id of the case to which proposal is connected.
    Integer firstRow = 56; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Searched string: part of name or code.
    try {
      List<WorktypeForProjectOutputModel> result = apiInstance.workTypesGetSearchedWorktypes(projectGuid, firstRow, rowCount, textToSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsReadApi#workTypesGetSearchedWorktypes");
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
| **projectGuid** | **String**| Id of the case to which proposal is connected. | |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Searched string: part of name or code. | [optional] [default to ] |

### Return type

[**List&lt;WorktypeForProjectOutputModel&gt;**](WorktypeForProjectOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the work types matching search criteria. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

