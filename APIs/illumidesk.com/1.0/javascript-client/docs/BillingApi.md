# IllumiDesk.BillingApi

All URIs are relative to *https://api.illumidesk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billingCardsCreate**](BillingApi.md#billingCardsCreate) | **POST** /v1/{namespace}/billing/cards/ | Create new credit card
[**billingCardsDelete**](BillingApi.md#billingCardsDelete) | **DELETE** /v1/{namespace}/billing/cards/{id}/ | Delete a credit card
[**billingCardsList**](BillingApi.md#billingCardsList) | **GET** /v1/{namespace}/billing/cards/ | Get credit cards
[**billingCardsRead**](BillingApi.md#billingCardsRead) | **GET** /v1/{namespace}/billing/cards/{id}/ | Get credit card by id
[**billingCardsReplace**](BillingApi.md#billingCardsReplace) | **PUT** /v1/{namespace}/billing/cards/{id}/ | Replace a credit card
[**billingCardsUpdate**](BillingApi.md#billingCardsUpdate) | **PATCH** /v1/{namespace}/billing/cards/{id}/ | Update a credit card
[**billingInvoiceItemsList**](BillingApi.md#billingInvoiceItemsList) | **GET** /v1/{namespace}/billing/invoices/{invoice_id}/invoice-items/ | Get invoice items for a given invoice.
[**billingInvoiceItemsRead**](BillingApi.md#billingInvoiceItemsRead) | **GET** /v1/{namespace}/billing/invoices/{invoice_id}/invoice-items/{id} | Get a specific InvoiceItem.
[**billingInvoicesList**](BillingApi.md#billingInvoicesList) | **GET** /v1/{namespace}/billing/invoices/ | Get invoices
[**billingInvoicesRead**](BillingApi.md#billingInvoicesRead) | **GET** /v1/{namespace}/billing/invoices/{id}/ | Get an invoice
[**billingPlansList**](BillingApi.md#billingPlansList) | **GET** /v1/{namespace}/billing/plans/ | Get billing plans
[**billingPlansRead**](BillingApi.md#billingPlansRead) | **GET** /v1/{namespace}/billing/plans/{id}/ | Get a billing plan
[**billingSubscriptionsCreate**](BillingApi.md#billingSubscriptionsCreate) | **POST** /v1/{namespace}/billing/subscriptions/ | Create a new subscription
[**billingSubscriptionsDelete**](BillingApi.md#billingSubscriptionsDelete) | **DELETE** /v1/{namespace}/billing/subscriptions/{id}/ | Delete a subscription
[**billingSubscriptionsList**](BillingApi.md#billingSubscriptionsList) | **GET** /v1/{namespace}/billing/subscriptions/ | Get active subscriptons
[**billingSubscriptionsRead**](BillingApi.md#billingSubscriptionsRead) | **GET** /v1/{namespace}/billing/subscriptions/{id}/ | Get a subscriptions
[**teamsBillingInvoiceItemsList_0**](BillingApi.md#teamsBillingInvoiceItemsList_0) | **GET** /v1/teams/{team}/billing/invoices/{invoice_id}/invoice-items/ | Get team invoice items for a given invoice.
[**teamsBillingInvoiceItemsRead_0**](BillingApi.md#teamsBillingInvoiceItemsRead_0) | **GET** /v1/teams/{team}/billing/invoices/{invoice_id}/invoice-items/{id} | Get a specific team InvoiceItem.
[**teamsBillingInvoicesList_0**](BillingApi.md#teamsBillingInvoicesList_0) | **GET** /v1/teams/{team}/billing/invoices/ | Get team invoices
[**teamsBillingInvoicesRead_0**](BillingApi.md#teamsBillingInvoicesRead_0) | **GET** /v1/teams/{team}/billing/invoices/{id}/ | Get an invoice
[**teamsBillingSubscriptionsCreate_0**](BillingApi.md#teamsBillingSubscriptionsCreate_0) | **POST** /v1/teams/{team}/billing/subscriptions/ | Create a new team subscription
[**teamsBillingSubscriptionsDelete_0**](BillingApi.md#teamsBillingSubscriptionsDelete_0) | **DELETE** /v1/teams/{team}/billing/subscriptions/{id}/ | Delete a subscription
[**teamsBillingSubscriptionsList_0**](BillingApi.md#teamsBillingSubscriptionsList_0) | **GET** /v1/teams/{team}/billing/subscriptions/ | Get active team subscriptons
[**teamsBillingSubscriptionsRead_0**](BillingApi.md#teamsBillingSubscriptionsRead_0) | **GET** /v1/teams/{team}/billing/subscriptions/{id}/ | Get team subscriptions



## billingCardsCreate

> Card billingCardsCreate(namespace, opts)

Create new credit card

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.BillingApi();
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'cardData': new IllumiDesk.CardDataPost() // CardDataPost | 
};
apiInstance.billingCardsCreate(namespace, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **cardData** | [**CardDataPost**](CardDataPost.md)|  | [optional] 

### Return type

[**Card**](Card.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## billingCardsDelete

> billingCardsDelete(namespace, id)

Delete a credit card

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.BillingApi();
let namespace = "namespace_example"; // String | User or team name.
let id = "id_example"; // String | Card unique identifier expressed as UUID.
apiInstance.billingCardsDelete(namespace, id, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **id** | **String**| Card unique identifier expressed as UUID. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## billingCardsList

> [Card] billingCardsList(namespace, opts)

Get credit cards

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.BillingApi();
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'limit': "limit_example", // String | Set limit when retrieving credit or debit cards.
  'offset': "offset_example", // String | Set offset when retriving cards.
  'ordering': "ordering_example" // String | Order when retrieving cards.
};
apiInstance.billingCardsList(namespace, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **limit** | **String**| Set limit when retrieving credit or debit cards. | [optional] 
 **offset** | **String**| Set offset when retriving cards. | [optional] 
 **ordering** | **String**| Order when retrieving cards. | [optional] 

### Return type

[**[Card]**](Card.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## billingCardsRead

> Card billingCardsRead(namespace, id)

Get credit card by id

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.BillingApi();
let namespace = "namespace_example"; // String | User or team name.
let id = "id_example"; // String | User unique identifier expressed as UUID.
apiInstance.billingCardsRead(namespace, id, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **id** | **String**| User unique identifier expressed as UUID. | 

### Return type

[**Card**](Card.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## billingCardsReplace

> Card billingCardsReplace(namespace, id, opts)

Replace a credit card

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.BillingApi();
let namespace = "namespace_example"; // String | User or team name.
let id = "id_example"; // String | 
let opts = {
  'cardData': new IllumiDesk.CardDataPutandPatch() // CardDataPutandPatch | 
};
apiInstance.billingCardsReplace(namespace, id, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **id** | **String**|  | 
 **cardData** | [**CardDataPutandPatch**](CardDataPutandPatch.md)|  | [optional] 

### Return type

[**Card**](Card.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## billingCardsUpdate

> Card billingCardsUpdate(namespace, id, opts)

Update a credit card

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.BillingApi();
let namespace = "namespace_example"; // String | User or team name.
let id = "id_example"; // String | Card unique identifier.
let opts = {
  'cardData': new IllumiDesk.CardDataPutandPatch() // CardDataPutandPatch | 
};
apiInstance.billingCardsUpdate(namespace, id, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **id** | **String**| Card unique identifier. | 
 **cardData** | [**CardDataPutandPatch**](CardDataPutandPatch.md)|  | [optional] 

### Return type

[**Card**](Card.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## billingInvoiceItemsList

> [InvoiceItem] billingInvoiceItemsList(namespace, invoiceId, opts)

Get invoice items for a given invoice.

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.BillingApi();
let namespace = "namespace_example"; // String | User or team name.
let invoiceId = "invoiceId_example"; // String | Invoice id, expressed as UUID.
let opts = {
  'limit': "limit_example", // String | Limit when getting items.
  'offset': "offset_example", // String | Offset when getting items.
  'ordering': "ordering_example" // String | Ordering when getting items.
};
apiInstance.billingInvoiceItemsList(namespace, invoiceId, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
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


## billingInvoiceItemsRead

> InvoiceItem billingInvoiceItemsRead(namespace, invoiceId, id)

Get a specific InvoiceItem.

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.BillingApi();
let namespace = "namespace_example"; // String | User or team name.
let invoiceId = "invoiceId_example"; // String | Invoice id, expressed as UUID.
let id = "id_example"; // String | InvoiceItem id, expressed as UUID.
apiInstance.billingInvoiceItemsRead(namespace, invoiceId, id, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **invoiceId** | **String**| Invoice id, expressed as UUID. | 
 **id** | **String**| InvoiceItem id, expressed as UUID. | 

### Return type

[**InvoiceItem**](InvoiceItem.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## billingInvoicesList

> [Invoice] billingInvoicesList(namespace, opts)

Get invoices

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.BillingApi();
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'limit': "limit_example", // String | Limit when getting items.
  'offset': "offset_example", // String | Offset when getting items.
  'ordering': "ordering_example" // String | Ordering when getting items.
};
apiInstance.billingInvoicesList(namespace, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **limit** | **String**| Limit when getting items. | [optional] 
 **offset** | **String**| Offset when getting items. | [optional] 
 **ordering** | **String**| Ordering when getting items. | [optional] 

### Return type

[**[Invoice]**](Invoice.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## billingInvoicesRead

> Invoice billingInvoicesRead(namespace, id)

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

let apiInstance = new IllumiDesk.BillingApi();
let namespace = "namespace_example"; // String | User or team name.
let id = "id_example"; // String | Invoice unique identifier expressed as UUID.
apiInstance.billingInvoicesRead(namespace, id, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **id** | **String**| Invoice unique identifier expressed as UUID. | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## billingPlansList

> [Plan] billingPlansList(namespace, opts)

Get billing plans

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.BillingApi();
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'limit': "limit_example", // String | Limit when getting items.
  'offset': "offset_example", // String | Offset when getting items.
  'ordering': "ordering_example" // String | Ordering when getting items.
};
apiInstance.billingPlansList(namespace, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **limit** | **String**| Limit when getting items. | [optional] 
 **offset** | **String**| Offset when getting items. | [optional] 
 **ordering** | **String**| Ordering when getting items. | [optional] 

### Return type

[**[Plan]**](Plan.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## billingPlansRead

> Plan billingPlansRead(namespace, id)

Get a billing plan

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.BillingApi();
let namespace = "namespace_example"; // String | User or team name.
let id = "id_example"; // String | Plan unique identifier expressed as UUID.
apiInstance.billingPlansRead(namespace, id, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **id** | **String**| Plan unique identifier expressed as UUID. | 

### Return type

[**Plan**](Plan.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## billingSubscriptionsCreate

> Subscription billingSubscriptionsCreate(namespace, opts)

Create a new subscription

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.BillingApi();
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'subscriptionData': new IllumiDesk.SubscriptionData() // SubscriptionData | 
};
apiInstance.billingSubscriptionsCreate(namespace, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **subscriptionData** | [**SubscriptionData**](SubscriptionData.md)|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## billingSubscriptionsDelete

> billingSubscriptionsDelete(namespace, id)

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

let apiInstance = new IllumiDesk.BillingApi();
let namespace = "namespace_example"; // String | User or team name.
let id = "id_example"; // String | Subscription unique identifier expressed as UUID.
apiInstance.billingSubscriptionsDelete(namespace, id, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **id** | **String**| Subscription unique identifier expressed as UUID. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## billingSubscriptionsList

> [Subscription] billingSubscriptionsList(namespace, opts)

Get active subscriptons

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.BillingApi();
let namespace = "namespace_example"; // String | User or team name.
let opts = {
  'limit': "limit_example", // String | Limit when getting items.
  'offset': "offset_example", // String | Offset when getting items.
  'ordering': "ordering_example" // String | Ordering when getting items.
};
apiInstance.billingSubscriptionsList(namespace, opts, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
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


## billingSubscriptionsRead

> Subscription billingSubscriptionsRead(namespace, id)

Get a subscriptions

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.BillingApi();
let namespace = "namespace_example"; // String | User or team name.
let id = "id_example"; // String | Unique identifier expressed as UUID.
apiInstance.billingSubscriptionsRead(namespace, id, (error, data, response) => {
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
 **namespace** | **String**| User or team name. | 
 **id** | **String**| Unique identifier expressed as UUID. | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## teamsBillingInvoiceItemsList_0

> [InvoiceItem] teamsBillingInvoiceItemsList_0(team, invoiceId, opts)

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

let apiInstance = new IllumiDesk.BillingApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let invoiceId = "invoiceId_example"; // String | Invoice id, expressed as UUID.
let opts = {
  'limit': "limit_example", // String | Limit when getting items.
  'offset': "offset_example", // String | Offset when getting items.
  'ordering': "ordering_example" // String | Ordering when getting items.
};
apiInstance.teamsBillingInvoiceItemsList_0(team, invoiceId, opts, (error, data, response) => {
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


## teamsBillingInvoiceItemsRead_0

> InvoiceItem teamsBillingInvoiceItemsRead_0(team, invoiceId, id)

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

let apiInstance = new IllumiDesk.BillingApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let invoiceId = "invoiceId_example"; // String | Invoice id, expressed as UUID.
let id = "id_example"; // String | InvoiceItem id, expressed as UUID.
apiInstance.teamsBillingInvoiceItemsRead_0(team, invoiceId, id, (error, data, response) => {
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


## teamsBillingInvoicesList_0

> [Invoice] teamsBillingInvoicesList_0(team, opts)

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

let apiInstance = new IllumiDesk.BillingApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let opts = {
  'limit': "limit_example", // String | Limit when getting items.
  'offset': "offset_example" // String | Offset when getting items.
};
apiInstance.teamsBillingInvoicesList_0(team, opts, (error, data, response) => {
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


## teamsBillingInvoicesRead_0

> Invoice teamsBillingInvoicesRead_0(team, id)

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

let apiInstance = new IllumiDesk.BillingApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let id = "id_example"; // String | Invoice unique identifier expressed as UUID.
apiInstance.teamsBillingInvoicesRead_0(team, id, (error, data, response) => {
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


## teamsBillingSubscriptionsCreate_0

> Subscription teamsBillingSubscriptionsCreate_0(team, opts)

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

let apiInstance = new IllumiDesk.BillingApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let opts = {
  'subscriptionData': new IllumiDesk.SubscriptionData() // SubscriptionData | 
};
apiInstance.teamsBillingSubscriptionsCreate_0(team, opts, (error, data, response) => {
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


## teamsBillingSubscriptionsDelete_0

> teamsBillingSubscriptionsDelete_0(team, id)

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

let apiInstance = new IllumiDesk.BillingApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let id = "id_example"; // String | Subscription unique identifier expressed as UUID.
apiInstance.teamsBillingSubscriptionsDelete_0(team, id, (error, data, response) => {
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


## teamsBillingSubscriptionsList_0

> [Subscription] teamsBillingSubscriptionsList_0(team, opts)

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

let apiInstance = new IllumiDesk.BillingApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let opts = {
  'limit': "limit_example", // String | Limit when getting items.
  'offset': "offset_example", // String | Offset when getting items.
  'ordering': "ordering_example" // String | Ordering when getting items.
};
apiInstance.teamsBillingSubscriptionsList_0(team, opts, (error, data, response) => {
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


## teamsBillingSubscriptionsRead_0

> Subscription teamsBillingSubscriptionsRead_0(team, id)

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

let apiInstance = new IllumiDesk.BillingApi();
let team = "team_example"; // String | Team unique identifier expressed as UUID or name.
let id = "id_example"; // String | Unique identifier expressed as UUID.
apiInstance.teamsBillingSubscriptionsRead_0(team, id, (error, data, response) => {
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

