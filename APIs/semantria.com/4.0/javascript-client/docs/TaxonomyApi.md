# Semantria.TaxonomyApi

All URIs are relative to *https://api.semantria.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addTaxonomy**](TaxonomyApi.md#addTaxonomy) | **POST** /taxonomy.{content_type} | Add taxonomy nodes
[**deleteTaxonomy**](TaxonomyApi.md#deleteTaxonomy) | **DELETE** /taxonomy.{content_type} | Remove taxonomy nodes
[**getTaxonomy**](TaxonomyApi.md#getTaxonomy) | **GET** /taxonomy.{content_type} | Retrieve taxonomy
[**updateTaxonomy**](TaxonomyApi.md#updateTaxonomy) | **PUT** /taxonomy.{content_type} | Update taxonomy nodes



## addTaxonomy

> [TaxonomyNodeResponseVersion] addTaxonomy(contentType, taxonomy, opts)

Add taxonomy nodes

This method adds taxonomy nodes on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.TaxonomyApi();
let contentType = "contentType_example"; // String | 
let taxonomy = {key: null}; // Object | List of parametrized JSON or XML objects.
let opts = {
  'configId': "configId_example" // String | Identifier of configuration queries linked to.
};
apiInstance.addTaxonomy(contentType, taxonomy, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **taxonomy** | **Object**| List of parametrized JSON or XML objects. | 
 **configId** | **String**| Identifier of configuration queries linked to. | [optional] 

### Return type

[**[TaxonomyNodeResponseVersion]**](TaxonomyNodeResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## deleteTaxonomy

> deleteTaxonomy(contentType, taxonomyNodeIDs, opts)

Remove taxonomy nodes

This method removes certain taxonomy nodes by their IDs on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.TaxonomyApi();
let contentType = "contentType_example"; // String | 
let taxonomyNodeIDs = ["null"]; // [String] | List of taxonomy node identifiers.
let opts = {
  'configId': "configId_example" // String | Identifier of configuration queries linked to.
};
apiInstance.deleteTaxonomy(contentType, taxonomyNodeIDs, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **taxonomyNodeIDs** | [**[String]**](String.md)| List of taxonomy node identifiers. | 
 **configId** | **String**| Identifier of configuration queries linked to. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getTaxonomy

> [TaxonomyNodeResponseVersion] getTaxonomy(contentType, opts)

Retrieve taxonomy

This method retrieves list of taxonomy available on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.TaxonomyApi();
let contentType = "contentType_example"; // String | 
let opts = {
  'configId': "configId_example" // String | Identifier of configuration taxonomy linked to.
};
apiInstance.getTaxonomy(contentType, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **configId** | **String**| Identifier of configuration taxonomy linked to. | [optional] 

### Return type

[**[TaxonomyNodeResponseVersion]**](TaxonomyNodeResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## updateTaxonomy

> [TaxonomyNodeResponseVersion] updateTaxonomy(contentType, taxonomy, opts)

Update taxonomy nodes

This method updates taxonomy nodes on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.TaxonomyApi();
let contentType = "contentType_example"; // String | 
let taxonomy = {key: null}; // Object | List of parametrized JSON or XML objects.
let opts = {
  'configId': "configId_example" // String | Identifier of configuration queries linked to.
};
apiInstance.updateTaxonomy(contentType, taxonomy, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **taxonomy** | **Object**| List of parametrized JSON or XML objects. | 
 **configId** | **String**| Identifier of configuration queries linked to. | [optional] 

### Return type

[**[TaxonomyNodeResponseVersion]**](TaxonomyNodeResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

