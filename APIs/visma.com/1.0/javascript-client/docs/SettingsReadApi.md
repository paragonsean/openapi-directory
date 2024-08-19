# SeveraPublicRestApiDocumentation.SettingsReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activityTypesGetActivityType**](SettingsReadApi.md#activityTypesGetActivityType) | **GET** /v1/activitytypes/{guid} | Get Activity Type by ID
[**activityTypesGetActivityTypes**](SettingsReadApi.md#activityTypesGetActivityTypes) | **GET** /v1/activitytypes | Get the Activity Types
[**bankAccountsGetBankAccount**](SettingsReadApi.md#bankAccountsGetBankAccount) | **GET** /v1/bankaccounts/{guid} | Get bank account by ID.
[**bankAccountsGetBankAccounts**](SettingsReadApi.md#bankAccountsGetBankAccounts) | **GET** /v1/bankaccounts | Get all bank accounts for current organization.
[**businessUnitsGetBusinessUnit**](SettingsReadApi.md#businessUnitsGetBusinessUnit) | **GET** /v1/businessunits/{guid} | Get businessUnit by ID.
[**businessUnitsGetBusinessUnits**](SettingsReadApi.md#businessUnitsGetBusinessUnits) | **GET** /v1/businessunits | Get all the BusinessUnits
[**communicationTypesGetCommunicationType**](SettingsReadApi.md#communicationTypesGetCommunicationType) | **GET** /v1/communicationtypes/{guid} | Get communication type by ID.
[**communicationTypesGetCommunicationTypes**](SettingsReadApi.md#communicationTypesGetCommunicationTypes) | **GET** /v1/communicationtypes | Get all communication types.
[**contactRolesGetContactRole**](SettingsReadApi.md#contactRolesGetContactRole) | **GET** /v1/contactroles/{guid} | Get contact role by ID.
[**contactRolesGetContactRoles**](SettingsReadApi.md#contactRolesGetContactRoles) | **GET** /v1/contactroles | Get contact roles.
[**costAccountsGetCostAccount**](SettingsReadApi.md#costAccountsGetCostAccount) | **GET** /v1/costaccounts/{guid} | Get cost account by Guid.
[**costAccountsGetCostAccounts**](SettingsReadApi.md#costAccountsGetCostAccounts) | **GET** /v1/costaccounts | Get cost accounts.
[**costCentersGetCostCenter**](SettingsReadApi.md#costCentersGetCostCenter) | **GET** /v1/costcenters/{guid} | Get cost center by ID.
[**costCentersGetCostCenters**](SettingsReadApi.md#costCentersGetCostCenters) | **GET** /v1/costcenters | Get cost centers.
[**countriesGetCountries**](SettingsReadApi.md#countriesGetCountries) | **GET** /v1/localization/countries | Get all the Countries.
[**countriesGetCountry**](SettingsReadApi.md#countriesGetCountry) | **GET** /v1/localization/countries/{guid} | Get country by ID.
[**countriesGetCountryByCode2**](SettingsReadApi.md#countriesGetCountryByCode2) | **GET** /v1/localization/countries/{code2} | Get a country by ISO Alpha-2 code
[**countriesGetCountryByCode3**](SettingsReadApi.md#countriesGetCountryByCode3) | **GET** /v1/localization/countries/{code3} | Get a country by ISO Alpha-3 code
[**countriesGetCountryByName**](SettingsReadApi.md#countriesGetCountryByName) | **GET** /v1/localization/countries/{countryName} | Get a country by name
[**countriesGetCountryRegion**](SettingsReadApi.md#countriesGetCountryRegion) | **GET** /v1/localization/countryregions/{guid} | Get country region by ID.
[**countriesGetCountryRegions**](SettingsReadApi.md#countriesGetCountryRegions) | **GET** /v1/localization/countries/{countryGuid}/countryregions | Get all the Country regions for a country.
[**currenciesGetCurrencies**](SettingsReadApi.md#currenciesGetCurrencies) | **GET** /v1/currencies | Get all the Currencies
[**currenciesGetCurrency**](SettingsReadApi.md#currenciesGetCurrency) | **GET** /v1/currencies/{guid} | Get currency by ID.
[**customerCustomPropertiesGetCustomerCustomProperties**](SettingsReadApi.md#customerCustomPropertiesGetCustomerCustomProperties) | **GET** /v1/customers/customproperties | Get the customer custom properties.
[**customerCustomPropertiesGetCustomerCustomProperty**](SettingsReadApi.md#customerCustomPropertiesGetCustomerCustomProperty) | **GET** /v1/customers/customproperties/{guid} | Get customer custom property by ID.
[**customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItem**](SettingsReadApi.md#customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItem) | **GET** /v1/customers/customproperties/customercustompropertyselectionitems/{guid} | Get customer custom property selection item by ID.
[**customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItems**](SettingsReadApi.md#customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItems) | **GET** /v1/customers/customproperties/{customPropertyGuid}/customercustompropertyselectionitems | Get the customer custom properties.
[**formattingCulturesGetFormattingCulture**](SettingsReadApi.md#formattingCulturesGetFormattingCulture) | **GET** /v1/localization/formattingcultures/{guid} | Get formatting culture by ID.
[**formattingCulturesGetFormattings**](SettingsReadApi.md#formattingCulturesGetFormattings) | **GET** /v1/localization/formattingcultures | Get all the Formatting Cultures
[**holidaysGetHolidays**](SettingsReadApi.md#holidaysGetHolidays) | **GET** /v1/holidays | Get holidays.
[**holidaysGetHolidaysByTimePeriod**](SettingsReadApi.md#holidaysGetHolidaysByTimePeriod) | **GET** /v1/holidaysbytimeperiod | Get holidays with start and end date.
[**industriesGetIndustries**](SettingsReadApi.md#industriesGetIndustries) | **GET** /v1/industries | Get all the industries.
[**industriesGetIndustry**](SettingsReadApi.md#industriesGetIndustry) | **GET** /v1/industries/{guid} | Get industry by ID.
[**invoiceStatusesGetInvoiceStatus**](SettingsReadApi.md#invoiceStatusesGetInvoiceStatus) | **GET** /v1/invoicestatuses/{guid} | Get Invoice status by ID.
[**invoiceStatusesGetInvoiceStatuses**](SettingsReadApi.md#invoiceStatusesGetInvoiceStatuses) | **GET** /v1/invoicestatuses | Get invoice statuses.
[**invoiceTemplatesGetInvoiceTemplate**](SettingsReadApi.md#invoiceTemplatesGetInvoiceTemplate) | **GET** /v1/invoicetemplates/{guid} | Get invoice template by ID.
[**invoiceTemplatesGetInvoiceTemplates**](SettingsReadApi.md#invoiceTemplatesGetInvoiceTemplates) | **GET** /v1/invoicetemplates | Get invoice templates.
[**keywordsGetKeyword**](SettingsReadApi.md#keywordsGetKeyword) | **GET** /v1/keywords/{guid} | Get keyword by ID.
[**keywordsGetKeywords**](SettingsReadApi.md#keywordsGetKeywords) | **GET** /v1/keywords | Get all the keywords.
[**kpiFormulasGetKpiFormulas**](SettingsReadApi.md#kpiFormulasGetKpiFormulas) | **GET** /v1/kpiformulas | Get saved KPI formulas.
[**languagesGetLanguage**](SettingsReadApi.md#languagesGetLanguage) | **GET** /v1/localization/languages/{guid} | Get language by ID
[**languagesGetLanguages**](SettingsReadApi.md#languagesGetLanguages) | **GET** /v1/localization/languages | Get all the languages
[**leadSourcesGetLeadSource**](SettingsReadApi.md#leadSourcesGetLeadSource) | **GET** /v1/leadsources/{guid} | Get lead source by ID.
[**leadSourcesGetLeadSources**](SettingsReadApi.md#leadSourcesGetLeadSources) | **GET** /v1/leadsources | Get the lead sources.
[**marketSegmentsGetMarketSegment**](SettingsReadApi.md#marketSegmentsGetMarketSegment) | **GET** /v1/marketsegments/{guid} | Get Market Segment by ID.
[**marketSegmentsGetMarketSegments**](SettingsReadApi.md#marketSegmentsGetMarketSegments) | **GET** /v1/marketsegments | Get the Market Segments.
[**overtimePricesGetOvertimePrice**](SettingsReadApi.md#overtimePricesGetOvertimePrice) | **GET** /v1/overtimeprices/{guid} | Get overtime price by ID.
[**overtimePricesGetOvertimePrices**](SettingsReadApi.md#overtimePricesGetOvertimePrices) | **GET** /v1/pricelistversions/{pricelistVersionGuid}/overtimeprices | Get all the overtime prices for a price list version.
[**overtimesGetOvertime**](SettingsReadApi.md#overtimesGetOvertime) | **GET** /v1/overtimes/{guid} | Get overtime definition by ID.
[**overtimesGetOvertimes**](SettingsReadApi.md#overtimesGetOvertimes) | **GET** /v1/overtimes | Get overtime definitions.
[**permissionProfilesGetPermissionProfile**](SettingsReadApi.md#permissionProfilesGetPermissionProfile) | **GET** /v1/permissionprofiles/{guid} | Get Permission Profile by ID.
[**permissionProfilesGetPermissionProfiles**](SettingsReadApi.md#permissionProfilesGetPermissionProfiles) | **GET** /v1/permissionprofiles | Get the Permission Profiles.
[**phaseStatusTypesGetPhaseStatusType**](SettingsReadApi.md#phaseStatusTypesGetPhaseStatusType) | **GET** /v1/phasestatustypes/{guid} | Get phase status type by GUID
[**phaseStatusTypesGetPhaseStatusTypes**](SettingsReadApi.md#phaseStatusTypesGetPhaseStatusTypes) | **GET** /v1/phasestatustypes | Get phase status types
[**priceListVersionsGetPricelistVersion**](SettingsReadApi.md#priceListVersionsGetPricelistVersion) | **GET** /v1/pricelistversions/{guid} | Get a price list version by guid.
[**priceListVersionsGetPricelistVersionsByPricelist**](SettingsReadApi.md#priceListVersionsGetPricelistVersionsByPricelist) | **GET** /v1/pricelists/{pricelistGuid}/pricelistversions | Get all price list versions of a price list.
[**priceListsGetPriceList**](SettingsReadApi.md#priceListsGetPriceList) | **GET** /v1/pricelists/{guid} | Get price list by GUID.
[**priceListsGetPricelists**](SettingsReadApi.md#priceListsGetPricelists) | **GET** /v1/pricelists | Get all price lists.
[**productCategoriesGetProductCategories**](SettingsReadApi.md#productCategoriesGetProductCategories) | **GET** /v1/productcategories | Get product categories.
[**productCategoriesGetProductCategory**](SettingsReadApi.md#productCategoriesGetProductCategory) | **GET** /v1/productcategories/{guid} | Get product category by ID.
[**productCountrySettingsGetProductCountrySettings**](SettingsReadApi.md#productCountrySettingsGetProductCountrySettings) | **GET** /v1/products/{productGuid}/productcountrysettings | Get all the country settings for a product
[**productPricesGetProductPrice**](SettingsReadApi.md#productPricesGetProductPrice) | **GET** /v1/productprices/{guid} | Get product price by ID.
[**productPricesGetProductPrices**](SettingsReadApi.md#productPricesGetProductPrices) | **GET** /v1/pricelistversions/{pricelistVersionGuid}/productprices | Get all the product prices for a price list version.
[**productsGetProduct**](SettingsReadApi.md#productsGetProduct) | **GET** /v1/products/{guid} | Get product by ID.
[**productsGetProducts**](SettingsReadApi.md#productsGetProducts) | **GET** /v1/products | Get all the Products
[**projectBillingCustomersGetProjectBillingCustomer**](SettingsReadApi.md#projectBillingCustomersGetProjectBillingCustomer) | **GET** /v1/projectbillingcustomers/{guid} | Get a project billing customer.
[**projectCustomPropertiesGetProjectCustomProperties**](SettingsReadApi.md#projectCustomPropertiesGetProjectCustomProperties) | **GET** /v1/projects/customproperties | Get the project custom properties.
[**projectCustomPropertiesGetProjectCustomProperty**](SettingsReadApi.md#projectCustomPropertiesGetProjectCustomProperty) | **GET** /v1/projects/customproperties/{guid} | Get project custom property by ID.
[**projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItem**](SettingsReadApi.md#projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItem) | **GET** /v1/projects/customproperties/projectcustompropertyselectionitems/{guid} | Get project custom property selection item by ID.
[**projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItems**](SettingsReadApi.md#projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItems) | **GET** /v1/projects/customproperties/{customPropertyGuid}/projectcustompropertyselectionitems | Get the project custom properties.
[**projectMemberCostExceptionsGetProjectMemberCostException**](SettingsReadApi.md#projectMemberCostExceptionsGetProjectMemberCostException) | **GET** /v1/projectmembercostexceptions/{guid} | Get project member cost exception by ID.
[**projectStatusTypesGetProjectStatusType**](SettingsReadApi.md#projectStatusTypesGetProjectStatusType) | **GET** /v1/projectstatustypes/{guid} | Get projectStatusType by ID
[**projectStatusTypesGetProjectStatusTypes**](SettingsReadApi.md#projectStatusTypesGetProjectStatusTypes) | **GET** /v1/projectstatustypes | Get all the ProjectStatusTypes
[**projectTaskStatusesGetProjectTaskStatus**](SettingsReadApi.md#projectTaskStatusesGetProjectTaskStatus) | **GET** /v1/projecttaskstatuses/{guid} | Get Project task status by ID.
[**projectTaskStatusesGetProjectTaskStatuses**](SettingsReadApi.md#projectTaskStatusesGetProjectTaskStatuses) | **GET** /v1/projecttaskstatuses | Get the project task statuses.
[**proposalStatusesGetProposalStatus**](SettingsReadApi.md#proposalStatusesGetProposalStatus) | **GET** /v1/proposalstatuses/{guid} | Get Proposal status by ID
[**proposalStatusesGetProposalStatuses**](SettingsReadApi.md#proposalStatusesGetProposalStatuses) | **GET** /v1/proposalstatuses | Get all the proposal statuses
[**proposalStatusesGetUsage**](SettingsReadApi.md#proposalStatusesGetUsage) | **GET** /v1/proposalstatuses/{guid}/usage | Get usage for an proposal status.
[**rolesGetRole**](SettingsReadApi.md#rolesGetRole) | **GET** /v1/roles/{guid} | Get role by GUID.
[**rolesGetRoles**](SettingsReadApi.md#rolesGetRoles) | **GET** /v1/roles | Get roles.
[**salesAccountsGetSalesAccount**](SettingsReadApi.md#salesAccountsGetSalesAccount) | **GET** /v1/salesaccounts/{guid} | Get sales account by ID.
[**salesAccountsGetSalesAccounts**](SettingsReadApi.md#salesAccountsGetSalesAccounts) | **GET** /v1/salesaccounts | Get sales accounts.
[**salesStatusTypesGetSalesStatusType**](SettingsReadApi.md#salesStatusTypesGetSalesStatusType) | **GET** /v1/salesstatustypes/{guid} | Get sales status type by ID
[**salesStatusTypesGetSalesStatusTypes**](SettingsReadApi.md#salesStatusTypesGetSalesStatusTypes) | **GET** /v1/salesstatustypes | Get all the sales status types
[**timeEntryTypesGetTimeEntryType**](SettingsReadApi.md#timeEntryTypesGetTimeEntryType) | **GET** /v1/timeentrytypes/{guid} | Get time entry type by ID.
[**timeEntryTypesGetTimeEntryTypes**](SettingsReadApi.md#timeEntryTypesGetTimeEntryTypes) | **GET** /v1/timeentrytypes | Get all time entry types.
[**timezonesGetTimezone**](SettingsReadApi.md#timezonesGetTimezone) | **GET** /v1/localization/timezones/{guid} | Get timezone by ID.
[**timezonesGetTimezones**](SettingsReadApi.md#timezonesGetTimezones) | **GET** /v1/localization/timezones | Get all the timezones.
[**travelExpenseTypeCountrySettingsGetTravelExpenseTypeCountrySettings**](SettingsReadApi.md#travelExpenseTypeCountrySettingsGetTravelExpenseTypeCountrySettings) | **GET** /v1/travelexpensetypes/{travelExpenseTypeGuid}/travelexpensetypecountrysettings | Get all country settings for a travel expense type
[**travelExpenseTypesGetTravelExpenseType**](SettingsReadApi.md#travelExpenseTypesGetTravelExpenseType) | **GET** /v1/travelexpensetypes/{guid} | Get travel expense type by guid.
[**travelExpenseTypesGetTravelExpenseTypes**](SettingsReadApi.md#travelExpenseTypesGetTravelExpenseTypes) | **GET** /v1/travelexpensetypes | Get all the travel expense types.
[**travelPricesGetTravelPrice**](SettingsReadApi.md#travelPricesGetTravelPrice) | **GET** /v1/travelprices/{guid} | Get travel price by ID.
[**travelPricesGetTravelPrices**](SettingsReadApi.md#travelPricesGetTravelPrices) | **GET** /v1/pricelistversions/{pricelistVersionGuid}/travelprices | Get all the travel prices for a price list version.
[**travelReimbursementStatusGetTravelReimbursementStatus**](SettingsReadApi.md#travelReimbursementStatusGetTravelReimbursementStatus) | **GET** /v1/travelreimbursementstatuses/{guid} | Get the travel reimbursement statuses by guid.
[**travelReimbursementStatusGetTravelReimbursementStatuses**](SettingsReadApi.md#travelReimbursementStatusGetTravelReimbursementStatuses) | **GET** /v1/travelreimbursementstatuses | Get the travel reimbursement statuses.
[**userCustomPropertiesGetUserCustomProperties**](SettingsReadApi.md#userCustomPropertiesGetUserCustomProperties) | **GET** /v1/users/customproperties | Get the user custom properties.
[**userCustomPropertiesGetUserCustomProperty**](SettingsReadApi.md#userCustomPropertiesGetUserCustomProperty) | **GET** /v1/users/customproperties/{guid} | Get user custom property by ID.
[**userCustomPropertySelectionItemsGetUserCustomPropertySelectionItem**](SettingsReadApi.md#userCustomPropertySelectionItemsGetUserCustomPropertySelectionItem) | **GET** /v1/users/customproperties/usercustompropertyselectionitems/{guid} | Get user custom property selection item by ID.
[**userCustomPropertySelectionItemsGetUserCustomPropertySelectionItems**](SettingsReadApi.md#userCustomPropertySelectionItemsGetUserCustomPropertySelectionItems) | **GET** /v1/users/customproperties/{customPropertyGuid}/usercustompropertyselectionitems | Get the user custom properties.
[**vatRatesGetVatRate**](SettingsReadApi.md#vatRatesGetVatRate) | **GET** /v1/vatrates/{guid} | Get a vat rate by GUID
[**vatRatesGetVatRates**](SettingsReadApi.md#vatRatesGetVatRates) | **GET** /v1/vatrates | Get all organization vat rates
[**workContractsGetWorkContract**](SettingsReadApi.md#workContractsGetWorkContract) | **GET** /v1/workcontracts/{guid} | Get work contract by ID.
[**workHourPricesGetWorkHourPrice**](SettingsReadApi.md#workHourPricesGetWorkHourPrice) | **GET** /v1/workhourprices/{guid} | Get work hour price by ID.
[**workHourPricesGetWorkHourPrices**](SettingsReadApi.md#workHourPricesGetWorkHourPrices) | **GET** /v1/pricelistversions/{pricelistVersionGuid}/workhourprices | Get all the workHourPrices for a price list version.
[**workTypesGetWorkType**](SettingsReadApi.md#workTypesGetWorkType) | **GET** /v1/worktypes/{guid} | Get work type by ID.
[**workTypesGetWorkTypes**](SettingsReadApi.md#workTypesGetWorkTypes) | **GET** /v1/worktypes | Get all work types.



## activityTypesGetActivityType

> ActivityTypeModel activityTypesGetActivityType(guid)

Get Activity Type by ID

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the Activity Type.
apiInstance.activityTypesGetActivityType(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the Activity Type. | 

### Return type

[**ActivityTypeModel**](ActivityTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## activityTypesGetActivityTypes

> [ActivityTypeModel] activityTypesGetActivityTypes(opts)

Get the Activity Types

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | If not given, return all Activity Types, if given as true return only active Activity Types, if given as false returns only inactive Activity Types
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'changedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get activity types that have been added or changed after this date time (greater or equal).
  'category': [new SeveraPublicRestApiDocumentation.ActivityCategory()] // [ActivityCategory] | Optional: Category or multiple categories of activity types to search for. Default all.
};
apiInstance.activityTypesGetActivityTypes(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| If not given, return all Activity Types, if given as true return only active Activity Types, if given as false returns only inactive Activity Types | [optional] 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **changedSince** | **Date**| Optional: Get activity types that have been added or changed after this date time (greater or equal). | [optional] 
 **category** | [**[ActivityCategory]**](ActivityCategory.md)| Optional: Category or multiple categories of activity types to search for. Default all. | [optional] 

### Return type

[**[ActivityTypeModel]**](ActivityTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bankAccountsGetBankAccount

> BankAccountOutputModel bankAccountsGetBankAccount(guid)

Get bank account by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the bank account.
apiInstance.bankAccountsGetBankAccount(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the bank account. | 

### Return type

[**BankAccountOutputModel**](BankAccountOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bankAccountsGetBankAccounts

> [BankAccountOutputModel] bankAccountsGetBankAccounts(opts)

Get all bank accounts for current organization.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'companyGuid': "companyGuid_example", // String | Optional: ID of the company.
  'businessUnitGuid': "businessUnitGuid_example", // String | Optional: ID of the business unit.
  'active': true, // Boolean | If not given, returns all bank accounts, if given as true returns only active bank accounts, if given as false returns only inactive bank accounts.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from bank account name.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=BankName&sortings[0].value=Desc &sortings[1].key=BusinessUnitName&sortings[1].value=Asc\".
};
apiInstance.bankAccountsGetBankAccounts(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **companyGuid** | **String**| Optional: ID of the company. | [optional] 
 **businessUnitGuid** | **String**| Optional: ID of the business unit. | [optional] 
 **active** | **Boolean**| If not given, returns all bank accounts, if given as true returns only active bank accounts, if given as false returns only inactive bank accounts. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from bank account name. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;BankName&amp;sortings[0].value&#x3D;Desc &amp;sortings[1].key&#x3D;BusinessUnitName&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] 

### Return type

[**[BankAccountOutputModel]**](BankAccountOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## businessUnitsGetBusinessUnit

> BusinessUnitModel businessUnitsGetBusinessUnit(guid)

Get businessUnit by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the businessUnit.
apiInstance.businessUnitsGetBusinessUnit(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the businessUnit. | 

### Return type

[**BusinessUnitModel**](BusinessUnitModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## businessUnitsGetBusinessUnits

> [BusinessUnitModel] businessUnitsGetBusinessUnits(opts)

Get all the BusinessUnits

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | If not given, return all BusinessUnits, if given as true return only active BusinessUnits, if given as false returns only inactive BusinessUnits
  'companyGuid': "companyGuid_example", // String | Optional: ID of the company to which the business units belong.
  'companyCountryGuid': "companyCountryGuid_example", // String | Optional: ID of the country in which the company of business units is located.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from business unit name.
  'changedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get business units that have been added or changed after this date time (greater or equal).
  'code': "''", // String | Optional: Code of the business unit.
  'name': "''" // String | Optional: Name of the business unit.
};
apiInstance.businessUnitsGetBusinessUnits(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| If not given, return all BusinessUnits, if given as true return only active BusinessUnits, if given as false returns only inactive BusinessUnits | [optional] 
 **companyGuid** | **String**| Optional: ID of the company to which the business units belong. | [optional] 
 **companyCountryGuid** | **String**| Optional: ID of the country in which the company of business units is located. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from business unit name. | [optional] [default to &#39;&#39;]
 **changedSince** | **Date**| Optional: Get business units that have been added or changed after this date time (greater or equal). | [optional] 
 **code** | **String**| Optional: Code of the business unit. | [optional] [default to &#39;&#39;]
 **name** | **String**| Optional: Name of the business unit. | [optional] [default to &#39;&#39;]

### Return type

[**[BusinessUnitModel]**](BusinessUnitModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## communicationTypesGetCommunicationType

> CommunicationTypeModel communicationTypesGetCommunicationType(guid)

Get communication type by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | ID used to get the communication type.
apiInstance.communicationTypesGetCommunicationType(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| ID used to get the communication type. | 

### Return type

[**CommunicationTypeModel**](CommunicationTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## communicationTypesGetCommunicationTypes

> [CommunicationTypeModel] communicationTypesGetCommunicationTypes(opts)

Get all communication types.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | Filter the communication types. If true/false, only the active/inactive ones are returned. If null, all the communication types are returned.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from communication type name.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=name&sortings[0].value=Asc\".
};
apiInstance.communicationTypesGetCommunicationTypes(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| Filter the communication types. If true/false, only the active/inactive ones are returned. If null, all the communication types are returned. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from communication type name. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc\&quot;. | [optional] 

### Return type

[**[CommunicationTypeModel]**](CommunicationTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contactRolesGetContactRole

> ContactRoleModel contactRolesGetContactRole(guid)

Get contact role by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | Id used to get the contact role.
apiInstance.contactRolesGetContactRole(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| Id used to get the contact role. | 

### Return type

[**ContactRoleModel**](ContactRoleModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contactRolesGetContactRoles

> [ContactRoleModel] contactRolesGetContactRoles(opts)

Get contact roles.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | If not given, return all contact roles, if given as true return only active contact roles, if given as false returns only inactive contact roles.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from contact role name.
  'calculateRowCount': false // Boolean | Optional: Calculate total number of rows.
};
apiInstance.contactRolesGetContactRoles(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| If not given, return all contact roles, if given as true return only active contact roles, if given as false returns only inactive contact roles. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from contact role name. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]

### Return type

[**[ContactRoleModel]**](ContactRoleModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## costAccountsGetCostAccount

> CostAccountModel costAccountsGetCostAccount(guid)

Get cost account by Guid.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | Cost account's guid.
apiInstance.costAccountsGetCostAccount(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| Cost account&#39;s guid. | 

### Return type

[**CostAccountModel**](CostAccountModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## costAccountsGetCostAccounts

> [CostAccountModel] costAccountsGetCostAccounts(opts)

Get cost accounts.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | If not given, return all cost accounts, if given as true return only active cost accounts, if given as false returns only inactive cost accounts.
  'firstRow': 56, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from cost account name or identifier.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc &sortings[1].key=Identifier&sortings[1].value=Asc\".
};
apiInstance.costAccountsGetCostAccounts(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| If not given, return all cost accounts, if given as true return only active cost accounts, if given as false returns only inactive cost accounts. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from cost account name or identifier. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc &amp;sortings[1].key&#x3D;Identifier&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] 

### Return type

[**[CostAccountModel]**](CostAccountModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## costCentersGetCostCenter

> CostCenterModel costCentersGetCostCenter(guid)

Get cost center by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | Id used to get the cost center.
apiInstance.costCentersGetCostCenter(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| Id used to get the cost center. | 

### Return type

[**CostCenterModel**](CostCenterModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## costCentersGetCostCenters

> [CostCenterModel] costCentersGetCostCenters(opts)

Get cost centers.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | If not given, return all cost centers, if given as true return only active cost centers, if given as false returns only inactive cost centers.
  'firstRow': 56, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from cost center name or identifier.
  'changedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get cost centers that have been added or changed after this date time (greater or equal).
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()], // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\".
  'identifier': "''", // String | Optional: Identifier of the cost center.
  'name': "''" // String | Optional: Name of the cost center.
};
apiInstance.costCentersGetCostCenters(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| If not given, return all cost centers, if given as true return only active cost centers, if given as false returns only inactive cost centers. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from cost center name or identifier. | [optional] [default to &#39;&#39;]
 **changedSince** | **Date**| Optional: Get cost centers that have been added or changed after this date time (greater or equal). | [optional] 
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. | [optional] 
 **identifier** | **String**| Optional: Identifier of the cost center. | [optional] [default to &#39;&#39;]
 **name** | **String**| Optional: Name of the cost center. | [optional] [default to &#39;&#39;]

### Return type

[**[CostCenterModel]**](CostCenterModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## countriesGetCountries

> [CountryModel] countriesGetCountries()

Get all the Countries.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
apiInstance.countriesGetCountries((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[CountryModel]**](CountryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## countriesGetCountry

> CountryModel countriesGetCountry(guid)

Get country by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the country.
apiInstance.countriesGetCountry(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the country. | 

### Return type

[**CountryModel**](CountryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## countriesGetCountryByCode2

> [CountryModel] countriesGetCountryByCode2(code2)

Get a country by ISO Alpha-2 code

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let code2 = "code2_example"; // String | Optional: ISO Alpha-2 code used to get a country.
apiInstance.countriesGetCountryByCode2(code2, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code2** | **String**| Optional: ISO Alpha-2 code used to get a country. | 

### Return type

[**[CountryModel]**](CountryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## countriesGetCountryByCode3

> [CountryModel] countriesGetCountryByCode3(code3)

Get a country by ISO Alpha-3 code

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let code3 = "code3_example"; // String | Optional: ISO Alpha-3 code used to get a country.
apiInstance.countriesGetCountryByCode3(code3, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code3** | **String**| Optional: ISO Alpha-3 code used to get a country. | 

### Return type

[**[CountryModel]**](CountryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## countriesGetCountryByName

> [CountryModel] countriesGetCountryByName(countryName)

Get a country by name

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let countryName = "countryName_example"; // String | Optional: English country name.
apiInstance.countriesGetCountryByName(countryName, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countryName** | **String**| Optional: English country name. | 

### Return type

[**[CountryModel]**](CountryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## countriesGetCountryRegion

> CountryRegionModel countriesGetCountryRegion(guid)

Get country region by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the country region.
apiInstance.countriesGetCountryRegion(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the country region. | 

### Return type

[**CountryRegionModel**](CountryRegionModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## countriesGetCountryRegions

> [CountryRegionModel] countriesGetCountryRegions(countryGuid)

Get all the Country regions for a country.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let countryGuid = "countryGuid_example"; // String | GUID of the country.
apiInstance.countriesGetCountryRegions(countryGuid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countryGuid** | **String**| GUID of the country. | 

### Return type

[**[CountryRegionModel]**](CountryRegionModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## currenciesGetCurrencies

> [CurrencyOutputModel] currenciesGetCurrencies(opts)

Get all the Currencies

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | If not given, return all Currencies, if given as true return only active Currencies, if given as false returns only inactive Currencies.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text based search applied to the result. Matches currency name and code.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=name&sortings[0].value=Asc\". Using additional sorting fields \"CreatedDate\" and / or \"LastUpdatedDate\" as keys sort currencies without a timestamp provided when sorting with other date fields.
};
apiInstance.currenciesGetCurrencies(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| If not given, return all Currencies, if given as true return only active Currencies, if given as false returns only inactive Currencies. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text based search applied to the result. Matches currency name and code. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc\&quot;. Using additional sorting fields \&quot;CreatedDate\&quot; and / or \&quot;LastUpdatedDate\&quot; as keys sort currencies without a timestamp provided when sorting with other date fields. | [optional] 

### Return type

[**[CurrencyOutputModel]**](CurrencyOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## currenciesGetCurrency

> CurrencyOutputModel currenciesGetCurrency(guid)

Get currency by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the currency.
apiInstance.currenciesGetCurrency(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the currency. | 

### Return type

[**CurrencyOutputModel**](CurrencyOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerCustomPropertiesGetCustomerCustomProperties

> [CustomPropertyModel] customerCustomPropertiesGetCustomerCustomProperties(opts)

Get the customer custom properties.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'active': true, // Boolean | Optional: Get only active or inactive customer properties.
  'textToSearch': "''", // String | Optional: Text to search from custom property name.
  'isInUse': true, // Boolean | Optional: Is the customer property used in any custom property usage.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc&sortings[1].key=Number&sortings[1].value=Asc\".
};
apiInstance.customerCustomPropertiesGetCustomerCustomProperties(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **active** | **Boolean**| Optional: Get only active or inactive customer properties. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from custom property name. | [optional] [default to &#39;&#39;]
 **isInUse** | **Boolean**| Optional: Is the customer property used in any custom property usage. | [optional] 
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc&amp;sortings[1].key&#x3D;Number&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] 

### Return type

[**[CustomPropertyModel]**](CustomPropertyModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerCustomPropertiesGetCustomerCustomProperty

> CustomPropertyModel customerCustomPropertiesGetCustomerCustomProperty(guid)

Get customer custom property by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | Id used to get the customer custom property.
apiInstance.customerCustomPropertiesGetCustomerCustomProperty(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| Id used to get the customer custom property. | 

### Return type

[**CustomPropertyModel**](CustomPropertyModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItem

> CustomerCustomPropertySelectionItemOutputModel customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItem(guid)

Get customer custom property selection item by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | Id used to get the customer custom property selection item.
apiInstance.customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItem(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| Id used to get the customer custom property selection item. | 

### Return type

[**CustomerCustomPropertySelectionItemOutputModel**](CustomerCustomPropertySelectionItemOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItems

> [CustomerCustomPropertySelectionItemOutputModel] customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItems(customPropertyGuid, opts)

Get the customer custom properties.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let customPropertyGuid = "customPropertyGuid_example"; // String | Custom property id used to get the customer custom property selection items.
let opts = {
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'isActive': true, // Boolean | Optional: Get only active or inactive selection items.
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get custom property selection items that have been added or changed after this date time (greater or equal).
};
apiInstance.customerCustomPropertySelectionItemsGetCustomerCustomPropertySelectionItems(customPropertyGuid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customPropertyGuid** | **String**| Custom property id used to get the customer custom property selection items. | 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **isActive** | **Boolean**| Optional: Get only active or inactive selection items. | [optional] 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **changedSince** | **Date**| Optional: Get custom property selection items that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[CustomerCustomPropertySelectionItemOutputModel]**](CustomerCustomPropertySelectionItemOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## formattingCulturesGetFormattingCulture

> FormattingCultureModel formattingCulturesGetFormattingCulture(guid)

Get formatting culture by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the formatting culture.
apiInstance.formattingCulturesGetFormattingCulture(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the formatting culture. | 

### Return type

[**FormattingCultureModel**](FormattingCultureModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## formattingCulturesGetFormattings

> [FormattingCultureModel] formattingCulturesGetFormattings()

Get all the Formatting Cultures

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
apiInstance.formattingCulturesGetFormattings((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[FormattingCultureModel]**](FormattingCultureModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## holidaysGetHolidays

> [HolidayModel] holidaysGetHolidays(opts)

Get holidays.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'year': 56, // Number | Optional: Holidays for this year only. Default: all years.
  'countryGuid': "countryGuid_example" // String | Optional: Holidays for this country only. Default local.
};
apiInstance.holidaysGetHolidays(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **Number**| Optional: Holidays for this year only. Default: all years. | [optional] 
 **countryGuid** | **String**| Optional: Holidays for this country only. Default local. | [optional] 

### Return type

[**[HolidayModel]**](HolidayModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## holidaysGetHolidaysByTimePeriod

> [HolidayModel] holidaysGetHolidaysByTimePeriod(opts)

Get holidays with start and end date.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Start date for holidays.
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | End date for holidays.
  'countryGuid': "countryGuid_example" // String | Optional: Holidays for this country only. Default local.
};
apiInstance.holidaysGetHolidaysByTimePeriod(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startDate** | **Date**| Start date for holidays. | [optional] 
 **endDate** | **Date**| End date for holidays. | [optional] 
 **countryGuid** | **String**| Optional: Holidays for this country only. Default local. | [optional] 

### Return type

[**[HolidayModel]**](HolidayModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## industriesGetIndustries

> [IndustryModel] industriesGetIndustries(opts)

Get all the industries.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | If not given, return all industries, if given as true return only active industries, if given as false returns only inactive industries.
  'firstRow': 56, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from industry name.
  'calculateRowCount': false // Boolean | Optional: Calculate total number of rows.
};
apiInstance.industriesGetIndustries(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| If not given, return all industries, if given as true return only active industries, if given as false returns only inactive industries. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from industry name. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]

### Return type

[**[IndustryModel]**](IndustryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## industriesGetIndustry

> IndustryModel industriesGetIndustry(guid)

Get industry by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the industry.
apiInstance.industriesGetIndustry(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the industry. | 

### Return type

[**IndustryModel**](IndustryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoiceStatusesGetInvoiceStatus

> InvoiceStatusModel invoiceStatusesGetInvoiceStatus(guid)

Get Invoice status by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the Invoice status.
apiInstance.invoiceStatusesGetInvoiceStatus(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the Invoice status. | 

### Return type

[**InvoiceStatusModel**](InvoiceStatusModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoiceStatusesGetInvoiceStatuses

> [InvoiceStatusModel] invoiceStatusesGetInvoiceStatuses(opts)

Get invoice statuses.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | Filter the invoice statuses. If true/false, only the active/inactive ones are returned. If null, all the invoice statuses are returned.
  'firstRow': 56, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from invoice status name.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc\".
};
apiInstance.invoiceStatusesGetInvoiceStatuses(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| Filter the invoice statuses. If true/false, only the active/inactive ones are returned. If null, all the invoice statuses are returned. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from invoice status name. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc\&quot;. | [optional] 

### Return type

[**[InvoiceStatusModel]**](InvoiceStatusModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoiceTemplatesGetInvoiceTemplate

> InvoiceTemplateModel invoiceTemplatesGetInvoiceTemplate(guid)

Get invoice template by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | ID of the invoice template.
apiInstance.invoiceTemplatesGetInvoiceTemplate(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| ID of the invoice template. | 

### Return type

[**InvoiceTemplateModel**](InvoiceTemplateModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoiceTemplatesGetInvoiceTemplates

> [InvoiceTemplateModel] invoiceTemplatesGetInvoiceTemplates(opts)

Get invoice templates.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | 
  'firstRow': 56, // Number | 
  'rowCount': 56, // Number | 
  'textToSearch': "''", // String | 
  'calculateRowCount': false, // Boolean | 
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | 
};
apiInstance.invoiceTemplatesGetInvoiceTemplates(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**|  | [optional] 
 **firstRow** | **Number**|  | [optional] 
 **rowCount** | **Number**|  | [optional] 
 **textToSearch** | **String**|  | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**|  | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)|  | [optional] 

### Return type

[**[InvoiceTemplateModel]**](InvoiceTemplateModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## keywordsGetKeyword

> KeywordModel keywordsGetKeyword(guid)

Get keyword by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the keyword.
apiInstance.keywordsGetKeyword(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the keyword. | 

### Return type

[**KeywordModel**](KeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## keywordsGetKeywords

> [KeywordModel] keywordsGetKeywords(opts)

Get all the keywords.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'category': new SeveraPublicRestApiDocumentation.KeywordCategory(), // KeywordCategory | Optional: category of the keyword.
  'active': true, // Boolean | If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from keyword.
  'changedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get keywords that have been added or changed after this date time (greater or equal).
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()], // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\".
  'keyword': "''" // String | Optional: Keyword name.
};
apiInstance.keywordsGetKeywords(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | [**KeywordCategory**](.md)| Optional: category of the keyword. | [optional] 
 **active** | **Boolean**| If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from keyword. | [optional] [default to &#39;&#39;]
 **changedSince** | **Date**| Optional: Get keywords that have been added or changed after this date time (greater or equal). | [optional] 
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. | [optional] 
 **keyword** | **String**| Optional: Keyword name. | [optional] [default to &#39;&#39;]

### Return type

[**[KeywordModel]**](KeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## kpiFormulasGetKpiFormulas

> [KpiFormulaModelBase] kpiFormulasGetKpiFormulas(opts)

Get saved KPI formulas.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'category': new SeveraPublicRestApiDocumentation.KpiFormulaCategory(), // KpiFormulaCategory | Optional: Category of KPI formula (Project, Invoice, User).
  'isActive': true, // Boolean | Optional: return with given active status. Default is to return all.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()], // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc\".
  'includeDefinition': false, // Boolean | Optional: Include definition to response. Default false.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get KPI formulas that have been added or changed after this date time (greater or equal).
};
apiInstance.kpiFormulasGetKpiFormulas(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | [**KpiFormulaCategory**](.md)| Optional: Category of KPI formula (Project, Invoice, User). | [optional] 
 **isActive** | **Boolean**| Optional: return with given active status. Default is to return all. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search. | [optional] [default to &#39;&#39;]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc\&quot;. | [optional] 
 **includeDefinition** | **Boolean**| Optional: Include definition to response. Default false. | [optional] [default to false]
 **changedSince** | **Date**| Optional: Get KPI formulas that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[KpiFormulaModelBase]**](KpiFormulaModelBase.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## languagesGetLanguage

> LanguageModel languagesGetLanguage(guid)

Get language by ID

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the language.
apiInstance.languagesGetLanguage(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the language. | 

### Return type

[**LanguageModel**](LanguageModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## languagesGetLanguages

> [LanguageModel] languagesGetLanguages(opts)

Get all the languages

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'isInvoiceLanguage': true // Boolean | Optional: which languages to fetch. only invoice languages or non invoice languages?, default all.
};
apiInstance.languagesGetLanguages(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isInvoiceLanguage** | **Boolean**| Optional: which languages to fetch. only invoice languages or non invoice languages?, default all. | [optional] 

### Return type

[**[LanguageModel]**](LanguageModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## leadSourcesGetLeadSource

> LeadSourceModel leadSourcesGetLeadSource(guid)

Get lead source by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the lead source.
apiInstance.leadSourcesGetLeadSource(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the lead source. | 

### Return type

[**LeadSourceModel**](LeadSourceModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## leadSourcesGetLeadSources

> [LeadSourceModel] leadSourcesGetLeadSources(opts)

Get the lead sources.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | If not given, return all lead sources, if given as true return only active lead sources, if given as false returns only inactive lead sources.
  'firstRow': 56, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from lead source name.
  'calculateRowCount': false // Boolean | Optional: Calculate total number of rows.
};
apiInstance.leadSourcesGetLeadSources(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| If not given, return all lead sources, if given as true return only active lead sources, if given as false returns only inactive lead sources. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from lead source name. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]

### Return type

[**[LeadSourceModel]**](LeadSourceModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## marketSegmentsGetMarketSegment

> MarketSegmentModel marketSegmentsGetMarketSegment(guid)

Get Market Segment by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the Market Segment.
apiInstance.marketSegmentsGetMarketSegment(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the Market Segment. | 

### Return type

[**MarketSegmentModel**](MarketSegmentModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## marketSegmentsGetMarketSegments

> [MarketSegmentModel] marketSegmentsGetMarketSegments(opts)

Get the Market Segments.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | If not given, return all Market Segments, if given as true return only active Market Segments, if given as false returns only inactive Market Segments.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from market segment name.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'includeChildSegments': true // Boolean | Optional: Include also child market segments. If false returns only parent segments. Default true.
};
apiInstance.marketSegmentsGetMarketSegments(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| If not given, return all Market Segments, if given as true return only active Market Segments, if given as false returns only inactive Market Segments. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from market segment name. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **includeChildSegments** | **Boolean**| Optional: Include also child market segments. If false returns only parent segments. Default true. | [optional] [default to true]

### Return type

[**[MarketSegmentModel]**](MarketSegmentModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## overtimePricesGetOvertimePrice

> OvertimePriceModel overtimePricesGetOvertimePrice(guid)

Get overtime price by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | Id used to get the overtime price.
apiInstance.overtimePricesGetOvertimePrice(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| Id used to get the overtime price. | 

### Return type

[**OvertimePriceModel**](OvertimePriceModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## overtimePricesGetOvertimePrices

> [OvertimePriceModel] overtimePricesGetOvertimePrices(pricelistVersionGuid)

Get all the overtime prices for a price list version.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let pricelistVersionGuid = "pricelistVersionGuid_example"; // String | 
apiInstance.overtimePricesGetOvertimePrices(pricelistVersionGuid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricelistVersionGuid** | **String**|  | 

### Return type

[**[OvertimePriceModel]**](OvertimePriceModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## overtimesGetOvertime

> OvertimeModel overtimesGetOvertime(guid)

Get overtime definition by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | Id used to get the overtime definition.
apiInstance.overtimesGetOvertime(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| Id used to get the overtime definition. | 

### Return type

[**OvertimeModel**](OvertimeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## overtimesGetOvertimes

> [OvertimeModel] overtimesGetOvertimes(opts)

Get overtime definitions.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | If not given, return all overtime definitions, if given as true return only active overtime definitions, if given as false returns only inactive overtime definitions.
  'firstRow': 56, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default all.
  'textToSearch': "''", // String | Optional: Text to search from overtime name.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=name&sortings[0].value=Asc\"\".
};
apiInstance.overtimesGetOvertimes(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| If not given, return all overtime definitions, if given as true return only active overtime definitions, if given as false returns only inactive overtime definitions. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default all. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from overtime name. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc\&quot;\&quot;. | [optional] 

### Return type

[**[OvertimeModel]**](OvertimeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## permissionProfilesGetPermissionProfile

> PermissionProfileModel permissionProfilesGetPermissionProfile(guid)

Get Permission Profile by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the Permission Profile.
apiInstance.permissionProfilesGetPermissionProfile(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the Permission Profile. | 

### Return type

[**PermissionProfileModel**](PermissionProfileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## permissionProfilesGetPermissionProfiles

> [PermissionProfileModel] permissionProfilesGetPermissionProfiles(opts)

Get the Permission Profiles.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | If not given, return all Permission Profiles, if given as true return only active Permission Profiles, if given as false returns only inactive Permission Profiles.
  'firstRow': 56, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from permission profile name.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=name&sortings[0].value=Asc&sortings[1].key=isActive&sortings[1].value=Asc\".
};
apiInstance.permissionProfilesGetPermissionProfiles(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| If not given, return all Permission Profiles, if given as true return only active Permission Profiles, if given as false returns only inactive Permission Profiles. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from permission profile name. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc&amp;sortings[1].key&#x3D;isActive&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] 

### Return type

[**[PermissionProfileModel]**](PermissionProfileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## phaseStatusTypesGetPhaseStatusType

> PhaseStatusTypeModel phaseStatusTypesGetPhaseStatusType(guid)

Get phase status type by GUID

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | Id used to get the phase status type.
apiInstance.phaseStatusTypesGetPhaseStatusType(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| Id used to get the phase status type. | 

### Return type

[**PhaseStatusTypeModel**](PhaseStatusTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## phaseStatusTypesGetPhaseStatusTypes

> [PhaseStatusTypeModel] phaseStatusTypesGetPhaseStatusTypes(opts)

Get phase status types

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | If not given, return all phase status types, if given as true return only active phase status types, if given as false returns only inactive phase status types
  'firstRow': 56, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default all.
  'textToSearch': "''", // String | 
  'calculateRowCount': false, // Boolean | 
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | 
};
apiInstance.phaseStatusTypesGetPhaseStatusTypes(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| If not given, return all phase status types, if given as true return only active phase status types, if given as false returns only inactive phase status types | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default all. | [optional] 
 **textToSearch** | **String**|  | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**|  | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)|  | [optional] 

### Return type

[**[PhaseStatusTypeModel]**](PhaseStatusTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## priceListVersionsGetPricelistVersion

> PricelistVersionOutputModel priceListVersionsGetPricelistVersion(guid)

Get a price list version by guid.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | 
apiInstance.priceListVersionsGetPricelistVersion(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**|  | 

### Return type

[**PricelistVersionOutputModel**](PricelistVersionOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## priceListVersionsGetPricelistVersionsByPricelist

> [PricelistVersionOutputModel] priceListVersionsGetPricelistVersionsByPricelist(pricelistGuid)

Get all price list versions of a price list.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let pricelistGuid = "pricelistGuid_example"; // String | 
apiInstance.priceListVersionsGetPricelistVersionsByPricelist(pricelistGuid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricelistGuid** | **String**|  | 

### Return type

[**[PricelistVersionOutputModel]**](PricelistVersionOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## priceListsGetPriceList

> PriceListModel priceListsGetPriceList(guid)

Get price list by GUID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | ID used to get the price list.
apiInstance.priceListsGetPriceList(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| ID used to get the price list. | 

### Return type

[**PriceListModel**](PriceListModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## priceListsGetPricelists

> [PriceListOutputModel] priceListsGetPricelists(opts)

Get all price lists.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | If not given, return all price lists, if given as true return only active price lists, if given as false returns only inactive price lists.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from price list name.
  'currencyGuid': "currencyGuid_example", // String | Optional: ID of the price list currency.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()], // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\".
  'name': "''" // String | Optional: Name of the price list.
};
apiInstance.priceListsGetPricelists(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| If not given, return all price lists, if given as true return only active price lists, if given as false returns only inactive price lists. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from price list name. | [optional] [default to &#39;&#39;]
 **currencyGuid** | **String**| Optional: ID of the price list currency. | [optional] 
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. | [optional] 
 **name** | **String**| Optional: Name of the price list. | [optional] [default to &#39;&#39;]

### Return type

[**[PriceListOutputModel]**](PriceListOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productCategoriesGetProductCategories

> [ProductCategoryModel] productCategoriesGetProductCategories(opts)

Get product categories.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | If not given, return all Product categories, if given as true return only active Product categories, if given as false returns only inactive Product categories.
  'firstRow': 56, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default all.
  'textToSearch': "''", // String | Optional: Text to search from product category name or code.
  'changedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get product categories that have been added or changed after this date time (greater or equal).
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: ?sortings[0].key=Name&sortings[0].value=Desc &sortings[1].key=Code&sortings[1].value=Asc.
};
apiInstance.productCategoriesGetProductCategories(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| If not given, return all Product categories, if given as true return only active Product categories, if given as false returns only inactive Product categories. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default all. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from product category name or code. | [optional] [default to &#39;&#39;]
 **changedSince** | **Date**| Optional: Get product categories that have been added or changed after this date time (greater or equal). | [optional] 
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: ?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc &amp;sortings[1].key&#x3D;Code&amp;sortings[1].value&#x3D;Asc. | [optional] 

### Return type

[**[ProductCategoryModel]**](ProductCategoryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productCategoriesGetProductCategory

> ProductCategoryModel productCategoriesGetProductCategory(guid)

Get product category by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | Id used to get the product category.
apiInstance.productCategoriesGetProductCategory(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| Id used to get the product category. | 

### Return type

[**ProductCategoryModel**](ProductCategoryModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productCountrySettingsGetProductCountrySettings

> [ProductCountrySettingsModel] productCountrySettingsGetProductCountrySettings(productGuid)

Get all the country settings for a product

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let productGuid = "productGuid_example"; // String | GUID of the product.
apiInstance.productCountrySettingsGetProductCountrySettings(productGuid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **productGuid** | **String**| GUID of the product. | 

### Return type

[**[ProductCountrySettingsModel]**](ProductCountrySettingsModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productPricesGetProductPrice

> ProductPriceOutputModel productPricesGetProductPrice(guid)

Get product price by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | Id used to get the product price.
apiInstance.productPricesGetProductPrice(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| Id used to get the product price. | 

### Return type

[**ProductPriceOutputModel**](ProductPriceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productPricesGetProductPrices

> [ProductPriceOutputModel] productPricesGetProductPrices(pricelistVersionGuid, opts)

Get all the product prices for a price list version.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let pricelistVersionGuid = "pricelistVersionGuid_example"; // String | ID of the price list version.
let opts = {
  'fromPricelistOnly': false, // Boolean | If true return only prices from the price list, if false also returns prices from the products. Default is false.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from Product name.
  'calculateRowCount': false, // Boolean | Optional: Calculate the number of total rows. Default false = total row count is returned as zero.
  'productCode': "''", // String | Optional: Absolute search for products with specified product code.
  'productGuids': ["null"], // [String] | Optional: Search all product price(s) by products guid(s).
  'isVolumePriced': true, // Boolean | Optional: If true, return only volume priced products. If false, return all non volume priced products. Default is null, which means return all products.
  'productCategoryGuids': ["null"], // [String] | Optional: Search product prices according to product category / categories by product category guid(s).
  'productTypes': [new SeveraPublicRestApiDocumentation.ProductType()] // [ProductType] | Optional: Search product prices according to product type / types.
};
apiInstance.productPricesGetProductPrices(pricelistVersionGuid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricelistVersionGuid** | **String**| ID of the price list version. | 
 **fromPricelistOnly** | **Boolean**| If true return only prices from the price list, if false also returns prices from the products. Default is false. | [optional] [default to false]
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from Product name. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate the number of total rows. Default false &#x3D; total row count is returned as zero. | [optional] [default to false]
 **productCode** | **String**| Optional: Absolute search for products with specified product code. | [optional] [default to &#39;&#39;]
 **productGuids** | [**[String]**](String.md)| Optional: Search all product price(s) by products guid(s). | [optional] 
 **isVolumePriced** | **Boolean**| Optional: If true, return only volume priced products. If false, return all non volume priced products. Default is null, which means return all products. | [optional] 
 **productCategoryGuids** | [**[String]**](String.md)| Optional: Search product prices according to product category / categories by product category guid(s). | [optional] 
 **productTypes** | [**[ProductType]**](ProductType.md)| Optional: Search product prices according to product type / types. | [optional] 

### Return type

[**[ProductPriceOutputModel]**](ProductPriceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsGetProduct

> ProductOutputModel productsGetProduct(guid)

Get product by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the product.
apiInstance.productsGetProduct(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the product. | 

### Return type

[**ProductOutputModel**](ProductOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsGetProducts

> [ProductOutputModel] productsGetProducts(opts)

Get all the Products

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'rowCount': 56, // Number | Optional: Number of rows to fetch
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'type': new SeveraPublicRestApiDocumentation.ProductType(), // ProductType | Product type. if given, it filters the products by the given type.
  'isActive': true, // Boolean | If not given, return all Products, if given as true return only isActive Products, if given as false returns only inactive Products
  'code': "code_example", // String | Optional: Code of the product.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get products that have been added or changed after this date time (greater or equal).
};
apiInstance.productsGetProducts(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rowCount** | **Number**| Optional: Number of rows to fetch | [optional] 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **type** | [**ProductType**](.md)| Product type. if given, it filters the products by the given type. | [optional] 
 **isActive** | **Boolean**| If not given, return all Products, if given as true return only isActive Products, if given as false returns only inactive Products | [optional] 
 **code** | **String**| Optional: Code of the product. | [optional] 
 **changedSince** | **Date**| Optional: Get products that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[ProductOutputModel]**](ProductOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectBillingCustomersGetProjectBillingCustomer

> ProjectBillingCustomerModel2 projectBillingCustomersGetProjectBillingCustomer(guid)

Get a project billing customer.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | ID of the project billing customer.
apiInstance.projectBillingCustomersGetProjectBillingCustomer(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| ID of the project billing customer. | 

### Return type

[**ProjectBillingCustomerModel2**](ProjectBillingCustomerModel2.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectCustomPropertiesGetProjectCustomProperties

> [CustomPropertyModel] projectCustomPropertiesGetProjectCustomProperties(opts)

Get the project custom properties.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'active': true, // Boolean | Optional: Get only active or inactive project properties.
  'textToSearch': "''", // String | Optional: Text to search from custom property name.
  'isInUse': true, // Boolean | Optional: Is the customer property used in any custom property usage.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc&sortings[1].key=Number&sortings[1].value=Asc\".
};
apiInstance.projectCustomPropertiesGetProjectCustomProperties(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **active** | **Boolean**| Optional: Get only active or inactive project properties. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from custom property name. | [optional] [default to &#39;&#39;]
 **isInUse** | **Boolean**| Optional: Is the customer property used in any custom property usage. | [optional] 
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc&amp;sortings[1].key&#x3D;Number&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] 

### Return type

[**[CustomPropertyModel]**](CustomPropertyModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectCustomPropertiesGetProjectCustomProperty

> CustomPropertyModel projectCustomPropertiesGetProjectCustomProperty(guid)

Get project custom property by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | Id used to get the project custom property.
apiInstance.projectCustomPropertiesGetProjectCustomProperty(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| Id used to get the project custom property. | 

### Return type

[**CustomPropertyModel**](CustomPropertyModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItem

> ProjectCustomPropertySelectionItemOutputModel projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItem(guid)

Get project custom property selection item by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | Id used to get the project custom property selection item.
apiInstance.projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItem(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| Id used to get the project custom property selection item. | 

### Return type

[**ProjectCustomPropertySelectionItemOutputModel**](ProjectCustomPropertySelectionItemOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItems

> [ProjectCustomPropertySelectionItemOutputModel] projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItems(customPropertyGuid, opts)

Get the project custom properties.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let customPropertyGuid = "customPropertyGuid_example"; // String | Custom property id used to get the project custom property selection items.
let opts = {
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'isActive': true, // Boolean | Optional: Get only active or inactive selection items.
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get custom property selection items that have been added or changed after this date time (greater or equal).
};
apiInstance.projectCustomPropertySelectionItemsGetProjectCustomPropertySelectionItems(customPropertyGuid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customPropertyGuid** | **String**| Custom property id used to get the project custom property selection items. | 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **isActive** | **Boolean**| Optional: Get only active or inactive selection items. | [optional] 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **changedSince** | **Date**| Optional: Get custom property selection items that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[ProjectCustomPropertySelectionItemOutputModel]**](ProjectCustomPropertySelectionItemOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectMemberCostExceptionsGetProjectMemberCostException

> ProjectMemberCostExceptionOutputModel projectMemberCostExceptionsGetProjectMemberCostException(guid)

Get project member cost exception by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the cost exception.
apiInstance.projectMemberCostExceptionsGetProjectMemberCostException(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the cost exception. | 

### Return type

[**ProjectMemberCostExceptionOutputModel**](ProjectMemberCostExceptionOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectStatusTypesGetProjectStatusType

> ProjectStatusTypeModel projectStatusTypesGetProjectStatusType(guid)

Get projectStatusType by ID

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the projectStatusType.
apiInstance.projectStatusTypesGetProjectStatusType(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the projectStatusType. | 

### Return type

[**ProjectStatusTypeModel**](ProjectStatusTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectStatusTypesGetProjectStatusTypes

> [ProjectStatusTypeModel] projectStatusTypesGetProjectStatusTypes(opts)

Get all the ProjectStatusTypes

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | If not given, return all ProjectStatusTypes, if given as true return only active ProjectStatusTypes, if given as false returns only inactive ProjectStatusTypes
  'firstRow': 56, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from ProjectStatusType name.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=name&sortings[0].value=Asc&sortings[1].key=isActive&sortings[1].value=Asc\"
};
apiInstance.projectStatusTypesGetProjectStatusTypes(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| If not given, return all ProjectStatusTypes, if given as true return only active ProjectStatusTypes, if given as false returns only inactive ProjectStatusTypes | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from ProjectStatusType name. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc&amp;sortings[1].key&#x3D;isActive&amp;sortings[1].value&#x3D;Asc\&quot; | [optional] 

### Return type

[**[ProjectStatusTypeModel]**](ProjectStatusTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectTaskStatusesGetProjectTaskStatus

> ProjectTaskStatusModel projectTaskStatusesGetProjectTaskStatus(guid)

Get Project task status by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the Project task status.
apiInstance.projectTaskStatusesGetProjectTaskStatus(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the Project task status. | 

### Return type

[**ProjectTaskStatusModel**](ProjectTaskStatusModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectTaskStatusesGetProjectTaskStatuses

> [ProjectTaskStatusModel] projectTaskStatusesGetProjectTaskStatuses(opts)

Get the project task statuses.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | If not given, return all project task statuses, if given as true return only active project task statuses, if given as false returns only inactive project task statuses.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from activity type name.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=name&sortings[0].value=Asc\".
};
apiInstance.projectTaskStatusesGetProjectTaskStatuses(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| If not given, return all project task statuses, if given as true return only active project task statuses, if given as false returns only inactive project task statuses. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from activity type name. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc\&quot;. | [optional] 

### Return type

[**[ProjectTaskStatusModel]**](ProjectTaskStatusModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proposalStatusesGetProposalStatus

> ProposalStatusOutputModel proposalStatusesGetProposalStatus(guid)

Get Proposal status by ID

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the Proposal status.
apiInstance.proposalStatusesGetProposalStatus(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the Proposal status. | 

### Return type

[**ProposalStatusOutputModel**](ProposalStatusOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proposalStatusesGetProposalStatuses

> [ProposalStatusOutputModel] proposalStatusesGetProposalStatuses(opts)

Get all the proposal statuses

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'isActive': true, // Boolean | Optional: If not given, return all proposal statuses, if given as true return only active proposal statuses, if given as false returns only inactive proposal statuses.
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'proposalStatusName': "''" // String | Optional: Search by proposal status name.
};
apiInstance.proposalStatusesGetProposalStatuses(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isActive** | **Boolean**| Optional: If not given, return all proposal statuses, if given as true return only active proposal statuses, if given as false returns only inactive proposal statuses. | [optional] 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **proposalStatusName** | **String**| Optional: Search by proposal status name. | [optional] [default to &#39;&#39;]

### Return type

[**[ProposalStatusOutputModel]**](ProposalStatusOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proposalStatusesGetUsage

> [UsageModel2] proposalStatusesGetUsage(guid)

Get usage for an proposal status.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the proposal status.
apiInstance.proposalStatusesGetUsage(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the proposal status. | 

### Return type

[**[UsageModel2]**](UsageModel2.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rolesGetRole

> RoleOutputModel rolesGetRole(guid)

Get role by GUID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | Id used to get the role.
apiInstance.rolesGetRole(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| Id used to get the role. | 

### Return type

[**RoleOutputModel**](RoleOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rolesGetRoles

> [RoleOutputModel] rolesGetRoles(opts)

Get roles.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'isActive': true, // Boolean | If not given, return all roles, if given as true return only active roles, if given as false returns only inactive roles.
  'pageToken': "pageToken_example", // String | Optional: Page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default all.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get roles that have been added or changed after this date time (greater or equal).
};
apiInstance.rolesGetRoles(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isActive** | **Boolean**| If not given, return all roles, if given as true return only active roles, if given as false returns only inactive roles. | [optional] 
 **pageToken** | **String**| Optional: Page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default all. | [optional] 
 **changedSince** | **Date**| Optional: Get roles that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[RoleOutputModel]**](RoleOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesAccountsGetSalesAccount

> SalesAccountModel salesAccountsGetSalesAccount(guid)

Get sales account by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | Id used to get the sales account.
apiInstance.salesAccountsGetSalesAccount(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| Id used to get the sales account. | 

### Return type

[**SalesAccountModel**](SalesAccountModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesAccountsGetSalesAccounts

> [SalesAccountModel] salesAccountsGetSalesAccounts(opts)

Get sales accounts.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | If not given, return all Sales accounts, if given as true return only active Sales accounts, if given as false returns only inactive Sales accounts.
  'firstRow': 56, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from cost account name or identifier.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc &sortings[1].key=Identifier&sortings[1].value=Asc\".
};
apiInstance.salesAccountsGetSalesAccounts(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| If not given, return all Sales accounts, if given as true return only active Sales accounts, if given as false returns only inactive Sales accounts. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from cost account name or identifier. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc &amp;sortings[1].key&#x3D;Identifier&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] 

### Return type

[**[SalesAccountModel]**](SalesAccountModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesStatusTypesGetSalesStatusType

> SalesStatusTypeOutputModel salesStatusTypesGetSalesStatusType(guid)

Get sales status type by ID

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the sales status type.
apiInstance.salesStatusTypesGetSalesStatusType(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the sales status type. | 

### Return type

[**SalesStatusTypeOutputModel**](SalesStatusTypeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesStatusTypesGetSalesStatusTypes

> [SalesStatusTypeOutputModel] salesStatusTypesGetSalesStatusTypes(opts)

Get all the sales status types

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | If not given, return all sales status types, if given as true return only active sales status types, if given as false returns only inactive sales status types
  'salesState': new SeveraPublicRestApiDocumentation.SalesStatusType(), // SalesStatusType | Optional: Get sales status types of the sales state.
  'firstRow': 0, // Number | Optional: First row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from sales status type name.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc &sortings[1].key=Code&sortings[1].value=Asc\"
};
apiInstance.salesStatusTypesGetSalesStatusTypes(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| If not given, return all sales status types, if given as true return only active sales status types, if given as false returns only inactive sales status types | [optional] 
 **salesState** | [**SalesStatusType**](.md)| Optional: Get sales status types of the sales state. | [optional] 
 **firstRow** | **Number**| Optional: First row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from sales status type name. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc &amp;sortings[1].key&#x3D;Code&amp;sortings[1].value&#x3D;Asc\&quot; | [optional] 

### Return type

[**[SalesStatusTypeOutputModel]**](SalesStatusTypeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeEntryTypesGetTimeEntryType

> TimeEntryTypeModel timeEntryTypesGetTimeEntryType(guid)

Get time entry type by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | ID used to get the time entry type.
apiInstance.timeEntryTypesGetTimeEntryType(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| ID used to get the time entry type. | 

### Return type

[**TimeEntryTypeModel**](TimeEntryTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeEntryTypesGetTimeEntryTypes

> [TimeEntryTypeModel] timeEntryTypesGetTimeEntryTypes(opts)

Get all time entry types.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | Filter the time entry types. If true/false, only the active/inactive ones are returned. If null, all the time entry types are returned.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from time entry type name.
  'calculateRowCount': false, // Boolean | Optional: Calculates the total row count.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=name&sortings[0].value=Asc\".
};
apiInstance.timeEntryTypesGetTimeEntryTypes(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| Filter the time entry types. If true/false, only the active/inactive ones are returned. If null, all the time entry types are returned. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from time entry type name. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculates the total row count. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc\&quot;. | [optional] 

### Return type

[**[TimeEntryTypeModel]**](TimeEntryTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timezonesGetTimezone

> TimezoneModel timezonesGetTimezone(guid)

Get timezone by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the timezone.
apiInstance.timezonesGetTimezone(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the timezone. | 

### Return type

[**TimezoneModel**](TimezoneModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timezonesGetTimezones

> [TimezoneModel] timezonesGetTimezones()

Get all the timezones.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
apiInstance.timezonesGetTimezones((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[TimezoneModel]**](TimezoneModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelExpenseTypeCountrySettingsGetTravelExpenseTypeCountrySettings

> [TravelExpenseTypeCountrySettingsModel] travelExpenseTypeCountrySettingsGetTravelExpenseTypeCountrySettings(travelExpenseTypeGuid)

Get all country settings for a travel expense type

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let travelExpenseTypeGuid = "travelExpenseTypeGuid_example"; // String | Guid of the travel expense type.
apiInstance.travelExpenseTypeCountrySettingsGetTravelExpenseTypeCountrySettings(travelExpenseTypeGuid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **travelExpenseTypeGuid** | **String**| Guid of the travel expense type. | 

### Return type

[**[TravelExpenseTypeCountrySettingsModel]**](TravelExpenseTypeCountrySettingsModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelExpenseTypesGetTravelExpenseType

> TravelExpenseTypeOutputModel travelExpenseTypesGetTravelExpenseType(guid)

Get travel expense type by guid.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the travel expense type.
apiInstance.travelExpenseTypesGetTravelExpenseType(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the travel expense type. | 

### Return type

[**TravelExpenseTypeOutputModel**](TravelExpenseTypeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelExpenseTypesGetTravelExpenseTypes

> [TravelExpenseTypeOutputModel] travelExpenseTypesGetTravelExpenseTypes(opts)

Get all the travel expense types.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | If not given, return all travel expense types, if given as true return only active travel expense types, if given as false returns only inactive travel expense types.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default all.
  'textToSearch': "textToSearch_example", // String | Searched string: part of name or code.
  'code': "''", // String | Optional: Code of the travel expense type.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=IsActive&sortings[0].value=Asc&sortings[1].key=Name&sortings[1].value=Desc.
};
apiInstance.travelExpenseTypesGetTravelExpenseTypes(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| If not given, return all travel expense types, if given as true return only active travel expense types, if given as false returns only inactive travel expense types. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default all. | [optional] 
 **textToSearch** | **String**| Searched string: part of name or code. | [optional] 
 **code** | **String**| Optional: Code of the travel expense type. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;IsActive&amp;sortings[0].value&#x3D;Asc&amp;sortings[1].key&#x3D;Name&amp;sortings[1].value&#x3D;Desc. | [optional] 

### Return type

[**[TravelExpenseTypeOutputModel]**](TravelExpenseTypeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelPricesGetTravelPrice

> TravelPriceOutputModel travelPricesGetTravelPrice(guid)

Get travel price by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | Id used to get the travel price.
apiInstance.travelPricesGetTravelPrice(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| Id used to get the travel price. | 

### Return type

[**TravelPriceOutputModel**](TravelPriceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelPricesGetTravelPrices

> [TravelPriceOutputModel] travelPricesGetTravelPrices(pricelistVersionGuid, opts)

Get all the travel prices for a price list version.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let pricelistVersionGuid = "pricelistVersionGuid_example"; // String | ID of the price list version.
let opts = {
  'fromPricelistOnly': false, // Boolean | If true return only prices from the price list, if false also returns prices from the products. Default is false.
  'expenseClasses': [new SeveraPublicRestApiDocumentation.ExpensesClass()], // [ExpensesClass] | Optional: List of expense classes to search by, defaults to all travel categories.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from Product name.
  'calculateRowCount': false // Boolean | Optional: Calculate the number of total rows. Default false = total row count is returned as zero.
};
apiInstance.travelPricesGetTravelPrices(pricelistVersionGuid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricelistVersionGuid** | **String**| ID of the price list version. | 
 **fromPricelistOnly** | **Boolean**| If true return only prices from the price list, if false also returns prices from the products. Default is false. | [optional] [default to false]
 **expenseClasses** | [**[ExpensesClass]**](ExpensesClass.md)| Optional: List of expense classes to search by, defaults to all travel categories. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from Product name. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate the number of total rows. Default false &#x3D; total row count is returned as zero. | [optional] [default to false]

### Return type

[**[TravelPriceOutputModel]**](TravelPriceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelReimbursementStatusGetTravelReimbursementStatus

> TravelReimbursementStatusModel travelReimbursementStatusGetTravelReimbursementStatus(guid)

Get the travel reimbursement statuses by guid.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | reimbursement status id to get.
apiInstance.travelReimbursementStatusGetTravelReimbursementStatus(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| reimbursement status id to get. | 

### Return type

[**TravelReimbursementStatusModel**](TravelReimbursementStatusModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelReimbursementStatusGetTravelReimbursementStatuses

> [TravelReimbursementStatusModel] travelReimbursementStatusGetTravelReimbursementStatuses(opts)

Get the travel reimbursement statuses.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | Optional: Filter the travel reimbursement statuses. If true/false, only the active/inactive ones are returned. If null, all the travel reimbursement statuses are returned.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from travel reimbursement name.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=name&sortings[0].value=Asc\".
};
apiInstance.travelReimbursementStatusGetTravelReimbursementStatuses(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| Optional: Filter the travel reimbursement statuses. If true/false, only the active/inactive ones are returned. If null, all the travel reimbursement statuses are returned. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from travel reimbursement name. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc\&quot;. | [optional] 

### Return type

[**[TravelReimbursementStatusModel]**](TravelReimbursementStatusModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userCustomPropertiesGetUserCustomProperties

> [UserCustomPropertyOutputModel] userCustomPropertiesGetUserCustomProperties(opts)

Get the user custom properties.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'isActive': true, // Boolean | Optional: Get only active or inactive user custom properties.
  'isInUse': true, // Boolean | Optional: Is the customer property used in any custom property usage.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get custom properties that have been added or changed after this date time (greater or equal).
};
apiInstance.userCustomPropertiesGetUserCustomProperties(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **isActive** | **Boolean**| Optional: Get only active or inactive user custom properties. | [optional] 
 **isInUse** | **Boolean**| Optional: Is the customer property used in any custom property usage. | [optional] 
 **changedSince** | **Date**| Optional: Get custom properties that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[UserCustomPropertyOutputModel]**](UserCustomPropertyOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userCustomPropertiesGetUserCustomProperty

> UserCustomPropertyOutputModel userCustomPropertiesGetUserCustomProperty(guid)

Get user custom property by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | Id used to get the user custom property.
apiInstance.userCustomPropertiesGetUserCustomProperty(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| Id used to get the user custom property. | 

### Return type

[**UserCustomPropertyOutputModel**](UserCustomPropertyOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userCustomPropertySelectionItemsGetUserCustomPropertySelectionItem

> UserCustomPropertySelectionItemOutputModel userCustomPropertySelectionItemsGetUserCustomPropertySelectionItem(guid)

Get user custom property selection item by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | Id used to get the user custom property selection item.
apiInstance.userCustomPropertySelectionItemsGetUserCustomPropertySelectionItem(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| Id used to get the user custom property selection item. | 

### Return type

[**UserCustomPropertySelectionItemOutputModel**](UserCustomPropertySelectionItemOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userCustomPropertySelectionItemsGetUserCustomPropertySelectionItems

> [UserCustomPropertySelectionItemOutputModel] userCustomPropertySelectionItemsGetUserCustomPropertySelectionItems(customPropertyGuid, opts)

Get the user custom properties.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let customPropertyGuid = "customPropertyGuid_example"; // String | Custom property id used to get the user custom property selection items.
let opts = {
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'isActive': true, // Boolean | Optional: Get only active or inactive selection items.
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get custom property selection items that have been added or changed after this date time (greater or equal).
};
apiInstance.userCustomPropertySelectionItemsGetUserCustomPropertySelectionItems(customPropertyGuid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customPropertyGuid** | **String**| Custom property id used to get the user custom property selection items. | 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **isActive** | **Boolean**| Optional: Get only active or inactive selection items. | [optional] 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **changedSince** | **Date**| Optional: Get custom property selection items that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[UserCustomPropertySelectionItemOutputModel]**](UserCustomPropertySelectionItemOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vatRatesGetVatRate

> VatRateOutputModel vatRatesGetVatRate(guid)

Get a vat rate by GUID

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | GUID used to get the vat rate.
apiInstance.vatRatesGetVatRate(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| GUID used to get the vat rate. | 

### Return type

[**VatRateOutputModel**](VatRateOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vatRatesGetVatRates

> [VatRateOutputModel] vatRatesGetVatRates(opts)

Get all organization vat rates

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'countryGuid': "countryGuid_example", // String | If not given, return all vat rates in organizations country. If given return only for that country.
  'active': true // Boolean | If not given, return all vat rates, if given as true return only active ones, if given as false returns only inactive ones.
};
apiInstance.vatRatesGetVatRates(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countryGuid** | **String**| If not given, return all vat rates in organizations country. If given return only for that country. | [optional] 
 **active** | **Boolean**| If not given, return all vat rates, if given as true return only active ones, if given as false returns only inactive ones. | [optional] 

### Return type

[**[VatRateOutputModel]**](VatRateOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workContractsGetWorkContract

> WorkContractOutputModel workContractsGetWorkContract(guid)

Get work contract by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | Id used to get the work contract.
apiInstance.workContractsGetWorkContract(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| Id used to get the work contract. | 

### Return type

[**WorkContractOutputModel**](WorkContractOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workHourPricesGetWorkHourPrice

> WorkHourPriceOutputModel workHourPricesGetWorkHourPrice(guid)

Get work hour price by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | Id used to get the work hour price.
apiInstance.workHourPricesGetWorkHourPrice(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| Id used to get the work hour price. | 

### Return type

[**WorkHourPriceOutputModel**](WorkHourPriceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workHourPricesGetWorkHourPrices

> WorkHourPriceOutputModel workHourPricesGetWorkHourPrices(pricelistVersionGuid, opts)

Get all the workHourPrices for a price list version.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let pricelistVersionGuid = "pricelistVersionGuid_example"; // String | Price list version identifier.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page..
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get prices that have been added or changed after this date time (greater or equal).
};
apiInstance.workHourPricesGetWorkHourPrices(pricelistVersionGuid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricelistVersionGuid** | **String**| Price list version identifier. | 
 **pageToken** | **String**| Optional: page token to fetch the next page.. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **changedSince** | **Date**| Optional: Get prices that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**WorkHourPriceOutputModel**](WorkHourPriceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workTypesGetWorkType

> WorkTypeOutputModel workTypesGetWorkType(guid)

Get work type by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let guid = "guid_example"; // String | Id used to get the work type.
apiInstance.workTypesGetWorkType(guid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **String**| Id used to get the work type. | 

### Return type

[**WorkTypeOutputModel**](WorkTypeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workTypesGetWorkTypes

> [WorkTypeOutputModel] workTypesGetWorkTypes(opts)

Get all work types.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.SettingsReadApi();
let opts = {
  'active': true, // Boolean | Filter the work types. If true/false, only the active/inactive ones are returned. If null, all the work types are returned.
  'productive': true, // Boolean | Filter the work types. If true/false, only the productive/non-productive ones are returned. If null, all the work types are returned.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from work type name or code.
  'code': "''", // String | Optional: Code of the work type.
  'changedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get work types that have been added or changed after this date time (greater or equal).
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=name&sortings[0].value=Asc\".
};
apiInstance.workTypesGetWorkTypes(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **Boolean**| Filter the work types. If true/false, only the active/inactive ones are returned. If null, all the work types are returned. | [optional] 
 **productive** | **Boolean**| Filter the work types. If true/false, only the productive/non-productive ones are returned. If null, all the work types are returned. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from work type name or code. | [optional] [default to &#39;&#39;]
 **code** | **String**| Optional: Code of the work type. | [optional] [default to &#39;&#39;]
 **changedSince** | **Date**| Optional: Get work types that have been added or changed after this date time (greater or equal). | [optional] 
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;name&amp;sortings[0].value&#x3D;Asc\&quot;. | [optional] 

### Return type

[**[WorkTypeOutputModel]**](WorkTypeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

