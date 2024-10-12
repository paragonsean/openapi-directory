# PublicApi.DomainsApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configureDomain**](DomainsApi.md#configureDomain) | **PUT** /domains/{domainName}/renew | Edit domain name renew state
[**editNameServers**](DomainsApi.md#editNameServers) | **PUT** /domains/{domainName}/nameservers | Edit domain name servers
[**getDomain**](DomainsApi.md#getDomain) | **GET** /domains/{domainName} | Details of a domain
[**getDomains**](DomainsApi.md#getDomains) | **GET** /domains | Overviews of domains
[**register**](DomainsApi.md#register) | **POST** /domains/registrations | Register a domain
[**transfer**](DomainsApi.md#transfer) | **POST** /domains/transfers | Transfer a domain



## configureDomain

> configureDomain(domainName, domainName2, opts)

Edit domain name renew state

Allowed if can_toggle_renew is true on the domain detail:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;If there are no unpaid invoices for the domain name anymore.&lt;/li&gt;&lt;li&gt;If the renewal won&#39;t start within 1 month.&lt;/li&gt;&lt;/ul&gt;  Allowed if the requesting user has the finance role.

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.DomainsApi();
let domainName = "domainName_example"; // String | The domain name
let domainName2 = "domainName_example"; // String | Automatically added
let opts = {
  'editDomainWillRenewRequest': new PublicApi.EditDomainWillRenewRequest() // EditDomainWillRenewRequest | Contains the domain renew information
};
apiInstance.configureDomain(domainName, domainName2, opts, (error, data, response) => {
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
 **domainName** | **String**| The domain name | 
 **domainName2** | **String**| Automatically added | 
 **editDomainWillRenewRequest** | [**EditDomainWillRenewRequest**](EditDomainWillRenewRequest.md)| Contains the domain renew information | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## editNameServers

> editNameServers(domainName, domainName2, opts)

Edit domain name servers



### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.DomainsApi();
let domainName = "domainName_example"; // String | The domain name
let domainName2 = "domainName_example"; // String | Automatically added
let opts = {
  'editNameServers': new PublicApi.EditNameServers() // EditNameServers | 
};
apiInstance.editNameServers(domainName, domainName2, opts, (error, data, response) => {
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
 **domainName** | **String**| The domain name | 
 **domainName2** | **String**| Automatically added | 
 **editNameServers** | [**EditNameServers**](EditNameServers.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## getDomain

> DomainDetail getDomain(domainName, domainName2)

Details of a domain

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.DomainsApi();
let domainName = "domainName_example"; // String | The domain name
let domainName2 = "domainName_example"; // String | Automatically added
apiInstance.getDomain(domainName, domainName2, (error, data, response) => {
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
 **domainName** | **String**| The domain name | 
 **domainName2** | **String**| Automatically added | 

### Return type

[**DomainDetail**](DomainDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDomains

> [Domain] getDomains(opts)

Overviews of domains

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.DomainsApi();
let opts = {
  'skip': 56, // Number | The number of items to skip in the resultset.
  'take': 56 // Number | The number of items to return in the resultset. The returned count can be equal or less than this number.
};
apiInstance.getDomains(opts, (error, data, response) => {
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
 **skip** | **Number**| The number of items to skip in the resultset. | [optional] 
 **take** | **Number**| The number of items to return in the resultset. The returned count can be equal or less than this number. | [optional] 

### Return type

[**[Domain]**](Domain.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## register

> register(opts)

Register a domain

Registers an available domain.&lt;br /&gt;Domain names with extension &#39;.ca&#39; are only available for registrants with country code &#39;CA&#39;.

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.DomainsApi();
let opts = {
  'registerDomain': new PublicApi.RegisterDomain() // RegisterDomain | 
};
apiInstance.register(opts, (error, data, response) => {
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
 **registerDomain** | [**RegisterDomain**](RegisterDomain.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## transfer

> transfer(opts)

Transfer a domain

Transfers a domain with a transfer authorization code.&lt;br /&gt;Domain names with extension &#39;.ca&#39; are only available for registrants with country code &#39;CA&#39;.

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.DomainsApi();
let opts = {
  'transferDomain': new PublicApi.TransferDomain() // TransferDomain | 
};
apiInstance.transfer(opts, (error, data, response) => {
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
 **transferDomain** | [**TransferDomain**](TransferDomain.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

