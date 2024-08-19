# ProjectsWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**filesPostProjectLink**](ProjectsWriteApi.md#filesPostProjectLink) | **POST** /v1/projectlinks | Add a link to a project. |
| [**keywordsLinkKeywordToProject**](ProjectsWriteApi.md#keywordsLinkKeywordToProject) | **POST** /v1/projects/{projectGuid}/keywords/{guid} | Link existing keyword to project |
| [**phaseMembersPostPhaseMember**](ProjectsWriteApi.md#phaseMembersPostPhaseMember) | **POST** /v1/phasemembers | Adds a phase member. |
| [**phaseMembersPostPhaseMembersFromBusinessUnitUsers**](ProjectsWriteApi.md#phaseMembersPostPhaseMembersFromBusinessUnitUsers) | **POST** /v1/phasemembersfrombusinessunitusers | Adds business unit users to phase members. |
| [**phasesPatchPhase**](ProjectsWriteApi.md#phasesPatchPhase) | **PATCH** /v1/phases/{guid} | Update (Patch) a phase or a part of it |
| [**phasesPostPhase**](ProjectsWriteApi.md#phasesPostPhase) | **POST** /v1/phases | Insert a phase |
| [**priceListsPostCustomPricelist**](ProjectsWriteApi.md#priceListsPostCustomPricelist) | **POST** /v1/projects/{projectGuid}/pricelists/custom | Create custom price list for a project. If project already has a custom price list returns existing price list. Creates a new price list if project doesn&#39;t have a custom price list. Project can only have one custom price list. Note that project&#39;s price list will be changed to the custom price list created here and also existing prices are copied to the new price list. |
| [**projectCustomValuesPatchProjectCustomValue**](ProjectsWriteApi.md#projectCustomValuesPatchProjectCustomValue) | **PATCH** /v1/projects/customvalues/{guid} | Update (Patch) a project custom value or a part of it. |
| [**projectCustomValuesPostProjectCustomValue**](ProjectsWriteApi.md#projectCustomValuesPostProjectCustomValue) | **POST** /v1/projects/customvalues | Insert a project custom value. |
| [**projectForecastsPatchForecast**](ProjectsWriteApi.md#projectForecastsPatchForecast) | **PATCH** /v1/projectforecasts/{guid} | Update (Patch) an project forecast or a part of it |
| [**projectForecastsPostForecast**](ProjectsWriteApi.md#projectForecastsPostForecast) | **POST** /v1/projectforecasts | Insert a project forecast |
| [**projectInvoiceSettingsPatchProjectInvoiceSettings_0**](ProjectsWriteApi.md#projectInvoiceSettingsPatchProjectInvoiceSettings_0) | **PATCH** /v1/projectinvoicesettings/{guid} | Update (Patch) project invoice settings. |
| [**projectInvoiceSettingsPostProjectInvoiceSettings_0**](ProjectsWriteApi.md#projectInvoiceSettingsPostProjectInvoiceSettings_0) | **POST** /v1/projectinvoicesettings | Create a new project invoice settings. |
| [**projectProductsPostProjectProduct**](ProjectsWriteApi.md#projectProductsPostProjectProduct) | **POST** /v1/projectproducts | Adds a product to a project. |
| [**projectWorkHourPricesPatchProjectWorkHourPrice**](ProjectsWriteApi.md#projectWorkHourPricesPatchProjectWorkHourPrice) | **PATCH** /v1/projectworkhourprices/{guid} | Update (Patch) a work hour price or a part of it |
| [**projectWorkHourPricesPostProjectWorkHourPrice**](ProjectsWriteApi.md#projectWorkHourPricesPostProjectWorkHourPrice) | **POST** /v1/projectworkhourprices | Insert a work hour price |
| [**projectWorkTypesPatchProjectWorktype**](ProjectsWriteApi.md#projectWorkTypesPatchProjectWorktype) | **PATCH** /v1/projectworktypes/{guid} | Update (patch) a project work type. |
| [**projectWorkTypesPostProjectWorktype**](ProjectsWriteApi.md#projectWorkTypesPostProjectWorktype) | **POST** /v1/projectworktypes | Adds a work type to a project. |
| [**projectsPatchProject**](ProjectsWriteApi.md#projectsPatchProject) | **PATCH** /v1/projects/{guid} | Update (Patch) a project or a part of it |
| [**projectsPostProject**](ProjectsWriteApi.md#projectsPostProject) | **POST** /v1/projects | Insert a project |
| [**proposalFeesPatchProposalFee**](ProjectsWriteApi.md#proposalFeesPatchProposalFee) | **PATCH** /v1/proposalfeerows/{guid} | Update (Patch) a proposal fee row or a part of it |
| [**proposalFeesPostProposalFee**](ProjectsWriteApi.md#proposalFeesPostProposalFee) | **POST** /v1/proposalfeerows | Insert a proposal fee row. |
| [**proposalSettingsPatchProposalSettings**](ProjectsWriteApi.md#proposalSettingsPatchProposalSettings) | **PATCH** /v1/proposals/{guid}/proposalsettings | Update (Patch) proposal settings |
| [**proposalSubtotalsPatchProposalSubtotal**](ProjectsWriteApi.md#proposalSubtotalsPatchProposalSubtotal) | **PATCH** /v1/proposalsubtotals/{guid} | Update (Patch) a Proposal subtotal or a part of it |
| [**proposalSubtotalsPostProposalSubtotal**](ProjectsWriteApi.md#proposalSubtotalsPostProposalSubtotal) | **POST** /v1/proposalsubtotals | Insert a proposal subtotal |
| [**proposalWorkhoursPatchProposalWorkhour**](ProjectsWriteApi.md#proposalWorkhoursPatchProposalWorkhour) | **PATCH** /v1/proposalworkrows/{guid} | Update (Patch) a proposal work row or a part of it. |
| [**proposalWorkhoursPostProposalWorkhour**](ProjectsWriteApi.md#proposalWorkhoursPostProposalWorkhour) | **POST** /v1/proposalworkrows | Insert a proposal work row. |
| [**proposalsPatchProposal**](ProjectsWriteApi.md#proposalsPatchProposal) | **PATCH** /v1/proposals/{guid} | Update (Patch) a Proposal or a part of it |
| [**proposalsPostProposal**](ProjectsWriteApi.md#proposalsPostProposal) | **POST** /v1/proposals | Insert a proposal. |
| [**salesNotesPatchProjectSalesNote**](ProjectsWriteApi.md#salesNotesPatchProjectSalesNote) | **PATCH** /v1/projectsalesnotes/{guid} | Update (Patch) a project sales note or a part of it. |
| [**salesNotesPostProjectSalesNotes**](ProjectsWriteApi.md#salesNotesPostProjectSalesNotes) | **POST** /v1/projectsalesnotes | Insert a project sales note. |


<a id="filesPostProjectLink"></a>
# **filesPostProjectLink**
> ProjectFileModel filesPostProjectLink(projectFileModel)

Add a link to a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    ProjectFileModel projectFileModel = new ProjectFileModel(); // ProjectFileModel | ProjectFileModel.
    try {
      ProjectFileModel result = apiInstance.filesPostProjectLink(projectFileModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#filesPostProjectLink");
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
| **projectFileModel** | [**ProjectFileModel**](ProjectFileModel.md)| ProjectFileModel. | [optional] |

### Return type

[**ProjectFileModel**](ProjectFileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created project file. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="keywordsLinkKeywordToProject"></a>
# **keywordsLinkKeywordToProject**
> ProjectKeywordModel keywordsLinkKeywordToProject(projectGuid, guid)

Link existing keyword to project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | 
    String guid = "guid_example"; // String | 
    try {
      ProjectKeywordModel result = apiInstance.keywordsLinkKeywordToProject(projectGuid, guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#keywordsLinkKeywordToProject");
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

[**ProjectKeywordModel**](ProjectKeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created project keyword link. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="phaseMembersPostPhaseMember"></a>
# **phaseMembersPostPhaseMember**
> PhaseMemberModel phaseMembersPostPhaseMember(addToAllSubPhases, phaseMemberModel)

Adds a phase member.

User is always added as a root phase (project) member also.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    Boolean addToAllSubPhases = true; // Boolean | Optional: Add member to all sub phases. Default true.
    PhaseMemberModel phaseMemberModel = new PhaseMemberModel(); // PhaseMemberModel | PhaseMemberModel.
    try {
      PhaseMemberModel result = apiInstance.phaseMembersPostPhaseMember(addToAllSubPhases, phaseMemberModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#phaseMembersPostPhaseMember");
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
| **addToAllSubPhases** | **Boolean**| Optional: Add member to all sub phases. Default true. | [optional] [default to true] |
| **phaseMemberModel** | [**PhaseMemberModel**](PhaseMemberModel.md)| PhaseMemberModel. | [optional] |

### Return type

[**PhaseMemberModel**](PhaseMemberModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Added member. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="phaseMembersPostPhaseMembersFromBusinessUnitUsers"></a>
# **phaseMembersPostPhaseMembersFromBusinessUnitUsers**
> List&lt;PhaseMemberModel&gt; phaseMembersPostPhaseMembersFromBusinessUnitUsers(addToAllSubPhases, phaseMembersFromBusinessUnitUsersModel)

Adds business unit users to phase members.

Users are always added as a root phase (project) member also.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    Boolean addToAllSubPhases = true; // Boolean | Optional: Add member to all sub phases. Default true.
    PhaseMembersFromBusinessUnitUsersModel phaseMembersFromBusinessUnitUsersModel = new PhaseMembersFromBusinessUnitUsersModel(); // PhaseMembersFromBusinessUnitUsersModel | PhaseMemberModel.
    try {
      List<PhaseMemberModel> result = apiInstance.phaseMembersPostPhaseMembersFromBusinessUnitUsers(addToAllSubPhases, phaseMembersFromBusinessUnitUsersModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#phaseMembersPostPhaseMembersFromBusinessUnitUsers");
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
| **addToAllSubPhases** | **Boolean**| Optional: Add member to all sub phases. Default true. | [optional] [default to true] |
| **phaseMembersFromBusinessUnitUsersModel** | [**PhaseMembersFromBusinessUnitUsersModel**](PhaseMembersFromBusinessUnitUsersModel.md)| PhaseMemberModel. | [optional] |

### Return type

[**List&lt;PhaseMemberModel&gt;**](PhaseMemberModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of added members. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="phasesPatchPhase"></a>
# **phasesPatchPhase**
> List&lt;PhaseOutputModel&gt; phasesPatchPhase(guid, patchOperation)

Update (Patch) a phase or a part of it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the phase
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of PhaseInputModel
    try {
      List<PhaseOutputModel> result = apiInstance.phasesPatchPhase(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#phasesPatchPhase");
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
| **guid** | **String**| ID of the phase | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of PhaseInputModel | [optional] |

### Return type

[**List&lt;PhaseOutputModel&gt;**](PhaseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated phase |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="phasesPostPhase"></a>
# **phasesPostPhase**
> PhaseOutputModel phasesPostPhase(phaseInputModel)

Insert a phase

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    PhaseInputModel phaseInputModel = new PhaseInputModel(); // PhaseInputModel | PhaseOutputModel
    try {
      PhaseOutputModel result = apiInstance.phasesPostPhase(phaseInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#phasesPostPhase");
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
| **phaseInputModel** | [**PhaseInputModel**](PhaseInputModel.md)| PhaseOutputModel | [optional] |

### Return type

[**PhaseOutputModel**](PhaseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created phase |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="priceListsPostCustomPricelist"></a>
# **priceListsPostCustomPricelist**
> CustomPriceListOutputModel priceListsPostCustomPricelist(projectGuid, isVolumePricing)

Create custom price list for a project. If project already has a custom price list returns existing price list. Creates a new price list if project doesn&#39;t have a custom price list. Project can only have one custom price list. Note that project&#39;s price list will be changed to the custom price list created here and also existing prices are copied to the new price list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | ID of the project.
    Boolean isVolumePricing = false; // Boolean | Get the custom volume pricing price list or regular custom price list. Default is false.
    try {
      CustomPriceListOutputModel result = apiInstance.priceListsPostCustomPricelist(projectGuid, isVolumePricing);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#priceListsPostCustomPricelist");
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
| **isVolumePricing** | **Boolean**| Get the custom volume pricing price list or regular custom price list. Default is false. | [optional] [default to false] |

### Return type

[**CustomPriceListOutputModel**](CustomPriceListOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectCustomValuesPatchProjectCustomValue"></a>
# **projectCustomValuesPatchProjectCustomValue**
> List&lt;ProjectCustomValueModel&gt; projectCustomValuesPatchProjectCustomValue(guid, patchOperation)

Update (Patch) a project custom value or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the project custom value Can also be comma separate list of IDs to patch multiple project custom values with one call. When multiple IDs are given, returns model which has list of succeeded project custom values and list of errors.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of ProjectCustomValueModel.
    try {
      List<ProjectCustomValueModel> result = apiInstance.projectCustomValuesPatchProjectCustomValue(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#projectCustomValuesPatchProjectCustomValue");
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
| **guid** | **String**| ID of the project custom value Can also be comma separate list of IDs to patch multiple project custom values with one call. When multiple IDs are given, returns model which has list of succeeded project custom values and list of errors. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of ProjectCustomValueModel. | [optional] |

### Return type

[**List&lt;ProjectCustomValueModel&gt;**](ProjectCustomValueModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated project custom values. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectCustomValuesPostProjectCustomValue"></a>
# **projectCustomValuesPostProjectCustomValue**
> List&lt;ProjectCustomValueModel&gt; projectCustomValuesPostProjectCustomValue(projectCustomValueModel)

Insert a project custom value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    ProjectCustomValueModel projectCustomValueModel = new ProjectCustomValueModel(); // ProjectCustomValueModel | ProjectCustomValueModel.
    try {
      List<ProjectCustomValueModel> result = apiInstance.projectCustomValuesPostProjectCustomValue(projectCustomValueModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#projectCustomValuesPostProjectCustomValue");
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
| **projectCustomValueModel** | [**ProjectCustomValueModel**](ProjectCustomValueModel.md)| ProjectCustomValueModel. | [optional] |

### Return type

[**List&lt;ProjectCustomValueModel&gt;**](ProjectCustomValueModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created project custom value. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectForecastsPatchForecast"></a>
# **projectForecastsPatchForecast**
> List&lt;ProjectForecastOutputModel&gt; projectForecastsPatchForecast(guid, patchOperation)

Update (Patch) an project forecast or a part of it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the project forecast
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of ProjectForecastInputModel
    try {
      List<ProjectForecastOutputModel> result = apiInstance.projectForecastsPatchForecast(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#projectForecastsPatchForecast");
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
| **guid** | **String**| ID of the project forecast | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of ProjectForecastInputModel | [optional] |

### Return type

[**List&lt;ProjectForecastOutputModel&gt;**](ProjectForecastOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated Project forecast |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectForecastsPostForecast"></a>
# **projectForecastsPostForecast**
> ProjectForecastOutputModel projectForecastsPostForecast(projectForecastInputModel)

Insert a project forecast

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    ProjectForecastInputModel projectForecastInputModel = new ProjectForecastInputModel(); // ProjectForecastInputModel | ProjectForecastOutputInputModel
    try {
      ProjectForecastOutputModel result = apiInstance.projectForecastsPostForecast(projectForecastInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#projectForecastsPostForecast");
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
| **projectForecastInputModel** | [**ProjectForecastInputModel**](ProjectForecastInputModel.md)| ProjectForecastOutputInputModel | [optional] |

### Return type

[**ProjectForecastOutputModel**](ProjectForecastOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Project forecast |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectInvoiceSettingsPatchProjectInvoiceSettings_0"></a>
# **projectInvoiceSettingsPatchProjectInvoiceSettings_0**
> List&lt;ProjectInvoiceSettingsOutputModel&gt; projectInvoiceSettingsPatchProjectInvoiceSettings_0(guid, patchOperation)

Update (Patch) project invoice settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the project invoice settings.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of ProjectInvoiceSettingsInputModel.
    try {
      List<ProjectInvoiceSettingsOutputModel> result = apiInstance.projectInvoiceSettingsPatchProjectInvoiceSettings_0(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#projectInvoiceSettingsPatchProjectInvoiceSettings_0");
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
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of ProjectInvoiceSettingsInputModel. | [optional] |

### Return type

[**List&lt;ProjectInvoiceSettingsOutputModel&gt;**](ProjectInvoiceSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project invoice settings. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectInvoiceSettingsPostProjectInvoiceSettings_0"></a>
# **projectInvoiceSettingsPostProjectInvoiceSettings_0**
> ProjectInvoiceSettingsOutputModel projectInvoiceSettingsPostProjectInvoiceSettings_0(projectInvoiceSettingsInputModel)

Create a new project invoice settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    ProjectInvoiceSettingsInputModel projectInvoiceSettingsInputModel = new ProjectInvoiceSettingsInputModel(); // ProjectInvoiceSettingsInputModel | Project invoice settings.
    try {
      ProjectInvoiceSettingsOutputModel result = apiInstance.projectInvoiceSettingsPostProjectInvoiceSettings_0(projectInvoiceSettingsInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#projectInvoiceSettingsPostProjectInvoiceSettings_0");
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
| **projectInvoiceSettingsInputModel** | [**ProjectInvoiceSettingsInputModel**](ProjectInvoiceSettingsInputModel.md)| Project invoice settings. | [optional] |

### Return type

[**ProjectInvoiceSettingsOutputModel**](ProjectInvoiceSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created project invoice settings. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectProductsPostProjectProduct"></a>
# **projectProductsPostProjectProduct**
> ProjectProductOutputModel projectProductsPostProjectProduct(projectProductInputModel)

Adds a product to a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    ProjectProductInputModel projectProductInputModel = new ProjectProductInputModel(); // ProjectProductInputModel | projectProductModel
    try {
      ProjectProductOutputModel result = apiInstance.projectProductsPostProjectProduct(projectProductInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#projectProductsPostProjectProduct");
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
| **projectProductInputModel** | [**ProjectProductInputModel**](ProjectProductInputModel.md)| projectProductModel | [optional] |

### Return type

[**ProjectProductOutputModel**](ProjectProductOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Added project product |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectWorkHourPricesPatchProjectWorkHourPrice"></a>
# **projectWorkHourPricesPatchProjectWorkHourPrice**
> List&lt;ProjectWorkHourPriceOutputModel&gt; projectWorkHourPricesPatchProjectWorkHourPrice(guid, patchOperation)

Update (Patch) a work hour price or a part of it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the work hour price
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of ProjectWorkHourPriceInputModel
    try {
      List<ProjectWorkHourPriceOutputModel> result = apiInstance.projectWorkHourPricesPatchProjectWorkHourPrice(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#projectWorkHourPricesPatchProjectWorkHourPrice");
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
| **guid** | **String**| ID of the work hour price | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of ProjectWorkHourPriceInputModel | [optional] |

### Return type

[**List&lt;ProjectWorkHourPriceOutputModel&gt;**](ProjectWorkHourPriceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated work hour prices |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectWorkHourPricesPostProjectWorkHourPrice"></a>
# **projectWorkHourPricesPostProjectWorkHourPrice**
> ProjectWorkHourPriceOutputModel projectWorkHourPricesPostProjectWorkHourPrice(projectWorkHourPriceInputModel)

Insert a work hour price

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    ProjectWorkHourPriceInputModel projectWorkHourPriceInputModel = new ProjectWorkHourPriceInputModel(); // ProjectWorkHourPriceInputModel | ProjectWorkHourPriceInputModel
    try {
      ProjectWorkHourPriceOutputModel result = apiInstance.projectWorkHourPricesPostProjectWorkHourPrice(projectWorkHourPriceInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#projectWorkHourPricesPostProjectWorkHourPrice");
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
| **projectWorkHourPriceInputModel** | [**ProjectWorkHourPriceInputModel**](ProjectWorkHourPriceInputModel.md)| ProjectWorkHourPriceInputModel | [optional] |

### Return type

[**ProjectWorkHourPriceOutputModel**](ProjectWorkHourPriceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created work hour prices |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectWorkTypesPatchProjectWorktype"></a>
# **projectWorkTypesPatchProjectWorktype**
> List&lt;ProjectWorkTypeModel&gt; projectWorkTypesPatchProjectWorktype(guid, patchOperation)

Update (patch) a project work type.

This currently can be used only to change the default work type in a project. The \&quot;UseWorktypesFromSetting\&quot; flag for the Project should be false (the project should not use the organization list of work types).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the project work type.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of ProjectWorkTypeModel.
    try {
      List<ProjectWorkTypeModel> result = apiInstance.projectWorkTypesPatchProjectWorktype(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#projectWorkTypesPatchProjectWorktype");
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
| **guid** | **String**| ID of the project work type. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of ProjectWorkTypeModel. | [optional] |

### Return type

[**List&lt;ProjectWorkTypeModel&gt;**](ProjectWorkTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated project work types. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectWorkTypesPostProjectWorktype"></a>
# **projectWorkTypesPostProjectWorktype**
> ProjectWorkTypeModel projectWorkTypesPostProjectWorktype(projectWorkTypeModel)

Adds a work type to a project.

The \&quot;UseWorktypesFromSetting\&quot; flag for the Project should be false (the project should not use the organization list of work types).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    ProjectWorkTypeModel projectWorkTypeModel = new ProjectWorkTypeModel(); // ProjectWorkTypeModel | ProjectWorkTypeModel.
    try {
      ProjectWorkTypeModel result = apiInstance.projectWorkTypesPostProjectWorktype(projectWorkTypeModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#projectWorkTypesPostProjectWorktype");
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
| **projectWorkTypeModel** | [**ProjectWorkTypeModel**](ProjectWorkTypeModel.md)| ProjectWorkTypeModel. | [optional] |

### Return type

[**ProjectWorkTypeModel**](ProjectWorkTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Added project work type. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectsPatchProject"></a>
# **projectsPatchProject**
> List&lt;ProjectOutputModel&gt; projectsPatchProject(guid, patchOperation)

Update (Patch) a project or a part of it

To update current project status, give ProjectStatusTypeGuid and possibly Description. To update current sales status, give SalesStatusTypeGuid (

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the project
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of ProjectInputModel
    try {
      List<ProjectOutputModel> result = apiInstance.projectsPatchProject(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#projectsPatchProject");
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
| **guid** | **String**| ID of the project | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of ProjectInputModel | [optional] |

### Return type

[**List&lt;ProjectOutputModel&gt;**](ProjectOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated projects |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectsPostProject"></a>
# **projectsPostProject**
> ProjectOutputModel projectsPostProject(projectInputModelBase)

Insert a project

When creating a new project, the price list property will be ignored, as it is chosen by default.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    ProjectInputModelBase projectInputModelBase = new ProjectInputModelBase(); // ProjectInputModelBase | ProjectInputModelBase
    try {
      ProjectOutputModel result = apiInstance.projectsPostProject(projectInputModelBase);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#projectsPostProject");
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
| **projectInputModelBase** | [**ProjectInputModelBase**](ProjectInputModelBase.md)| ProjectInputModelBase | [optional] |

### Return type

[**ProjectOutputModel**](ProjectOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created project |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalFeesPatchProposalFee"></a>
# **proposalFeesPatchProposalFee**
> List&lt;ProposalFeeRowOutputModel&gt; proposalFeesPatchProposalFee(guid, patchOperation)

Update (Patch) a proposal fee row or a part of it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the proposal fee row
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of ProposalFeeModel
    try {
      List<ProposalFeeRowOutputModel> result = apiInstance.proposalFeesPatchProposalFee(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#proposalFeesPatchProposalFee");
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
| **guid** | **String**| ID of the proposal fee row | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of ProposalFeeModel | [optional] |

### Return type

[**List&lt;ProposalFeeRowOutputModel&gt;**](ProposalFeeRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated proposal fee rows |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalFeesPostProposalFee"></a>
# **proposalFeesPostProposalFee**
> ProposalFeeRowOutputModel proposalFeesPostProposalFee(proposalFeeRowInputModel)

Insert a proposal fee row.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    ProposalFeeRowInputModel proposalFeeRowInputModel = new ProposalFeeRowInputModel(); // ProposalFeeRowInputModel | ProposalFeeModel
    try {
      ProposalFeeRowOutputModel result = apiInstance.proposalFeesPostProposalFee(proposalFeeRowInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#proposalFeesPostProposalFee");
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
| **proposalFeeRowInputModel** | [**ProposalFeeRowInputModel**](ProposalFeeRowInputModel.md)| ProposalFeeModel | [optional] |

### Return type

[**ProposalFeeRowOutputModel**](ProposalFeeRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created proposal fee row. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalSettingsPatchProposalSettings"></a>
# **proposalSettingsPatchProposalSettings**
> List&lt;ProposalSettingsOutputModel&gt; proposalSettingsPatchProposalSettings(guid, patchOperation)

Update (Patch) proposal settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    String guid = "guid_example"; // String | Guid of the Proposal
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of ProposalSettingsInputModel
    try {
      List<ProposalSettingsOutputModel> result = apiInstance.proposalSettingsPatchProposalSettings(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#proposalSettingsPatchProposalSettings");
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
| **guid** | **String**| Guid of the Proposal | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of ProposalSettingsInputModel | [optional] |

### Return type

[**List&lt;ProposalSettingsOutputModel&gt;**](ProposalSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated Proposal settings |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalSubtotalsPatchProposalSubtotal"></a>
# **proposalSubtotalsPatchProposalSubtotal**
> List&lt;ProposalSubtotalOutputModel&gt; proposalSubtotalsPatchProposalSubtotal(guid, patchOperation)

Update (Patch) a Proposal subtotal or a part of it

It is not possible to changed the proposalGuid for an existing proposal subtotal. Also, when a proposal subtotal is connected to a phase, the connection can only be broken if the phase is deleted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the Proposal subtotal
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of ProposalSubtotalModel
    try {
      List<ProposalSubtotalOutputModel> result = apiInstance.proposalSubtotalsPatchProposalSubtotal(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#proposalSubtotalsPatchProposalSubtotal");
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
| **guid** | **String**| ID of the Proposal subtotal | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of ProposalSubtotalModel | [optional] |

### Return type

[**List&lt;ProposalSubtotalOutputModel&gt;**](ProposalSubtotalOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated Proposal subtotals |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalSubtotalsPostProposalSubtotal"></a>
# **proposalSubtotalsPostProposalSubtotal**
> ProposalSubtotalOutputModel proposalSubtotalsPostProposalSubtotal(proposalSubtotalInputModel)

Insert a proposal subtotal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    ProposalSubtotalInputModel proposalSubtotalInputModel = new ProposalSubtotalInputModel(); // ProposalSubtotalInputModel | ProposalSubtotalModel
    try {
      ProposalSubtotalOutputModel result = apiInstance.proposalSubtotalsPostProposalSubtotal(proposalSubtotalInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#proposalSubtotalsPostProposalSubtotal");
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
| **proposalSubtotalInputModel** | [**ProposalSubtotalInputModel**](ProposalSubtotalInputModel.md)| ProposalSubtotalModel | [optional] |

### Return type

[**ProposalSubtotalOutputModel**](ProposalSubtotalOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created proposal subtotal. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalWorkhoursPatchProposalWorkhour"></a>
# **proposalWorkhoursPatchProposalWorkhour**
> List&lt;ProposalWorkhourRowOutputModel&gt; proposalWorkhoursPatchProposalWorkhour(guid, patchOperation)

Update (Patch) a proposal work row or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the proposal work row.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of ProposalWorkhourModel.
    try {
      List<ProposalWorkhourRowOutputModel> result = apiInstance.proposalWorkhoursPatchProposalWorkhour(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#proposalWorkhoursPatchProposalWorkhour");
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
| **guid** | **String**| ID of the proposal work row. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of ProposalWorkhourModel. | [optional] |

### Return type

[**List&lt;ProposalWorkhourRowOutputModel&gt;**](ProposalWorkhourRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updated proposal work row. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalWorkhoursPostProposalWorkhour"></a>
# **proposalWorkhoursPostProposalWorkhour**
> ProposalWorkhourRowOutputModel proposalWorkhoursPostProposalWorkhour(proposalWorkhourRowInputModel)

Insert a proposal work row.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    ProposalWorkhourRowInputModel proposalWorkhourRowInputModel = new ProposalWorkhourRowInputModel(); // ProposalWorkhourRowInputModel | ProposalWorkhourModel
    try {
      ProposalWorkhourRowOutputModel result = apiInstance.proposalWorkhoursPostProposalWorkhour(proposalWorkhourRowInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#proposalWorkhoursPostProposalWorkhour");
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
| **proposalWorkhourRowInputModel** | [**ProposalWorkhourRowInputModel**](ProposalWorkhourRowInputModel.md)| ProposalWorkhourModel | [optional] |

### Return type

[**ProposalWorkhourRowOutputModel**](ProposalWorkhourRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created proposal work row. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalsPatchProposal"></a>
# **proposalsPatchProposal**
> List&lt;ProposalOutputModel&gt; proposalsPatchProposal(guid, patchOperation)

Update (Patch) a Proposal or a part of it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    String guid = "guid_example"; // String | Guid of the Proposal
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of ProposalInputModel
    try {
      List<ProposalOutputModel> result = apiInstance.proposalsPatchProposal(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#proposalsPatchProposal");
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
| **guid** | **String**| Guid of the Proposal | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of ProposalInputModel | [optional] |

### Return type

[**List&lt;ProposalOutputModel&gt;**](ProposalOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated Proposals |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalsPostProposal"></a>
# **proposalsPostProposal**
> ProposalOutputModel proposalsPostProposal(proposalInputModel)

Insert a proposal.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    ProposalInputModel proposalInputModel = new ProposalInputModel(); // ProposalInputModel | ProposalInputModel
    try {
      ProposalOutputModel result = apiInstance.proposalsPostProposal(proposalInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#proposalsPostProposal");
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
| **proposalInputModel** | [**ProposalInputModel**](ProposalInputModel.md)| ProposalInputModel | [optional] |

### Return type

[**ProposalOutputModel**](ProposalOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created proposal. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="salesNotesPatchProjectSalesNote"></a>
# **salesNotesPatchProjectSalesNote**
> List&lt;ProjectSalesNoteOutputModel&gt; salesNotesPatchProjectSalesNote(guid, patchOperation)

Update (Patch) a project sales note or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the project sales note.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of project sales note model.
    try {
      List<ProjectSalesNoteOutputModel> result = apiInstance.salesNotesPatchProjectSalesNote(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#salesNotesPatchProjectSalesNote");
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
| **guid** | **String**| ID of the project sales note. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of project sales note model. | [optional] |

### Return type

[**List&lt;ProjectSalesNoteOutputModel&gt;**](ProjectSalesNoteOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated sales notes. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="salesNotesPostProjectSalesNotes"></a>
# **salesNotesPostProjectSalesNotes**
> ProjectSalesNoteOutputModel salesNotesPostProjectSalesNotes(projectSalesNoteInputModel)

Insert a project sales note.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsWriteApi;

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

    ProjectsWriteApi apiInstance = new ProjectsWriteApi(defaultClient);
    ProjectSalesNoteInputModel projectSalesNoteInputModel = new ProjectSalesNoteInputModel(); // ProjectSalesNoteInputModel | SalesNoteOutputModel
    try {
      ProjectSalesNoteOutputModel result = apiInstance.salesNotesPostProjectSalesNotes(projectSalesNoteInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsWriteApi#salesNotesPostProjectSalesNotes");
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
| **projectSalesNoteInputModel** | [**ProjectSalesNoteInputModel**](ProjectSalesNoteInputModel.md)| SalesNoteOutputModel | [optional] |

### Return type

[**ProjectSalesNoteOutputModel**](ProjectSalesNoteOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created project sales note. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

