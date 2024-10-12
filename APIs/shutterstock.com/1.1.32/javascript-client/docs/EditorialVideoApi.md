# ShutterstockApiExplorer.EditorialVideoApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEditorialVideo**](EditorialVideoApi.md#getEditorialVideo) | **GET** /v2/editorial/videos/{id} | Get editorial video content details
[**getEditorialVideoLicenseList**](EditorialVideoApi.md#getEditorialVideoLicenseList) | **GET** /v2/editorial/videos/licenses | List editorial video licenses
[**licenseEditorialVideo**](EditorialVideoApi.md#licenseEditorialVideo) | **POST** /v2/editorial/videos/licenses | License editorial video content
[**listEditorialVideoCategories**](EditorialVideoApi.md#listEditorialVideoCategories) | **GET** /v2/editorial/videos/categories | List editorial video categories
[**searchEditorialVideos**](EditorialVideoApi.md#searchEditorialVideos) | **GET** /v2/editorial/videos/search | Search editorial video content



## getEditorialVideo

> EditorialVideoContent getEditorialVideo(id, country, opts)

Get editorial video content details

This endpoint shows information about an editorial image, including a URL to a preview image and the sizes that it is available in.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new ShutterstockApiExplorer.EditorialVideoApi();
let id = "9926131a"; // String | Editorial ID
let country = "USA"; // String | Returns only if the content is available for distribution in a certain country
let opts = {
  'searchId': "00000000-0000-0000-0000-000000000000" // String | The ID of the search that is related to this request
};
apiInstance.getEditorialVideo(id, country, opts, (error, data, response) => {
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
 **id** | **String**| Editorial ID | 
 **country** | **String**| Returns only if the content is available for distribution in a certain country | 
 **searchId** | **String**| The ID of the search that is related to this request | [optional] 

### Return type

[**EditorialVideoContent**](EditorialVideoContent.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEditorialVideoLicenseList

> DownloadHistoryDataList getEditorialVideoLicenseList(opts)

List editorial video licenses

This endpoint lists existing editorial video licenses.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.EditorialVideoApi();
let opts = {
  'videoId': "12345678", // String | Show licenses for the specified editorial video ID
  'license': "premier_editorial_all_media", // String | Show editorial videos that are available with the specified license name
  'page': 1, // Number | Page number
  'perPage': 20, // Number | Number of results per page
  'sort': "'newest'", // String | Sort order
  'username': "aUniqueUsername", // String | Filter licenses by username of licensee
  'startDate': new Date("2021-03-29T13:25:13.521Z"), // Date | Show licenses created on or after the specified date
  'endDate': new Date("2021-03-29T13:25:13.521Z"), // Date | Show licenses created before the specified date
  'downloadAvailability': "'all'", // String | Filter licenses by download availability
  'teamHistory': false // Boolean | Set to true to see license history for all members of your team.
};
apiInstance.getEditorialVideoLicenseList(opts, (error, data, response) => {
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
 **videoId** | **String**| Show licenses for the specified editorial video ID | [optional] 
 **license** | **String**| Show editorial videos that are available with the specified license name | [optional] 
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 20]
 **sort** | **String**| Sort order | [optional] [default to &#39;newest&#39;]
 **username** | **String**| Filter licenses by username of licensee | [optional] 
 **startDate** | **Date**| Show licenses created on or after the specified date | [optional] 
 **endDate** | **Date**| Show licenses created before the specified date | [optional] 
 **downloadAvailability** | **String**| Filter licenses by download availability | [optional] [default to &#39;all&#39;]
 **teamHistory** | **Boolean**| Set to true to see license history for all members of your team. | [optional] [default to false]

### Return type

[**DownloadHistoryDataList**](DownloadHistoryDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## licenseEditorialVideo

> LicenseEditorialContentResults licenseEditorialVideo(licenseEditorialVideoContentRequest)

License editorial video content

This endpoint gets licenses for one or more editorial videos. You must specify the country and one or more editorial videos to license. The download links in the response are valid for 8 hours.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.EditorialVideoApi();
let licenseEditorialVideoContentRequest = {"$ref":"#/components/schemas/LicenseEditorialVideoContentRequest/example"}; // LicenseEditorialVideoContentRequest | License editorial video content
apiInstance.licenseEditorialVideo(licenseEditorialVideoContentRequest, (error, data, response) => {
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
 **licenseEditorialVideoContentRequest** | [**LicenseEditorialVideoContentRequest**](LicenseEditorialVideoContentRequest.md)| License editorial video content | 

### Return type

[**LicenseEditorialContentResults**](LicenseEditorialContentResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listEditorialVideoCategories

> EditorialVideoCategoryResults listEditorialVideoCategories()

List editorial video categories

This endpoint lists the categories that editorial videos can belong to, which are separate from the categories that other types of assets can belong to.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new ShutterstockApiExplorer.EditorialVideoApi();
apiInstance.listEditorialVideoCategories((error, data, response) => {
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

[**EditorialVideoCategoryResults**](EditorialVideoCategoryResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchEditorialVideos

> EditorialVideoSearchResults searchEditorialVideos(country, opts)

Search editorial video content

This endpoint searches for editorial videos. If you specify more than one search parameter, the API uses an AND condition. For example, if you set the &#x60;category&#x60; parameter to \&quot;Alone,Performing\&quot; and also specify a &#x60;query&#x60; parameter, the results include only videos that match the query and are in both the Alone and Performing categories.  You can also filter search terms out in the &#x60;query&#x60; parameter by prefixing the term with NOT.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new ShutterstockApiExplorer.EditorialVideoApi();
let country = "USA"; // String | Show only editorial video content that is available for distribution in a certain country
let opts = {
  'query': "The Academy Awards", // String | One or more search terms separated by spaces
  'sort': "'relevant'", // String | Sort by
  'category': "Alone,Performing", // String | Show editorial content with each of the specified editorial categories; specify category names in a comma-separated list
  'supplierCode': ["null"], // [String] | Show only editorial video content from certain suppliers
  'dateStart': new Date("2020-05-29"), // Date | Show only editorial video content generated on or after a specific date
  'dateEnd': new Date("2021-05-29"), // Date | Show only editorial video content generated on or before a specific date
  'resolution': "4k", // String | Show only editorial video content with specific resolution
  'fps': 24, // Number | Show only editorial video content generated with specific frames per second
  'perPage': 20, // Number | Number of results per page
  'cursor': "eyJ2IjoxLCJzIjoxfQ==" // String | The cursor of the page with which to start fetching results; this cursor is returned from previous requests
};
apiInstance.searchEditorialVideos(country, opts, (error, data, response) => {
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
 **country** | **String**| Show only editorial video content that is available for distribution in a certain country | 
 **query** | **String**| One or more search terms separated by spaces | [optional] 
 **sort** | **String**| Sort by | [optional] [default to &#39;relevant&#39;]
 **category** | **String**| Show editorial content with each of the specified editorial categories; specify category names in a comma-separated list | [optional] 
 **supplierCode** | [**[String]**](String.md)| Show only editorial video content from certain suppliers | [optional] 
 **dateStart** | **Date**| Show only editorial video content generated on or after a specific date | [optional] 
 **dateEnd** | **Date**| Show only editorial video content generated on or before a specific date | [optional] 
 **resolution** | **String**| Show only editorial video content with specific resolution | [optional] 
 **fps** | **Number**| Show only editorial video content generated with specific frames per second | [optional] 
 **perPage** | **Number**| Number of results per page | [optional] [default to 20]
 **cursor** | **String**| The cursor of the page with which to start fetching results; this cursor is returned from previous requests | [optional] 

### Return type

[**EditorialVideoSearchResults**](EditorialVideoSearchResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

