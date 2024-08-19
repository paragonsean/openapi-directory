# SettingsDeleteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activityTypesDeleteActivityType**](SettingsDeleteApi.md#activityTypesDeleteActivityType) | **DELETE** /v1/activitytypes/{guid} | Delete an activity type. |
| [**communicationTypesDeleteCommunicationType**](SettingsDeleteApi.md#communicationTypesDeleteCommunicationType) | **DELETE** /v1/communicationtypes/{guid} | Deletes a communication type. |
| [**contactRolesDeleteContactRole**](SettingsDeleteApi.md#contactRolesDeleteContactRole) | **DELETE** /v1/contactroles/{guid} | Delete a contact role. |
| [**costAccountsDeleteCostAccount**](SettingsDeleteApi.md#costAccountsDeleteCostAccount) | **DELETE** /v1/costaccounts/{guid} | Delete a cost account. |
| [**costCentersDeleteCostCenter**](SettingsDeleteApi.md#costCentersDeleteCostCenter) | **DELETE** /v1/costcenters/{guid} | Delete a cost center. |
| [**customerCustomPropertiesDeleteCustomerCustomProperty**](SettingsDeleteApi.md#customerCustomPropertiesDeleteCustomerCustomProperty) | **DELETE** /v1/customers/customproperties/{guid} | Deletes a customer custom property. |
| [**customerCustomPropertySelectionItemsDeleteCustomerCustomPropertySelectionItem**](SettingsDeleteApi.md#customerCustomPropertySelectionItemsDeleteCustomerCustomPropertySelectionItem) | **DELETE** /v1/customers/customproperties/customercustompropertyselectionitems/{guid} | Deletes a customer custom property selection item. |
| [**industriesDeleteIndustry**](SettingsDeleteApi.md#industriesDeleteIndustry) | **DELETE** /v1/industries/{guid} | Delete an industry. |
| [**invoiceStatusesDeleteInvoiceStatus**](SettingsDeleteApi.md#invoiceStatusesDeleteInvoiceStatus) | **DELETE** /v1/invoicestatuses/{guid} | Delete an invoice status. |
| [**keywordsDeleteKeyword**](SettingsDeleteApi.md#keywordsDeleteKeyword) | **DELETE** /v1/keywords/{guid} | Delete keyword by ID. It will also be deleted from any entity it is used in (Project, etc.) |
| [**leadSourcesDeleteLeadSource**](SettingsDeleteApi.md#leadSourcesDeleteLeadSource) | **DELETE** /v1/leadsources/{guid} | Delete a lead source. |
| [**marketSegmentsDeleteMarketSegment**](SettingsDeleteApi.md#marketSegmentsDeleteMarketSegment) | **DELETE** /v1/marketsegments/{guid} | Delete a market segment. |
| [**overtimesDeleteOvertime**](SettingsDeleteApi.md#overtimesDeleteOvertime) | **DELETE** /v1/overtimes/{guid} | Delete an overtime. |
| [**phaseStatusTypesDeletePhaseStatusType**](SettingsDeleteApi.md#phaseStatusTypesDeletePhaseStatusType) | **DELETE** /v1/phasestatustypes/{guid} | Delete a phase status type |
| [**productCategoriesDeleteProductCategory**](SettingsDeleteApi.md#productCategoriesDeleteProductCategory) | **DELETE** /v1/productcategories/{guid} | Delete a product category. |
| [**productCountrySettingsDeleteProductCountrySetting**](SettingsDeleteApi.md#productCountrySettingsDeleteProductCountrySetting) | **DELETE** /v1/productcountrysettings/{guid} | Deletes a product country setting |
| [**productsDeleteProduct**](SettingsDeleteApi.md#productsDeleteProduct) | **DELETE** /v1/products/{guid} | Delete a product. |
| [**projectBillingCustomersDeleteProjectBillingCustomer**](SettingsDeleteApi.md#projectBillingCustomersDeleteProjectBillingCustomer) | **DELETE** /v1/projectbillingcustomers/{guid} | Deletes a project billing customer. |
| [**projectCustomPropertiesDeleteProjectCustomProperty**](SettingsDeleteApi.md#projectCustomPropertiesDeleteProjectCustomProperty) | **DELETE** /v1/projects/customproperties/{guid} | Deletes a project custom property. |
| [**projectCustomPropertySelectionItemsDeleteProjectCustomPropertySelectionItem**](SettingsDeleteApi.md#projectCustomPropertySelectionItemsDeleteProjectCustomPropertySelectionItem) | **DELETE** /v1/projects/customproperties/projectcustompropertyselectionitems/{guid} | Deletes a project custom property selection item. |
| [**projectMemberCostExceptionsDelete**](SettingsDeleteApi.md#projectMemberCostExceptionsDelete) | **DELETE** /v1/projectmembercostexceptions/{guid} | Deletes a project member cost exception. |
| [**projectStatusTypesDeleteProjectStatusType**](SettingsDeleteApi.md#projectStatusTypesDeleteProjectStatusType) | **DELETE** /v1/projectstatustypes/{guid} | Delete a projectStatusType |
| [**projectTaskStatusesDeleteProjectTaskStatus**](SettingsDeleteApi.md#projectTaskStatusesDeleteProjectTaskStatus) | **DELETE** /v1/projecttaskstatuses/{guid} | Delete a project task status. |
| [**proposalStatusesDeleteProposalStatus**](SettingsDeleteApi.md#proposalStatusesDeleteProposalStatus) | **DELETE** /v1/proposalstatuses/{guid} | Delete an proposal status |
| [**rolesDeleteRole**](SettingsDeleteApi.md#rolesDeleteRole) | **DELETE** /v1/roles/{guid} | Delete a role. |
| [**salesAccountsDeleteSalesAccount**](SettingsDeleteApi.md#salesAccountsDeleteSalesAccount) | **DELETE** /v1/salesaccounts/{guid} | Delete a sales account. |
| [**salesStatusTypesDeleteSalesStatusType**](SettingsDeleteApi.md#salesStatusTypesDeleteSalesStatusType) | **DELETE** /v1/salesstatustypes/{guid} | Delete an sales status type. |
| [**timeEntryTypesDeleteTimeEntryType**](SettingsDeleteApi.md#timeEntryTypesDeleteTimeEntryType) | **DELETE** /v1/timeentrytypes/{guid} | Deletes a time entry type. |
| [**travelExpenseTypeCountrySettingsDeleteTravelExpenseTypeCountrySetting**](SettingsDeleteApi.md#travelExpenseTypeCountrySettingsDeleteTravelExpenseTypeCountrySetting) | **DELETE** /v1/travelexpensetypecountrysettings/{guid} | Deletes a travel expense type country setting |
| [**travelExpenseTypesDeleteTravelExpenseType**](SettingsDeleteApi.md#travelExpenseTypesDeleteTravelExpenseType) | **DELETE** /v1/travelexpensetypes/{guid} | Deletes a travel expense type. |
| [**travelReimbursementStatusDeleteTravelReimbursementStatus**](SettingsDeleteApi.md#travelReimbursementStatusDeleteTravelReimbursementStatus) | **DELETE** /v1/travelreimbursementstatuses/{guid} | Delete a travel reimbursement status. |
| [**userCustomPropertiesDeleteUserCustomProperty**](SettingsDeleteApi.md#userCustomPropertiesDeleteUserCustomProperty) | **DELETE** /v1/users/customproperties/{guid} | Deletes a user custom property. |
| [**userCustomPropertySelectionItemsDeleteUserCustomPropertySelectionItem**](SettingsDeleteApi.md#userCustomPropertySelectionItemsDeleteUserCustomPropertySelectionItem) | **DELETE** /v1/users/customproperties/usercustompropertyselectionitems/{guid} | Deletes a user custom property selection item. |
| [**vatRatesDeleteVatRate**](SettingsDeleteApi.md#vatRatesDeleteVatRate) | **DELETE** /v1/vatrates/{guid} | Delete a vat rate |
| [**workContractsDeleteWorkContract**](SettingsDeleteApi.md#workContractsDeleteWorkContract) | **DELETE** /v1/workcontracts/{guid} | Delete a work contract. |
| [**workTypesDeleteWorkType**](SettingsDeleteApi.md#workTypesDeleteWorkType) | **DELETE** /v1/worktypes/{guid} | Deletes a work type. |


<a id="activityTypesDeleteActivityType"></a>
# **activityTypesDeleteActivityType**
> activityTypesDeleteActivityType(guid, moveUsagesToGuid)

Delete an activity type.

Returns: No Content (204) if succeeded. Not found (404) if activity type can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the activity type to delete
    String moveUsagesToGuid = "moveUsagesToGuid_example"; // String | Optional: ID of the activity type to which to move usages of this activity type. Default null. If activity type is in use and usages aren't moved the deletion might fail.
    try {
      apiInstance.activityTypesDeleteActivityType(guid, moveUsagesToGuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#activityTypesDeleteActivityType");
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
| **guid** | **String**| ID for the activity type to delete | |
| **moveUsagesToGuid** | **String**| Optional: ID of the activity type to which to move usages of this activity type. Default null. If activity type is in use and usages aren&#39;t moved the deletion might fail. | [optional] |

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

<a id="communicationTypesDeleteCommunicationType"></a>
# **communicationTypesDeleteCommunicationType**
> communicationTypesDeleteCommunicationType(guid)

Deletes a communication type.

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the communication type.
    try {
      apiInstance.communicationTypesDeleteCommunicationType(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#communicationTypesDeleteCommunicationType");
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
| **guid** | **String**| GUID used to delete the communication type. | |

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

<a id="contactRolesDeleteContactRole"></a>
# **contactRolesDeleteContactRole**
> contactRolesDeleteContactRole(guid, moveUsagesToGuid)

Delete a contact role.

Returns: No Content (204) if succeeded. Not found (404) if contact role can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the contact role to delete.
    String moveUsagesToGuid = "moveUsagesToGuid_example"; // String | Optional: ID of the contact role to which to move usages of this contact role. Default null. If contact role is in use and usages aren't moved the deletion might fail.
    try {
      apiInstance.contactRolesDeleteContactRole(guid, moveUsagesToGuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#contactRolesDeleteContactRole");
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
| **guid** | **String**| ID for the contact role to delete. | |
| **moveUsagesToGuid** | **String**| Optional: ID of the contact role to which to move usages of this contact role. Default null. If contact role is in use and usages aren&#39;t moved the deletion might fail. | [optional] |

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

<a id="costAccountsDeleteCostAccount"></a>
# **costAccountsDeleteCostAccount**
> costAccountsDeleteCostAccount(guid)

Delete a cost account.

Returns: No Content (204) if succeeded. Not found (404) if cost account can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the cost account to delete.
    try {
      apiInstance.costAccountsDeleteCostAccount(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#costAccountsDeleteCostAccount");
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
| **guid** | **String**| ID for the cost account to delete. | |

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

<a id="costCentersDeleteCostCenter"></a>
# **costCentersDeleteCostCenter**
> costCentersDeleteCostCenter(guid)

Delete a cost center.

Returns: No Content (204) if succeeded. Not found (404) if cost center can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the cost center to delete.
    try {
      apiInstance.costCentersDeleteCostCenter(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#costCentersDeleteCostCenter");
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
| **guid** | **String**| ID for the cost center to delete. | |

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

<a id="customerCustomPropertiesDeleteCustomerCustomProperty"></a>
# **customerCustomPropertiesDeleteCustomerCustomProperty**
> customerCustomPropertiesDeleteCustomerCustomProperty(guid)

Deletes a customer custom property.

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the customer custom property.
    try {
      apiInstance.customerCustomPropertiesDeleteCustomerCustomProperty(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#customerCustomPropertiesDeleteCustomerCustomProperty");
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
| **guid** | **String**| GUID used to delete the customer custom property. | |

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

<a id="customerCustomPropertySelectionItemsDeleteCustomerCustomPropertySelectionItem"></a>
# **customerCustomPropertySelectionItemsDeleteCustomerCustomPropertySelectionItem**
> customerCustomPropertySelectionItemsDeleteCustomerCustomPropertySelectionItem(guid)

Deletes a customer custom property selection item.

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the customer custom property selection item.
    try {
      apiInstance.customerCustomPropertySelectionItemsDeleteCustomerCustomPropertySelectionItem(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#customerCustomPropertySelectionItemsDeleteCustomerCustomPropertySelectionItem");
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
| **guid** | **String**| GUID used to delete the customer custom property selection item. | |

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

<a id="industriesDeleteIndustry"></a>
# **industriesDeleteIndustry**
> industriesDeleteIndustry(guid, moveUsagesToGuid)

Delete an industry.

Returns: No Content (204) if succeeded. Not found (404) if industry can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the industry to delete.
    String moveUsagesToGuid = "moveUsagesToGuid_example"; // String | Optional: ID of the industry to which to move usages of this industry. Default null. If industry is in use and usages aren't moved the deletion might fail.
    try {
      apiInstance.industriesDeleteIndustry(guid, moveUsagesToGuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#industriesDeleteIndustry");
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
| **guid** | **String**| ID for the industry to delete. | |
| **moveUsagesToGuid** | **String**| Optional: ID of the industry to which to move usages of this industry. Default null. If industry is in use and usages aren&#39;t moved the deletion might fail. | [optional] |

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

<a id="invoiceStatusesDeleteInvoiceStatus"></a>
# **invoiceStatusesDeleteInvoiceStatus**
> invoiceStatusesDeleteInvoiceStatus(guid)

Delete an invoice status.

Returns: No Content (204) if succeeded. Not found (404) if invoice status can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the invoice status to delete.
    try {
      apiInstance.invoiceStatusesDeleteInvoiceStatus(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#invoiceStatusesDeleteInvoiceStatus");
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
| **guid** | **String**| ID for the invoice status to delete. | |

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

<a id="keywordsDeleteKeyword"></a>
# **keywordsDeleteKeyword**
> keywordsDeleteKeyword(guid, moveUsagesToGuid)

Delete keyword by ID. It will also be deleted from any entity it is used in (Project, etc.)

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the keyword.
    String moveUsagesToGuid = "moveUsagesToGuid_example"; // String | Optional: ID of the keyword to which to move usages of this keyword. Default null. If keyword is in use and usages aren't moved the deletion might fail.
    try {
      apiInstance.keywordsDeleteKeyword(guid, moveUsagesToGuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#keywordsDeleteKeyword");
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
| **guid** | **String**| GUID used to get the keyword. | |
| **moveUsagesToGuid** | **String**| Optional: ID of the keyword to which to move usages of this keyword. Default null. If keyword is in use and usages aren&#39;t moved the deletion might fail. | [optional] |

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

<a id="leadSourcesDeleteLeadSource"></a>
# **leadSourcesDeleteLeadSource**
> leadSourcesDeleteLeadSource(guid, moveUsagesToGuid)

Delete a lead source.

Returns: No Content (204) if succeeded. Not found (404) if lead source can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the lead source to delete.
    String moveUsagesToGuid = "moveUsagesToGuid_example"; // String | Optional: ID of the lead source to which to move usages of this lead source. Default null. If industry is in use and usages aren't moved the deletion might fail.
    try {
      apiInstance.leadSourcesDeleteLeadSource(guid, moveUsagesToGuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#leadSourcesDeleteLeadSource");
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
| **guid** | **String**| ID for the lead source to delete. | |
| **moveUsagesToGuid** | **String**| Optional: ID of the lead source to which to move usages of this lead source. Default null. If industry is in use and usages aren&#39;t moved the deletion might fail. | [optional] |

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

<a id="marketSegmentsDeleteMarketSegment"></a>
# **marketSegmentsDeleteMarketSegment**
> marketSegmentsDeleteMarketSegment(guid, moveUsagesToGuid)

Delete a market segment.

Returns: No Content (204) if succeeded. Not found (404) if market segment can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the market segment to delete.
    String moveUsagesToGuid = "moveUsagesToGuid_example"; // String | Optional: ID of the lead source to which to move usages of this market segment. Default null.
    try {
      apiInstance.marketSegmentsDeleteMarketSegment(guid, moveUsagesToGuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#marketSegmentsDeleteMarketSegment");
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
| **guid** | **String**| ID for the market segment to delete. | |
| **moveUsagesToGuid** | **String**| Optional: ID of the lead source to which to move usages of this market segment. Default null. | [optional] |

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

<a id="overtimesDeleteOvertime"></a>
# **overtimesDeleteOvertime**
> overtimesDeleteOvertime(guid)

Delete an overtime.

Returns: No Content (204) if succeeded. Not found (404) if overtime can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the overtime to delete.
    try {
      apiInstance.overtimesDeleteOvertime(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#overtimesDeleteOvertime");
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
| **guid** | **String**| ID for the overtime to delete. | |

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

<a id="phaseStatusTypesDeletePhaseStatusType"></a>
# **phaseStatusTypesDeletePhaseStatusType**
> phaseStatusTypesDeletePhaseStatusType(guid, moveUsagesToGuid)

Delete a phase status type

Returns: No Content (204) if succeeded. Not found (404) if phase status type can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the phase status type to delete
    String moveUsagesToGuid = "moveUsagesToGuid_example"; // String | Optional: ID of the phase status type to which to move usages of this phase status type. Default null. If phase status type is in use and usages aren't moved the deletion might fail.
    try {
      apiInstance.phaseStatusTypesDeletePhaseStatusType(guid, moveUsagesToGuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#phaseStatusTypesDeletePhaseStatusType");
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
| **guid** | **String**| ID for the phase status type to delete | |
| **moveUsagesToGuid** | **String**| Optional: ID of the phase status type to which to move usages of this phase status type. Default null. If phase status type is in use and usages aren&#39;t moved the deletion might fail. | [optional] |

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

<a id="productCategoriesDeleteProductCategory"></a>
# **productCategoriesDeleteProductCategory**
> productCategoriesDeleteProductCategory(guid)

Delete a product category.

Returns: No Content (204) if succeeded. Not found (404) if product category can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the product category to delete.
    try {
      apiInstance.productCategoriesDeleteProductCategory(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#productCategoriesDeleteProductCategory");
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
| **guid** | **String**| ID for the product category to delete. | |

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

<a id="productCountrySettingsDeleteProductCountrySetting"></a>
# **productCountrySettingsDeleteProductCountrySetting**
> productCountrySettingsDeleteProductCountrySetting(guid)

Deletes a product country setting

Returns: No Content (204) if succeeded. Not found (404) if product country setting can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the product country setting.
    try {
      apiInstance.productCountrySettingsDeleteProductCountrySetting(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#productCountrySettingsDeleteProductCountrySetting");
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
| **guid** | **String**| GUID used to delete the product country setting. | |

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

<a id="productsDeleteProduct"></a>
# **productsDeleteProduct**
> productsDeleteProduct(guid)

Delete a product.

Returns: No Content (204) if succeeded. Not found (404) if product can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the product to delete.
    try {
      apiInstance.productsDeleteProduct(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#productsDeleteProduct");
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
| **guid** | **String**| ID for the product to delete. | |

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

<a id="projectBillingCustomersDeleteProjectBillingCustomer"></a>
# **projectBillingCustomersDeleteProjectBillingCustomer**
> projectBillingCustomersDeleteProjectBillingCustomer(guid)

Deletes a project billing customer.

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID of the project billing customer to remove.
    try {
      apiInstance.projectBillingCustomersDeleteProjectBillingCustomer(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#projectBillingCustomersDeleteProjectBillingCustomer");
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
| **guid** | **String**| GUID of the project billing customer to remove. | |

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

<a id="projectCustomPropertiesDeleteProjectCustomProperty"></a>
# **projectCustomPropertiesDeleteProjectCustomProperty**
> projectCustomPropertiesDeleteProjectCustomProperty(guid)

Deletes a project custom property.

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the project custom property.
    try {
      apiInstance.projectCustomPropertiesDeleteProjectCustomProperty(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#projectCustomPropertiesDeleteProjectCustomProperty");
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
| **guid** | **String**| GUID used to delete the project custom property. | |

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

<a id="projectCustomPropertySelectionItemsDeleteProjectCustomPropertySelectionItem"></a>
# **projectCustomPropertySelectionItemsDeleteProjectCustomPropertySelectionItem**
> projectCustomPropertySelectionItemsDeleteProjectCustomPropertySelectionItem(guid)

Deletes a project custom property selection item.

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the project custom property selection item.
    try {
      apiInstance.projectCustomPropertySelectionItemsDeleteProjectCustomPropertySelectionItem(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#projectCustomPropertySelectionItemsDeleteProjectCustomPropertySelectionItem");
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
| **guid** | **String**| GUID used to delete the project custom property selection item. | |

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

<a id="projectMemberCostExceptionsDelete"></a>
# **projectMemberCostExceptionsDelete**
> projectMemberCostExceptionsDelete(guid)

Deletes a project member cost exception.

Deletes project member cost exception. Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the project member cost exception.
    try {
      apiInstance.projectMemberCostExceptionsDelete(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#projectMemberCostExceptionsDelete");
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
| **guid** | **String**| GUID used to delete the project member cost exception. | |

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

<a id="projectStatusTypesDeleteProjectStatusType"></a>
# **projectStatusTypesDeleteProjectStatusType**
> projectStatusTypesDeleteProjectStatusType(guid, moveUsagesToGuid)

Delete a projectStatusType

Returns: No Content (204) if succeeded. Not found (404) if projectStatusType can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the projectStatusType to delete
    String moveUsagesToGuid = "moveUsagesToGuid_example"; // String | Optional: ID of the project status type to which to move usages of this project status type. Default null. If project status type is in use and usages aren't moved the deletion might fail.
    try {
      apiInstance.projectStatusTypesDeleteProjectStatusType(guid, moveUsagesToGuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#projectStatusTypesDeleteProjectStatusType");
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
| **guid** | **String**| ID for the projectStatusType to delete | |
| **moveUsagesToGuid** | **String**| Optional: ID of the project status type to which to move usages of this project status type. Default null. If project status type is in use and usages aren&#39;t moved the deletion might fail. | [optional] |

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

<a id="projectTaskStatusesDeleteProjectTaskStatus"></a>
# **projectTaskStatusesDeleteProjectTaskStatus**
> projectTaskStatusesDeleteProjectTaskStatus(guid, moveUsagesToGuid)

Delete a project task status.

Returns: No Content (204) if succeeded. Not found (404) if product can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the project task status to delete.
    String moveUsagesToGuid = "moveUsagesToGuid_example"; // String | Optional: ID of the project task status to which to move usages of this project task status. Default null.
    try {
      apiInstance.projectTaskStatusesDeleteProjectTaskStatus(guid, moveUsagesToGuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#projectTaskStatusesDeleteProjectTaskStatus");
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
| **guid** | **String**| ID for the project task status to delete. | |
| **moveUsagesToGuid** | **String**| Optional: ID of the project task status to which to move usages of this project task status. Default null. | [optional] |

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

<a id="proposalStatusesDeleteProposalStatus"></a>
# **proposalStatusesDeleteProposalStatus**
> proposalStatusesDeleteProposalStatus(guid, moveUsagesToGuid)

Delete an proposal status

Returns: No Content (204) if succeeded. Not found (404) if proposal status can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the proposal status to delete
    String moveUsagesToGuid = "moveUsagesToGuid_example"; // String | Optional: ID of the proposal status to which to move usages of this proposal status. Default null. If proposal status is in use and usages aren't moved the deletion might fail.
    try {
      apiInstance.proposalStatusesDeleteProposalStatus(guid, moveUsagesToGuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#proposalStatusesDeleteProposalStatus");
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
| **guid** | **String**| ID for the proposal status to delete | |
| **moveUsagesToGuid** | **String**| Optional: ID of the proposal status to which to move usages of this proposal status. Default null. If proposal status is in use and usages aren&#39;t moved the deletion might fail. | [optional] |

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

<a id="rolesDeleteRole"></a>
# **rolesDeleteRole**
> rolesDeleteRole(guid)

Delete a role.

Returns: No Content (204) if succeeded. Not found (404) if role can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the role to delete.
    try {
      apiInstance.rolesDeleteRole(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#rolesDeleteRole");
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
| **guid** | **String**| ID for the role to delete. | |

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

<a id="salesAccountsDeleteSalesAccount"></a>
# **salesAccountsDeleteSalesAccount**
> salesAccountsDeleteSalesAccount(guid)

Delete a sales account.

Returns: No Content (204) if succeeded. Not found (404) if sales account can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the sales account to delete.
    try {
      apiInstance.salesAccountsDeleteSalesAccount(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#salesAccountsDeleteSalesAccount");
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
| **guid** | **String**| ID for the sales account to delete. | |

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

<a id="salesStatusTypesDeleteSalesStatusType"></a>
# **salesStatusTypesDeleteSalesStatusType**
> salesStatusTypesDeleteSalesStatusType(guid, moveUsagesToGuid)

Delete an sales status type.

Returns: No Content (204) if succeeded. Not found (404) if sales status type can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the sales status type to delete.
    String moveUsagesToGuid = "moveUsagesToGuid_example"; // String | Optional: ID of the sales status type to which to move usages of this sales status type. Default null. If sales status type is in use and usages aren't moved the deletion might fail.
    try {
      apiInstance.salesStatusTypesDeleteSalesStatusType(guid, moveUsagesToGuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#salesStatusTypesDeleteSalesStatusType");
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
| **guid** | **String**| ID for the sales status type to delete. | |
| **moveUsagesToGuid** | **String**| Optional: ID of the sales status type to which to move usages of this sales status type. Default null. If sales status type is in use and usages aren&#39;t moved the deletion might fail. | [optional] |

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

<a id="timeEntryTypesDeleteTimeEntryType"></a>
# **timeEntryTypesDeleteTimeEntryType**
> timeEntryTypesDeleteTimeEntryType(guid)

Deletes a time entry type.

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the time entry type.
    try {
      apiInstance.timeEntryTypesDeleteTimeEntryType(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#timeEntryTypesDeleteTimeEntryType");
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
| **guid** | **String**| GUID used to delete the time entry type. | |

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

<a id="travelExpenseTypeCountrySettingsDeleteTravelExpenseTypeCountrySetting"></a>
# **travelExpenseTypeCountrySettingsDeleteTravelExpenseTypeCountrySetting**
> travelExpenseTypeCountrySettingsDeleteTravelExpenseTypeCountrySetting(guid)

Deletes a travel expense type country setting

Returns: No Content (204) if succeeded. Not found (404) if travel expense type country setting can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the travel expense type country setting.
    try {
      apiInstance.travelExpenseTypeCountrySettingsDeleteTravelExpenseTypeCountrySetting(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#travelExpenseTypeCountrySettingsDeleteTravelExpenseTypeCountrySetting");
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
| **guid** | **String**| GUID used to delete the travel expense type country setting. | |

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

<a id="travelExpenseTypesDeleteTravelExpenseType"></a>
# **travelExpenseTypesDeleteTravelExpenseType**
> travelExpenseTypesDeleteTravelExpenseType(guid)

Deletes a travel expense type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | Guid for the travel expense type to delete.
    try {
      apiInstance.travelExpenseTypesDeleteTravelExpenseType(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#travelExpenseTypesDeleteTravelExpenseType");
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
| **guid** | **String**| Guid for the travel expense type to delete. | |

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

<a id="travelReimbursementStatusDeleteTravelReimbursementStatus"></a>
# **travelReimbursementStatusDeleteTravelReimbursementStatus**
> travelReimbursementStatusDeleteTravelReimbursementStatus(guid, moveUsagesToGuid)

Delete a travel reimbursement status.

Returns: No Content (204) if succeeded. Not found (404) if travel reimbursement status can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the travel reimbursement status to delete.
    String moveUsagesToGuid = "moveUsagesToGuid_example"; // String | Optional: ID of the travel reimbursement status to which to move usages of this travel reimbursement status. Default null. If travel reimbursement status is in use and usages aren't moved the deletion might fail.
    try {
      apiInstance.travelReimbursementStatusDeleteTravelReimbursementStatus(guid, moveUsagesToGuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#travelReimbursementStatusDeleteTravelReimbursementStatus");
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
| **guid** | **String**| ID for the travel reimbursement status to delete. | |
| **moveUsagesToGuid** | **String**| Optional: ID of the travel reimbursement status to which to move usages of this travel reimbursement status. Default null. If travel reimbursement status is in use and usages aren&#39;t moved the deletion might fail. | [optional] |

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

<a id="userCustomPropertiesDeleteUserCustomProperty"></a>
# **userCustomPropertiesDeleteUserCustomProperty**
> userCustomPropertiesDeleteUserCustomProperty(guid)

Deletes a user custom property.

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the user custom property.
    try {
      apiInstance.userCustomPropertiesDeleteUserCustomProperty(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#userCustomPropertiesDeleteUserCustomProperty");
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
| **guid** | **String**| GUID used to delete the user custom property. | |

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

<a id="userCustomPropertySelectionItemsDeleteUserCustomPropertySelectionItem"></a>
# **userCustomPropertySelectionItemsDeleteUserCustomPropertySelectionItem**
> userCustomPropertySelectionItemsDeleteUserCustomPropertySelectionItem(guid)

Deletes a user custom property selection item.

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the user custom property selection item.
    try {
      apiInstance.userCustomPropertySelectionItemsDeleteUserCustomPropertySelectionItem(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#userCustomPropertySelectionItemsDeleteUserCustomPropertySelectionItem");
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
| **guid** | **String**| GUID used to delete the user custom property selection item. | |

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

<a id="vatRatesDeleteVatRate"></a>
# **vatRatesDeleteVatRate**
> vatRatesDeleteVatRate(guid)

Delete a vat rate

Returns: No Content (204) if succeeded. Bad Request (400) if vat rate is the default one. Not Found (404) if vat rate can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID for the vat rate to delete
    try {
      apiInstance.vatRatesDeleteVatRate(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#vatRatesDeleteVatRate");
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
| **guid** | **String**| GUID for the vat rate to delete | |

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

<a id="workContractsDeleteWorkContract"></a>
# **workContractsDeleteWorkContract**
> workContractsDeleteWorkContract(guid)

Delete a work contract.

Returns: No Content (204) if succeeded. Not found (404) if work contract can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the work contract to delete.
    try {
      apiInstance.workContractsDeleteWorkContract(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#workContractsDeleteWorkContract");
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
| **guid** | **String**| ID for the work contract to delete. | |

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

<a id="workTypesDeleteWorkType"></a>
# **workTypesDeleteWorkType**
> workTypesDeleteWorkType(guid, moveUsagesToGuid)

Deletes a work type.

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsDeleteApi;

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

    SettingsDeleteApi apiInstance = new SettingsDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the work type.
    String moveUsagesToGuid = "moveUsagesToGuid_example"; // String | Optional: ID of the work type to which to move usages of this work type. Default null. If work type is in use and usages aren't moved the deletion might fail.
    try {
      apiInstance.workTypesDeleteWorkType(guid, moveUsagesToGuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsDeleteApi#workTypesDeleteWorkType");
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
| **guid** | **String**| GUID used to delete the work type. | |
| **moveUsagesToGuid** | **String**| Optional: ID of the work type to which to move usages of this work type. Default null. If work type is in use and usages aren&#39;t moved the deletion might fail. | [optional] |

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

