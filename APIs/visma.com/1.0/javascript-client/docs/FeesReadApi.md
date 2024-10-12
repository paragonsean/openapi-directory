# SeveraPublicRestApiDocumentation.FeesReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**flatRatesGetAllFlatRates**](FeesReadApi.md#flatRatesGetAllFlatRates) | **GET** /v1/flatrates | Get all flat rates
[**flatRatesGetFlatrate**](FeesReadApi.md#flatRatesGetFlatrate) | **GET** /v1/flatrates/{guid} | Get flat rate.
[**flatRatesGetFlatratesForProject**](FeesReadApi.md#flatRatesGetFlatratesForProject) | **GET** /v1/projects/{projectGuid}/flatrates | Get project&#39;s flat rates.
[**projectFeesGetDeletedProjectFees**](FeesReadApi.md#projectFeesGetDeletedProjectFees) | **GET** /v1/deletedprojectfees | Get the deleted project fees.
[**projectFeesGetProjectFee**](FeesReadApi.md#projectFeesGetProjectFee) | **GET** /v1/projectfees/{guid} | Get projectFee by ID.
[**projectFeesGetProjectFeesByToken**](FeesReadApi.md#projectFeesGetProjectFeesByToken) | **GET** /v1/projectfees | Get the project fees.
[**projectFeesGetProjectFeesForProject**](FeesReadApi.md#projectFeesGetProjectFeesForProject) | **GET** /v1/projects/{projectGuid}/projectfees | Get all the project fees for a project
[**projectFeesGetUserProjectFees**](FeesReadApi.md#projectFeesGetUserProjectFees) | **GET** /v1/users/{userGuid}/projectfees | Get all the projectFees for a user
[**projectRecurringFeeRulesGetProjectRecurringFeeRule**](FeesReadApi.md#projectRecurringFeeRulesGetProjectRecurringFeeRule) | **GET** /v1/projectrecurringfeerules/{guid} | Get project&#39;s RecurringFeeRule by ID.
[**projectRecurringFeeRulesGetProjectRecurringFeeRules**](FeesReadApi.md#projectRecurringFeeRulesGetProjectRecurringFeeRules) | **GET** /v1/projectrecurringfeerules | Get the recurring fee rules.
[**projectRecurringFeeRulesGetProjectRecurringFeeRulesForProject**](FeesReadApi.md#projectRecurringFeeRulesGetProjectRecurringFeeRulesForProject) | **GET** /v1/projects/{projectGuid}/projectrecurringfeerules | Get all the Recurring Fee Rules for a project



## flatRatesGetAllFlatRates

> [FlatRateOutputModel] flatRatesGetAllFlatRates(opts)

Get all flat rates

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

let apiInstance = new SeveraPublicRestApiDocumentation.FeesReadApi();
let opts = {
  'pageToken': "pageToken_example", // String | Optional: Page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'changedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get flat rates that have been added or changed after this date time (greater or equal).
  'invoiceGuid': "invoiceGuid_example" // String | Optional: Get flat rates by invoice guid. Default all.
};
apiInstance.flatRatesGetAllFlatRates(opts, (error, data, response) => {
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
 **pageToken** | **String**| Optional: Page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **changedSince** | **Date**| Optional: Get flat rates that have been added or changed after this date time (greater or equal). | [optional] 
 **invoiceGuid** | **String**| Optional: Get flat rates by invoice guid. Default all. | [optional] 

### Return type

[**[FlatRateOutputModel]**](FlatRateOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## flatRatesGetFlatrate

> [FlatRateOutputModel] flatRatesGetFlatrate(guid)

Get flat rate.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FeesReadApi();
let guid = "guid_example"; // String | Id of the flat rate.
apiInstance.flatRatesGetFlatrate(guid, (error, data, response) => {
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
 **guid** | **String**| Id of the flat rate. | 

### Return type

[**[FlatRateOutputModel]**](FlatRateOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## flatRatesGetFlatratesForProject

> [FlatRateOutputModel] flatRatesGetFlatratesForProject(projectGuid)

Get project&#39;s flat rates.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FeesReadApi();
let projectGuid = "projectGuid_example"; // String | Id of the project.
apiInstance.flatRatesGetFlatratesForProject(projectGuid, (error, data, response) => {
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
 **projectGuid** | **String**| Id of the project. | 

### Return type

[**[FlatRateOutputModel]**](FlatRateOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectFeesGetDeletedProjectFees

> [DeletedProjectFeeModel] projectFeesGetDeletedProjectFees(opts)

Get the deleted project fees.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FeesReadApi();
let opts = {
  'pageToken': "pageToken_example", // String | 
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'projectGuids': ["null"], // [String] | Optional: ID of the project for the deleted project fees to be fetched. If not provided, returns for all projects. Default all.
  'userGuids': ["null"], // [String] | Optional: ID of the user. If not provided, returns for all users. Default all.
  'deletedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get project fees that have been deleted after this date time (greater or equal).
};
apiInstance.projectFeesGetDeletedProjectFees(opts, (error, data, response) => {
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
 **pageToken** | **String**|  | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **projectGuids** | [**[String]**](String.md)| Optional: ID of the project for the deleted project fees to be fetched. If not provided, returns for all projects. Default all. | [optional] 
 **userGuids** | [**[String]**](String.md)| Optional: ID of the user. If not provided, returns for all users. Default all. | [optional] 
 **deletedSince** | **Date**| Optional: Get project fees that have been deleted after this date time (greater or equal). | [optional] 

### Return type

[**[DeletedProjectFeeModel]**](DeletedProjectFeeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectFeesGetProjectFee

> ProjectFeeOutputModel projectFeesGetProjectFee(guid)

Get projectFee by ID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FeesReadApi();
let guid = "guid_example"; // String | Id used to get the projectFee.
apiInstance.projectFeesGetProjectFee(guid, (error, data, response) => {
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
 **guid** | **String**| Id used to get the projectFee. | 

### Return type

[**ProjectFeeOutputModel**](ProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectFeesGetProjectFeesByToken

> [ProjectFeeOutputModel] projectFeesGetProjectFeesByToken(opts)

Get the project fees.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FeesReadApi();
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: Number of rows to fetch
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get project fees that have been added or changed after this date time (greater or equal).
};
apiInstance.projectFeesGetProjectFeesByToken(opts, (error, data, response) => {
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
 **rowCount** | **Number**| Optional: Number of rows to fetch | [optional] 
 **changedSince** | **Date**| Optional: Get project fees that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[ProjectFeeOutputModel]**](ProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectFeesGetProjectFeesForProject

> [ProjectFeeOutputModel] projectFeesGetProjectFeesForProject(projectGuid, opts)

Get all the project fees for a project

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

let apiInstance = new SeveraPublicRestApiDocumentation.FeesReadApi();
let projectGuid = "projectGuid_example"; // String | ID of the project.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: Number of rows to fetch.
  'productType': new SeveraPublicRestApiDocumentation.ProductType(), // ProductType | Optional: ProjectFee's product type. if given, it filters the projectFees by the given type. FixedFees (Own work), Materials (Products), Subcontracting
  'isBillable': true, // Boolean | Optional: Filter the project fees. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null.
  'isBilled': true, // Boolean | Optional: Filter the project fees. If true/false, only the ones that are/are not invoiced are returned. If null, all are returned. Default is null.
  'invoiceableDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Filter the project fees. When given, only the ones that are invoiceable before or on the given date are returned. Default is null.
  'includeRecurringRules': false, // Boolean | Optional: Also fetches recurring rules along with project fees. Default is false.
  'isBillablePeriodInFuture': true // Boolean | Optional. Filter the project fees. If true/false, only the ones that will be billable in the future are returned. If null, all are returned. Default is false.
};
apiInstance.projectFeesGetProjectFeesForProject(projectGuid, opts, (error, data, response) => {
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
 **projectGuid** | **String**| ID of the project. | 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: Number of rows to fetch. | [optional] 
 **productType** | [**ProductType**](.md)| Optional: ProjectFee&#39;s product type. if given, it filters the projectFees by the given type. FixedFees (Own work), Materials (Products), Subcontracting | [optional] 
 **isBillable** | **Boolean**| Optional: Filter the project fees. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null. | [optional] 
 **isBilled** | **Boolean**| Optional: Filter the project fees. If true/false, only the ones that are/are not invoiced are returned. If null, all are returned. Default is null. | [optional] 
 **invoiceableDate** | **Date**| Optional: Filter the project fees. When given, only the ones that are invoiceable before or on the given date are returned. Default is null. | [optional] 
 **includeRecurringRules** | **Boolean**| Optional: Also fetches recurring rules along with project fees. Default is false. | [optional] [default to false]
 **isBillablePeriodInFuture** | **Boolean**| Optional. Filter the project fees. If true/false, only the ones that will be billable in the future are returned. If null, all are returned. Default is false. | [optional] 

### Return type

[**[ProjectFeeOutputModel]**](ProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectFeesGetUserProjectFees

> [ProjectFeeOutputModel] projectFeesGetUserProjectFees(userGuid, opts)

Get all the projectFees for a user

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

let apiInstance = new SeveraPublicRestApiDocumentation.FeesReadApi();
let userGuid = "userGuid_example"; // String | ID of the user.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: Number of rows to fetch.
  'productType': new SeveraPublicRestApiDocumentation.ProductType(), // ProductType | Optional: ProjectFee's product type. if given, it filters the projectFees by the given type. FixedFees (Own work), Materials (Products), Subcontracting.
  'isBillable': true, // Boolean | Optional: Filter the project fees. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null.
  'isBilled': true, // Boolean | Optional: Filter the project fees. If true/false, only the ones that are/are not invoiced are returned. If null, all are returned. Default is null.
  'invoiceableDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Filter the project fees. When given, only the ones that are invoiceable before or on the given date are returned. Default is null.
  'hasPhase': true, // Boolean | Optional: Filter the project fees. If true/false, only the ones are connected/not-connected to a phase are returned. If null, all are returned. Default is null.
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Start date search criteria. Only get project fees that have event date from this date.
  'endDate': new Date("2013-10-20T19:20:30+01:00") // Date | End date search criteria. Only get project fees that have event date until this date.
};
apiInstance.projectFeesGetUserProjectFees(userGuid, opts, (error, data, response) => {
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
 **userGuid** | **String**| ID of the user. | 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: Number of rows to fetch. | [optional] 
 **productType** | [**ProductType**](.md)| Optional: ProjectFee&#39;s product type. if given, it filters the projectFees by the given type. FixedFees (Own work), Materials (Products), Subcontracting. | [optional] 
 **isBillable** | **Boolean**| Optional: Filter the project fees. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null. | [optional] 
 **isBilled** | **Boolean**| Optional: Filter the project fees. If true/false, only the ones that are/are not invoiced are returned. If null, all are returned. Default is null. | [optional] 
 **invoiceableDate** | **Date**| Optional: Filter the project fees. When given, only the ones that are invoiceable before or on the given date are returned. Default is null. | [optional] 
 **hasPhase** | **Boolean**| Optional: Filter the project fees. If true/false, only the ones are connected/not-connected to a phase are returned. If null, all are returned. Default is null. | [optional] 
 **startDate** | **Date**| Start date search criteria. Only get project fees that have event date from this date. | [optional] 
 **endDate** | **Date**| End date search criteria. Only get project fees that have event date until this date. | [optional] 

### Return type

[**[ProjectFeeOutputModel]**](ProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectRecurringFeeRulesGetProjectRecurringFeeRule

> ProjectRecurringFeeRuleOutputModel projectRecurringFeeRulesGetProjectRecurringFeeRule(guid, opts)

Get project&#39;s RecurringFeeRule by ID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FeesReadApi();
let guid = "guid_example"; // String | Id used to get the ProjectRecurringFeeRule.
let opts = {
  'includeInactive': false // Boolean | Indicates the rule should be returned even if it is not active. Default is false.
};
apiInstance.projectRecurringFeeRulesGetProjectRecurringFeeRule(guid, opts, (error, data, response) => {
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
 **guid** | **String**| Id used to get the ProjectRecurringFeeRule. | 
 **includeInactive** | **Boolean**| Indicates the rule should be returned even if it is not active. Default is false. | [optional] [default to false]

### Return type

[**ProjectRecurringFeeRuleOutputModel**](ProjectRecurringFeeRuleOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectRecurringFeeRulesGetProjectRecurringFeeRules

> [ProjectRecurringFeeRuleOutputModel] projectRecurringFeeRulesGetProjectRecurringFeeRules(opts)

Get the recurring fee rules.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FeesReadApi();
let opts = {
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'productType': new SeveraPublicRestApiDocumentation.ProductType(), // ProductType | projectRecurringFeeRule's product type. if given, it filters the projectRecurringFeeRules by the given type.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get recurring fee rules that have been added or changed after this date time (greater or equal).
};
apiInstance.projectRecurringFeeRulesGetProjectRecurringFeeRules(opts, (error, data, response) => {
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
 **productType** | [**ProductType**](.md)| projectRecurringFeeRule&#39;s product type. if given, it filters the projectRecurringFeeRules by the given type. | [optional] 
 **changedSince** | **Date**| Optional: Get recurring fee rules that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[ProjectRecurringFeeRuleOutputModel]**](ProjectRecurringFeeRuleOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectRecurringFeeRulesGetProjectRecurringFeeRulesForProject

> [ProjectRecurringFeeRuleOutputModel] projectRecurringFeeRulesGetProjectRecurringFeeRulesForProject(projectGuid, opts)

Get all the Recurring Fee Rules for a project

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

let apiInstance = new SeveraPublicRestApiDocumentation.FeesReadApi();
let projectGuid = "projectGuid_example"; // String | ID of the project to get the recurring fee rules.
let opts = {
  'productType': new SeveraPublicRestApiDocumentation.ProductType(), // ProductType | projectRecurringFeeRule's product type. if given, it filters the projectRecurringFeeRules by the given type.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'isBillablePeriodInFuture': true, // Boolean | Optional. Filter the project recurring fee rules. If true/false, only the ones that will be billable in the future are returned. If null, all are returned. Default is false.
  'billableTimePeriod': new SeveraPublicRestApiDocumentation.BillablePeriod() // BillablePeriod | the time period for any uninvoiced recurring rules.
};
apiInstance.projectRecurringFeeRulesGetProjectRecurringFeeRulesForProject(projectGuid, opts, (error, data, response) => {
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
 **projectGuid** | **String**| ID of the project to get the recurring fee rules. | 
 **productType** | [**ProductType**](.md)| projectRecurringFeeRule&#39;s product type. if given, it filters the projectRecurringFeeRules by the given type. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **isBillablePeriodInFuture** | **Boolean**| Optional. Filter the project recurring fee rules. If true/false, only the ones that will be billable in the future are returned. If null, all are returned. Default is false. | [optional] 
 **billableTimePeriod** | [**BillablePeriod**](.md)| the time period for any uninvoiced recurring rules. | [optional] 

### Return type

[**[ProjectRecurringFeeRuleOutputModel]**](ProjectRecurringFeeRuleOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

