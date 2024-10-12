# Trello.OrganizationApi

All URIs are relative to *https://trello.com/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addOrganizations**](OrganizationApi.md#addOrganizations) | **POST** /organizations | addOrganizations()
[**addOrganizationsLogoByIdOrg**](OrganizationApi.md#addOrganizationsLogoByIdOrg) | **POST** /organizations/{idOrg}/logo | addOrganizationsLogoByIdOrg()
[**deleteOrganizationsByIdOrg**](OrganizationApi.md#deleteOrganizationsByIdOrg) | **DELETE** /organizations/{idOrg} | deleteOrganizationsByIdOrg()
[**deleteOrganizationsLogoByIdOrg**](OrganizationApi.md#deleteOrganizationsLogoByIdOrg) | **DELETE** /organizations/{idOrg}/logo | deleteOrganizationsLogoByIdOrg()
[**deleteOrganizationsMembersAllByIdOrgByIdMember**](OrganizationApi.md#deleteOrganizationsMembersAllByIdOrgByIdMember) | **DELETE** /organizations/{idOrg}/members/{idMember}/all | deleteOrganizationsMembersAllByIdOrgByIdMember()
[**deleteOrganizationsMembersByIdOrgByIdMember**](OrganizationApi.md#deleteOrganizationsMembersByIdOrgByIdMember) | **DELETE** /organizations/{idOrg}/members/{idMember} | deleteOrganizationsMembersByIdOrgByIdMember()
[**deleteOrganizationsPrefsAssociatedDomainByIdOrg**](OrganizationApi.md#deleteOrganizationsPrefsAssociatedDomainByIdOrg) | **DELETE** /organizations/{idOrg}/prefs/associatedDomain | deleteOrganizationsPrefsAssociatedDomainByIdOrg()
[**deleteOrganizationsPrefsOrgInviteRestrictByIdOrg**](OrganizationApi.md#deleteOrganizationsPrefsOrgInviteRestrictByIdOrg) | **DELETE** /organizations/{idOrg}/prefs/orgInviteRestrict | deleteOrganizationsPrefsOrgInviteRestrictByIdOrg()
[**getOrganizationsActionsByIdOrg**](OrganizationApi.md#getOrganizationsActionsByIdOrg) | **GET** /organizations/{idOrg}/actions | getOrganizationsActionsByIdOrg()
[**getOrganizationsBoardsByIdOrg**](OrganizationApi.md#getOrganizationsBoardsByIdOrg) | **GET** /organizations/{idOrg}/boards | getOrganizationsBoardsByIdOrg()
[**getOrganizationsBoardsByIdOrgByFilter**](OrganizationApi.md#getOrganizationsBoardsByIdOrgByFilter) | **GET** /organizations/{idOrg}/boards/{filter} | getOrganizationsBoardsByIdOrgByFilter()
[**getOrganizationsByIdOrg**](OrganizationApi.md#getOrganizationsByIdOrg) | **GET** /organizations/{idOrg} | getOrganizationsByIdOrg()
[**getOrganizationsByIdOrgByField**](OrganizationApi.md#getOrganizationsByIdOrgByField) | **GET** /organizations/{idOrg}/{field} | getOrganizationsByIdOrgByField()
[**getOrganizationsDeltasByIdOrg**](OrganizationApi.md#getOrganizationsDeltasByIdOrg) | **GET** /organizations/{idOrg}/deltas | getOrganizationsDeltasByIdOrg()
[**getOrganizationsMembersByIdOrg**](OrganizationApi.md#getOrganizationsMembersByIdOrg) | **GET** /organizations/{idOrg}/members | getOrganizationsMembersByIdOrg()
[**getOrganizationsMembersByIdOrgByFilter**](OrganizationApi.md#getOrganizationsMembersByIdOrgByFilter) | **GET** /organizations/{idOrg}/members/{filter} | getOrganizationsMembersByIdOrgByFilter()
[**getOrganizationsMembersCardsByIdOrgByIdMember**](OrganizationApi.md#getOrganizationsMembersCardsByIdOrgByIdMember) | **GET** /organizations/{idOrg}/members/{idMember}/cards | getOrganizationsMembersCardsByIdOrgByIdMember()
[**getOrganizationsMembersInvitedByIdOrg**](OrganizationApi.md#getOrganizationsMembersInvitedByIdOrg) | **GET** /organizations/{idOrg}/membersInvited | getOrganizationsMembersInvitedByIdOrg()
[**getOrganizationsMembersInvitedByIdOrgByField**](OrganizationApi.md#getOrganizationsMembersInvitedByIdOrgByField) | **GET** /organizations/{idOrg}/membersInvited/{field} | getOrganizationsMembersInvitedByIdOrgByField()
[**getOrganizationsMembershipsByIdOrg**](OrganizationApi.md#getOrganizationsMembershipsByIdOrg) | **GET** /organizations/{idOrg}/memberships | getOrganizationsMembershipsByIdOrg()
[**getOrganizationsMembershipsByIdOrgByIdMembership**](OrganizationApi.md#getOrganizationsMembershipsByIdOrgByIdMembership) | **GET** /organizations/{idOrg}/memberships/{idMembership} | getOrganizationsMembershipsByIdOrgByIdMembership()
[**updateOrganizationsByIdOrg**](OrganizationApi.md#updateOrganizationsByIdOrg) | **PUT** /organizations/{idOrg} | updateOrganizationsByIdOrg()
[**updateOrganizationsDescByIdOrg**](OrganizationApi.md#updateOrganizationsDescByIdOrg) | **PUT** /organizations/{idOrg}/desc | updateOrganizationsDescByIdOrg()
[**updateOrganizationsDisplayNameByIdOrg**](OrganizationApi.md#updateOrganizationsDisplayNameByIdOrg) | **PUT** /organizations/{idOrg}/displayName | updateOrganizationsDisplayNameByIdOrg()
[**updateOrganizationsMembersByIdOrg**](OrganizationApi.md#updateOrganizationsMembersByIdOrg) | **PUT** /organizations/{idOrg}/members | updateOrganizationsMembersByIdOrg()
[**updateOrganizationsMembersByIdOrgByIdMember**](OrganizationApi.md#updateOrganizationsMembersByIdOrgByIdMember) | **PUT** /organizations/{idOrg}/members/{idMember} | updateOrganizationsMembersByIdOrgByIdMember()
[**updateOrganizationsMembersDeactivatedByIdOrgByIdMember**](OrganizationApi.md#updateOrganizationsMembersDeactivatedByIdOrgByIdMember) | **PUT** /organizations/{idOrg}/members/{idMember}/deactivated | updateOrganizationsMembersDeactivatedByIdOrgByIdMember()
[**updateOrganizationsMembershipsByIdOrgByIdMembership**](OrganizationApi.md#updateOrganizationsMembershipsByIdOrgByIdMembership) | **PUT** /organizations/{idOrg}/memberships/{idMembership} | updateOrganizationsMembershipsByIdOrgByIdMembership()
[**updateOrganizationsNameByIdOrg**](OrganizationApi.md#updateOrganizationsNameByIdOrg) | **PUT** /organizations/{idOrg}/name | updateOrganizationsNameByIdOrg()
[**updateOrganizationsPrefsAssociatedDomainByIdOrg**](OrganizationApi.md#updateOrganizationsPrefsAssociatedDomainByIdOrg) | **PUT** /organizations/{idOrg}/prefs/associatedDomain | updateOrganizationsPrefsAssociatedDomainByIdOrg()
[**updateOrganizationsPrefsBoardVisibilityRestrictOrgByIdOrg**](OrganizationApi.md#updateOrganizationsPrefsBoardVisibilityRestrictOrgByIdOrg) | **PUT** /organizations/{idOrg}/prefs/boardVisibilityRestrict/org | updateOrganizationsPrefsBoardVisibilityRestrictOrgByIdOrg()
[**updateOrganizationsPrefsBoardVisibilityRestrictPrivateByIdOrg**](OrganizationApi.md#updateOrganizationsPrefsBoardVisibilityRestrictPrivateByIdOrg) | **PUT** /organizations/{idOrg}/prefs/boardVisibilityRestrict/private | updateOrganizationsPrefsBoardVisibilityRestrictPrivateByIdOrg()
[**updateOrganizationsPrefsBoardVisibilityRestrictPublicByIdOrg**](OrganizationApi.md#updateOrganizationsPrefsBoardVisibilityRestrictPublicByIdOrg) | **PUT** /organizations/{idOrg}/prefs/boardVisibilityRestrict/public | updateOrganizationsPrefsBoardVisibilityRestrictPublicByIdOrg()
[**updateOrganizationsPrefsExternalMembersDisabledByIdOrg**](OrganizationApi.md#updateOrganizationsPrefsExternalMembersDisabledByIdOrg) | **PUT** /organizations/{idOrg}/prefs/externalMembersDisabled | updateOrganizationsPrefsExternalMembersDisabledByIdOrg()
[**updateOrganizationsPrefsGoogleAppsVersionByIdOrg**](OrganizationApi.md#updateOrganizationsPrefsGoogleAppsVersionByIdOrg) | **PUT** /organizations/{idOrg}/prefs/googleAppsVersion | updateOrganizationsPrefsGoogleAppsVersionByIdOrg()
[**updateOrganizationsPrefsOrgInviteRestrictByIdOrg**](OrganizationApi.md#updateOrganizationsPrefsOrgInviteRestrictByIdOrg) | **PUT** /organizations/{idOrg}/prefs/orgInviteRestrict | updateOrganizationsPrefsOrgInviteRestrictByIdOrg()
[**updateOrganizationsPrefsPermissionLevelByIdOrg**](OrganizationApi.md#updateOrganizationsPrefsPermissionLevelByIdOrg) | **PUT** /organizations/{idOrg}/prefs/permissionLevel | updateOrganizationsPrefsPermissionLevelByIdOrg()
[**updateOrganizationsWebsiteByIdOrg**](OrganizationApi.md#updateOrganizationsWebsiteByIdOrg) | **PUT** /organizations/{idOrg}/website | updateOrganizationsWebsiteByIdOrg()



## addOrganizations

> addOrganizations(key, token, organizations)

addOrganizations()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let organizations = new Trello.Organizations(); // Organizations | Attributes of \"Organizations\" to be added.
apiInstance.addOrganizations(key, token, organizations, (error, data, response) => {
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
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **organizations** | [**Organizations**](Organizations.md)| Attributes of \&quot;Organizations\&quot; to be added. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## addOrganizationsLogoByIdOrg

> addOrganizationsLogoByIdOrg(idOrg, key, token, organizationsLogo)

addOrganizationsLogoByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let organizationsLogo = new Trello.OrganizationsLogo(); // OrganizationsLogo | Attributes of \"Organizations Logo\" to be added.
apiInstance.addOrganizationsLogoByIdOrg(idOrg, key, token, organizationsLogo, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **organizationsLogo** | [**OrganizationsLogo**](OrganizationsLogo.md)| Attributes of \&quot;Organizations Logo\&quot; to be added. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## deleteOrganizationsByIdOrg

> deleteOrganizationsByIdOrg(idOrg, key, token)

deleteOrganizationsByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.deleteOrganizationsByIdOrg(idOrg, key, token, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationsLogoByIdOrg

> deleteOrganizationsLogoByIdOrg(idOrg, key, token)

deleteOrganizationsLogoByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.deleteOrganizationsLogoByIdOrg(idOrg, key, token, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationsMembersAllByIdOrgByIdMember

> deleteOrganizationsMembersAllByIdOrgByIdMember(idOrg, idMember, key, token)

deleteOrganizationsMembersAllByIdOrgByIdMember()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let idMember = "idMember_example"; // String | idMember
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.deleteOrganizationsMembersAllByIdOrgByIdMember(idOrg, idMember, key, token, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **idMember** | **String**| idMember | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationsMembersByIdOrgByIdMember

> deleteOrganizationsMembersByIdOrgByIdMember(idOrg, idMember, key, token)

deleteOrganizationsMembersByIdOrgByIdMember()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let idMember = "idMember_example"; // String | idMember
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.deleteOrganizationsMembersByIdOrgByIdMember(idOrg, idMember, key, token, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **idMember** | **String**| idMember | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationsPrefsAssociatedDomainByIdOrg

> deleteOrganizationsPrefsAssociatedDomainByIdOrg(idOrg, key, token)

deleteOrganizationsPrefsAssociatedDomainByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.deleteOrganizationsPrefsAssociatedDomainByIdOrg(idOrg, key, token, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationsPrefsOrgInviteRestrictByIdOrg

> deleteOrganizationsPrefsOrgInviteRestrictByIdOrg(idOrg, value, key, token)

deleteOrganizationsPrefsOrgInviteRestrictByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let value = "value_example"; // String | An email address with optional expansion tokens
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.deleteOrganizationsPrefsOrgInviteRestrictByIdOrg(idOrg, value, key, token, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **value** | **String**| An email address with optional expansion tokens | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationsActionsByIdOrg

> getOrganizationsActionsByIdOrg(idOrg, key, token, opts)

getOrganizationsActionsByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'entities': "entities_example", // String |  true or false
  'display': "display_example", // String |  true or false
  'filter': "'all'", // String | all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
  'fields': "'all'", // String | all or a comma-separated list of: data, date, idMemberCreator or type
  'limit': "'50'", // String | a number from 0 to 1000
  'format': "'list'", // String | One of: count, list or minimal
  'since': "since_example", // String | A date, null or lastView
  'before': "before_example", // String | A date, or null
  'page': "'0'", // String | Page * limit must be less than 1000
  'idModels': "idModels_example", // String | Only return actions related to these model ids
  'member': "member_example", // String |  true or false
  'memberFields': "'avatarHash, fullName, initials and username'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'memberCreator': "memberCreator_example", // String |  true or false
  'memberCreatorFields': "'avatarHash, fullName, initials and username'" // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
};
apiInstance.getOrganizationsActionsByIdOrg(idOrg, key, token, opts, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **entities** | **String**|  true or false | [optional] 
 **display** | **String**|  true or false | [optional] 
 **filter** | **String**| all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization | [optional] [default to &#39;all&#39;]
 **fields** | **String**| all or a comma-separated list of: data, date, idMemberCreator or type | [optional] [default to &#39;all&#39;]
 **limit** | **String**| a number from 0 to 1000 | [optional] [default to &#39;50&#39;]
 **format** | **String**| One of: count, list or minimal | [optional] [default to &#39;list&#39;]
 **since** | **String**| A date, null or lastView | [optional] 
 **before** | **String**| A date, or null | [optional] 
 **page** | **String**| Page * limit must be less than 1000 | [optional] [default to &#39;0&#39;]
 **idModels** | **String**| Only return actions related to these model ids | [optional] 
 **member** | **String**|  true or false | [optional] 
 **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, fullName, initials and username&#39;]
 **memberCreator** | **String**|  true or false | [optional] 
 **memberCreatorFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, fullName, initials and username&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationsBoardsByIdOrg

> getOrganizationsBoardsByIdOrg(idOrg, key, token, opts)

getOrganizationsBoardsByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'filter': "'all'", // String | all or a comma-separated list of: closed, members, open, organization, pinned, public, starred or unpinned
  'fields': "'all'", // String | all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
  'actions': "actions_example", // String | all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
  'actionsEntities': "actionsEntities_example", // String |  true or false
  'actionsLimit': "'50'", // String | a number from 0 to 1000
  'actionsFormat': "'list'", // String | One of: count, list or minimal
  'actionsSince': "actionsSince_example", // String | A date, null or lastView
  'actionFields': "'all'", // String | all or a comma-separated list of: data, date, idMemberCreator or type
  'memberships': "'none'", // String | all or a comma-separated list of: active, admin, deactivated, me or normal
  'organization': "organization_example", // String |  true or false
  'organizationFields': "'name and displayName'", // String | all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
  'lists': "'none'" // String | One of: all, closed, none or open
};
apiInstance.getOrganizationsBoardsByIdOrg(idOrg, key, token, opts, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **filter** | **String**| all or a comma-separated list of: closed, members, open, organization, pinned, public, starred or unpinned | [optional] [default to &#39;all&#39;]
 **fields** | **String**| all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url | [optional] [default to &#39;all&#39;]
 **actions** | **String**| all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization | [optional] 
 **actionsEntities** | **String**|  true or false | [optional] 
 **actionsLimit** | **String**| a number from 0 to 1000 | [optional] [default to &#39;50&#39;]
 **actionsFormat** | **String**| One of: count, list or minimal | [optional] [default to &#39;list&#39;]
 **actionsSince** | **String**| A date, null or lastView | [optional] 
 **actionFields** | **String**| all or a comma-separated list of: data, date, idMemberCreator or type | [optional] [default to &#39;all&#39;]
 **memberships** | **String**| all or a comma-separated list of: active, admin, deactivated, me or normal | [optional] [default to &#39;none&#39;]
 **organization** | **String**|  true or false | [optional] 
 **organizationFields** | **String**| all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website | [optional] [default to &#39;name and displayName&#39;]
 **lists** | **String**| One of: all, closed, none or open | [optional] [default to &#39;none&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationsBoardsByIdOrgByFilter

> getOrganizationsBoardsByIdOrgByFilter(idOrg, filter, key, token)

getOrganizationsBoardsByIdOrgByFilter()

### Example

```javascript
import Trello from 'trello';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let filter = "filter_example"; // String | filter
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getOrganizationsBoardsByIdOrgByFilter(idOrg, filter, key, token, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **filter** | **String**| filter | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationsByIdOrg

> getOrganizationsByIdOrg(idOrg, key, token, opts)

getOrganizationsByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'actions': "actions_example", // String | all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
  'actionsEntities': "actionsEntities_example", // String |  true or false
  'actionsDisplay': "actionsDisplay_example", // String |  true or false
  'actionsLimit': "'50'", // String | a number from 0 to 1000
  'actionFields': "'all'", // String | all or a comma-separated list of: data, date, idMemberCreator or type
  'memberships': "'none'", // String | all or a comma-separated list of: active, admin, deactivated, me or normal
  'membershipsMember': "membershipsMember_example", // String |  true or false
  'membershipsMemberFields': "'fullName and username'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'members': "'none'", // String | One of: admins, all, none, normal or owners
  'memberFields': "'avatarHash, fullName, initials, username and confirmed'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'memberActivity': "memberActivity_example", // String | true or false ; works for premium organizations only.
  'membersInvited': "'none'", // String | One of: admins, all, none, normal or owners
  'membersInvitedFields': "'avatarHash, initials, fullName and username'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'boards': "'none'", // String | all or a comma-separated list of: closed, members, open, organization, pinned, public, starred or unpinned
  'boardFields': "'all'", // String | all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
  'boardActions': "boardActions_example", // String | all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
  'boardActionsEntities': "boardActionsEntities_example", // String |  true or false
  'boardActionsDisplay': "boardActionsDisplay_example", // String |  true or false
  'boardActionsFormat': "'list'", // String | One of: count, list or minimal
  'boardActionsSince': "boardActionsSince_example", // String | A date, null or lastView
  'boardActionsLimit': "'50'", // String | a number from 0 to 1000
  'boardActionFields': "'all'", // String | all or a comma-separated list of: data, date, idMemberCreator or type
  'boardLists': "'none'", // String | One of: all, closed, none or open
  'paidAccount': "paidAccount_example", // String |  true or false
  'fields': "'name, displayName, desc, descData, url, website, logoHash, products and powerUps'" // String | all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website
};
apiInstance.getOrganizationsByIdOrg(idOrg, key, token, opts, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **actions** | **String**| all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization | [optional] 
 **actionsEntities** | **String**|  true or false | [optional] 
 **actionsDisplay** | **String**|  true or false | [optional] 
 **actionsLimit** | **String**| a number from 0 to 1000 | [optional] [default to &#39;50&#39;]
 **actionFields** | **String**| all or a comma-separated list of: data, date, idMemberCreator or type | [optional] [default to &#39;all&#39;]
 **memberships** | **String**| all or a comma-separated list of: active, admin, deactivated, me or normal | [optional] [default to &#39;none&#39;]
 **membershipsMember** | **String**|  true or false | [optional] 
 **membershipsMemberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;fullName and username&#39;]
 **members** | **String**| One of: admins, all, none, normal or owners | [optional] [default to &#39;none&#39;]
 **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, fullName, initials, username and confirmed&#39;]
 **memberActivity** | **String**| true or false ; works for premium organizations only. | [optional] 
 **membersInvited** | **String**| One of: admins, all, none, normal or owners | [optional] [default to &#39;none&#39;]
 **membersInvitedFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, initials, fullName and username&#39;]
 **boards** | **String**| all or a comma-separated list of: closed, members, open, organization, pinned, public, starred or unpinned | [optional] [default to &#39;none&#39;]
 **boardFields** | **String**| all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url | [optional] [default to &#39;all&#39;]
 **boardActions** | **String**| all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization | [optional] 
 **boardActionsEntities** | **String**|  true or false | [optional] 
 **boardActionsDisplay** | **String**|  true or false | [optional] 
 **boardActionsFormat** | **String**| One of: count, list or minimal | [optional] [default to &#39;list&#39;]
 **boardActionsSince** | **String**| A date, null or lastView | [optional] 
 **boardActionsLimit** | **String**| a number from 0 to 1000 | [optional] [default to &#39;50&#39;]
 **boardActionFields** | **String**| all or a comma-separated list of: data, date, idMemberCreator or type | [optional] [default to &#39;all&#39;]
 **boardLists** | **String**| One of: all, closed, none or open | [optional] [default to &#39;none&#39;]
 **paidAccount** | **String**|  true or false | [optional] 
 **fields** | **String**| all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website | [optional] [default to &#39;name, displayName, desc, descData, url, website, logoHash, products and powerUps&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationsByIdOrgByField

> getOrganizationsByIdOrgByField(idOrg, field, key, token)

getOrganizationsByIdOrgByField()

### Example

```javascript
import Trello from 'trello';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let field = "field_example"; // String | field
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getOrganizationsByIdOrgByField(idOrg, field, key, token, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **field** | **String**| field | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationsDeltasByIdOrg

> getOrganizationsDeltasByIdOrg(idOrg, tags, ixLastUpdate, key, token)

getOrganizationsDeltasByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let tags = "tags_example"; // String | A valid tag for subscribing
let ixLastUpdate = "ixLastUpdate_example"; // String | a number from -1 to Infinity
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getOrganizationsDeltasByIdOrg(idOrg, tags, ixLastUpdate, key, token, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **tags** | **String**| A valid tag for subscribing | 
 **ixLastUpdate** | **String**| a number from -1 to Infinity | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationsMembersByIdOrg

> getOrganizationsMembersByIdOrg(idOrg, key, token, opts)

getOrganizationsMembersByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'filter': "'all'", // String | One of: admins, all, none, normal or owners
  'fields': "'fullName and username'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'activity': "activity_example" // String | true or false ; works for premium organizations only.
};
apiInstance.getOrganizationsMembersByIdOrg(idOrg, key, token, opts, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **filter** | **String**| One of: admins, all, none, normal or owners | [optional] [default to &#39;all&#39;]
 **fields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;fullName and username&#39;]
 **activity** | **String**| true or false ; works for premium organizations only. | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationsMembersByIdOrgByFilter

> getOrganizationsMembersByIdOrgByFilter(idOrg, filter, key, token)

getOrganizationsMembersByIdOrgByFilter()

### Example

```javascript
import Trello from 'trello';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let filter = "filter_example"; // String | filter
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getOrganizationsMembersByIdOrgByFilter(idOrg, filter, key, token, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **filter** | **String**| filter | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationsMembersCardsByIdOrgByIdMember

> getOrganizationsMembersCardsByIdOrgByIdMember(idOrg, idMember, key, token, opts)

getOrganizationsMembersCardsByIdOrgByIdMember()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let idMember = "idMember_example"; // String | idMember
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'actions': "actions_example", // String | all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization
  'attachments': "attachments_example", // String | A boolean value or &quot;cover&quot; for only card cover attachments
  'attachmentFields': "'all'", // String | all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url
  'members': "members_example", // String |  true or false
  'memberFields': "'avatarHash, fullName, initials and username'", // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
  'checkItemStates': "checkItemStates_example", // String |  true or false
  'checklists': "'none'", // String | One of: all or none
  'board': "board_example", // String |  true or false
  'boardFields': "'name, desc, closed, idOrganization, pinned, url and prefs'", // String | all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url
  'list': "list_example", // String |  true or false
  'listFields': "'all'", // String | all or a comma-separated list of: closed, idBoard, name, pos or subscribed
  'filter': "'visible'", // String | One of: all, closed, none, open or visible
  'fields': "'all'" // String | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url
};
apiInstance.getOrganizationsMembersCardsByIdOrgByIdMember(idOrg, idMember, key, token, opts, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **idMember** | **String**| idMember | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **actions** | **String**| all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization | [optional] 
 **attachments** | **String**| A boolean value or &amp;quot;cover&amp;quot; for only card cover attachments | [optional] 
 **attachmentFields** | **String**| all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url | [optional] [default to &#39;all&#39;]
 **members** | **String**|  true or false | [optional] 
 **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;avatarHash, fullName, initials and username&#39;]
 **checkItemStates** | **String**|  true or false | [optional] 
 **checklists** | **String**| One of: all or none | [optional] [default to &#39;none&#39;]
 **board** | **String**|  true or false | [optional] 
 **boardFields** | **String**| all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url | [optional] [default to &#39;name, desc, closed, idOrganization, pinned, url and prefs&#39;]
 **list** | **String**|  true or false | [optional] 
 **listFields** | **String**| all or a comma-separated list of: closed, idBoard, name, pos or subscribed | [optional] [default to &#39;all&#39;]
 **filter** | **String**| One of: all, closed, none, open or visible | [optional] [default to &#39;visible&#39;]
 **fields** | **String**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url | [optional] [default to &#39;all&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationsMembersInvitedByIdOrg

> getOrganizationsMembersInvitedByIdOrg(idOrg, key, token, opts)

getOrganizationsMembersInvitedByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'fields': "'all'" // String | all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username
};
apiInstance.getOrganizationsMembersInvitedByIdOrg(idOrg, key, token, opts, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **fields** | **String**| all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username | [optional] [default to &#39;all&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationsMembersInvitedByIdOrgByField

> getOrganizationsMembersInvitedByIdOrgByField(idOrg, field, key, token)

getOrganizationsMembersInvitedByIdOrgByField()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let field = "field_example"; // String | field
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
apiInstance.getOrganizationsMembersInvitedByIdOrgByField(idOrg, field, key, token, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **field** | **String**| field | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationsMembershipsByIdOrg

> getOrganizationsMembershipsByIdOrg(idOrg, key, token, opts)

getOrganizationsMembershipsByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'filter': "'all'", // String | all or a comma-separated list of: active, admin, deactivated, me or normal
  'member': "member_example", // String |  true or false
  'memberFields': "'fullName and username'" // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
};
apiInstance.getOrganizationsMembershipsByIdOrg(idOrg, key, token, opts, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **filter** | **String**| all or a comma-separated list of: active, admin, deactivated, me or normal | [optional] [default to &#39;all&#39;]
 **member** | **String**|  true or false | [optional] 
 **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;fullName and username&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizationsMembershipsByIdOrgByIdMembership

> getOrganizationsMembershipsByIdOrgByIdMembership(idOrg, idMembership, key, token, opts)

getOrganizationsMembershipsByIdOrgByIdMembership()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let idMembership = "idMembership_example"; // String | idMembership
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let opts = {
  'member': "member_example", // String |  true or false
  'memberFields': "'fullName and username'" // String | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username
};
apiInstance.getOrganizationsMembershipsByIdOrgByIdMembership(idOrg, idMembership, key, token, opts, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **idMembership** | **String**| idMembership | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **member** | **String**|  true or false | [optional] 
 **memberFields** | **String**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username | [optional] [default to &#39;fullName and username&#39;]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateOrganizationsByIdOrg

> updateOrganizationsByIdOrg(idOrg, key, token, organizations)

updateOrganizationsByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let organizations = new Trello.Organizations(); // Organizations | Attributes of \"Organizations\" to be updated.
apiInstance.updateOrganizationsByIdOrg(idOrg, key, token, organizations, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **organizations** | [**Organizations**](Organizations.md)| Attributes of \&quot;Organizations\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateOrganizationsDescByIdOrg

> updateOrganizationsDescByIdOrg(idOrg, key, token, organizationsDesc)

updateOrganizationsDescByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let organizationsDesc = new Trello.OrganizationsDesc(); // OrganizationsDesc | Attributes of \"Organizations Desc\" to be updated.
apiInstance.updateOrganizationsDescByIdOrg(idOrg, key, token, organizationsDesc, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **organizationsDesc** | [**OrganizationsDesc**](OrganizationsDesc.md)| Attributes of \&quot;Organizations Desc\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateOrganizationsDisplayNameByIdOrg

> updateOrganizationsDisplayNameByIdOrg(idOrg, key, token, organizationsDisplayName)

updateOrganizationsDisplayNameByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let organizationsDisplayName = new Trello.OrganizationsDisplayName(); // OrganizationsDisplayName | Attributes of \"Organizations Display Name\" to be updated.
apiInstance.updateOrganizationsDisplayNameByIdOrg(idOrg, key, token, organizationsDisplayName, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **organizationsDisplayName** | [**OrganizationsDisplayName**](OrganizationsDisplayName.md)| Attributes of \&quot;Organizations Display Name\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateOrganizationsMembersByIdOrg

> updateOrganizationsMembersByIdOrg(idOrg, key, token, organizationsMembers)

updateOrganizationsMembersByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let organizationsMembers = new Trello.OrganizationsMembers(); // OrganizationsMembers | Attributes of \"Organizations Members\" to be updated.
apiInstance.updateOrganizationsMembersByIdOrg(idOrg, key, token, organizationsMembers, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **organizationsMembers** | [**OrganizationsMembers**](OrganizationsMembers.md)| Attributes of \&quot;Organizations Members\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateOrganizationsMembersByIdOrgByIdMember

> updateOrganizationsMembersByIdOrgByIdMember(idOrg, idMember, key, token, organizationsMembers)

updateOrganizationsMembersByIdOrgByIdMember()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let idMember = "idMember_example"; // String | idMember
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let organizationsMembers = new Trello.OrganizationsMembers(); // OrganizationsMembers | Attributes of \"Organizations Members\" to be updated.
apiInstance.updateOrganizationsMembersByIdOrgByIdMember(idOrg, idMember, key, token, organizationsMembers, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **idMember** | **String**| idMember | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **organizationsMembers** | [**OrganizationsMembers**](OrganizationsMembers.md)| Attributes of \&quot;Organizations Members\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateOrganizationsMembersDeactivatedByIdOrgByIdMember

> updateOrganizationsMembersDeactivatedByIdOrgByIdMember(idOrg, idMember, key, token, organizationsMembersDeactivated)

updateOrganizationsMembersDeactivatedByIdOrgByIdMember()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let idMember = "idMember_example"; // String | idMember
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let organizationsMembersDeactivated = new Trello.OrganizationsMembersDeactivated(); // OrganizationsMembersDeactivated | Attributes of \"Organizations Members Deactivated\" to be updated.
apiInstance.updateOrganizationsMembersDeactivatedByIdOrgByIdMember(idOrg, idMember, key, token, organizationsMembersDeactivated, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **idMember** | **String**| idMember | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **organizationsMembersDeactivated** | [**OrganizationsMembersDeactivated**](OrganizationsMembersDeactivated.md)| Attributes of \&quot;Organizations Members Deactivated\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateOrganizationsMembershipsByIdOrgByIdMembership

> updateOrganizationsMembershipsByIdOrgByIdMembership(idOrg, idMembership, key, token, organizationsMemberships)

updateOrganizationsMembershipsByIdOrgByIdMembership()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let idMembership = "idMembership_example"; // String | idMembership
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let organizationsMemberships = new Trello.OrganizationsMemberships(); // OrganizationsMemberships | Attributes of \"Organizations Memberships\" to be updated.
apiInstance.updateOrganizationsMembershipsByIdOrgByIdMembership(idOrg, idMembership, key, token, organizationsMemberships, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **idMembership** | **String**| idMembership | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **organizationsMemberships** | [**OrganizationsMemberships**](OrganizationsMemberships.md)| Attributes of \&quot;Organizations Memberships\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateOrganizationsNameByIdOrg

> updateOrganizationsNameByIdOrg(idOrg, key, token, organizationsName)

updateOrganizationsNameByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let organizationsName = new Trello.OrganizationsName(); // OrganizationsName | Attributes of \"Organizations Name\" to be updated.
apiInstance.updateOrganizationsNameByIdOrg(idOrg, key, token, organizationsName, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **organizationsName** | [**OrganizationsName**](OrganizationsName.md)| Attributes of \&quot;Organizations Name\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateOrganizationsPrefsAssociatedDomainByIdOrg

> updateOrganizationsPrefsAssociatedDomainByIdOrg(idOrg, key, token, prefsAssociatedDomain)

updateOrganizationsPrefsAssociatedDomainByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let prefsAssociatedDomain = new Trello.PrefsAssociatedDomain(); // PrefsAssociatedDomain | Attributes of \"Prefs Associated Domain\" to be updated.
apiInstance.updateOrganizationsPrefsAssociatedDomainByIdOrg(idOrg, key, token, prefsAssociatedDomain, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **prefsAssociatedDomain** | [**PrefsAssociatedDomain**](PrefsAssociatedDomain.md)| Attributes of \&quot;Prefs Associated Domain\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateOrganizationsPrefsBoardVisibilityRestrictOrgByIdOrg

> updateOrganizationsPrefsBoardVisibilityRestrictOrgByIdOrg(idOrg, key, token, prefsBoardVisibilityRestrict)

updateOrganizationsPrefsBoardVisibilityRestrictOrgByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let prefsBoardVisibilityRestrict = new Trello.PrefsBoardVisibilityRestrict(); // PrefsBoardVisibilityRestrict | Attributes of \"Prefs Board Visibility Restrict\" to be updated.
apiInstance.updateOrganizationsPrefsBoardVisibilityRestrictOrgByIdOrg(idOrg, key, token, prefsBoardVisibilityRestrict, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **prefsBoardVisibilityRestrict** | [**PrefsBoardVisibilityRestrict**](PrefsBoardVisibilityRestrict.md)| Attributes of \&quot;Prefs Board Visibility Restrict\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateOrganizationsPrefsBoardVisibilityRestrictPrivateByIdOrg

> updateOrganizationsPrefsBoardVisibilityRestrictPrivateByIdOrg(idOrg, key, token, prefsBoardVisibilityRestrict)

updateOrganizationsPrefsBoardVisibilityRestrictPrivateByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let prefsBoardVisibilityRestrict = new Trello.PrefsBoardVisibilityRestrict(); // PrefsBoardVisibilityRestrict | Attributes of \"Prefs Board Visibility Restrict\" to be updated.
apiInstance.updateOrganizationsPrefsBoardVisibilityRestrictPrivateByIdOrg(idOrg, key, token, prefsBoardVisibilityRestrict, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **prefsBoardVisibilityRestrict** | [**PrefsBoardVisibilityRestrict**](PrefsBoardVisibilityRestrict.md)| Attributes of \&quot;Prefs Board Visibility Restrict\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateOrganizationsPrefsBoardVisibilityRestrictPublicByIdOrg

> updateOrganizationsPrefsBoardVisibilityRestrictPublicByIdOrg(idOrg, key, token, prefsBoardVisibilityRestrict)

updateOrganizationsPrefsBoardVisibilityRestrictPublicByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let prefsBoardVisibilityRestrict = new Trello.PrefsBoardVisibilityRestrict(); // PrefsBoardVisibilityRestrict | Attributes of \"Prefs Board Visibility Restrict\" to be updated.
apiInstance.updateOrganizationsPrefsBoardVisibilityRestrictPublicByIdOrg(idOrg, key, token, prefsBoardVisibilityRestrict, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **prefsBoardVisibilityRestrict** | [**PrefsBoardVisibilityRestrict**](PrefsBoardVisibilityRestrict.md)| Attributes of \&quot;Prefs Board Visibility Restrict\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateOrganizationsPrefsExternalMembersDisabledByIdOrg

> updateOrganizationsPrefsExternalMembersDisabledByIdOrg(idOrg, key, token, prefsExternalMembersDisabled)

updateOrganizationsPrefsExternalMembersDisabledByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let prefsExternalMembersDisabled = new Trello.PrefsExternalMembersDisabled(); // PrefsExternalMembersDisabled | Attributes of \"Prefs External Members Disabled\" to be updated.
apiInstance.updateOrganizationsPrefsExternalMembersDisabledByIdOrg(idOrg, key, token, prefsExternalMembersDisabled, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **prefsExternalMembersDisabled** | [**PrefsExternalMembersDisabled**](PrefsExternalMembersDisabled.md)| Attributes of \&quot;Prefs External Members Disabled\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateOrganizationsPrefsGoogleAppsVersionByIdOrg

> updateOrganizationsPrefsGoogleAppsVersionByIdOrg(idOrg, key, token, prefsGoogleAppsVersion)

updateOrganizationsPrefsGoogleAppsVersionByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let prefsGoogleAppsVersion = new Trello.PrefsGoogleAppsVersion(); // PrefsGoogleAppsVersion | Attributes of \"Prefs Google Apps Version\" to be updated.
apiInstance.updateOrganizationsPrefsGoogleAppsVersionByIdOrg(idOrg, key, token, prefsGoogleAppsVersion, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **prefsGoogleAppsVersion** | [**PrefsGoogleAppsVersion**](PrefsGoogleAppsVersion.md)| Attributes of \&quot;Prefs Google Apps Version\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateOrganizationsPrefsOrgInviteRestrictByIdOrg

> updateOrganizationsPrefsOrgInviteRestrictByIdOrg(idOrg, key, token, prefsOrgInviteRestrict)

updateOrganizationsPrefsOrgInviteRestrictByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let prefsOrgInviteRestrict = new Trello.PrefsOrgInviteRestrict(); // PrefsOrgInviteRestrict | Attributes of \"Prefs Org Invite Restrict\" to be updated.
apiInstance.updateOrganizationsPrefsOrgInviteRestrictByIdOrg(idOrg, key, token, prefsOrgInviteRestrict, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **prefsOrgInviteRestrict** | [**PrefsOrgInviteRestrict**](PrefsOrgInviteRestrict.md)| Attributes of \&quot;Prefs Org Invite Restrict\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateOrganizationsPrefsPermissionLevelByIdOrg

> updateOrganizationsPrefsPermissionLevelByIdOrg(idOrg, key, token, prefsPermissionLevel)

updateOrganizationsPrefsPermissionLevelByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let prefsPermissionLevel = new Trello.PrefsPermissionLevel(); // PrefsPermissionLevel | Attributes of \"Prefs Permission Level\" to be updated.
apiInstance.updateOrganizationsPrefsPermissionLevelByIdOrg(idOrg, key, token, prefsPermissionLevel, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **prefsPermissionLevel** | [**PrefsPermissionLevel**](PrefsPermissionLevel.md)| Attributes of \&quot;Prefs Permission Level\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateOrganizationsWebsiteByIdOrg

> updateOrganizationsWebsiteByIdOrg(idOrg, key, token, organizationsWebsite)

updateOrganizationsWebsiteByIdOrg()

### Example

```javascript
import Trello from 'trello';
let defaultClient = Trello.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: api_token
let api_token = defaultClient.authentications['api_token'];
api_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_token.apiKeyPrefix = 'Token';

let apiInstance = new Trello.OrganizationApi();
let idOrg = "idOrg_example"; // String | idOrg or name
let key = "key_example"; // String | <a href=\"https://trello.com/1/appKey/generate\"  target=\"_blank\">Generate your application key</a>
let token = "token_example"; // String | <a href=\"https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\"  target=\"_blank\">Getting a token from a user</a>
let organizationsWebsite = new Trello.OrganizationsWebsite(); // OrganizationsWebsite | Attributes of \"Organizations Website\" to be updated.
apiInstance.updateOrganizationsWebsiteByIdOrg(idOrg, key, token, organizationsWebsite, (error, data, response) => {
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
 **idOrg** | **String**| idOrg or name | 
 **key** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt; | 
 **token** | **String**| &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt; | 
 **organizationsWebsite** | [**OrganizationsWebsite**](OrganizationsWebsite.md)| Attributes of \&quot;Organizations Website\&quot; to be updated. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

