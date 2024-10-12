# AvazaApiDocumentation.CompanyApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyGet**](CompanyApi.md#companyGet) | **GET** /api/Company | Gets list of Companies
[**companyGetByID**](CompanyApi.md#companyGetByID) | **GET** /api/Company/{id} | Gets Company by Company ID
[**companyLookup**](CompanyApi.md#companyLookup) | **GET** /api/Company/Lookup | Gets minimal list of Companies.
[**companyPost**](CompanyApi.md#companyPost) | **POST** /api/Company | Create a Company
[**companyPut**](CompanyApi.md#companyPut) | **PUT** /api/Company | Update a Company record.



## companyGet

> CompanyList companyGet(opts)

Gets list of Companies

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.CompanyApi();
let opts = {
  'updatedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'pageSize': 56, // Number | Number of results per page
  'pageNumber': 56, // Number | 1 based page number to retrieve
  'sort': "sort_example" // String | (optional) Supply one of: \"DateUpdated\", \"DateCreated\", \"CompanyName\",\"DateUpdated desc\",\"DateCreated desc\", \"CompanyName desc\"
};
apiInstance.companyGet(opts, (error, data, response) => {
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
 **updatedAfter** | **Date**|  | [optional] 
 **pageSize** | **Number**| Number of results per page | [optional] 
 **pageNumber** | **Number**| 1 based page number to retrieve | [optional] 
 **sort** | **String**| (optional) Supply one of: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;CompanyName\&quot;,\&quot;DateUpdated desc\&quot;,\&quot;DateCreated desc\&quot;, \&quot;CompanyName desc\&quot; | [optional] 

### Return type

[**CompanyList**](CompanyList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## companyGetByID

> Company companyGetByID(id)

Gets Company by Company ID

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.CompanyApi();
let id = 789; // Number | Company ID Number
apiInstance.companyGetByID(id, (error, data, response) => {
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
 **id** | **Number**| Company ID Number | 

### Return type

[**Company**](Company.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## companyLookup

> CompanyDropdownList companyLookup(opts)

Gets minimal list of Companies.

Certain roles see a restricted set of companies based on their project memberships

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.CompanyApi();
let opts = {
  'pageSize': 56, // Number | Number of items per page (max 1000)
  'pageNumber': 56, // Number | Page to display. Starts from 1.
  'search': "search_example" // String | Search string to match against Company title
};
apiInstance.companyLookup(opts, (error, data, response) => {
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
 **pageSize** | **Number**| Number of items per page (max 1000) | [optional] 
 **pageNumber** | **Number**| Page to display. Starts from 1. | [optional] 
 **search** | **String**| Search string to match against Company title | [optional] 

### Return type

[**CompanyDropdownList**](CompanyDropdownList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## companyPost

> Company companyPost(model)

Create a Company

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.CompanyApi();
let model = new AvazaApiDocumentation.NewCompany(); // NewCompany | 
apiInstance.companyPost(model, (error, data, response) => {
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
 **model** | [**NewCompany**](NewCompany.md)|  | 

### Return type

[**Company**](Company.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## companyPut

> Company companyPut(model)

Update a Company record.

Requires CompanyID and a list of field names to update. The FieldsToUpdate field accepts a string array containing field names that should be updated.

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.CompanyApi();
let model = new AvazaApiDocumentation.UpdateCompany(); // UpdateCompany | 
apiInstance.companyPut(model, (error, data, response) => {
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
 **model** | [**UpdateCompany**](UpdateCompany.md)|  | 

### Return type

[**Company**](Company.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

