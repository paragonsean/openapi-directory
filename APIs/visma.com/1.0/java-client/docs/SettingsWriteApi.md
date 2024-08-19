# SettingsWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activityTypesPatchActivityType**](SettingsWriteApi.md#activityTypesPatchActivityType) | **PATCH** /v1/activitytypes/{guid} | Update (Patch) an Activity Type or a part of it |
| [**activityTypesPostActivityType**](SettingsWriteApi.md#activityTypesPostActivityType) | **POST** /v1/activitytypes | Insert an Activity type. |
| [**businessUnitsPatchBusinessUnit**](SettingsWriteApi.md#businessUnitsPatchBusinessUnit) | **PATCH** /v1/businessunits/{guid} | Update (Patch) an businessUnit or a part of it. |
| [**communicationTypesPatchCommunicationType**](SettingsWriteApi.md#communicationTypesPatchCommunicationType) | **PATCH** /v1/communicationtypes/{guid} | Update (Patch) a communication type or a part of it. |
| [**communicationTypesPostCommunicationType**](SettingsWriteApi.md#communicationTypesPostCommunicationType) | **POST** /v1/communicationtypes | Insert a communication type. |
| [**contactRolesPatchContactRole**](SettingsWriteApi.md#contactRolesPatchContactRole) | **PATCH** /v1/contactroles/{guid} | Update (Patch) a contact role or a part of it. |
| [**contactRolesPostContactRole**](SettingsWriteApi.md#contactRolesPostContactRole) | **POST** /v1/contactroles | Insert a contact role. |
| [**costAccountsPatchCostAccount**](SettingsWriteApi.md#costAccountsPatchCostAccount) | **PATCH** /v1/costaccounts/{guid} | Update (Patch) a cost account or a part of it. |
| [**costAccountsPostCostAccount**](SettingsWriteApi.md#costAccountsPostCostAccount) | **POST** /v1/costaccounts | Insert a cost account. |
| [**costCentersPatchCostCenter**](SettingsWriteApi.md#costCentersPatchCostCenter) | **PATCH** /v1/costcenters/{guid} | Update (Patch) a cost center or a part of it. |
| [**costCentersPostCostCenter**](SettingsWriteApi.md#costCentersPostCostCenter) | **POST** /v1/costcenters | Insert a cost center. |
| [**currenciesPatchCurrency**](SettingsWriteApi.md#currenciesPatchCurrency) | **PATCH** /v1/currencies/{guid} | Update (Patch) an currency or a part of it. |
| [**customerCustomPropertiesPatchCustomerCustomProperty**](SettingsWriteApi.md#customerCustomPropertiesPatchCustomerCustomProperty) | **PATCH** /v1/customers/customproperties/{guid} | Update (Patch) a customer custom property or a part of it. |
| [**customerCustomPropertiesPostCustomerCustomProperty**](SettingsWriteApi.md#customerCustomPropertiesPostCustomerCustomProperty) | **POST** /v1/customers/customproperties | Insert a customer custom property. |
| [**customerCustomPropertySelectionItemsPatchCustomerCustomPropertySelectionItem**](SettingsWriteApi.md#customerCustomPropertySelectionItemsPatchCustomerCustomPropertySelectionItem) | **PATCH** /v1/customers/customproperties/customercustompropertyselectionitems/{guid} | Update (Patch) a customer custom property selection item or a part of it. |
| [**customerCustomPropertySelectionItemsPostCustomerCustomPropertySelectionItem**](SettingsWriteApi.md#customerCustomPropertySelectionItemsPostCustomerCustomPropertySelectionItem) | **POST** /v1/customers/customproperties/customercustompropertyselectionitems | Insert a customer custom property selection item. |
| [**industriesPatchIndustry**](SettingsWriteApi.md#industriesPatchIndustry) | **PATCH** /v1/industries/{guid} | Update (Patch) an industry or a part of it. |
| [**industriesPostIndustry**](SettingsWriteApi.md#industriesPostIndustry) | **POST** /v1/industries | Insert an industry. |
| [**invoiceStatusesPatchInvoiceStatus**](SettingsWriteApi.md#invoiceStatusesPatchInvoiceStatus) | **PATCH** /v1/invoicestatuses/{guid} | Update (Patch) an Invoice status or a part of it. |
| [**invoiceStatusesPostInvoiceStatus**](SettingsWriteApi.md#invoiceStatusesPostInvoiceStatus) | **POST** /v1/invoicestatuses | Insert a invoice status. |
| [**keywordsPatchKeyword**](SettingsWriteApi.md#keywordsPatchKeyword) | **PATCH** /v1/keywords/{guid} | Update (Patch) a keyword or a part of it. |
| [**keywordsPostKeyword**](SettingsWriteApi.md#keywordsPostKeyword) | **POST** /v1/keywords | Insert a keyword. |
| [**leadSourcesPatchLeadSource**](SettingsWriteApi.md#leadSourcesPatchLeadSource) | **PATCH** /v1/leadsources/{guid} | Update (Patch) an lead source or a part of it. |
| [**leadSourcesPostLeadSource**](SettingsWriteApi.md#leadSourcesPostLeadSource) | **POST** /v1/leadsources | Insert a lead source. |
| [**marketSegmentsPatchMarketSegment**](SettingsWriteApi.md#marketSegmentsPatchMarketSegment) | **PATCH** /v1/marketsegments/{guid} | Update (Patch) an Market Segment or a part of it. |
| [**marketSegmentsPostMarketSegment**](SettingsWriteApi.md#marketSegmentsPostMarketSegment) | **POST** /v1/marketsegments | Insert a market segment. |
| [**overtimesPatchOvertime**](SettingsWriteApi.md#overtimesPatchOvertime) | **PATCH** /v1/overtimes/{guid} | Update (Patch) an overtime or a part of it. |
| [**overtimesPostOvertime**](SettingsWriteApi.md#overtimesPostOvertime) | **POST** /v1/overtimes | Insert an overtime. |
| [**phaseStatusTypesPatchPhaseStatusType**](SettingsWriteApi.md#phaseStatusTypesPatchPhaseStatusType) | **PATCH** /v1/phasestatustypes/{guid} | Update (Patch) a phase status type or a part of it |
| [**phaseStatusTypesPostPhaseStatusType**](SettingsWriteApi.md#phaseStatusTypesPostPhaseStatusType) | **POST** /v1/phasestatustypes | Insert a phase status type |
| [**productCategoriesPatchProductCategory**](SettingsWriteApi.md#productCategoriesPatchProductCategory) | **PATCH** /v1/productcategories/{guid} | Update (Patch) a product category or a part of it. |
| [**productCategoriesPostProductCategory**](SettingsWriteApi.md#productCategoriesPostProductCategory) | **POST** /v1/productcategories | Insert a product category. |
| [**productCountrySettingsPatchProductCountrySettings**](SettingsWriteApi.md#productCountrySettingsPatchProductCountrySettings) | **PATCH** /v1/productcountrysettings/{guid} | Update (Patch) a product country setting |
| [**productCountrySettingsPostProductCountrySettings**](SettingsWriteApi.md#productCountrySettingsPostProductCountrySettings) | **POST** /v1/productcountrysettings | Insert a product country setting |
| [**productsPatchProduct**](SettingsWriteApi.md#productsPatchProduct) | **PATCH** /v1/products/{guid} | Update (Patch) an product or a part of it. |
| [**productsPostProduct**](SettingsWriteApi.md#productsPostProduct) | **POST** /v1/products | Insert a product. |
| [**projectBillingCustomersPatchProjectBillingCustomer**](SettingsWriteApi.md#projectBillingCustomersPatchProjectBillingCustomer) | **PATCH** /v1/projectbillingcustomers/{guid} | Update (Patch) a project billing customer. |
| [**projectBillingCustomersPostProjectBillingCustomer**](SettingsWriteApi.md#projectBillingCustomersPostProjectBillingCustomer) | **POST** /v1/projectbillingcustomers | Insert a billing customer for a project. |
| [**projectCustomPropertiesPatchProjectCustomProperty**](SettingsWriteApi.md#projectCustomPropertiesPatchProjectCustomProperty) | **PATCH** /v1/projects/customproperties/{guid} | Update (Patch) a project custom property or a part of it. |
| [**projectCustomPropertiesPostProjectCustomProperty**](SettingsWriteApi.md#projectCustomPropertiesPostProjectCustomProperty) | **POST** /v1/projects/customproperties | Insert a project custom property. |
| [**projectCustomPropertySelectionItemsPatchProjectCustomPropertySelectionItem**](SettingsWriteApi.md#projectCustomPropertySelectionItemsPatchProjectCustomPropertySelectionItem) | **PATCH** /v1/projects/customproperties/projectcustompropertyselectionitems/{guid} | Update (Patch) a project custom property selection item or a part of it. |
| [**projectCustomPropertySelectionItemsPostProjectCustomPropertySelectionItem**](SettingsWriteApi.md#projectCustomPropertySelectionItemsPostProjectCustomPropertySelectionItem) | **POST** /v1/projects/customproperties/projectcustompropertyselectionitems | Insert a project custom property selection item. |
| [**projectMemberCostExceptionsPatch**](SettingsWriteApi.md#projectMemberCostExceptionsPatch) | **PATCH** /v1/projectmembercostexceptions/{guid} | Update (Patch) project member cost exception. |
| [**projectMemberCostExceptionsPost**](SettingsWriteApi.md#projectMemberCostExceptionsPost) | **POST** /v1/projectmembercostexceptions | Add a cost exception to a project member. |
| [**projectStatusTypesPatchProjectStatusType**](SettingsWriteApi.md#projectStatusTypesPatchProjectStatusType) | **PATCH** /v1/projectstatustypes/{guid} | Update (Patch) a projectStatusType or a part of it |
| [**projectStatusTypesPostProjectStatusType**](SettingsWriteApi.md#projectStatusTypesPostProjectStatusType) | **POST** /v1/projectstatustypes | Insert a project status type |
| [**projectTaskStatusesPatchProjectTaskStatus**](SettingsWriteApi.md#projectTaskStatusesPatchProjectTaskStatus) | **PATCH** /v1/projecttaskstatuses/{guid} | Update (Patch) an Project task status or a part of it. |
| [**projectTaskStatusesPostProjectTaskStatus**](SettingsWriteApi.md#projectTaskStatusesPostProjectTaskStatus) | **POST** /v1/projecttaskstatuses | Insert a project task status. |
| [**proposalStatusesPatchProposalStatus**](SettingsWriteApi.md#proposalStatusesPatchProposalStatus) | **PATCH** /v1/proposalstatuses/{guid} | Update (Patch) an Proposal status or a part of it |
| [**proposalStatusesPostProposalStatus**](SettingsWriteApi.md#proposalStatusesPostProposalStatus) | **POST** /v1/proposalstatuses | Insert a proposal status |
| [**rolesPatchRole**](SettingsWriteApi.md#rolesPatchRole) | **PATCH** /v1/roles/{guid} | Update (Patch) a role or a part of it. |
| [**rolesPostRole**](SettingsWriteApi.md#rolesPostRole) | **POST** /v1/roles | Insert a role. |
| [**salesAccountsPatchSalesAccount**](SettingsWriteApi.md#salesAccountsPatchSalesAccount) | **PATCH** /v1/salesaccounts/{guid} | Update (Patch) a sales account or a part of it. |
| [**salesAccountsPostSalesAccount**](SettingsWriteApi.md#salesAccountsPostSalesAccount) | **POST** /v1/salesaccounts | Insert a sales account. |
| [**salesStatusTypesPatchSalesStatusType**](SettingsWriteApi.md#salesStatusTypesPatchSalesStatusType) | **PATCH** /v1/salesstatustypes/{guid} | Update (Patch) an sales status type or a part of it |
| [**salesStatusTypesPostSalesStatusType**](SettingsWriteApi.md#salesStatusTypesPostSalesStatusType) | **POST** /v1/salesstatustypes | Insert a sales status type |
| [**timeEntryTypesPatchTimeEntryType**](SettingsWriteApi.md#timeEntryTypesPatchTimeEntryType) | **PATCH** /v1/timeentrytypes/{guid} | Update (Patch) a time entry type or a part of it. |
| [**timeEntryTypesPostTimeEntryType**](SettingsWriteApi.md#timeEntryTypesPostTimeEntryType) | **POST** /v1/timeentrytypes | Insert a time entry type. |
| [**travelExpenseTypeCountrySettingsPatchTravelExpenseTypeCountrySettings**](SettingsWriteApi.md#travelExpenseTypeCountrySettingsPatchTravelExpenseTypeCountrySettings) | **PATCH** /v1/travelexpensetypecountrysettings/{guid} | Update (Patch) a travel expense type country setting |
| [**travelExpenseTypeCountrySettingsPostTravelExpenseTypeCountrySettings**](SettingsWriteApi.md#travelExpenseTypeCountrySettingsPostTravelExpenseTypeCountrySettings) | **POST** /v1/travelexpensetypecountrysettings | Insert a travel expense type country setting |
| [**travelExpenseTypesPatchTravelExpenseType**](SettingsWriteApi.md#travelExpenseTypesPatchTravelExpenseType) | **PATCH** /v1/travelexpensetypes/{guid} | Update (Patch) an travel expense type or a part of it. |
| [**travelExpenseTypesPostTravelExpenseType**](SettingsWriteApi.md#travelExpenseTypesPostTravelExpenseType) | **POST** /v1/travelexpensetypes | Insert a new travel expense type. |
| [**travelReimbursementStatusPatchTravelReimbursementStatus**](SettingsWriteApi.md#travelReimbursementStatusPatchTravelReimbursementStatus) | **PATCH** /v1/travelreimbursementstatuses/{guid} | Update (Patch) a travel reimbursement status or a part of it. |
| [**travelReimbursementStatusPostTravelReimbursementStatus**](SettingsWriteApi.md#travelReimbursementStatusPostTravelReimbursementStatus) | **POST** /v1/travelreimbursementstatuses | Insert a travel reimbursement status. |
| [**userCustomPropertiesPatchUserCustomProperty**](SettingsWriteApi.md#userCustomPropertiesPatchUserCustomProperty) | **PATCH** /v1/users/customproperties/{guid} | Update (Patch) a user custom property or a part of it. |
| [**userCustomPropertiesPostUserCustomProperty**](SettingsWriteApi.md#userCustomPropertiesPostUserCustomProperty) | **POST** /v1/users/customproperties | Insert a user custom property. |
| [**userCustomPropertySelectionItemsPatchUserCustomPropertySelectionItem**](SettingsWriteApi.md#userCustomPropertySelectionItemsPatchUserCustomPropertySelectionItem) | **PATCH** /v1/users/customproperties/usercustompropertyselectionitems/{guid} | Update (Patch) a user custom property selection item or a part of it. |
| [**userCustomPropertySelectionItemsPostUserCustomPropertySelectionItem**](SettingsWriteApi.md#userCustomPropertySelectionItemsPostUserCustomPropertySelectionItem) | **POST** /v1/users/customproperties/usercustompropertyselectionitems | Insert a user custom property selection item. |
| [**vatRatesPatchVatRate**](SettingsWriteApi.md#vatRatesPatchVatRate) | **PATCH** /v1/vatrates/{guid} | Update (Patch) a vat rate or a part of it |
| [**vatRatesPostVatRate**](SettingsWriteApi.md#vatRatesPostVatRate) | **POST** /v1/vatrates | Insert a vat rate |
| [**workContractsPatchWorkContract**](SettingsWriteApi.md#workContractsPatchWorkContract) | **PATCH** /v1/workcontracts/{guid} | Update (Patch) a work contract or a part of it. |
| [**workContractsPostWorkContract**](SettingsWriteApi.md#workContractsPostWorkContract) | **POST** /v1/workcontracts | Insert a work contract. |
| [**workTypesPatchWorkType**](SettingsWriteApi.md#workTypesPatchWorkType) | **PATCH** /v1/worktypes/{guid} | Update (Patch) a work type or a part of it. |
| [**workTypesPostWorkType**](SettingsWriteApi.md#workTypesPostWorkType) | **POST** /v1/worktypes | Insert a work type. |


<a id="activityTypesPatchActivityType"></a>
# **activityTypesPatchActivityType**
> List&lt;ActivityTypeModel&gt; activityTypesPatchActivityType(guid, patchOperation)

Update (Patch) an Activity Type or a part of it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the Activity Type
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of ActivityTypeModel
    try {
      List<ActivityTypeModel> result = apiInstance.activityTypesPatchActivityType(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#activityTypesPatchActivityType");
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
| **guid** | **String**| ID of the Activity Type | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of ActivityTypeModel | [optional] |

### Return type

[**List&lt;ActivityTypeModel&gt;**](ActivityTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated Activity Types |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="activityTypesPostActivityType"></a>
# **activityTypesPostActivityType**
> ActivityTypeModel activityTypesPostActivityType(activityTypeModel)

Insert an Activity type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    ActivityTypeModel activityTypeModel = new ActivityTypeModel(); // ActivityTypeModel | Activity type
    try {
      ActivityTypeModel result = apiInstance.activityTypesPostActivityType(activityTypeModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#activityTypesPostActivityType");
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
| **activityTypeModel** | [**ActivityTypeModel**](ActivityTypeModel.md)| Activity type | [optional] |

### Return type

[**ActivityTypeModel**](ActivityTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Inserted ActivityType |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="businessUnitsPatchBusinessUnit"></a>
# **businessUnitsPatchBusinessUnit**
> List&lt;BusinessUnitModel&gt; businessUnitsPatchBusinessUnit(guid, patchOperation)

Update (Patch) an businessUnit or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the businessUnit.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of BusinessUnitModel.
    try {
      List<BusinessUnitModel> result = apiInstance.businessUnitsPatchBusinessUnit(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#businessUnitsPatchBusinessUnit");
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
| **guid** | **String**| ID of the businessUnit. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of BusinessUnitModel. | [optional] |

### Return type

[**List&lt;BusinessUnitModel&gt;**](BusinessUnitModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated business units. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="communicationTypesPatchCommunicationType"></a>
# **communicationTypesPatchCommunicationType**
> List&lt;CommunicationTypeModel&gt; communicationTypesPatchCommunicationType(guid, patchOperation)

Update (Patch) a communication type or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the communication type.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of CommunicationTypeModel.
    try {
      List<CommunicationTypeModel> result = apiInstance.communicationTypesPatchCommunicationType(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#communicationTypesPatchCommunicationType");
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
| **guid** | **String**| ID of the communication type. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of CommunicationTypeModel. | [optional] |

### Return type

[**List&lt;CommunicationTypeModel&gt;**](CommunicationTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated communication model. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="communicationTypesPostCommunicationType"></a>
# **communicationTypesPostCommunicationType**
> CommunicationTypeModel communicationTypesPostCommunicationType(communicationTypeModel)

Insert a communication type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    CommunicationTypeModel communicationTypeModel = new CommunicationTypeModel(); // CommunicationTypeModel | CommunicationTypeModel.
    try {
      CommunicationTypeModel result = apiInstance.communicationTypesPostCommunicationType(communicationTypeModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#communicationTypesPostCommunicationType");
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
| **communicationTypeModel** | [**CommunicationTypeModel**](CommunicationTypeModel.md)| CommunicationTypeModel. | [optional] |

### Return type

[**CommunicationTypeModel**](CommunicationTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created communication type. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="contactRolesPatchContactRole"></a>
# **contactRolesPatchContactRole**
> List&lt;ContactRoleModel&gt; contactRolesPatchContactRole(guid, patchOperation)

Update (Patch) a contact role or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the contact role.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of ContactRoleModel.
    try {
      List<ContactRoleModel> result = apiInstance.contactRolesPatchContactRole(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#contactRolesPatchContactRole");
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
| **guid** | **String**| ID of the contact role. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of ContactRoleModel. | [optional] |

### Return type

[**List&lt;ContactRoleModel&gt;**](ContactRoleModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated contact role. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="contactRolesPostContactRole"></a>
# **contactRolesPostContactRole**
> ContactRoleModel contactRolesPostContactRole(contactRoleModel)

Insert a contact role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    ContactRoleModel contactRoleModel = new ContactRoleModel(); // ContactRoleModel | ContactRoleModel.
    try {
      ContactRoleModel result = apiInstance.contactRolesPostContactRole(contactRoleModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#contactRolesPostContactRole");
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
| **contactRoleModel** | [**ContactRoleModel**](ContactRoleModel.md)| ContactRoleModel. | [optional] |

### Return type

[**ContactRoleModel**](ContactRoleModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created contact role. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="costAccountsPatchCostAccount"></a>
# **costAccountsPatchCostAccount**
> List&lt;CostAccountModel&gt; costAccountsPatchCostAccount(guid, patchOperation)

Update (Patch) a cost account or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the cost account.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of CostAccountModel.
    try {
      List<CostAccountModel> result = apiInstance.costAccountsPatchCostAccount(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#costAccountsPatchCostAccount");
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
| **guid** | **String**| ID of the cost account. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of CostAccountModel. | [optional] |

### Return type

[**List&lt;CostAccountModel&gt;**](CostAccountModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated cost account. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="costAccountsPostCostAccount"></a>
# **costAccountsPostCostAccount**
> CostAccountModel costAccountsPostCostAccount(costAccountModel)

Insert a cost account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    CostAccountModel costAccountModel = new CostAccountModel(); // CostAccountModel | CostAccountModel.
    try {
      CostAccountModel result = apiInstance.costAccountsPostCostAccount(costAccountModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#costAccountsPostCostAccount");
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
| **costAccountModel** | [**CostAccountModel**](CostAccountModel.md)| CostAccountModel. | [optional] |

### Return type

[**CostAccountModel**](CostAccountModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created cost account. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="costCentersPatchCostCenter"></a>
# **costCentersPatchCostCenter**
> List&lt;CostCenterModel&gt; costCentersPatchCostCenter(guid, patchOperation)

Update (Patch) a cost center or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the cost center.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of CostCenterModel.
    try {
      List<CostCenterModel> result = apiInstance.costCentersPatchCostCenter(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#costCentersPatchCostCenter");
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
| **guid** | **String**| ID of the cost center. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of CostCenterModel. | [optional] |

### Return type

[**List&lt;CostCenterModel&gt;**](CostCenterModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated cost center. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="costCentersPostCostCenter"></a>
# **costCentersPostCostCenter**
> CostCenterModel costCentersPostCostCenter(costCenterModel)

Insert a cost center.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    CostCenterModel costCenterModel = new CostCenterModel(); // CostCenterModel | CostCenterModel.
    try {
      CostCenterModel result = apiInstance.costCentersPostCostCenter(costCenterModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#costCentersPostCostCenter");
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
| **costCenterModel** | [**CostCenterModel**](CostCenterModel.md)| CostCenterModel. | [optional] |

### Return type

[**CostCenterModel**](CostCenterModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created cost center. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="currenciesPatchCurrency"></a>
# **currenciesPatchCurrency**
> List&lt;CurrencyOutputModel&gt; currenciesPatchCurrency(guid, patchOperation)

Update (Patch) an currency or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the currency.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of CurrencyModel.
    try {
      List<CurrencyOutputModel> result = apiInstance.currenciesPatchCurrency(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#currenciesPatchCurrency");
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
| **guid** | **String**| ID of the currency. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of CurrencyModel. | [optional] |

### Return type

[**List&lt;CurrencyOutputModel&gt;**](CurrencyOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated currencies. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customerCustomPropertiesPatchCustomerCustomProperty"></a>
# **customerCustomPropertiesPatchCustomerCustomProperty**
> List&lt;CustomPropertyModel&gt; customerCustomPropertiesPatchCustomerCustomProperty(guid, patchOperation)

Update (Patch) a customer custom property or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the customer custom property Can also be comma separate list of IDs to patch multiple customer custom properties with one call. When multiple IDs are given, returns model which has list of succeeded customer custom properties and list of errors.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of CustomerCustomPropertyModel.
    try {
      List<CustomPropertyModel> result = apiInstance.customerCustomPropertiesPatchCustomerCustomProperty(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#customerCustomPropertiesPatchCustomerCustomProperty");
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
| **guid** | **String**| ID of the customer custom property Can also be comma separate list of IDs to patch multiple customer custom properties with one call. When multiple IDs are given, returns model which has list of succeeded customer custom properties and list of errors. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of CustomerCustomPropertyModel. | [optional] |

### Return type

[**List&lt;CustomPropertyModel&gt;**](CustomPropertyModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated customer custom properties. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customerCustomPropertiesPostCustomerCustomProperty"></a>
# **customerCustomPropertiesPostCustomerCustomProperty**
> List&lt;CustomPropertyModel&gt; customerCustomPropertiesPostCustomerCustomProperty(customPropertyModel)

Insert a customer custom property.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    CustomPropertyModel customPropertyModel = new CustomPropertyModel(); // CustomPropertyModel | CustomerCustomPropertyModel.
    try {
      List<CustomPropertyModel> result = apiInstance.customerCustomPropertiesPostCustomerCustomProperty(customPropertyModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#customerCustomPropertiesPostCustomerCustomProperty");
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
| **customPropertyModel** | [**CustomPropertyModel**](CustomPropertyModel.md)| CustomerCustomPropertyModel. | [optional] |

### Return type

[**List&lt;CustomPropertyModel&gt;**](CustomPropertyModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created customer custom property. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customerCustomPropertySelectionItemsPatchCustomerCustomPropertySelectionItem"></a>
# **customerCustomPropertySelectionItemsPatchCustomerCustomPropertySelectionItem**
> List&lt;CustomerCustomPropertySelectionItemOutputModel&gt; customerCustomPropertySelectionItemsPatchCustomerCustomPropertySelectionItem(guid, patchOperation)

Update (Patch) a customer custom property selection item or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the customer custom property selection item.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of CustomerCustomPropertySelectionItemInputModel.
    try {
      List<CustomerCustomPropertySelectionItemOutputModel> result = apiInstance.customerCustomPropertySelectionItemsPatchCustomerCustomPropertySelectionItem(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#customerCustomPropertySelectionItemsPatchCustomerCustomPropertySelectionItem");
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
| **guid** | **String**| ID of the customer custom property selection item. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of CustomerCustomPropertySelectionItemInputModel. | [optional] |

### Return type

[**List&lt;CustomerCustomPropertySelectionItemOutputModel&gt;**](CustomerCustomPropertySelectionItemOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated customer custom properties. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customerCustomPropertySelectionItemsPostCustomerCustomPropertySelectionItem"></a>
# **customerCustomPropertySelectionItemsPostCustomerCustomPropertySelectionItem**
> CustomerCustomPropertySelectionItemOutputModel customerCustomPropertySelectionItemsPostCustomerCustomPropertySelectionItem(customerCustomPropertySelectionItemInputModel)

Insert a customer custom property selection item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    CustomerCustomPropertySelectionItemInputModel customerCustomPropertySelectionItemInputModel = new CustomerCustomPropertySelectionItemInputModel(); // CustomerCustomPropertySelectionItemInputModel | CustomPropertySelectionItemInputModel.
    try {
      CustomerCustomPropertySelectionItemOutputModel result = apiInstance.customerCustomPropertySelectionItemsPostCustomerCustomPropertySelectionItem(customerCustomPropertySelectionItemInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#customerCustomPropertySelectionItemsPostCustomerCustomPropertySelectionItem");
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
| **customerCustomPropertySelectionItemInputModel** | [**CustomerCustomPropertySelectionItemInputModel**](CustomerCustomPropertySelectionItemInputModel.md)| CustomPropertySelectionItemInputModel. | [optional] |

### Return type

[**CustomerCustomPropertySelectionItemOutputModel**](CustomerCustomPropertySelectionItemOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created customer custom property. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="industriesPatchIndustry"></a>
# **industriesPatchIndustry**
> List&lt;IndustryModel&gt; industriesPatchIndustry(guid, patchOperation)

Update (Patch) an industry or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the industry.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of IndustryModel.
    try {
      List<IndustryModel> result = apiInstance.industriesPatchIndustry(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#industriesPatchIndustry");
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
| **guid** | **String**| ID of the industry. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of IndustryModel. | [optional] |

### Return type

[**List&lt;IndustryModel&gt;**](IndustryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated industries. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="industriesPostIndustry"></a>
# **industriesPostIndustry**
> IndustryModel industriesPostIndustry(industryModel)

Insert an industry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    IndustryModel industryModel = new IndustryModel(); // IndustryModel | IndustryModel.
    try {
      IndustryModel result = apiInstance.industriesPostIndustry(industryModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#industriesPostIndustry");
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
| **industryModel** | [**IndustryModel**](IndustryModel.md)| IndustryModel. | [optional] |

### Return type

[**IndustryModel**](IndustryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Inserted industry. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="invoiceStatusesPatchInvoiceStatus"></a>
# **invoiceStatusesPatchInvoiceStatus**
> List&lt;InvoiceStatusModel&gt; invoiceStatusesPatchInvoiceStatus(guid, patchOperation)

Update (Patch) an Invoice status or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the Invoice status.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of InvoiceStatusModel.
    try {
      List<InvoiceStatusModel> result = apiInstance.invoiceStatusesPatchInvoiceStatus(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#invoiceStatusesPatchInvoiceStatus");
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
| **guid** | **String**| ID of the Invoice status. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of InvoiceStatusModel. | [optional] |

### Return type

[**List&lt;InvoiceStatusModel&gt;**](InvoiceStatusModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated Invoice statuses. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="invoiceStatusesPostInvoiceStatus"></a>
# **invoiceStatusesPostInvoiceStatus**
> InvoiceStatusModel invoiceStatusesPostInvoiceStatus(invoiceStatusModel)

Insert a invoice status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    InvoiceStatusModel invoiceStatusModel = new InvoiceStatusModel(); // InvoiceStatusModel | InvoiceStatusModel.
    try {
      InvoiceStatusModel result = apiInstance.invoiceStatusesPostInvoiceStatus(invoiceStatusModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#invoiceStatusesPostInvoiceStatus");
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
| **invoiceStatusModel** | [**InvoiceStatusModel**](InvoiceStatusModel.md)| InvoiceStatusModel. | [optional] |

### Return type

[**InvoiceStatusModel**](InvoiceStatusModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Inserted invoice status. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="keywordsPatchKeyword"></a>
# **keywordsPatchKeyword**
> List&lt;KeywordModel&gt; keywordsPatchKeyword(guid, patchOperation)

Update (Patch) a keyword or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the keyword.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document.
    try {
      List<KeywordModel> result = apiInstance.keywordsPatchKeyword(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#keywordsPatchKeyword");
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
| **guid** | **String**| ID of the keyword. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document. | [optional] |

### Return type

[**List&lt;KeywordModel&gt;**](KeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated keywords. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="keywordsPostKeyword"></a>
# **keywordsPostKeyword**
> KeywordModel keywordsPostKeyword(keywordModel)

Insert a keyword.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    KeywordModel keywordModel = new KeywordModel(); // KeywordModel | KeywordModel.
    try {
      KeywordModel result = apiInstance.keywordsPostKeyword(keywordModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#keywordsPostKeyword");
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
| **keywordModel** | [**KeywordModel**](KeywordModel.md)| KeywordModel. | [optional] |

### Return type

[**KeywordModel**](KeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created contact role. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="leadSourcesPatchLeadSource"></a>
# **leadSourcesPatchLeadSource**
> List&lt;LeadSourceModel&gt; leadSourcesPatchLeadSource(guid, patchOperation)

Update (Patch) an lead source or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the lead source.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of LeadSourceModel.
    try {
      List<LeadSourceModel> result = apiInstance.leadSourcesPatchLeadSource(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#leadSourcesPatchLeadSource");
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
| **guid** | **String**| ID of the lead source. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of LeadSourceModel. | [optional] |

### Return type

[**List&lt;LeadSourceModel&gt;**](LeadSourceModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated lead sources. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="leadSourcesPostLeadSource"></a>
# **leadSourcesPostLeadSource**
> LeadSourceModel leadSourcesPostLeadSource(leadSourceModel)

Insert a lead source.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    LeadSourceModel leadSourceModel = new LeadSourceModel(); // LeadSourceModel | LeadSourceModel.
    try {
      LeadSourceModel result = apiInstance.leadSourcesPostLeadSource(leadSourceModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#leadSourcesPostLeadSource");
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
| **leadSourceModel** | [**LeadSourceModel**](LeadSourceModel.md)| LeadSourceModel. | [optional] |

### Return type

[**LeadSourceModel**](LeadSourceModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Inserted lead source. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="marketSegmentsPatchMarketSegment"></a>
# **marketSegmentsPatchMarketSegment**
> List&lt;MarketSegmentModel&gt; marketSegmentsPatchMarketSegment(guid, patchOperation)

Update (Patch) an Market Segment or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the Market Segment.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of MarketSegmentModel.
    try {
      List<MarketSegmentModel> result = apiInstance.marketSegmentsPatchMarketSegment(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#marketSegmentsPatchMarketSegment");
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
| **guid** | **String**| ID of the Market Segment. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of MarketSegmentModel. | [optional] |

### Return type

[**List&lt;MarketSegmentModel&gt;**](MarketSegmentModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated Market Segments. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="marketSegmentsPostMarketSegment"></a>
# **marketSegmentsPostMarketSegment**
> MarketSegmentModel marketSegmentsPostMarketSegment(marketSegmentModel)

Insert a market segment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    MarketSegmentModel marketSegmentModel = new MarketSegmentModel(); // MarketSegmentModel | MarketSegmentModel.
    try {
      MarketSegmentModel result = apiInstance.marketSegmentsPostMarketSegment(marketSegmentModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#marketSegmentsPostMarketSegment");
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
| **marketSegmentModel** | [**MarketSegmentModel**](MarketSegmentModel.md)| MarketSegmentModel. | [optional] |

### Return type

[**MarketSegmentModel**](MarketSegmentModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created market segment. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="overtimesPatchOvertime"></a>
# **overtimesPatchOvertime**
> List&lt;OvertimeModel&gt; overtimesPatchOvertime(guid, patchOperation)

Update (Patch) an overtime or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the overtime.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of OvertimeModel.
    try {
      List<OvertimeModel> result = apiInstance.overtimesPatchOvertime(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#overtimesPatchOvertime");
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
| **guid** | **String**| ID of the overtime. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of OvertimeModel. | [optional] |

### Return type

[**List&lt;OvertimeModel&gt;**](OvertimeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of overtimes. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="overtimesPostOvertime"></a>
# **overtimesPostOvertime**
> OvertimeModel overtimesPostOvertime(overtimeModel)

Insert an overtime.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    OvertimeModel overtimeModel = new OvertimeModel(); // OvertimeModel | OvertimeModel.
    try {
      OvertimeModel result = apiInstance.overtimesPostOvertime(overtimeModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#overtimesPostOvertime");
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
| **overtimeModel** | [**OvertimeModel**](OvertimeModel.md)| OvertimeModel. | [optional] |

### Return type

[**OvertimeModel**](OvertimeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created overtime. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="phaseStatusTypesPatchPhaseStatusType"></a>
# **phaseStatusTypesPatchPhaseStatusType**
> List&lt;PhaseStatusTypeModel&gt; phaseStatusTypesPatchPhaseStatusType(guid, patchOperation)

Update (Patch) a phase status type or a part of it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the phase status type
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of TaskStatusTypeModel
    try {
      List<PhaseStatusTypeModel> result = apiInstance.phaseStatusTypesPatchPhaseStatusType(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#phaseStatusTypesPatchPhaseStatusType");
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
| **guid** | **String**| ID of the phase status type | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of TaskStatusTypeModel | [optional] |

### Return type

[**List&lt;PhaseStatusTypeModel&gt;**](PhaseStatusTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated phase status type |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="phaseStatusTypesPostPhaseStatusType"></a>
# **phaseStatusTypesPostPhaseStatusType**
> PhaseStatusTypeModel phaseStatusTypesPostPhaseStatusType(phaseStatusTypeModel)

Insert a phase status type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    PhaseStatusTypeModel phaseStatusTypeModel = new PhaseStatusTypeModel(); // PhaseStatusTypeModel | PhaseStatusTypeModel
    try {
      PhaseStatusTypeModel result = apiInstance.phaseStatusTypesPostPhaseStatusType(phaseStatusTypeModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#phaseStatusTypesPostPhaseStatusType");
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
| **phaseStatusTypeModel** | [**PhaseStatusTypeModel**](PhaseStatusTypeModel.md)| PhaseStatusTypeModel | [optional] |

### Return type

[**PhaseStatusTypeModel**](PhaseStatusTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created phase status type |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="productCategoriesPatchProductCategory"></a>
# **productCategoriesPatchProductCategory**
> List&lt;ProductCategoryModel&gt; productCategoriesPatchProductCategory(guid, patchOperation)

Update (Patch) a product category or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the product category.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of ProductCategoryModel.
    try {
      List<ProductCategoryModel> result = apiInstance.productCategoriesPatchProductCategory(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#productCategoriesPatchProductCategory");
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
| **guid** | **String**| ID of the product category. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of ProductCategoryModel. | [optional] |

### Return type

[**List&lt;ProductCategoryModel&gt;**](ProductCategoryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated product category. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="productCategoriesPostProductCategory"></a>
# **productCategoriesPostProductCategory**
> ProductCategoryModel productCategoriesPostProductCategory(productCategoryModel)

Insert a product category.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    ProductCategoryModel productCategoryModel = new ProductCategoryModel(); // ProductCategoryModel | ProductCategoryModel.
    try {
      ProductCategoryModel result = apiInstance.productCategoriesPostProductCategory(productCategoryModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#productCategoriesPostProductCategory");
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
| **productCategoryModel** | [**ProductCategoryModel**](ProductCategoryModel.md)| ProductCategoryModel. | [optional] |

### Return type

[**ProductCategoryModel**](ProductCategoryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created product category. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="productCountrySettingsPatchProductCountrySettings"></a>
# **productCountrySettingsPatchProductCountrySettings**
> List&lt;ProductCountrySettingsModel&gt; productCountrySettingsPatchProductCountrySettings(guid, patchOperation)

Update (Patch) a product country setting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the product country setting
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of ProductCountrySettingsModel
    try {
      List<ProductCountrySettingsModel> result = apiInstance.productCountrySettingsPatchProductCountrySettings(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#productCountrySettingsPatchProductCountrySettings");
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
| **guid** | **String**| ID of the product country setting | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of ProductCountrySettingsModel | [optional] |

### Return type

[**List&lt;ProductCountrySettingsModel&gt;**](ProductCountrySettingsModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated product country settings |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="productCountrySettingsPostProductCountrySettings"></a>
# **productCountrySettingsPostProductCountrySettings**
> ProductCountrySettingsModel productCountrySettingsPostProductCountrySettings(productCountrySettingsModel)

Insert a product country setting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    ProductCountrySettingsModel productCountrySettingsModel = new ProductCountrySettingsModel(); // ProductCountrySettingsModel | ProductCountrySettingsModel
    try {
      ProductCountrySettingsModel result = apiInstance.productCountrySettingsPostProductCountrySettings(productCountrySettingsModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#productCountrySettingsPostProductCountrySettings");
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
| **productCountrySettingsModel** | [**ProductCountrySettingsModel**](ProductCountrySettingsModel.md)| ProductCountrySettingsModel | [optional] |

### Return type

[**ProductCountrySettingsModel**](ProductCountrySettingsModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Inserted product country setting |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="productsPatchProduct"></a>
# **productsPatchProduct**
> List&lt;ProductOutputModel&gt; productsPatchProduct(guid, patchOperation)

Update (Patch) an product or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the product.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of ProductModel.
    try {
      List<ProductOutputModel> result = apiInstance.productsPatchProduct(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#productsPatchProduct");
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
| **guid** | **String**| ID of the product. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of ProductModel. | [optional] |

### Return type

[**List&lt;ProductOutputModel&gt;**](ProductOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated products. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="productsPostProduct"></a>
# **productsPostProduct**
> ProductOutputModel productsPostProduct(productInputModel)

Insert a product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    ProductInputModel productInputModel = new ProductInputModel(); // ProductInputModel | ProductModel.
    try {
      ProductOutputModel result = apiInstance.productsPostProduct(productInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#productsPostProduct");
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
| **productInputModel** | [**ProductInputModel**](ProductInputModel.md)| ProductModel. | [optional] |

### Return type

[**ProductOutputModel**](ProductOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created product. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectBillingCustomersPatchProjectBillingCustomer"></a>
# **projectBillingCustomersPatchProjectBillingCustomer**
> List&lt;ProjectBillingCustomerModel2&gt; projectBillingCustomersPatchProjectBillingCustomer(guid, patchOperation)

Update (Patch) a project billing customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the project billing customer.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of ProjectBillingCustomerModel.
    try {
      List<ProjectBillingCustomerModel2> result = apiInstance.projectBillingCustomersPatchProjectBillingCustomer(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#projectBillingCustomersPatchProjectBillingCustomer");
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
| **guid** | **String**| ID of the project billing customer. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of ProjectBillingCustomerModel. | [optional] |

### Return type

[**List&lt;ProjectBillingCustomerModel2&gt;**](ProjectBillingCustomerModel2.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated project billing customer. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectBillingCustomersPostProjectBillingCustomer"></a>
# **projectBillingCustomersPostProjectBillingCustomer**
> ProjectBillingCustomerModel2 projectBillingCustomersPostProjectBillingCustomer(projectBillingCustomerModel2)

Insert a billing customer for a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    ProjectBillingCustomerModel2 projectBillingCustomerModel2 = new ProjectBillingCustomerModel2(); // ProjectBillingCustomerModel2 | ProjectBillingCustomerModel.
    try {
      ProjectBillingCustomerModel2 result = apiInstance.projectBillingCustomersPostProjectBillingCustomer(projectBillingCustomerModel2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#projectBillingCustomersPostProjectBillingCustomer");
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
| **projectBillingCustomerModel2** | [**ProjectBillingCustomerModel2**](ProjectBillingCustomerModel2.md)| ProjectBillingCustomerModel. | [optional] |

### Return type

[**ProjectBillingCustomerModel2**](ProjectBillingCustomerModel2.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created billing customer. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectCustomPropertiesPatchProjectCustomProperty"></a>
# **projectCustomPropertiesPatchProjectCustomProperty**
> List&lt;CustomPropertyModel&gt; projectCustomPropertiesPatchProjectCustomProperty(guid, patchOperation)

Update (Patch) a project custom property or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the project custom property Can also be comma separate list of IDs to patch multiple project custom properties with one call. When multiple IDs are given, returns model which has list of succeeded project custom properties and list of errors.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of ProjectCustomPropertyModel.
    try {
      List<CustomPropertyModel> result = apiInstance.projectCustomPropertiesPatchProjectCustomProperty(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#projectCustomPropertiesPatchProjectCustomProperty");
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
| **guid** | **String**| ID of the project custom property Can also be comma separate list of IDs to patch multiple project custom properties with one call. When multiple IDs are given, returns model which has list of succeeded project custom properties and list of errors. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of ProjectCustomPropertyModel. | [optional] |

### Return type

[**List&lt;CustomPropertyModel&gt;**](CustomPropertyModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated project custom properties. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectCustomPropertiesPostProjectCustomProperty"></a>
# **projectCustomPropertiesPostProjectCustomProperty**
> List&lt;CustomPropertyModel&gt; projectCustomPropertiesPostProjectCustomProperty(customPropertyModel)

Insert a project custom property.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    CustomPropertyModel customPropertyModel = new CustomPropertyModel(); // CustomPropertyModel | ProjectCustomPropertyModel.
    try {
      List<CustomPropertyModel> result = apiInstance.projectCustomPropertiesPostProjectCustomProperty(customPropertyModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#projectCustomPropertiesPostProjectCustomProperty");
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
| **customPropertyModel** | [**CustomPropertyModel**](CustomPropertyModel.md)| ProjectCustomPropertyModel. | [optional] |

### Return type

[**List&lt;CustomPropertyModel&gt;**](CustomPropertyModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created project custom property. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectCustomPropertySelectionItemsPatchProjectCustomPropertySelectionItem"></a>
# **projectCustomPropertySelectionItemsPatchProjectCustomPropertySelectionItem**
> List&lt;ProjectCustomPropertySelectionItemOutputModel&gt; projectCustomPropertySelectionItemsPatchProjectCustomPropertySelectionItem(guid, patchOperation)

Update (Patch) a project custom property selection item or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the project custom property selection item.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of ProjectCustomPropertySelectionItemInputModel.
    try {
      List<ProjectCustomPropertySelectionItemOutputModel> result = apiInstance.projectCustomPropertySelectionItemsPatchProjectCustomPropertySelectionItem(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#projectCustomPropertySelectionItemsPatchProjectCustomPropertySelectionItem");
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
| **guid** | **String**| ID of the project custom property selection item. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of ProjectCustomPropertySelectionItemInputModel. | [optional] |

### Return type

[**List&lt;ProjectCustomPropertySelectionItemOutputModel&gt;**](ProjectCustomPropertySelectionItemOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated project custom properties. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectCustomPropertySelectionItemsPostProjectCustomPropertySelectionItem"></a>
# **projectCustomPropertySelectionItemsPostProjectCustomPropertySelectionItem**
> ProjectCustomPropertySelectionItemOutputModel projectCustomPropertySelectionItemsPostProjectCustomPropertySelectionItem(projectCustomPropertySelectionItemInputModel)

Insert a project custom property selection item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    ProjectCustomPropertySelectionItemInputModel projectCustomPropertySelectionItemInputModel = new ProjectCustomPropertySelectionItemInputModel(); // ProjectCustomPropertySelectionItemInputModel | CustomPropertySelectionItemInputModel.
    try {
      ProjectCustomPropertySelectionItemOutputModel result = apiInstance.projectCustomPropertySelectionItemsPostProjectCustomPropertySelectionItem(projectCustomPropertySelectionItemInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#projectCustomPropertySelectionItemsPostProjectCustomPropertySelectionItem");
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
| **projectCustomPropertySelectionItemInputModel** | [**ProjectCustomPropertySelectionItemInputModel**](ProjectCustomPropertySelectionItemInputModel.md)| CustomPropertySelectionItemInputModel. | [optional] |

### Return type

[**ProjectCustomPropertySelectionItemOutputModel**](ProjectCustomPropertySelectionItemOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created project custom property. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectMemberCostExceptionsPatch"></a>
# **projectMemberCostExceptionsPatch**
> List&lt;ProjectMemberCostExceptionOutputModel&gt; projectMemberCostExceptionsPatch(guid, patchOperation)

Update (Patch) project member cost exception.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the project member cost exception.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of ProjectMemberCostExceptionModel.
    try {
      List<ProjectMemberCostExceptionOutputModel> result = apiInstance.projectMemberCostExceptionsPatch(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#projectMemberCostExceptionsPatch");
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
| **guid** | **String**| ID of the project member cost exception. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of ProjectMemberCostExceptionModel. | [optional] |

### Return type

[**List&lt;ProjectMemberCostExceptionOutputModel&gt;**](ProjectMemberCostExceptionOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated links. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectMemberCostExceptionsPost"></a>
# **projectMemberCostExceptionsPost**
> ProjectMemberCostExceptionOutputModel projectMemberCostExceptionsPost(projectMemberCostExceptionInputModel)

Add a cost exception to a project member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    ProjectMemberCostExceptionInputModel projectMemberCostExceptionInputModel = new ProjectMemberCostExceptionInputModel(); // ProjectMemberCostExceptionInputModel | ProjectMemberCostExceptionModel.
    try {
      ProjectMemberCostExceptionOutputModel result = apiInstance.projectMemberCostExceptionsPost(projectMemberCostExceptionInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#projectMemberCostExceptionsPost");
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
| **projectMemberCostExceptionInputModel** | [**ProjectMemberCostExceptionInputModel**](ProjectMemberCostExceptionInputModel.md)| ProjectMemberCostExceptionModel. | [optional] |

### Return type

[**ProjectMemberCostExceptionOutputModel**](ProjectMemberCostExceptionOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Inserted link. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectStatusTypesPatchProjectStatusType"></a>
# **projectStatusTypesPatchProjectStatusType**
> List&lt;ProjectStatusTypeModel&gt; projectStatusTypesPatchProjectStatusType(guid, patchOperation)

Update (Patch) a projectStatusType or a part of it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the projectStatusType
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of ProjectStatusTypeModel
    try {
      List<ProjectStatusTypeModel> result = apiInstance.projectStatusTypesPatchProjectStatusType(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#projectStatusTypesPatchProjectStatusType");
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
| **guid** | **String**| ID of the projectStatusType | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of ProjectStatusTypeModel | [optional] |

### Return type

[**List&lt;ProjectStatusTypeModel&gt;**](ProjectStatusTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated business units |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectStatusTypesPostProjectStatusType"></a>
# **projectStatusTypesPostProjectStatusType**
> ProjectStatusTypeModel projectStatusTypesPostProjectStatusType(projectStatusTypeModel)

Insert a project status type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    ProjectStatusTypeModel projectStatusTypeModel = new ProjectStatusTypeModel(); // ProjectStatusTypeModel | ProjectStatusTypeModel
    try {
      ProjectStatusTypeModel result = apiInstance.projectStatusTypesPostProjectStatusType(projectStatusTypeModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#projectStatusTypesPostProjectStatusType");
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
| **projectStatusTypeModel** | [**ProjectStatusTypeModel**](ProjectStatusTypeModel.md)| ProjectStatusTypeModel | [optional] |

### Return type

[**ProjectStatusTypeModel**](ProjectStatusTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Project status type |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectTaskStatusesPatchProjectTaskStatus"></a>
# **projectTaskStatusesPatchProjectTaskStatus**
> List&lt;ProjectTaskStatusModel&gt; projectTaskStatusesPatchProjectTaskStatus(guid, patchOperation)

Update (Patch) an Project task status or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the Project task status.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of ProjectTaskStatusModel.
    try {
      List<ProjectTaskStatusModel> result = apiInstance.projectTaskStatusesPatchProjectTaskStatus(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#projectTaskStatusesPatchProjectTaskStatus");
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
| **guid** | **String**| ID of the Project task status. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of ProjectTaskStatusModel. | [optional] |

### Return type

[**List&lt;ProjectTaskStatusModel&gt;**](ProjectTaskStatusModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated Project task status. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectTaskStatusesPostProjectTaskStatus"></a>
# **projectTaskStatusesPostProjectTaskStatus**
> ProjectTaskStatusModel projectTaskStatusesPostProjectTaskStatus(projectTaskStatusModel)

Insert a project task status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    ProjectTaskStatusModel projectTaskStatusModel = new ProjectTaskStatusModel(); // ProjectTaskStatusModel | ProjectTaskStatusModel.
    try {
      ProjectTaskStatusModel result = apiInstance.projectTaskStatusesPostProjectTaskStatus(projectTaskStatusModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#projectTaskStatusesPostProjectTaskStatus");
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
| **projectTaskStatusModel** | [**ProjectTaskStatusModel**](ProjectTaskStatusModel.md)| ProjectTaskStatusModel. | [optional] |

### Return type

[**ProjectTaskStatusModel**](ProjectTaskStatusModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Project task status.  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalStatusesPatchProposalStatus"></a>
# **proposalStatusesPatchProposalStatus**
> List&lt;ProposalStatusOutputModel&gt; proposalStatusesPatchProposalStatus(guid, patchOperation)

Update (Patch) an Proposal status or a part of it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the Proposal status
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of ProposalStatusModel
    try {
      List<ProposalStatusOutputModel> result = apiInstance.proposalStatusesPatchProposalStatus(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#proposalStatusesPatchProposalStatus");
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
| **guid** | **String**| ID of the Proposal status | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of ProposalStatusModel | [optional] |

### Return type

[**List&lt;ProposalStatusOutputModel&gt;**](ProposalStatusOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated Proposal statuses |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalStatusesPostProposalStatus"></a>
# **proposalStatusesPostProposalStatus**
> ProposalStatusOutputModel proposalStatusesPostProposalStatus(proposalStatusInputModel)

Insert a proposal status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    ProposalStatusInputModel proposalStatusInputModel = new ProposalStatusInputModel(); // ProposalStatusInputModel | ProposalStatusModel
    try {
      ProposalStatusOutputModel result = apiInstance.proposalStatusesPostProposalStatus(proposalStatusInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#proposalStatusesPostProposalStatus");
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
| **proposalStatusInputModel** | [**ProposalStatusInputModel**](ProposalStatusInputModel.md)| ProposalStatusModel | [optional] |

### Return type

[**ProposalStatusOutputModel**](ProposalStatusOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Inserted proposal status |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="rolesPatchRole"></a>
# **rolesPatchRole**
> List&lt;RoleOutputModel&gt; rolesPatchRole(guid, patchOperation)

Update (Patch) a role or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the role.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of RoleInputModel.
    try {
      List<RoleOutputModel> result = apiInstance.rolesPatchRole(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#rolesPatchRole");
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
| **guid** | **String**| ID of the role. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of RoleInputModel. | [optional] |

### Return type

[**List&lt;RoleOutputModel&gt;**](RoleOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated roles. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="rolesPostRole"></a>
# **rolesPostRole**
> RoleOutputModel rolesPostRole(roleInputModel)

Insert a role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    RoleInputModel roleInputModel = new RoleInputModel(); // RoleInputModel | RoleInputModel.
    try {
      RoleOutputModel result = apiInstance.rolesPostRole(roleInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#rolesPostRole");
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
| **roleInputModel** | [**RoleInputModel**](RoleInputModel.md)| RoleInputModel. | [optional] |

### Return type

[**RoleOutputModel**](RoleOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created role. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="salesAccountsPatchSalesAccount"></a>
# **salesAccountsPatchSalesAccount**
> List&lt;SalesAccountModel&gt; salesAccountsPatchSalesAccount(guid, patchOperation)

Update (Patch) a sales account or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the sales account.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of SalesAccountModel.
    try {
      List<SalesAccountModel> result = apiInstance.salesAccountsPatchSalesAccount(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#salesAccountsPatchSalesAccount");
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
| **guid** | **String**| ID of the sales account. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of SalesAccountModel. | [optional] |

### Return type

[**List&lt;SalesAccountModel&gt;**](SalesAccountModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated sales account. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="salesAccountsPostSalesAccount"></a>
# **salesAccountsPostSalesAccount**
> SalesAccountModel salesAccountsPostSalesAccount(salesAccountModel)

Insert a sales account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    SalesAccountModel salesAccountModel = new SalesAccountModel(); // SalesAccountModel | SalesAccountModel.
    try {
      SalesAccountModel result = apiInstance.salesAccountsPostSalesAccount(salesAccountModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#salesAccountsPostSalesAccount");
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
| **salesAccountModel** | [**SalesAccountModel**](SalesAccountModel.md)| SalesAccountModel. | [optional] |

### Return type

[**SalesAccountModel**](SalesAccountModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created sales account. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="salesStatusTypesPatchSalesStatusType"></a>
# **salesStatusTypesPatchSalesStatusType**
> List&lt;SalesStatusTypeOutputModel&gt; salesStatusTypesPatchSalesStatusType(guid, patchOperation)

Update (Patch) an sales status type or a part of it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the sales status type
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of salesStatusType
    try {
      List<SalesStatusTypeOutputModel> result = apiInstance.salesStatusTypesPatchSalesStatusType(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#salesStatusTypesPatchSalesStatusType");
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
| **guid** | **String**| ID of the sales status type | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of salesStatusType | [optional] |

### Return type

[**List&lt;SalesStatusTypeOutputModel&gt;**](SalesStatusTypeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated sales status types |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="salesStatusTypesPostSalesStatusType"></a>
# **salesStatusTypesPostSalesStatusType**
> SalesStatusTypeOutputModel salesStatusTypesPostSalesStatusType(salesStatusTypeInputModel)

Insert a sales status type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    SalesStatusTypeInputModel salesStatusTypeInputModel = new SalesStatusTypeInputModel(); // SalesStatusTypeInputModel | salesStatusType
    try {
      SalesStatusTypeOutputModel result = apiInstance.salesStatusTypesPostSalesStatusType(salesStatusTypeInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#salesStatusTypesPostSalesStatusType");
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
| **salesStatusTypeInputModel** | [**SalesStatusTypeInputModel**](SalesStatusTypeInputModel.md)| salesStatusType | [optional] |

### Return type

[**SalesStatusTypeOutputModel**](SalesStatusTypeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Sales status type |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="timeEntryTypesPatchTimeEntryType"></a>
# **timeEntryTypesPatchTimeEntryType**
> List&lt;TimeEntryTypeModel&gt; timeEntryTypesPatchTimeEntryType(guid, patchOperation)

Update (Patch) a time entry type or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the time entry type.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of TimeEntryTypeModel.
    try {
      List<TimeEntryTypeModel> result = apiInstance.timeEntryTypesPatchTimeEntryType(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#timeEntryTypesPatchTimeEntryType");
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
| **guid** | **String**| ID of the time entry type. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of TimeEntryTypeModel. | [optional] |

### Return type

[**List&lt;TimeEntryTypeModel&gt;**](TimeEntryTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated time entry type model. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="timeEntryTypesPostTimeEntryType"></a>
# **timeEntryTypesPostTimeEntryType**
> TimeEntryTypeModel timeEntryTypesPostTimeEntryType(timeEntryTypeModel)

Insert a time entry type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    TimeEntryTypeModel timeEntryTypeModel = new TimeEntryTypeModel(); // TimeEntryTypeModel | TimeEntryTypeModel.
    try {
      TimeEntryTypeModel result = apiInstance.timeEntryTypesPostTimeEntryType(timeEntryTypeModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#timeEntryTypesPostTimeEntryType");
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
| **timeEntryTypeModel** | [**TimeEntryTypeModel**](TimeEntryTypeModel.md)| TimeEntryTypeModel. | [optional] |

### Return type

[**TimeEntryTypeModel**](TimeEntryTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created time entry type. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="travelExpenseTypeCountrySettingsPatchTravelExpenseTypeCountrySettings"></a>
# **travelExpenseTypeCountrySettingsPatchTravelExpenseTypeCountrySettings**
> List&lt;TravelExpenseTypeCountrySettingsModel&gt; travelExpenseTypeCountrySettingsPatchTravelExpenseTypeCountrySettings(guid, patchOperation)

Update (Patch) a travel expense type country setting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the travel expense type country setting
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of TravelExpenseTypeCountrySettingsModel
    try {
      List<TravelExpenseTypeCountrySettingsModel> result = apiInstance.travelExpenseTypeCountrySettingsPatchTravelExpenseTypeCountrySettings(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#travelExpenseTypeCountrySettingsPatchTravelExpenseTypeCountrySettings");
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
| **guid** | **String**| ID of the travel expense type country setting | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of TravelExpenseTypeCountrySettingsModel | [optional] |

### Return type

[**List&lt;TravelExpenseTypeCountrySettingsModel&gt;**](TravelExpenseTypeCountrySettingsModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated travel expense type country settings |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="travelExpenseTypeCountrySettingsPostTravelExpenseTypeCountrySettings"></a>
# **travelExpenseTypeCountrySettingsPostTravelExpenseTypeCountrySettings**
> TravelExpenseTypeCountrySettingsModel travelExpenseTypeCountrySettingsPostTravelExpenseTypeCountrySettings(travelExpenseTypeCountrySettingsModel)

Insert a travel expense type country setting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    TravelExpenseTypeCountrySettingsModel travelExpenseTypeCountrySettingsModel = new TravelExpenseTypeCountrySettingsModel(); // TravelExpenseTypeCountrySettingsModel | Travel expense type country setting model
    try {
      TravelExpenseTypeCountrySettingsModel result = apiInstance.travelExpenseTypeCountrySettingsPostTravelExpenseTypeCountrySettings(travelExpenseTypeCountrySettingsModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#travelExpenseTypeCountrySettingsPostTravelExpenseTypeCountrySettings");
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
| **travelExpenseTypeCountrySettingsModel** | [**TravelExpenseTypeCountrySettingsModel**](TravelExpenseTypeCountrySettingsModel.md)| Travel expense type country setting model | [optional] |

### Return type

[**TravelExpenseTypeCountrySettingsModel**](TravelExpenseTypeCountrySettingsModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Added travel expense type country setting |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="travelExpenseTypesPatchTravelExpenseType"></a>
# **travelExpenseTypesPatchTravelExpenseType**
> List&lt;TravelExpenseTypeOutputModel&gt; travelExpenseTypesPatchTravelExpenseType(guid, patchOperation)

Update (Patch) an travel expense type or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | Guid of the travel expense type.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of TravelExpenseTypeInputModel.
    try {
      List<TravelExpenseTypeOutputModel> result = apiInstance.travelExpenseTypesPatchTravelExpenseType(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#travelExpenseTypesPatchTravelExpenseType");
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
| **guid** | **String**| Guid of the travel expense type. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of TravelExpenseTypeInputModel. | [optional] |

### Return type

[**List&lt;TravelExpenseTypeOutputModel&gt;**](TravelExpenseTypeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated travel expense types. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="travelExpenseTypesPostTravelExpenseType"></a>
# **travelExpenseTypesPostTravelExpenseType**
> TravelExpenseTypeOutputModel travelExpenseTypesPostTravelExpenseType(travelExpenseTypeInputModel)

Insert a new travel expense type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    TravelExpenseTypeInputModel travelExpenseTypeInputModel = new TravelExpenseTypeInputModel(); // TravelExpenseTypeInputModel | TravelExpenseTypeInputModel.
    try {
      TravelExpenseTypeOutputModel result = apiInstance.travelExpenseTypesPostTravelExpenseType(travelExpenseTypeInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#travelExpenseTypesPostTravelExpenseType");
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
| **travelExpenseTypeInputModel** | [**TravelExpenseTypeInputModel**](TravelExpenseTypeInputModel.md)| TravelExpenseTypeInputModel. | [optional] |

### Return type

[**TravelExpenseTypeOutputModel**](TravelExpenseTypeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created travel expense type. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="travelReimbursementStatusPatchTravelReimbursementStatus"></a>
# **travelReimbursementStatusPatchTravelReimbursementStatus**
> List&lt;TravelReimbursementStatusModel&gt; travelReimbursementStatusPatchTravelReimbursementStatus(guid, patchOperation)

Update (Patch) a travel reimbursement status or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the travel reimbursement status.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of TravelReimbursementStatusModel.
    try {
      List<TravelReimbursementStatusModel> result = apiInstance.travelReimbursementStatusPatchTravelReimbursementStatus(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#travelReimbursementStatusPatchTravelReimbursementStatus");
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
| **guid** | **String**| ID of the travel reimbursement status. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of TravelReimbursementStatusModel. | [optional] |

### Return type

[**List&lt;TravelReimbursementStatusModel&gt;**](TravelReimbursementStatusModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated travel reimbursement statuses. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="travelReimbursementStatusPostTravelReimbursementStatus"></a>
# **travelReimbursementStatusPostTravelReimbursementStatus**
> TravelReimbursementStatusModel travelReimbursementStatusPostTravelReimbursementStatus(travelReimbursementStatusModel)

Insert a travel reimbursement status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    TravelReimbursementStatusModel travelReimbursementStatusModel = new TravelReimbursementStatusModel(); // TravelReimbursementStatusModel | TravelReimbursementStatusModel.
    try {
      TravelReimbursementStatusModel result = apiInstance.travelReimbursementStatusPostTravelReimbursementStatus(travelReimbursementStatusModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#travelReimbursementStatusPostTravelReimbursementStatus");
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
| **travelReimbursementStatusModel** | [**TravelReimbursementStatusModel**](TravelReimbursementStatusModel.md)| TravelReimbursementStatusModel. | [optional] |

### Return type

[**TravelReimbursementStatusModel**](TravelReimbursementStatusModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created travel reimbursement status. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="userCustomPropertiesPatchUserCustomProperty"></a>
# **userCustomPropertiesPatchUserCustomProperty**
> List&lt;UserCustomPropertyOutputModel&gt; userCustomPropertiesPatchUserCustomProperty(guid, patchOperation)

Update (Patch) a user custom property or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the user custom property Can also be comma separate list of IDs to patch multiple user custom properties with one call. When multiple IDs are given, returns model which has list of succeeded user custom properties and list of errors.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of UserCustomPropertyModel.
    try {
      List<UserCustomPropertyOutputModel> result = apiInstance.userCustomPropertiesPatchUserCustomProperty(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#userCustomPropertiesPatchUserCustomProperty");
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
| **guid** | **String**| ID of the user custom property Can also be comma separate list of IDs to patch multiple user custom properties with one call. When multiple IDs are given, returns model which has list of succeeded user custom properties and list of errors. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of UserCustomPropertyModel. | [optional] |

### Return type

[**List&lt;UserCustomPropertyOutputModel&gt;**](UserCustomPropertyOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated user custom properties. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="userCustomPropertiesPostUserCustomProperty"></a>
# **userCustomPropertiesPostUserCustomProperty**
> UserCustomPropertyOutputModel userCustomPropertiesPostUserCustomProperty(userCustomPropertyInputModel)

Insert a user custom property.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    UserCustomPropertyInputModel userCustomPropertyInputModel = new UserCustomPropertyInputModel(); // UserCustomPropertyInputModel | UserCustomPropertyModel.
    try {
      UserCustomPropertyOutputModel result = apiInstance.userCustomPropertiesPostUserCustomProperty(userCustomPropertyInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#userCustomPropertiesPostUserCustomProperty");
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
| **userCustomPropertyInputModel** | [**UserCustomPropertyInputModel**](UserCustomPropertyInputModel.md)| UserCustomPropertyModel. | [optional] |

### Return type

[**UserCustomPropertyOutputModel**](UserCustomPropertyOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created user custom property. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="userCustomPropertySelectionItemsPatchUserCustomPropertySelectionItem"></a>
# **userCustomPropertySelectionItemsPatchUserCustomPropertySelectionItem**
> List&lt;UserCustomPropertySelectionItemOutputModel&gt; userCustomPropertySelectionItemsPatchUserCustomPropertySelectionItem(guid, patchOperation)

Update (Patch) a user custom property selection item or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the user custom property selection item.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of UserCustomPropertySelectionItemInputModel.
    try {
      List<UserCustomPropertySelectionItemOutputModel> result = apiInstance.userCustomPropertySelectionItemsPatchUserCustomPropertySelectionItem(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#userCustomPropertySelectionItemsPatchUserCustomPropertySelectionItem");
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
| **guid** | **String**| ID of the user custom property selection item. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of UserCustomPropertySelectionItemInputModel. | [optional] |

### Return type

[**List&lt;UserCustomPropertySelectionItemOutputModel&gt;**](UserCustomPropertySelectionItemOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated user custom properties. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="userCustomPropertySelectionItemsPostUserCustomPropertySelectionItem"></a>
# **userCustomPropertySelectionItemsPostUserCustomPropertySelectionItem**
> UserCustomPropertySelectionItemOutputModel userCustomPropertySelectionItemsPostUserCustomPropertySelectionItem(userCustomPropertySelectionItemInputModel)

Insert a user custom property selection item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    UserCustomPropertySelectionItemInputModel userCustomPropertySelectionItemInputModel = new UserCustomPropertySelectionItemInputModel(); // UserCustomPropertySelectionItemInputModel | UserPropertySelectionItemInputModel.
    try {
      UserCustomPropertySelectionItemOutputModel result = apiInstance.userCustomPropertySelectionItemsPostUserCustomPropertySelectionItem(userCustomPropertySelectionItemInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#userCustomPropertySelectionItemsPostUserCustomPropertySelectionItem");
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
| **userCustomPropertySelectionItemInputModel** | [**UserCustomPropertySelectionItemInputModel**](UserCustomPropertySelectionItemInputModel.md)| UserPropertySelectionItemInputModel. | [optional] |

### Return type

[**UserCustomPropertySelectionItemOutputModel**](UserCustomPropertySelectionItemOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created user custom property. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="vatRatesPatchVatRate"></a>
# **vatRatesPatchVatRate**
> List&lt;VatRateOutputModel&gt; vatRatesPatchVatRate(guid, patchOperation)

Update (Patch) a vat rate or a part of it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | GUID of the vat rate
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of ValueAddedTaxModel
    try {
      List<VatRateOutputModel> result = apiInstance.vatRatesPatchVatRate(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#vatRatesPatchVatRate");
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
| **guid** | **String**| GUID of the vat rate | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of ValueAddedTaxModel | [optional] |

### Return type

[**List&lt;VatRateOutputModel&gt;**](VatRateOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated vat rates |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="vatRatesPostVatRate"></a>
# **vatRatesPostVatRate**
> VatRateOutputModel vatRatesPostVatRate(vatRateInputModel)

Insert a vat rate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    VatRateInputModel vatRateInputModel = new VatRateInputModel(); // VatRateInputModel | VatRateInputModel
    try {
      VatRateOutputModel result = apiInstance.vatRatesPostVatRate(vatRateInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#vatRatesPostVatRate");
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
| **vatRateInputModel** | [**VatRateInputModel**](VatRateInputModel.md)| VatRateInputModel | [optional] |

### Return type

[**VatRateOutputModel**](VatRateOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Inserted vat rate |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workContractsPatchWorkContract"></a>
# **workContractsPatchWorkContract**
> List&lt;WorkContractOutputModel&gt; workContractsPatchWorkContract(guid, patchOperation)

Update (Patch) a work contract or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the work contract.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of WorkContractOutputModel.
    try {
      List<WorkContractOutputModel> result = apiInstance.workContractsPatchWorkContract(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#workContractsPatchWorkContract");
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
| **guid** | **String**| ID of the work contract. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of WorkContractOutputModel. | [optional] |

### Return type

[**List&lt;WorkContractOutputModel&gt;**](WorkContractOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated work contract. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workContractsPostWorkContract"></a>
# **workContractsPostWorkContract**
> WorkContractOutputModel workContractsPostWorkContract(resetFlextime, workContractInputModel)

Insert a work contract.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    Boolean resetFlextime = true; // Boolean | Optional. Reset flextime to zero when new work contract starts or keep the flextime value. Default true = reset flextime.
    WorkContractInputModel workContractInputModel = new WorkContractInputModel(); // WorkContractInputModel | WorkContractOutputModel.
    try {
      WorkContractOutputModel result = apiInstance.workContractsPostWorkContract(resetFlextime, workContractInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#workContractsPostWorkContract");
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
| **resetFlextime** | **Boolean**| Optional. Reset flextime to zero when new work contract starts or keep the flextime value. Default true &#x3D; reset flextime. | [optional] [default to true] |
| **workContractInputModel** | [**WorkContractInputModel**](WorkContractInputModel.md)| WorkContractOutputModel. | [optional] |

### Return type

[**WorkContractOutputModel**](WorkContractOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created work contract. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workTypesPatchWorkType"></a>
# **workTypesPatchWorkType**
> List&lt;WorkTypeOutputModel&gt; workTypesPatchWorkType(guid, patchOperation)

Update (Patch) a work type or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the work type.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of WorkTypeModel.
    try {
      List<WorkTypeOutputModel> result = apiInstance.workTypesPatchWorkType(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#workTypesPatchWorkType");
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
| **guid** | **String**| ID of the work type. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of WorkTypeModel. | [optional] |

### Return type

[**List&lt;WorkTypeOutputModel&gt;**](WorkTypeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated work types. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workTypesPostWorkType"></a>
# **workTypesPostWorkType**
> WorkTypeOutputModel workTypesPostWorkType(workTypeInputModel)

Insert a work type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsWriteApi;

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

    SettingsWriteApi apiInstance = new SettingsWriteApi(defaultClient);
    WorkTypeInputModel workTypeInputModel = new WorkTypeInputModel(); // WorkTypeInputModel | WorkTypeModel.
    try {
      WorkTypeOutputModel result = apiInstance.workTypesPostWorkType(workTypeInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsWriteApi#workTypesPostWorkType");
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
| **workTypeInputModel** | [**WorkTypeInputModel**](WorkTypeInputModel.md)| WorkTypeModel. | [optional] |

### Return type

[**WorkTypeOutputModel**](WorkTypeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created work type. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

