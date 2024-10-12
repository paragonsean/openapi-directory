# PublicApi.MailZonesApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configureAlias**](MailZonesApi.md#configureAlias) | **PUT** /mailzones/{domainName}/aliases/{emailAddress} | Configure a alias
[**configureAntiSpam**](MailZonesApi.md#configureAntiSpam) | **PUT** /mailzones/{domainName}/antispam | Configure anti-spam for mail zone
[**configureSmtpDomain**](MailZonesApi.md#configureSmtpDomain) | **PUT** /mailzones/{domainName}/smtpdomains/{hostname} | Configure an extra smtp domain
[**createAlias**](MailZonesApi.md#createAlias) | **POST** /mailzones/{domainName}/aliases | Create a new alias
[**createCatchAll**](MailZonesApi.md#createCatchAll) | **POST** /mailzones/{domainName}/catchall | Create a catch-all on the mail zone
[**createSmtpDomain**](MailZonesApi.md#createSmtpDomain) | **POST** /mailzones/{domainName}/smtpdomains | Create an extra smtp domain
[**deleteAlias**](MailZonesApi.md#deleteAlias) | **DELETE** /mailzones/{domainName}/aliases/{emailAddress} | Delete a alias
[**deleteCatchAll**](MailZonesApi.md#deleteCatchAll) | **DELETE** /mailzones/{domainName}/catchall/{emailAddress} | Delete a catch-all on the mail zone
[**deleteSmtpDomain**](MailZonesApi.md#deleteSmtpDomain) | **DELETE** /mailzones/{domainName}/smtpdomains/{hostname} | Delete an extra smtp domain
[**getMailZone**](MailZonesApi.md#getMailZone) | **GET** /mailzones/{domainName} | Get the mail zone.



## configureAlias

> configureAlias(domainName, emailAddress, domainName2, emailAddress2, opts)

Configure a alias

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MailZonesApi();
let domainName = "domainName_example"; // String | Mail zone domain name.
let emailAddress = "emailAddress_example"; // String | Alias e-mail address.
let domainName2 = "domainName_example"; // String | Automatically added
let emailAddress2 = "emailAddress_example"; // String | Automatically added
let opts = {
  'updateAliasRequest': new PublicApi.UpdateAliasRequest() // UpdateAliasRequest | Contains the alias information.
};
apiInstance.configureAlias(domainName, emailAddress, domainName2, emailAddress2, opts, (error, data, response) => {
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
 **domainName** | **String**| Mail zone domain name. | 
 **emailAddress** | **String**| Alias e-mail address. | 
 **domainName2** | **String**| Automatically added | 
 **emailAddress2** | **String**| Automatically added | 
 **updateAliasRequest** | [**UpdateAliasRequest**](UpdateAliasRequest.md)| Contains the alias information. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## configureAntiSpam

> configureAntiSpam(domainName, domainName2, opts)

Configure anti-spam for mail zone

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MailZonesApi();
let domainName = "domainName_example"; // String | Mail zone domain name.
let domainName2 = "domainName_example"; // String | Automatically added
let opts = {
  'updateAntiSpamRequest': new PublicApi.UpdateAntiSpamRequest() // UpdateAntiSpamRequest | Contains the anti-spam information.
};
apiInstance.configureAntiSpam(domainName, domainName2, opts, (error, data, response) => {
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
 **domainName** | **String**| Mail zone domain name. | 
 **domainName2** | **String**| Automatically added | 
 **updateAntiSpamRequest** | [**UpdateAntiSpamRequest**](UpdateAntiSpamRequest.md)| Contains the anti-spam information. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## configureSmtpDomain

> configureSmtpDomain(domainName, hostname, domainName2, opts)

Configure an extra smtp domain

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MailZonesApi();
let domainName = "domainName_example"; // String | Mail zone domain name.
let hostname = "hostname_example"; // String | Smtp domain name.
let domainName2 = "domainName_example"; // String | Automatically added
let opts = {
  'updateSmtpDomainRequest': new PublicApi.UpdateSmtpDomainRequest() // UpdateSmtpDomainRequest | Contains the smtp domain information.
};
apiInstance.configureSmtpDomain(domainName, hostname, domainName2, opts, (error, data, response) => {
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
 **domainName** | **String**| Mail zone domain name. | 
 **hostname** | **String**| Smtp domain name. | 
 **domainName2** | **String**| Automatically added | 
 **updateSmtpDomainRequest** | [**UpdateSmtpDomainRequest**](UpdateSmtpDomainRequest.md)| Contains the smtp domain information. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAlias

> createAlias(domainName, domainName2, opts)

Create a new alias

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MailZonesApi();
let domainName = "domainName_example"; // String | Mail zone domain name.
let domainName2 = "domainName_example"; // String | Automatically added
let opts = {
  'createAliasRequest': new PublicApi.CreateAliasRequest() // CreateAliasRequest | Contains the alias information.
};
apiInstance.createAlias(domainName, domainName2, opts, (error, data, response) => {
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
 **domainName** | **String**| Mail zone domain name. | 
 **domainName2** | **String**| Automatically added | 
 **createAliasRequest** | [**CreateAliasRequest**](CreateAliasRequest.md)| Contains the alias information. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createCatchAll

> createCatchAll(domainName, domainName2, opts)

Create a catch-all on the mail zone

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MailZonesApi();
let domainName = "domainName_example"; // String | Mail zone domain name.
let domainName2 = "domainName_example"; // String | Automatically added
let opts = {
  'createCatchAllRequest': new PublicApi.CreateCatchAllRequest() // CreateCatchAllRequest | Contains the catch-all information.
};
apiInstance.createCatchAll(domainName, domainName2, opts, (error, data, response) => {
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
 **domainName** | **String**| Mail zone domain name. | 
 **domainName2** | **String**| Automatically added | 
 **createCatchAllRequest** | [**CreateCatchAllRequest**](CreateCatchAllRequest.md)| Contains the catch-all information. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## createSmtpDomain

> createSmtpDomain(domainName, domainName2, opts)

Create an extra smtp domain

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MailZonesApi();
let domainName = "domainName_example"; // String | Mail zone domain name.
let domainName2 = "domainName_example"; // String | Automatically added
let opts = {
  'createSmtpDomainRequest': new PublicApi.CreateSmtpDomainRequest() // CreateSmtpDomainRequest | Contains the smtp domain information.
};
apiInstance.createSmtpDomain(domainName, domainName2, opts, (error, data, response) => {
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
 **domainName** | **String**| Mail zone domain name. | 
 **domainName2** | **String**| Automatically added | 
 **createSmtpDomainRequest** | [**CreateSmtpDomainRequest**](CreateSmtpDomainRequest.md)| Contains the smtp domain information. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAlias

> deleteAlias(domainName, emailAddress, domainName2, emailAddress2)

Delete a alias

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MailZonesApi();
let domainName = "domainName_example"; // String | Mail zone domain name.
let emailAddress = "emailAddress_example"; // String | Alias e-mail address.
let domainName2 = "domainName_example"; // String | Automatically added
let emailAddress2 = "emailAddress_example"; // String | Automatically added
apiInstance.deleteAlias(domainName, emailAddress, domainName2, emailAddress2, (error, data, response) => {
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
 **domainName** | **String**| Mail zone domain name. | 
 **emailAddress** | **String**| Alias e-mail address. | 
 **domainName2** | **String**| Automatically added | 
 **emailAddress2** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteCatchAll

> deleteCatchAll(domainName, emailAddress, domainName2, emailAddress2)

Delete a catch-all on the mail zone

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MailZonesApi();
let domainName = "domainName_example"; // String | Mail zone domain name.
let emailAddress = "emailAddress_example"; // String | E-mail address to which all e-mails are sent to inexistent mailboxes or aliases.
let domainName2 = "domainName_example"; // String | Automatically added
let emailAddress2 = "emailAddress_example"; // String | Automatically added
apiInstance.deleteCatchAll(domainName, emailAddress, domainName2, emailAddress2, (error, data, response) => {
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
 **domainName** | **String**| Mail zone domain name. | 
 **emailAddress** | **String**| E-mail address to which all e-mails are sent to inexistent mailboxes or aliases. | 
 **domainName2** | **String**| Automatically added | 
 **emailAddress2** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSmtpDomain

> deleteSmtpDomain(domainName, hostname, domainName2)

Delete an extra smtp domain

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MailZonesApi();
let domainName = "domainName_example"; // String | Mail zone domain name.
let hostname = "hostname_example"; // String | Smtp domain name.
let domainName2 = "domainName_example"; // String | Automatically added
apiInstance.deleteSmtpDomain(domainName, hostname, domainName2, (error, data, response) => {
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
 **domainName** | **String**| Mail zone domain name. | 
 **hostname** | **String**| Smtp domain name. | 
 **domainName2** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getMailZone

> MailZone getMailZone(domainName, domainName2)

Get the mail zone.

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MailZonesApi();
let domainName = "domainName_example"; // String | Mail zone domain name.
let domainName2 = "domainName_example"; // String | Automatically added
apiInstance.getMailZone(domainName, domainName2, (error, data, response) => {
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
 **domainName** | **String**| Mail zone domain name. | 
 **domainName2** | **String**| Automatically added | 

### Return type

[**MailZone**](MailZone.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

