# DomainsIndexApi.DomainsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domainsTldZoneIdDownloadGet**](DomainsApi.md#domainsTldZoneIdDownloadGet) | **GET** /domains/tld/{zone_id}/download | Download Whole Dataset for TLD
[**domainsTldZoneIdSearchGet**](DomainsApi.md#domainsTldZoneIdSearchGet) | **GET** /domains/tld/{zone_id}/search | Domains Search for TLD
[**domainsUpdatesAddedDownloadGet**](DomainsApi.md#domainsUpdatesAddedDownloadGet) | **GET** /domains/updates/added/download | Download added domains, latest if date not specified
[**domainsUpdatesAddedGet**](DomainsApi.md#domainsUpdatesAddedGet) | **GET** /domains/updates/added | Get added domains, latest if date not specified
[**domainsUpdatesDeletedDownloadGet**](DomainsApi.md#domainsUpdatesDeletedDownloadGet) | **GET** /domains/updates/deleted/download | Download deleted domains, latest if date not specified
[**domainsUpdatesDeletedGet**](DomainsApi.md#domainsUpdatesDeletedGet) | **GET** /domains/updates/deleted | Get deleted domains, latest if date not specified
[**domainsUpdatesListGet**](DomainsApi.md#domainsUpdatesListGet) | **GET** /domains/updates/list | List of updates
[**getSearchDomainItem**](DomainsApi.md#getSearchDomainItem) | **GET** /domains/search | Domains Database Search
[**getTldDomainItem**](DomainsApi.md#getTldDomainItem) | **GET** /domains/tld/{zone_id} | Get TLD records



## domainsTldZoneIdDownloadGet

> domainsTldZoneIdDownloadGet(zoneId, opts)

Download Whole Dataset for TLD

### Example

```javascript
import DomainsIndexApi from 'domains_index_api';

let apiInstance = new DomainsIndexApi.DomainsApi();
let zoneId = "zoneId_example"; // String | 
let opts = {
  'apiKey': "apiKey_example", // String | API key
  'date': "date_example" // String | Request date
};
apiInstance.domainsTldZoneIdDownloadGet(zoneId, opts, (error, data, response) => {
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
 **zoneId** | **String**|  | 
 **apiKey** | **String**| API key | [optional] 
 **date** | **String**| Request date | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## domainsTldZoneIdSearchGet

> SearchResults domainsTldZoneIdSearchGet(zoneId, opts)

Domains Search for TLD

### Example

```javascript
import DomainsIndexApi from 'domains_index_api';

let apiInstance = new DomainsIndexApi.DomainsApi();
let zoneId = "zoneId_example"; // String | 
let opts = {
  'apiKey': "apiKey_example", // String | API key
  'date': "date_example", // String | Request date
  'page': "page_example", // String | Search page to request
  'limit': 50, // Number | Results per page
  'domain': "domain_example", // String | Domain includes
  'country': "country_example", // String | Hosting Country
  'isDead': true, // Boolean | Dead or Not, default not
  'A': "A_example", // String | A record includes
  'NS': "NS_example", // String | NS record includes
  'CNAME': "CNAME_example", // String | CNAME record includes
  'MX': "MX_example", // String | MX record includes
  'TXT': "TXT_example" // String | TXT record includes
};
apiInstance.domainsTldZoneIdSearchGet(zoneId, opts, (error, data, response) => {
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
 **zoneId** | **String**|  | 
 **apiKey** | **String**| API key | [optional] 
 **date** | **String**| Request date | [optional] 
 **page** | **String**| Search page to request | [optional] 
 **limit** | **Number**| Results per page | [optional] [default to 50]
 **domain** | **String**| Domain includes | [optional] 
 **country** | **String**| Hosting Country | [optional] 
 **isDead** | **Boolean**| Dead or Not, default not | [optional] 
 **A** | **String**| A record includes | [optional] 
 **NS** | **String**| NS record includes | [optional] 
 **CNAME** | **String**| CNAME record includes | [optional] 
 **MX** | **String**| MX record includes | [optional] 
 **TXT** | **String**| TXT record includes | [optional] 

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainsUpdatesAddedDownloadGet

> domainsUpdatesAddedDownloadGet(opts)

Download added domains, latest if date not specified

### Example

```javascript
import DomainsIndexApi from 'domains_index_api';

let apiInstance = new DomainsIndexApi.DomainsApi();
let opts = {
  'apiKey': "apiKey_example", // String | API key
  'date': "date_example" // String | Request date
};
apiInstance.domainsUpdatesAddedDownloadGet(opts, (error, data, response) => {
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
 **apiKey** | **String**| API key | [optional] 
 **date** | **String**| Request date | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## domainsUpdatesAddedGet

> SearchResults domainsUpdatesAddedGet(opts)

Get added domains, latest if date not specified

### Example

```javascript
import DomainsIndexApi from 'domains_index_api';

let apiInstance = new DomainsIndexApi.DomainsApi();
let opts = {
  'apiKey': "apiKey_example", // String | API key
  'date': "date_example", // String | Request date
  'page': "page_example", // String | Search page to request
  'limit': 50 // Number | Results per page
};
apiInstance.domainsUpdatesAddedGet(opts, (error, data, response) => {
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
 **apiKey** | **String**| API key | [optional] 
 **date** | **String**| Request date | [optional] 
 **page** | **String**| Search page to request | [optional] 
 **limit** | **Number**| Results per page | [optional] [default to 50]

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainsUpdatesDeletedDownloadGet

> domainsUpdatesDeletedDownloadGet(opts)

Download deleted domains, latest if date not specified

### Example

```javascript
import DomainsIndexApi from 'domains_index_api';

let apiInstance = new DomainsIndexApi.DomainsApi();
let opts = {
  'apiKey': "apiKey_example", // String | API key
  'date': "date_example" // String | Request date
};
apiInstance.domainsUpdatesDeletedDownloadGet(opts, (error, data, response) => {
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
 **apiKey** | **String**| API key | [optional] 
 **date** | **String**| Request date | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## domainsUpdatesDeletedGet

> SearchResults domainsUpdatesDeletedGet(opts)

Get deleted domains, latest if date not specified

### Example

```javascript
import DomainsIndexApi from 'domains_index_api';

let apiInstance = new DomainsIndexApi.DomainsApi();
let opts = {
  'apiKey': "apiKey_example", // String | API key
  'date': "date_example", // String | Request date
  'page': "page_example", // String | Search page to request
  'limit': 50 // Number | Results per page
};
apiInstance.domainsUpdatesDeletedGet(opts, (error, data, response) => {
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
 **apiKey** | **String**| API key | [optional] 
 **date** | **String**| Request date | [optional] 
 **page** | **String**| Search page to request | [optional] 
 **limit** | **Number**| Results per page | [optional] [default to 50]

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## domainsUpdatesListGet

> UpdateModel domainsUpdatesListGet(opts)

List of updates

### Example

```javascript
import DomainsIndexApi from 'domains_index_api';

let apiInstance = new DomainsIndexApi.DomainsApi();
let opts = {
  'apiKey': "apiKey_example" // String | API key
};
apiInstance.domainsUpdatesListGet(opts, (error, data, response) => {
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
 **apiKey** | **String**| API key | [optional] 

### Return type

[**UpdateModel**](UpdateModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSearchDomainItem

> SearchResults getSearchDomainItem(opts)

Domains Database Search

### Example

```javascript
import DomainsIndexApi from 'domains_index_api';

let apiInstance = new DomainsIndexApi.DomainsApi();
let opts = {
  'apiKey': "apiKey_example", // String | API key
  'date': "date_example", // String | Request date
  'page': "page_example", // String | Search page to request
  'limit': 50, // Number | Results per page
  'domain': "domain_example", // String | Domain includes
  'zone': "zone_example", // String | In Zone
  'country': "country_example", // String | Hosting Country
  'isDead': true, // Boolean | Dead or Not, default not
  'A': "A_example", // String | A record includes
  'NS': "NS_example", // String | NS record includes
  'CNAME': "CNAME_example", // String | CNAME record includes
  'MX': "MX_example", // String | MX record includes
  'TXT': "TXT_example" // String | TXT record includes
};
apiInstance.getSearchDomainItem(opts, (error, data, response) => {
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
 **apiKey** | **String**| API key | [optional] 
 **date** | **String**| Request date | [optional] 
 **page** | **String**| Search page to request | [optional] 
 **limit** | **Number**| Results per page | [optional] [default to 50]
 **domain** | **String**| Domain includes | [optional] 
 **zone** | **String**| In Zone | [optional] 
 **country** | **String**| Hosting Country | [optional] 
 **isDead** | **Boolean**| Dead or Not, default not | [optional] 
 **A** | **String**| A record includes | [optional] 
 **NS** | **String**| NS record includes | [optional] 
 **CNAME** | **String**| CNAME record includes | [optional] 
 **MX** | **String**| MX record includes | [optional] 
 **TXT** | **String**| TXT record includes | [optional] 

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTldDomainItem

> SearchResults getTldDomainItem(zoneId, opts)

Get TLD records

### Example

```javascript
import DomainsIndexApi from 'domains_index_api';

let apiInstance = new DomainsIndexApi.DomainsApi();
let zoneId = "zoneId_example"; // String | 
let opts = {
  'apiKey': "apiKey_example", // String | API key
  'date': "date_example", // String | Request date
  'page': "page_example", // String | Search page to request
  'limit': 50, // Number | Results per page
  'domain': "domain_example", // String | Domain includes
  'country': "country_example", // String | Hosting Country
  'isDead': true, // Boolean | Dead or Not, default not
  'A': "A_example", // String | A record includes
  'NS': "NS_example", // String | NS record includes
  'CNAME': "CNAME_example", // String | CNAME record includes
  'MX': "MX_example", // String | MX record includes
  'TXT': "TXT_example" // String | TXT record includes
};
apiInstance.getTldDomainItem(zoneId, opts, (error, data, response) => {
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
 **zoneId** | **String**|  | 
 **apiKey** | **String**| API key | [optional] 
 **date** | **String**| Request date | [optional] 
 **page** | **String**| Search page to request | [optional] 
 **limit** | **Number**| Results per page | [optional] [default to 50]
 **domain** | **String**| Domain includes | [optional] 
 **country** | **String**| Hosting Country | [optional] 
 **isDead** | **Boolean**| Dead or Not, default not | [optional] 
 **A** | **String**| A record includes | [optional] 
 **NS** | **String**| NS record includes | [optional] 
 **CNAME** | **String**| CNAME record includes | [optional] 
 **MX** | **String**| MX record includes | [optional] 
 **TXT** | **String**| TXT record includes | [optional] 

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

