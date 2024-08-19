# IllumiDesk.TeamsApi

All URIs are relative to *https://api.illumidesk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teamsBillingInvoiceItemsList**](TeamsApi.md#teamsBillingInvoiceItemsList) | **GET** /v1/teams/{team}/billing/invoices/{invoice_id}/invoice-items/ | Get team invoice items for a given invoice.
[**teamsBillingInvoiceItemsRead**](TeamsApi.md#teamsBillingInvoiceItemsRead) | **GET** /v1/teams/{team}/billing/invoices/{invoice_id}/invoice-items/{id} | Get a specific team InvoiceItem.
[**teamsBillingInvoicesList**](TeamsApi.md#teamsBillingInvoicesList) | **GET** /v1/teams/{team}/billing/invoices/ | Get team invoices
[**teamsBillingInvoicesRead**](TeamsApi.md#teamsBillingInvoicesRead) | **GET** /v1/teams/{team}/billing/invoices/{id}/ | Get an invoice
[**teamsBillingSubscriptionsCreate**](TeamsApi.md#teamsBillingSubscriptionsCreate) | **POST** /v1/teams/{team}/billing/subscriptions/ | Create a new team subscription
[**teamsBillingSubscriptionsDelete**](TeamsApi.md#teamsBillingSubscriptionsDelete) | **DELETE** /v1/teams/{team}/billing/subscriptions/{id}/ | Delete a subscription
[**teamsBillingSubscriptionsList**](TeamsApi.md#teamsBillingSubscriptionsList) | **GET** /v1/teams/{team}/billing/subscriptions/ | Get active team subscriptons
[**teamsBillingSubscriptionsRead**](TeamsApi.md#teamsBillingSubscriptionsRead) | **GET** /v1/teams/{team}/billing/subscriptions/{id}/ | Get team subscriptions
[**teamsCreate**](TeamsApi.md#teamsCreate) | **POST** /v1/teams/ | Create a new team
[**teamsDelete**](TeamsApi.md#teamsDelete) | **DELETE** /v1/teams/{team}/ | Delete a team
[**teamsGroupsAddToGroup**](TeamsApi.md#teamsGroupsAddToGroup) | **POST** /v1/teams/{team}/groups/{group}/add/ | Add user to group
[**teamsGroupsDelete**](TeamsApi.md#teamsGroupsDelete) | **DELETE** /v1/teams/{team}/groups/{group}/ | Delete team group
[**teamsGroupsList**](TeamsApi.md#teamsGroupsList) | **GET** /v1/teams/{team}/groups/ | Get team groups
[**teamsGroupsRead**](TeamsApi.md#teamsGroupsRead) | **GET** /v1/teams/{team}/groups/{group}/ | Get team group
[**teamsGroupsRemoveFromGroup**](TeamsApi.md#teamsGroupsRemoveFromGroup) | **POST** /v1/teams/{team}/groups/{group}/remove/ | User removed from group
[**teamsGroupsReplace**](TeamsApi.md#teamsGroupsReplace) | **PUT** /v1/teams/{team}/groups/{group}/ | Patch team group
[**teamsGroupsUpdate**](TeamsApi.md#teamsGroupsUpdate) | **PATCH** /v1/teams/{team}/groups/{group}/ | Patch team group
[**teamsList**](TeamsApi.md#teamsList) | **GET** /v1/teams/ | Get teams
[**teamsRead**](TeamsApi.md#teamsRead) | **GET** /v1/teams/{team}/ | Get a team
[**teamsReplace**](TeamsApi.md#teamsReplace) | **PUT** /v1/teams/{team}/ | Replace a team
[**teamsUpdate**](TeamsApi.md#teamsUpdate) | **PATCH** /v1/teams/{team}/ | Update a team



## teamsBillingInvoiceItemsList

> [InvoiceItem] teamsBillingInvoiceItemsList(team, invoiceId, opts)

Get team invoice items for a given invoice.

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.TeamsApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let invoiceId = "invoiceId_example"; // String | Invoice id, expressed as UUID.
let opts = {
  'limit': "limit_example", // String | Limit when getting items.
  'offset': "offset_example", // String | Offset when getting items.
  'ordering': "ordering_example" // String | Ordering when getting items.
};
apiInstance.teamsBillingInvoiceItemsList(team, invoiceId, opts, (error, data, response) => {
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
 **team** | **String**| Team unique identifier expressed as UUID or name. | 
 **invoiceId** | **String**| Invoice id, expressed as UUID. | 
 **limit** | **String**| Limit when getting items. | [optional] 
 **offset** | **String**| Offset when getting items. | [optional] 
 **ordering** | **String**| Ordering when getting items. | [optional] 

### Return type

[**[InvoiceItem]**](InvoiceItem.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## teamsBillingInvoiceItemsRead

> InvoiceItem teamsBillingInvoiceItemsRead(team, invoiceId, id)

Get a specific team InvoiceItem.

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.TeamsApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let invoiceId = "invoiceId_example"; // String | Invoice id, expressed as UUID.
let id = "id_example"; // String | InvoiceItem id, expressed as UUID.
apiInstance.teamsBillingInvoiceItemsRead(team, invoiceId, id, (error, data, response) => {
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
 **team** | **String**| Team unique identifier expressed as UUID or name. | 
 **invoiceId** | **String**| Invoice id, expressed as UUID. | 
 **id** | **String**| InvoiceItem id, expressed as UUID. | 

### Return type

[**InvoiceItem**](InvoiceItem.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## teamsBillingInvoicesList

> [Invoice] teamsBillingInvoicesList(team, opts)

Get team invoices

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.TeamsApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let opts = {
  'limit': "limit_example", // String | Limit when getting items.
  'offset': "offset_example" // String | Offset when getting items.
};
apiInstance.teamsBillingInvoicesList(team, opts, (error, data, response) => {
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
 **team** | **String**| Team unique identifier expressed as UUID or name. | 
 **limit** | **String**| Limit when getting items. | [optional] 
 **offset** | **String**| Offset when getting items. | [optional] 

### Return type

[**[Invoice]**](Invoice.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## teamsBillingInvoicesRead

> Invoice teamsBillingInvoicesRead(team, id)

Get an invoice

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.TeamsApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let id = "id_example"; // String | Invoice unique identifier expressed as UUID.
apiInstance.teamsBillingInvoicesRead(team, id, (error, data, response) => {
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
 **team** | **String**| Team unique identifier expressed as UUID or name. | 
 **id** | **String**| Invoice unique identifier expressed as UUID. | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## teamsBillingSubscriptionsCreate

> Subscription teamsBillingSubscriptionsCreate(team, opts)

Create a new team subscription

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.TeamsApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let opts = {
  'subscriptionData': new IllumiDesk.SubscriptionData() // SubscriptionData | 
};
apiInstance.teamsBillingSubscriptionsCreate(team, opts, (error, data, response) => {
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
 **team** | **String**| Team unique identifier expressed as UUID or name. | 
 **subscriptionData** | [**SubscriptionData**](SubscriptionData.md)|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## teamsBillingSubscriptionsDelete

> teamsBillingSubscriptionsDelete(team, id)

Delete a subscription

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.TeamsApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let id = "id_example"; // String | Subscription unique identifier expressed as UUID.
apiInstance.teamsBillingSubscriptionsDelete(team, id, (error, data, response) => {
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
 **team** | **String**| Team unique identifier expressed as UUID or name. | 
 **id** | **String**| Subscription unique identifier expressed as UUID. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## teamsBillingSubscriptionsList

> [Subscription] teamsBillingSubscriptionsList(team, opts)

Get active team subscriptons

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.TeamsApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let opts = {
  'limit': "limit_example", // String | Limit when getting items.
  'offset': "offset_example", // String | Offset when getting items.
  'ordering': "ordering_example" // String | Ordering when getting items.
};
apiInstance.teamsBillingSubscriptionsList(team, opts, (error, data, response) => {
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
 **team** | **String**| Team unique identifier expressed as UUID or name. | 
 **limit** | **String**| Limit when getting items. | [optional] 
 **offset** | **String**| Offset when getting items. | [optional] 
 **ordering** | **String**| Ordering when getting items. | [optional] 

### Return type

[**[Subscription]**](Subscription.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## teamsBillingSubscriptionsRead

> Subscription teamsBillingSubscriptionsRead(team, id)

Get team subscriptions

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.TeamsApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let id = "id_example"; // String | Unique identifier expressed as UUID.
apiInstance.teamsBillingSubscriptionsRead(team, id, (error, data, response) => {
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
 **team** | **String**| Team unique identifier expressed as UUID or name. | 
 **id** | **String**| Unique identifier expressed as UUID. | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## teamsCreate

> Team teamsCreate(opts)

Create a new team

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.TeamsApi();
let opts = {
  'teamData': new IllumiDesk.TeamData() // TeamData | 
};
apiInstance.teamsCreate(opts, (error, data, response) => {
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
 **teamData** | [**TeamData**](TeamData.md)|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## teamsDelete

> teamsDelete(team)

Delete a team

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.TeamsApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
apiInstance.teamsDelete(team, (error, data, response) => {
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
 **team** | **String**| Team unique identifier expressed as UUID or name. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## teamsGroupsAddToGroup

> GroupUser teamsGroupsAddToGroup(team, group)

Add user to group

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.TeamsApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let group = "group_example"; // String | Group unique identifier expressed as UUID or name.
apiInstance.teamsGroupsAddToGroup(team, group, (error, data, response) => {
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
 **team** | **String**| Team unique identifier expressed as UUID or name. | 
 **group** | **String**| Group unique identifier expressed as UUID or name. | 

### Return type

[**GroupUser**](GroupUser.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## teamsGroupsDelete

> teamsGroupsDelete(team, group)

Delete team group

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.TeamsApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let group = "group_example"; // String | Group unique identifier expressed as UUID or name.
apiInstance.teamsGroupsDelete(team, group, (error, data, response) => {
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
 **team** | **String**| Team unique identifier expressed as UUID or name. | 
 **group** | **String**| Group unique identifier expressed as UUID or name. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## teamsGroupsList

> [Group] teamsGroupsList(team, opts)

Get team groups

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.TeamsApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let opts = {
  'limit': "limit_example", // String | Limit when getting data.
  'offset': "offset_example" // String | Offset when getting data.
};
apiInstance.teamsGroupsList(team, opts, (error, data, response) => {
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
 **team** | **String**| Team unique identifier expressed as UUID or name. | 
 **limit** | **String**| Limit when getting data. | [optional] 
 **offset** | **String**| Offset when getting data. | [optional] 

### Return type

[**[Group]**](Group.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## teamsGroupsRead

> Group teamsGroupsRead(team, group)

Get team group

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.TeamsApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let group = "group_example"; // String | Group unique identifier expressed as UUID or name.
apiInstance.teamsGroupsRead(team, group, (error, data, response) => {
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
 **team** | **String**| Team unique identifier expressed as UUID or name. | 
 **group** | **String**| Group unique identifier expressed as UUID or name. | 

### Return type

[**Group**](Group.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## teamsGroupsRemoveFromGroup

> teamsGroupsRemoveFromGroup(team, group)

User removed from group

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.TeamsApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let group = "group_example"; // String | Group unique identifier expressed as UUID or name.
apiInstance.teamsGroupsRemoveFromGroup(team, group, (error, data, response) => {
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
 **team** | **String**| Team unique identifier expressed as UUID or name. | 
 **group** | **String**| Group unique identifier expressed as UUID or name. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## teamsGroupsReplace

> Group teamsGroupsReplace(team, group, opts)

Patch team group

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.TeamsApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let group = "group_example"; // String | Group unique identifier expressed as UUID or name.
let opts = {
  'groupData': new IllumiDesk.GroupData() // GroupData | 
};
apiInstance.teamsGroupsReplace(team, group, opts, (error, data, response) => {
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
 **team** | **String**| Team unique identifier expressed as UUID or name. | 
 **group** | **String**| Group unique identifier expressed as UUID or name. | 
 **groupData** | [**GroupData**](GroupData.md)|  | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## teamsGroupsUpdate

> Group teamsGroupsUpdate(team, group, opts)

Patch team group

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.TeamsApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let group = "group_example"; // String | Group unique identifier expressed as UUID or name.
let opts = {
  'groupData': new IllumiDesk.GroupData() // GroupData | 
};
apiInstance.teamsGroupsUpdate(team, group, opts, (error, data, response) => {
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
 **team** | **String**| Team unique identifier expressed as UUID or name. | 
 **group** | **String**| Group unique identifier expressed as UUID or name. | 
 **groupData** | [**GroupData**](GroupData.md)|  | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## teamsList

> [Team] teamsList(opts)

Get teams

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.TeamsApi();
let opts = {
  'limit': "limit_example", // String | Limit when getting data.
  'offset': "offset_example" // String | Offset when getting data.
};
apiInstance.teamsList(opts, (error, data, response) => {
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
 **limit** | **String**| Limit when getting data. | [optional] 
 **offset** | **String**| Offset when getting data. | [optional] 

### Return type

[**[Team]**](Team.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## teamsRead

> Team teamsRead(team)

Get a team

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.TeamsApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
apiInstance.teamsRead(team, (error, data, response) => {
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
 **team** | **String**| Team unique identifier expressed as UUID or name. | 

### Return type

[**Team**](Team.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## teamsReplace

> Team teamsReplace(team, opts)

Replace a team

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.TeamsApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let opts = {
  'teamData': new IllumiDesk.TeamData() // TeamData | 
};
apiInstance.teamsReplace(team, opts, (error, data, response) => {
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
 **team** | **String**| Team unique identifier expressed as UUID or name. | 
 **teamData** | [**TeamData**](TeamData.md)|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## teamsUpdate

> Team teamsUpdate(team, opts)

Update a team

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.TeamsApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let opts = {
  'teamData': new IllumiDesk.TeamData() // TeamData | 
};
apiInstance.teamsUpdate(team, opts, (error, data, response) => {
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
 **team** | **String**| Team unique identifier expressed as UUID or name. | 
 **teamData** | [**TeamData**](TeamData.md)|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html

