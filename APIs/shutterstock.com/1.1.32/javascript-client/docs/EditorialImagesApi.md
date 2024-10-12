# ShutterstockApiExplorer.EditorialImagesApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEditorialCategories**](EditorialImagesApi.md#getEditorialCategories) | **GET** /v2/editorial/categories | (Deprecated) List editorial categories
[**getEditorialImage**](EditorialImagesApi.md#getEditorialImage) | **GET** /v2/editorial/images/{id} | Get editorial content details
[**getEditorialImageLicenseList**](EditorialImagesApi.md#getEditorialImageLicenseList) | **GET** /v2/editorial/images/licenses | List editorial image licenses
[**getEditorialImageLivefeed**](EditorialImagesApi.md#getEditorialImageLivefeed) | **GET** /v2/editorial/images/livefeeds/{id} | Get editorial livefeed
[**getEditorialImageLivefeedItems**](EditorialImagesApi.md#getEditorialImageLivefeedItems) | **GET** /v2/editorial/images/livefeeds/{id}/items | Get editorial livefeed items
[**getEditorialImageLivefeedList**](EditorialImagesApi.md#getEditorialImageLivefeedList) | **GET** /v2/editorial/images/livefeeds | Get editorial livefeed list
[**getEditorialLivefeed**](EditorialImagesApi.md#getEditorialLivefeed) | **GET** /v2/editorial/livefeeds/{id} | (Deprecated) Get editorial livefeed
[**getEditorialLivefeedItems**](EditorialImagesApi.md#getEditorialLivefeedItems) | **GET** /v2/editorial/livefeeds/{id}/items | (Deprecated) Get editorial livefeed items
[**getEditorialLivefeedList**](EditorialImagesApi.md#getEditorialLivefeedList) | **GET** /v2/editorial/livefeeds | (Deprecated) Get editorial livefeed list
[**getUpdatedEditorialImage**](EditorialImagesApi.md#getUpdatedEditorialImage) | **GET** /v2/editorial/updated | (Deprecated) List updated content
[**getUpdatedEditorialImages**](EditorialImagesApi.md#getUpdatedEditorialImages) | **GET** /v2/editorial/images/updated | List updated content
[**licenseEditorialImage**](EditorialImagesApi.md#licenseEditorialImage) | **POST** /v2/editorial/licenses | (Deprecated) License editorial content
[**licenseEditorialImages**](EditorialImagesApi.md#licenseEditorialImages) | **POST** /v2/editorial/images/licenses | License editorial content
[**listEditorialImageCategories**](EditorialImagesApi.md#listEditorialImageCategories) | **GET** /v2/editorial/images/categories | List editorial categories
[**searchEditorial**](EditorialImagesApi.md#searchEditorial) | **GET** /v2/editorial/search | (Deprecated) Search editorial content
[**searchEditorialImages**](EditorialImagesApi.md#searchEditorialImages) | **GET** /v2/editorial/images/search | Search editorial images
[**v2EditorialIdGet**](EditorialImagesApi.md#v2EditorialIdGet) | **GET** /v2/editorial/{id} | (Deprecated) Get editorial content details



## getEditorialCategories

> EditorialCategoryResults getEditorialCategories()

(Deprecated) List editorial categories

Deprecated; use &#x60;GET /v2/editorial/images/categories&#x60; instead. This endpoint lists the categories that editorial images can belong to, which are separate from the categories that other types of assets can belong to.

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

let apiInstance = new ShutterstockApiExplorer.EditorialImagesApi();
apiInstance.getEditorialCategories((error, data, response) => {
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

[**EditorialCategoryResults**](EditorialCategoryResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEditorialImage

> EditorialContent getEditorialImage(id, country)

Get editorial content details

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

let apiInstance = new ShutterstockApiExplorer.EditorialImagesApi();
let id = "9926131a"; // String | Editorial ID
let country = "USA"; // String | Returns only if the content is available for distribution in a certain country
apiInstance.getEditorialImage(id, country, (error, data, response) => {
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

### Return type

[**EditorialContent**](EditorialContent.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEditorialImageLicenseList

> DownloadHistoryDataList getEditorialImageLicenseList(opts)

List editorial image licenses

This endpoint lists existing editorial image licenses.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.EditorialImagesApi();
let opts = {
  'imageId': "12345678", // String | Show licenses for the specified editorial image ID
  'license': "premier_editorial_all_digital", // String | Show editorial images that are available with the specified license name
  'page': 1, // Number | Page number
  'perPage': 20, // Number | Number of results per page
  'sort': "'newest'", // String | Sort order
  'username': "aUniqueUsername", // String | Filter licenses by username of licensee
  'startDate': new Date("2021-03-29T13:25:13.521Z"), // Date | Show licenses created on or after the specified date
  'endDate': new Date("2021-03-29T13:25:13.521Z"), // Date | Show licenses created before the specified date
  'downloadAvailability': "'all'", // String | Filter licenses by download availability
  'teamHistory': false // Boolean | Set to true to see license history for all members of your team.
};
apiInstance.getEditorialImageLicenseList(opts, (error, data, response) => {
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
 **imageId** | **String**| Show licenses for the specified editorial image ID | [optional] 
 **license** | **String**| Show editorial images that are available with the specified license name | [optional] 
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


## getEditorialImageLivefeed

> EditorialImageLivefeed getEditorialImageLivefeed(id, country)

Get editorial livefeed

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

let apiInstance = new ShutterstockApiExplorer.EditorialImagesApi();
let id = "2018%2F10%2F15%2FWomen%20of%20the%20Year%20Lunch%20%26%20Awards%2C%20London"; // String | Editorial livefeed ID; must be an URI encoded string
let country = "USA"; // String | Returns only if the livefeed is available for distribution in a certain country
apiInstance.getEditorialImageLivefeed(id, country, (error, data, response) => {
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
 **id** | **String**| Editorial livefeed ID; must be an URI encoded string | 
 **country** | **String**| Returns only if the livefeed is available for distribution in a certain country | 

### Return type

[**EditorialImageLivefeed**](EditorialImageLivefeed.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEditorialImageLivefeedItems

> EditorialImageContentDataList getEditorialImageLivefeedItems(id, country)

Get editorial livefeed items

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

let apiInstance = new ShutterstockApiExplorer.EditorialImagesApi();
let id = "2018%2F10%2F15%2FWomen%20of%20the%20Year%20Lunch%20%26%20Awards%2C%20London"; // String | Editorial livefeed ID; must be an URI encoded string
let country = "USA"; // String | Returns only if the livefeed items are available for distribution in a certain country
apiInstance.getEditorialImageLivefeedItems(id, country, (error, data, response) => {
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
 **id** | **String**| Editorial livefeed ID; must be an URI encoded string | 
 **country** | **String**| Returns only if the livefeed items are available for distribution in a certain country | 

### Return type

[**EditorialImageContentDataList**](EditorialImageContentDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEditorialImageLivefeedList

> EditorialImageLivefeedList getEditorialImageLivefeedList(country, opts)

Get editorial livefeed list

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

let apiInstance = new ShutterstockApiExplorer.EditorialImagesApi();
let country = "USA"; // String | Returns only livefeeds that are available for distribution in a certain country
let opts = {
  'page': 1, // Number | Page number
  'perPage': 20 // Number | Number of results per page
};
apiInstance.getEditorialImageLivefeedList(country, opts, (error, data, response) => {
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
 **country** | **String**| Returns only livefeeds that are available for distribution in a certain country | 
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 20]

### Return type

[**EditorialImageLivefeedList**](EditorialImageLivefeedList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEditorialLivefeed

> EditorialLivefeed getEditorialLivefeed(id, country)

(Deprecated) Get editorial livefeed

Deprecated: use &#x60;GET /v2/editorial/images/livefeeds/{id}&#x60; instead to get an editorial livefeed.

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

let apiInstance = new ShutterstockApiExplorer.EditorialImagesApi();
let id = "2018%2F10%2F15%2FWomen%20of%20the%20Year%20Lunch%20%26%20Awards%2C%20London"; // String | Editorial livefeed ID; must be an URI encoded string
let country = "USA"; // String | Returns only if the livefeed is available for distribution in a certain country
apiInstance.getEditorialLivefeed(id, country, (error, data, response) => {
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
 **id** | **String**| Editorial livefeed ID; must be an URI encoded string | 
 **country** | **String**| Returns only if the livefeed is available for distribution in a certain country | 

### Return type

[**EditorialLivefeed**](EditorialLivefeed.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEditorialLivefeedItems

> EditorialContentDataList getEditorialLivefeedItems(id, country)

(Deprecated) Get editorial livefeed items

Deprecated; use &#x60;GET /v2/editorial/images/livefeeds/{id}/items&#x60; instead to get editorial livefeed items.

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

let apiInstance = new ShutterstockApiExplorer.EditorialImagesApi();
let id = "2018%2F10%2F15%2FWomen%20of%20the%20Year%20Lunch%20%26%20Awards%2C%20London"; // String | Editorial livefeed ID; must be an URI encoded string
let country = "USA"; // String | Returns only if the livefeed items are available for distribution in a certain country
apiInstance.getEditorialLivefeedItems(id, country, (error, data, response) => {
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
 **id** | **String**| Editorial livefeed ID; must be an URI encoded string | 
 **country** | **String**| Returns only if the livefeed items are available for distribution in a certain country | 

### Return type

[**EditorialContentDataList**](EditorialContentDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEditorialLivefeedList

> EditorialLivefeedList getEditorialLivefeedList(country, opts)

(Deprecated) Get editorial livefeed list

Deprecated; use &#x60;GET /v2/editorial/images/livefeeds&#x60; instead to get a list of editorial livefeeds.

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

let apiInstance = new ShutterstockApiExplorer.EditorialImagesApi();
let country = "USA"; // String | Returns only livefeeds that are available for distribution in a certain country
let opts = {
  'page': 1, // Number | Page number
  'perPage': 20 // Number | Number of results per page
};
apiInstance.getEditorialLivefeedList(country, opts, (error, data, response) => {
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
 **country** | **String**| Returns only livefeeds that are available for distribution in a certain country | 
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 20]

### Return type

[**EditorialLivefeedList**](EditorialLivefeedList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUpdatedEditorialImage

> EditorialUpdatedResults getUpdatedEditorialImage(type, dateUpdatedStart, dateUpdatedEnd, country, opts)

(Deprecated) List updated content

Deprecated; use &#x60;GET /v2/editorial/images/updated&#x60; instead to get recently updated items.

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

let apiInstance = new ShutterstockApiExplorer.EditorialImagesApi();
let type = "edit"; // String | Specify `addition` to return only images that were added or `edit` to return only images that were edited or deleted
let dateUpdatedStart = new Date("2021-03-29T13:25:13.521Z"); // Date | Show images images added, edited, or deleted after the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
let dateUpdatedEnd = new Date("2021-03-29T13:25:13.521Z"); // Date | Show images images added, edited, or deleted before the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
let country = "USA"; // String | Show only editorial content that is available for distribution in a certain country
let opts = {
  'dateTakenStart': new Date("2020-02-04"), // Date | Show images that were taken on or after the specified date; use this parameter if you want recently created images from the collection instead of updated older assets
  'dateTakenEnd': new Date("2020-02-05"), // Date | Show images that were taken before the specified date
  'cursor': "eyJ2IjoxLCJzIjoyfQ==", // String | The cursor of the page with which to start fetching results; this cursor is returned from previous requests
  'sort': "newest", // String | Sort by
  'supplierCode': ["null"], // [String] | Show only editorial content from certain suppliers
  'perPage': 200 // Number | Number of results per page
};
apiInstance.getUpdatedEditorialImage(type, dateUpdatedStart, dateUpdatedEnd, country, opts, (error, data, response) => {
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
 **type** | **String**| Specify &#x60;addition&#x60; to return only images that were added or &#x60;edit&#x60; to return only images that were edited or deleted | 
 **dateUpdatedStart** | **Date**| Show images images added, edited, or deleted after the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00. | 
 **dateUpdatedEnd** | **Date**| Show images images added, edited, or deleted before the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00. | 
 **country** | **String**| Show only editorial content that is available for distribution in a certain country | 
 **dateTakenStart** | **Date**| Show images that were taken on or after the specified date; use this parameter if you want recently created images from the collection instead of updated older assets | [optional] 
 **dateTakenEnd** | **Date**| Show images that were taken before the specified date | [optional] 
 **cursor** | **String**| The cursor of the page with which to start fetching results; this cursor is returned from previous requests | [optional] 
 **sort** | **String**| Sort by | [optional] [default to &#39;newest&#39;]
 **supplierCode** | [**[String]**](String.md)| Show only editorial content from certain suppliers | [optional] 
 **perPage** | **Number**| Number of results per page | [optional] [default to 500]

### Return type

[**EditorialUpdatedResults**](EditorialUpdatedResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUpdatedEditorialImages

> EditorialUpdatedResults getUpdatedEditorialImages(type, dateUpdatedStart, dateUpdatedEnd, country, opts)

List updated content

This endpoint lists editorial images that have been updated in the specified time period to update content management systems (CMS) or digital asset management (DAM) systems. In most cases, use the date_updated_start and date_updated_end parameters to specify a range updates based on when the updates happened. You can also use the date_taken_start and date_taken_end parameters to specify a range of updates based on when the image was taken.

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

let apiInstance = new ShutterstockApiExplorer.EditorialImagesApi();
let type = "edit"; // String | Specify `addition` to return only images that were added or `edit` to return only images that were edited or deleted
let dateUpdatedStart = new Date("2021-03-29T13:25:13.521Z"); // Date | Show images images added, edited, or deleted after the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
let dateUpdatedEnd = new Date("2021-03-29T13:25:13.521Z"); // Date | Show images images added, edited, or deleted before the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00.
let country = "USA"; // String | Show only editorial content that is available for distribution in a certain country
let opts = {
  'dateTakenStart': new Date("2020-02-04"), // Date | Show images that were taken on or after the specified date; use this parameter if you want recently created images from the collection instead of updated older assets
  'dateTakenEnd': new Date("2020-02-05"), // Date | Show images that were taken before the specified date
  'cursor': "eyJ2IjoxLCJzIjoyfQ==", // String | The cursor of the page with which to start fetching results; this cursor is returned from previous requests
  'sort': "newest", // String | Sort by
  'supplierCode': ["null"], // [String] | Show only editorial content from certain suppliers
  'perPage': 200 // Number | Number of results per page
};
apiInstance.getUpdatedEditorialImages(type, dateUpdatedStart, dateUpdatedEnd, country, opts, (error, data, response) => {
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
 **type** | **String**| Specify &#x60;addition&#x60; to return only images that were added or &#x60;edit&#x60; to return only images that were edited or deleted | 
 **dateUpdatedStart** | **Date**| Show images images added, edited, or deleted after the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00. | 
 **dateUpdatedEnd** | **Date**| Show images images added, edited, or deleted before the specified date. Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00. | 
 **country** | **String**| Show only editorial content that is available for distribution in a certain country | 
 **dateTakenStart** | **Date**| Show images that were taken on or after the specified date; use this parameter if you want recently created images from the collection instead of updated older assets | [optional] 
 **dateTakenEnd** | **Date**| Show images that were taken before the specified date | [optional] 
 **cursor** | **String**| The cursor of the page with which to start fetching results; this cursor is returned from previous requests | [optional] 
 **sort** | **String**| Sort by | [optional] [default to &#39;newest&#39;]
 **supplierCode** | [**[String]**](String.md)| Show only editorial content from certain suppliers | [optional] 
 **perPage** | **Number**| Number of results per page | [optional] [default to 500]

### Return type

[**EditorialUpdatedResults**](EditorialUpdatedResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## licenseEditorialImage

> LicenseEditorialContentResults licenseEditorialImage(licenseEditorialContentRequest)

(Deprecated) License editorial content

Deprecated; use &#x60;POST /v2/editorial/images/licenses&#x60; instead to get licenses for one or more editorial images. You must specify the country and one or more editorial images to license. The download links in the response are valid for 8 hours.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.EditorialImagesApi();
let licenseEditorialContentRequest = {"$ref":"#/components/schemas/LicenseEditorialContentRequest/example"}; // LicenseEditorialContentRequest | License editorial content
apiInstance.licenseEditorialImage(licenseEditorialContentRequest, (error, data, response) => {
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
 **licenseEditorialContentRequest** | [**LicenseEditorialContentRequest**](LicenseEditorialContentRequest.md)| License editorial content | 

### Return type

[**LicenseEditorialContentResults**](LicenseEditorialContentResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## licenseEditorialImages

> LicenseEditorialContentResults licenseEditorialImages(licenseEditorialContentRequest)

License editorial content

This endpoint gets licenses for one or more editorial images. You must specify the country and one or more editorial images to license. The download links in the response are valid for 8 hours.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.EditorialImagesApi();
let licenseEditorialContentRequest = {"$ref":"#/components/schemas/LicenseEditorialContentRequest/example"}; // LicenseEditorialContentRequest | License editorial content
apiInstance.licenseEditorialImages(licenseEditorialContentRequest, (error, data, response) => {
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
 **licenseEditorialContentRequest** | [**LicenseEditorialContentRequest**](LicenseEditorialContentRequest.md)| License editorial content | 

### Return type

[**LicenseEditorialContentResults**](LicenseEditorialContentResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listEditorialImageCategories

> EditorialImageCategoryResults listEditorialImageCategories()

List editorial categories

This endpoint lists the categories that editorial images can belong to, which are separate from the categories that other types of assets can belong to.

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

let apiInstance = new ShutterstockApiExplorer.EditorialImagesApi();
apiInstance.listEditorialImageCategories((error, data, response) => {
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

[**EditorialImageCategoryResults**](EditorialImageCategoryResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchEditorial

> EditorialSearchResults searchEditorial(country, opts)

(Deprecated) Search editorial content

Deprecated; use &#x60;GET /v2/editorial/images/search&#x60; instead to search for editorial images.

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

let apiInstance = new ShutterstockApiExplorer.EditorialImagesApi();
let country = "USA"; // String | Show only editorial content that is available for distribution in a certain country
let opts = {
  'query': "query_example", // String | One or more search terms separated by spaces
  'sort': "'relevant'", // String | Sort by
  'category': "category_example", // String | Show editorial content within a certain editorial category; specify by category name
  'supplierCode': ["null"], // [String] | Show only editorial content from certain suppliers
  'dateStart': new Date("2013-10-20"), // Date | Show only editorial content generated on or after a specific date
  'dateEnd': new Date("2013-10-20"), // Date | Show only editorial content generated on or before a specific date
  'perPage': 20, // Number | Number of results per page
  'cursor': "cursor_example" // String | The cursor of the page with which to start fetching results; this cursor is returned from previous requests
};
apiInstance.searchEditorial(country, opts, (error, data, response) => {
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
 **country** | **String**| Show only editorial content that is available for distribution in a certain country | 
 **query** | **String**| One or more search terms separated by spaces | [optional] 
 **sort** | **String**| Sort by | [optional] [default to &#39;relevant&#39;]
 **category** | **String**| Show editorial content within a certain editorial category; specify by category name | [optional] 
 **supplierCode** | [**[String]**](String.md)| Show only editorial content from certain suppliers | [optional] 
 **dateStart** | **Date**| Show only editorial content generated on or after a specific date | [optional] 
 **dateEnd** | **Date**| Show only editorial content generated on or before a specific date | [optional] 
 **perPage** | **Number**| Number of results per page | [optional] [default to 20]
 **cursor** | **String**| The cursor of the page with which to start fetching results; this cursor is returned from previous requests | [optional] 

### Return type

[**EditorialSearchResults**](EditorialSearchResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchEditorialImages

> EditorialSearchResults searchEditorialImages(country, opts)

Search editorial images

This endpoint searches for editorial images. If you specify more than one search parameter, the API uses an AND condition. For example, if you set the &#x60;category&#x60; parameter to \&quot;Alone,Performing\&quot; and also specify a &#x60;query&#x60; parameter, the results include only images that match the query and are in both the Alone and Performing categories. You can also filter search terms out in the &#x60;query&#x60; parameter by prefixing the term with NOT.

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

let apiInstance = new ShutterstockApiExplorer.EditorialImagesApi();
let country = "USA"; // String | Show only editorial content that is available for distribution in a certain country
let opts = {
  'query': "The Academy Awards", // String | One or more search terms separated by spaces
  'sort': "'relevant'", // String | Sort by
  'category': "Alone,Performing", // String | Show editorial content with each of the specified editorial categories; specify category names in a comma-separated list
  'supplierCode': ["null"], // [String] | Show only editorial content from certain suppliers
  'dateStart': new Date("2020-05-29"), // Date | Show only editorial content generated on or after a specific date
  'dateEnd': new Date("2021-05-29"), // Date | Show only editorial content generated on or before a specific date
  'perPage': 20, // Number | Number of results per page
  'cursor': "eyJ2IjoxLCJzIjoxfQ==" // String | The cursor of the page with which to start fetching results; this cursor is returned from previous requests
};
apiInstance.searchEditorialImages(country, opts, (error, data, response) => {
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
 **country** | **String**| Show only editorial content that is available for distribution in a certain country | 
 **query** | **String**| One or more search terms separated by spaces | [optional] 
 **sort** | **String**| Sort by | [optional] [default to &#39;relevant&#39;]
 **category** | **String**| Show editorial content with each of the specified editorial categories; specify category names in a comma-separated list | [optional] 
 **supplierCode** | [**[String]**](String.md)| Show only editorial content from certain suppliers | [optional] 
 **dateStart** | **Date**| Show only editorial content generated on or after a specific date | [optional] 
 **dateEnd** | **Date**| Show only editorial content generated on or before a specific date | [optional] 
 **perPage** | **Number**| Number of results per page | [optional] [default to 20]
 **cursor** | **String**| The cursor of the page with which to start fetching results; this cursor is returned from previous requests | [optional] 

### Return type

[**EditorialSearchResults**](EditorialSearchResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v2EditorialIdGet

> EditorialContent v2EditorialIdGet(id, country, opts)

(Deprecated) Get editorial content details

Deprecated; use &#x60;GET /v2/editorial/images/{id}&#x60; instead to show information about an editorial image, including a URL to a preview image and the sizes that it is available in.

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

let apiInstance = new ShutterstockApiExplorer.EditorialImagesApi();
let id = "9926131a"; // String | Editorial ID
let country = "USA"; // String | Returns only if the content is available for distribution in a certain country
let opts = {
  'searchId': "00000000-0000-0000-0000-000000000000" // String | The ID of the search that is related to this request
};
apiInstance.v2EditorialIdGet(id, country, opts, (error, data, response) => {
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

[**EditorialContent**](EditorialContent.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

