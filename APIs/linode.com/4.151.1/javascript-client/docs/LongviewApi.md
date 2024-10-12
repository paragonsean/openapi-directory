# LinodeApi.LongviewApi

All URIs are relative to *https://api.linode.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createLongviewClient**](LongviewApi.md#createLongviewClient) | **POST** /longview/clients | Longview Client Create
[**deleteLongviewClient**](LongviewApi.md#deleteLongviewClient) | **DELETE** /longview/clients/{clientId} | Longview Client Delete
[**getLongviewClient**](LongviewApi.md#getLongviewClient) | **GET** /longview/clients/{clientId} | Longview Client View
[**getLongviewClients**](LongviewApi.md#getLongviewClients) | **GET** /longview/clients | Longview Clients List
[**getLongviewPlan**](LongviewApi.md#getLongviewPlan) | **GET** /longview/plan | Longview Plan View
[**getLongviewSubscription**](LongviewApi.md#getLongviewSubscription) | **GET** /longview/subscriptions/{subscriptionId} | Longview Subscription View
[**getLongviewSubscriptions**](LongviewApi.md#getLongviewSubscriptions) | **GET** /longview/subscriptions | Longview Subscriptions List
[**updateLongviewClient**](LongviewApi.md#updateLongviewClient) | **PUT** /longview/clients/{clientId} | Longview Client Update
[**updateLongviewPlan**](LongviewApi.md#updateLongviewPlan) | **PUT** /longview/plan | Longview Plan Update



## createLongviewClient

> LongviewClient createLongviewClient(longviewClient)

Longview Client Create

Creates a Longview Client.  This Client will not begin monitoring the status of your server until you configure the Longview Client application on your Linode using the returning &#x60;install_code&#x60; and &#x60;api_key&#x60;. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LongviewApi();
let longviewClient = new LinodeApi.LongviewClient(); // LongviewClient | Information about the LongviewClient to create.
apiInstance.createLongviewClient(longviewClient, (error, data, response) => {
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
 **longviewClient** | [**LongviewClient**](LongviewClient.md)| Information about the LongviewClient to create. | 

### Return type

[**LongviewClient**](LongviewClient.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteLongviewClient

> Object deleteLongviewClient(clientId)

Longview Client Delete

Deletes a Longview Client from your Account.  **All information stored for this client will be lost.**  This _does not_ uninstall the Longview Client application for your Linode - you must do that manually. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LongviewApi();
let clientId = 56; // Number | The Longview Client ID to access.
apiInstance.deleteLongviewClient(clientId, (error, data, response) => {
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
 **clientId** | **Number**| The Longview Client ID to access. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLongviewClient

> LongviewClient getLongviewClient(clientId)

Longview Client View

Returns a single Longview Client you can access. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LongviewApi();
let clientId = 56; // Number | The Longview Client ID to access.
apiInstance.getLongviewClient(clientId, (error, data, response) => {
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
 **clientId** | **Number**| The Longview Client ID to access. | 

### Return type

[**LongviewClient**](LongviewClient.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLongviewClients

> GetLongviewClients200Response getLongviewClients(opts)

Longview Clients List

Returns a paginated list of Longview Clients you have access to. Longview Client is used to monitor stats on your Linode with the help of the Longview Client application. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LongviewApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getLongviewClients(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetLongviewClients200Response**](GetLongviewClients200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLongviewPlan

> LongviewSubscription getLongviewPlan()

Longview Plan View

Get the details of your current Longview plan. This returns a &#x60;LongviewSubscription&#x60; object for your current Longview Pro plan, or an empty set &#x60;{}&#x60; if your current plan is Longview Free.  You must have at least one of the following &#x60;global&#x60; [User Grants](/docs/api/account/#users-grants-view) in order to access this endpoint:    - &#x60;\&quot;account_access\&quot;: read_write&#x60;   - &#x60;\&quot;account_access\&quot;: read_only&#x60;   - &#x60;\&quot;longview_subscription\&quot;: true&#x60;   - &#x60;\&quot;add_longview\&quot;: true&#x60;   To update your subscription plan, send a request to [Update Longview Plan](/docs/api/longview/#longview-plan-update). 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LongviewApi();
apiInstance.getLongviewPlan((error, data, response) => {
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

[**LongviewSubscription**](LongviewSubscription.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLongviewSubscription

> LongviewSubscription getLongviewSubscription(subscriptionId)

Longview Subscription View

Get the Longview plan details as a single &#x60;LongviewSubscription&#x60; object for the provided subscription ID. This is a public endpoint and requires no authentication. 

### Example

```javascript
import LinodeApi from 'linode_api';

let apiInstance = new LinodeApi.LongviewApi();
let subscriptionId = "subscriptionId_example"; // String | The Longview Subscription to look up.
apiInstance.getLongviewSubscription(subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| The Longview Subscription to look up. | 

### Return type

[**LongviewSubscription**](LongviewSubscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLongviewSubscriptions

> GetLongviewSubscriptions200Response getLongviewSubscriptions(opts)

Longview Subscriptions List

Returns a paginated list of available Longview Subscriptions. This is a public endpoint and requires no authentication. 

### Example

```javascript
import LinodeApi from 'linode_api';

let apiInstance = new LinodeApi.LongviewApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getLongviewSubscriptions(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetLongviewSubscriptions200Response**](GetLongviewSubscriptions200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateLongviewClient

> LongviewClient updateLongviewClient(clientId, longviewClient)

Longview Client Update

Updates a Longview Client.  This cannot update how it monitors your server; use the Longview Client application on your Linode for monitoring configuration. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LongviewApi();
let clientId = 56; // Number | The Longview Client ID to access.
let longviewClient = new LinodeApi.LongviewClient(); // LongviewClient | The fields to update.
apiInstance.updateLongviewClient(clientId, longviewClient, (error, data, response) => {
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
 **clientId** | **Number**| The Longview Client ID to access. | 
 **longviewClient** | [**LongviewClient**](LongviewClient.md)| The fields to update. | 

### Return type

[**LongviewClient**](LongviewClient.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateLongviewPlan

> LongviewSubscription updateLongviewPlan(longviewPlan)

Longview Plan Update

Update your Longview plan to that of the given subcription ID. This returns a &#x60;LongviewSubscription&#x60; object for the updated Longview Pro plan, or an empty set &#x60;{}&#x60; if the updated plan is Longview Free.  You must have &#x60;\&quot;longview_subscription\&quot;: true&#x60; configured as a &#x60;global&#x60; [User Grant](/docs/api/account/#users-grants-view) in order to access this endpoint.  You can send a request to the [List Longview Subscriptions](/docs/api/longview/#longview-subscriptions-list) endpoint to receive the details, including &#x60;id&#x60;&#39;s, of each plan. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LongviewApi();
let longviewPlan = new LinodeApi.LongviewPlan(); // LongviewPlan | Update your Longview subscription plan.
apiInstance.updateLongviewPlan(longviewPlan, (error, data, response) => {
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
 **longviewPlan** | [**LongviewPlan**](LongviewPlan.md)| Update your Longview subscription plan. | 

### Return type

[**LongviewSubscription**](LongviewSubscription.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

