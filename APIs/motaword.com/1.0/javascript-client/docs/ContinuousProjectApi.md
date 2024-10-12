# MotaWordApi.ContinuousProjectApi

All URIs are relative to *https://api.motaword.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addDocument**](ContinuousProjectApi.md#addDocument) | **POST** /continuous_projects/{projectId}/documents | Add a new document to your continuous project
[**collectAnalytics**](ContinuousProjectApi.md#collectAnalytics) | **POST** /continuous_projects/{id}/collect-analytics | Save/collect analytics data from Active widget
[**complete**](ContinuousProjectApi.md#complete) | **POST** /continuous_projects/{id}/complete | Complete continuous project
[**completeContinuousDocument**](ContinuousProjectApi.md#completeContinuousDocument) | **POST** /continuous_projects/{id}/documents/{documentId}/complete | Complete a continuous project document
[**completeLanguage**](ContinuousProjectApi.md#completeLanguage) | **POST** /continuous_projects/{id}/languages/{targetLanguage}/complete | Complete continuous project language
[**createActiveWidget**](ContinuousProjectApi.md#createActiveWidget) | **POST** /continuous_projects/{projectId}/widgets | Create a new Active widget
[**createContinuousProject**](ContinuousProjectApi.md#createContinuousProject) | **POST** /continuous_projects | Create a continuous project
[**createSubscription**](ContinuousProjectApi.md#createSubscription) | **POST** /continuous_projects/{id}/subscription | Create subscription for continuous project
[**deleteActiveWidget**](ContinuousProjectApi.md#deleteActiveWidget) | **DELETE** /continuous_projects/{projectId}/widgets/{widgetId} | Delete a single widget for this Active project
[**deleteContinuousProject**](ContinuousProjectApi.md#deleteContinuousProject) | **DELETE** /continuous_projects/{id} | Delete a continuous project
[**deleteSubscription**](ContinuousProjectApi.md#deleteSubscription) | **DELETE** /continuous_projects/{id}/subscription | Delete subscription for continuous project
[**getActiveWidget**](ContinuousProjectApi.md#getActiveWidget) | **GET** /continuous_projects/{projectId}/widgets/{widgetId} | View an Active widget
[**getActiveWidgets**](ContinuousProjectApi.md#getActiveWidgets) | **GET** /continuous_projects/{projectId}/widgets | View Active widgets
[**getAnalyticsToken**](ContinuousProjectApi.md#getAnalyticsToken) | **GET** /continuous_projects/{id}/analytics-token | Get JWT token to be used in analytics dashboards
[**getContinuousProject**](ContinuousProjectApi.md#getContinuousProject) | **GET** /continuous_projects/{id} | View a continuous project
[**getContinuousProjectDocument**](ContinuousProjectApi.md#getContinuousProjectDocument) | **GET** /continuous_projects/{projectId}/documents/{documentId} | View a continuous document
[**getContinuousProjectDocumentProgress**](ContinuousProjectApi.md#getContinuousProjectDocumentProgress) | **GET** /continuous_projects/{projectId}/documents/{documentId}/progress | Monitor progress of a continuous document
[**getContinuousProjectDocuments**](ContinuousProjectApi.md#getContinuousProjectDocuments) | **GET** /continuous_projects/{projectId}/documents | View continuous documents
[**getContinuousProjectInvoices**](ContinuousProjectApi.md#getContinuousProjectInvoices) | **GET** /continuous_projects/{projectId}/invoices | Invoices of a continuous project
[**getContinuousProjectProgress**](ContinuousProjectApi.md#getContinuousProjectProgress) | **GET** /continuous_projects/{projectId}/progress | Monitor progress and status of a continous project
[**getContinuousProjects**](ContinuousProjectApi.md#getContinuousProjects) | **GET** /continuous_projects | View continuous projects
[**getQuoteForDocument**](ContinuousProjectApi.md#getQuoteForDocument) | **POST** /continuous_projects/{id}/documents/{documentId}/quote | Get a quote for a continuous project document
[**getQuoteForDocuments**](ContinuousProjectApi.md#getQuoteForDocuments) | **POST** /continuous_projects/{id}/documents/quote | Get quote for documents
[**getQuoteForLanguage**](ContinuousProjectApi.md#getQuoteForLanguage) | **POST** /continuous_projects/{id}/languages/{targetLanguage}/quote | Get quote for language
[**getQuoteForLanguages**](ContinuousProjectApi.md#getQuoteForLanguages) | **POST** /continuous_projects/{id}/languages/quote | Get quote for languages
[**getSubscription**](ContinuousProjectApi.md#getSubscription) | **GET** /continuous_projects/{id}/subscription | Get subscription for continuous project
[**postContinuousProjectDocumentProgress**](ContinuousProjectApi.md#postContinuousProjectDocumentProgress) | **POST** /continuous_projects/{projectId}/documents/progress | Get continuous project document progress for multiple IDs
[**resetActiveWidgetToken**](ContinuousProjectApi.md#resetActiveWidgetToken) | **POST** /continuous_projects/{projectId}/widgets/{widgetId}/reset-token | Reset Active widget token
[**translate**](ContinuousProjectApi.md#translate) | **POST** /continuous_projects/{id}/translate/{targetLanguage} | Instantly translate your content
[**updateActiveWidget**](ContinuousProjectApi.md#updateActiveWidget) | **POST** /continuous_projects/{projectId}/widgets/{widgetId} | Update Active widget settings.
[**updateContinuousProject**](ContinuousProjectApi.md#updateContinuousProject) | **POST** /continuous_projects/{id} | Update a continuous project
[**updateDocument**](ContinuousProjectApi.md#updateDocument) | **POST** /continuous_projects/{projectId}/documents/{documentId} | Update the document
[**updateSubscription**](ContinuousProjectApi.md#updateSubscription) | **PUT** /continuous_projects/{id}/subscription | Update subscription for continuous project
[**updateSubscriptionPaymentMethod**](ContinuousProjectApi.md#updateSubscriptionPaymentMethod) | **PUT** /continuous_projects/{id}/subscription/payment | Update subscription payment method for continuous project



## addDocument

> ContinuousProjectDocument addDocument(projectId, opts)

Add a new document to your continuous project

Add a new document to your continuous project. If the name already exists, it will update the existing document. In most scenarios, this operation will also trigger auto-translation of your document, via MT and/or TM.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let projectId = 74; // Number | Continuous project ID
let opts = {
  'addOrUpdateDocumentRequest': new MotaWordApi.AddOrUpdateDocumentRequest() // AddOrUpdateDocumentRequest | 
};
apiInstance.addDocument(projectId, opts, (error, data, response) => {
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
 **projectId** | **Number**| Continuous project ID | 
 **addOrUpdateDocumentRequest** | [**AddOrUpdateDocumentRequest**](AddOrUpdateDocumentRequest.md)|  | [optional] 

### Return type

[**ContinuousProjectDocument**](ContinuousProjectDocument.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## collectAnalytics

> OperationStatus collectAnalytics(id, opts)

Save/collect analytics data from Active widget

Save/collect analytics data from Active widget

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let id = 74; // Number | Continuous project ID
let opts = {
  'analyticsCollection': new MotaWordApi.AnalyticsCollection() // AnalyticsCollection | 
};
apiInstance.collectAnalytics(id, opts, (error, data, response) => {
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
 **id** | **Number**| Continuous project ID | 
 **analyticsCollection** | [**AnalyticsCollection**](AnalyticsCollection.md)|  | [optional] 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## complete

> OperationStatus complete(id)

Complete continuous project

Complete continuous project

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let id = 74; // Number | Continuous project ID
apiInstance.complete(id, (error, data, response) => {
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
 **id** | **Number**| Continuous project ID | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## completeContinuousDocument

> OperationStatus completeContinuousDocument(id, documentId)

Complete a continuous project document

Complete a continuous project document. Per your project settings, a continuous project document can be target language-specific or project-wide for all target languages of the project.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let id = 74; // Number | Continuous project ID
let documentId = 179469; // Number | Document ID
apiInstance.completeContinuousDocument(id, documentId, (error, data, response) => {
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
 **id** | **Number**| Continuous project ID | 
 **documentId** | **Number**| Document ID | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## completeLanguage

> OperationStatus completeLanguage(id, targetLanguage)

Complete continuous project language

Complete continuous project language

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let id = 74; // Number | Continuous project ID
let targetLanguage = "en-US"; // String | Target language that you want to complete
apiInstance.completeLanguage(id, targetLanguage, (error, data, response) => {
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
 **id** | **Number**| Continuous project ID | 
 **targetLanguage** | **String**| Target language that you want to complete | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createActiveWidget

> ActiveWidget createActiveWidget(projectId, opts)

Create a new Active widget

Create a new widget for your Active project to be used in your website. Most website-specific configuration is provided via widgets. This does not create a new Active project, just a separate widget.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let projectId = 74; // Number | Continuous project ID
let opts = {
  'activeWidget': new MotaWordApi.ActiveWidget() // ActiveWidget | 
};
apiInstance.createActiveWidget(projectId, opts, (error, data, response) => {
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
 **projectId** | **Number**| Continuous project ID | 
 **activeWidget** | [**ActiveWidget**](ActiveWidget.md)|  | [optional] 

### Return type

[**ActiveWidget**](ActiveWidget.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createContinuousProject

> ContinuousProject createContinuousProject(opts)

Create a continuous project

Create a new continuous project for your software, website, CI/CD translation needs.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let opts = {
  'continuousProject': new MotaWordApi.ContinuousProject() // ContinuousProject | 
};
apiInstance.createContinuousProject(opts, (error, data, response) => {
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
 **continuousProject** | [**ContinuousProject**](ContinuousProject.md)|  | [optional] 

### Return type

[**ContinuousProject**](ContinuousProject.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSubscription

> Subscription createSubscription(id, subscription)

Create subscription for continuous project

Create subscription for continuous project

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let id = 74; // Number | Continuous project ID
let subscription = new MotaWordApi.Subscription(); // Subscription | 
apiInstance.createSubscription(id, subscription, (error, data, response) => {
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
 **id** | **Number**| Continuous project ID | 
 **subscription** | [**Subscription**](Subscription.md)|  | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteActiveWidget

> OperationStatus deleteActiveWidget(projectId, widgetId)

Delete a single widget for this Active project

Delete a single widget for this Active project

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let projectId = 74; // Number | Continuous Project ID
let widgetId = 236; // Number | Active widget ID belonging to this Continuous Project
apiInstance.deleteActiveWidget(projectId, widgetId, (error, data, response) => {
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
 **projectId** | **Number**| Continuous Project ID | 
 **widgetId** | **Number**| Active widget ID belonging to this Continuous Project | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteContinuousProject

> OperationStatus deleteContinuousProject(id)

Delete a continuous project

Delete an existing continuous project. Your project will be cancelled, and you will still be charged for the amount of translations we have done for you so far.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let id = 74; // Number | Continuous project ID
apiInstance.deleteContinuousProject(id, (error, data, response) => {
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
 **id** | **Number**| Continuous project ID | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSubscription

> Subscription deleteSubscription(id)

Delete subscription for continuous project

Delete subscription for continuous project

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let id = 74; // Number | Continuous project ID
apiInstance.deleteSubscription(id, (error, data, response) => {
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
 **id** | **Number**| Continuous project ID | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getActiveWidget

> ActiveWidget getActiveWidget(projectId, widgetId)

View an Active widget

View the details of an Active widget to be used in your website. Most website-specific configuration is provided via widgets.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let projectId = 74; // Number | Continuous Project ID
let widgetId = 236; // Number | Active widget ID belonging to this Continuous Project
apiInstance.getActiveWidget(projectId, widgetId, (error, data, response) => {
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
 **projectId** | **Number**| Continuous Project ID | 
 **widgetId** | **Number**| Active widget ID belonging to this Continuous Project | 

### Return type

[**ActiveWidget**](ActiveWidget.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getActiveWidgets

> ActiveWidgetList getActiveWidgets(projectId)

View Active widgets

View a list of widgets in your Active project to be used in your website. Most website-specific configuration is provided via widgets.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let projectId = 74; // Number | Continuous Project ID
apiInstance.getActiveWidgets(projectId, (error, data, response) => {
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
 **projectId** | **Number**| Continuous Project ID | 

### Return type

[**ActiveWidgetList**](ActiveWidgetList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAnalyticsToken

> AnalyticsToken getAnalyticsToken(id)

Get JWT token to be used in analytics dashboards

Get JWT token to be used in analytics dashboards

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let id = 74; // Number | Continuous project ID
apiInstance.getAnalyticsToken(id, (error, data, response) => {
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
 **id** | **Number**| Continuous project ID | 

### Return type

[**AnalyticsToken**](AnalyticsToken.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContinuousProject

> ContinuousProject getContinuousProject(id)

View a continuous project

View the details of a continuous project.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let id = 74; // Number | Continuous Project ID
apiInstance.getContinuousProject(id, (error, data, response) => {
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
 **id** | **Number**| Continuous Project ID | 

### Return type

[**ContinuousProject**](ContinuousProject.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContinuousProjectDocument

> ContinuousProjectDocument getContinuousProjectDocument(projectId, documentId)

View a continuous document

View the details of a source document in continuous translation project.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let projectId = 74; // Number | Continuous project ID
let documentId = 179469; // Number | Document ID/Name
apiInstance.getContinuousProjectDocument(projectId, documentId, (error, data, response) => {
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
 **projectId** | **Number**| Continuous project ID | 
 **documentId** | **Number**| Document ID/Name | 

### Return type

[**ContinuousProjectDocument**](ContinuousProjectDocument.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContinuousProjectDocumentProgress

> Progress getContinuousProjectDocumentProgress(projectId, documentId, opts)

Monitor progress of a continuous document

Monitor the translation progress of a document in a continuous project in real-time.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let projectId = 74; // Number | Continuous project ID
let documentId = 179469; // Number | Document ID/Name
let opts = {
  'filterByLanguage': "filterByLanguage_example" // String | 
};
apiInstance.getContinuousProjectDocumentProgress(projectId, documentId, opts, (error, data, response) => {
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
 **projectId** | **Number**| Continuous project ID | 
 **documentId** | **Number**| Document ID/Name | 
 **filterByLanguage** | **String**|  | [optional] 

### Return type

[**Progress**](Progress.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContinuousProjectDocuments

> ContinuousProjectDocumentList getContinuousProjectDocuments(projectId, opts)

View continuous documents

View the documents under this continuous project

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let projectId = 74; // Number | Continuous Project ID
let opts = {
  'filterByLanguage': "filterByLanguage_example" // String | 
};
apiInstance.getContinuousProjectDocuments(projectId, opts, (error, data, response) => {
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
 **projectId** | **Number**| Continuous Project ID | 
 **filterByLanguage** | **String**|  | [optional] 

### Return type

[**ContinuousProjectDocumentList**](ContinuousProjectDocumentList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContinuousProjectInvoices

> ContinuousProjectInvoices getContinuousProjectInvoices(projectId)

Invoices of a continuous project

Get real-time access to a continuous project&#39;s invoices.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let projectId = 74; // Number | Project ID
apiInstance.getContinuousProjectInvoices(projectId, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 

### Return type

[**ContinuousProjectInvoices**](ContinuousProjectInvoices.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContinuousProjectProgress

> ContinuousProjectProgress getContinuousProjectProgress(projectId, opts)

Monitor progress and status of a continous project

Monitor the translation progress of an ongoing continuous project in real-time.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let projectId = 74; // Number | Project ID
let opts = {
  'filterByLanguage': "filterByLanguage_example" // String | 
};
apiInstance.getContinuousProjectProgress(projectId, opts, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 
 **filterByLanguage** | **String**|  | [optional] 

### Return type

[**ContinuousProjectProgress**](ContinuousProjectProgress.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContinuousProjects

> ContinuousProjectsList getContinuousProjects(opts)

View continuous projects

View a list of continuous projects under your account. Continuous projects are those that are constantly updated, such as a CI/CD project, software project, website translation and such.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let opts = {
  'type': "'active'" // String | Type of continuous project.
};
apiInstance.getContinuousProjects(opts, (error, data, response) => {
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
 **type** | **String**| Type of continuous project. | [optional] [default to &#39;active&#39;]

### Return type

[**ContinuousProjectsList**](ContinuousProjectsList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getQuoteForDocument

> ProjectList getQuoteForDocument(id, documentId)

Get a quote for a continuous project document

Get a new quote for provided document in continuous project. Per your project settings, a continuous project document can be target language-specific or project-wide for all target languages of the project.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let id = 74; // Number | Continuous project ID
let documentId = 179469; // Number | Document ID
apiInstance.getQuoteForDocument(id, documentId, (error, data, response) => {
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
 **id** | **Number**| Continuous project ID | 
 **documentId** | **Number**| Document ID | 

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getQuoteForDocuments

> ProjectList getQuoteForDocuments(id, opts)

Get quote for documents

Get a new quote for provided documents in continuous project

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let id = 74; // Number | Continuous project ID
let opts = {
  'getQuotesForDocumentsBody': new MotaWordApi.GetQuotesForDocumentsBody() // GetQuotesForDocumentsBody | 
};
apiInstance.getQuoteForDocuments(id, opts, (error, data, response) => {
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
 **id** | **Number**| Continuous project ID | 
 **getQuotesForDocumentsBody** | [**GetQuotesForDocumentsBody**](GetQuotesForDocumentsBody.md)|  | [optional] 

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getQuoteForLanguage

> ProjectList getQuoteForLanguage(id, targetLanguage)

Get quote for language

Get a new quote for provided target language in continuous project

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let id = 74; // Number | Continuous project ID
let targetLanguage = "en-US"; // String | Target language that you want to complete
apiInstance.getQuoteForLanguage(id, targetLanguage, (error, data, response) => {
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
 **id** | **Number**| Continuous project ID | 
 **targetLanguage** | **String**| Target language that you want to complete | 

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getQuoteForLanguages

> ProjectList getQuoteForLanguages(id, opts)

Get quote for languages

Get a new quote for provided target languages in continuous project

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let id = 74; // Number | Continuous project ID
let opts = {
  'getQuotesForLanguagesBody': new MotaWordApi.GetQuotesForLanguagesBody() // GetQuotesForLanguagesBody | 
};
apiInstance.getQuoteForLanguages(id, opts, (error, data, response) => {
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
 **id** | **Number**| Continuous project ID | 
 **getQuotesForLanguagesBody** | [**GetQuotesForLanguagesBody**](GetQuotesForLanguagesBody.md)|  | [optional] 

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSubscription

> Subscription getSubscription(id)

Get subscription for continuous project

Get subscription for continuous project

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let id = 74; // Number | Continuous project ID
apiInstance.getSubscription(id, (error, data, response) => {
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
 **id** | **Number**| Continuous project ID | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postContinuousProjectDocumentProgress

> Progress postContinuousProjectDocumentProgress(projectId, opts)

Get continuous project document progress for multiple IDs

Get continuous project document progress for multiple IDs

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let projectId = 74; // Number | Continuous project ID
let opts = {
  'continuousProjectDocumentProgressBody': new MotaWordApi.ContinuousProjectDocumentProgressBody() // ContinuousProjectDocumentProgressBody | 
};
apiInstance.postContinuousProjectDocumentProgress(projectId, opts, (error, data, response) => {
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
 **projectId** | **Number**| Continuous project ID | 
 **continuousProjectDocumentProgressBody** | [**ContinuousProjectDocumentProgressBody**](ContinuousProjectDocumentProgressBody.md)|  | [optional] 

### Return type

[**Progress**](Progress.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resetActiveWidgetToken

> ActiveWidget resetActiveWidgetToken(projectId, widgetId)

Reset Active widget token

Reset the public token used with your Active widget. This token is used when communicating from your environment to MotaWord systems for translation, analytics and meta.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let projectId = 74; // Number | Continuous Project ID
let widgetId = 236; // Number | Active widget ID belonging to this Continuous Project
apiInstance.resetActiveWidgetToken(projectId, widgetId, (error, data, response) => {
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
 **projectId** | **Number**| Continuous Project ID | 
 **widgetId** | **Number**| Active widget ID belonging to this Continuous Project | 

### Return type

[**ActiveWidget**](ActiveWidget.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## translate

> InstantTranslationResult translate(id, targetLanguage, opts)

Instantly translate your content

Instantly translate your content with your existing TM and MT resources. This is the primary endpoint to translate your files and content on the fly, especially in CI/CD environments. This is a complex endpoint that is configured in your Active or Continuous Project dashboards. For instance, you can configure whether to use your TM, or translate missing strings via MT and then post-edit those new translations. There are various scenarios you can establish via a set of configurations.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let id = 74; // Number | Continuous project ID
let targetLanguage = "en-US"; // String | Target language that you want to instantly translate your file into.
let opts = {
  'instantTranslationRequest': new MotaWordApi.InstantTranslationRequest() // InstantTranslationRequest | 
};
apiInstance.translate(id, targetLanguage, opts, (error, data, response) => {
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
 **id** | **Number**| Continuous project ID | 
 **targetLanguage** | **String**| Target language that you want to instantly translate your file into. | 
 **instantTranslationRequest** | [**InstantTranslationRequest**](InstantTranslationRequest.md)|  | [optional] 

### Return type

[**InstantTranslationResult**](InstantTranslationResult.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateActiveWidget

> ActiveWidget updateActiveWidget(projectId, widgetId, opts)

Update Active widget settings.

Update Active widget settings.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let projectId = 74; // Number | Continuous Project ID
let widgetId = 236; // Number | Active widget ID belonging to this Continuous Project
let opts = {
  'activeWidget': new MotaWordApi.ActiveWidget() // ActiveWidget | 
};
apiInstance.updateActiveWidget(projectId, widgetId, opts, (error, data, response) => {
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
 **projectId** | **Number**| Continuous Project ID | 
 **widgetId** | **Number**| Active widget ID belonging to this Continuous Project | 
 **activeWidget** | [**ActiveWidget**](ActiveWidget.md)|  | [optional] 

### Return type

[**ActiveWidget**](ActiveWidget.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateContinuousProject

> ContinuousProject updateContinuousProject(id, opts)

Update a continuous project

Update the details and settings of continuous project.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let id = 74; // Number | Continuous project ID
let opts = {
  'continuousProjectUpdateContent': new MotaWordApi.ContinuousProjectUpdateContent() // ContinuousProjectUpdateContent | 
};
apiInstance.updateContinuousProject(id, opts, (error, data, response) => {
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
 **id** | **Number**| Continuous project ID | 
 **continuousProjectUpdateContent** | [**ContinuousProjectUpdateContent**](ContinuousProjectUpdateContent.md)|  | [optional] 

### Return type

[**ContinuousProject**](ContinuousProject.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDocument

> ContinuousProjectDocument updateDocument(projectId, documentId, opts)

Update the document

Update source document in your continuous project. In most scenarios, this operation will also trigger auto-translation of your document, via MT and/or TM.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let projectId = 74; // Number | Continuous project ID
let documentId = 179469; // Number | Continuous project document ID
let opts = {
  'addOrUpdateDocumentRequest': new MotaWordApi.AddOrUpdateDocumentRequest() // AddOrUpdateDocumentRequest | 
};
apiInstance.updateDocument(projectId, documentId, opts, (error, data, response) => {
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
 **projectId** | **Number**| Continuous project ID | 
 **documentId** | **Number**| Continuous project document ID | 
 **addOrUpdateDocumentRequest** | [**AddOrUpdateDocumentRequest**](AddOrUpdateDocumentRequest.md)|  | [optional] 

### Return type

[**ContinuousProjectDocument**](ContinuousProjectDocument.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSubscription

> Subscription updateSubscription(id, subscription)

Update subscription for continuous project

Update subscription for continuous project

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let id = 74; // Number | Continuous project ID
let subscription = new MotaWordApi.Subscription(); // Subscription | 
apiInstance.updateSubscription(id, subscription, (error, data, response) => {
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
 **id** | **Number**| Continuous project ID | 
 **subscription** | [**Subscription**](Subscription.md)|  | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSubscriptionPaymentMethod

> Subscription updateSubscriptionPaymentMethod(id, subscription)

Update subscription payment method for continuous project

Update subscription payment method for continuous project

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.ContinuousProjectApi();
let id = 74; // Number | Continuous project ID
let subscription = new MotaWordApi.Subscription(); // Subscription | 
apiInstance.updateSubscriptionPaymentMethod(id, subscription, (error, data, response) => {
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
 **id** | **Number**| Continuous project ID | 
 **subscription** | [**Subscription**](Subscription.md)|  | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

