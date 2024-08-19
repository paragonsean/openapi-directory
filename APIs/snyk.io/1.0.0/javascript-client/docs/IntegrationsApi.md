# SnykApi.IntegrationsApi

All URIs are relative to *https://api.snyk.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addNewIntegration**](IntegrationsApi.md#addNewIntegration) | **POST** /org/{orgId}/integrations | Add new integration
[**cloneAnIntegrationWithSettingsAndCredentials**](IntegrationsApi.md#cloneAnIntegrationWithSettingsAndCredentials) | **POST** /org/{orgId}/integrations/{integrationId}/clone | Clone an integration (with settings and credentials)
[**deleteCredentials**](IntegrationsApi.md#deleteCredentials) | **DELETE** /org/{orgId}/integrations/{integrationId}/authentication | Delete credentials
[**getExistingIntegrationByType**](IntegrationsApi.md#getExistingIntegrationByType) | **GET** /org/{orgId}/integrations/{type} | Get existing integration by type
[**list**](IntegrationsApi.md#list) | **GET** /org/{orgId}/integrations | List
[**provisionNewBrokerToken**](IntegrationsApi.md#provisionNewBrokerToken) | **POST** /org/{orgId}/integrations/{integrationId}/authentication/provision-token | Provision new broker token
[**retrieve**](IntegrationsApi.md#retrieve) | **GET** /org/{orgId}/integrations/{integrationId}/settings | Retrieve
[**switchBetweenBrokerTokens**](IntegrationsApi.md#switchBetweenBrokerTokens) | **POST** /org/{orgId}/integrations/{integrationId}/authentication/switch-token | Switch between broker tokens
[**update**](IntegrationsApi.md#update) | **PUT** /org/{orgId}/integrations/{integrationId}/settings | Update
[**updateExistingIntegration**](IntegrationsApi.md#updateExistingIntegration) | **PUT** /org/{orgId}/integrations/{integrationId} | Update existing integration



## addNewIntegration

> addNewIntegration(orgId, opts)

Add new integration

Add new integration for given organization.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.IntegrationsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have admin access to this organization.
let opts = {
  'addNewIntegrationRequest': new SnykApi.AddNewIntegrationRequest() // AddNewIntegrationRequest | 
};
apiInstance.addNewIntegration(orgId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | 
 **addNewIntegrationRequest** | [**AddNewIntegrationRequest**](AddNewIntegrationRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## cloneAnIntegrationWithSettingsAndCredentials

> cloneAnIntegrationWithSettingsAndCredentials(orgId, integrationId, opts)

Clone an integration (with settings and credentials)

Clone an integration, including all of its settings and credentials from one organization to another organization in the same group. This API supports both brokered and non-brokered integrations.  Use this API for when you want to share a Broker token between several Snyk organizations (integrations).

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.IntegrationsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | Source organization public ID to clone integration settings from. The `API_KEY` must have access to this organization.
let integrationId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | Source integration public ID to clone.
let opts = {
  'cloneAnIntegrationWithSettingsAndCredentialsRequest': new SnykApi.CloneAnIntegrationWithSettingsAndCredentialsRequest() // CloneAnIntegrationWithSettingsAndCredentialsRequest | 
};
apiInstance.cloneAnIntegrationWithSettingsAndCredentials(orgId, integrationId, opts, (error, data, response) => {
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
 **orgId** | **String**| Source organization public ID to clone integration settings from. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **integrationId** | **String**| Source integration public ID to clone. | 
 **cloneAnIntegrationWithSettingsAndCredentialsRequest** | [**CloneAnIntegrationWithSettingsAndCredentialsRequest**](CloneAnIntegrationWithSettingsAndCredentialsRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## deleteCredentials

> deleteCredentials(orgId, integrationId)

Delete credentials

Removes any credentials set for this integration. If this is a brokered connection the operation will have no effect.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.IntegrationsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
let integrationId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The integration ID.
apiInstance.deleteCredentials(orgId, integrationId, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **integrationId** | **String**| The integration ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getExistingIntegrationByType

> GetExistingIntegrationByType200Response getExistingIntegrationByType(orgId, type)

Get existing integration by type



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.IntegrationsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The `API_KEY` must have admin access to this organization.
let type = "github"; // String | Integration type.
apiInstance.getExistingIntegrationByType(orgId, type, (error, data, response) => {
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
 **orgId** | **String**| The &#x60;API_KEY&#x60; must have admin access to this organization. | 
 **type** | **String**| Integration type. | 

### Return type

[**GetExistingIntegrationByType200Response**](GetExistingIntegrationByType200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## list

> Object list(orgId)

List



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.IntegrationsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization public ID. The `API_KEY` must have admin access to this organization.
apiInstance.list(orgId, (error, data, response) => {
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
 **orgId** | **String**| The organization public ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## provisionNewBrokerToken

> provisionNewBrokerToken(orgId, integrationId)

Provision new broker token

Issue a new and unique provisional broker token for the brokered integration.  Used for zero down-time token rotation with the Snyk Broker. Once provisioned, the token can be used to initialize a new broker client before using the switch API to update the token in use by the integration.  The new provisional token will fail to be created if the integration, or any other integration in the same group, already has one provisioned.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.IntegrationsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The `API_KEY` must have access to this organization.
let integrationId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | 
apiInstance.provisionNewBrokerToken(orgId, integrationId, (error, data, response) => {
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
 **orgId** | **String**| The &#x60;API_KEY&#x60; must have access to this organization. | 
 **integrationId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## retrieve

> Retrieve200Response retrieve(orgId, integrationId)

Retrieve



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.IntegrationsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have admin access to this organization.
let integrationId = "9a3e5d90-b782-468a-a042-9a2073736f0b"; // String | The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured.
apiInstance.retrieve(orgId, integrationId, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | 
 **integrationId** | **String**| The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured. | 

### Return type

[**Retrieve200Response**](Retrieve200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## switchBetweenBrokerTokens

> switchBetweenBrokerTokens(orgId, integrationId)

Switch between broker tokens

Switch the existing broker token with the provisioned token for this integration and any other in the same group. Only perform this action when you have a Broker client running with the provisioned token. This action will fail if there is no token provisioned for this integration or any integration in the same group.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.IntegrationsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The `API_KEY` must have access to this organization.
let integrationId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | 
apiInstance.switchBetweenBrokerTokens(orgId, integrationId, (error, data, response) => {
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
 **orgId** | **String**| The &#x60;API_KEY&#x60; must have access to this organization. | 
 **integrationId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## update

> Retrieve200Response update(orgId, integrationId, opts)

Update



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.IntegrationsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have admin access to this organization.
let integrationId = "9a3e5d90-b782-468a-a042-9a2073736f0b"; // String | The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured.
let opts = {
  'updateRequest': new SnykApi.UpdateRequest() // UpdateRequest | 
};
apiInstance.update(orgId, integrationId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | 
 **integrationId** | **String**| The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured. | 
 **updateRequest** | [**UpdateRequest**](UpdateRequest.md)|  | [optional] 

### Return type

[**Retrieve200Response**](Retrieve200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## updateExistingIntegration

> updateExistingIntegration(orgId, integrationId, opts)

Update existing integration

+ Update integration&#39;s credentials for given organization. Integration must be **not brokered**  + Enable or disable brokered integration for given organization. *Credentials required for disabling brokered integration*  Examples in right section:  1. Set up a broker for an existing integration  2. Update credentials for an existing non-brokered integration  3. Disable broker for an existing integration

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.IntegrationsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have admin access to this organization.
let integrationId = "9a3e5d90-b782-468a-a042-9a2073736f0b"; // String | The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured.
let opts = {
  'updateExistingIntegrationRequest': new SnykApi.UpdateExistingIntegrationRequest() // UpdateExistingIntegrationRequest | 
};
apiInstance.updateExistingIntegration(orgId, integrationId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | 
 **integrationId** | **String**| The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured. | 
 **updateExistingIntegrationRequest** | [**UpdateExistingIntegrationRequest**](UpdateExistingIntegrationRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8

