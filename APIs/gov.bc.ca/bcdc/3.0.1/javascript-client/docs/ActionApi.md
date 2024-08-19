# BcDataCatalogueApi.ActionApi

All URIs are relative to *https://catalogue.data.gov.bc.ca/api/3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actionOrganizationActivityListGet**](ActionApi.md#actionOrganizationActivityListGet) | **GET** /action/organization_activity_list | Get the activity stream of an organization
[**actionOrganizationActivityListHtmlGet**](ActionApi.md#actionOrganizationActivityListHtmlGet) | **GET** /action/organization_activity_list_html | Get the activity stream of an organization, HTML format
[**actionOrganizationAutocompleteGet**](ActionApi.md#actionOrganizationAutocompleteGet) | **GET** /action/organization_autocomplete | Get names of organizations that match a query string
[**actionOrganizationFollowerCountGet**](ActionApi.md#actionOrganizationFollowerCountGet) | **GET** /action/organization_follower_count | Get number of followers of an organization
[**actionOrganizationFollowerListGet**](ActionApi.md#actionOrganizationFollowerListGet) | **GET** /action/organization_follower_list | Get users following an organization
[**actionOrganizationListForUserGet**](ActionApi.md#actionOrganizationListForUserGet) | **GET** /action/organization_list_for_user | Get organizations that a user has a given permission for
[**actionOrganizationListGet**](ActionApi.md#actionOrganizationListGet) | **GET** /action/organization_list | Get names of all organizations
[**actionOrganizationRevisionListGet**](ActionApi.md#actionOrganizationRevisionListGet) | **GET** /action/organization_revision_list | Get organization revisions
[**actionOrganizationShowGet**](ActionApi.md#actionOrganizationShowGet) | **GET** /action/organization_show | Get details of a specific organization
[**actionPackageActivityListGet**](ActionApi.md#actionPackageActivityListGet) | **GET** /action/package_activity_list | Get the activity stream of a package (dataset)
[**actionPackageActivityListHtmlGet**](ActionApi.md#actionPackageActivityListHtmlGet) | **GET** /action/package_activity_list_html | Get the activity stream of a package (dataset), HTML format
[**actionPackageAutocompleteGet**](ActionApi.md#actionPackageAutocompleteGet) | **GET** /action/package_autocomplete | Find packages (datasets) matching a query
[**actionPackageListGet**](ActionApi.md#actionPackageListGet) | **GET** /action/package_list | Get a list of all packages (datasets)
[**actionPackageRelationshipsListGet**](ActionApi.md#actionPackageRelationshipsListGet) | **GET** /action/package_relationships_list | Get package (dataset) relationships
[**actionPackageRevisionListGet**](ActionApi.md#actionPackageRevisionListGet) | **GET** /action/package_revision_list | Get list of revisions for a package (dataset)
[**actionPackageSearchGet**](ActionApi.md#actionPackageSearchGet) | **GET** /action/package_search | Find packages (datasets) matching query terms
[**actionPackageShowGet**](ActionApi.md#actionPackageShowGet) | **GET** /action/package_show | Get metadata about one specific package (dataset)
[**actionRelatedListGet**](ActionApi.md#actionRelatedListGet) | **GET** /action/related_list | Gets items related to a package (dataset)
[**actionResourceSearchGet**](ActionApi.md#actionResourceSearchGet) | **GET** /action/resource_search | Find resources
[**actionResourceShowGet**](ActionApi.md#actionResourceShowGet) | **GET** /action/resource_show | Get metadata for a specific resource
[**actionStatusShowGet**](ActionApi.md#actionStatusShowGet) | **GET** /action/status_show | Get the site status
[**actionTagListGet**](ActionApi.md#actionTagListGet) | **GET** /action/tag_list | Get a list of tags



## actionOrganizationActivityListGet

> actionOrganizationActivityListGet(opts)

Get the activity stream of an organization

Return an organization&#39;s activity stream

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
let opts = {
  'id': "'ministry-of-agriculture'" // String | The id or name of the organization
};
apiInstance.actionOrganizationActivityListGet(opts, (error, data, response) => {
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
 **id** | **String**| The id or name of the organization | [optional] [default to &#39;ministry-of-agriculture&#39;]

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## actionOrganizationActivityListHtmlGet

> actionOrganizationActivityListHtmlGet(opts)

Get the activity stream of an organization, HTML format

Return an organization&#39;s activity stream as HTML

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
let opts = {
  'id': "'ministry-of-agriculture'" // String | The id or name of the organization
};
apiInstance.actionOrganizationActivityListHtmlGet(opts, (error, data, response) => {
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
 **id** | **String**| The id or name of the organization | [optional] [default to &#39;ministry-of-agriculture&#39;]

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## actionOrganizationAutocompleteGet

> actionOrganizationAutocompleteGet(opts)

Get names of organizations that match a query string

Return a list of organization names that contain a string

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
let opts = {
  'q': "'ministry'", // String | The string to search for
  'limit': 20 // Number | The maximum number of organizations to return (optional)
};
apiInstance.actionOrganizationAutocompleteGet(opts, (error, data, response) => {
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
 **q** | **String**| The string to search for | [optional] [default to &#39;ministry&#39;]
 **limit** | **Number**| The maximum number of organizations to return (optional) | [optional] [default to 20]

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## actionOrganizationFollowerCountGet

> actionOrganizationFollowerCountGet(opts)

Get number of followers of an organization

Return the number of followers of an organization

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
let opts = {
  'id': "'ministry-of-agriculture'" // String | The id or name of the organization
};
apiInstance.actionOrganizationFollowerCountGet(opts, (error, data, response) => {
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
 **id** | **String**| The id or name of the organization | [optional] [default to &#39;ministry-of-agriculture&#39;]

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## actionOrganizationFollowerListGet

> actionOrganizationFollowerListGet(opts)

Get users following an organization

Return a list of users that are following a given organization

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
let opts = {
  'id': "'ministry-of-agriculture'" // String | The id or name of the organization
};
apiInstance.actionOrganizationFollowerListGet(opts, (error, data, response) => {
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
 **id** | **String**| The id or name of the organization | [optional] [default to &#39;ministry-of-agriculture&#39;]

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## actionOrganizationListForUserGet

> actionOrganizationListForUserGet(opts)

Get organizations that a user has a given permission for

Return the organizations that the user has a given permission for

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
let opts = {
  'permission': "'\"edit_group\"'" // String | The permission the user has against the returned organization
};
apiInstance.actionOrganizationListForUserGet(opts, (error, data, response) => {
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
 **permission** | **String**| The permission the user has against the returned organization | [optional] [default to &#39;&quot;edit_group&quot;&#39;]

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## actionOrganizationListGet

> actionOrganizationListGet(opts)

Get names of all organizations

Returns the names of all indexed organizations

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
let opts = {
  'offset': 0, // Number | The offset (index) of the first organizations to return
  'limit': 100 // Number | The number of organizations to be returned per page
};
apiInstance.actionOrganizationListGet(opts, (error, data, response) => {
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
 **offset** | **Number**| The offset (index) of the first organizations to return | [optional] [default to 0]
 **limit** | **Number**| The number of organizations to be returned per page | [optional] [default to 100]

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## actionOrganizationRevisionListGet

> actionOrganizationRevisionListGet(opts)

Get organization revisions

Return an organization&#39;s revisions

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
let opts = {
  'id': "'ministry-of-agriculture'" // String | The name or id of the organization
};
apiInstance.actionOrganizationRevisionListGet(opts, (error, data, response) => {
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
 **id** | **String**| The name or id of the organization | [optional] [default to &#39;ministry-of-agriculture&#39;]

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## actionOrganizationShowGet

> actionOrganizationShowGet(opts)

Get details of a specific organization

Return the details of an organization

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
let opts = {
  'id': "'ministry-of-agriculture'", // String | The id or name of the organization
  'includeDatasets': true // Boolean | include a list of the organization's datasets
};
apiInstance.actionOrganizationShowGet(opts, (error, data, response) => {
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
 **id** | **String**| The id or name of the organization | [optional] [default to &#39;ministry-of-agriculture&#39;]
 **includeDatasets** | **Boolean**| include a list of the organization&#39;s datasets | [optional] [default to true]

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## actionPackageActivityListGet

> actionPackageActivityListGet(opts)

Get the activity stream of a package (dataset)

Returns a package&#39;s activity stream

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
let opts = {
  'id': "'grizzly-bear-population-units'", // String | The id or name of the package
  'offset': 0, // Number | Where to start getting activity items from
  'limit': 31 // Number | The maximum number of activities to return
};
apiInstance.actionPackageActivityListGet(opts, (error, data, response) => {
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
 **id** | **String**| The id or name of the package | [optional] [default to &#39;grizzly-bear-population-units&#39;]
 **offset** | **Number**| Where to start getting activity items from | [optional] [default to 0]
 **limit** | **Number**| The maximum number of activities to return | [optional] [default to 31]

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## actionPackageActivityListHtmlGet

> actionPackageActivityListHtmlGet(opts)

Get the activity stream of a package (dataset), HTML format

The activity stream is rendered as a snippet of HTML meant to be included in an HTML pag, i.e it doesn&#39;t have any header or footer.

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
let opts = {
  'id': "'grizzly-bear-population-units'", // String | The id or name of the package
  'offset': 0, // Number | Where to start getting activity items from
  'limit': 31 // Number | The maximum number of activities to return
};
apiInstance.actionPackageActivityListHtmlGet(opts, (error, data, response) => {
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
 **id** | **String**| The id or name of the package | [optional] [default to &#39;grizzly-bear-population-units&#39;]
 **offset** | **Number**| Where to start getting activity items from | [optional] [default to 0]
 **limit** | **Number**| The maximum number of activities to return | [optional] [default to 31]

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## actionPackageAutocompleteGet

> actionPackageAutocompleteGet(opts)

Find packages (datasets) matching a query

Return a list of datasets that match a string

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
let opts = {
  'q': "'\"Okanagan Lake\"'", // String | The string to query
  'limit': 10 // Number | The maximum number of resource formats to return
};
apiInstance.actionPackageAutocompleteGet(opts, (error, data, response) => {
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
 **q** | **String**| The string to query | [optional] [default to &#39;&quot;Okanagan Lake&quot;&#39;]
 **limit** | **Number**| The maximum number of resource formats to return | [optional] [default to 10]

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## actionPackageListGet

> actionPackageListGet(opts)

Get a list of all packages (datasets)

Returns the names of all indexed packages (datasets)

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
let opts = {
  'offset': 0, // Number | The offset (index) of the first package to return
  'limit': 100 // Number | The number of packages to be returned per page
};
apiInstance.actionPackageListGet(opts, (error, data, response) => {
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
 **offset** | **Number**| The offset (index) of the first package to return | [optional] [default to 0]
 **limit** | **Number**| The number of packages to be returned per page | [optional] [default to 100]

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## actionPackageRelationshipsListGet

> actionPackageRelationshipsListGet(opts)

Get package (dataset) relationships

Return a dataset&#39;s relationships

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
let opts = {
  'id': "'grizzly-bear-population-units'", // String | The id or name of the first package
  'id2': "'important-fossil-areas'", // String | The id or name of the second package
  'rel': "rel_example" // String | relationship as string
};
apiInstance.actionPackageRelationshipsListGet(opts, (error, data, response) => {
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
 **id** | **String**| The id or name of the first package | [optional] [default to &#39;grizzly-bear-population-units&#39;]
 **id2** | **String**| The id or name of the second package | [optional] [default to &#39;important-fossil-areas&#39;]
 **rel** | **String**| relationship as string | [optional] 

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## actionPackageRevisionListGet

> actionPackageRevisionListGet(opts)

Get list of revisions for a package (dataset)

Return a dataset&#39;s revision as a list of dictionaries

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
let opts = {
  'id': "'grizzly-bear-population-units'" // String | The id or name of the dataset
};
apiInstance.actionPackageRevisionListGet(opts, (error, data, response) => {
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
 **id** | **String**| The id or name of the dataset | [optional] [default to &#39;grizzly-bear-population-units&#39;]

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## actionPackageSearchGet

> actionPackageSearchGet(opts)

Find packages (datasets) matching query terms

Searches for packages (datasets) matching the specified query terms

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
let opts = {
  'q': "'\"Okanagan Lake\"'" // String | A query string
};
apiInstance.actionPackageSearchGet(opts, (error, data, response) => {
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
 **q** | **String**| A query string | [optional] [default to &#39;&quot;Okanagan Lake&quot;&#39;]

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## actionPackageShowGet

> actionPackageShowGet(opts)

Get metadata about one specific package (dataset)

Returns metadata about the package (dataset) corresponding to the specified unique name

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
let opts = {
  'id': "'grizzly-bear-population-units'" // String | The package name
};
apiInstance.actionPackageShowGet(opts, (error, data, response) => {
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
 **id** | **String**| The package name | [optional] [default to &#39;grizzly-bear-population-units&#39;]

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## actionRelatedListGet

> actionRelatedListGet(opts)

Gets items related to a package (dataset)

Returns a dataset&#39;s related items.

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
let opts = {
  'id': "id_example", // String | id or name of the dataset (optional)
  'dataset': "dataset_example", // String | Dataset dictionary of the dataset (optional)
  'typeFilter': "typeFilter_example", // String | The type of related item to show (optional)
  'sort': "sort_example", // String | The order to sort the related items in
  'featured': "featured_example" // String | whether or not to restrict the results to only featured items
};
apiInstance.actionRelatedListGet(opts, (error, data, response) => {
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
 **id** | **String**| id or name of the dataset (optional) | [optional] 
 **dataset** | **String**| Dataset dictionary of the dataset (optional) | [optional] 
 **typeFilter** | **String**| The type of related item to show (optional) | [optional] 
 **sort** | **String**| The order to sort the related items in | [optional] 
 **featured** | **String**| whether or not to restrict the results to only featured items | [optional] 

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## actionResourceSearchGet

> actionResourceSearchGet(opts)

Find resources

Returns a dictionary with two fields &#x60;&#x60;count&#x60;&#x60; and &#x60;&#x60;results&#x60;&#x60;.             The &#x60;&#x60;count&#x60;&#x60; field contains the total number of Resources                found without the limit or query parameters having an effect.             The &#x60;&#x60;results&#x60;&#x60; field is a list of dictized Resource objects.             The query parameter is a required field. It is a string in                the form &#x60;&#x60;{field}:{term}&#x60;&#x60; or a list of strings, each of the             same form. Within each string, &#x60;&#x60;{field}&#x60;&#x60; is a field or extra             field on the Resource domain object.

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
let opts = {
  'query': "'format:csv'", // String | The search criteria string or list of strings of the form ``{field}:{term1}``
  'fields': "fields_example", // String | Depreciated
  'orderBy': "orderBy_example", // String | A field on the resource model that orders the results
  'offset': 0, // Number | Apply an offset to the query
  'limit': 0 // Number | Apply a limit to the query
};
apiInstance.actionResourceSearchGet(opts, (error, data, response) => {
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
 **query** | **String**| The search criteria string or list of strings of the form &#x60;&#x60;{field}:{term1}&#x60;&#x60; | [optional] [default to &#39;format:csv&#39;]
 **fields** | **String**| Depreciated | [optional] 
 **orderBy** | **String**| A field on the resource model that orders the results | [optional] 
 **offset** | **Number**| Apply an offset to the query | [optional] [default to 0]
 **limit** | **Number**| Apply a limit to the query | [optional] [default to 0]

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## actionResourceShowGet

> actionResourceShowGet(opts)

Get metadata for a specific resource

Return the metadata of a resource

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
let opts = {
  'id': "'e6c8bb1d-3726-418b-9b7e-1d97a9bbb817'", // String | The id of the resource
  'includeTracking': false // Boolean | Add tracking information to dataset
};
apiInstance.actionResourceShowGet(opts, (error, data, response) => {
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
 **id** | **String**| The id of the resource | [optional] [default to &#39;e6c8bb1d-3726-418b-9b7e-1d97a9bbb817&#39;]
 **includeTracking** | **Boolean**| Add tracking information to dataset | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## actionStatusShowGet

> actionStatusShowGet()

Get the site status

Returns the site status

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
apiInstance.actionStatusShowGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## actionTagListGet

> actionTagListGet(opts)

Get a list of tags

Returns the names of all indexed tags

### Example

```javascript
import BcDataCatalogueApi from 'bc_data_catalogue_api';
let defaultClient = BcDataCatalogueApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: githubAccessCode
let githubAccessCode = defaultClient.authentications['githubAccessCode'];
githubAccessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BcDataCatalogueApi.ActionApi();
let opts = {
  'offset': 0, // Number | The offset (index) of the first tag to return
  'limit': 100 // Number | The number of tags to be returned per page
};
apiInstance.actionTagListGet(opts, (error, data, response) => {
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
 **offset** | **Number**| The offset (index) of the first tag to return | [optional] [default to 0]
 **limit** | **Number**| The number of tags to be returned per page | [optional] [default to 100]

### Return type

null (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey), [githubAccessCode](../README.md#githubAccessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

