# BulkDataStorageSystemServices.ProductsApi

All URIs are relative to *http://localhost/BDSS-API*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLatestProductFilesByProductIdAndTime**](ProductsApi.md#getLatestProductFilesByProductIdAndTime) | **GET** /products/{shortName}/latest | Returns products along with their latest files by short names.
[**getPopulartProducts**](ProductsApi.md#getPopulartProducts) | **GET** /products/popular | Returns popular products along with latest files.
[**getProductSubTree**](ProductsApi.md#getProductSubTree) | **GET** /products/tree/{shortName} | Returns products&#39; hierarchical subtree.
[**getProductsByName**](ProductsApi.md#getProductsByName) | **GET** /products/byname/{productName} | Returns files associated with products (of level PRODUCT) based on their full or partial names.
[**getProductsByShortName**](ProductsApi.md#getProductsByShortName) | **GET** /products/{shortName} | Returns products along with their associated files by short names.
[**getProductsTree**](ProductsApi.md#getProductsTree) | **GET** /products/tree | Returns products&#39; hierarchical tree.
[**getProductsWithLatestProductFiles**](ProductsApi.md#getProductsWithLatestProductFiles) | **GET** /products/all/latest | Returns all products with Latest Files.



## getLatestProductFilesByProductIdAndTime

> getLatestProductFilesByProductIdAndTime(shortName, opts)

Returns products along with their latest files by short names.

Use this GET to search for latest released bulk data products by their short names and release year. The return response will include the latest files within the year specified.  An error message will be returned if product(s) cannot be found for the year specified

### Example

```javascript
import BulkDataStorageSystemServices from 'bulk_data_storage_system_services';

let apiInstance = new BulkDataStorageSystemServices.ProductsApi();
let shortName = "shortName_example"; // String | Short name of the product, for example, \"PTGRSP\"
let opts = {
  'year': 56, // Number | Year of the product files  needed, for example, 2001.
  'hierarchy': "'false'" // String | Boolean flag (possible values: true and false) to indicate if product hierarchy needs to be return in the response. By default it doesn't return the hierarchy in the response.
};
apiInstance.getLatestProductFilesByProductIdAndTime(shortName, opts, (error, data, response) => {
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
 **shortName** | **String**| Short name of the product, for example, \&quot;PTGRSP\&quot; | 
 **year** | **Number**| Year of the product files  needed, for example, 2001. | [optional] 
 **hierarchy** | **String**| Boolean flag (possible values: true and false) to indicate if product hierarchy needs to be return in the response. By default it doesn&#39;t return the hierarchy in the response. | [optional] [default to &#39;false&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPopulartProducts

> getPopulartProducts()

Returns popular products along with latest files.

Use this GET to retrieve these bulk data files by their popularity. The response includes product fields such as title, description, frequency, and level.

### Example

```javascript
import BulkDataStorageSystemServices from 'bulk_data_storage_system_services';

let apiInstance = new BulkDataStorageSystemServices.ProductsApi();
apiInstance.getPopulartProducts((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProductSubTree

> getProductSubTree(shortName)

Returns products&#39; hierarchical subtree.

Use this GET to search for bulk data products by their short names. This works almost like products/tree GET, the difference is that it returns subtree data starting from a particular tree node (i.e. the GET returns all children if parent short name is entered). If a product cannot be found by its short name (has to be exact match and is not case sensitive), then an error message will appear in response body.

### Example

```javascript
import BulkDataStorageSystemServices from 'bulk_data_storage_system_services';

let apiInstance = new BulkDataStorageSystemServices.ProductsApi();
let shortName = "shortName_example"; // String | Short name of the product, for example, \"PTISSD\"
apiInstance.getProductSubTree(shortName, (error, data, response) => {
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
 **shortName** | **String**| Short name of the product, for example, \&quot;PTISSD\&quot; | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProductsByName

> getProductsByName(productName, opts)

Returns files associated with products (of level PRODUCT) based on their full or partial names.

Use this GET to search for bulk data services by product name or description. An error message will be returned if the product cannot be found by name. Note that product name is not case sensitive. You can enter full or partial name of an existing product to receive bulk data services. Default values for field names are as follows - if both years are not defined, toYear will be set equal to current year, fromYear will be set equal to previous year - if fromYear is defined, toYear will be set equal to fromYear+1 - if fromMonth not defined, current month will be used - if toMonth not defined, it will be set equal to fromMonth - if fromDay is not defined, it will be set equal to current day (today) - if toDay is not defined, it will be set to the last day of toMonth/toYear

### Example

```javascript
import BulkDataStorageSystemServices from 'bulk_data_storage_system_services';

let apiInstance = new BulkDataStorageSystemServices.ProductsApi();
let productName = "productName_example"; // String | Name of the product, for example, \"Trademark\"
let opts = {
  'fromYear': 56, // Number | Year from when the product files are needed, for example, 1999.
  'toYear': 56, // Number | Year until when the product files are needed, for example, 2000.
  'fromMonth': 56, // Number | Month from when the product files are needed, for example, 01.
  'toMonth': 56, // Number | Month until when the product files are needed, for example, 12.
  'fromDay': 56, // Number | Day from when the product files are needed, for example, 01.
  'toDay': 56, // Number | Day until when the product files are needed, for example, 31.
  'hierarchy': "'false'", // String | Boolean flag to indicate if product hierarchy needs to be return in the response. By default it doesn't return the hierarchy in the response.
  'maxFiles': 20 // Number | Max. number of files to retrieve, per product. Set value to -1 to get all files
};
apiInstance.getProductsByName(productName, opts, (error, data, response) => {
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
 **productName** | **String**| Name of the product, for example, \&quot;Trademark\&quot; | 
 **fromYear** | **Number**| Year from when the product files are needed, for example, 1999. | [optional] 
 **toYear** | **Number**| Year until when the product files are needed, for example, 2000. | [optional] 
 **fromMonth** | **Number**| Month from when the product files are needed, for example, 01. | [optional] 
 **toMonth** | **Number**| Month until when the product files are needed, for example, 12. | [optional] 
 **fromDay** | **Number**| Day from when the product files are needed, for example, 01. | [optional] 
 **toDay** | **Number**| Day until when the product files are needed, for example, 31. | [optional] 
 **hierarchy** | **String**| Boolean flag to indicate if product hierarchy needs to be return in the response. By default it doesn&#39;t return the hierarchy in the response. | [optional] [default to &#39;false&#39;]
 **maxFiles** | **Number**| Max. number of files to retrieve, per product. Set value to -1 to get all files | [optional] [default to 20]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProductsByShortName

> getProductsByShortName(shortName, opts)

Returns products along with their associated files by short names.

Use this GET to search for bulk data products by their short names and description. Note that \&quot;From\&quot; and \&quot;To\&quot; dates can be inputted separately as year/month/day values or as a single date string in format \&quot;YYYY-MM-DD\&quot;. If all values are entered, single date strings have a higher priority For the list of default values rules, see GET /products/byname/{productName} above

### Example

```javascript
import BulkDataStorageSystemServices from 'bulk_data_storage_system_services';

let apiInstance = new BulkDataStorageSystemServices.ProductsApi();
let shortName = "shortName_example"; // String | Short name  of the product, for example, \"PTGRSP\"
let opts = {
  'fromYear': 56, // Number | Year from when the product files are needed, for example, 1999.
  'toYear': 56, // Number | Year until when the product files are needed, for example, 2000.
  'fromMonth': 56, // Number | Month from when the product files are needed, for example, 01.
  'toMonth': 56, // Number | Month until when the product files are needed, for example, 12.
  'fromDay': 56, // Number | Day from when the product files are needed, for example, 01.
  'toDay': 56, // Number | Day until when the product files are needed, for example, 31.
  'fromDate': "fromDate_example", // String | Year from when the product files are needed, for example, 1999-01-01.
  'toDate': "toDate_example", // String | Year until when the product files are needed, for example, 2001-12-31.
  'hierarchy': "'false'" // String | Boolean flag (possible values: true and false) to indicate if product hierarchy needs to be return in the response. By default it doesn't return the hierarchy in the response.
};
apiInstance.getProductsByShortName(shortName, opts, (error, data, response) => {
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
 **shortName** | **String**| Short name  of the product, for example, \&quot;PTGRSP\&quot; | 
 **fromYear** | **Number**| Year from when the product files are needed, for example, 1999. | [optional] 
 **toYear** | **Number**| Year until when the product files are needed, for example, 2000. | [optional] 
 **fromMonth** | **Number**| Month from when the product files are needed, for example, 01. | [optional] 
 **toMonth** | **Number**| Month until when the product files are needed, for example, 12. | [optional] 
 **fromDay** | **Number**| Day from when the product files are needed, for example, 01. | [optional] 
 **toDay** | **Number**| Day until when the product files are needed, for example, 31. | [optional] 
 **fromDate** | **String**| Year from when the product files are needed, for example, 1999-01-01. | [optional] 
 **toDate** | **String**| Year until when the product files are needed, for example, 2001-12-31. | [optional] 
 **hierarchy** | **String**| Boolean flag (possible values: true and false) to indicate if product hierarchy needs to be return in the response. By default it doesn&#39;t return the hierarchy in the response. | [optional] [default to &#39;false&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProductsTree

> getProductsTree()

Returns products&#39; hierarchical tree.

Use this GET to retrieve short name and parent/child relationships for bulk data products. Short names are unique IDs of the products and should be used in other GETs where {shortName} parameter is required Use this GET to perform initial exploration of the existing products hierarchy Short names are unique IDs of the products and should be used in other GETs where {shortName} parameter is required

### Example

```javascript
import BulkDataStorageSystemServices from 'bulk_data_storage_system_services';

let apiInstance = new BulkDataStorageSystemServices.ProductsApi();
apiInstance.getProductsTree((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProductsWithLatestProductFiles

> getProductsWithLatestProductFiles()

Returns all products with Latest Files.

Use this GET to retrieve latest released bulk data products. Note that there is one file per product. The response includes product fields such as title, description, frequency, and level.

### Example

```javascript
import BulkDataStorageSystemServices from 'bulk_data_storage_system_services';

let apiInstance = new BulkDataStorageSystemServices.ProductsApi();
apiInstance.getProductsWithLatestProductFiles((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

