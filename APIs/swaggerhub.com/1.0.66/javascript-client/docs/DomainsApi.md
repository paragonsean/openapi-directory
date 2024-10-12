# SwaggerHubRegistryApi.DomainsApi

All URIs are relative to *https://api.swaggerhub.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addDomainCommentReplyV2**](DomainsApi.md#addDomainCommentReplyV2) | **POST** /domains/{owner}/{domain}/{version}/comments/{comment}/replies | Reply to a comment
[**addDomainCommentV2**](DomainsApi.md#addDomainCommentV2) | **POST** /domains/{owner}/{domain}/{version}/comments | Add a new comment
[**cloneDomain**](DomainsApi.md#cloneDomain) | **POST** /domains/{owner}/{domain}/{version}/clone | Create a new domain version
[**deleteDomain**](DomainsApi.md#deleteDomain) | **DELETE** /domains/{owner}/{domain} | Delete a domain
[**deleteDomainCommentReplyV2**](DomainsApi.md#deleteDomainCommentReplyV2) | **DELETE** /domains/{owner}/{domain}/{version}/comments/{comment}/replies/{reply} | Delete a comment reply
[**deleteDomainCommentV2**](DomainsApi.md#deleteDomainCommentV2) | **DELETE** /domains/{owner}/{domain}/{version}/comments/{comment} | Delete a comment
[**deleteDomainVersion**](DomainsApi.md#deleteDomainVersion) | **DELETE** /domains/{owner}/{domain}/{version} | Delete a domain version
[**forkDomain**](DomainsApi.md#forkDomain) | **POST** /domains/{owner}/{domain}/{version}/fork | Fork a domain
[**getDomainCommentsV2**](DomainsApi.md#getDomainCommentsV2) | **GET** /domains/{owner}/{domain}/{version}/comments | Get comments for the specified domain version
[**getDomainDefaultVersion**](DomainsApi.md#getDomainDefaultVersion) | **GET** /domains/{owner}/{domain}/settings/default | Get the default version of a domain
[**getDomainDefinition**](DomainsApi.md#getDomainDefinition) | **GET** /domains/{owner}/{domain}/{version} | Get the OpenAPI definition of the specified domain version
[**getDomainJsonDefinition**](DomainsApi.md#getDomainJsonDefinition) | **GET** /domains/{owner}/{domain}/{version}/domain.json | Get the OpenAPI definition for the specified domain version in JSON format
[**getDomainLifecycleSettings**](DomainsApi.md#getDomainLifecycleSettings) | **GET** /domains/{owner}/{domain}/{version}/settings/lifecycle | Get the published status for the specified domain and version
[**getDomainPrivateSettings**](DomainsApi.md#getDomainPrivateSettings) | **GET** /domains/{owner}/{domain}/{version}/settings/private | Get the visibility (public or private) of a domain version
[**getDomainVersions**](DomainsApi.md#getDomainVersions) | **GET** /domains/{owner}/{domain} | Get a list of domain versions
[**getDomainYamlDefinition**](DomainsApi.md#getDomainYamlDefinition) | **GET** /domains/{owner}/{domain}/{version}/domain.yaml | Get the OpenAPI definition for the specified domain version in YAML format
[**getOwnerDomains**](DomainsApi.md#getOwnerDomains) | **GET** /domains/{owner} | Get a list of domains of the specified owner
[**renameDomain**](DomainsApi.md#renameDomain) | **POST** /domains/{owner}/{domain}/rename | Rename a domain
[**saveDomainDefinition**](DomainsApi.md#saveDomainDefinition) | **POST** /domains/{owner}/{domain} | Create or update a domain
[**searchApisAndDomains_0**](DomainsApi.md#searchApisAndDomains_0) | **GET** /specs | Retrieve a list of currently defined APIs, domains, and templates in APIs.json format
[**searchDomains**](DomainsApi.md#searchDomains) | **GET** /domains | Search domains
[**setDomainCommentStatusV2**](DomainsApi.md#setDomainCommentStatusV2) | **PUT** /domains/{owner}/{domain}/{version}/comments/{comment}/status/{status} | Resolve or reopen a comment
[**setDomainDefaultVersion**](DomainsApi.md#setDomainDefaultVersion) | **PUT** /domains/{owner}/{domain}/settings/default | Set the default version for a domain
[**setDomainLifecycleSettings**](DomainsApi.md#setDomainLifecycleSettings) | **PUT** /domains/{owner}/{domain}/{version}/settings/lifecycle | Publish or unpublish a domain version
[**setDomainPrivateSettings**](DomainsApi.md#setDomainPrivateSettings) | **PUT** /domains/{owner}/{domain}/{version}/settings/private | Set the visibility (public or private) of a domain version
[**updateDomainCommentReplyV2**](DomainsApi.md#updateDomainCommentReplyV2) | **PATCH** /domains/{owner}/{domain}/{version}/comments/{comment}/replies/{reply} | Update a comment reply
[**updateDomainCommentV2**](DomainsApi.md#updateDomainCommentV2) | **PATCH** /domains/{owner}/{domain}/{version}/comments/{comment} | Update a comment
[**updateDomainCommentsV2**](DomainsApi.md#updateDomainCommentsV2) | **POST** /domains/{owner}/{domain}/{version}/comments/batch | Bulk update comments



## addDomainCommentReplyV2

> [Comment] addDomainCommentReplyV2(owner, domain, version, comment, body)

Reply to a comment

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let version = "version_example"; // String | Version identifier
let comment = "comment_example"; // String | Comment identifier
let body = new SwaggerHubRegistryApi.NewReply(); // NewReply | 
apiInstance.addDomainCommentReplyV2(owner, domain, version, comment, body, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **comment** | **String**| Comment identifier | 
 **body** | [**NewReply**](NewReply.md)|  | 

### Return type

[**[Comment]**](Comment.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addDomainCommentV2

> ClosableComment addDomainCommentV2(owner, domain, version, body)

Add a new comment

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let version = "version_example"; // String | Version identifier
let body = new SwaggerHubRegistryApi.NewComment(); // NewComment | 
apiInstance.addDomainCommentV2(owner, domain, version, body, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **body** | [**NewComment**](NewComment.md)|  | 

### Return type

[**ClosableComment**](ClosableComment.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloneDomain

> cloneDomain(owner, domain, version, newVersion)

Create a new domain version

Use this operation to clone an existing domain version as a new version.  Note that the new version is not automatically set as the default version.

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let version = "version_example"; // String | The version to clone (case-sensitive)
let newVersion = new SwaggerHubRegistryApi.NewVersion(); // NewVersion | An object that contains the new version number and other parameters. The version number must be in the format described in the [documentation](https://support.smartbear.com/swaggerhub/docs/apis/versioning.html#format).
apiInstance.cloneDomain(owner, domain, version, newVersion, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **version** | **String**| The version to clone (case-sensitive) | 
 **newVersion** | [**NewVersion**](NewVersion.md)| An object that contains the new version number and other parameters. The version number must be in the format described in the [documentation](https://support.smartbear.com/swaggerhub/docs/apis/versioning.html#format). | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteDomain

> deleteDomain(owner, domain, opts)

Delete a domain

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let opts = {
  'force': false // Boolean | If this domain is referenced from other APIs and domains, this parameter must be `true`. Otherwise, the request will be rejected with status code 424.
};
apiInstance.deleteDomain(owner, domain, opts, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **force** | **Boolean**| If this domain is referenced from other APIs and domains, this parameter must be &#x60;true&#x60;. Otherwise, the request will be rejected with status code 424. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDomainCommentReplyV2

> deleteDomainCommentReplyV2(owner, domain, version, comment, reply)

Delete a comment reply

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let version = "version_example"; // String | Version identifier
let comment = "comment_example"; // String | Comment identifier
let reply = "reply_example"; // String | Reply identifier
apiInstance.deleteDomainCommentReplyV2(owner, domain, version, comment, reply, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **comment** | **String**| Comment identifier | 
 **reply** | **String**| Reply identifier | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteDomainCommentV2

> deleteDomainCommentV2(owner, domain, version, comment)

Delete a comment

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let version = "version_example"; // String | Version identifier
let comment = "comment_example"; // String | Comment identifier
apiInstance.deleteDomainCommentV2(owner, domain, version, comment, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **comment** | **String**| Comment identifier | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteDomainVersion

> deleteDomainVersion(owner, domain, version, opts)

Delete a domain version

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let version = "version_example"; // String | Version identifier
let opts = {
  'force': false // Boolean | If this domain version is referenced from other APIs and domains, this parameter must be `true`. Otherwise, the request will be rejected with status code 424.
};
apiInstance.deleteDomainVersion(owner, domain, version, opts, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **force** | **Boolean**| If this domain version is referenced from other APIs and domains, this parameter must be &#x60;true&#x60;. Otherwise, the request will be rejected with status code 424. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## forkDomain

> forkDomain(owner, domain, version, forkVersion)

Fork a domain

Creates a [fork](https://support.smartbear.com/swaggerhub/docs/apis/forking-api.html) of the specified domain definition and version. The fork can be created as a new domain, or as a new version in another existing domain.

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let version = "version_example"; // String | Version identifier
let forkVersion = new SwaggerHubRegistryApi.ForkVersion(); // ForkVersion | Fork parameters
apiInstance.forkDomain(owner, domain, version, forkVersion, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **forkVersion** | [**ForkVersion**](ForkVersion.md)| Fork parameters | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDomainCommentsV2

> [ClosableComment] getDomainCommentsV2(owner, domain, version)

Get comments for the specified domain version

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let version = "version_example"; // String | Version identifier
apiInstance.getDomainCommentsV2(owner, domain, version, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **version** | **String**| Version identifier | 

### Return type

[**[ClosableComment]**](ClosableComment.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDomainDefaultVersion

> DefaultVersion getDomainDefaultVersion(owner, domain)

Get the default version of a domain

This operation returns the version identifier, such as &#x60;1.0.0&#x60;. To get the definition itself, use &#x60;GET /domains/{owner}/{domain}/{version}&#x60;.

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
apiInstance.getDomainDefaultVersion(owner, domain, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 

### Return type

[**DefaultVersion**](DefaultVersion.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDomainDefinition

> Object getDomainDefinition(owner, domain, version)

Get the OpenAPI definition of the specified domain version

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let version = "version_example"; // String | Version identifier
apiInstance.getDomainDefinition(owner, domain, version, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **version** | **String**| Version identifier | 

### Return type

**Object**

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/yaml


## getDomainJsonDefinition

> Object getDomainJsonDefinition(owner, domain, version)

Get the OpenAPI definition for the specified domain version in JSON format

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let version = "version_example"; // String | Version identifier
apiInstance.getDomainJsonDefinition(owner, domain, version, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **version** | **String**| Version identifier | 

### Return type

**Object**

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDomainLifecycleSettings

> LifecycleSettings getDomainLifecycleSettings(owner, domain, version)

Get the published status for the specified domain and version

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let version = "version_example"; // String | Version identifier
apiInstance.getDomainLifecycleSettings(owner, domain, version, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **version** | **String**| Version identifier | 

### Return type

[**LifecycleSettings**](LifecycleSettings.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDomainPrivateSettings

> VisibilitySettings getDomainPrivateSettings(owner, domain, version)

Get the visibility (public or private) of a domain version

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let version = "version_example"; // String | Version identifier
apiInstance.getDomainPrivateSettings(owner, domain, version, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **version** | **String**| Version identifier | 

### Return type

[**VisibilitySettings**](VisibilitySettings.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDomainVersions

> ApisJson getDomainVersions(owner, domain)

Get a list of domain versions

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
apiInstance.getDomainVersions(owner, domain, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 

### Return type

[**ApisJson**](ApisJson.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDomainYamlDefinition

> Object getDomainYamlDefinition(owner, domain, version)

Get the OpenAPI definition for the specified domain version in YAML format

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let version = "version_example"; // String | Version identifier
apiInstance.getDomainYamlDefinition(owner, domain, version, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **version** | **String**| Version identifier | 

### Return type

**Object**

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/yaml


## getOwnerDomains

> ApisJson getOwnerDomains(owner, opts)

Get a list of domains of the specified owner

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let opts = {
  'page': 0, // Number | Page to return
  'limit': 10, // Number | Number of results per page (1 .. 100)
  'sort': "'NAME'", // String | Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by `info.title` 
  'order': "'ASC'" // String | Sort order
};
apiInstance.getOwnerDomains(owner, opts, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **page** | **Number**| Page to return | [optional] [default to 0]
 **limit** | **Number**| Number of results per page (1 .. 100) | [optional] [default to 10]
 **sort** | **String**| Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by &#x60;info.title&#x60;  | [optional] [default to &#39;NAME&#39;]
 **order** | **String**| Sort order | [optional] [default to &#39;ASC&#39;]

### Return type

[**ApisJson**](ApisJson.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## renameDomain

> renameDomain(owner, domain, newName, opts)

Rename a domain

The new name must follow the [naming rules](https://support.smartbear.com/swaggerhub/docs/apis/creating-api.html).

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let newName = "newName_example"; // String | New name
let opts = {
  'force': false // Boolean | If this domain is referenced from other APIs and domains, this parameter must be true. Otherwise, the request will be rejected with status code 424.
};
apiInstance.renameDomain(owner, domain, newName, opts, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **newName** | **String**| New name | 
 **force** | **Boolean**| If this domain is referenced from other APIs and domains, this parameter must be true. Otherwise, the request will be rejected with status code 424. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## saveDomainDefinition

> saveDomainDefinition(owner, domain, opts)

Create or update a domain

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let opts = {
  'isPrivate': false, // Boolean | Specifies whether the domain has to be private
  'version': "version_example", // String | Domain version. If omitted, will be taken from the `info.version` field in the definition.
  'force': true, // Boolean | Force update
  'definition': "definition_example" // String | OpenAPI definition of this domain
};
apiInstance.saveDomainDefinition(owner, domain, opts, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **isPrivate** | **Boolean**| Specifies whether the domain has to be private | [optional] [default to false]
 **version** | **String**| Domain version. If omitted, will be taken from the &#x60;info.version&#x60; field in the definition. | [optional] 
 **force** | **Boolean**| Force update | [optional] 
 **definition** | **String**| OpenAPI definition of this domain | [optional] 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: application/json, application/yaml
- **Accept**: Not defined


## searchApisAndDomains_0

> ApisJson searchApisAndDomains_0(opts)

Retrieve a list of currently defined APIs, domains, and templates in APIs.json format

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let opts = {
  'specType': "'ANY'", // String | Type of definitions to search: * API - APIs only * DOMAIN - domains only * TEMPLATE - templates only * ANY - APIs, domains, and templates 
  'visibility': "'ANY'", // String | The visibility of a definition in SwaggerHub: * PUBLIC - can be viewed by anyone * PRIVATE - can only be viewed by you or your organization and those that you are collaborating with or have shared it with * ANY - either PUBLIC or PRIVATE 
  'state': "'ALL'", // String | Matches against published state of the spec: * UNPUBLISHED - spec is a draft, a work in progress * PUBLISHED - spec is a stable version ready for consuming from client applications * ANY - either PUBLISHED or UNPUBLISHED 
  'owner': "owner_example", // String | API or domain owner. Can be username or organization name. Case-sensitive.
  'query': "query_example", // String | Free text query to match
  'page': 0, // Number | Page to return
  'limit': 10, // Number | Number of results per page (1 .. 100)
  'sort': "'NAME'", // String | Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by `info.title` 
  'order': "'ASC'" // String | Sort order
};
apiInstance.searchApisAndDomains_0(opts, (error, data, response) => {
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
 **specType** | **String**| Type of definitions to search: * API - APIs only * DOMAIN - domains only * TEMPLATE - templates only * ANY - APIs, domains, and templates  | [optional] [default to &#39;ANY&#39;]
 **visibility** | **String**| The visibility of a definition in SwaggerHub: * PUBLIC - can be viewed by anyone * PRIVATE - can only be viewed by you or your organization and those that you are collaborating with or have shared it with * ANY - either PUBLIC or PRIVATE  | [optional] [default to &#39;ANY&#39;]
 **state** | **String**| Matches against published state of the spec: * UNPUBLISHED - spec is a draft, a work in progress * PUBLISHED - spec is a stable version ready for consuming from client applications * ANY - either PUBLISHED or UNPUBLISHED  | [optional] [default to &#39;ALL&#39;]
 **owner** | **String**| API or domain owner. Can be username or organization name. Case-sensitive. | [optional] 
 **query** | **String**| Free text query to match | [optional] 
 **page** | **Number**| Page to return | [optional] [default to 0]
 **limit** | **Number**| Number of results per page (1 .. 100) | [optional] [default to 10]
 **sort** | **String**| Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by &#x60;info.title&#x60;  | [optional] [default to &#39;NAME&#39;]
 **order** | **String**| Sort order | [optional] [default to &#39;ASC&#39;]

### Return type

[**ApisJson**](ApisJson.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchDomains

> searchDomains(opts)

Search domains

This is a convenience alias for &#x60;GET /specs?specType&#x3D;DOMAIN&#x60;.

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let opts = {
  'query': "query_example", // String | Free text query to match
  'state': "'ALL'", // String | Matches against published state of the spec: * UNPUBLISHED - spec is a draft, a work in progress * PUBLISHED - spec is a stable version ready for consuming from client applications * ANY - either PUBLISHED or UNPUBLISHED 
  'page': 0, // Number | Page to return
  'limit': 10, // Number | Number of results per page (1 .. 100)
  'sort': "'NAME'", // String | Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by `info.title` 
  'order': "'ASC'" // String | Sort order
};
apiInstance.searchDomains(opts, (error, data, response) => {
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
 **query** | **String**| Free text query to match | [optional] 
 **state** | **String**| Matches against published state of the spec: * UNPUBLISHED - spec is a draft, a work in progress * PUBLISHED - spec is a stable version ready for consuming from client applications * ANY - either PUBLISHED or UNPUBLISHED  | [optional] [default to &#39;ALL&#39;]
 **page** | **Number**| Page to return | [optional] [default to 0]
 **limit** | **Number**| Number of results per page (1 .. 100) | [optional] [default to 10]
 **sort** | **String**| Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by &#x60;info.title&#x60;  | [optional] [default to &#39;NAME&#39;]
 **order** | **String**| Sort order | [optional] [default to &#39;ASC&#39;]

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setDomainCommentStatusV2

> setDomainCommentStatusV2(owner, domain, version, comment, status)

Resolve or reopen a comment

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let version = "version_example"; // String | Version identifier
let comment = "comment_example"; // String | Comment identifier
let status = "status_example"; // String | Comment status
apiInstance.setDomainCommentStatusV2(owner, domain, version, comment, status, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **comment** | **String**| Comment identifier | 
 **status** | **String**| Comment status | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setDomainDefaultVersion

> setDomainDefaultVersion(owner, domain, defaultVersion)

Set the default version for a domain

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let defaultVersion = new SwaggerHubRegistryApi.DefaultVersion(); // DefaultVersion | An object that specifies the default version for this domain
apiInstance.setDomainDefaultVersion(owner, domain, defaultVersion, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **defaultVersion** | [**DefaultVersion**](DefaultVersion.md)| An object that specifies the default version for this domain | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## setDomainLifecycleSettings

> setDomainLifecycleSettings(owner, domain, version, settings, opts)

Publish or unpublish a domain version

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let version = "version_example"; // String | Version identifier
let settings = new SwaggerHubRegistryApi.LifecycleSettings(); // LifecycleSettings | An object that specifies the new `published` state: `true` means published, `false` - unpublished
let opts = {
  'force': false // Boolean | To publish a domain that references other _unpublished_ domains, this parameter must be `true`. Otherwise, the request will be rejected with status code 424.
};
apiInstance.setDomainLifecycleSettings(owner, domain, version, settings, opts, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **settings** | [**LifecycleSettings**](LifecycleSettings.md)| An object that specifies the new &#x60;published&#x60; state: &#x60;true&#x60; means published, &#x60;false&#x60; - unpublished | 
 **force** | **Boolean**| To publish a domain that references other _unpublished_ domains, this parameter must be &#x60;true&#x60;. Otherwise, the request will be rejected with status code 424. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setDomainPrivateSettings

> setDomainPrivateSettings(owner, domain, version, settings, opts)

Set the visibility (public or private) of a domain version

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let version = "version_example"; // String | Version identifier
let settings = new SwaggerHubRegistryApi.VisibilitySettings(); // VisibilitySettings | An object that specifies the new visibility level: `true` means private, `false` - public
let opts = {
  'force': false // Boolean | To change the visibility from _public_ to _private_ in case this domain is referenced from other _public_ definitions, this parameter must be `true`. Otherwise, the request will be rejected with status code 424.
};
apiInstance.setDomainPrivateSettings(owner, domain, version, settings, opts, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **settings** | [**VisibilitySettings**](VisibilitySettings.md)| An object that specifies the new visibility level: &#x60;true&#x60; means private, &#x60;false&#x60; - public | 
 **force** | **Boolean**| To change the visibility from _public_ to _private_ in case this domain is referenced from other _public_ definitions, this parameter must be &#x60;true&#x60;. Otherwise, the request will be rejected with status code 424. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDomainCommentReplyV2

> Comment updateDomainCommentReplyV2(owner, domain, version, comment, reply, opts)

Update a comment reply

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let version = "version_example"; // String | Version identifier
let comment = "comment_example"; // String | Comment identifier
let reply = "reply_example"; // String | Reply identifier
let opts = {
  'body': new SwaggerHubRegistryApi.CommentPatch() // CommentPatch | 
};
apiInstance.updateDomainCommentReplyV2(owner, domain, version, comment, reply, opts, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **comment** | **String**| Comment identifier | 
 **reply** | **String**| Reply identifier | 
 **body** | [**CommentPatch**](CommentPatch.md)|  | [optional] 

### Return type

[**Comment**](Comment.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDomainCommentV2

> ClosableComment updateDomainCommentV2(owner, domain, version, comment, opts)

Update a comment

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let version = "version_example"; // String | Version identifier
let comment = "comment_example"; // String | Comment identifier
let opts = {
  'body': new SwaggerHubRegistryApi.ClosableCommentPatch() // ClosableCommentPatch | 
};
apiInstance.updateDomainCommentV2(owner, domain, version, comment, opts, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **comment** | **String**| Comment identifier | 
 **body** | [**ClosableCommentPatch**](ClosableCommentPatch.md)|  | [optional] 

### Return type

[**ClosableComment**](ClosableComment.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDomainCommentsV2

> updateDomainCommentsV2(owner, domain, version, body)

Bulk update comments

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.DomainsApi();
let owner = "owner_example"; // String | Domain owner (organization or user, case-sensitive)
let domain = "domain_example"; // String | Domain name (case-sensitive)
let version = "version_example"; // String | Version identifier
let body = new SwaggerHubRegistryApi.CommentsBatch(); // CommentsBatch | 
apiInstance.updateDomainCommentsV2(owner, domain, version, body, (error, data, response) => {
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
 **owner** | **String**| Domain owner (organization or user, case-sensitive) | 
 **domain** | **String**| Domain name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **body** | [**CommentsBatch**](CommentsBatch.md)|  | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

