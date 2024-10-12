# DracoonApi.SystemAuthConfigApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAdConfig**](SystemAuthConfigApi.md#createAdConfig) | **POST** /v4/system/config/auth/ads | Create Active Directory configuration
[**createOAuthClient**](SystemAuthConfigApi.md#createOAuthClient) | **POST** /v4/system/config/oauth/clients | Create OAuth client
[**createOpenIdIdpConfig**](SystemAuthConfigApi.md#createOpenIdIdpConfig) | **POST** /v4/system/config/auth/openid/idps | Create OpenID Connect IDP configuration
[**createRadiusConfig**](SystemAuthConfigApi.md#createRadiusConfig) | **POST** /v4/system/config/auth/radius | Create RADIUS configuration
[**removeAdConfig**](SystemAuthConfigApi.md#removeAdConfig) | **DELETE** /v4/system/config/auth/ads/{ad_id} | Remove Active Directory configuration
[**removeOAuthClient**](SystemAuthConfigApi.md#removeOAuthClient) | **DELETE** /v4/system/config/oauth/clients/{client_id} | Remove OAuth client
[**removeOpenIdIdpConfig**](SystemAuthConfigApi.md#removeOpenIdIdpConfig) | **DELETE** /v4/system/config/auth/openid/idps/{idp_id} | Remove OpenID Connect IDP configuration
[**removeRadiusConfig**](SystemAuthConfigApi.md#removeRadiusConfig) | **DELETE** /v4/system/config/auth/radius | Remove RADIUS configuration
[**requestAdConfig**](SystemAuthConfigApi.md#requestAdConfig) | **GET** /v4/system/config/auth/ads/{ad_id} | Request Active Directory configuration
[**requestAdConfigs**](SystemAuthConfigApi.md#requestAdConfigs) | **GET** /v4/system/config/auth/ads | Request list of Active Directory configurations
[**requestOAuthClient**](SystemAuthConfigApi.md#requestOAuthClient) | **GET** /v4/system/config/oauth/clients/{client_id} | Request OAuth client
[**requestOAuthClients**](SystemAuthConfigApi.md#requestOAuthClients) | **GET** /v4/system/config/oauth/clients | Request list of OAuth clients
[**requestOpenIdIdpConfig**](SystemAuthConfigApi.md#requestOpenIdIdpConfig) | **GET** /v4/system/config/auth/openid/idps/{idp_id} | Request OpenID Connect IDP configuration
[**requestOpenIdIdpConfigs**](SystemAuthConfigApi.md#requestOpenIdIdpConfigs) | **GET** /v4/system/config/auth/openid/idps | Request list of OpenID Connect IDP configurations
[**requestRadiusConfig**](SystemAuthConfigApi.md#requestRadiusConfig) | **GET** /v4/system/config/auth/radius | Request RADIUS configuration
[**testAdConfig**](SystemAuthConfigApi.md#testAdConfig) | **POST** /v4/system/config/actions/test/ad | Test Active Directory configuration
[**testRadiusConfig**](SystemAuthConfigApi.md#testRadiusConfig) | **POST** /v4/system/config/actions/test/radius | Test RADIUS server availability
[**updateAdConfig**](SystemAuthConfigApi.md#updateAdConfig) | **PUT** /v4/system/config/auth/ads/{ad_id} | Update Active Directory configuration
[**updateOAuthClient**](SystemAuthConfigApi.md#updateOAuthClient) | **PUT** /v4/system/config/oauth/clients/{client_id} | Update OAuth client
[**updateOpenIdIdpConfig**](SystemAuthConfigApi.md#updateOpenIdIdpConfig) | **PUT** /v4/system/config/auth/openid/idps/{idp_id} | Update OpenID Connect IDP configuration
[**updateRadiusConfig**](SystemAuthConfigApi.md#updateRadiusConfig) | **PUT** /v4/system/config/auth/radius | Update RADIUS configuration



## createAdConfig

> ActiveDirectoryConfig createAdConfig(createActiveDirectoryConfigRequest, opts)

Create Active Directory configuration

### Description: Create a new Active Directory configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; of the Provider Customer required.  ### Postcondition: New Active Directory configuration created.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemAuthConfigApi();
let createActiveDirectoryConfigRequest = new DracoonApi.CreateActiveDirectoryConfigRequest(); // CreateActiveDirectoryConfigRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.createAdConfig(createActiveDirectoryConfigRequest, opts, (error, data, response) => {
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
 **createActiveDirectoryConfigRequest** | [**CreateActiveDirectoryConfigRequest**](CreateActiveDirectoryConfigRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**ActiveDirectoryConfig**](ActiveDirectoryConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOAuthClient

> OAuthClient createOAuthClient(createOAuthClientRequest, opts)

Create OAuth client

### Description: Create a new OAuth client.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: New OAuth client created.  ### Further Information:   Client secret **MUST** have:   * at least 12 characters, at most 32 characters   * only lower case characters, upper case characters and digits   * at least 1 lower case character, 1 upper case character and 1 digit    The client secret is optional and will be generated if it is left empty.    Valid grant types are:   * &#x60;authorization_code&#x60;   * &#x60;implicit&#x60;   * &#x60;password&#x60;   * &#x60;client_credentials&#x60;   * &#x60;refresh_token&#x60;    Grant type &#x60;client_credentials&#x60; is currently **NOT** permitted!  Allowed characters for client ID are: &#x60;[a-zA-Z0-9_-]&#x60;  If grant types &#x60;authorization_code&#x60; or &#x60;implicit&#x60; are used, a redirect URI **MUST** be provided!  Default access token validity: **8 hours**   Default refresh token validity: **30 days** Default approval validity: **½ year**

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemAuthConfigApi();
let createOAuthClientRequest = new DracoonApi.CreateOAuthClientRequest(); // CreateOAuthClientRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.createOAuthClient(createOAuthClientRequest, opts, (error, data, response) => {
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
 **createOAuthClientRequest** | [**CreateOAuthClientRequest**](CreateOAuthClientRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**OAuthClient**](OAuthClient.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOpenIdIdpConfig

> OpenIdIdpConfig createOpenIdIdpConfig(createOpenIdIdpConfigRequest, opts)

Create OpenID Connect IDP configuration

### Description: Create new OpenID Connect IDP configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: New OpenID Connect IDP configuration is created.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemAuthConfigApi();
let createOpenIdIdpConfigRequest = new DracoonApi.CreateOpenIdIdpConfigRequest(); // CreateOpenIdIdpConfigRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.createOpenIdIdpConfig(createOpenIdIdpConfigRequest, opts, (error, data, response) => {
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
 **createOpenIdIdpConfigRequest** | [**CreateOpenIdIdpConfigRequest**](CreateOpenIdIdpConfigRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**OpenIdIdpConfig**](OpenIdIdpConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRadiusConfig

> RadiusConfig createRadiusConfig(radiusConfigCreateRequest, opts)

Create RADIUS configuration

### Description:   Create new RADIUS configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: New RADIUS configuration is created.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemAuthConfigApi();
let radiusConfigCreateRequest = new DracoonApi.RadiusConfigCreateRequest(); // RadiusConfigCreateRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.createRadiusConfig(radiusConfigCreateRequest, opts, (error, data, response) => {
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
 **radiusConfigCreateRequest** | [**RadiusConfigCreateRequest**](RadiusConfigCreateRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**RadiusConfig**](RadiusConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeAdConfig

> removeAdConfig(adId, opts)

Remove Active Directory configuration

### Description: Delete an existing Active Directory configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Active Directory configuration is removed.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemAuthConfigApi();
let adId = 56; // Number | Active Directory ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.removeAdConfig(adId, opts, (error, data, response) => {
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
 **adId** | **Number**| Active Directory ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeOAuthClient

> removeOAuthClient(clientId, opts)

Remove OAuth client

### Description: Delete an existing OAuth client.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: OAuth client is removed.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemAuthConfigApi();
let clientId = "clientId_example"; // String | OAuth client ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.removeOAuthClient(clientId, opts, (error, data, response) => {
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
 **clientId** | **String**| OAuth client ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeOpenIdIdpConfig

> removeOpenIdIdpConfig(idpId, opts)

Remove OpenID Connect IDP configuration

### Description: Delete an existing OpenID Connect IDP configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: OpenID Connect IDP configuration is removed.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemAuthConfigApi();
let idpId = 56; // Number | OpenID Connect IDP configuration ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.removeOpenIdIdpConfig(idpId, opts, (error, data, response) => {
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
 **idpId** | **Number**| OpenID Connect IDP configuration ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeRadiusConfig

> removeRadiusConfig(opts)

Remove RADIUS configuration

### Description:   Delete existing RADIUS configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: RADIUS configuration is deleted.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemAuthConfigApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.removeRadiusConfig(opts, (error, data, response) => {
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
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestAdConfig

> ActiveDirectoryConfig requestAdConfig(adId, opts)

Request Active Directory configuration

### Description:   Retrieve the configuration of an Active Directory.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Active Directory configuration is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemAuthConfigApi();
let adId = 56; // Number | Active Directory ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestAdConfig(adId, opts, (error, data, response) => {
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
 **adId** | **Number**| Active Directory ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**ActiveDirectoryConfig**](ActiveDirectoryConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestAdConfigs

> ActiveDirectoryConfigList requestAdConfigs(opts)

Request list of Active Directory configurations

### Description:   Retrieve a list of configured Active Directories.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; of the Provider Customer required.  ### Postcondition: List of Active Directory configurations is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemAuthConfigApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestAdConfigs(opts, (error, data, response) => {
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
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**ActiveDirectoryConfigList**](ActiveDirectoryConfigList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestOAuthClient

> OAuthClient requestOAuthClient(clientId, opts)

Request OAuth client

### Description:   Retrieve the configuration of an OAuth client.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: OAuth client is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemAuthConfigApi();
let clientId = "clientId_example"; // String | OAuth client ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestOAuthClient(clientId, opts, (error, data, response) => {
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
 **clientId** | **String**| OAuth client ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**OAuthClient**](OAuthClient.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestOAuthClients

> [OAuthClient] requestOAuthClients(opts)

Request list of OAuth clients

### Description:   Retrieve a list of configured OAuth clients.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: List of OAuth clients is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;isStandard:eq:true&#x60;   Get standard OAuth clients.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;isStandard&#x60; | Standard client filter | &#x60;eq&#x60; |  | &#x60;true or false&#x60; | | &#x60;isExternal&#x60; | External client filter | &#x60;eq&#x60; |  | &#x60;true or false&#x60; | | &#x60;isEnabled&#x60; | Enabled/disabled clients filter | &#x60;eq&#x60; |  | &#x60;true or false&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;clientName:desc|isStandard:asc&#x60;   Sort by &#x60;clientName&#x60; descending **AND** &#x60;isStandard&#x60; ascending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;clientName&#x60; | Client name | | &#x60;isStandard&#x60; | Is a standard client | | &#x60;isExternal&#x60; | Is a external client | | &#x60;isEnabled&#x60; | Is a enabled client |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemAuthConfigApi();
let opts = {
  'filter': "filter_example", // String | Filter string
  'sort': "sort_example", // String | Sort string
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestOAuthClients(opts, (error, data, response) => {
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
 **filter** | **String**| Filter string | [optional] 
 **sort** | **String**| Sort string | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**[OAuthClient]**](OAuthClient.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestOpenIdIdpConfig

> OpenIdIdpConfig requestOpenIdIdpConfig(idpId, opts)

Request OpenID Connect IDP configuration

### Description:   Retrieve an OpenID Connect IDP configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: OpenID Connect IDP configuration is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemAuthConfigApi();
let idpId = 56; // Number | OpenID Connect IDP configuration ID
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestOpenIdIdpConfig(idpId, opts, (error, data, response) => {
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
 **idpId** | **Number**| OpenID Connect IDP configuration ID | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**OpenIdIdpConfig**](OpenIdIdpConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestOpenIdIdpConfigs

> [OpenIdIdpConfig] requestOpenIdIdpConfigs(opts)

Request list of OpenID Connect IDP configurations

### Description:   Retrieve a list of configured OpenID Connect IDPs.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: List of OpenID Connect IDP configurations is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemAuthConfigApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestOpenIdIdpConfigs(opts, (error, data, response) => {
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
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**[OpenIdIdpConfig]**](OpenIdIdpConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestRadiusConfig

> RadiusConfig requestRadiusConfig(opts)

Request RADIUS configuration

### Description:   Retrieve a RADIUS configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: RADIUS configuration is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemAuthConfigApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestRadiusConfig(opts, (error, data, response) => {
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
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**RadiusConfig**](RadiusConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## testAdConfig

> TestActiveDirectoryConfigResponse testAdConfig(testActiveDirectoryConfigRequest, opts)

Test Active Directory configuration

### Description:   Test Active Directory configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Active Directory configuration is returned if successful.  ### Further Information: DRACOON tries to establish a connection with the provided information.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemAuthConfigApi();
let testActiveDirectoryConfigRequest = new DracoonApi.TestActiveDirectoryConfigRequest(); // TestActiveDirectoryConfigRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.testAdConfig(testActiveDirectoryConfigRequest, opts, (error, data, response) => {
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
 **testActiveDirectoryConfigRequest** | [**TestActiveDirectoryConfigRequest**](TestActiveDirectoryConfigRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**TestActiveDirectoryConfigResponse**](TestActiveDirectoryConfigResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## testRadiusConfig

> testRadiusConfig(opts)

Test RADIUS server availability

### Description:   Test RADIUS configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; of the Provider Customer required.  ### Postcondition: RADIUS configuration is returned if successful.  ### Further Information: DRACOON tries to establish a connection with the provided information.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemAuthConfigApi();
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.testRadiusConfig(opts, (error, data, response) => {
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
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAdConfig

> ActiveDirectoryConfig updateAdConfig(adId, updateActiveDirectoryConfigRequest, opts)

Update Active Directory configuration

### Description:   Update an existing Active Directory configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Active Directory configuration updated.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemAuthConfigApi();
let adId = 56; // Number | Active Directory ID
let updateActiveDirectoryConfigRequest = new DracoonApi.UpdateActiveDirectoryConfigRequest(); // UpdateActiveDirectoryConfigRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateAdConfig(adId, updateActiveDirectoryConfigRequest, opts, (error, data, response) => {
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
 **adId** | **Number**| Active Directory ID | 
 **updateActiveDirectoryConfigRequest** | [**UpdateActiveDirectoryConfigRequest**](UpdateActiveDirectoryConfigRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**ActiveDirectoryConfig**](ActiveDirectoryConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOAuthClient

> OAuthClient updateOAuthClient(clientId, updateOAuthClientRequest, opts)

Update OAuth client

### Description:   Update an existing OAuth client.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: OAuth client updated.  ### Further Information:   Client secret **MUST** have:   * at least 12 characters, at most 32 characters   * only lower case characters, upper case characters and digits   * at least 1 lower case character, 1 upper case character and 1 digit    The client secret is optional and will be generated if it is left empty.    Valid grant types are:   * &#x60;authorization_code&#x60;   * &#x60;implicit&#x60;   * &#x60;password&#x60;   * &#x60;client_credentials&#x60;   * &#x60;refresh_token&#x60;    Grant type &#x60;client_credentials&#x60; is currently **NOT** permitted!  If grant types &#x60;authorization_code&#x60; or &#x60;implicit&#x60; are used, a redirect URI **MUST** be provided! 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemAuthConfigApi();
let clientId = "clientId_example"; // String | OAuth client ID
let updateOAuthClientRequest = new DracoonApi.UpdateOAuthClientRequest(); // UpdateOAuthClientRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateOAuthClient(clientId, updateOAuthClientRequest, opts, (error, data, response) => {
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
 **clientId** | **String**| OAuth client ID | 
 **updateOAuthClientRequest** | [**UpdateOAuthClientRequest**](UpdateOAuthClientRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**OAuthClient**](OAuthClient.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOpenIdIdpConfig

> OpenIdIdpConfig updateOpenIdIdpConfig(idpId, updateOpenIdIdpConfigRequest, opts)

Update OpenID Connect IDP configuration

### Description:   Update an existing OpenID Connect IDP configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: OpenID Connect IDP configuration is updated.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemAuthConfigApi();
let idpId = 56; // Number | OpenID Connect IDP configuration ID
let updateOpenIdIdpConfigRequest = new DracoonApi.UpdateOpenIdIdpConfigRequest(); // UpdateOpenIdIdpConfigRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateOpenIdIdpConfig(idpId, updateOpenIdIdpConfigRequest, opts, (error, data, response) => {
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
 **idpId** | **Number**| OpenID Connect IDP configuration ID | 
 **updateOpenIdIdpConfigRequest** | [**UpdateOpenIdIdpConfigRequest**](UpdateOpenIdIdpConfigRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**OpenIdIdpConfig**](OpenIdIdpConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRadiusConfig

> RadiusConfig updateRadiusConfig(radiusConfigUpdateRequest, opts)

Update RADIUS configuration

### Description:   Update existing RADIUS configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: RADIUS configuration is updated.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.SystemAuthConfigApi();
let radiusConfigUpdateRequest = new DracoonApi.RadiusConfigUpdateRequest(); // RadiusConfigUpdateRequest | 
let opts = {
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.updateRadiusConfig(radiusConfigUpdateRequest, opts, (error, data, response) => {
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
 **radiusConfigUpdateRequest** | [**RadiusConfigUpdateRequest**](RadiusConfigUpdateRequest.md)|  | 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**RadiusConfig**](RadiusConfig.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

