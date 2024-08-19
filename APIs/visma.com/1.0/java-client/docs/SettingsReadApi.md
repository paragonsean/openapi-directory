# SettingsReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activityTypesGetActivityType**](SettingsReadApi.md#activityTypesGetActivityType) | **GET** /v1/activitytypes/{guid} | Get Activity Type by ID |
| [**activityTypesGetActivityTypes**](SettingsReadApi.md#activityTypesGetActivityTypes) | **GET** /v1/activitytypes | Get the Activity Types |
| [**bankAccountsGetBankAccount**](SettingsReadApi.md#bankAccountsGetBankAccount) | **GET** /v1/bankaccounts/{guid} | Get bank account by ID. |
| [**bankAccountsGetBankAccounts**](SettingsReadApi.md#bankAccountsGetBankAccounts) | **GET** /v1/bankaccounts | Get all bank accounts for current organization. |
| [**businessUnitsGetBusinessUnit**](SettingsReadApi.md#businessUnitsGetBusinessUnit) | **GET** /v1/businessunits/{guid} | Get businessUnit by ID. |
| [**businessUnitsGetBusinessUnits**](SettingsReadApi.md#businessUnitsGetBusinessUnits) | **GET** /v1/businessunits | Get all the BusinessUnits |
| [**communicationTypesGetCommunicationType**](SettingsReadApi.md#communicationTypesGetCommunicationType) | **GET** /v1/communicationtypes/{guid} | Get communication type by ID. |
| [**communicationTypesGetCommunicationTypes**](SettingsReadApi.md#communicationTypesGetCommunicationTypes) | **GET** /v1/communicationtypes | Get all communication types. |
| [**contactRolesGetContactRole**](SettingsReadApi.md#contactRolesGetContactRole) | **GET** /v1/contactroles/{guid} | Get contact role by ID. |
| [**contactRolesGetContactRoles**](SettingsReadApi.md#contactRolesGetContactRoles) | **GET** /v1/contactroles | Get contact roles. |
| [**costAccountsGetCostAccount**](SettingsReadApi.md#costAccountsGetCostAccount) | **GET** /v1/costaccounts/{guid} | Get cost account by Guid. |
| [**costAccountsGetCostAccounts**](SettingsReadApi.md#costAccountsGetCostAccounts) | **GET** /v1/costaccounts | Get cost accounts. |
| [**costCentersGetCostCenter**](SettingsReadApi.md#costCentersGetCostCenter) | **GET** /v1/costcenters/{guid} | Get cost center by ID. |
| [**costCentersGetCostCenters**](SettingsReadApi.md#costCentersGetCostCenters) | **GET** /v1/costcenters | Get cost centers. |
| [**countriesGetCountries**](SettingsReadApi.md#countriesGetCountries) | **GET** /v1/localization/countries | Get all the Countries. |
| [**countriesGetCountry**](SettingsReadApi.md#countriesGetCountry) | **GET** /v1/localization/countries/{guid} | Get country by ID. |
| [**countriesGetCountryByCode2**](SettingsReadApi.md#countriesGetCountryByCode2) | **GET** /v1/localization/countries/{code2} | Get a country by ISO Alpha-2 code |
| [**countriesGetCountryByCode3**](SettingsReadApi.md#countriesGetCountryByCode3) | **GET** /v1/localization/countries/{code3} | Get a country by ISO Alpha-3 code |
| [**countriesGetCountryByName**](SettingsReadApi.md#countriesGetCountryByName) | **GET** /v1/localization/countries/{countryName} | Get a country by name |
| [**countriesGetCountryRegion**](SettingsReadApi.md#countriesGetCountryRegion) | **GET** /v1/localization/countryregions/{guid} | Get country region by ID. |
| [**countriesGetCountryRegions**](SettingsReadApi.md#countriesGetCountryRegions) | **GET** /v1/localization/countries/{countryGuid}/countryregions | Get all the Country regions for a country. |
| [**currenciesGetCurrencies**](SettingsReadApi.md#currenciesGetCurrencies) | **GET** /v1/currencies | Get all the Currencies |
| [**currenciesGetCurrency**](SettingsReadApi.md#currenciesGetCurrency) | **GET** /v1/currencies/{guid} | Get currency by ID. |
| [**customerCustomPropertiesGetCustomerCustomProperties**](SettingsReadApi.md#customerCustomPropertiesGetCustomerCustomProperties) | **GET** /v1/customers/customproperties | Get the customer custom properties. |
| [**customerCustomPropertiesGetCustomerCustomProperty**](SettingsReadApi.md#customerCustomPropertiesGetCustomerCustomProperty) | **GET** /v1/customers/customproperties/{guid} | Get customer custom property by ID. |
| [**customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItem**](SettingsReadApi.md#customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItem) | **GET** /v1/customers/customproperties/customercustompropertyselectionitems/{guid} | Get customer custom property selection item by ID. |
| [**customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItems**](SettingsReadApi.md#customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItems) | **GET** /v1/customers/customproperties/{customPropertyGuid}/customercustompropertyselectionitems | Get the customer custom properties. |
| [**formattingCulturesGetFormattingCulture**](SettingsReadApi.md#formattingCulturesGetFormattingCulture) | **GET** /v1/localization/formattingcultures/{guid} | Get formatting culture by ID. |
| [**formattingCulturesGetFormattings**](SettingsReadApi.md#formattingCulturesGetFormattings) | **GET** /v1/localization/formattingcultures | Get all the Formatting Cultures |
| [**holidaysGetHolidays**](SettingsReadApi.md#holidaysGetHolidays) | **GET** /v1/holidays | Get holidays. |
| [**holidaysGetHolidaysByTimePeriod**](SettingsReadApi.md#holidaysGetHolidaysByTimePeriod) | **GET** /v1/holidaysbytimeperiod | Get holidays with start and end date. |
| [**industriesGetIndustries**](SettingsReadApi.md#industriesGetIndustries) | **GET** /v1/industries | Get all the industries. |
| [**industriesGetIndustry**](SettingsReadApi.md#industriesGetIndustry) | **GET** /v1/industries/{guid} | Get industry by ID. |
| [**invoiceStatusesGetInvoiceStatus**](SettingsReadApi.md#invoiceStatusesGetInvoiceStatus) | **GET** /v1/invoicestatuses/{guid} | Get Invoice status by ID. |
| [**invoiceStatusesGetInvoiceStatuses**](SettingsReadApi.md#invoiceStatusesGetInvoiceStatuses) | **GET** /v1/invoicestatuses | Get invoice statuses. |
| [**invoiceTemplatesGetInvoiceTemplate**](SettingsReadApi.md#invoiceTemplatesGetInvoiceTemplate) | **GET** /v1/invoicetemplates/{guid} | Get invoice template by ID. |
| [**invoiceTemplatesGetInvoiceTemplates**](SettingsReadApi.md#invoiceTemplatesGetInvoiceTemplates) | **GET** /v1/invoicetemplates | Get invoice templates. |
| [**keywordsGetKeyword**](SettingsReadApi.md#keywordsGetKeyword) | **GET** /v1/keywords/{guid} | Get keyword by ID. |
| [**keywordsGetKeywords**](SettingsReadApi.md#keywordsGetKeywords) | **GET** /v1/keywords | Get all the keywords. |
| [**kpiFormulasGetKpiFormulas**](SettingsReadApi.md#kpiFormulasGetKpiFormulas) | **GET** /v1/kpiformulas | Get saved KPI formulas. |
| [**languagesGetLanguage**](SettingsReadApi.md#languagesGetLanguage) | **GET** /v1/localization/languages/{guid} | Get language by ID |
| [**languagesGetLanguages**](SettingsReadApi.md#languagesGetLanguages) | **GET** /v1/localization/languages | Get all the languages |
| [**leadSourcesGetLeadSource**](SettingsReadApi.md#leadSourcesGetLeadSource) | **GET** /v1/leadsources/{guid} | Get lead source by ID. |
| [**leadSourcesGetLeadSources**](SettingsReadApi.md#leadSourcesGetLeadSources) | **GET** /v1/leadsources | Get the lead sources. |
| [**marketSegmentsGetMarketSegment**](SettingsReadApi.md#marketSegmentsGetMarketSegment) | **GET** /v1/marketsegments/{guid} | Get Market Segment by ID. |
| [**marketSegmentsGetMarketSegments**](SettingsReadApi.md#marketSegmentsGetMarketSegments) | **GET** /v1/marketsegments | Get the Market Segments. |
| [**overtimePricesGetOvertimePrice**](SettingsReadApi.md#overtimePricesGetOvertimePrice) | **GET** /v1/overtimeprices/{guid} | Get overtime price by ID. |
| [**overtimePricesGetOvertimePrices**](SettingsReadApi.md#overtimePricesGetOvertimePrices) | **GET** /v1/pricelistversions/{pricelistVersionGuid}/overtimeprices | Get all the overtime prices for a price list version. |
| [**overtimesGetOvertime**](SettingsReadApi.md#overtimesGetOvertime) | **GET** /v1/overtimes/{guid} | Get overtime definition by ID. |
| [**overtimesGetOvertimes**](SettingsReadApi.md#overtimesGetOvertimes) | **GET** /v1/overtimes | Get overtime definitions. |
| [**permissionProfilesGetPermissionProfile**](SettingsReadApi.md#permissionProfilesGetPermissionProfile) | **GET** /v1/permissionprofiles/{guid} | Get Permission Profile by ID. |
| [**permissionProfilesGetPermissionProfiles**](SettingsReadApi.md#permissionProfilesGetPermissionProfiles) | **GET** /v1/permissionprofiles | Get the Permission Profiles. |
| [**phaseStatusTypesGetPhaseStatusType**](SettingsReadApi.md#phaseStatusTypesGetPhaseStatusType) | **GET** /v1/phasestatustypes/{guid} | Get phase status type by GUID |
| [**phaseStatusTypesGetPhaseStatusTypes**](SettingsReadApi.md#phaseStatusTypesGetPhaseStatusTypes) | **GET** /v1/phasestatustypes | Get phase status types |
| [**priceListVersionsGetPricelistVersion**](SettingsReadApi.md#priceListVersionsGetPricelistVersion) | **GET** /v1/pricelistversions/{guid} | Get a price list version by guid. |
| [**priceListVersionsGetPricelistVersionsByPricelist**](SettingsReadApi.md#priceListVersionsGetPricelistVersionsByPricelist) | **GET** /v1/pricelists/{pricelistGuid}/pricelistversions | Get all price list versions of a price list. |
| [**priceListsGetPriceList**](SettingsReadApi.md#priceListsGetPriceList) | **GET** /v1/pricelists/{guid} | Get price list by GUID. |
| [**priceListsGetPricelists**](SettingsReadApi.md#priceListsGetPricelists) | **GET** /v1/pricelists | Get all price lists. |
| [**productCategoriesGetProductCategories**](SettingsReadApi.md#productCategoriesGetProductCategories) | **GET** /v1/productcategories | Get product categories. |
| [**productCategoriesGetProductCategory**](SettingsReadApi.md#productCategoriesGetProductCategory) | **GET** /v1/productcategories/{guid} | Get product category by ID. |
| [**productCountrySettingsGetProductCountrySettings**](SettingsReadApi.md#productCountrySettingsGetProductCountrySettings) | **GET** /v1/products/{productGuid}/productcountrysettings | Get all the country settings for a product |
| [**productPricesGetProductPrice**](SettingsReadApi.md#productPricesGetProductPrice) | **GET** /v1/productprices/{guid} | Get product price by ID. |
| [**productPricesGetProductPrices**](SettingsReadApi.md#productPricesGetProductPrices) | **GET** /v1/pricelistversions/{pricelistVersionGuid}/productprices | Get all the product prices for a price list version. |
| [**productsGetProduct**](SettingsReadApi.md#productsGetProduct) | **GET** /v1/products/{guid} | Get product by ID. |
| [**productsGetProducts**](SettingsReadApi.md#productsGetProducts) | **GET** /v1/products | Get all the Products |
| [**projectBillingCustomersGetProjectBillingCustomer**](SettingsReadApi.md#projectBillingCustomersGetProjectBillingCustomer) | **GET** /v1/projectbillingcustomers/{guid} | Get a project billing customer. |
| [**projectCustomPropertiesGetProjectCustomProperties**](SettingsReadApi.md#projectCustomPropertiesGetProjectCustomProperties) | **GET** /v1/projects/customproperties | Get the project custom properties. |
| [**projectCustomPropertiesGetProjectCustomProperty**](SettingsReadApi.md#projectCustomPropertiesGetProjectCustomProperty) | **GET** /v1/projects/customproperties/{guid} | Get project custom property by ID. |
| [**projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItem**](SettingsReadApi.md#projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItem) | **GET** /v1/projects/customproperties/projectcustompropertyselectionitems/{guid} | Get project custom property selection item by ID. |
| [**projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItems**](SettingsReadApi.md#projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItems) | **GET** /v1/projects/customproperties/{customPropertyGuid}/projectcustompropertyselectionitems | Get the project custom properties. |
| [**projectMemberCostExceptionsGetProjectMemberCostException**](SettingsReadApi.md#projectMemberCostExceptionsGetProjectMemberCostException) | **GET** /v1/projectmembercostexceptions/{guid} | Get project member cost exception by ID. |
| [**projectStatusTypesGetProjectStatusType**](SettingsReadApi.md#projectStatusTypesGetProjectStatusType) | **GET** /v1/projectstatustypes/{guid} | Get projectStatusType by ID |
| [**projectStatusTypesGetProjectStatusTypes**](SettingsReadApi.md#projectStatusTypesGetProjectStatusTypes) | **GET** /v1/projectstatustypes | Get all the ProjectStatusTypes |
| [**projectTaskStatusesGetProjectTaskStatus**](SettingsReadApi.md#projectTaskStatusesGetProjectTaskStatus) | **GET** /v1/projecttaskstatuses/{guid} | Get Project task status by ID. |
| [**projectTaskStatusesGetProjectTaskStatuses**](SettingsReadApi.md#projectTaskStatusesGetProjectTaskStatuses) | **GET** /v1/projecttaskstatuses | Get the project task statuses. |
| [**proposalStatusesGetProposalStatus**](SettingsReadApi.md#proposalStatusesGetProposalStatus) | **GET** /v1/proposalstatuses/{guid} | Get Proposal status by ID |
| [**proposalStatusesGetProposalStatuses**](SettingsReadApi.md#proposalStatusesGetProposalStatuses) | **GET** /v1/proposalstatuses | Get all the proposal statuses |
| [**proposalStatusesGetUsage**](SettingsReadApi.md#proposalStatusesGetUsage) | **GET** /v1/proposalstatuses/{guid}/usage | Get usage for an proposal status. |
| [**rolesGetRole**](SettingsReadApi.md#rolesGetRole) | **GET** /v1/roles/{guid} | Get role by GUID. |
| [**rolesGetRoles**](SettingsReadApi.md#rolesGetRoles) | **GET** /v1/roles | Get roles. |
| [**salesAccountsGetSalesAccount**](SettingsReadApi.md#salesAccountsGetSalesAccount) | **GET** /v1/salesaccounts/{guid} | Get sales account by ID. |
| [**salesAccountsGetSalesAccounts**](SettingsReadApi.md#salesAccountsGetSalesAccounts) | **GET** /v1/salesaccounts | Get sales accounts. |
| [**salesStatusTypesGetSalesStatusType**](SettingsReadApi.md#salesStatusTypesGetSalesStatusType) | **GET** /v1/salesstatustypes/{guid} | Get sales status type by ID |
| [**salesStatusTypesGetSalesStatusTypes**](SettingsReadApi.md#salesStatusTypesGetSalesStatusTypes) | **GET** /v1/salesstatustypes | Get all the sales status types |
| [**timeEntryTypesGetTimeEntryType**](SettingsReadApi.md#timeEntryTypesGetTimeEntryType) | **GET** /v1/timeentrytypes/{guid} | Get time entry type by ID. |
| [**timeEntryTypesGetTimeEntryTypes**](SettingsReadApi.md#timeEntryTypesGetTimeEntryTypes) | **GET** /v1/timeentrytypes | Get all time entry types. |
| [**timezonesGetTimezone**](SettingsReadApi.md#timezonesGetTimezone) | **GET** /v1/localization/timezones/{guid} | Get timezone by ID. |
| [**timezonesGetTimezones**](SettingsReadApi.md#timezonesGetTimezones) | **GET** /v1/localization/timezones | Get all the timezones. |
| [**travelExpenseTypeCountrySettingsGetTravelExpenseTypeCountrySettings**](SettingsReadApi.md#travelExpenseTypeCountrySettingsGetTravelExpenseTypeCountrySettings) | **GET** /v1/travelexpensetypes/{travelExpenseTypeGuid}/travelexpensetypecountrysettings | Get all country settings for a travel expense type |
| [**travelExpenseTypesGetTravelExpenseType**](SettingsReadApi.md#travelExpenseTypesGetTravelExpenseType) | **GET** /v1/travelexpensetypes/{guid} | Get travel expense type by guid. |
| [**travelExpenseTypesGetTravelExpenseTypes**](SettingsReadApi.md#travelExpenseTypesGetTravelExpenseTypes) | **GET** /v1/travelexpensetypes | Get all the travel expense types. |
| [**travelPricesGetTravelPrice**](SettingsReadApi.md#travelPricesGetTravelPrice) | **GET** /v1/travelprices/{guid} | Get travel price by ID. |
| [**travelPricesGetTravelPrices**](SettingsReadApi.md#travelPricesGetTravelPrices) | **GET** /v1/pricelistversions/{pricelistVersionGuid}/travelprices | Get all the travel prices for a price list version. |
| [**travelReimbursementStatusGetTravelReimbursementStatus**](SettingsReadApi.md#travelReimbursementStatusGetTravelReimbursementStatus) | **GET** /v1/travelreimbursementstatuses/{guid} | Get the travel reimbursement statuses by guid. |
| [**travelReimbursementStatusGetTravelReimbursementStatuses**](SettingsReadApi.md#travelReimbursementStatusGetTravelReimbursementStatuses) | **GET** /v1/travelreimbursementstatuses | Get the travel reimbursement statuses. |
| [**userCustomPropertiesGetUserCustomProperties**](SettingsReadApi.md#userCustomPropertiesGetUserCustomProperties) | **GET** /v1/users/customproperties | Get the user custom properties. |
| [**userCustomPropertiesGetUserCustomProperty**](SettingsReadApi.md#userCustomPropertiesGetUserCustomProperty) | **GET** /v1/users/customproperties/{guid} | Get user custom property by ID. |
| [**userCustomPropertySelectionItemsGetUserCustomPropertySelectionItem**](SettingsReadApi.md#userCustomPropertySelectionItemsGetUserCustomPropertySelectionItem) | **GET** /v1/users/customproperties/usercustompropertyselectionitems/{guid} | Get user custom property selection item by ID. |
| [**userCustomPropertySelectionItemsGetUserCustomPropertySelectionItems**](SettingsReadApi.md#userCustomPropertySelectionItemsGetUserCustomPropertySelectionItems) | **GET** /v1/users/customproperties/{customPropertyGuid}/usercustompropertyselectionitems | Get the user custom properties. |
| [**vatRatesGetVatRate**](SettingsReadApi.md#vatRatesGetVatRate) | **GET** /v1/vatrates/{guid} | Get a vat rate by GUID |
| [**vatRatesGetVatRates**](SettingsReadApi.md#vatRatesGetVatRates) | **GET** /v1/vatrates | Get all organization vat rates |
| [**workContractsGetWorkContract**](SettingsReadApi.md#workContractsGetWorkContract) | **GET** /v1/workcontracts/{guid} | Get work contract by ID. |
| [**workHourPricesGetWorkHourPrice**](SettingsReadApi.md#workHourPricesGetWorkHourPrice) | **GET** /v1/workhourprices/{guid} | Get work hour price by ID. |
| [**workHourPricesGetWorkHourPrices**](SettingsReadApi.md#workHourPricesGetWorkHourPrices) | **GET** /v1/pricelistversions/{pricelistVersionGuid}/workhourprices | Get all the workHourPrices for a price list version. |
| [**workTypesGetWorkType**](SettingsReadApi.md#workTypesGetWorkType) | **GET** /v1/worktypes/{guid} | Get work type by ID. |
| [**workTypesGetWorkTypes**](SettingsReadApi.md#workTypesGetWorkTypes) | **GET** /v1/worktypes | Get all work types. |


<a id="activityTypesGetActivityType"></a>
# **activityTypesGetActivityType**
> ActivityTypeModel activityTypesGetActivityType(guid)

Get Activity Type by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the Activity Type.
    try {
      ActivityTypeModel result = apiInstance.activityTypesGetActivityType(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#activityTypesGetActivityType");
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
| **guid** | **String**| GUID used to get the Activity Type. | |

### Return type

[**ActivityTypeModel**](ActivityTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Activity Type |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="activityTypesGetActivityTypes"></a>
# **activityTypesGetActivityTypes**
> List&lt;ActivityTypeModel&gt; activityTypesGetActivityTypes(active, pageToken, rowCount, changedSince, category)

Get the Activity Types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | If not given, return all Activity Types, if given as true return only active Activity Types, if given as false returns only inactive Activity Types
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get activity types that have been added or changed after this date time (greater or equal).
    List<ActivityCategory> category = Arrays.asList(); // List<ActivityCategory> | Optional: Category or multiple categories of activity types to search for. Default all.
    try {
      List<ActivityTypeModel> result = apiInstance.activityTypesGetActivityTypes(active, pageToken, rowCount, changedSince, category);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#activityTypesGetActivityTypes");
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
| **active** | **Boolean**| If not given, return all Activity Types, if given as true return only active Activity Types, if given as false returns only inactive Activity Types | [optional] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get activity types that have been added or changed after this date time (greater or equal). | [optional] |
| **category** | [**List&lt;ActivityCategory&gt;**](ActivityCategory.md)| Optional: Category or multiple categories of activity types to search for. Default all. | [optional] |

### Return type

[**List&lt;ActivityTypeModel&gt;**](ActivityTypeModel.md)

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

<a id="bankAccountsGetBankAccount"></a>
# **bankAccountsGetBankAccount**
> BankAccountOutputModel bankAccountsGetBankAccount(guid)

Get bank account by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the bank account.
    try {
      BankAccountOutputModel result = apiInstance.bankAccountsGetBankAccount(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#bankAccountsGetBankAccount");
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
| **guid** | **String**| GUID used to get the bank account. | |

### Return type

[**BankAccountOutputModel**](BankAccountOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bank account. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="bankAccountsGetBankAccounts"></a>
# **bankAccountsGetBankAccounts**
> List&lt;BankAccountOutputModel&gt; bankAccountsGetBankAccounts(companyGuid, businessUnitGuid, active, firstRow, rowCount, textToSearch, calculateRowCount, sortings)

Get all bank accounts for current organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String companyGuid = "companyGuid_example"; // String | Optional: ID of the company.
    String businessUnitGuid = "businessUnitGuid_example"; // String | Optional: ID of the business unit.
    Boolean active = true; // Boolean | If not given, returns all bank accounts, if given as true returns only active bank accounts, if given as false returns only inactive bank accounts.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from bank account name.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=BankName&sortings[0].value=Desc &sortings[1].key=BusinessUnitName&sortings[1].value=Asc\".
    try {
      List<BankAccountOutputModel> result = apiInstance.bankAccountsGetBankAccounts(companyGuid, businessUnitGuid, active, firstRow, rowCount, textToSearch, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#bankAccountsGetBankAccounts");
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
| **companyGuid** | **String**| Optional: ID of the company. | [optional] |
| **businessUnitGuid** | **String**| Optional: ID of the business unit. | [optional] |
| **active** | **Boolean**| If not given, returns all bank accounts, if given as true returns only active bank accounts, if given as false returns only inactive bank accounts. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from bank account name. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;BankName&amp;sortings[0].value&#x3D;Desc &amp;sortings[1].key&#x3D;BusinessUnitName&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] |

### Return type

[**List&lt;BankAccountOutputModel&gt;**](BankAccountOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bank accounts. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="businessUnitsGetBusinessUnit"></a>
# **businessUnitsGetBusinessUnit**
> BusinessUnitModel businessUnitsGetBusinessUnit(guid)

Get businessUnit by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the businessUnit.
    try {
      BusinessUnitModel result = apiInstance.businessUnitsGetBusinessUnit(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#businessUnitsGetBusinessUnit");
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
| **guid** | **String**| GUID used to get the businessUnit. | |

### Return type

[**BusinessUnitModel**](BusinessUnitModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | BusinessUnit. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="businessUnitsGetBusinessUnits"></a>
# **businessUnitsGetBusinessUnits**
> List&lt;BusinessUnitModel&gt; businessUnitsGetBusinessUnits(active, companyGuid, companyCountryGuid, firstRow, rowCount, textToSearch, changedSince, code, name)

Get all the BusinessUnits

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | If not given, return all BusinessUnits, if given as true return only active BusinessUnits, if given as false returns only inactive BusinessUnits
    String companyGuid = "companyGuid_example"; // String | Optional: ID of the company to which the business units belong.
    String companyCountryGuid = "companyCountryGuid_example"; // String | Optional: ID of the country in which the company of business units is located.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from business unit name.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get business units that have been added or changed after this date time (greater or equal).
    String code = ""; // String | Optional: Code of the business unit.
    String name = ""; // String | Optional: Name of the business unit.
    try {
      List<BusinessUnitModel> result = apiInstance.businessUnitsGetBusinessUnits(active, companyGuid, companyCountryGuid, firstRow, rowCount, textToSearch, changedSince, code, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#businessUnitsGetBusinessUnits");
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
| **active** | **Boolean**| If not given, return all BusinessUnits, if given as true return only active BusinessUnits, if given as false returns only inactive BusinessUnits | [optional] |
| **companyGuid** | **String**| Optional: ID of the company to which the business units belong. | [optional] |
| **companyCountryGuid** | **String**| Optional: ID of the country in which the company of business units is located. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from business unit name. | [optional] [default to ] |
| **changedSince** | **OffsetDateTime**| Optional: Get business units that have been added or changed after this date time (greater or equal). | [optional] |
| **code** | **String**| Optional: Code of the business unit. | [optional] [default to ] |
| **name** | **String**| Optional: Name of the business unit. | [optional] [default to ] |

### Return type

[**List&lt;BusinessUnitModel&gt;**](BusinessUnitModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the BusinessUnits |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="communicationTypesGetCommunicationType"></a>
# **communicationTypesGetCommunicationType**
> CommunicationTypeModel communicationTypesGetCommunicationType(guid)

Get communication type by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | ID used to get the communication type.
    try {
      CommunicationTypeModel result = apiInstance.communicationTypesGetCommunicationType(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#communicationTypesGetCommunicationType");
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
| **guid** | **String**| ID used to get the communication type. | |

### Return type

[**CommunicationTypeModel**](CommunicationTypeModel.md)

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

<a id="communicationTypesGetCommunicationTypes"></a>
# **communicationTypesGetCommunicationTypes**
> List&lt;CommunicationTypeModel&gt; communicationTypesGetCommunicationTypes(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings)

Get all communication types.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | Filter the communication types. If true/false, only the active/inactive ones are returned. If null, all the communication types are returned.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from communication type name.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=name&sortings[0].value=Asc\".
    try {
      List<CommunicationTypeModel> result = apiInstance.communicationTypesGetCommunicationTypes(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#communicationTypesGetCommunicationTypes");
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
| **active** | **Boolean**| Filter the communication types. If true/false, only the active/inactive ones are returned. If null, all the communication types are returned. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from communication type name. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc\&quot;. | [optional] |

### Return type

[**List&lt;CommunicationTypeModel&gt;**](CommunicationTypeModel.md)

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

<a id="contactRolesGetContactRole"></a>
# **contactRolesGetContactRole**
> ContactRoleModel contactRolesGetContactRole(guid)

Get contact role by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the contact role.
    try {
      ContactRoleModel result = apiInstance.contactRolesGetContactRole(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#contactRolesGetContactRole");
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
| **guid** | **String**| Id used to get the contact role. | |

### Return type

[**ContactRoleModel**](ContactRoleModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ContactRoleModel. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="contactRolesGetContactRoles"></a>
# **contactRolesGetContactRoles**
> List&lt;ContactRoleModel&gt; contactRolesGetContactRoles(active, firstRow, rowCount, textToSearch, calculateRowCount)

Get contact roles.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | If not given, return all contact roles, if given as true return only active contact roles, if given as false returns only inactive contact roles.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from contact role name.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    try {
      List<ContactRoleModel> result = apiInstance.contactRolesGetContactRoles(active, firstRow, rowCount, textToSearch, calculateRowCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#contactRolesGetContactRoles");
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
| **active** | **Boolean**| If not given, return all contact roles, if given as true return only active contact roles, if given as false returns only inactive contact roles. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from contact role name. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |

### Return type

[**List&lt;ContactRoleModel&gt;**](ContactRoleModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the contact roles. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="costAccountsGetCostAccount"></a>
# **costAccountsGetCostAccount**
> CostAccountModel costAccountsGetCostAccount(guid)

Get cost account by Guid.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | Cost account's guid.
    try {
      CostAccountModel result = apiInstance.costAccountsGetCostAccount(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#costAccountsGetCostAccount");
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
| **guid** | **String**| Cost account&#39;s guid. | |

### Return type

[**CostAccountModel**](CostAccountModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CostAccountModel. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="costAccountsGetCostAccounts"></a>
# **costAccountsGetCostAccounts**
> List&lt;CostAccountModel&gt; costAccountsGetCostAccounts(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings)

Get cost accounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | If not given, return all cost accounts, if given as true return only active cost accounts, if given as false returns only inactive cost accounts.
    Integer firstRow = 56; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from cost account name or identifier.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc &sortings[1].key=Identifier&sortings[1].value=Asc\".
    try {
      List<CostAccountModel> result = apiInstance.costAccountsGetCostAccounts(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#costAccountsGetCostAccounts");
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
| **active** | **Boolean**| If not given, return all cost accounts, if given as true return only active cost accounts, if given as false returns only inactive cost accounts. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from cost account name or identifier. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc &amp;sortings[1].key&#x3D;Identifier&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] |

### Return type

[**List&lt;CostAccountModel&gt;**](CostAccountModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the cost accounts. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="costCentersGetCostCenter"></a>
# **costCentersGetCostCenter**
> CostCenterModel costCentersGetCostCenter(guid)

Get cost center by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the cost center.
    try {
      CostCenterModel result = apiInstance.costCentersGetCostCenter(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#costCentersGetCostCenter");
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
| **guid** | **String**| Id used to get the cost center. | |

### Return type

[**CostCenterModel**](CostCenterModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CostCenterModel. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="costCentersGetCostCenters"></a>
# **costCentersGetCostCenters**
> List&lt;CostCenterModel&gt; costCentersGetCostCenters(active, firstRow, rowCount, textToSearch, changedSince, calculateRowCount, sortings, identifier, name)

Get cost centers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | If not given, return all cost centers, if given as true return only active cost centers, if given as false returns only inactive cost centers.
    Integer firstRow = 56; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from cost center name or identifier.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get cost centers that have been added or changed after this date time (greater or equal).
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\".
    String identifier = ""; // String | Optional: Identifier of the cost center.
    String name = ""; // String | Optional: Name of the cost center.
    try {
      List<CostCenterModel> result = apiInstance.costCentersGetCostCenters(active, firstRow, rowCount, textToSearch, changedSince, calculateRowCount, sortings, identifier, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#costCentersGetCostCenters");
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
| **active** | **Boolean**| If not given, return all cost centers, if given as true return only active cost centers, if given as false returns only inactive cost centers. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from cost center name or identifier. | [optional] [default to ] |
| **changedSince** | **OffsetDateTime**| Optional: Get cost centers that have been added or changed after this date time (greater or equal). | [optional] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. | [optional] |
| **identifier** | **String**| Optional: Identifier of the cost center. | [optional] [default to ] |
| **name** | **String**| Optional: Name of the cost center. | [optional] [default to ] |

### Return type

[**List&lt;CostCenterModel&gt;**](CostCenterModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the cost centers. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="countriesGetCountries"></a>
# **countriesGetCountries**
> List&lt;CountryModel&gt; countriesGetCountries()

Get all the Countries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    try {
      List<CountryModel> result = apiInstance.countriesGetCountries();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#countriesGetCountries");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;CountryModel&gt;**](CountryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the Countries. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="countriesGetCountry"></a>
# **countriesGetCountry**
> CountryModel countriesGetCountry(guid)

Get country by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the country.
    try {
      CountryModel result = apiInstance.countriesGetCountry(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#countriesGetCountry");
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
| **guid** | **String**| GUID used to get the country. | |

### Return type

[**CountryModel**](CountryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Country. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="countriesGetCountryByCode2"></a>
# **countriesGetCountryByCode2**
> List&lt;CountryModel&gt; countriesGetCountryByCode2(code2)

Get a country by ISO Alpha-2 code

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String code2 = "code2_example"; // String | Optional: ISO Alpha-2 code used to get a country.
    try {
      List<CountryModel> result = apiInstance.countriesGetCountryByCode2(code2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#countriesGetCountryByCode2");
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
| **code2** | **String**| Optional: ISO Alpha-2 code used to get a country. | |

### Return type

[**List&lt;CountryModel&gt;**](CountryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Country |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="countriesGetCountryByCode3"></a>
# **countriesGetCountryByCode3**
> List&lt;CountryModel&gt; countriesGetCountryByCode3(code3)

Get a country by ISO Alpha-3 code

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String code3 = "code3_example"; // String | Optional: ISO Alpha-3 code used to get a country.
    try {
      List<CountryModel> result = apiInstance.countriesGetCountryByCode3(code3);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#countriesGetCountryByCode3");
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
| **code3** | **String**| Optional: ISO Alpha-3 code used to get a country. | |

### Return type

[**List&lt;CountryModel&gt;**](CountryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Country |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="countriesGetCountryByName"></a>
# **countriesGetCountryByName**
> List&lt;CountryModel&gt; countriesGetCountryByName(countryName)

Get a country by name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String countryName = "countryName_example"; // String | Optional: English country name.
    try {
      List<CountryModel> result = apiInstance.countriesGetCountryByName(countryName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#countriesGetCountryByName");
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
| **countryName** | **String**| Optional: English country name. | |

### Return type

[**List&lt;CountryModel&gt;**](CountryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Country |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="countriesGetCountryRegion"></a>
# **countriesGetCountryRegion**
> CountryRegionModel countriesGetCountryRegion(guid)

Get country region by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the country region.
    try {
      CountryRegionModel result = apiInstance.countriesGetCountryRegion(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#countriesGetCountryRegion");
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
| **guid** | **String**| GUID used to get the country region. | |

### Return type

[**CountryRegionModel**](CountryRegionModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CountryRegion. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="countriesGetCountryRegions"></a>
# **countriesGetCountryRegions**
> List&lt;CountryRegionModel&gt; countriesGetCountryRegions(countryGuid)

Get all the Country regions for a country.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String countryGuid = "countryGuid_example"; // String | GUID of the country.
    try {
      List<CountryRegionModel> result = apiInstance.countriesGetCountryRegions(countryGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#countriesGetCountryRegions");
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
| **countryGuid** | **String**| GUID of the country. | |

### Return type

[**List&lt;CountryRegionModel&gt;**](CountryRegionModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the CountryRegions of the country. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="currenciesGetCurrencies"></a>
# **currenciesGetCurrencies**
> List&lt;CurrencyOutputModel&gt; currenciesGetCurrencies(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings)

Get all the Currencies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | If not given, return all Currencies, if given as true return only active Currencies, if given as false returns only inactive Currencies.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text based search applied to the result. Matches currency name and code.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=name&sortings[0].value=Asc\". Using additional sorting fields \"CreatedDate\" and / or \"LastUpdatedDate\" as keys sort currencies without a timestamp provided when sorting with other date fields.
    try {
      List<CurrencyOutputModel> result = apiInstance.currenciesGetCurrencies(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#currenciesGetCurrencies");
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
| **active** | **Boolean**| If not given, return all Currencies, if given as true return only active Currencies, if given as false returns only inactive Currencies. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text based search applied to the result. Matches currency name and code. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc\&quot;. Using additional sorting fields \&quot;CreatedDate\&quot; and / or \&quot;LastUpdatedDate\&quot; as keys sort currencies without a timestamp provided when sorting with other date fields. | [optional] |

### Return type

[**List&lt;CurrencyOutputModel&gt;**](CurrencyOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the Currencies |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="currenciesGetCurrency"></a>
# **currenciesGetCurrency**
> CurrencyOutputModel currenciesGetCurrency(guid)

Get currency by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the currency.
    try {
      CurrencyOutputModel result = apiInstance.currenciesGetCurrency(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#currenciesGetCurrency");
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
| **guid** | **String**| GUID used to get the currency. | |

### Return type

[**CurrencyOutputModel**](CurrencyOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CurrencyModel. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="customerCustomPropertiesGetCustomerCustomProperties"></a>
# **customerCustomPropertiesGetCustomerCustomProperties**
> List&lt;CustomPropertyModel&gt; customerCustomPropertiesGetCustomerCustomProperties(firstRow, rowCount, active, textToSearch, isInUse, calculateRowCount, sortings)

Get the customer custom properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    Boolean active = true; // Boolean | Optional: Get only active or inactive customer properties.
    String textToSearch = ""; // String | Optional: Text to search from custom property name.
    Boolean isInUse = true; // Boolean | Optional: Is the customer property used in any custom property usage.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc&sortings[1].key=Number&sortings[1].value=Asc\".
    try {
      List<CustomPropertyModel> result = apiInstance.customerCustomPropertiesGetCustomerCustomProperties(firstRow, rowCount, active, textToSearch, isInUse, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#customerCustomPropertiesGetCustomerCustomProperties");
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
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **active** | **Boolean**| Optional: Get only active or inactive customer properties. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from custom property name. | [optional] [default to ] |
| **isInUse** | **Boolean**| Optional: Is the customer property used in any custom property usage. | [optional] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc&amp;sortings[1].key&#x3D;Number&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] |

### Return type

[**List&lt;CustomPropertyModel&gt;**](CustomPropertyModel.md)

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

<a id="customerCustomPropertiesGetCustomerCustomProperty"></a>
# **customerCustomPropertiesGetCustomerCustomProperty**
> CustomPropertyModel customerCustomPropertiesGetCustomerCustomProperty(guid)

Get customer custom property by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the customer custom property.
    try {
      CustomPropertyModel result = apiInstance.customerCustomPropertiesGetCustomerCustomProperty(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#customerCustomPropertiesGetCustomerCustomProperty");
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
| **guid** | **String**| Id used to get the customer custom property. | |

### Return type

[**CustomPropertyModel**](CustomPropertyModel.md)

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

<a id="customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItem"></a>
# **customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItem**
> CustomerCustomPropertySelectionItemOutputModel customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItem(guid)

Get customer custom property selection item by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the customer custom property selection item.
    try {
      CustomerCustomPropertySelectionItemOutputModel result = apiInstance.customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItem(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItem");
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
| **guid** | **String**| Id used to get the customer custom property selection item. | |

### Return type

[**CustomerCustomPropertySelectionItemOutputModel**](CustomerCustomPropertySelectionItemOutputModel.md)

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

<a id="customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItems"></a>
# **customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItems**
> List&lt;CustomerCustomPropertySelectionItemOutputModel&gt; customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItems(customPropertyGuid, rowCount, isActive, pageToken, changedSince)

Get the customer custom properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String customPropertyGuid = "customPropertyGuid_example"; // String | Custom property id used to get the customer custom property selection items.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    Boolean isActive = true; // Boolean | Optional: Get only active or inactive selection items.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get custom property selection items that have been added or changed after this date time (greater or equal).
    try {
      List<CustomerCustomPropertySelectionItemOutputModel> result = apiInstance.customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItems(customPropertyGuid, rowCount, isActive, pageToken, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItems");
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
| **customPropertyGuid** | **String**| Custom property id used to get the customer custom property selection items. | |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **isActive** | **Boolean**| Optional: Get only active or inactive selection items. | [optional] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get custom property selection items that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;CustomerCustomPropertySelectionItemOutputModel&gt;**](CustomerCustomPropertySelectionItemOutputModel.md)

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

<a id="formattingCulturesGetFormattingCulture"></a>
# **formattingCulturesGetFormattingCulture**
> FormattingCultureModel formattingCulturesGetFormattingCulture(guid)

Get formatting culture by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the formatting culture.
    try {
      FormattingCultureModel result = apiInstance.formattingCulturesGetFormattingCulture(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#formattingCulturesGetFormattingCulture");
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
| **guid** | **String**| GUID used to get the formatting culture. | |

### Return type

[**FormattingCultureModel**](FormattingCultureModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Formatting culture. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="formattingCulturesGetFormattings"></a>
# **formattingCulturesGetFormattings**
> List&lt;FormattingCultureModel&gt; formattingCulturesGetFormattings()

Get all the Formatting Cultures

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    try {
      List<FormattingCultureModel> result = apiInstance.formattingCulturesGetFormattings();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#formattingCulturesGetFormattings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;FormattingCultureModel&gt;**](FormattingCultureModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the Formatting Cultures |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="holidaysGetHolidays"></a>
# **holidaysGetHolidays**
> List&lt;HolidayModel&gt; holidaysGetHolidays(year, countryGuid)

Get holidays.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Integer year = 56; // Integer | Optional: Holidays for this year only. Default: all years.
    String countryGuid = "countryGuid_example"; // String | Optional: Holidays for this country only. Default local.
    try {
      List<HolidayModel> result = apiInstance.holidaysGetHolidays(year, countryGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#holidaysGetHolidays");
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
| **year** | **Integer**| Optional: Holidays for this year only. Default: all years. | [optional] |
| **countryGuid** | **String**| Optional: Holidays for this country only. Default local. | [optional] |

### Return type

[**List&lt;HolidayModel&gt;**](HolidayModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of holidays.  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="holidaysGetHolidaysByTimePeriod"></a>
# **holidaysGetHolidaysByTimePeriod**
> List&lt;HolidayModel&gt; holidaysGetHolidaysByTimePeriod(startDate, endDate, countryGuid)

Get holidays with start and end date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Start date for holidays.
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | End date for holidays.
    String countryGuid = "countryGuid_example"; // String | Optional: Holidays for this country only. Default local.
    try {
      List<HolidayModel> result = apiInstance.holidaysGetHolidaysByTimePeriod(startDate, endDate, countryGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#holidaysGetHolidaysByTimePeriod");
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
| **startDate** | **OffsetDateTime**| Start date for holidays. | [optional] |
| **endDate** | **OffsetDateTime**| End date for holidays. | [optional] |
| **countryGuid** | **String**| Optional: Holidays for this country only. Default local. | [optional] |

### Return type

[**List&lt;HolidayModel&gt;**](HolidayModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of holidays.  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="industriesGetIndustries"></a>
# **industriesGetIndustries**
> List&lt;IndustryModel&gt; industriesGetIndustries(active, firstRow, rowCount, textToSearch, calculateRowCount)

Get all the industries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | If not given, return all industries, if given as true return only active industries, if given as false returns only inactive industries.
    Integer firstRow = 56; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from industry name.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    try {
      List<IndustryModel> result = apiInstance.industriesGetIndustries(active, firstRow, rowCount, textToSearch, calculateRowCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#industriesGetIndustries");
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
| **active** | **Boolean**| If not given, return all industries, if given as true return only active industries, if given as false returns only inactive industries. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from industry name. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |

### Return type

[**List&lt;IndustryModel&gt;**](IndustryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the industries. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="industriesGetIndustry"></a>
# **industriesGetIndustry**
> IndustryModel industriesGetIndustry(guid)

Get industry by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the industry.
    try {
      IndustryModel result = apiInstance.industriesGetIndustry(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#industriesGetIndustry");
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
| **guid** | **String**| GUID used to get the industry. | |

### Return type

[**IndustryModel**](IndustryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Industry. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="invoiceStatusesGetInvoiceStatus"></a>
# **invoiceStatusesGetInvoiceStatus**
> InvoiceStatusModel invoiceStatusesGetInvoiceStatus(guid)

Get Invoice status by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the Invoice status.
    try {
      InvoiceStatusModel result = apiInstance.invoiceStatusesGetInvoiceStatus(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#invoiceStatusesGetInvoiceStatus");
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
| **guid** | **String**| GUID used to get the Invoice status. | |

### Return type

[**InvoiceStatusModel**](InvoiceStatusModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invoice status. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="invoiceStatusesGetInvoiceStatuses"></a>
# **invoiceStatusesGetInvoiceStatuses**
> List&lt;InvoiceStatusModel&gt; invoiceStatusesGetInvoiceStatuses(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings)

Get invoice statuses.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | Filter the invoice statuses. If true/false, only the active/inactive ones are returned. If null, all the invoice statuses are returned.
    Integer firstRow = 56; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from invoice status name.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc\".
    try {
      List<InvoiceStatusModel> result = apiInstance.invoiceStatusesGetInvoiceStatuses(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#invoiceStatusesGetInvoiceStatuses");
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
| **active** | **Boolean**| Filter the invoice statuses. If true/false, only the active/inactive ones are returned. If null, all the invoice statuses are returned. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from invoice status name. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc\&quot;. | [optional] |

### Return type

[**List&lt;InvoiceStatusModel&gt;**](InvoiceStatusModel.md)

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

<a id="invoiceTemplatesGetInvoiceTemplate"></a>
# **invoiceTemplatesGetInvoiceTemplate**
> InvoiceTemplateModel invoiceTemplatesGetInvoiceTemplate(guid)

Get invoice template by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | ID of the invoice template.
    try {
      InvoiceTemplateModel result = apiInstance.invoiceTemplatesGetInvoiceTemplate(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#invoiceTemplatesGetInvoiceTemplate");
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
| **guid** | **String**| ID of the invoice template. | |

### Return type

[**InvoiceTemplateModel**](InvoiceTemplateModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | InvoiceTemplatesModel. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="invoiceTemplatesGetInvoiceTemplates"></a>
# **invoiceTemplatesGetInvoiceTemplates**
> List&lt;InvoiceTemplateModel&gt; invoiceTemplatesGetInvoiceTemplates(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings)

Get invoice templates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | 
    Integer firstRow = 56; // Integer | 
    Integer rowCount = 56; // Integer | 
    String textToSearch = ""; // String | 
    Boolean calculateRowCount = false; // Boolean | 
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | 
    try {
      List<InvoiceTemplateModel> result = apiInstance.invoiceTemplatesGetInvoiceTemplates(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#invoiceTemplatesGetInvoiceTemplates");
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
| **active** | **Boolean**|  | [optional] |
| **firstRow** | **Integer**|  | [optional] |
| **rowCount** | **Integer**|  | [optional] |
| **textToSearch** | **String**|  | [optional] [default to ] |
| **calculateRowCount** | **Boolean**|  | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)|  | [optional] |

### Return type

[**List&lt;InvoiceTemplateModel&gt;**](InvoiceTemplateModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | InvoiceTemplatesModel. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="keywordsGetKeyword"></a>
# **keywordsGetKeyword**
> KeywordModel keywordsGetKeyword(guid)

Get keyword by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the keyword.
    try {
      KeywordModel result = apiInstance.keywordsGetKeyword(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#keywordsGetKeyword");
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

### Return type

[**KeywordModel**](KeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Keyword. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="keywordsGetKeywords"></a>
# **keywordsGetKeywords**
> List&lt;KeywordModel&gt; keywordsGetKeywords(category, active, firstRow, rowCount, textToSearch, changedSince, calculateRowCount, sortings, keyword)

Get all the keywords.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    KeywordCategory category = KeywordCategory.fromValue("Project"); // KeywordCategory | Optional: category of the keyword.
    Boolean active = true; // Boolean | If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from keyword.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get keywords that have been added or changed after this date time (greater or equal).
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\".
    String keyword = ""; // String | Optional: Keyword name.
    try {
      List<KeywordModel> result = apiInstance.keywordsGetKeywords(category, active, firstRow, rowCount, textToSearch, changedSince, calculateRowCount, sortings, keyword);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#keywordsGetKeywords");
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
| **category** | [**KeywordCategory**](.md)| Optional: category of the keyword. | [optional] [enum: Project, Contact, User, File] |
| **active** | **Boolean**| If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from keyword. | [optional] [default to ] |
| **changedSince** | **OffsetDateTime**| Optional: Get keywords that have been added or changed after this date time (greater or equal). | [optional] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. | [optional] |
| **keyword** | **String**| Optional: Keyword name. | [optional] [default to ] |

### Return type

[**List&lt;KeywordModel&gt;**](KeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the Keywords. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="kpiFormulasGetKpiFormulas"></a>
# **kpiFormulasGetKpiFormulas**
> List&lt;KpiFormulaModelBase&gt; kpiFormulasGetKpiFormulas(category, isActive, firstRow, rowCount, textToSearch, sortings, includeDefinition, changedSince)

Get saved KPI formulas.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    KpiFormulaCategory category = KpiFormulaCategory.fromValue("Unknown"); // KpiFormulaCategory | Optional: Category of KPI formula (Project, Invoice, User).
    Boolean isActive = true; // Boolean | Optional: return with given active status. Default is to return all.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc\".
    Boolean includeDefinition = false; // Boolean | Optional: Include definition to response. Default false.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get KPI formulas that have been added or changed after this date time (greater or equal).
    try {
      List<KpiFormulaModelBase> result = apiInstance.kpiFormulasGetKpiFormulas(category, isActive, firstRow, rowCount, textToSearch, sortings, includeDefinition, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#kpiFormulasGetKpiFormulas");
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
| **category** | [**KpiFormulaCategory**](.md)| Optional: Category of KPI formula (Project, Invoice, User). | [optional] [enum: Unknown, Functions, Project, User, Invoice] |
| **isActive** | **Boolean**| Optional: return with given active status. Default is to return all. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search. | [optional] [default to ] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc\&quot;. | [optional] |
| **includeDefinition** | **Boolean**| Optional: Include definition to response. Default false. | [optional] [default to false] |
| **changedSince** | **OffsetDateTime**| Optional: Get KPI formulas that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;KpiFormulaModelBase&gt;**](KpiFormulaModelBase.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | KPI formulas. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="languagesGetLanguage"></a>
# **languagesGetLanguage**
> LanguageModel languagesGetLanguage(guid)

Get language by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the language.
    try {
      LanguageModel result = apiInstance.languagesGetLanguage(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#languagesGetLanguage");
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
| **guid** | **String**| GUID used to get the language. | |

### Return type

[**LanguageModel**](LanguageModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Language |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="languagesGetLanguages"></a>
# **languagesGetLanguages**
> List&lt;LanguageModel&gt; languagesGetLanguages(isInvoiceLanguage)

Get all the languages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean isInvoiceLanguage = true; // Boolean | Optional: which languages to fetch. only invoice languages or non invoice languages?, default all.
    try {
      List<LanguageModel> result = apiInstance.languagesGetLanguages(isInvoiceLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#languagesGetLanguages");
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
| **isInvoiceLanguage** | **Boolean**| Optional: which languages to fetch. only invoice languages or non invoice languages?, default all. | [optional] |

### Return type

[**List&lt;LanguageModel&gt;**](LanguageModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the Languages |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="leadSourcesGetLeadSource"></a>
# **leadSourcesGetLeadSource**
> LeadSourceModel leadSourcesGetLeadSource(guid)

Get lead source by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the lead source.
    try {
      LeadSourceModel result = apiInstance.leadSourcesGetLeadSource(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#leadSourcesGetLeadSource");
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
| **guid** | **String**| GUID used to get the lead source. | |

### Return type

[**LeadSourceModel**](LeadSourceModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | lead source. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="leadSourcesGetLeadSources"></a>
# **leadSourcesGetLeadSources**
> List&lt;LeadSourceModel&gt; leadSourcesGetLeadSources(active, firstRow, rowCount, textToSearch, calculateRowCount)

Get the lead sources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | If not given, return all lead sources, if given as true return only active lead sources, if given as false returns only inactive lead sources.
    Integer firstRow = 56; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from lead source name.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    try {
      List<LeadSourceModel> result = apiInstance.leadSourcesGetLeadSources(active, firstRow, rowCount, textToSearch, calculateRowCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#leadSourcesGetLeadSources");
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
| **active** | **Boolean**| If not given, return all lead sources, if given as true return only active lead sources, if given as false returns only inactive lead sources. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from lead source name. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |

### Return type

[**List&lt;LeadSourceModel&gt;**](LeadSourceModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of lead sources. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="marketSegmentsGetMarketSegment"></a>
# **marketSegmentsGetMarketSegment**
> MarketSegmentModel marketSegmentsGetMarketSegment(guid)

Get Market Segment by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the Market Segment.
    try {
      MarketSegmentModel result = apiInstance.marketSegmentsGetMarketSegment(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#marketSegmentsGetMarketSegment");
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
| **guid** | **String**| GUID used to get the Market Segment. | |

### Return type

[**MarketSegmentModel**](MarketSegmentModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Market Segment. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="marketSegmentsGetMarketSegments"></a>
# **marketSegmentsGetMarketSegments**
> List&lt;MarketSegmentModel&gt; marketSegmentsGetMarketSegments(active, firstRow, rowCount, textToSearch, calculateRowCount, includeChildSegments)

Get the Market Segments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | If not given, return all Market Segments, if given as true return only active Market Segments, if given as false returns only inactive Market Segments.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from market segment name.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    Boolean includeChildSegments = true; // Boolean | Optional: Include also child market segments. If false returns only parent segments. Default true.
    try {
      List<MarketSegmentModel> result = apiInstance.marketSegmentsGetMarketSegments(active, firstRow, rowCount, textToSearch, calculateRowCount, includeChildSegments);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#marketSegmentsGetMarketSegments");
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
| **active** | **Boolean**| If not given, return all Market Segments, if given as true return only active Market Segments, if given as false returns only inactive Market Segments. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from market segment name. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **includeChildSegments** | **Boolean**| Optional: Include also child market segments. If false returns only parent segments. Default true. | [optional] [default to true] |

### Return type

[**List&lt;MarketSegmentModel&gt;**](MarketSegmentModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Market Segments. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="overtimePricesGetOvertimePrice"></a>
# **overtimePricesGetOvertimePrice**
> OvertimePriceModel overtimePricesGetOvertimePrice(guid)

Get overtime price by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the overtime price.
    try {
      OvertimePriceModel result = apiInstance.overtimePricesGetOvertimePrice(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#overtimePricesGetOvertimePrice");
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
| **guid** | **String**| Id used to get the overtime price. | |

### Return type

[**OvertimePriceModel**](OvertimePriceModel.md)

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

<a id="overtimePricesGetOvertimePrices"></a>
# **overtimePricesGetOvertimePrices**
> List&lt;OvertimePriceModel&gt; overtimePricesGetOvertimePrices(pricelistVersionGuid)

Get all the overtime prices for a price list version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String pricelistVersionGuid = "pricelistVersionGuid_example"; // String | 
    try {
      List<OvertimePriceModel> result = apiInstance.overtimePricesGetOvertimePrices(pricelistVersionGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#overtimePricesGetOvertimePrices");
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
| **pricelistVersionGuid** | **String**|  | |

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

<a id="overtimesGetOvertime"></a>
# **overtimesGetOvertime**
> OvertimeModel overtimesGetOvertime(guid)

Get overtime definition by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the overtime definition.
    try {
      OvertimeModel result = apiInstance.overtimesGetOvertime(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#overtimesGetOvertime");
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
| **guid** | **String**| Id used to get the overtime definition. | |

### Return type

[**OvertimeModel**](OvertimeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OvertimeModel. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="overtimesGetOvertimes"></a>
# **overtimesGetOvertimes**
> List&lt;OvertimeModel&gt; overtimesGetOvertimes(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings)

Get overtime definitions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | If not given, return all overtime definitions, if given as true return only active overtime definitions, if given as false returns only inactive overtime definitions.
    Integer firstRow = 56; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default all.
    String textToSearch = ""; // String | Optional: Text to search from overtime name.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=name&sortings[0].value=Asc\"\".
    try {
      List<OvertimeModel> result = apiInstance.overtimesGetOvertimes(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#overtimesGetOvertimes");
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
| **active** | **Boolean**| If not given, return all overtime definitions, if given as true return only active overtime definitions, if given as false returns only inactive overtime definitions. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default all. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from overtime name. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc\&quot;\&quot;. | [optional] |

### Return type

[**List&lt;OvertimeModel&gt;**](OvertimeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Overtime definitions. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="permissionProfilesGetPermissionProfile"></a>
# **permissionProfilesGetPermissionProfile**
> PermissionProfileModel permissionProfilesGetPermissionProfile(guid)

Get Permission Profile by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the Permission Profile.
    try {
      PermissionProfileModel result = apiInstance.permissionProfilesGetPermissionProfile(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#permissionProfilesGetPermissionProfile");
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
| **guid** | **String**| GUID used to get the Permission Profile. | |

### Return type

[**PermissionProfileModel**](PermissionProfileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | PermissionProfileModel. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="permissionProfilesGetPermissionProfiles"></a>
# **permissionProfilesGetPermissionProfiles**
> List&lt;PermissionProfileModel&gt; permissionProfilesGetPermissionProfiles(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings)

Get the Permission Profiles.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | If not given, return all Permission Profiles, if given as true return only active Permission Profiles, if given as false returns only inactive Permission Profiles.
    Integer firstRow = 56; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from permission profile name.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=name&sortings[0].value=Asc&sortings[1].key=isActive&sortings[1].value=Asc\".
    try {
      List<PermissionProfileModel> result = apiInstance.permissionProfilesGetPermissionProfiles(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#permissionProfilesGetPermissionProfiles");
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
| **active** | **Boolean**| If not given, return all Permission Profiles, if given as true return only active Permission Profiles, if given as false returns only inactive Permission Profiles. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from permission profile name. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc&amp;sortings[1].key&#x3D;isActive&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] |

### Return type

[**List&lt;PermissionProfileModel&gt;**](PermissionProfileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Permission Profiles. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="phaseStatusTypesGetPhaseStatusType"></a>
# **phaseStatusTypesGetPhaseStatusType**
> PhaseStatusTypeModel phaseStatusTypesGetPhaseStatusType(guid)

Get phase status type by GUID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the phase status type.
    try {
      PhaseStatusTypeModel result = apiInstance.phaseStatusTypesGetPhaseStatusType(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#phaseStatusTypesGetPhaseStatusType");
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
| **guid** | **String**| Id used to get the phase status type. | |

### Return type

[**PhaseStatusTypeModel**](PhaseStatusTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | PhaseStatusTypeModel |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="phaseStatusTypesGetPhaseStatusTypes"></a>
# **phaseStatusTypesGetPhaseStatusTypes**
> List&lt;PhaseStatusTypeModel&gt; phaseStatusTypesGetPhaseStatusTypes(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings)

Get phase status types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | If not given, return all phase status types, if given as true return only active phase status types, if given as false returns only inactive phase status types
    Integer firstRow = 56; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default all.
    String textToSearch = ""; // String | 
    Boolean calculateRowCount = false; // Boolean | 
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | 
    try {
      List<PhaseStatusTypeModel> result = apiInstance.phaseStatusTypesGetPhaseStatusTypes(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#phaseStatusTypesGetPhaseStatusTypes");
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
| **active** | **Boolean**| If not given, return all phase status types, if given as true return only active phase status types, if given as false returns only inactive phase status types | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default all. | [optional] |
| **textToSearch** | **String**|  | [optional] [default to ] |
| **calculateRowCount** | **Boolean**|  | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)|  | [optional] |

### Return type

[**List&lt;PhaseStatusTypeModel&gt;**](PhaseStatusTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the phase status types |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="priceListVersionsGetPricelistVersion"></a>
# **priceListVersionsGetPricelistVersion**
> PricelistVersionOutputModel priceListVersionsGetPricelistVersion(guid)

Get a price list version by guid.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | 
    try {
      PricelistVersionOutputModel result = apiInstance.priceListVersionsGetPricelistVersion(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#priceListVersionsGetPricelistVersion");
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
| **guid** | **String**|  | |

### Return type

[**PricelistVersionOutputModel**](PricelistVersionOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Price list version. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="priceListVersionsGetPricelistVersionsByPricelist"></a>
# **priceListVersionsGetPricelistVersionsByPricelist**
> List&lt;PricelistVersionOutputModel&gt; priceListVersionsGetPricelistVersionsByPricelist(pricelistGuid)

Get all price list versions of a price list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String pricelistGuid = "pricelistGuid_example"; // String | 
    try {
      List<PricelistVersionOutputModel> result = apiInstance.priceListVersionsGetPricelistVersionsByPricelist(pricelistGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#priceListVersionsGetPricelistVersionsByPricelist");
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
| **pricelistGuid** | **String**|  | |

### Return type

[**List&lt;PricelistVersionOutputModel&gt;**](PricelistVersionOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Price list versions. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="priceListsGetPriceList"></a>
# **priceListsGetPriceList**
> PriceListModel priceListsGetPriceList(guid)

Get price list by GUID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | ID used to get the price list.
    try {
      PriceListModel result = apiInstance.priceListsGetPriceList(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#priceListsGetPriceList");
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
| **guid** | **String**| ID used to get the price list. | |

### Return type

[**PriceListModel**](PriceListModel.md)

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

<a id="priceListsGetPricelists"></a>
# **priceListsGetPricelists**
> List&lt;PriceListOutputModel&gt; priceListsGetPricelists(active, firstRow, rowCount, textToSearch, currencyGuid, calculateRowCount, sortings, name)

Get all price lists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | If not given, return all price lists, if given as true return only active price lists, if given as false returns only inactive price lists.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from price list name.
    String currencyGuid = "currencyGuid_example"; // String | Optional: ID of the price list currency.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\".
    String name = ""; // String | Optional: Name of the price list.
    try {
      List<PriceListOutputModel> result = apiInstance.priceListsGetPricelists(active, firstRow, rowCount, textToSearch, currencyGuid, calculateRowCount, sortings, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#priceListsGetPricelists");
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
| **active** | **Boolean**| If not given, return all price lists, if given as true return only active price lists, if given as false returns only inactive price lists. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from price list name. | [optional] [default to ] |
| **currencyGuid** | **String**| Optional: ID of the price list currency. | [optional] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. | [optional] |
| **name** | **String**| Optional: Name of the price list. | [optional] [default to ] |

### Return type

[**List&lt;PriceListOutputModel&gt;**](PriceListOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the price lists. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="productCategoriesGetProductCategories"></a>
# **productCategoriesGetProductCategories**
> List&lt;ProductCategoryModel&gt; productCategoriesGetProductCategories(active, firstRow, rowCount, textToSearch, changedSince, calculateRowCount, sortings)

Get product categories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | If not given, return all Product categories, if given as true return only active Product categories, if given as false returns only inactive Product categories.
    Integer firstRow = 56; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default all.
    String textToSearch = ""; // String | Optional: Text to search from product category name or code.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get product categories that have been added or changed after this date time (greater or equal).
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: ?sortings[0].key=Name&sortings[0].value=Desc &sortings[1].key=Code&sortings[1].value=Asc.
    try {
      List<ProductCategoryModel> result = apiInstance.productCategoriesGetProductCategories(active, firstRow, rowCount, textToSearch, changedSince, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#productCategoriesGetProductCategories");
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
| **active** | **Boolean**| If not given, return all Product categories, if given as true return only active Product categories, if given as false returns only inactive Product categories. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default all. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from product category name or code. | [optional] [default to ] |
| **changedSince** | **OffsetDateTime**| Optional: Get product categories that have been added or changed after this date time (greater or equal). | [optional] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: ?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc &amp;sortings[1].key&#x3D;Code&amp;sortings[1].value&#x3D;Asc. | [optional] |

### Return type

[**List&lt;ProductCategoryModel&gt;**](ProductCategoryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product categories. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="productCategoriesGetProductCategory"></a>
# **productCategoriesGetProductCategory**
> ProductCategoryModel productCategoriesGetProductCategory(guid)

Get product category by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the product category.
    try {
      ProductCategoryModel result = apiInstance.productCategoriesGetProductCategory(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#productCategoriesGetProductCategory");
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
| **guid** | **String**| Id used to get the product category. | |

### Return type

[**ProductCategoryModel**](ProductCategoryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProductCategoryModel. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="productCountrySettingsGetProductCountrySettings"></a>
# **productCountrySettingsGetProductCountrySettings**
> List&lt;ProductCountrySettingsModel&gt; productCountrySettingsGetProductCountrySettings(productGuid)

Get all the country settings for a product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String productGuid = "productGuid_example"; // String | GUID of the product.
    try {
      List<ProductCountrySettingsModel> result = apiInstance.productCountrySettingsGetProductCountrySettings(productGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#productCountrySettingsGetProductCountrySettings");
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
| **productGuid** | **String**| GUID of the product. | |

### Return type

[**List&lt;ProductCountrySettingsModel&gt;**](ProductCountrySettingsModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the ProductCountrySettings (tax related information) |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="productPricesGetProductPrice"></a>
# **productPricesGetProductPrice**
> ProductPriceOutputModel productPricesGetProductPrice(guid)

Get product price by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the product price.
    try {
      ProductPriceOutputModel result = apiInstance.productPricesGetProductPrice(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#productPricesGetProductPrice");
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
| **guid** | **String**| Id used to get the product price. | |

### Return type

[**ProductPriceOutputModel**](ProductPriceOutputModel.md)

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

<a id="productPricesGetProductPrices"></a>
# **productPricesGetProductPrices**
> List&lt;ProductPriceOutputModel&gt; productPricesGetProductPrices(pricelistVersionGuid, fromPricelistOnly, firstRow, rowCount, textToSearch, calculateRowCount, productCode, productGuids, isVolumePriced, productCategoryGuids, productTypes)

Get all the product prices for a price list version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String pricelistVersionGuid = "pricelistVersionGuid_example"; // String | ID of the price list version.
    Boolean fromPricelistOnly = false; // Boolean | If true return only prices from the price list, if false also returns prices from the products. Default is false.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from Product name.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate the number of total rows. Default false = total row count is returned as zero.
    String productCode = ""; // String | Optional: Absolute search for products with specified product code.
    List<String> productGuids = Arrays.asList(); // List<String> | Optional: Search all product price(s) by products guid(s).
    Boolean isVolumePriced = true; // Boolean | Optional: If true, return only volume priced products. If false, return all non volume priced products. Default is null, which means return all products.
    List<String> productCategoryGuids = Arrays.asList(); // List<String> | Optional: Search product prices according to product category / categories by product category guid(s).
    List<ProductType> productTypes = Arrays.asList(); // List<ProductType> | Optional: Search product prices according to product type / types.
    try {
      List<ProductPriceOutputModel> result = apiInstance.productPricesGetProductPrices(pricelistVersionGuid, fromPricelistOnly, firstRow, rowCount, textToSearch, calculateRowCount, productCode, productGuids, isVolumePriced, productCategoryGuids, productTypes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#productPricesGetProductPrices");
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
| **pricelistVersionGuid** | **String**| ID of the price list version. | |
| **fromPricelistOnly** | **Boolean**| If true return only prices from the price list, if false also returns prices from the products. Default is false. | [optional] [default to false] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from Product name. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate the number of total rows. Default false &#x3D; total row count is returned as zero. | [optional] [default to false] |
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

<a id="productsGetProduct"></a>
# **productsGetProduct**
> ProductOutputModel productsGetProduct(guid)

Get product by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the product.
    try {
      ProductOutputModel result = apiInstance.productsGetProduct(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#productsGetProduct");
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
| **guid** | **String**| GUID used to get the product. | |

### Return type

[**ProductOutputModel**](ProductOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="productsGetProducts"></a>
# **productsGetProducts**
> List&lt;ProductOutputModel&gt; productsGetProducts(rowCount, pageToken, type, isActive, code, changedSince)

Get all the Products

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Integer rowCount = 56; // Integer | Optional: Number of rows to fetch
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    ProductType type = ProductType.fromValue("FixedFees"); // ProductType | Product type. if given, it filters the products by the given type.
    Boolean isActive = true; // Boolean | If not given, return all Products, if given as true return only isActive Products, if given as false returns only inactive Products
    String code = "code_example"; // String | Optional: Code of the product.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get products that have been added or changed after this date time (greater or equal).
    try {
      List<ProductOutputModel> result = apiInstance.productsGetProducts(rowCount, pageToken, type, isActive, code, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#productsGetProducts");
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
| **rowCount** | **Integer**| Optional: Number of rows to fetch | [optional] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **type** | [**ProductType**](.md)| Product type. if given, it filters the products by the given type. | [optional] [enum: FixedFees, Materials, Subcontracting] |
| **isActive** | **Boolean**| If not given, return all Products, if given as true return only isActive Products, if given as false returns only inactive Products | [optional] |
| **code** | **String**| Optional: Code of the product. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get products that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;ProductOutputModel&gt;**](ProductOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the Products |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectBillingCustomersGetProjectBillingCustomer"></a>
# **projectBillingCustomersGetProjectBillingCustomer**
> ProjectBillingCustomerModel2 projectBillingCustomersGetProjectBillingCustomer(guid)

Get a project billing customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | ID of the project billing customer.
    try {
      ProjectBillingCustomerModel2 result = apiInstance.projectBillingCustomersGetProjectBillingCustomer(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#projectBillingCustomersGetProjectBillingCustomer");
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

### Return type

[**ProjectBillingCustomerModel2**](ProjectBillingCustomerModel2.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Project billing customer. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectCustomPropertiesGetProjectCustomProperties"></a>
# **projectCustomPropertiesGetProjectCustomProperties**
> List&lt;CustomPropertyModel&gt; projectCustomPropertiesGetProjectCustomProperties(firstRow, rowCount, active, textToSearch, isInUse, calculateRowCount, sortings)

Get the project custom properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    Boolean active = true; // Boolean | Optional: Get only active or inactive project properties.
    String textToSearch = ""; // String | Optional: Text to search from custom property name.
    Boolean isInUse = true; // Boolean | Optional: Is the customer property used in any custom property usage.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc&sortings[1].key=Number&sortings[1].value=Asc\".
    try {
      List<CustomPropertyModel> result = apiInstance.projectCustomPropertiesGetProjectCustomProperties(firstRow, rowCount, active, textToSearch, isInUse, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#projectCustomPropertiesGetProjectCustomProperties");
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
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **active** | **Boolean**| Optional: Get only active or inactive project properties. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from custom property name. | [optional] [default to ] |
| **isInUse** | **Boolean**| Optional: Is the customer property used in any custom property usage. | [optional] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc&amp;sortings[1].key&#x3D;Number&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] |

### Return type

[**List&lt;CustomPropertyModel&gt;**](CustomPropertyModel.md)

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

<a id="projectCustomPropertiesGetProjectCustomProperty"></a>
# **projectCustomPropertiesGetProjectCustomProperty**
> CustomPropertyModel projectCustomPropertiesGetProjectCustomProperty(guid)

Get project custom property by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the project custom property.
    try {
      CustomPropertyModel result = apiInstance.projectCustomPropertiesGetProjectCustomProperty(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#projectCustomPropertiesGetProjectCustomProperty");
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
| **guid** | **String**| Id used to get the project custom property. | |

### Return type

[**CustomPropertyModel**](CustomPropertyModel.md)

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

<a id="projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItem"></a>
# **projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItem**
> ProjectCustomPropertySelectionItemOutputModel projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItem(guid)

Get project custom property selection item by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the project custom property selection item.
    try {
      ProjectCustomPropertySelectionItemOutputModel result = apiInstance.projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItem(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItem");
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
| **guid** | **String**| Id used to get the project custom property selection item. | |

### Return type

[**ProjectCustomPropertySelectionItemOutputModel**](ProjectCustomPropertySelectionItemOutputModel.md)

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

<a id="projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItems"></a>
# **projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItems**
> List&lt;ProjectCustomPropertySelectionItemOutputModel&gt; projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItems(customPropertyGuid, rowCount, isActive, pageToken, changedSince)

Get the project custom properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String customPropertyGuid = "customPropertyGuid_example"; // String | Custom property id used to get the project custom property selection items.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    Boolean isActive = true; // Boolean | Optional: Get only active or inactive selection items.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get custom property selection items that have been added or changed after this date time (greater or equal).
    try {
      List<ProjectCustomPropertySelectionItemOutputModel> result = apiInstance.projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItems(customPropertyGuid, rowCount, isActive, pageToken, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItems");
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
| **customPropertyGuid** | **String**| Custom property id used to get the project custom property selection items. | |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **isActive** | **Boolean**| Optional: Get only active or inactive selection items. | [optional] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get custom property selection items that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;ProjectCustomPropertySelectionItemOutputModel&gt;**](ProjectCustomPropertySelectionItemOutputModel.md)

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

<a id="projectMemberCostExceptionsGetProjectMemberCostException"></a>
# **projectMemberCostExceptionsGetProjectMemberCostException**
> ProjectMemberCostExceptionOutputModel projectMemberCostExceptionsGetProjectMemberCostException(guid)

Get project member cost exception by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the cost exception.
    try {
      ProjectMemberCostExceptionOutputModel result = apiInstance.projectMemberCostExceptionsGetProjectMemberCostException(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#projectMemberCostExceptionsGetProjectMemberCostException");
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
| **guid** | **String**| GUID used to get the cost exception. | |

### Return type

[**ProjectMemberCostExceptionOutputModel**](ProjectMemberCostExceptionOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Link. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectStatusTypesGetProjectStatusType"></a>
# **projectStatusTypesGetProjectStatusType**
> ProjectStatusTypeModel projectStatusTypesGetProjectStatusType(guid)

Get projectStatusType by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the projectStatusType.
    try {
      ProjectStatusTypeModel result = apiInstance.projectStatusTypesGetProjectStatusType(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#projectStatusTypesGetProjectStatusType");
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
| **guid** | **String**| GUID used to get the projectStatusType. | |

### Return type

[**ProjectStatusTypeModel**](ProjectStatusTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | projectStatusType |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectStatusTypesGetProjectStatusTypes"></a>
# **projectStatusTypesGetProjectStatusTypes**
> List&lt;ProjectStatusTypeModel&gt; projectStatusTypesGetProjectStatusTypes(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings)

Get all the ProjectStatusTypes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | If not given, return all ProjectStatusTypes, if given as true return only active ProjectStatusTypes, if given as false returns only inactive ProjectStatusTypes
    Integer firstRow = 56; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from ProjectStatusType name.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=name&sortings[0].value=Asc&sortings[1].key=isActive&sortings[1].value=Asc\"
    try {
      List<ProjectStatusTypeModel> result = apiInstance.projectStatusTypesGetProjectStatusTypes(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#projectStatusTypesGetProjectStatusTypes");
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
| **active** | **Boolean**| If not given, return all ProjectStatusTypes, if given as true return only active ProjectStatusTypes, if given as false returns only inactive ProjectStatusTypes | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from ProjectStatusType name. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc&amp;sortings[1].key&#x3D;isActive&amp;sortings[1].value&#x3D;Asc\&quot; | [optional] |

### Return type

[**List&lt;ProjectStatusTypeModel&gt;**](ProjectStatusTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the ProjectStatusTypes |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectTaskStatusesGetProjectTaskStatus"></a>
# **projectTaskStatusesGetProjectTaskStatus**
> ProjectTaskStatusModel projectTaskStatusesGetProjectTaskStatus(guid)

Get Project task status by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the Project task status.
    try {
      ProjectTaskStatusModel result = apiInstance.projectTaskStatusesGetProjectTaskStatus(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#projectTaskStatusesGetProjectTaskStatus");
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
| **guid** | **String**| GUID used to get the Project task status. | |

### Return type

[**ProjectTaskStatusModel**](ProjectTaskStatusModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Project task status. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectTaskStatusesGetProjectTaskStatuses"></a>
# **projectTaskStatusesGetProjectTaskStatuses**
> List&lt;ProjectTaskStatusModel&gt; projectTaskStatusesGetProjectTaskStatuses(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings)

Get the project task statuses.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | If not given, return all project task statuses, if given as true return only active project task statuses, if given as false returns only inactive project task statuses.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from activity type name.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=name&sortings[0].value=Asc\".
    try {
      List<ProjectTaskStatusModel> result = apiInstance.projectTaskStatusesGetProjectTaskStatuses(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#projectTaskStatusesGetProjectTaskStatuses");
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
| **active** | **Boolean**| If not given, return all project task statuses, if given as true return only active project task statuses, if given as false returns only inactive project task statuses. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from activity type name. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc\&quot;. | [optional] |

### Return type

[**List&lt;ProjectTaskStatusModel&gt;**](ProjectTaskStatusModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Activity Types. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalStatusesGetProposalStatus"></a>
# **proposalStatusesGetProposalStatus**
> ProposalStatusOutputModel proposalStatusesGetProposalStatus(guid)

Get Proposal status by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the Proposal status.
    try {
      ProposalStatusOutputModel result = apiInstance.proposalStatusesGetProposalStatus(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#proposalStatusesGetProposalStatus");
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
| **guid** | **String**| GUID used to get the Proposal status. | |

### Return type

[**ProposalStatusOutputModel**](ProposalStatusOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Proposal status |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalStatusesGetProposalStatuses"></a>
# **proposalStatusesGetProposalStatuses**
> List&lt;ProposalStatusOutputModel&gt; proposalStatusesGetProposalStatuses(isActive, pageToken, rowCount, proposalStatusName)

Get all the proposal statuses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean isActive = true; // Boolean | Optional: If not given, return all proposal statuses, if given as true return only active proposal statuses, if given as false returns only inactive proposal statuses.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String proposalStatusName = ""; // String | Optional: Search by proposal status name.
    try {
      List<ProposalStatusOutputModel> result = apiInstance.proposalStatusesGetProposalStatuses(isActive, pageToken, rowCount, proposalStatusName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#proposalStatusesGetProposalStatuses");
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
| **isActive** | **Boolean**| Optional: If not given, return all proposal statuses, if given as true return only active proposal statuses, if given as false returns only inactive proposal statuses. | [optional] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **proposalStatusName** | **String**| Optional: Search by proposal status name. | [optional] [default to ] |

### Return type

[**List&lt;ProposalStatusOutputModel&gt;**](ProposalStatusOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Proposal statuses |  * NextPageToken - Page token to fetch the next page <br>  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="proposalStatusesGetUsage"></a>
# **proposalStatusesGetUsage**
> List&lt;UsageModel2&gt; proposalStatusesGetUsage(guid)

Get usage for an proposal status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the proposal status.
    try {
      List<UsageModel2> result = apiInstance.proposalStatusesGetUsage(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#proposalStatusesGetUsage");
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
| **guid** | **String**| GUID used to get the proposal status. | |

### Return type

[**List&lt;UsageModel2&gt;**](UsageModel2.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Usage |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="rolesGetRole"></a>
# **rolesGetRole**
> RoleOutputModel rolesGetRole(guid)

Get role by GUID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the role.
    try {
      RoleOutputModel result = apiInstance.rolesGetRole(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#rolesGetRole");
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
| **guid** | **String**| Id used to get the role. | |

### Return type

[**RoleOutputModel**](RoleOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | RoleOutputModel. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="rolesGetRoles"></a>
# **rolesGetRoles**
> List&lt;RoleOutputModel&gt; rolesGetRoles(isActive, pageToken, rowCount, changedSince)

Get roles.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean isActive = true; // Boolean | If not given, return all roles, if given as true return only active roles, if given as false returns only inactive roles.
    String pageToken = "pageToken_example"; // String | Optional: Page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default all.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get roles that have been added or changed after this date time (greater or equal).
    try {
      List<RoleOutputModel> result = apiInstance.rolesGetRoles(isActive, pageToken, rowCount, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#rolesGetRoles");
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
| **isActive** | **Boolean**| If not given, return all roles, if given as true return only active roles, if given as false returns only inactive roles. | [optional] |
| **pageToken** | **String**| Optional: Page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default all. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get roles that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;RoleOutputModel&gt;**](RoleOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the roles. |  * NextPageToken - Page token to fetch the next page <br>  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="salesAccountsGetSalesAccount"></a>
# **salesAccountsGetSalesAccount**
> SalesAccountModel salesAccountsGetSalesAccount(guid)

Get sales account by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the sales account.
    try {
      SalesAccountModel result = apiInstance.salesAccountsGetSalesAccount(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#salesAccountsGetSalesAccount");
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
| **guid** | **String**| Id used to get the sales account. | |

### Return type

[**SalesAccountModel**](SalesAccountModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | SalesAccountModel. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="salesAccountsGetSalesAccounts"></a>
# **salesAccountsGetSalesAccounts**
> List&lt;SalesAccountModel&gt; salesAccountsGetSalesAccounts(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings)

Get sales accounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | If not given, return all Sales accounts, if given as true return only active Sales accounts, if given as false returns only inactive Sales accounts.
    Integer firstRow = 56; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from cost account name or identifier.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc &sortings[1].key=Identifier&sortings[1].value=Asc\".
    try {
      List<SalesAccountModel> result = apiInstance.salesAccountsGetSalesAccounts(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#salesAccountsGetSalesAccounts");
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
| **active** | **Boolean**| If not given, return all Sales accounts, if given as true return only active Sales accounts, if given as false returns only inactive Sales accounts. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from cost account name or identifier. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc &amp;sortings[1].key&#x3D;Identifier&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] |

### Return type

[**List&lt;SalesAccountModel&gt;**](SalesAccountModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the sales accounts. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="salesStatusTypesGetSalesStatusType"></a>
# **salesStatusTypesGetSalesStatusType**
> SalesStatusTypeOutputModel salesStatusTypesGetSalesStatusType(guid)

Get sales status type by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the sales status type.
    try {
      SalesStatusTypeOutputModel result = apiInstance.salesStatusTypesGetSalesStatusType(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#salesStatusTypesGetSalesStatusType");
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
| **guid** | **String**| GUID used to get the sales status type. | |

### Return type

[**SalesStatusTypeOutputModel**](SalesStatusTypeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sales status type |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="salesStatusTypesGetSalesStatusTypes"></a>
# **salesStatusTypesGetSalesStatusTypes**
> List&lt;SalesStatusTypeOutputModel&gt; salesStatusTypesGetSalesStatusTypes(active, salesState, firstRow, rowCount, textToSearch, calculateRowCount, sortings)

Get all the sales status types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | If not given, return all sales status types, if given as true return only active sales status types, if given as false returns only inactive sales status types
    SalesStatusType salesState = SalesStatusType.fromValue("InProgress"); // SalesStatusType | Optional: Get sales status types of the sales state.
    Integer firstRow = 0; // Integer | Optional: First row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from sales status type name.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc &sortings[1].key=Code&sortings[1].value=Asc\"
    try {
      List<SalesStatusTypeOutputModel> result = apiInstance.salesStatusTypesGetSalesStatusTypes(active, salesState, firstRow, rowCount, textToSearch, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#salesStatusTypesGetSalesStatusTypes");
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
| **active** | **Boolean**| If not given, return all sales status types, if given as true return only active sales status types, if given as false returns only inactive sales status types | [optional] |
| **salesState** | [**SalesStatusType**](.md)| Optional: Get sales status types of the sales state. | [optional] [enum: InProgress, Won, Lost] |
| **firstRow** | **Integer**| Optional: First row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from sales status type name. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc &amp;sortings[1].key&#x3D;Code&amp;sortings[1].value&#x3D;Asc\&quot; | [optional] |

### Return type

[**List&lt;SalesStatusTypeOutputModel&gt;**](SalesStatusTypeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sales status types |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="timeEntryTypesGetTimeEntryType"></a>
# **timeEntryTypesGetTimeEntryType**
> TimeEntryTypeModel timeEntryTypesGetTimeEntryType(guid)

Get time entry type by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | ID used to get the time entry type.
    try {
      TimeEntryTypeModel result = apiInstance.timeEntryTypesGetTimeEntryType(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#timeEntryTypesGetTimeEntryType");
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
| **guid** | **String**| ID used to get the time entry type. | |

### Return type

[**TimeEntryTypeModel**](TimeEntryTypeModel.md)

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

<a id="timeEntryTypesGetTimeEntryTypes"></a>
# **timeEntryTypesGetTimeEntryTypes**
> List&lt;TimeEntryTypeModel&gt; timeEntryTypesGetTimeEntryTypes(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings)

Get all time entry types.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | Filter the time entry types. If true/false, only the active/inactive ones are returned. If null, all the time entry types are returned.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from time entry type name.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculates the total row count.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=name&sortings[0].value=Asc\".
    try {
      List<TimeEntryTypeModel> result = apiInstance.timeEntryTypesGetTimeEntryTypes(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#timeEntryTypesGetTimeEntryTypes");
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
| **active** | **Boolean**| Filter the time entry types. If true/false, only the active/inactive ones are returned. If null, all the time entry types are returned. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from time entry type name. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculates the total row count. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc\&quot;. | [optional] |

### Return type

[**List&lt;TimeEntryTypeModel&gt;**](TimeEntryTypeModel.md)

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

<a id="timezonesGetTimezone"></a>
# **timezonesGetTimezone**
> TimezoneModel timezonesGetTimezone(guid)

Get timezone by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the timezone.
    try {
      TimezoneModel result = apiInstance.timezonesGetTimezone(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#timezonesGetTimezone");
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
| **guid** | **String**| GUID used to get the timezone. | |

### Return type

[**TimezoneModel**](TimezoneModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Timezone. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="timezonesGetTimezones"></a>
# **timezonesGetTimezones**
> List&lt;TimezoneModel&gt; timezonesGetTimezones()

Get all the timezones.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    try {
      List<TimezoneModel> result = apiInstance.timezonesGetTimezones();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#timezonesGetTimezones");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;TimezoneModel&gt;**](TimezoneModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the Timezones. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="travelExpenseTypeCountrySettingsGetTravelExpenseTypeCountrySettings"></a>
# **travelExpenseTypeCountrySettingsGetTravelExpenseTypeCountrySettings**
> List&lt;TravelExpenseTypeCountrySettingsModel&gt; travelExpenseTypeCountrySettingsGetTravelExpenseTypeCountrySettings(travelExpenseTypeGuid)

Get all country settings for a travel expense type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String travelExpenseTypeGuid = "travelExpenseTypeGuid_example"; // String | Guid of the travel expense type.
    try {
      List<TravelExpenseTypeCountrySettingsModel> result = apiInstance.travelExpenseTypeCountrySettingsGetTravelExpenseTypeCountrySettings(travelExpenseTypeGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#travelExpenseTypeCountrySettingsGetTravelExpenseTypeCountrySettings");
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
| **travelExpenseTypeGuid** | **String**| Guid of the travel expense type. | |

### Return type

[**List&lt;TravelExpenseTypeCountrySettingsModel&gt;**](TravelExpenseTypeCountrySettingsModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the TravelExpenseCountrySettings (tax related information) |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="travelExpenseTypesGetTravelExpenseType"></a>
# **travelExpenseTypesGetTravelExpenseType**
> TravelExpenseTypeOutputModel travelExpenseTypesGetTravelExpenseType(guid)

Get travel expense type by guid.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the travel expense type.
    try {
      TravelExpenseTypeOutputModel result = apiInstance.travelExpenseTypesGetTravelExpenseType(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#travelExpenseTypesGetTravelExpenseType");
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
| **guid** | **String**| GUID used to get the travel expense type. | |

### Return type

[**TravelExpenseTypeOutputModel**](TravelExpenseTypeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Travel expense type. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="travelExpenseTypesGetTravelExpenseTypes"></a>
# **travelExpenseTypesGetTravelExpenseTypes**
> List&lt;TravelExpenseTypeOutputModel&gt; travelExpenseTypesGetTravelExpenseTypes(active, firstRow, rowCount, textToSearch, code, calculateRowCount, sortings)

Get all the travel expense types.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | If not given, return all travel expense types, if given as true return only active travel expense types, if given as false returns only inactive travel expense types.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default all.
    String textToSearch = "textToSearch_example"; // String | Searched string: part of name or code.
    String code = ""; // String | Optional: Code of the travel expense type.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=IsActive&sortings[0].value=Asc&sortings[1].key=Name&sortings[1].value=Desc.
    try {
      List<TravelExpenseTypeOutputModel> result = apiInstance.travelExpenseTypesGetTravelExpenseTypes(active, firstRow, rowCount, textToSearch, code, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#travelExpenseTypesGetTravelExpenseTypes");
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
| **active** | **Boolean**| If not given, return all travel expense types, if given as true return only active travel expense types, if given as false returns only inactive travel expense types. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default all. | [optional] |
| **textToSearch** | **String**| Searched string: part of name or code. | [optional] |
| **code** | **String**| Optional: Code of the travel expense type. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;IsActive&amp;sortings[0].value&#x3D;Asc&amp;sortings[1].key&#x3D;Name&amp;sortings[1].value&#x3D;Desc. | [optional] |

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
| **200** | All the travel expense types. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="travelPricesGetTravelPrice"></a>
# **travelPricesGetTravelPrice**
> TravelPriceOutputModel travelPricesGetTravelPrice(guid)

Get travel price by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the travel price.
    try {
      TravelPriceOutputModel result = apiInstance.travelPricesGetTravelPrice(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#travelPricesGetTravelPrice");
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
| **guid** | **String**| Id used to get the travel price. | |

### Return type

[**TravelPriceOutputModel**](TravelPriceOutputModel.md)

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

<a id="travelPricesGetTravelPrices"></a>
# **travelPricesGetTravelPrices**
> List&lt;TravelPriceOutputModel&gt; travelPricesGetTravelPrices(pricelistVersionGuid, fromPricelistOnly, expenseClasses, firstRow, rowCount, textToSearch, calculateRowCount)

Get all the travel prices for a price list version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String pricelistVersionGuid = "pricelistVersionGuid_example"; // String | ID of the price list version.
    Boolean fromPricelistOnly = false; // Boolean | If true return only prices from the price list, if false also returns prices from the products. Default is false.
    List<ExpensesClass> expenseClasses = Arrays.asList(); // List<ExpensesClass> | Optional: List of expense classes to search by, defaults to all travel categories.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from Product name.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate the number of total rows. Default false = total row count is returned as zero.
    try {
      List<TravelPriceOutputModel> result = apiInstance.travelPricesGetTravelPrices(pricelistVersionGuid, fromPricelistOnly, expenseClasses, firstRow, rowCount, textToSearch, calculateRowCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#travelPricesGetTravelPrices");
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
| **pricelistVersionGuid** | **String**| ID of the price list version. | |
| **fromPricelistOnly** | **Boolean**| If true return only prices from the price list, if false also returns prices from the products. Default is false. | [optional] [default to false] |
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

<a id="travelReimbursementStatusGetTravelReimbursementStatus"></a>
# **travelReimbursementStatusGetTravelReimbursementStatus**
> TravelReimbursementStatusModel travelReimbursementStatusGetTravelReimbursementStatus(guid)

Get the travel reimbursement statuses by guid.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | reimbursement status id to get.
    try {
      TravelReimbursementStatusModel result = apiInstance.travelReimbursementStatusGetTravelReimbursementStatus(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#travelReimbursementStatusGetTravelReimbursementStatus");
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
| **guid** | **String**| reimbursement status id to get. | |

### Return type

[**TravelReimbursementStatusModel**](TravelReimbursementStatusModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TravelReimbursementStatusModel. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="travelReimbursementStatusGetTravelReimbursementStatuses"></a>
# **travelReimbursementStatusGetTravelReimbursementStatuses**
> List&lt;TravelReimbursementStatusModel&gt; travelReimbursementStatusGetTravelReimbursementStatuses(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings)

Get the travel reimbursement statuses.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | Optional: Filter the travel reimbursement statuses. If true/false, only the active/inactive ones are returned. If null, all the travel reimbursement statuses are returned.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from travel reimbursement name.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=name&sortings[0].value=Asc\".
    try {
      List<TravelReimbursementStatusModel> result = apiInstance.travelReimbursementStatusGetTravelReimbursementStatuses(active, firstRow, rowCount, textToSearch, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#travelReimbursementStatusGetTravelReimbursementStatuses");
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
| **active** | **Boolean**| Optional: Filter the travel reimbursement statuses. If true/false, only the active/inactive ones are returned. If null, all the travel reimbursement statuses are returned. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from travel reimbursement name. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc\&quot;. | [optional] |

### Return type

[**List&lt;TravelReimbursementStatusModel&gt;**](TravelReimbursementStatusModel.md)

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

<a id="userCustomPropertiesGetUserCustomProperties"></a>
# **userCustomPropertiesGetUserCustomProperties**
> List&lt;UserCustomPropertyOutputModel&gt; userCustomPropertiesGetUserCustomProperties(pageToken, rowCount, isActive, isInUse, changedSince)

Get the user custom properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    Boolean isActive = true; // Boolean | Optional: Get only active or inactive user custom properties.
    Boolean isInUse = true; // Boolean | Optional: Is the customer property used in any custom property usage.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get custom properties that have been added or changed after this date time (greater or equal).
    try {
      List<UserCustomPropertyOutputModel> result = apiInstance.userCustomPropertiesGetUserCustomProperties(pageToken, rowCount, isActive, isInUse, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#userCustomPropertiesGetUserCustomProperties");
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
| **isActive** | **Boolean**| Optional: Get only active or inactive user custom properties. | [optional] |
| **isInUse** | **Boolean**| Optional: Is the customer property used in any custom property usage. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get custom properties that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;UserCustomPropertyOutputModel&gt;**](UserCustomPropertyOutputModel.md)

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

<a id="userCustomPropertiesGetUserCustomProperty"></a>
# **userCustomPropertiesGetUserCustomProperty**
> UserCustomPropertyOutputModel userCustomPropertiesGetUserCustomProperty(guid)

Get user custom property by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the user custom property.
    try {
      UserCustomPropertyOutputModel result = apiInstance.userCustomPropertiesGetUserCustomProperty(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#userCustomPropertiesGetUserCustomProperty");
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
| **guid** | **String**| Id used to get the user custom property. | |

### Return type

[**UserCustomPropertyOutputModel**](UserCustomPropertyOutputModel.md)

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

<a id="userCustomPropertySelectionItemsGetUserCustomPropertySelectionItem"></a>
# **userCustomPropertySelectionItemsGetUserCustomPropertySelectionItem**
> UserCustomPropertySelectionItemOutputModel userCustomPropertySelectionItemsGetUserCustomPropertySelectionItem(guid)

Get user custom property selection item by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the user custom property selection item.
    try {
      UserCustomPropertySelectionItemOutputModel result = apiInstance.userCustomPropertySelectionItemsGetUserCustomPropertySelectionItem(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#userCustomPropertySelectionItemsGetUserCustomPropertySelectionItem");
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
| **guid** | **String**| Id used to get the user custom property selection item. | |

### Return type

[**UserCustomPropertySelectionItemOutputModel**](UserCustomPropertySelectionItemOutputModel.md)

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

<a id="userCustomPropertySelectionItemsGetUserCustomPropertySelectionItems"></a>
# **userCustomPropertySelectionItemsGetUserCustomPropertySelectionItems**
> List&lt;UserCustomPropertySelectionItemOutputModel&gt; userCustomPropertySelectionItemsGetUserCustomPropertySelectionItems(customPropertyGuid, rowCount, isActive, pageToken, changedSince)

Get the user custom properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String customPropertyGuid = "customPropertyGuid_example"; // String | Custom property id used to get the user custom property selection items.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    Boolean isActive = true; // Boolean | Optional: Get only active or inactive selection items.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get custom property selection items that have been added or changed after this date time (greater or equal).
    try {
      List<UserCustomPropertySelectionItemOutputModel> result = apiInstance.userCustomPropertySelectionItemsGetUserCustomPropertySelectionItems(customPropertyGuid, rowCount, isActive, pageToken, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#userCustomPropertySelectionItemsGetUserCustomPropertySelectionItems");
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
| **customPropertyGuid** | **String**| Custom property id used to get the user custom property selection items. | |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **isActive** | **Boolean**| Optional: Get only active or inactive selection items. | [optional] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get custom property selection items that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;UserCustomPropertySelectionItemOutputModel&gt;**](UserCustomPropertySelectionItemOutputModel.md)

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

<a id="vatRatesGetVatRate"></a>
# **vatRatesGetVatRate**
> VatRateOutputModel vatRatesGetVatRate(guid)

Get a vat rate by GUID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the vat rate.
    try {
      VatRateOutputModel result = apiInstance.vatRatesGetVatRate(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#vatRatesGetVatRate");
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
| **guid** | **String**| GUID used to get the vat rate. | |

### Return type

[**VatRateOutputModel**](VatRateOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Vat rate |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="vatRatesGetVatRates"></a>
# **vatRatesGetVatRates**
> List&lt;VatRateOutputModel&gt; vatRatesGetVatRates(countryGuid, active)

Get all organization vat rates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String countryGuid = "countryGuid_example"; // String | If not given, return all vat rates in organizations country. If given return only for that country.
    Boolean active = true; // Boolean | If not given, return all vat rates, if given as true return only active ones, if given as false returns only inactive ones.
    try {
      List<VatRateOutputModel> result = apiInstance.vatRatesGetVatRates(countryGuid, active);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#vatRatesGetVatRates");
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
| **countryGuid** | **String**| If not given, return all vat rates in organizations country. If given return only for that country. | [optional] |
| **active** | **Boolean**| If not given, return all vat rates, if given as true return only active ones, if given as false returns only inactive ones. | [optional] |

### Return type

[**List&lt;VatRateOutputModel&gt;**](VatRateOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Vat rates |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workContractsGetWorkContract"></a>
# **workContractsGetWorkContract**
> WorkContractOutputModel workContractsGetWorkContract(guid)

Get work contract by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the work contract.
    try {
      WorkContractOutputModel result = apiInstance.workContractsGetWorkContract(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#workContractsGetWorkContract");
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
| **guid** | **String**| Id used to get the work contract. | |

### Return type

[**WorkContractOutputModel**](WorkContractOutputModel.md)

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

<a id="workHourPricesGetWorkHourPrice"></a>
# **workHourPricesGetWorkHourPrice**
> WorkHourPriceOutputModel workHourPricesGetWorkHourPrice(guid)

Get work hour price by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the work hour price.
    try {
      WorkHourPriceOutputModel result = apiInstance.workHourPricesGetWorkHourPrice(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#workHourPricesGetWorkHourPrice");
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

[**WorkHourPriceOutputModel**](WorkHourPriceOutputModel.md)

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

<a id="workHourPricesGetWorkHourPrices"></a>
# **workHourPricesGetWorkHourPrices**
> WorkHourPriceOutputModel workHourPricesGetWorkHourPrices(pricelistVersionGuid, pageToken, rowCount, changedSince)

Get all the workHourPrices for a price list version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String pricelistVersionGuid = "pricelistVersionGuid_example"; // String | Price list version identifier.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page..
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get prices that have been added or changed after this date time (greater or equal).
    try {
      WorkHourPriceOutputModel result = apiInstance.workHourPricesGetWorkHourPrices(pricelistVersionGuid, pageToken, rowCount, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#workHourPricesGetWorkHourPrices");
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
| **pricelistVersionGuid** | **String**| Price list version identifier. | |
| **pageToken** | **String**| Optional: page token to fetch the next page.. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get prices that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**WorkHourPriceOutputModel**](WorkHourPriceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | workHourPrices. |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workTypesGetWorkType"></a>
# **workTypesGetWorkType**
> WorkTypeOutputModel workTypesGetWorkType(guid)

Get work type by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the work type.
    try {
      WorkTypeOutputModel result = apiInstance.workTypesGetWorkType(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#workTypesGetWorkType");
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
| **guid** | **String**| Id used to get the work type. | |

### Return type

[**WorkTypeOutputModel**](WorkTypeOutputModel.md)

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

<a id="workTypesGetWorkTypes"></a>
# **workTypesGetWorkTypes**
> List&lt;WorkTypeOutputModel&gt; workTypesGetWorkTypes(active, productive, firstRow, rowCount, textToSearch, code, changedSince, calculateRowCount, sortings)

Get all work types.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SettingsReadApi;

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

    SettingsReadApi apiInstance = new SettingsReadApi(defaultClient);
    Boolean active = true; // Boolean | Filter the work types. If true/false, only the active/inactive ones are returned. If null, all the work types are returned.
    Boolean productive = true; // Boolean | Filter the work types. If true/false, only the productive/non-productive ones are returned. If null, all the work types are returned.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from work type name or code.
    String code = ""; // String | Optional: Code of the work type.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get work types that have been added or changed after this date time (greater or equal).
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=name&sortings[0].value=Asc\".
    try {
      List<WorkTypeOutputModel> result = apiInstance.workTypesGetWorkTypes(active, productive, firstRow, rowCount, textToSearch, code, changedSince, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SettingsReadApi#workTypesGetWorkTypes");
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
| **active** | **Boolean**| Filter the work types. If true/false, only the active/inactive ones are returned. If null, all the work types are returned. | [optional] |
| **productive** | **Boolean**| Filter the work types. If true/false, only the productive/non-productive ones are returned. If null, all the work types are returned. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from work type name or code. | [optional] [default to ] |
| **code** | **String**| Optional: Code of the work type. | [optional] [default to ] |
| **changedSince** | **OffsetDateTime**| Optional: Get work types that have been added or changed after this date time (greater or equal). | [optional] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc\&quot;. | [optional] |

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
| **200** | All the work types matching search criteria. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

