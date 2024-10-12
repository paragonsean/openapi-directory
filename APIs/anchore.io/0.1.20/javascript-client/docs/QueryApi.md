# AnchoreEngineApiServer.QueryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queryImagesByPackage**](QueryApi.md#queryImagesByPackage) | **GET** /query/images/by_package | List of images containing given package
[**queryImagesByVulnerability**](QueryApi.md#queryImagesByVulnerability) | **GET** /query/images/by_vulnerability | List images vulnerable to the specific vulnerability ID.
[**queryVulnerabilities**](QueryApi.md#queryVulnerabilities) | **GET** /query/vulnerabilities | Listing information about given vulnerability



## queryImagesByPackage

> PaginatedImageList queryImagesByPackage(name, opts)

List of images containing given package

Filterable query interface to search for images containing specified package

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.QueryApi();
let name = "name_example"; // String | Name of package to search for (e.g. sed)
let opts = {
  'packageType': "packageType_example", // String | Type of package to filter on (e.g. dpkg)
  'version': "version_example", // String | Version of named package to filter on (e.g. 4.4-1)
  'page': "page_example", // String | The page of results to fetch. Pages start at 1
  'limit': 56, // Number | Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.queryImagesByPackage(name, opts, (error, data, response) => {
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
 **name** | **String**| Name of package to search for (e.g. sed) | 
 **packageType** | **String**| Type of package to filter on (e.g. dpkg) | [optional] 
 **version** | **String**| Version of named package to filter on (e.g. 4.4-1) | [optional] 
 **page** | **String**| The page of results to fetch. Pages start at 1 | [optional] 
 **limit** | **Number**| Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page | [optional] 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**PaginatedImageList**](PaginatedImageList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryImagesByVulnerability

> PaginatedVulnerableImageList queryImagesByVulnerability(vulnerabilityId, opts)

List images vulnerable to the specific vulnerability ID.

Returns a listing of images and their respective packages vulnerable to the given vulnerability ID

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.QueryApi();
let vulnerabilityId = "vulnerabilityId_example"; // String | The ID of the vulnerability to search for within all images stored in anchore-engine (e.g. CVE-1999-0001)
let opts = {
  'namespace': "namespace_example", // String | Filter results to images within the given vulnerability namespace (e.g. debian:8, ubuntu:14.04)
  'affectedPackage': "affectedPackage_example", // String | Filter results to images with vulnable packages with the given package name (e.g. libssl)
  'severity': "severity_example", // String | Filter results to vulnerable package/vulnerability with the given severity
  'vendorOnly': true, // Boolean | Filter results to include only vulnerabilities that are not marked as invalid by upstream OS vendor data
  'page': 56, // Number | The page of results to fetch. Pages start at 1
  'limit': 56, // Number | Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.queryImagesByVulnerability(vulnerabilityId, opts, (error, data, response) => {
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
 **vulnerabilityId** | **String**| The ID of the vulnerability to search for within all images stored in anchore-engine (e.g. CVE-1999-0001) | 
 **namespace** | **String**| Filter results to images within the given vulnerability namespace (e.g. debian:8, ubuntu:14.04) | [optional] 
 **affectedPackage** | **String**| Filter results to images with vulnable packages with the given package name (e.g. libssl) | [optional] 
 **severity** | **String**| Filter results to vulnerable package/vulnerability with the given severity | [optional] 
 **vendorOnly** | **Boolean**| Filter results to include only vulnerabilities that are not marked as invalid by upstream OS vendor data | [optional] [default to true]
 **page** | **Number**| The page of results to fetch. Pages start at 1 | [optional] 
 **limit** | **Number**| Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page | [optional] 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**PaginatedVulnerableImageList**](PaginatedVulnerableImageList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryVulnerabilities

> PaginatedVulnerabilityList queryVulnerabilities(id, opts)

Listing information about given vulnerability

List (w/filters) vulnerability records known by the system, with affected packages information if present

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.QueryApi();
let id = ["null"]; // [String] | The ID of the vulnerability (e.g. CVE-1999-0001)
let opts = {
  'affectedPackage': "affectedPackage_example", // String | Filter results by specified package name (e.g. sed)
  'affectedPackageVersion': "affectedPackageVersion_example", // String | Filter results by specified package version (e.g. 4.4-1)
  'page': "'1'", // String | The page of results to fetch. Pages start at 1
  'limit': 56, // Number | Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page
  'namespace': ["null"] // [String] | Namespace(s) to filter vulnerability records by
};
apiInstance.queryVulnerabilities(id, opts, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| The ID of the vulnerability (e.g. CVE-1999-0001) | 
 **affectedPackage** | **String**| Filter results by specified package name (e.g. sed) | [optional] 
 **affectedPackageVersion** | **String**| Filter results by specified package version (e.g. 4.4-1) | [optional] 
 **page** | **String**| The page of results to fetch. Pages start at 1 | [optional] [default to &#39;1&#39;]
 **limit** | **Number**| Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page | [optional] 
 **namespace** | [**[String]**](String.md)| Namespace(s) to filter vulnerability records by | [optional] 

### Return type

[**PaginatedVulnerabilityList**](PaginatedVulnerabilityList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

