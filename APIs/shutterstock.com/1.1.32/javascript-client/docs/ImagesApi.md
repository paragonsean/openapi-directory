# ShutterstockApiExplorer.ImagesApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addImageCollectionItems**](ImagesApi.md#addImageCollectionItems) | **POST** /v2/images/collections/{id}/items | Add images to collections
[**bulkSearchImages**](ImagesApi.md#bulkSearchImages) | **POST** /v2/bulk_search/images | Run multiple image searches
[**createImageCollection**](ImagesApi.md#createImageCollection) | **POST** /v2/images/collections | Create image collections
[**deleteImageCollection**](ImagesApi.md#deleteImageCollection) | **DELETE** /v2/images/collections/{id} | Delete image collections
[**deleteImageCollectionItems**](ImagesApi.md#deleteImageCollectionItems) | **DELETE** /v2/images/collections/{id}/items | Remove images from collections
[**downloadImage**](ImagesApi.md#downloadImage) | **POST** /v2/images/licenses/{id}/downloads | Download images
[**getFeaturedImageCollection**](ImagesApi.md#getFeaturedImageCollection) | **GET** /v2/images/collections/featured/{id} | Get the details of featured image collections
[**getFeaturedImageCollectionItems**](ImagesApi.md#getFeaturedImageCollectionItems) | **GET** /v2/images/collections/featured/{id}/items | Get the contents of featured image collections
[**getFeaturedImageCollectionList**](ImagesApi.md#getFeaturedImageCollectionList) | **GET** /v2/images/collections/featured | List featured image collections
[**getImage**](ImagesApi.md#getImage) | **GET** /v2/images/{id} | Get details about images
[**getImageCollection**](ImagesApi.md#getImageCollection) | **GET** /v2/images/collections/{id} | Get the details of image collections
[**getImageCollectionItems**](ImagesApi.md#getImageCollectionItems) | **GET** /v2/images/collections/{id}/items | Get the contents of image collections
[**getImageCollectionList**](ImagesApi.md#getImageCollectionList) | **GET** /v2/images/collections | List image collections
[**getImageKeywordSuggestions**](ImagesApi.md#getImageKeywordSuggestions) | **POST** /v2/images/search/suggestions | Get keywords from text
[**getImageLicenseList**](ImagesApi.md#getImageLicenseList) | **GET** /v2/images/licenses | List image licenses
[**getImageList**](ImagesApi.md#getImageList) | **GET** /v2/images | List images
[**getImageRecommendations**](ImagesApi.md#getImageRecommendations) | **GET** /v2/images/recommendations | List recommended images
[**getImageSuggestions**](ImagesApi.md#getImageSuggestions) | **GET** /v2/images/search/suggestions | Get suggestions for a search term
[**getUpdatedImages**](ImagesApi.md#getUpdatedImages) | **GET** /v2/images/updated | List updated images
[**licenseImages**](ImagesApi.md#licenseImages) | **POST** /v2/images/licenses | License images
[**listImageCategories**](ImagesApi.md#listImageCategories) | **GET** /v2/images/categories | List image categories
[**listSimilarImages**](ImagesApi.md#listSimilarImages) | **GET** /v2/images/{id}/similar | List similar images
[**renameImageCollection**](ImagesApi.md#renameImageCollection) | **POST** /v2/images/collections/{id} | Rename image collections
[**searchImages**](ImagesApi.md#searchImages) | **GET** /v2/images/search | Search for images



## addImageCollectionItems

> addImageCollectionItems(id, collectionItemRequest)

Add images to collections

This endpoint adds one or more images to a collection by image IDs.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let id = "126351027"; // String | Collection ID
let collectionItemRequest = {"items":[{"id":"49572945"}]}; // CollectionItemRequest | Array of image IDs to add to the collection
apiInstance.addImageCollectionItems(id, collectionItemRequest, (error, data, response) => {
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
 **id** | **String**| Collection ID | 
 **collectionItemRequest** | [**CollectionItemRequest**](CollectionItemRequest.md)| Array of image IDs to add to the collection | 

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## bulkSearchImages

> BulkImageSearchResults bulkSearchImages(searchImage, opts)

Run multiple image searches

This endpoint runs up to 5 image searches in a single request and returns up to 20 results per search. You can provide global search parameters in the query parameters and override them for each search in the body parameter. The query and body parameters are the same as in the &#x60;GET /v2/images/search&#x60; endpoint.

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

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let searchImage = {"$ref":"#/components/schemas/BulkImageSearchRequest/example"}; // [SearchImage] | List of queries to request results for and filters to apply per query; these values override the defaults in the query parameters
let opts = {
  'addedDate': new Date("2021-03-29"), // Date | Show images added on the specified date
  'addedDateStart': new Date("2021-03-29"), // Date | Show images added on or after the specified date
  'aspectRatioMin': 1.7778, // Number | Show images with the specified aspect ratio or higher, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image
  'aspectRatioMax': 1.7778, // Number | Show images with the specified aspect ratio or lower, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image
  'aspectRatio': 1.7778, // Number | Show images with the specified aspect ratio, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image
  'addedDateEnd': new Date("2021-03-29"), // Date | Show images added before the specified date
  'category': "category_example", // String | Show images with the specified Shutterstock-defined category; specify a category name or ID
  'color': "4F21EA", // String | Specify either a hexadecimal color in the format '4F21EA' or 'grayscale'; the API returns images that use similar colors
  'contributor': ["null"], // [String] | Show images with the specified contributor names or IDs, allows multiple
  'contributorCountry': new ShutterstockApiExplorer.BulkSearchImagesContributorCountryParameter(), // BulkSearchImagesContributorCountryParameter | Show images from contributors in one or more specified countries, or start with NOT to exclude a country from the search
  'fields': "fields_example", // String | Fields to display in the response; see the documentation for the fields parameter in the overview section
  'height': 56, // Number | (Deprecated; use height_from and height_to instead) Show images with the specified height
  'heightFrom': 1080, // Number | Show images with the specified height or larger, in pixels
  'heightTo': 1080, // Number | Show images with the specified height or smaller, in pixels
  'imageType': ["null"], // [String] | Show images of the specified type
  'keywordSafeSearch': true, // Boolean | Hide results with potentially unsafe keywords
  'language': new ShutterstockApiExplorer.Language(), // Language | Set query and result language (uses Accept-Language header if not set)
  'license': ["'commercial'"], // [String] | Show only images with the specified license
  'model': ["null"], // [String] | Show image results with the specified model IDs
  'orientation': "vertical", // String | Show image results with horizontal or vertical orientation
  'page': 1, // Number | Page number
  'perPage': 10, // Number | Number of results per page
  'peopleModelReleased': true, // Boolean | Show images of people with a signed model release
  'peopleAge': "20s", // String | Show images that feature people of the specified age category
  'peopleEthnicity': ["null"], // [String] | Show images with people of the specified ethnicities, or start with NOT to show images without those ethnicities
  'peopleGender': "both", // String | Show images with people of the specified gender
  'peopleNumber': 2, // Number | Show images with the specified number of people
  'region': new ShutterstockApiExplorer.BulkSearchImagesRegionParameter(), // BulkSearchImagesRegionParameter | Raise or lower search result rankings based on the result's relevance to a specified region; you can provide a country code or an IP address from which the API infers a country
  'safe': true, // Boolean | Enable or disable safe search
  'sort': "'popular'", // String | Sort by
  'spellcheckQuery': true, // Boolean | Spellcheck the search query and return results on suggested spellings
  'view': "'minimal'", // String | Amount of detail to render in the response
  'width': 56, // Number | (Deprecated; use width_from and width_to instead) Show images with the specified width
  'widthFrom': 1920, // Number | Show images with the specified width or larger, in pixels
  'widthTo': 1920 // Number | Show images with the specified width or smaller, in pixels
};
apiInstance.bulkSearchImages(searchImage, opts, (error, data, response) => {
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
 **searchImage** | [**[SearchImage]**](SearchImage.md)| List of queries to request results for and filters to apply per query; these values override the defaults in the query parameters | 
 **addedDate** | **Date**| Show images added on the specified date | [optional] 
 **addedDateStart** | **Date**| Show images added on or after the specified date | [optional] 
 **aspectRatioMin** | **Number**| Show images with the specified aspect ratio or higher, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image | [optional] 
 **aspectRatioMax** | **Number**| Show images with the specified aspect ratio or lower, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image | [optional] 
 **aspectRatio** | **Number**| Show images with the specified aspect ratio, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image | [optional] 
 **addedDateEnd** | **Date**| Show images added before the specified date | [optional] 
 **category** | **String**| Show images with the specified Shutterstock-defined category; specify a category name or ID | [optional] 
 **color** | **String**| Specify either a hexadecimal color in the format &#39;4F21EA&#39; or &#39;grayscale&#39;; the API returns images that use similar colors | [optional] 
 **contributor** | [**[String]**](String.md)| Show images with the specified contributor names or IDs, allows multiple | [optional] 
 **contributorCountry** | [**BulkSearchImagesContributorCountryParameter**](.md)| Show images from contributors in one or more specified countries, or start with NOT to exclude a country from the search | [optional] 
 **fields** | **String**| Fields to display in the response; see the documentation for the fields parameter in the overview section | [optional] 
 **height** | **Number**| (Deprecated; use height_from and height_to instead) Show images with the specified height | [optional] 
 **heightFrom** | **Number**| Show images with the specified height or larger, in pixels | [optional] 
 **heightTo** | **Number**| Show images with the specified height or smaller, in pixels | [optional] 
 **imageType** | [**[String]**](String.md)| Show images of the specified type | [optional] 
 **keywordSafeSearch** | **Boolean**| Hide results with potentially unsafe keywords | [optional] [default to true]
 **language** | [**Language**](.md)| Set query and result language (uses Accept-Language header if not set) | [optional] 
 **license** | [**[String]**](String.md)| Show only images with the specified license | [optional] 
 **model** | [**[String]**](String.md)| Show image results with the specified model IDs | [optional] 
 **orientation** | **String**| Show image results with horizontal or vertical orientation | [optional] 
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 20]
 **peopleModelReleased** | **Boolean**| Show images of people with a signed model release | [optional] 
 **peopleAge** | **String**| Show images that feature people of the specified age category | [optional] 
 **peopleEthnicity** | [**[String]**](String.md)| Show images with people of the specified ethnicities, or start with NOT to show images without those ethnicities | [optional] 
 **peopleGender** | **String**| Show images with people of the specified gender | [optional] 
 **peopleNumber** | **Number**| Show images with the specified number of people | [optional] 
 **region** | [**BulkSearchImagesRegionParameter**](.md)| Raise or lower search result rankings based on the result&#39;s relevance to a specified region; you can provide a country code or an IP address from which the API infers a country | [optional] 
 **safe** | **Boolean**| Enable or disable safe search | [optional] [default to true]
 **sort** | **String**| Sort by | [optional] [default to &#39;popular&#39;]
 **spellcheckQuery** | **Boolean**| Spellcheck the search query and return results on suggested spellings | [optional] [default to true]
 **view** | **String**| Amount of detail to render in the response | [optional] [default to &#39;minimal&#39;]
 **width** | **Number**| (Deprecated; use width_from and width_to instead) Show images with the specified width | [optional] 
 **widthFrom** | **Number**| Show images with the specified width or larger, in pixels | [optional] 
 **widthTo** | **Number**| Show images with the specified width or smaller, in pixels | [optional] 

### Return type

[**BulkImageSearchResults**](BulkImageSearchResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createImageCollection

> CollectionCreateResponse createImageCollection(collectionCreateRequest)

Create image collections

This endpoint creates one or more image collections (lightboxes). To add images to the collections, use &#x60;POST /v2/images/collections/{id}/items&#x60;.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let collectionCreateRequest = {"$ref":"#/components/schemas/CollectionCreateRequest/example"}; // CollectionCreateRequest | The names of the new collections
apiInstance.createImageCollection(collectionCreateRequest, (error, data, response) => {
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
 **collectionCreateRequest** | [**CollectionCreateRequest**](CollectionCreateRequest.md)| The names of the new collections | 

### Return type

[**CollectionCreateResponse**](CollectionCreateResponse.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteImageCollection

> deleteImageCollection(id)

Delete image collections

This endpoint deletes an image collection.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let id = "136351027"; // String | Collection ID
apiInstance.deleteImageCollection(id, (error, data, response) => {
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
 **id** | **String**| Collection ID | 

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteImageCollectionItems

> deleteImageCollectionItems(id, opts)

Remove images from collections

This endpoint removes one or more images from a collection.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let id = "126351027"; // String | Collection ID
let opts = {
  'itemId': ["null"] // [String] | One or more image IDs to remove from the collection
};
apiInstance.deleteImageCollectionItems(id, opts, (error, data, response) => {
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
 **id** | **String**| Collection ID | 
 **itemId** | [**[String]**](String.md)| One or more image IDs to remove from the collection | [optional] 

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## downloadImage

> Url downloadImage(id, redownloadImage)

Download images

This endpoint redownloads images that you have already received a license for. The download links in the response are valid for 8 hours.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let id = "e123"; // String | License ID
let redownloadImage = {"$ref":"#/components/schemas/RedownloadImage/example"}; // RedownloadImage | Information about the images to redownload
apiInstance.downloadImage(id, redownloadImage, (error, data, response) => {
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
 **id** | **String**| License ID | 
 **redownloadImage** | [**RedownloadImage**](RedownloadImage.md)| Information about the images to redownload | 

### Return type

[**Url**](Url.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getFeaturedImageCollection

> FeaturedCollection getFeaturedImageCollection(id, opts)

Get the details of featured image collections

This endpoint gets more detailed information about a featured collection, including its cover image and timestamps for its creation and most recent update. To get the images, use &#x60;GET /v2/images/collections/featured/{id}/items&#x60;.

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

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let id = "136351027"; // String | Collection ID
let opts = {
  'embed': "embed_example", // String | Which sharing information to include in the response, such as a URL to the collection
  'assetHint': "'1x'" // String | Cover image size
};
apiInstance.getFeaturedImageCollection(id, opts, (error, data, response) => {
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
 **id** | **String**| Collection ID | 
 **embed** | **String**| Which sharing information to include in the response, such as a URL to the collection | [optional] 
 **assetHint** | **String**| Cover image size | [optional] [default to &#39;1x&#39;]

### Return type

[**FeaturedCollection**](FeaturedCollection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFeaturedImageCollectionItems

> CollectionItemDataList getFeaturedImageCollectionItems(id, opts)

Get the contents of featured image collections

This endpoint lists the IDs of images in a featured collection and the date that each was added.

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

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let id = "136351027"; // String | Collection ID
let opts = {
  'page': 1, // Number | Page number
  'perPage': 100 // Number | Number of results per page
};
apiInstance.getFeaturedImageCollectionItems(id, opts, (error, data, response) => {
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
 **id** | **String**| Collection ID | 
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 100]

### Return type

[**CollectionItemDataList**](CollectionItemDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFeaturedImageCollectionList

> FeaturedCollectionDataList getFeaturedImageCollectionList(opts)

List featured image collections

This endpoint lists featured collections of specific types and a name and cover image for each collection.

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

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let opts = {
  'embed': "share_url", // String | Which sharing information to include in the response, such as a URL to the collection
  'type': ["null"], // [String] | The types of collections to return
  'assetHint': "1x" // String | Cover image size
};
apiInstance.getFeaturedImageCollectionList(opts, (error, data, response) => {
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
 **embed** | **String**| Which sharing information to include in the response, such as a URL to the collection | [optional] 
 **type** | [**[String]**](String.md)| The types of collections to return | [optional] 
 **assetHint** | **String**| Cover image size | [optional] [default to &#39;1x&#39;]

### Return type

[**FeaturedCollectionDataList**](FeaturedCollectionDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImage

> Image getImage(id, opts)

Get details about images

This endpoint shows information about an image, including a URL to a preview image and the sizes that it is available in.

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

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let id = "465011609"; // String | Image ID
let opts = {
  'language': new ShutterstockApiExplorer.Language(), // Language | Language for the keywords and categories in the response
  'view': "'full'", // String | Amount of detail to render in the response
  'searchId': "00000000-0000-0000-0000-000000000000" // String | The ID of the search that is related to this request
};
apiInstance.getImage(id, opts, (error, data, response) => {
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
 **id** | **String**| Image ID | 
 **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] 
 **view** | **String**| Amount of detail to render in the response | [optional] [default to &#39;full&#39;]
 **searchId** | **String**| The ID of the search that is related to this request | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageCollection

> Collection getImageCollection(id, opts)

Get the details of image collections

This endpoint gets more detailed information about a collection, including its cover image and timestamps for its creation and most recent update. To get the images in collections, use &#x60;GET /v2/images/collections/{id}/items&#x60;.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let id = "126351027"; // String | Collection ID
let opts = {
  'embed': ["null"], // [String] | Which sharing information to include in the response, such as a URL to the collection
  'shareCode': "shareCode_example" // String | Code to retrieve a shared collection
};
apiInstance.getImageCollection(id, opts, (error, data, response) => {
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
 **id** | **String**| Collection ID | 
 **embed** | [**[String]**](String.md)| Which sharing information to include in the response, such as a URL to the collection | [optional] 
 **shareCode** | **String**| Code to retrieve a shared collection | [optional] 

### Return type

[**Collection**](Collection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageCollectionItems

> CollectionItemDataList getImageCollectionItems(id, opts)

Get the contents of image collections

This endpoint lists the IDs of images in a collection and the date that each was added.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let id = "126351027"; // String | Collection ID
let opts = {
  'page': 1, // Number | Page number
  'perPage': 100, // Number | Number of results per page
  'shareCode': "shareCode_example", // String | Code to retrieve the contents of a shared collection
  'sort': "'oldest'" // String | Sort order
};
apiInstance.getImageCollectionItems(id, opts, (error, data, response) => {
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
 **id** | **String**| Collection ID | 
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 100]
 **shareCode** | **String**| Code to retrieve the contents of a shared collection | [optional] 
 **sort** | **String**| Sort order | [optional] [default to &#39;oldest&#39;]

### Return type

[**CollectionItemDataList**](CollectionItemDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageCollectionList

> CollectionDataList getImageCollectionList(opts)

List image collections

This endpoint lists your collections of images and their basic attributes.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let opts = {
  'embed': ["null"], // [String] | Which sharing information to include in the response, such as a URL to the collection
  'page': 1, // Number | Page number
  'perPage': 2 // Number | Number of results per page
};
apiInstance.getImageCollectionList(opts, (error, data, response) => {
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
 **embed** | [**[String]**](String.md)| Which sharing information to include in the response, such as a URL to the collection | [optional] 
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 100]

### Return type

[**CollectionDataList**](CollectionDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageKeywordSuggestions

> SearchEntitiesResponse getImageKeywordSuggestions(searchEntitiesRequest)

Get keywords from text

This endpoint returns up to 10 important keywords from a block of plain text.

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

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let searchEntitiesRequest = {"$ref":"#/components/schemas/SearchEntitiesRequest/example"}; // SearchEntitiesRequest | Plain text to extract keywords from
apiInstance.getImageKeywordSuggestions(searchEntitiesRequest, (error, data, response) => {
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
 **searchEntitiesRequest** | [**SearchEntitiesRequest**](SearchEntitiesRequest.md)| Plain text to extract keywords from | 

### Return type

[**SearchEntitiesResponse**](SearchEntitiesResponse.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getImageLicenseList

> DownloadHistoryDataList getImageLicenseList(opts)

List image licenses

This endpoint lists existing licenses.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let opts = {
  'imageId': "12345678", // String | Show licenses for the specified image ID
  'license': "standard", // String | Show images that are available with the specified license, such as `standard` or `enhanced`; prepending a `-` sign excludes results from that license
  'page': 1, // Number | Page number
  'perPage': 20, // Number | Number of results per page
  'sort': "'newest'", // String | Sort order
  'username': "aUniqueUsername", // String | Filter licenses by username of licensee
  'startDate': new Date("2021-03-29T13:25:13.521Z"), // Date | Show licenses created on or after the specified date
  'endDate': new Date("2021-03-29T13:25:13.521Z"), // Date | Show licenses created before the specified date
  'downloadAvailability': "'all'", // String | Filter licenses by download availability
  'teamHistory': false // Boolean | Set to true to see license history for all members of your team.
};
apiInstance.getImageLicenseList(opts, (error, data, response) => {
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
 **imageId** | **String**| Show licenses for the specified image ID | [optional] 
 **license** | **String**| Show images that are available with the specified license, such as &#x60;standard&#x60; or &#x60;enhanced&#x60;; prepending a &#x60;-&#x60; sign excludes results from that license | [optional] 
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


## getImageList

> ImageDataList getImageList(id, opts)

List images

This endpoint lists information about one or more images, including the available sizes.

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

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let id = ["null"]; // [String] | One or more image IDs
let opts = {
  'view': "minimal", // String | Amount of detail to render in the response
  'searchId': "00000000-0000-0000-0000-000000000000" // String | The ID of the search that is related to this request
};
apiInstance.getImageList(id, opts, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| One or more image IDs | 
 **view** | **String**| Amount of detail to render in the response | [optional] [default to &#39;minimal&#39;]
 **searchId** | **String**| The ID of the search that is related to this request | [optional] 

### Return type

[**ImageDataList**](ImageDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageRecommendations

> RecommendationDataList getImageRecommendations(id, opts)

List recommended images

This endpoint returns images that customers put in the same collection as the specified image IDs.

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

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let id = ["null"]; // [String] | Image IDs
let opts = {
  'maxItems': 20, // Number | Maximum number of results returned in the response
  'safe': true // Boolean | Restrict results to safe images
};
apiInstance.getImageRecommendations(id, opts, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| Image IDs | 
 **maxItems** | **Number**| Maximum number of results returned in the response | [optional] [default to 20]
 **safe** | **Boolean**| Restrict results to safe images | [optional] [default to true]

### Return type

[**RecommendationDataList**](RecommendationDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImageSuggestions

> Suggestions getImageSuggestions(query, opts)

Get suggestions for a search term

This endpoint provides autocomplete suggestions for partial search terms.

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

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let query = "cats"; // String | Search term for which you want keyword suggestions
let opts = {
  'limit': 10 // Number | Limit the number of suggestions
};
apiInstance.getImageSuggestions(query, opts, (error, data, response) => {
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
 **query** | **String**| Search term for which you want keyword suggestions | 
 **limit** | **Number**| Limit the number of suggestions | [optional] [default to 10]

### Return type

[**Suggestions**](Suggestions.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUpdatedImages

> UpdatedMediaDataList getUpdatedImages(opts)

List updated images

This endpoint lists images that have been updated in the specified time period to update content management systems (CMS) or digital asset management (DAM) systems. In most cases, use the &#x60;interval&#x60; parameter to show images that were updated recently, but you can also use the &#x60;start_date&#x60; and &#x60;end_date&#x60; parameters to specify a range of no more than three days. Do not use the &#x60;interval&#x60; parameter with either &#x60;start_date&#x60; or &#x60;end_date&#x60;.

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

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let opts = {
  'type': ["null"], // [String] | Show images that were added, deleted, or edited; by default, the endpoint returns images that were updated in any of these ways
  'startDate': new Date("2021-03-29"), // Date | Show images updated on or after the specified date
  'endDate': new Date("2021-03-29"), // Date | Show images updated before the specified date
  'interval': "'1 HOUR'", // String | Show images updated in the specified time period, where the time period is an interval (like SQL INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows images that were updated in the hour preceding the request
  'page': 1, // Number | Page number
  'perPage': 100, // Number | Number of results per page
  'sort': "'newest'" // String | Sort order
};
apiInstance.getUpdatedImages(opts, (error, data, response) => {
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
 **type** | [**[String]**](String.md)| Show images that were added, deleted, or edited; by default, the endpoint returns images that were updated in any of these ways | [optional] 
 **startDate** | **Date**| Show images updated on or after the specified date | [optional] 
 **endDate** | **Date**| Show images updated before the specified date | [optional] 
 **interval** | **String**| Show images updated in the specified time period, where the time period is an interval (like SQL INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default is 1 HOUR, which shows images that were updated in the hour preceding the request | [optional] [default to &#39;1 HOUR&#39;]
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 100]
 **sort** | **String**| Sort order | [optional] [default to &#39;newest&#39;]

### Return type

[**UpdatedMediaDataList**](UpdatedMediaDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## licenseImages

> LicenseImageResultDataList licenseImages(licenseImageRequest, opts)

License images

This endpoint gets licenses for one or more images. You must specify the image IDs in the body parameter and other details like the format, size, and subscription ID either in the query parameter or with each image ID in the body parameter. Values in the body parameter override values in the query parameters. The download links in the response are valid for 8 hours.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let licenseImageRequest = {"$ref":"#/components/schemas/LicenseImageRequest/example"}; // LicenseImageRequest | List of images to request licenses for and information about each license transaction; these values override the defaults in the query parameters
let opts = {
  'subscriptionId': "subscriptionId_example", // String | Subscription ID to use to license the image
  'format': "format_example", // String | (Deprecated) Image format
  'size': "'huge'", // String | Image size
  'searchId': "searchId_example" // String | Search ID that was provided in the results of an image search
};
apiInstance.licenseImages(licenseImageRequest, opts, (error, data, response) => {
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
 **licenseImageRequest** | [**LicenseImageRequest**](LicenseImageRequest.md)| List of images to request licenses for and information about each license transaction; these values override the defaults in the query parameters | 
 **subscriptionId** | **String**| Subscription ID to use to license the image | [optional] 
 **format** | **String**| (Deprecated) Image format | [optional] 
 **size** | **String**| Image size | [optional] [default to &#39;huge&#39;]
 **searchId** | **String**| Search ID that was provided in the results of an image search | [optional] 

### Return type

[**LicenseImageResultDataList**](LicenseImageResultDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listImageCategories

> CategoryDataList listImageCategories(opts)

List image categories

This endpoint lists the categories (Shutterstock-assigned genres) that images can belong to.

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

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let opts = {
  'language': new ShutterstockApiExplorer.Language() // Language | Language for the keywords and categories in the response
};
apiInstance.listImageCategories(opts, (error, data, response) => {
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
 **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] 

### Return type

[**CategoryDataList**](CategoryDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSimilarImages

> ImageSearchResults listSimilarImages(id, opts)

List similar images

This endpoint returns images that are visually similar to an image that you specify.

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

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let id = "465011609"; // String | Image ID
let opts = {
  'language': new ShutterstockApiExplorer.Language(), // Language | Language for the keywords and categories in the response
  'page': 1, // Number | Page number
  'perPage': 20, // Number | Number of results per page
  'view': "'minimal'" // String | Amount of detail to render in the response
};
apiInstance.listSimilarImages(id, opts, (error, data, response) => {
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
 **id** | **String**| Image ID | 
 **language** | [**Language**](.md)| Language for the keywords and categories in the response | [optional] 
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 20]
 **view** | **String**| Amount of detail to render in the response | [optional] [default to &#39;minimal&#39;]

### Return type

[**ImageSearchResults**](ImageSearchResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## renameImageCollection

> renameImageCollection(id, collectionUpdateRequest)

Rename image collections

This endpoint sets a new name for an image collection.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let id = "126351027"; // String | Collection ID
let collectionUpdateRequest = {"$ref":"#/components/schemas/CollectionUpdateRequest/example"}; // CollectionUpdateRequest | The new name for the collection
apiInstance.renameImageCollection(id, collectionUpdateRequest, (error, data, response) => {
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
 **id** | **String**| Collection ID | 
 **collectionUpdateRequest** | [**CollectionUpdateRequest**](CollectionUpdateRequest.md)| The new name for the collection | 

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## searchImages

> ImageSearchResults searchImages(opts)

Search for images

This endpoint searches for images. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in the &#x60;query&#x60; parameter by prefixing the term with NOT. Free API accounts show results only from a limited library of media, not the full Shutterstock media library. Also, the number of search fields they can use in a request is limited.

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

let apiInstance = new ShutterstockApiExplorer.ImagesApi();
let opts = {
  'addedDate': new Date("2021-03-29"), // Date | Show images added on the specified date
  'addedDateStart': new Date("2021-03-29"), // Date | Show images added on or after the specified date
  'aspectRatioMin': 1.7778, // Number | Show images with the specified aspect ratio or higher, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image
  'aspectRatioMax': 1.7778, // Number | Show images with the specified aspect ratio or lower, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image
  'aspectRatio': 1.7778, // Number | Show images with the specified aspect ratio, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image
  'aiSearch': true, // Boolean | Set to true and specify the `ai_objective` and `ai_industry` parameters to use AI-powered search; the API returns information about how well images meet the objective for the industry 
  'aiLabelsLimit': 20, // Number | For AI-powered search, specify the maximum number of labels to return
  'aiIndustry': "aiIndustry_example", // String | For AI-powered search, specify the industry to target; requires that the `ai_search` parameter is set to true
  'aiObjective': "aiObjective_example", // String | For AI-powered search, specify the goal of the media; requires that the `ai_search` parameter is set to true
  'addedDateEnd': new Date("2021-03-29"), // Date | Show images added before the specified date
  'category': "category_example", // String | Show images with the specified Shutterstock-defined category; specify a category name or ID
  'color': "4F21EA", // String | Specify either a hexadecimal color in the format '4F21EA' or 'grayscale'; the API returns images that use similar colors
  'contributor': ["null"], // [String] | Show images with the specified contributor names or IDs, allows multiple
  'contributorCountry': new ShutterstockApiExplorer.BulkSearchImagesContributorCountryParameter(), // BulkSearchImagesContributorCountryParameter | Show images from contributors in one or more specified countries, or start with NOT to exclude a country from the search
  'fields': "fields_example", // String | Fields to display in the response; see the documentation for the fields parameter in the overview section
  'height': 56, // Number | (Deprecated; use height_from and height_to instead) Show images with the specified height
  'heightFrom': 1080, // Number | Show images with the specified height or larger, in pixels
  'heightTo': 1080, // Number | Show images with the specified height or smaller, in pixels
  'imageType': ["null"], // [String] | Show images of the specified type
  'keywordSafeSearch': true, // Boolean | Hide results with potentially unsafe keywords
  'language': new ShutterstockApiExplorer.Language(), // Language | Set query and result language (uses Accept-Language header if not set)
  'license': ["'commercial'"], // [String] | Show only images with the specified license
  'model': ["null"], // [String] | Show image results with the specified model IDs
  'orientation': "vertical", // String | Show image results with horizontal or vertical orientation
  'page': 1, // Number | Page number
  'perPage': 50, // Number | Number of results per page
  'peopleModelReleased': true, // Boolean | Show images of people with a signed model release
  'peopleAge': "20s", // String | Show images that feature people of the specified age category
  'peopleEthnicity': ["null"], // [String] | Show images with people of the specified ethnicities, or start with NOT to show images without those ethnicities
  'peopleGender': "both", // String | Show images with people of the specified gender
  'peopleNumber': 2, // Number | Show images with the specified number of people
  'query': "dogs on the beach", // String | One or more search terms separated by spaces; you can use NOT to filter out images that match a term
  'region': new ShutterstockApiExplorer.BulkSearchImagesRegionParameter(), // BulkSearchImagesRegionParameter | Raise or lower search result rankings based on the result's relevance to a specified region; you can provide a country code or an IP address from which the API infers a country
  'safe': true, // Boolean | Enable or disable safe search
  'sort': "'popular'", // String | Sort by
  'spellcheckQuery': true, // Boolean | Spellcheck the search query and return results on suggested spellings
  'view': "'minimal'", // String | Amount of detail to render in the response
  'width': 56, // Number | (Deprecated; use width_from and width_to instead) Show images with the specified width
  'widthFrom': 1920, // Number | Show images with the specified width or larger, in pixels
  'widthTo': 1920 // Number | Show images with the specified width or smaller, in pixels
};
apiInstance.searchImages(opts, (error, data, response) => {
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
 **addedDate** | **Date**| Show images added on the specified date | [optional] 
 **addedDateStart** | **Date**| Show images added on or after the specified date | [optional] 
 **aspectRatioMin** | **Number**| Show images with the specified aspect ratio or higher, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image | [optional] 
 **aspectRatioMax** | **Number**| Show images with the specified aspect ratio or lower, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image | [optional] 
 **aspectRatio** | **Number**| Show images with the specified aspect ratio, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image | [optional] 
 **aiSearch** | **Boolean**| Set to true and specify the &#x60;ai_objective&#x60; and &#x60;ai_industry&#x60; parameters to use AI-powered search; the API returns information about how well images meet the objective for the industry  | [optional] 
 **aiLabelsLimit** | **Number**| For AI-powered search, specify the maximum number of labels to return | [optional] [default to 20]
 **aiIndustry** | **String**| For AI-powered search, specify the industry to target; requires that the &#x60;ai_search&#x60; parameter is set to true | [optional] 
 **aiObjective** | **String**| For AI-powered search, specify the goal of the media; requires that the &#x60;ai_search&#x60; parameter is set to true | [optional] 
 **addedDateEnd** | **Date**| Show images added before the specified date | [optional] 
 **category** | **String**| Show images with the specified Shutterstock-defined category; specify a category name or ID | [optional] 
 **color** | **String**| Specify either a hexadecimal color in the format &#39;4F21EA&#39; or &#39;grayscale&#39;; the API returns images that use similar colors | [optional] 
 **contributor** | [**[String]**](String.md)| Show images with the specified contributor names or IDs, allows multiple | [optional] 
 **contributorCountry** | [**BulkSearchImagesContributorCountryParameter**](.md)| Show images from contributors in one or more specified countries, or start with NOT to exclude a country from the search | [optional] 
 **fields** | **String**| Fields to display in the response; see the documentation for the fields parameter in the overview section | [optional] 
 **height** | **Number**| (Deprecated; use height_from and height_to instead) Show images with the specified height | [optional] 
 **heightFrom** | **Number**| Show images with the specified height or larger, in pixels | [optional] 
 **heightTo** | **Number**| Show images with the specified height or smaller, in pixels | [optional] 
 **imageType** | [**[String]**](String.md)| Show images of the specified type | [optional] 
 **keywordSafeSearch** | **Boolean**| Hide results with potentially unsafe keywords | [optional] [default to true]
 **language** | [**Language**](.md)| Set query and result language (uses Accept-Language header if not set) | [optional] 
 **license** | [**[String]**](String.md)| Show only images with the specified license | [optional] 
 **model** | [**[String]**](String.md)| Show image results with the specified model IDs | [optional] 
 **orientation** | **String**| Show image results with horizontal or vertical orientation | [optional] 
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 20]
 **peopleModelReleased** | **Boolean**| Show images of people with a signed model release | [optional] 
 **peopleAge** | **String**| Show images that feature people of the specified age category | [optional] 
 **peopleEthnicity** | [**[String]**](String.md)| Show images with people of the specified ethnicities, or start with NOT to show images without those ethnicities | [optional] 
 **peopleGender** | **String**| Show images with people of the specified gender | [optional] 
 **peopleNumber** | **Number**| Show images with the specified number of people | [optional] 
 **query** | **String**| One or more search terms separated by spaces; you can use NOT to filter out images that match a term | [optional] 
 **region** | [**BulkSearchImagesRegionParameter**](.md)| Raise or lower search result rankings based on the result&#39;s relevance to a specified region; you can provide a country code or an IP address from which the API infers a country | [optional] 
 **safe** | **Boolean**| Enable or disable safe search | [optional] [default to true]
 **sort** | **String**| Sort by | [optional] [default to &#39;popular&#39;]
 **spellcheckQuery** | **Boolean**| Spellcheck the search query and return results on suggested spellings | [optional] [default to true]
 **view** | **String**| Amount of detail to render in the response | [optional] [default to &#39;minimal&#39;]
 **width** | **Number**| (Deprecated; use width_from and width_to instead) Show images with the specified width | [optional] 
 **widthFrom** | **Number**| Show images with the specified width or larger, in pixels | [optional] 
 **widthTo** | **Number**| Show images with the specified width or smaller, in pixels | [optional] 

### Return type

[**ImageSearchResults**](ImageSearchResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

