# CmsDomains.DomainsApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCmsV3DomainsDomainIdGetById**](DomainsApi.md#getCmsV3DomainsDomainIdGetById) | **GET** /cms/v3/domains/{domainId} | Get a single domain
[**getCmsV3DomainsGetPage**](DomainsApi.md#getCmsV3DomainsGetPage) | **GET** /cms/v3/domains/ | Get current domains



## getCmsV3DomainsDomainIdGetById

> Domain getCmsV3DomainsDomainIdGetById(domainId)

Get a single domain

Returns a single domains with the id specified.

### Example

```javascript
import CmsDomains from 'cms_domains';
let defaultClient = CmsDomains.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2_legacy
let oauth2_legacy = defaultClient.authentications['oauth2_legacy'];
oauth2_legacy.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: private_apps_legacy
let private_apps_legacy = defaultClient.authentications['private_apps_legacy'];
private_apps_legacy.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_apps_legacy.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: private_apps
let private_apps = defaultClient.authentications['private_apps'];
private_apps.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_apps.apiKeyPrefix = 'Token';

let apiInstance = new CmsDomains.DomainsApi();
let domainId = "domainId_example"; // String | The unique ID of the domain.
apiInstance.getCmsV3DomainsDomainIdGetById(domainId, (error, data, response) => {
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
 **domainId** | **String**| The unique ID of the domain. | 

### Return type

[**Domain**](Domain.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy), [oauth2](../README.md#oauth2), [private_apps](../README.md#private_apps)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## getCmsV3DomainsGetPage

> CollectionResponseWithTotalDomainForwardPaging getCmsV3DomainsGetPage(opts)

Get current domains

Returns all existing domains that have been created. Results can be limited and filtered by creation or updated date.

### Example

```javascript
import CmsDomains from 'cms_domains';
let defaultClient = CmsDomains.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2_legacy
let oauth2_legacy = defaultClient.authentications['oauth2_legacy'];
oauth2_legacy.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: private_apps_legacy
let private_apps_legacy = defaultClient.authentications['private_apps_legacy'];
private_apps_legacy.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_apps_legacy.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: private_apps
let private_apps = defaultClient.authentications['private_apps'];
private_apps.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_apps.apiKeyPrefix = 'Token';

let apiInstance = new CmsDomains.DomainsApi();
let opts = {
  'createdAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Only return domains created at this date.
  'createdAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Only return domains created after this date.
  'createdBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Only return domains created before this date.
  'updatedAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Only return domains updated at this date.
  'updatedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Only return domains updated after this date.
  'updatedBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Only return domains updated before this date.
  'sort': ["null"], // [String] | 
  'after': "after_example", // String | The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
  'limit': 56, // Number | Maximum number of results per page.
  'archived': true // Boolean | Whether to return only results that have been archived.
};
apiInstance.getCmsV3DomainsGetPage(opts, (error, data, response) => {
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
 **createdAt** | **Date**| Only return domains created at this date. | [optional] 
 **createdAfter** | **Date**| Only return domains created after this date. | [optional] 
 **createdBefore** | **Date**| Only return domains created before this date. | [optional] 
 **updatedAt** | **Date**| Only return domains updated at this date. | [optional] 
 **updatedAfter** | **Date**| Only return domains updated after this date. | [optional] 
 **updatedBefore** | **Date**| Only return domains updated before this date. | [optional] 
 **sort** | [**[String]**](String.md)|  | [optional] 
 **after** | **String**| The paging cursor token of the last successfully read resource will be returned as the &#x60;paging.next.after&#x60; JSON property of a paged response containing more results. | [optional] 
 **limit** | **Number**| Maximum number of results per page. | [optional] 
 **archived** | **Boolean**| Whether to return only results that have been archived. | [optional] 

### Return type

[**CollectionResponseWithTotalDomainForwardPaging**](CollectionResponseWithTotalDomainForwardPaging.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy), [oauth2](../README.md#oauth2), [private_apps](../README.md#private_apps)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*

