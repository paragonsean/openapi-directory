# BcGeographicalNamesWebServiceRestApi.FeatureTaxonomyApi

All URIs are relative to *https://apps.gov.bc.ca/pub/bcgnws*

Method | HTTP request | Description
------------- | ------------- | -------------
[**featureCategoriesGet**](FeatureTaxonomyApi.md#featureCategoriesGet) | **GET** /featureCategories | Get all feature categories
[**featureClassesGet**](FeatureTaxonomyApi.md#featureClassesGet) | **GET** /featureClasses | Get all feature classes
[**featureTypesGet**](FeatureTaxonomyApi.md#featureTypesGet) | **GET** /featureTypes | Get all feature types



## featureCategoriesGet

> featureCategoriesGet(outputFormat)

Get all feature categories

Gets a list of all feature categories used by the BC Geographical Names Information System (BCGNIS).  Note: there are three levels of classification in the BCGNIS feature taxonomy: classes, categories and types.  A type is a subset of a category, and a category is a subset of a class.

### Example

```javascript
import BcGeographicalNamesWebServiceRestApi from 'bc_geographical_names_web_service_rest_api';

let apiInstance = new BcGeographicalNamesWebServiceRestApi.FeatureTaxonomyApi();
let outputFormat = "json"; // String | The format of the output.
apiInstance.featureCategoriesGet(outputFormat, (error, data, response) => {
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
 **outputFormat** | **String**| The format of the output. | [default to &#39;json&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## featureClassesGet

> featureClassesGet(outputFormat)

Get all feature classes

Gets a list of all feature classes used by the BC Geographical Names Information System (BCGNIS).  Note: there are three levels of classification in the BCGNIS feature taxonomy: classes, categories and types.  A type is a subset of a category, and a category is a subset of a class.

### Example

```javascript
import BcGeographicalNamesWebServiceRestApi from 'bc_geographical_names_web_service_rest_api';

let apiInstance = new BcGeographicalNamesWebServiceRestApi.FeatureTaxonomyApi();
let outputFormat = "json"; // String | The format of the output.
apiInstance.featureClassesGet(outputFormat, (error, data, response) => {
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
 **outputFormat** | **String**| The format of the output. | [default to &#39;json&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## featureTypesGet

> featureTypesGet(outputFormat)

Get all feature types

Gets a list of all feature types used by the BC Geographical Names Information System (BCGNIS).  Note: there are three levels of classification in the BCGNIS feature taxonomy: classes, categories and types.  A type is a subset of a category, and a category is a subset of a class.

### Example

```javascript
import BcGeographicalNamesWebServiceRestApi from 'bc_geographical_names_web_service_rest_api';

let apiInstance = new BcGeographicalNamesWebServiceRestApi.FeatureTaxonomyApi();
let outputFormat = "json"; // String | The format of the output.
apiInstance.featureTypesGet(outputFormat, (error, data, response) => {
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
 **outputFormat** | **String**| The format of the output. | [default to &#39;json&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

