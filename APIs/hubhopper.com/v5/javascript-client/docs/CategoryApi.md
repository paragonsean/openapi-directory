# HubhopperPartnerIntegrationApiSProduction.CategoryApi

All URIs are relative to *https://apis.hubhopper.com/partner*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categoriesCategoryIdGet**](CategoryApi.md#categoriesCategoryIdGet) | **GET** /categories/{categoryId} | 
[**categoriesCategoryIdPodcastsGet**](CategoryApi.md#categoriesCategoryIdPodcastsGet) | **GET** /categories/{categoryId}/podcasts | 
[**categoriesGet**](CategoryApi.md#categoriesGet) | **GET** /categories | 



## categoriesCategoryIdGet

> SingleCategory categoriesCategoryIdGet(categoryId)



Get specific content category.

### Example

```javascript
import HubhopperPartnerIntegrationApiSProduction from 'hubhopper_partner_integration_api_s_production';
let defaultClient = HubhopperPartnerIntegrationApiSProduction.ApiClient.instance;
// Configure API key authorization: partner_id
let partner_id = defaultClient.authentications['partner_id'];
partner_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//partner_id.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new HubhopperPartnerIntegrationApiSProduction.CategoryApi();
let categoryId = "categoryId_example"; // String | Unique qualifier for a category.
apiInstance.categoriesCategoryIdGet(categoryId, (error, data, response) => {
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
 **categoryId** | **String**| Unique qualifier for a category. | 

### Return type

[**SingleCategory**](SingleCategory.md)

### Authorization

[partner_id](../README.md#partner_id), [api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoriesCategoryIdPodcastsGet

> PodcastList categoriesCategoryIdPodcastsGet(categoryId, opts)



Get a list of all podcasts under a category.

### Example

```javascript
import HubhopperPartnerIntegrationApiSProduction from 'hubhopper_partner_integration_api_s_production';
let defaultClient = HubhopperPartnerIntegrationApiSProduction.ApiClient.instance;
// Configure API key authorization: partner_id
let partner_id = defaultClient.authentications['partner_id'];
partner_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//partner_id.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new HubhopperPartnerIntegrationApiSProduction.CategoryApi();
let categoryId = "categoryId_example"; // String | Unique qualifier for a category.
let opts = {
  'page': "page_example", // String | Provide the page number to fetch.
  'pageSize': "pageSize_example", // String | Provide the size of the page to fetch.
  'order': "order_example", // String | Order the items by 'newest' | 'random'
  'filters': "filters_example" // String | Takes filters like 'lang' in a url encoded json.  Example: 1)Single -> &nbsp;&nbsp;&nbsp;&nbsp; var filterJson = {\"lang\":[\"en\"]}; &nbsp;&nbsp;&nbsp;&nbsp; var url = baseUrl+'?'+filters=enocdeURI(JSON.stringify(filterJson)); 2)Multiple -> &nbsp;&nbsp;&nbsp;&nbsp; var filterJson = {\"lang\":[\"en\",\"hi\"]}; &nbsp;&nbsp;&nbsp;&nbsp; var url = baseUrl+'?'+filters=enocdeURI(JSON.stringify(filterJson));
};
apiInstance.categoriesCategoryIdPodcastsGet(categoryId, opts, (error, data, response) => {
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
 **categoryId** | **String**| Unique qualifier for a category. | 
 **page** | **String**| Provide the page number to fetch. | [optional] 
 **pageSize** | **String**| Provide the size of the page to fetch. | [optional] 
 **order** | **String**| Order the items by &#39;newest&#39; | &#39;random&#39; | [optional] 
 **filters** | **String**| Takes filters like &#39;lang&#39; in a url encoded json.  Example: 1)Single -&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var filterJson &#x3D; {\&quot;lang\&quot;:[\&quot;en\&quot;]}; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var url &#x3D; baseUrl+&#39;?&#39;+filters&#x3D;enocdeURI(JSON.stringify(filterJson)); 2)Multiple -&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var filterJson &#x3D; {\&quot;lang\&quot;:[\&quot;en\&quot;,\&quot;hi\&quot;]}; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var url &#x3D; baseUrl+&#39;?&#39;+filters&#x3D;enocdeURI(JSON.stringify(filterJson)); | [optional] 

### Return type

[**PodcastList**](PodcastList.md)

### Authorization

[partner_id](../README.md#partner_id), [api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoriesGet

> CategoryList categoriesGet(opts)



Get the list of all content categories.

### Example

```javascript
import HubhopperPartnerIntegrationApiSProduction from 'hubhopper_partner_integration_api_s_production';
let defaultClient = HubhopperPartnerIntegrationApiSProduction.ApiClient.instance;
// Configure API key authorization: partner_id
let partner_id = defaultClient.authentications['partner_id'];
partner_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//partner_id.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new HubhopperPartnerIntegrationApiSProduction.CategoryApi();
let opts = {
  'pageSize': "pageSize_example", // String | Provide the size of the page to fetch.
  'page': "page_example" // String | Provide the page number to fetch.
};
apiInstance.categoriesGet(opts, (error, data, response) => {
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
 **pageSize** | **String**| Provide the size of the page to fetch. | [optional] 
 **page** | **String**| Provide the page number to fetch. | [optional] 

### Return type

[**CategoryList**](CategoryList.md)

### Authorization

[partner_id](../README.md#partner_id), [api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

