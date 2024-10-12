# NetlifysApiDocumentation.SiteApi

All URIs are relative to *https://api.netlify.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSite**](SiteApi.md#createSite) | **POST** /sites | 
[**createSiteInTeam**](SiteApi.md#createSiteInTeam) | **POST** /{account_slug}/sites | 
[**deleteSite**](SiteApi.md#deleteSite) | **DELETE** /sites/{site_id} | 
[**getSite**](SiteApi.md#getSite) | **GET** /sites/{site_id} | 
[**listSites**](SiteApi.md#listSites) | **GET** /sites | 
[**listSitesForAccount**](SiteApi.md#listSitesForAccount) | **GET** /{account_slug}/sites | 
[**unlinkSiteRepo**](SiteApi.md#unlinkSiteRepo) | **PUT** /sites/{site_id}/unlink_repo | 
[**updateSite**](SiteApi.md#updateSite) | **PATCH** /sites/{site_id} | 



## createSite

> Site createSite(site, opts)



**Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [createEnvVars](#tag/environmentVariables/operation/createEnvVars) to create environment variables for a site.

### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SiteApi();
let site = new NetlifysApiDocumentation.SiteSetup(); // SiteSetup | 
let opts = {
  'configureDns': true // Boolean | 
};
apiInstance.createSite(site, opts, (error, data, response) => {
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
 **site** | [**SiteSetup**](SiteSetup.md)|  | 
 **configureDns** | **Boolean**|  | [optional] 

### Return type

[**Site**](Site.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSiteInTeam

> Site createSiteInTeam(accountSlug, opts)



**Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [createEnvVars](#tag/environmentVariables/operation/createEnvVars) to create environment variables for a site.

### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SiteApi();
let accountSlug = "accountSlug_example"; // String | 
let opts = {
  'configureDns': true, // Boolean | 
  'site': new NetlifysApiDocumentation.SiteSetup() // SiteSetup | 
};
apiInstance.createSiteInTeam(accountSlug, opts, (error, data, response) => {
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
 **accountSlug** | **String**|  | 
 **configureDns** | **Boolean**|  | [optional] 
 **site** | [**SiteSetup**](SiteSetup.md)|  | [optional] 

### Return type

[**Site**](Site.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSite

> deleteSite(siteId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SiteApi();
let siteId = "siteId_example"; // String | 
apiInstance.deleteSite(siteId, (error, data, response) => {
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
 **siteId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSite

> Site getSite(siteId)



**Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [getEnvVars](#tag/environmentVariables/operation/getEnvVars) to retrieve site environment variables.

### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SiteApi();
let siteId = "siteId_example"; // String | 
apiInstance.getSite(siteId, (error, data, response) => {
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
 **siteId** | **String**|  | 

### Return type

[**Site**](Site.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSites

> [Site] listSites(opts)



**Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [getEnvVars](#tag/environmentVariables/operation/getEnvVars) to retrieve site environment variables.

### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SiteApi();
let opts = {
  'name': "name_example", // String | 
  'filter': "filter_example", // String | 
  'page': 56, // Number | 
  'perPage': 56 // Number | 
};
apiInstance.listSites(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 
 **filter** | **String**|  | [optional] 
 **page** | **Number**|  | [optional] 
 **perPage** | **Number**|  | [optional] 

### Return type

[**[Site]**](Site.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSitesForAccount

> [Site] listSitesForAccount(accountSlug, opts)



**Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [getEnvVars](#tag/environmentVariables/operation/getEnvVars) to retrieve site environment variables.

### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SiteApi();
let accountSlug = "accountSlug_example"; // String | 
let opts = {
  'name': "name_example", // String | 
  'page': 56, // Number | 
  'perPage': 56 // Number | 
};
apiInstance.listSitesForAccount(accountSlug, opts, (error, data, response) => {
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
 **accountSlug** | **String**|  | 
 **name** | **String**|  | [optional] 
 **page** | **Number**|  | [optional] 
 **perPage** | **Number**|  | [optional] 

### Return type

[**[Site]**](Site.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## unlinkSiteRepo

> Site unlinkSiteRepo(siteId)



[Beta] Unlinks the repo from the site.  This action will also: - Delete associated deploy keys - Delete outgoing webhooks for the repo - Delete the site&#39;s build hooks

### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SiteApi();
let siteId = "siteId_example"; // String | 
apiInstance.unlinkSiteRepo(siteId, (error, data, response) => {
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
 **siteId** | **String**|  | 

### Return type

[**Site**](Site.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSite

> Site updateSite(siteId, site)



**Note:** Environment variable keys and values will soon be moved from &#x60;build_settings.env&#x60; and &#x60;repo.env&#x60; to a new endpoint. Please use [updateEnvVar](#tag/environmentVariables/operation/updateEnvVar) to update a site&#39;s environment variables.

### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SiteApi();
let siteId = "siteId_example"; // String | 
let site = new NetlifysApiDocumentation.SiteSetup(); // SiteSetup | 
apiInstance.updateSite(siteId, site, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **site** | [**SiteSetup**](SiteSetup.md)|  | 

### Return type

[**Site**](Site.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

