# FigshareApi.CollectionsApi

All URIs are relative to *https://api.figshare.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collectionArticles**](CollectionsApi.md#collectionArticles) | **GET** /collections/{collection_id}/articles | Public Collection Articles
[**collectionDetails**](CollectionsApi.md#collectionDetails) | **GET** /collections/{collection_id} | Collection details
[**collectionVersionDetails**](CollectionsApi.md#collectionVersionDetails) | **GET** /collections/{collection_id}/versions/{version_id} | Collection Version details
[**collectionVersions**](CollectionsApi.md#collectionVersions) | **GET** /collections/{collection_id}/versions | Collection Versions list
[**collectionsList**](CollectionsApi.md#collectionsList) | **GET** /collections | Public Collections
[**collectionsSearch**](CollectionsApi.md#collectionsSearch) | **POST** /collections/search | Public Collections Search
[**privateCollectionArticleDelete**](CollectionsApi.md#privateCollectionArticleDelete) | **DELETE** /account/collections/{collection_id}/articles/{article_id} | Delete collection article
[**privateCollectionArticlesAdd**](CollectionsApi.md#privateCollectionArticlesAdd) | **POST** /account/collections/{collection_id}/articles | Add collection articles
[**privateCollectionArticlesList**](CollectionsApi.md#privateCollectionArticlesList) | **GET** /account/collections/{collection_id}/articles | List collection articles
[**privateCollectionArticlesReplace**](CollectionsApi.md#privateCollectionArticlesReplace) | **PUT** /account/collections/{collection_id}/articles | Replace collection articles
[**privateCollectionAuthorDelete**](CollectionsApi.md#privateCollectionAuthorDelete) | **DELETE** /account/collections/{collection_id}/authors/{author_id} | Delete collection author
[**privateCollectionAuthorsAdd**](CollectionsApi.md#privateCollectionAuthorsAdd) | **POST** /account/collections/{collection_id}/authors | Add collection authors
[**privateCollectionAuthorsList**](CollectionsApi.md#privateCollectionAuthorsList) | **GET** /account/collections/{collection_id}/authors | List collection authors
[**privateCollectionAuthorsReplace**](CollectionsApi.md#privateCollectionAuthorsReplace) | **PUT** /account/collections/{collection_id}/authors | Replace collection authors
[**privateCollectionCategoriesAdd**](CollectionsApi.md#privateCollectionCategoriesAdd) | **POST** /account/collections/{collection_id}/categories | Add collection categories
[**privateCollectionCategoriesList**](CollectionsApi.md#privateCollectionCategoriesList) | **GET** /account/collections/{collection_id}/categories | List collection categories
[**privateCollectionCategoriesReplace**](CollectionsApi.md#privateCollectionCategoriesReplace) | **PUT** /account/collections/{collection_id}/categories | Replace collection categories
[**privateCollectionCategoryDelete**](CollectionsApi.md#privateCollectionCategoryDelete) | **DELETE** /account/collections/{collection_id}/categories/{category_id} | Delete collection category
[**privateCollectionCreate**](CollectionsApi.md#privateCollectionCreate) | **POST** /account/collections | Create collection
[**privateCollectionDelete**](CollectionsApi.md#privateCollectionDelete) | **DELETE** /account/collections/{collection_id} | Delete collection
[**privateCollectionDetails**](CollectionsApi.md#privateCollectionDetails) | **GET** /account/collections/{collection_id} | Collection details
[**privateCollectionPrivateLinkCreate**](CollectionsApi.md#privateCollectionPrivateLinkCreate) | **POST** /account/collections/{collection_id}/private_links | Create collection private link
[**privateCollectionPrivateLinkDelete**](CollectionsApi.md#privateCollectionPrivateLinkDelete) | **DELETE** /account/collections/{collection_id}/private_links/{link_id} | Disable private link
[**privateCollectionPrivateLinkUpdate**](CollectionsApi.md#privateCollectionPrivateLinkUpdate) | **PUT** /account/collections/{collection_id}/private_links/{link_id} | Update collection private link
[**privateCollectionPrivateLinksList**](CollectionsApi.md#privateCollectionPrivateLinksList) | **GET** /account/collections/{collection_id}/private_links | List collection private links
[**privateCollectionPublish**](CollectionsApi.md#privateCollectionPublish) | **POST** /account/collections/{collection_id}/publish | Private Collection Publish
[**privateCollectionReserveDoi**](CollectionsApi.md#privateCollectionReserveDoi) | **POST** /account/collections/{collection_id}/reserve_doi | Private Collection Reserve DOI
[**privateCollectionReserveHandle**](CollectionsApi.md#privateCollectionReserveHandle) | **POST** /account/collections/{collection_id}/reserve_handle | Private Collection Reserve Handle
[**privateCollectionResource**](CollectionsApi.md#privateCollectionResource) | **POST** /account/collections/{collection_id}/resource | Private Collection Resource
[**privateCollectionUpdate**](CollectionsApi.md#privateCollectionUpdate) | **PUT** /account/collections/{collection_id} | Update collection
[**privateCollectionsList**](CollectionsApi.md#privateCollectionsList) | **GET** /account/collections | Private Collections List
[**privateCollectionsSearch**](CollectionsApi.md#privateCollectionsSearch) | **POST** /account/collections/search | Private Collections Search



## collectionArticles

> [Article] collectionArticles(collectionId, opts)

Public Collection Articles

Returns a list of public collection articles

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection Unique identifier
let opts = {
  'page': 789, // Number | Page number. Used for pagination with page_size
  'pageSize': 10, // Number | The number of results included on a page. Used for pagination with page
  'limit': 789, // Number | Number of results included on a page. Used for pagination with query
  'offset': 789 // Number | Where to start the listing(the offset of the first result). Used for pagination with limit
};
apiInstance.collectionArticles(collectionId, opts, (error, data, response) => {
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
 **collectionId** | **Number**| Collection Unique identifier | 
 **page** | **Number**| Page number. Used for pagination with page_size | [optional] 
 **pageSize** | **Number**| The number of results included on a page. Used for pagination with page | [optional] [default to 10]
 **limit** | **Number**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **Number**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 

### Return type

[**[Article]**](Article.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionDetails

> CollectionComplete collectionDetails(collectionId)

Collection details

View a collection

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection Unique identifier
apiInstance.collectionDetails(collectionId, (error, data, response) => {
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
 **collectionId** | **Number**| Collection Unique identifier | 

### Return type

[**CollectionComplete**](CollectionComplete.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionVersionDetails

> CollectionComplete collectionVersionDetails(collectionId, versionId)

Collection Version details

View details for a certain version of a collection

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection Unique identifier
let versionId = 789; // Number | Version Number
apiInstance.collectionVersionDetails(collectionId, versionId, (error, data, response) => {
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
 **collectionId** | **Number**| Collection Unique identifier | 
 **versionId** | **Number**| Version Number | 

### Return type

[**CollectionComplete**](CollectionComplete.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionVersions

> [CollectionVersions] collectionVersions(collectionId)

Collection Versions list

Returns a list of public collection Versions

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection Unique identifier
apiInstance.collectionVersions(collectionId, (error, data, response) => {
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
 **collectionId** | **Number**| Collection Unique identifier | 

### Return type

[**[CollectionVersions]**](CollectionVersions.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionsList

> [Collection] collectionsList(opts)

Public Collections

Returns a list of public collections

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.CollectionsApi();
let opts = {
  'xCursor': "xCursor_example", // String | Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected.
  'page': 789, // Number | Page number. Used for pagination with page_size
  'pageSize': 10, // Number | The number of results included on a page. Used for pagination with page
  'limit': 789, // Number | Number of results included on a page. Used for pagination with query
  'offset': 789, // Number | Where to start the listing(the offset of the first result). Used for pagination with limit
  'order': "'published_date'", // String | The field by which to order. Default varies by endpoint/resource.
  'orderDirection': "'desc'", // String | 
  'institution': 789, // Number | only return collections from this institution
  'publishedSince': "publishedSince_example", // String | Filter by collection publishing date. Will only return collections published after the date. date(ISO 8601) YYYY-MM-DD
  'modifiedSince': "modifiedSince_example", // String | Filter by collection modified date. Will only return collections published after the date. date(ISO 8601) YYYY-MM-DD
  'group': 789, // Number | only return collections from this group
  'resourceDoi': "resourceDoi_example", // String | only return collections with this resource_doi
  'doi': "doi_example", // String | only return collections with this doi
  'handle': "handle_example" // String | only return collections with this handle
};
apiInstance.collectionsList(opts, (error, data, response) => {
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
 **xCursor** | **String**| Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected. | [optional] 
 **page** | **Number**| Page number. Used for pagination with page_size | [optional] 
 **pageSize** | **Number**| The number of results included on a page. Used for pagination with page | [optional] [default to 10]
 **limit** | **Number**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **Number**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 
 **order** | **String**| The field by which to order. Default varies by endpoint/resource. | [optional] [default to &#39;published_date&#39;]
 **orderDirection** | **String**|  | [optional] [default to &#39;desc&#39;]
 **institution** | **Number**| only return collections from this institution | [optional] 
 **publishedSince** | **String**| Filter by collection publishing date. Will only return collections published after the date. date(ISO 8601) YYYY-MM-DD | [optional] 
 **modifiedSince** | **String**| Filter by collection modified date. Will only return collections published after the date. date(ISO 8601) YYYY-MM-DD | [optional] 
 **group** | **Number**| only return collections from this group | [optional] 
 **resourceDoi** | **String**| only return collections with this resource_doi | [optional] 
 **doi** | **String**| only return collections with this doi | [optional] 
 **handle** | **String**| only return collections with this handle | [optional] 

### Return type

[**[Collection]**](Collection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionsSearch

> [Collection] collectionsSearch(opts)

Public Collections Search

Returns a list of public collections

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.CollectionsApi();
let opts = {
  'xCursor': "xCursor_example", // String | Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected.
  'collectionSearch': new FigshareApi.CollectionSearch() // CollectionSearch | Search Parameters
};
apiInstance.collectionsSearch(opts, (error, data, response) => {
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
 **xCursor** | **String**| Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected. | [optional] 
 **collectionSearch** | [**CollectionSearch**](CollectionSearch.md)| Search Parameters | [optional] 

### Return type

[**[Collection]**](Collection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateCollectionArticleDelete

> privateCollectionArticleDelete(collectionId, articleId)

Delete collection article

De-associate article from collection

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection unique identifier
let articleId = 789; // Number | Collection article unique identifier
apiInstance.privateCollectionArticleDelete(collectionId, articleId, (error, data, response) => {
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
 **collectionId** | **Number**| Collection unique identifier | 
 **articleId** | **Number**| Collection article unique identifier | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateCollectionArticlesAdd

> Location privateCollectionArticlesAdd(collectionId, articlesCreator)

Add collection articles

Associate new articles with the collection. This will add new articles to the list of already associated articles

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection unique identifier
let articlesCreator = new FigshareApi.ArticlesCreator(); // ArticlesCreator | Articles list
apiInstance.privateCollectionArticlesAdd(collectionId, articlesCreator, (error, data, response) => {
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
 **collectionId** | **Number**| Collection unique identifier | 
 **articlesCreator** | [**ArticlesCreator**](ArticlesCreator.md)| Articles list | 

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateCollectionArticlesList

> [Article] privateCollectionArticlesList(collectionId, opts)

List collection articles

List collection articles

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection unique identifier
let opts = {
  'page': 789, // Number | Page number. Used for pagination with page_size
  'pageSize': 10, // Number | The number of results included on a page. Used for pagination with page
  'limit': 789, // Number | Number of results included on a page. Used for pagination with query
  'offset': 789 // Number | Where to start the listing(the offset of the first result). Used for pagination with limit
};
apiInstance.privateCollectionArticlesList(collectionId, opts, (error, data, response) => {
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
 **collectionId** | **Number**| Collection unique identifier | 
 **page** | **Number**| Page number. Used for pagination with page_size | [optional] 
 **pageSize** | **Number**| The number of results included on a page. Used for pagination with page | [optional] [default to 10]
 **limit** | **Number**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **Number**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 

### Return type

[**[Article]**](Article.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateCollectionArticlesReplace

> privateCollectionArticlesReplace(collectionId, articlesCreator)

Replace collection articles

Associate new articles with the collection. This will remove all already associated articles and add these new ones

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection unique identifier
let articlesCreator = new FigshareApi.ArticlesCreator(); // ArticlesCreator | Articles List
apiInstance.privateCollectionArticlesReplace(collectionId, articlesCreator, (error, data, response) => {
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
 **collectionId** | **Number**| Collection unique identifier | 
 **articlesCreator** | [**ArticlesCreator**](ArticlesCreator.md)| Articles List | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateCollectionAuthorDelete

> privateCollectionAuthorDelete(collectionId, authorId)

Delete collection author

Delete collection author

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection unique identifier
let authorId = 789; // Number | Collection Author unique identifier
apiInstance.privateCollectionAuthorDelete(collectionId, authorId, (error, data, response) => {
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
 **collectionId** | **Number**| Collection unique identifier | 
 **authorId** | **Number**| Collection Author unique identifier | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateCollectionAuthorsAdd

> Location privateCollectionAuthorsAdd(collectionId, authorsCreator)

Add collection authors

Associate new authors with the collection. This will add new authors to the list of already associated authors

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection unique identifier
let authorsCreator = new FigshareApi.AuthorsCreator(); // AuthorsCreator | List of authors
apiInstance.privateCollectionAuthorsAdd(collectionId, authorsCreator, (error, data, response) => {
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
 **collectionId** | **Number**| Collection unique identifier | 
 **authorsCreator** | [**AuthorsCreator**](AuthorsCreator.md)| List of authors | 

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateCollectionAuthorsList

> [Author] privateCollectionAuthorsList(collectionId)

List collection authors

List collection authors

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection unique identifier
apiInstance.privateCollectionAuthorsList(collectionId, (error, data, response) => {
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
 **collectionId** | **Number**| Collection unique identifier | 

### Return type

[**[Author]**](Author.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateCollectionAuthorsReplace

> privateCollectionAuthorsReplace(collectionId, authorsCreator)

Replace collection authors

Associate new authors with the collection. This will remove all already associated authors and add these new ones

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection unique identifier
let authorsCreator = new FigshareApi.AuthorsCreator(); // AuthorsCreator | List of authors
apiInstance.privateCollectionAuthorsReplace(collectionId, authorsCreator, (error, data, response) => {
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
 **collectionId** | **Number**| Collection unique identifier | 
 **authorsCreator** | [**AuthorsCreator**](AuthorsCreator.md)| List of authors | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateCollectionCategoriesAdd

> Location privateCollectionCategoriesAdd(collectionId, categoriesCreator)

Add collection categories

Associate new categories with the collection. This will add new categories to the list of already associated categories

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection unique identifier
let categoriesCreator = new FigshareApi.CategoriesCreator(); // CategoriesCreator | Categories list
apiInstance.privateCollectionCategoriesAdd(collectionId, categoriesCreator, (error, data, response) => {
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
 **collectionId** | **Number**| Collection unique identifier | 
 **categoriesCreator** | [**CategoriesCreator**](CategoriesCreator.md)| Categories list | 

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateCollectionCategoriesList

> [Category] privateCollectionCategoriesList(collectionId)

List collection categories

List collection categories

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection unique identifier
apiInstance.privateCollectionCategoriesList(collectionId, (error, data, response) => {
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
 **collectionId** | **Number**| Collection unique identifier | 

### Return type

[**[Category]**](Category.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateCollectionCategoriesReplace

> privateCollectionCategoriesReplace(collectionId, categoriesCreator)

Replace collection categories

Associate new categories with the collection. This will remove all already associated categories and add these new ones

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection unique identifier
let categoriesCreator = new FigshareApi.CategoriesCreator(); // CategoriesCreator | Categories list
apiInstance.privateCollectionCategoriesReplace(collectionId, categoriesCreator, (error, data, response) => {
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
 **collectionId** | **Number**| Collection unique identifier | 
 **categoriesCreator** | [**CategoriesCreator**](CategoriesCreator.md)| Categories list | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateCollectionCategoryDelete

> privateCollectionCategoryDelete(collectionId, categoryId)

Delete collection category

De-associate category from collection

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection unique identifier
let categoryId = 789; // Number | Collection category unique identifier
apiInstance.privateCollectionCategoryDelete(collectionId, categoryId, (error, data, response) => {
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
 **collectionId** | **Number**| Collection unique identifier | 
 **categoryId** | **Number**| Collection category unique identifier | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateCollectionCreate

> LocationWarnings privateCollectionCreate(collectionCreate)

Create collection

Create a new Collection by sending collection information

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionCreate = new FigshareApi.CollectionCreate(); // CollectionCreate | Collection description
apiInstance.privateCollectionCreate(collectionCreate, (error, data, response) => {
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
 **collectionCreate** | [**CollectionCreate**](CollectionCreate.md)| Collection description | 

### Return type

[**LocationWarnings**](LocationWarnings.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateCollectionDelete

> privateCollectionDelete(collectionId)

Delete collection

Delete n collection

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection Unique identifier
apiInstance.privateCollectionDelete(collectionId, (error, data, response) => {
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
 **collectionId** | **Number**| Collection Unique identifier | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateCollectionDetails

> CollectionCompletePrivate privateCollectionDetails(collectionId)

Collection details

View a collection

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection Unique identifier
apiInstance.privateCollectionDetails(collectionId, (error, data, response) => {
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
 **collectionId** | **Number**| Collection Unique identifier | 

### Return type

[**CollectionCompletePrivate**](CollectionCompletePrivate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateCollectionPrivateLinkCreate

> PrivateLinkResponse privateCollectionPrivateLinkCreate(collectionId, opts)

Create collection private link

Create new private link

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection unique identifier
let opts = {
  'collectionPrivateLinkCreator': new FigshareApi.CollectionPrivateLinkCreator() // CollectionPrivateLinkCreator | 
};
apiInstance.privateCollectionPrivateLinkCreate(collectionId, opts, (error, data, response) => {
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
 **collectionId** | **Number**| Collection unique identifier | 
 **collectionPrivateLinkCreator** | [**CollectionPrivateLinkCreator**](CollectionPrivateLinkCreator.md)|  | [optional] 

### Return type

[**PrivateLinkResponse**](PrivateLinkResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateCollectionPrivateLinkDelete

> privateCollectionPrivateLinkDelete(collectionId, linkId)

Disable private link

Disable/delete private link for this collection

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection unique identifier
let linkId = "linkId_example"; // String | Private link token
apiInstance.privateCollectionPrivateLinkDelete(collectionId, linkId, (error, data, response) => {
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
 **collectionId** | **Number**| Collection unique identifier | 
 **linkId** | **String**| Private link token | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateCollectionPrivateLinkUpdate

> privateCollectionPrivateLinkUpdate(collectionId, linkId, opts)

Update collection private link

Update existing private link for this collection

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection unique identifier
let linkId = "linkId_example"; // String | Private link token
let opts = {
  'collectionPrivateLinkCreator': new FigshareApi.CollectionPrivateLinkCreator() // CollectionPrivateLinkCreator | 
};
apiInstance.privateCollectionPrivateLinkUpdate(collectionId, linkId, opts, (error, data, response) => {
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
 **collectionId** | **Number**| Collection unique identifier | 
 **linkId** | **String**| Private link token | 
 **collectionPrivateLinkCreator** | [**CollectionPrivateLinkCreator**](CollectionPrivateLinkCreator.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateCollectionPrivateLinksList

> [PrivateLink] privateCollectionPrivateLinksList(collectionId)

List collection private links

List article private links

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection unique identifier
apiInstance.privateCollectionPrivateLinksList(collectionId, (error, data, response) => {
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
 **collectionId** | **Number**| Collection unique identifier | 

### Return type

[**[PrivateLink]**](PrivateLink.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateCollectionPublish

> Location privateCollectionPublish(collectionId)

Private Collection Publish

When a collection is published, a new public version will be generated. Any further updates to the collection will affect the private collection data. In order to make these changes publicly visible, an explicit publish operation is needed.

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection Unique identifier
apiInstance.privateCollectionPublish(collectionId, (error, data, response) => {
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
 **collectionId** | **Number**| Collection Unique identifier | 

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateCollectionReserveDoi

> CollectionDOI privateCollectionReserveDoi(collectionId)

Private Collection Reserve DOI

Reserve DOI for collection

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection Unique identifier
apiInstance.privateCollectionReserveDoi(collectionId, (error, data, response) => {
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
 **collectionId** | **Number**| Collection Unique identifier | 

### Return type

[**CollectionDOI**](CollectionDOI.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateCollectionReserveHandle

> CollectionHandle privateCollectionReserveHandle(collectionId)

Private Collection Reserve Handle

Reserve Handle for collection

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection Unique identifier
apiInstance.privateCollectionReserveHandle(collectionId, (error, data, response) => {
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
 **collectionId** | **Number**| Collection Unique identifier | 

### Return type

[**CollectionHandle**](CollectionHandle.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateCollectionResource

> Location privateCollectionResource(collectionId, resource)

Private Collection Resource

Edit collection resource data.

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection unique identifier
let resource = new FigshareApi.Resource(); // Resource | Resource data
apiInstance.privateCollectionResource(collectionId, resource, (error, data, response) => {
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
 **collectionId** | **Number**| Collection unique identifier | 
 **resource** | [**Resource**](Resource.md)| Resource data | 

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateCollectionUpdate

> LocationWarningsUpdate privateCollectionUpdate(collectionId, collectionUpdate)

Update collection

Update collection details; request can also be made with the PATCH method.

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let collectionId = 789; // Number | Collection Unique identifier
let collectionUpdate = new FigshareApi.CollectionUpdate(); // CollectionUpdate | Collection description
apiInstance.privateCollectionUpdate(collectionId, collectionUpdate, (error, data, response) => {
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
 **collectionId** | **Number**| Collection Unique identifier | 
 **collectionUpdate** | [**CollectionUpdate**](CollectionUpdate.md)| Collection description | 

### Return type

[**LocationWarningsUpdate**](LocationWarningsUpdate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateCollectionsList

> [Collection] privateCollectionsList(opts)

Private Collections List

List private collections

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let opts = {
  'page': 789, // Number | Page number. Used for pagination with page_size
  'pageSize': 10, // Number | The number of results included on a page. Used for pagination with page
  'limit': 789, // Number | Number of results included on a page. Used for pagination with query
  'offset': 789, // Number | Where to start the listing(the offset of the first result). Used for pagination with limit
  'order': "'published_date'", // String | The field by which to order. Default varies by endpoint/resource.
  'orderDirection': "'desc'" // String | 
};
apiInstance.privateCollectionsList(opts, (error, data, response) => {
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
 **page** | **Number**| Page number. Used for pagination with page_size | [optional] 
 **pageSize** | **Number**| The number of results included on a page. Used for pagination with page | [optional] [default to 10]
 **limit** | **Number**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **Number**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 
 **order** | **String**| The field by which to order. Default varies by endpoint/resource. | [optional] [default to &#39;published_date&#39;]
 **orderDirection** | **String**|  | [optional] [default to &#39;desc&#39;]

### Return type

[**[Collection]**](Collection.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateCollectionsSearch

> [Collection] privateCollectionsSearch(privateCollectionSearch)

Private Collections Search

Returns a list of private Collections

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.CollectionsApi();
let privateCollectionSearch = new FigshareApi.PrivateCollectionSearch(); // PrivateCollectionSearch | Search Parameters
apiInstance.privateCollectionsSearch(privateCollectionSearch, (error, data, response) => {
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
 **privateCollectionSearch** | [**PrivateCollectionSearch**](PrivateCollectionSearch.md)| Search Parameters | 

### Return type

[**[Collection]**](Collection.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

