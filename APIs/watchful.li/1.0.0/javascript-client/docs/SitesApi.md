# WatchfulLi.SitesApi

All URIs are relative to *https://watchful.li/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addSiteToBackupQueue**](SitesApi.md#addSiteToBackupQueue) | **POST** /sites/{id}/backupnow | Add the site to the backup queue
[**createAudits**](SitesApi.md#createAudits) | **POST** /sites/{id}/audits | Create an audit for the site
[**createLog**](SitesApi.md#createLog) | **POST** /sites/{id}/logs | Create a custom log for a specific website
[**createSite**](SitesApi.md#createSite) | **POST** /sites | Create a site
[**deleteMonitor**](SitesApi.md#deleteMonitor) | **DELETE** /sites/{id}/monitor | Delete uptime monitor
[**getBackupProfiles**](SitesApi.md#getBackupProfiles) | **GET** /sites/{id}/backupprofiles | Return backup profile
[**getListBackups**](SitesApi.md#getListBackups) | **GET** /sites/{id}/backups | List of latest backups
[**getSiteAudits**](SitesApi.md#getSiteAudits) | **GET** /sites/{id}/audits | Return audits for a specific website
[**getSiteById**](SitesApi.md#getSiteById) | **GET** /sites/{id} | Find sites by ID
[**getSites**](SitesApi.md#getSites) | **GET** /sites | Get a list of Sites
[**getUptime**](SitesApi.md#getUptime) | **GET** /sites/{id}/uptime | Return uptime data
[**installExtension**](SitesApi.md#installExtension) | **POST** /sites/{id}/extensions | Install extension
[**postMonitor**](SitesApi.md#postMonitor) | **POST** /sites/{id}/monitor | Post uptime monitor
[**postTags**](SitesApi.md#postTags) | **POST** /sites/{id}/tags | Add tags for a specific website
[**scanner**](SitesApi.md#scanner) | **GET** /sites/{id}/scanner | Scan the site for malware
[**seoAnalyze**](SitesApi.md#seoAnalyze) | **GET** /sites/{id}/seo | SEO analyze for a page
[**sitesIdDelete**](SitesApi.md#sitesIdDelete) | **DELETE** /sites/{id} | Delete a specific Site
[**sitesIdExtensionsGet**](SitesApi.md#sitesIdExtensionsGet) | **GET** /sites/{id}/extensions | Get extensions for a site
[**sitesIdLogsGet**](SitesApi.md#sitesIdLogsGet) | **GET** /sites/{id}/logs | Return logs for a specific website
[**sitesIdPut**](SitesApi.md#sitesIdPut) | **PUT** /sites/{id} | Update a site
[**sitesIdTagsGet**](SitesApi.md#sitesIdTagsGet) | **GET** /sites/{id}/tags | Return tags for a specific website
[**sitesMetadataGet**](SitesApi.md#sitesMetadataGet) | **GET** /sites/metadata | Get the list of fields
[**startSiteBackup**](SitesApi.md#startSiteBackup) | **POST** /sites/{id}/backupstart | Start a remote backup for the site
[**stepSiteBackup**](SitesApi.md#stepSiteBackup) | **POST** /sites/{id}/backupstep | Step (continue) a remote backup for the site
[**updateJoomla**](SitesApi.md#updateJoomla) | **POST** /sites/{id}/updatejoomla | Update Joomla core on the remote site
[**validateDebugSite**](SitesApi.md#validateDebugSite) | **GET** /sites/{id}/validatedebug | validate the site, return the debug information
[**validateSite**](SitesApi.md#validateSite) | **GET** /sites/{id}/validate | validate the site, return the new logs



## addSiteToBackupQueue

> Site addSiteToBackupQueue(id)

Add the site to the backup queue

Add the site to the backup queue

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website
apiInstance.addSiteToBackupQueue(id, (error, data, response) => {
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
 **id** | **Number**| ID of the website | 

### Return type

[**Site**](Site.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## createAudits

> Audit createAudits(id)

Create an audit for the site

Create an audit for the site

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website
apiInstance.createAudits(id, (error, data, response) => {
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
 **id** | **Number**| ID of the website | 

### Return type

[**Audit**](Audit.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## createLog

> Log createLog(id, body)

Create a custom log for a specific website

Create a custom log for a specific website

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website
let body = new WatchfulLi.PostLog(); // PostLog | JSON object Log (only type custom)
apiInstance.createLog(id, body, (error, data, response) => {
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
 **id** | **Number**| ID of the website | 
 **body** | [**PostLog**](PostLog.md)| JSON object Log (only type custom) | 

### Return type

[**Log**](Log.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## createSite

> Site createSite(body)

Create a site

Create a site

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let body = new WatchfulLi.PostSite(); // PostSite | JSON object Site
apiInstance.createSite(body, (error, data, response) => {
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
 **body** | [**PostSite**](PostSite.md)| JSON object Site | 

### Return type

[**Site**](Site.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## deleteMonitor

> Object deleteMonitor(id)

Delete uptime monitor

Return boolean

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website
apiInstance.deleteMonitor(id, (error, data, response) => {
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
 **id** | **Number**| ID of the website | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## getBackupProfiles

> getBackupProfiles(id)

Return backup profile

Return backup profile

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website
apiInstance.getBackupProfiles(id, (error, data, response) => {
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
 **id** | **Number**| ID of the website | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getListBackups

> getListBackups(id)

List of latest backups

List of latest backups

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website
apiInstance.getListBackups(id, (error, data, response) => {
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
 **id** | **Number**| ID of the website | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSiteAudits

> [Audit] getSiteAudits(id, opts)

Return audits for a specific website

Return audits for a specific website

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website
let opts = {
  'fields': "fields_example", // String | Fields to return separate by comas: name,id
  'limit': 789, // Number | Number of object to return (max 100, default 25)
  'limitstart': 789, // Number | Start of the return (default 0)
  'order': "order_example" // String | ORDER by this field
};
apiInstance.getSiteAudits(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the website | 
 **fields** | **String**| Fields to return separate by comas: name,id | [optional] 
 **limit** | **Number**| Number of object to return (max 100, default 25) | [optional] 
 **limitstart** | **Number**| Start of the return (default 0) | [optional] 
 **order** | **String**| ORDER by this field | [optional] 

### Return type

[**[Audit]**](Audit.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## getSiteById

> Site getSiteById(id, opts)

Find sites by ID

Return a site based on ID

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID that needs to be fetched
let opts = {
  'fields': "fields_example" // String | Fields to return separate by comas: name,id
};
apiInstance.getSiteById(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID that needs to be fetched | 
 **fields** | **String**| Fields to return separate by comas: name,id | [optional] 

### Return type

[**Site**](Site.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## getSites

> Site getSites(opts)

Get a list of Sites

Returns a list of Sites

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let opts = {
  'siteids': "siteids_example", // String | List of sites id separated by comma
  'name': "name_example", // String | Site name. Do a 'LIKE' search, you can also use '%'
  'accessUrl': "accessUrl_example", // String | Access URL. Do a 'LIKE' search, you can also use '%'
  'jVersion': "jVersion_example", // String | Joomla version. Do a 'LIKE' search, you can also use '%'
  'ip': "ip_example", // String | Ip address. Do a 'LIKE' search, you can also use '%'
  'jUpdate': 56, // Number | Joomla core update status (1: update required, 0: update not required)
  'canUpdate': 56, // Number | canUpdate
  'published': 56, // Number | Is published
  'error': "error_example", // String | Has errors
  'nbUpdates': "nbUpdates_example", // String | 
  'up': 56, // Number | Is online
  'fields': "fields_example", // String | Fields to return separated by commas (e.g. name,id)
  'limit': 789, // Number | Number of objects to return (max 100, default 25)
  'limitstart': 789, // Number | Start of the return (default 0)
  'order': "order_example" // String | ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name-
};
apiInstance.getSites(opts, (error, data, response) => {
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
 **siteids** | **String**| List of sites id separated by comma | [optional] 
 **name** | **String**| Site name. Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] 
 **accessUrl** | **String**| Access URL. Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] 
 **jVersion** | **String**| Joomla version. Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] 
 **ip** | **String**| Ip address. Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] 
 **jUpdate** | **Number**| Joomla core update status (1: update required, 0: update not required) | [optional] 
 **canUpdate** | **Number**| canUpdate | [optional] 
 **published** | **Number**| Is published | [optional] 
 **error** | **String**| Has errors | [optional] 
 **nbUpdates** | **String**|  | [optional] 
 **up** | **Number**| Is online | [optional] 
 **fields** | **String**| Fields to return separated by commas (e.g. name,id) | [optional] 
 **limit** | **Number**| Number of objects to return (max 100, default 25) | [optional] 
 **limitstart** | **Number**| Start of the return (default 0) | [optional] 
 **order** | **String**| ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name- | [optional] 

### Return type

[**Site**](Site.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## getUptime

> Object getUptime(id)

Return uptime data

Return uptime data

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website
apiInstance.getUptime(id, (error, data, response) => {
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
 **id** | **Number**| ID of the website | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## installExtension

> installExtension(id, url)

Install extension

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website
let url = "url_example"; // String | URL to install the extension from
apiInstance.installExtension(id, url, (error, data, response) => {
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
 **id** | **Number**| ID of the website | 
 **url** | **String**| URL to install the extension from | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postMonitor

> Object postMonitor(id)

Post uptime monitor

Return boolean

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website
apiInstance.postMonitor(id, (error, data, response) => {
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
 **id** | **Number**| ID of the website | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## postTags

> Site postTags(id, body)

Add tags for a specific website

Add tags for a specific website

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website
let body = new WatchfulLi.Tag(); // Tag | JSON object Tag
apiInstance.postTags(id, body, (error, data, response) => {
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
 **id** | **Number**| ID of the website | 
 **body** | [**Tag**](Tag.md)| JSON object Tag | 

### Return type

[**Site**](Site.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## scanner

> String scanner(id)

Scan the site for malware

Scan the site for malware

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website
apiInstance.scanner(id, (error, data, response) => {
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
 **id** | **Number**| ID of the website | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## seoAnalyze

> String seoAnalyze(id)

SEO analyze for a page

SEO analyze for a page

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website
apiInstance.seoAnalyze(id, (error, data, response) => {
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
 **id** | **Number**| ID of the website | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## sitesIdDelete

> String sitesIdDelete(id)

Delete a specific Site

Delete a specific Site

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of Site that needs to be deleted
apiInstance.sitesIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| ID of Site that needs to be deleted | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## sitesIdExtensionsGet

> Extension sitesIdExtensionsGet(id, opts)

Get extensions for a site

Get extensions for a site

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website
let opts = {
  'fields': "fields_example", // String | Fields to return separate by comas: name,id
  'limit': 789, // Number | Number of object to return (max 100, default 25)
  'limitstart': 789, // Number | Start of the return (default 0)
  'order': "order_example" // String | ORDER by this field
};
apiInstance.sitesIdExtensionsGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the website | 
 **fields** | **String**| Fields to return separate by comas: name,id | [optional] 
 **limit** | **Number**| Number of object to return (max 100, default 25) | [optional] 
 **limitstart** | **Number**| Start of the return (default 0) | [optional] 
 **order** | **String**| ORDER by this field | [optional] 

### Return type

[**Extension**](Extension.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## sitesIdLogsGet

> Log sitesIdLogsGet(id, opts)

Return logs for a specific website

Return logs for a specific website

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website
let opts = {
  'logEntry': "logEntry_example", // String | Do a 'LIKE' search, you can also use '%'
  'logType': "logType_example", // String | Type of the log
  'from': "from_example", // String | Logs after this date, format YYYY-MM-DD HH:MM:SS
  'to': "to_example", // String | Logs before this date, format YYYY-MM-DD HH:MM:SS
  'fields': "fields_example", // String | Fields to return separate by comas: name,id
  'limit': 789, // Number | Number of object to return (max 100, default 25)
  'limitstart': 789, // Number | Start of the return (default 0)
  'order': "order_example" // String | ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name-
};
apiInstance.sitesIdLogsGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the website | 
 **logEntry** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] 
 **logType** | **String**| Type of the log | [optional] 
 **from** | **String**| Logs after this date, format YYYY-MM-DD HH:MM:SS | [optional] 
 **to** | **String**| Logs before this date, format YYYY-MM-DD HH:MM:SS | [optional] 
 **fields** | **String**| Fields to return separate by comas: name,id | [optional] 
 **limit** | **Number**| Number of object to return (max 100, default 25) | [optional] 
 **limitstart** | **Number**| Start of the return (default 0) | [optional] 
 **order** | **String**| ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name- | [optional] 

### Return type

[**Log**](Log.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## sitesIdPut

> Site sitesIdPut(id, body)

Update a site

Update a site

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website that needs to be update
let body = new WatchfulLi.PostSite(); // PostSite | JSON object Site
apiInstance.sitesIdPut(id, body, (error, data, response) => {
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
 **id** | **Number**| ID of the website that needs to be update | 
 **body** | [**PostSite**](PostSite.md)| JSON object Site | 

### Return type

[**Site**](Site.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## sitesIdTagsGet

> Tag sitesIdTagsGet(id, opts)

Return tags for a specific website

Return tags for a specific website

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website
let opts = {
  'name': "name_example", // String | Do a 'LIKE' search, you can also use '%'
  'type': "type_example", // String | Bootstrap color of the tag
  'fields': "fields_example", // String | Fields to return separate by comas: name,id
  'limit': 789, // Number | Number of object to return (max 100, default 25)
  'limitstart': 789, // Number | Start of the return (default 0)
  'order': "order_example" // String | ORDER by this field
};
apiInstance.sitesIdTagsGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the website | 
 **name** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] 
 **type** | **String**| Bootstrap color of the tag | [optional] 
 **fields** | **String**| Fields to return separate by comas: name,id | [optional] 
 **limit** | **Number**| Number of object to return (max 100, default 25) | [optional] 
 **limitstart** | **Number**| Start of the return (default 0) | [optional] 
 **order** | **String**| ORDER by this field | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## sitesMetadataGet

> String sitesMetadataGet()

Get the list of fields

Returns a list of fields

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
apiInstance.sitesMetadataGet((error, data, response) => {
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

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## startSiteBackup

> Site startSiteBackup(id)

Start a remote backup for the site

Start a remote backup for the site

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website
apiInstance.startSiteBackup(id, (error, data, response) => {
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
 **id** | **Number**| ID of the website | 

### Return type

[**Site**](Site.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## stepSiteBackup

> Site stepSiteBackup(id)

Step (continue) a remote backup for the site

Step (continue) a remote backup for the site

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website
apiInstance.stepSiteBackup(id, (error, data, response) => {
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
 **id** | **Number**| ID of the website | 

### Return type

[**Site**](Site.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## updateJoomla

> String updateJoomla(id)

Update Joomla core on the remote site

Update Joomla core on the remote site

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website
apiInstance.updateJoomla(id, (error, data, response) => {
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
 **id** | **Number**| ID of the website | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## validateDebugSite

> Log validateDebugSite(id)

validate the site, return the debug information

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website
apiInstance.validateDebugSite(id, (error, data, response) => {
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
 **id** | **Number**| ID of the website | 

### Return type

[**Log**](Log.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## validateSite

> Log validateSite(id)

validate the site, return the new logs

validate the site

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.SitesApi();
let id = 789; // Number | ID of the website
apiInstance.validateSite(id, (error, data, response) => {
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
 **id** | **Number**| ID of the website | 

### Return type

[**Log**](Log.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain

