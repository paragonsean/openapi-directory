# CoreApiV2.ArticlesApi

All URIs are relative to *http://core.ac.uk/api-v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getArticleByCoreId**](ArticlesApi.md#getArticleByCoreId) | **GET** /articles/get/{coreId} | Get article by CORE ID
[**getArticleByCoreIdBatch**](ArticlesApi.md#getArticleByCoreIdBatch) | **POST** /articles/get | Batch operation for retrieving articles by CORE ID
[**getArticleHistoryByCoreId**](ArticlesApi.md#getArticleHistoryByCoreId) | **GET** /articles/get/{coreId}/history | Get article history by CORE ID
[**getArticlePdfByCoreId**](ArticlesApi.md#getArticlePdfByCoreId) | **GET** /articles/get/{coreId}/download/pdf | Get fulltext PDF by CORE ID
[**nearDuplicateArticles**](ArticlesApi.md#nearDuplicateArticles) | **POST** /articles/dedup | Get all near duplicate articles
[**searchArticles**](ArticlesApi.md#searchArticles) | **GET** /articles/search/{query} | Search through all documents
[**searchArticlesBatch**](ArticlesApi.md#searchArticlesBatch) | **POST** /articles/search | Batch operation for search through articles
[**similarArticles**](ArticlesApi.md#similarArticles) | **POST** /articles/similar | Get articles by similarity to a text



## getArticleByCoreId

> ArticleResponse getArticleByCoreId(coreId, opts)

Get article by CORE ID

Method will retrieve an article based on given CORE ID.

### Example

```javascript
import CoreApiV2 from 'core_api_v2';
let defaultClient = CoreApiV2.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new CoreApiV2.ArticlesApi();
let coreId = 789; // Number | CORE ID of the article that needs to be fetched.
let opts = {
  'metadata': true, // Boolean | Whether to retrieve the full article metadata or only the ID. The default value is true.
  'fulltext': false, // Boolean | Whether to retrieve full text of the article. The default value is false
  'citations': false, // Boolean | Whether to retrieve citations found in the article. The default value is false
  'similar': false, // Boolean | Whether to retrieve a list of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time
  'duplicate': false, // Boolean | Whether to retrieve a list of CORE IDs of different versions of the article. The default value is false
  'urls': false, // Boolean | Whether to retrieve a list of URLs from which the article can be downloaded. This can include links to PDFs as well as HTML pages. The default value is false
  'faithfulMetadata': false // Boolean | Returns the records raw XML metadata from the original repository. The default value is false
};
apiInstance.getArticleByCoreId(coreId, opts, (error, data, response) => {
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
 **coreId** | **Number**| CORE ID of the article that needs to be fetched. | 
 **metadata** | **Boolean**| Whether to retrieve the full article metadata or only the ID. The default value is true. | [optional] [default to true]
 **fulltext** | **Boolean**| Whether to retrieve full text of the article. The default value is false | [optional] [default to false]
 **citations** | **Boolean**| Whether to retrieve citations found in the article. The default value is false | [optional] [default to false]
 **similar** | **Boolean**| Whether to retrieve a list of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time | [optional] [default to false]
 **duplicate** | **Boolean**| Whether to retrieve a list of CORE IDs of different versions of the article. The default value is false | [optional] [default to false]
 **urls** | **Boolean**| Whether to retrieve a list of URLs from which the article can be downloaded. This can include links to PDFs as well as HTML pages. The default value is false | [optional] [default to false]
 **faithfulMetadata** | **Boolean**| Returns the records raw XML metadata from the original repository. The default value is false | [optional] [default to false]

### Return type

[**ArticleResponse**](ArticleResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getArticleByCoreIdBatch

> [ArticleResponse] getArticleByCoreIdBatch(body, opts)

Batch operation for retrieving articles by CORE ID

Method accepts a JSON array of CORE IDs and retrieves a list of articles. The response array is ordered based on the order of the IDs in the request array.

### Example

```javascript
import CoreApiV2 from 'core_api_v2';
let defaultClient = CoreApiV2.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new CoreApiV2.ArticlesApi();
let body = [null]; // [Number] | JSON array with CORE IDs of articles that need to be fetched
let opts = {
  'metadata': true, // Boolean | Whether to retrieve the full article metadata or only the IDs. The default value is true
  'fulltext': false, // Boolean | Whether to retrieve fulltexts of the articles. The default value is false
  'citations': false, // Boolean | Whether to retrieve citations found in the articles. The default value is false
  'similar': false, // Boolean | Whether to retrieve lists of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time
  'duplicate': false, // Boolean | Whether to retrieve CORE IDs of different versions of the articles. The default value is false
  'urls': false, // Boolean | Whether to retrieve lists of URLs of the article fulltexts. The default value is false
  'faithfulMetadata': false // Boolean | Returns the records raw XML metadata from the original repository. The default value is false
};
apiInstance.getArticleByCoreIdBatch(body, opts, (error, data, response) => {
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
 **body** | [**[Number]**](Number.md)| JSON array with CORE IDs of articles that need to be fetched | 
 **metadata** | **Boolean**| Whether to retrieve the full article metadata or only the IDs. The default value is true | [optional] [default to true]
 **fulltext** | **Boolean**| Whether to retrieve fulltexts of the articles. The default value is false | [optional] [default to false]
 **citations** | **Boolean**| Whether to retrieve citations found in the articles. The default value is false | [optional] [default to false]
 **similar** | **Boolean**| Whether to retrieve lists of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time | [optional] [default to false]
 **duplicate** | **Boolean**| Whether to retrieve CORE IDs of different versions of the articles. The default value is false | [optional] [default to false]
 **urls** | **Boolean**| Whether to retrieve lists of URLs of the article fulltexts. The default value is false | [optional] [default to false]
 **faithfulMetadata** | **Boolean**| Returns the records raw XML metadata from the original repository. The default value is false | [optional] [default to false]

### Return type

[**[ArticleResponse]**](ArticleResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getArticleHistoryByCoreId

> ArticleHistoryResponse getArticleHistoryByCoreId(coreId, opts)

Get article history by CORE ID

Method accepts a single CORE ID and returns a list of all historical versions of the article, which are stored in CORE database. The results are ordered from the newest one to the oldest one.

### Example

```javascript
import CoreApiV2 from 'core_api_v2';
let defaultClient = CoreApiV2.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new CoreApiV2.ArticlesApi();
let coreId = "coreId_example"; // String | CORE ID of the article which history should be fetched
let opts = {
  'page': 1, // Number | Which page of the history results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page).
  'pageSize': 10 // Number | The number of results to return per page. Can be any number between 10 and 100, default is 10.
};
apiInstance.getArticleHistoryByCoreId(coreId, opts, (error, data, response) => {
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
 **coreId** | **String**| CORE ID of the article which history should be fetched | 
 **page** | **Number**| Which page of the history results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page). | [optional] [default to 1]
 **pageSize** | **Number**| The number of results to return per page. Can be any number between 10 and 100, default is 10. | [optional] [default to 10]

### Return type

[**ArticleHistoryResponse**](ArticleHistoryResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getArticlePdfByCoreId

> getArticlePdfByCoreId(coreId)

Get fulltext PDF by CORE ID

Method will retrieve an article based on given CORE ID.

### Example

```javascript
import CoreApiV2 from 'core_api_v2';
let defaultClient = CoreApiV2.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new CoreApiV2.ArticlesApi();
let coreId = "coreId_example"; // String | ID of article history that needs to be fetched
apiInstance.getArticlePdfByCoreId(coreId, (error, data, response) => {
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
 **coreId** | **String**| ID of article history that needs to be fetched | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## nearDuplicateArticles

> Object nearDuplicateArticles(opts)

Get all near duplicate articles

Method accepts values for several parameters and retrieves a JSON array of articles which have near duplicate content matching the input parameters&#39; values. The response array contains ids of the near duplicate articles along with their relevance scores.

### Example

```javascript
import CoreApiV2 from 'core_api_v2';
let defaultClient = CoreApiV2.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new CoreApiV2.ArticlesApi();
let opts = {
  'doi': "doi_example", // String | The DOI for which the duplicates will be identified
  'title': "title_example", // String | Title to match when looking for duplicate articles. Only useful when either value for @year or @description is supplied.
  'year': "year_example", // String | Year the article was published. Only useful when value for @title is supplied. 
  'description': "description_example", // String | Abstract for an article based on which its duplicates will be found. Only useful when value for @title is supplied.
  'fulltext': "fulltext_example", // String | Full text for an article based on which its duplicates will be found.
  'identifier': "identifier_example", // String | Article identifier for which the duplicates will be identified. Only useful when either values for @doi or (@title and @year) or (@title and @abstract) or @fulltext are supplied.
  'repositoryId': "repositoryId_example" // String | Limit the duplicates search to particular repository id. 
};
apiInstance.nearDuplicateArticles(opts, (error, data, response) => {
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
 **doi** | **String**| The DOI for which the duplicates will be identified | [optional] 
 **title** | **String**| Title to match when looking for duplicate articles. Only useful when either value for @year or @description is supplied. | [optional] 
 **year** | **String**| Year the article was published. Only useful when value for @title is supplied.  | [optional] 
 **description** | **String**| Abstract for an article based on which its duplicates will be found. Only useful when value for @title is supplied. | [optional] 
 **fulltext** | **String**| Full text for an article based on which its duplicates will be found. | [optional] 
 **identifier** | **String**| Article identifier for which the duplicates will be identified. Only useful when either values for @doi or (@title and @year) or (@title and @abstract) or @fulltext are supplied. | [optional] 
 **repositoryId** | **String**| Limit the duplicates search to particular repository id.  | [optional] 

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchArticles

> ArticleSearchResponse searchArticles(query, opts)

Search through all documents

Searches through all articles and returns a JSON array with search results. Method searches through all article fields.

### Example

```javascript
import CoreApiV2 from 'core_api_v2';
let defaultClient = CoreApiV2.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new CoreApiV2.ArticlesApi();
let query = 789; // Number | The search query
let opts = {
  'page': 1, // Number | Which page of the search results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page).
  'pageSize': 10, // Number | The number of results to return per page. Can be any number between 10 and 100, default is 10.
  'metadata': true, // Boolean | Whether to retrieve the full article metadata or only the ID. The default value is true.
  'fulltext': false, // Boolean | Whether to retrieve full text of the article. The default value is false
  'citations': false, // Boolean | Whether to retrieve citations found in the article. The default value is false
  'similar': false, // Boolean | Whether to retrieve a list of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time
  'duplicate': false, // Boolean | Whether to retrieve a list of CORE IDs of different versions of the article. The default value is false
  'urls': false, // Boolean | Whether to retrieve a list of URLs from which the article can be downloaded. This can include links to PDFs as well as HTML pages. The default value is false
  'faithfulMetadata': false // Boolean | Returns the records raw XML metadata from the original repository. The default value is false
};
apiInstance.searchArticles(query, opts, (error, data, response) => {
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
 **query** | **Number**| The search query | 
 **page** | **Number**| Which page of the search results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page). | [optional] [default to 1]
 **pageSize** | **Number**| The number of results to return per page. Can be any number between 10 and 100, default is 10. | [optional] [default to 10]
 **metadata** | **Boolean**| Whether to retrieve the full article metadata or only the ID. The default value is true. | [optional] [default to true]
 **fulltext** | **Boolean**| Whether to retrieve full text of the article. The default value is false | [optional] [default to false]
 **citations** | **Boolean**| Whether to retrieve citations found in the article. The default value is false | [optional] [default to false]
 **similar** | **Boolean**| Whether to retrieve a list of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time | [optional] [default to false]
 **duplicate** | **Boolean**| Whether to retrieve a list of CORE IDs of different versions of the article. The default value is false | [optional] [default to false]
 **urls** | **Boolean**| Whether to retrieve a list of URLs from which the article can be downloaded. This can include links to PDFs as well as HTML pages. The default value is false | [optional] [default to false]
 **faithfulMetadata** | **Boolean**| Returns the records raw XML metadata from the original repository. The default value is false | [optional] [default to false]

### Return type

[**ArticleSearchResponse**](ArticleSearchResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchArticlesBatch

> [ArticleSearchResponse] searchArticlesBatch(body, opts)

Batch operation for search through articles

Method accepts a JSON array of search queries and parameters. It then searches through all articles and returns a JSON array of search results for each of the queries. Method searches through all article fields (title, authors, subjects, identifiers, etc.).

### Example

```javascript
import CoreApiV2 from 'core_api_v2';
let defaultClient = CoreApiV2.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new CoreApiV2.ArticlesApi();
let body = [new CoreApiV2.SearchRequest()]; // [SearchRequest] | JSON array with search queries and parameters. One request can contain up to 100 queries
let opts = {
  'metadata': true, // Boolean | Whether to retrieve the full article metadata or only the ID. The default value is true.
  'fulltext': false, // Boolean | Whether to retrieve full text of the article. The default value is false
  'citations': false, // Boolean | Whether to retrieve citations found in the article. The default value is false
  'similar': false, // Boolean | Whether to retrieve a list of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time
  'duplicate': false, // Boolean | Whether to retrieve a list of CORE IDs of different versions of the article. The default value is false
  'urls': false, // Boolean | Whether to retrieve a list of URLs from which the article can be downloaded. This can include links to PDFs as well as HTML pages. The default value is false
  'faithfulMetadata': false // Boolean | Whether to retrieve the raw XML metadata of the article. The default value is false
};
apiInstance.searchArticlesBatch(body, opts, (error, data, response) => {
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
 **body** | [**[SearchRequest]**](SearchRequest.md)| JSON array with search queries and parameters. One request can contain up to 100 queries | 
 **metadata** | **Boolean**| Whether to retrieve the full article metadata or only the ID. The default value is true. | [optional] [default to true]
 **fulltext** | **Boolean**| Whether to retrieve full text of the article. The default value is false | [optional] [default to false]
 **citations** | **Boolean**| Whether to retrieve citations found in the article. The default value is false | [optional] [default to false]
 **similar** | **Boolean**| Whether to retrieve a list of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time | [optional] [default to false]
 **duplicate** | **Boolean**| Whether to retrieve a list of CORE IDs of different versions of the article. The default value is false | [optional] [default to false]
 **urls** | **Boolean**| Whether to retrieve a list of URLs from which the article can be downloaded. This can include links to PDFs as well as HTML pages. The default value is false | [optional] [default to false]
 **faithfulMetadata** | **Boolean**| Whether to retrieve the raw XML metadata of the article. The default value is false | [optional] [default to false]

### Return type

[**[ArticleSearchResponse]**](ArticleSearchResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## similarArticles

> ArticleSimilarResponse similarArticles(body, opts)

Get articles by similarity to a text

Method accepts a text and retrieves a JSON array of articles which are similar to the given text. The response array is ordered based on similarity score, starting from the most similar.

### Example

```javascript
import CoreApiV2 from 'core_api_v2';
let defaultClient = CoreApiV2.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new CoreApiV2.ArticlesApi();
let body = new CoreApiV2.SimilarRequest(); // SimilarRequest | The text that requires similar articles to be calculated on
let opts = {
  'limit': 10, // Number | How many similar articles to retrieve at most. Can be any number betwen 1 and 100, default is 10
  'metadata': true, // Boolean | Whether to retrieve the full article metadata or only the IDs of the similar articles. The default value is true
  'fulltext': false, // Boolean | Whether to retrieve fulltexts of the similar articles. The default value is false
  'citations': false, // Boolean | Whether to retrieve citations found in the articles. The default value is false
  'similar': false, // Boolean | Whether to retrieve lists of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time
  'duplicate': false, // Boolean | Whether to retrieve CORE IDs of different versions of the articles. The default value is false
  'urls': false, // Boolean | Whether to retrieve lists of URLs of the article fulltexts. The default value is false
  'faithfulMetadata': false // Boolean | Whether to retrieve the raw XML metadata of the articles. The default value is false
};
apiInstance.similarArticles(body, opts, (error, data, response) => {
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
 **body** | [**SimilarRequest**](SimilarRequest.md)| The text that requires similar articles to be calculated on | 
 **limit** | **Number**| How many similar articles to retrieve at most. Can be any number betwen 1 and 100, default is 10 | [optional] [default to 10]
 **metadata** | **Boolean**| Whether to retrieve the full article metadata or only the IDs of the similar articles. The default value is true | [optional] [default to true]
 **fulltext** | **Boolean**| Whether to retrieve fulltexts of the similar articles. The default value is false | [optional] [default to false]
 **citations** | **Boolean**| Whether to retrieve citations found in the articles. The default value is false | [optional] [default to false]
 **similar** | **Boolean**| Whether to retrieve lists of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time | [optional] [default to false]
 **duplicate** | **Boolean**| Whether to retrieve CORE IDs of different versions of the articles. The default value is false | [optional] [default to false]
 **urls** | **Boolean**| Whether to retrieve lists of URLs of the article fulltexts. The default value is false | [optional] [default to false]
 **faithfulMetadata** | **Boolean**| Whether to retrieve the raw XML metadata of the articles. The default value is false | [optional] [default to false]

### Return type

[**ArticleSimilarResponse**](ArticleSimilarResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

