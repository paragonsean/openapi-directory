# CompanyApi.DefaultApi

All URIs are relative to *https://api.roaring.io/company/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyBoardMembersGet**](DefaultApi.md#companyBoardMembersGet) | **GET** /company-board-members | 
[**companyBoardMembersPost**](DefaultApi.md#companyBoardMembersPost) | **POST** /company-board-members | 
[**companyCreditDecisionGet**](DefaultApi.md#companyCreditDecisionGet) | **GET** /company-credit-decision | 
[**companyEconomyOverviewGet**](DefaultApi.md#companyEconomyOverviewGet) | **GET** /company-economy-overview | 
[**companyEconomyOverviewPost**](DefaultApi.md#companyEconomyOverviewPost) | **POST** /company-economy-overview | 
[**companyEventPost**](DefaultApi.md#companyEventPost) | **POST** /company-event | 
[**companyOverviewGet**](DefaultApi.md#companyOverviewGet) | **GET** /company-overview | 
[**companyOverviewPost**](DefaultApi.md#companyOverviewPost) | **POST** /company-overview | 
[**companySignatoryGet**](DefaultApi.md#companySignatoryGet) | **GET** /company-signatory | 
[**companySignatoryPost**](DefaultApi.md#companySignatoryPost) | **POST** /company-signatory | 
[**companySimpleSearchGet**](DefaultApi.md#companySimpleSearchGet) | **GET** /company-simple-search | 



## companyBoardMembersGet

> CompanyBoardMembersResult companyBoardMembersGet(countryCode, companyId)



### Example

```javascript
import CompanyApi from 'company_api';

let apiInstance = new CompanyApi.DefaultApi();
let countryCode = "countryCode_example"; // String | Country code for the company
let companyId = "companyId_example"; // String | Company identification for the company
apiInstance.companyBoardMembersGet(countryCode, companyId, (error, data, response) => {
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
 **countryCode** | **String**| Country code for the company | 
 **companyId** | **String**| Company identification for the company | 

### Return type

[**CompanyBoardMembersResult**](CompanyBoardMembersResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## companyBoardMembersPost

> CompanyBoardMembersMulti companyBoardMembersPost(countryCode, body)



### Example

```javascript
import CompanyApi from 'company_api';

let apiInstance = new CompanyApi.DefaultApi();
let countryCode = "countryCode_example"; // String | Country code for the company
let body = new CompanyApi.CompanyLookupRequestBody(); // CompanyLookupRequestBody | Request body with company identifiers to lookup
apiInstance.companyBoardMembersPost(countryCode, body, (error, data, response) => {
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
 **countryCode** | **String**| Country code for the company | 
 **body** | [**CompanyLookupRequestBody**](CompanyLookupRequestBody.md)| Request body with company identifiers to lookup | 

### Return type

[**CompanyBoardMembersMulti**](CompanyBoardMembersMulti.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## companyCreditDecisionGet

> CompanyCreditDecisionResult companyCreditDecisionGet(countryCode, companyId, template)



### Example

```javascript
import CompanyApi from 'company_api';

let apiInstance = new CompanyApi.DefaultApi();
let countryCode = "countryCode_example"; // String | Country code for the company
let companyId = "companyId_example"; // String | Company identification for the company
let template = "template_example"; // String | Template for credit decision
apiInstance.companyCreditDecisionGet(countryCode, companyId, template, (error, data, response) => {
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
 **countryCode** | **String**| Country code for the company | 
 **companyId** | **String**| Company identification for the company | 
 **template** | **String**| Template for credit decision | 

### Return type

[**CompanyCreditDecisionResult**](CompanyCreditDecisionResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## companyEconomyOverviewGet

> CompanyEconomyOverviewResult companyEconomyOverviewGet(countryCode, companyId)



### Example

```javascript
import CompanyApi from 'company_api';

let apiInstance = new CompanyApi.DefaultApi();
let countryCode = "countryCode_example"; // String | Country code for the company
let companyId = "companyId_example"; // String | Company identification for the company
apiInstance.companyEconomyOverviewGet(countryCode, companyId, (error, data, response) => {
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
 **countryCode** | **String**| Country code for the company | 
 **companyId** | **String**| Company identification for the company | 

### Return type

[**CompanyEconomyOverviewResult**](CompanyEconomyOverviewResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## companyEconomyOverviewPost

> CompanyEconomyOverviewMulti companyEconomyOverviewPost(countryCode, body)



### Example

```javascript
import CompanyApi from 'company_api';

let apiInstance = new CompanyApi.DefaultApi();
let countryCode = "countryCode_example"; // String | Country code for the company
let body = new CompanyApi.CompanyLookupRequestBody(); // CompanyLookupRequestBody | Request body with company identifiers to lookup
apiInstance.companyEconomyOverviewPost(countryCode, body, (error, data, response) => {
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
 **countryCode** | **String**| Country code for the company | 
 **body** | [**CompanyLookupRequestBody**](CompanyLookupRequestBody.md)| Request body with company identifiers to lookup | 

### Return type

[**CompanyEconomyOverviewMulti**](CompanyEconomyOverviewMulti.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## companyEventPost

> CompanyEventResult companyEventPost(countryCode, body)



### Example

```javascript
import CompanyApi from 'company_api';

let apiInstance = new CompanyApi.DefaultApi();
let countryCode = "countryCode_example"; // String | Country code for the company
let body = new CompanyApi.CompanyEventRequestBody(); // CompanyEventRequestBody | Request body with company identifiers to lookup
apiInstance.companyEventPost(countryCode, body, (error, data, response) => {
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
 **countryCode** | **String**| Country code for the company | 
 **body** | [**CompanyEventRequestBody**](CompanyEventRequestBody.md)| Request body with company identifiers to lookup | 

### Return type

[**CompanyEventResult**](CompanyEventResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## companyOverviewGet

> CompanyOverviewResult companyOverviewGet(countryCode, companyId)



### Example

```javascript
import CompanyApi from 'company_api';

let apiInstance = new CompanyApi.DefaultApi();
let countryCode = "countryCode_example"; // String | Country code for the company
let companyId = "companyId_example"; // String | Company identification for the company
apiInstance.companyOverviewGet(countryCode, companyId, (error, data, response) => {
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
 **countryCode** | **String**| Country code for the company | 
 **companyId** | **String**| Company identification for the company | 

### Return type

[**CompanyOverviewResult**](CompanyOverviewResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## companyOverviewPost

> CompanyOverviewMulti companyOverviewPost(countryCode, body)



### Example

```javascript
import CompanyApi from 'company_api';

let apiInstance = new CompanyApi.DefaultApi();
let countryCode = "countryCode_example"; // String | Country code for the company
let body = new CompanyApi.CompanyLookupRequestBody(); // CompanyLookupRequestBody | Request body with company identifiers to lookup
apiInstance.companyOverviewPost(countryCode, body, (error, data, response) => {
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
 **countryCode** | **String**| Country code for the company | 
 **body** | [**CompanyLookupRequestBody**](CompanyLookupRequestBody.md)| Request body with company identifiers to lookup | 

### Return type

[**CompanyOverviewMulti**](CompanyOverviewMulti.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## companySignatoryGet

> CompanySignatoryResult companySignatoryGet(countryCode, companyId)



### Example

```javascript
import CompanyApi from 'company_api';

let apiInstance = new CompanyApi.DefaultApi();
let countryCode = "countryCode_example"; // String | Country code for the company
let companyId = "companyId_example"; // String | Company identification for the company
apiInstance.companySignatoryGet(countryCode, companyId, (error, data, response) => {
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
 **countryCode** | **String**| Country code for the company | 
 **companyId** | **String**| Company identification for the company | 

### Return type

[**CompanySignatoryResult**](CompanySignatoryResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## companySignatoryPost

> CompanySignatoryMulti companySignatoryPost(countryCode, body)



### Example

```javascript
import CompanyApi from 'company_api';

let apiInstance = new CompanyApi.DefaultApi();
let countryCode = "countryCode_example"; // String | Country code for the company
let body = new CompanyApi.CompanyLookupRequestBody(); // CompanyLookupRequestBody | Request body with company identifiers to lookup
apiInstance.companySignatoryPost(countryCode, body, (error, data, response) => {
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
 **countryCode** | **String**| Country code for the company | 
 **body** | [**CompanyLookupRequestBody**](CompanyLookupRequestBody.md)| Request body with company identifiers to lookup | 

### Return type

[**CompanySignatoryMulti**](CompanySignatoryMulti.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## companySimpleSearchGet

> companySimpleSearchGet(countryCode, opts)



### Example

```javascript
import CompanyApi from 'company_api';

let apiInstance = new CompanyApi.DefaultApi();
let countryCode = "countryCode_example"; // String | Country code for the company
let opts = {
  'companyName': "companyName_example", // String | Company name
  'town': "town_example" // String | Town
};
apiInstance.companySimpleSearchGet(countryCode, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countryCode** | **String**| Country code for the company | 
 **companyName** | **String**| Company name | [optional] 
 **town** | **String**| Town | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

