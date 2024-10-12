# FigshareApi.ArticlesApi

All URIs are relative to *https://api.figshare.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountArticleReport**](ArticlesApi.md#accountArticleReport) | **GET** /account/articles/export | Account Article Report
[**accountArticleReportGenerate**](ArticlesApi.md#accountArticleReportGenerate) | **POST** /account/articles/export | Initiate a new Report
[**articleDetails**](ArticlesApi.md#articleDetails) | **GET** /articles/{article_id} | View article details
[**articleFileDetails**](ArticlesApi.md#articleFileDetails) | **GET** /articles/{article_id}/files/{file_id} | Article file details
[**articleFiles**](ArticlesApi.md#articleFiles) | **GET** /articles/{article_id}/files | List article files
[**articleVersionConfidentiality**](ArticlesApi.md#articleVersionConfidentiality) | **GET** /articles/{article_id}/versions/{v_number}/confidentiality | Public Article Confidentiality for article version
[**articleVersionDetails**](ArticlesApi.md#articleVersionDetails) | **GET** /articles/{article_id}/versions/{v_number} | Article details for version
[**articleVersionEmbargo**](ArticlesApi.md#articleVersionEmbargo) | **GET** /articles/{article_id}/versions/{v_number}/embargo | Public Article Embargo for article version
[**articleVersionUpdate**](ArticlesApi.md#articleVersionUpdate) | **PUT** /account/articles/{article_id}/versions/{version_id}/ | Update article version
[**articleVersionUpdateThumb**](ArticlesApi.md#articleVersionUpdateThumb) | **PUT** /account/articles/{article_id}/versions/{version_id}/update_thumb | Update article version thumbnail
[**articleVersions**](ArticlesApi.md#articleVersions) | **GET** /articles/{article_id}/versions | List article versions
[**articlesList**](ArticlesApi.md#articlesList) | **GET** /articles | Public Articles
[**articlesSearch**](ArticlesApi.md#articlesSearch) | **POST** /articles/search | Public Articles Search
[**privateArticleAuthorDelete**](ArticlesApi.md#privateArticleAuthorDelete) | **DELETE** /account/articles/{article_id}/authors/{author_id} | Delete article author
[**privateArticleAuthorsAdd**](ArticlesApi.md#privateArticleAuthorsAdd) | **POST** /account/articles/{article_id}/authors | Add article authors
[**privateArticleAuthorsList**](ArticlesApi.md#privateArticleAuthorsList) | **GET** /account/articles/{article_id}/authors | List article authors
[**privateArticleAuthorsReplace**](ArticlesApi.md#privateArticleAuthorsReplace) | **PUT** /account/articles/{article_id}/authors | Replace article authors
[**privateArticleCategoriesAdd**](ArticlesApi.md#privateArticleCategoriesAdd) | **POST** /account/articles/{article_id}/categories | Add article categories
[**privateArticleCategoriesList**](ArticlesApi.md#privateArticleCategoriesList) | **GET** /account/articles/{article_id}/categories | List article categories
[**privateArticleCategoriesReplace**](ArticlesApi.md#privateArticleCategoriesReplace) | **PUT** /account/articles/{article_id}/categories | Replace article categories
[**privateArticleCategoryDelete**](ArticlesApi.md#privateArticleCategoryDelete) | **DELETE** /account/articles/{article_id}/categories/{category_id} | Delete article category
[**privateArticleConfidentialityDelete**](ArticlesApi.md#privateArticleConfidentialityDelete) | **DELETE** /account/articles/{article_id}/confidentiality | Delete article confidentiality
[**privateArticleConfidentialityDetails**](ArticlesApi.md#privateArticleConfidentialityDetails) | **GET** /account/articles/{article_id}/confidentiality | Article confidentiality details
[**privateArticleConfidentialityUpdate**](ArticlesApi.md#privateArticleConfidentialityUpdate) | **PUT** /account/articles/{article_id}/confidentiality | Update article confidentiality
[**privateArticleCreate**](ArticlesApi.md#privateArticleCreate) | **POST** /account/articles | Create new Article
[**privateArticleDelete**](ArticlesApi.md#privateArticleDelete) | **DELETE** /account/articles/{article_id} | Delete article
[**privateArticleDetails**](ArticlesApi.md#privateArticleDetails) | **GET** /account/articles/{article_id} | Article details
[**privateArticleEmbargoDelete**](ArticlesApi.md#privateArticleEmbargoDelete) | **DELETE** /account/articles/{article_id}/embargo | Delete Article Embargo
[**privateArticleEmbargoDetails**](ArticlesApi.md#privateArticleEmbargoDetails) | **GET** /account/articles/{article_id}/embargo | Article Embargo Details
[**privateArticleEmbargoUpdate**](ArticlesApi.md#privateArticleEmbargoUpdate) | **PUT** /account/articles/{article_id}/embargo | Update Article Embargo
[**privateArticleFile**](ArticlesApi.md#privateArticleFile) | **GET** /account/articles/{article_id}/files/{file_id} | Single File
[**privateArticleFileDelete**](ArticlesApi.md#privateArticleFileDelete) | **DELETE** /account/articles/{article_id}/files/{file_id} | File Delete
[**privateArticleFilesList**](ArticlesApi.md#privateArticleFilesList) | **GET** /account/articles/{article_id}/files | List article files
[**privateArticlePrivateLink**](ArticlesApi.md#privateArticlePrivateLink) | **GET** /account/articles/{article_id}/private_links | List private links
[**privateArticlePrivateLinkCreate**](ArticlesApi.md#privateArticlePrivateLinkCreate) | **POST** /account/articles/{article_id}/private_links | Create private link
[**privateArticlePrivateLinkDelete**](ArticlesApi.md#privateArticlePrivateLinkDelete) | **DELETE** /account/articles/{article_id}/private_links/{link_id} | Disable private link
[**privateArticlePrivateLinkUpdate**](ArticlesApi.md#privateArticlePrivateLinkUpdate) | **PUT** /account/articles/{article_id}/private_links/{link_id} | Update private link
[**privateArticlePublish**](ArticlesApi.md#privateArticlePublish) | **POST** /account/articles/{article_id}/publish | Private Article Publish
[**privateArticleReserveDoi**](ArticlesApi.md#privateArticleReserveDoi) | **POST** /account/articles/{article_id}/reserve_doi | Private Article Reserve DOI
[**privateArticleReserveHandle**](ArticlesApi.md#privateArticleReserveHandle) | **POST** /account/articles/{article_id}/reserve_handle | Private Article Reserve Handle
[**privateArticleResource**](ArticlesApi.md#privateArticleResource) | **POST** /account/articles/{article_id}/resource | Private Article Resource
[**privateArticleUpdate**](ArticlesApi.md#privateArticleUpdate) | **PUT** /account/articles/{article_id} | Update article
[**privateArticleUploadComplete**](ArticlesApi.md#privateArticleUploadComplete) | **POST** /account/articles/{article_id}/files/{file_id} | Complete Upload
[**privateArticleUploadInitiate**](ArticlesApi.md#privateArticleUploadInitiate) | **POST** /account/articles/{article_id}/files | Initiate Upload
[**privateArticlesList**](ArticlesApi.md#privateArticlesList) | **GET** /account/articles | Private Articles
[**privateArticlesSearch**](ArticlesApi.md#privateArticlesSearch) | **POST** /account/articles/search | Private Articles search



## accountArticleReport

> [AccountReport] accountArticleReport(opts)

Account Article Report

Return status on all reports generated for the account from the oauth credentials

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let opts = {
  'groupId': 789 // Number | A group ID to filter by
};
apiInstance.accountArticleReport(opts, (error, data, response) => {
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
 **groupId** | **Number**| A group ID to filter by | [optional] 

### Return type

[**[AccountReport]**](AccountReport.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountArticleReportGenerate

> AccountReport accountArticleReportGenerate()

Initiate a new Report

Initiate a new Article Report for this Account. There is a limit of 1 report per day.

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
apiInstance.accountArticleReportGenerate((error, data, response) => {
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

[**AccountReport**](AccountReport.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articleDetails

> ArticleComplete articleDetails(articleId)

View article details

View an article

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article Unique identifier
apiInstance.articleDetails(articleId, (error, data, response) => {
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
 **articleId** | **Number**| Article Unique identifier | 

### Return type

[**ArticleComplete**](ArticleComplete.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articleFileDetails

> PublicFile articleFileDetails(articleId, fileId)

Article file details

File by id

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article Unique identifier
let fileId = 789; // Number | File Unique identifier
apiInstance.articleFileDetails(articleId, fileId, (error, data, response) => {
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
 **articleId** | **Number**| Article Unique identifier | 
 **fileId** | **Number**| File Unique identifier | 

### Return type

[**PublicFile**](PublicFile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articleFiles

> [PublicFile] articleFiles(articleId)

List article files

Files list for article

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article Unique identifier
apiInstance.articleFiles(articleId, (error, data, response) => {
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
 **articleId** | **Number**| Article Unique identifier | 

### Return type

[**[PublicFile]**](PublicFile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articleVersionConfidentiality

> ArticleConfidentiality articleVersionConfidentiality(articleId, vNumber)

Public Article Confidentiality for article version

Confidentiality for article version. The confidentiality feature is now deprecated. This has been replaced by the new extended embargo functionality and all items that used to be confidential have now been migrated to items with a permanent embargo on files. All API endpoints related to this functionality will remain for backwards compatibility, but will now be attached to the new extended embargo workflows.

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article Unique identifier
let vNumber = 789; // Number | Version Number
apiInstance.articleVersionConfidentiality(articleId, vNumber, (error, data, response) => {
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
 **articleId** | **Number**| Article Unique identifier | 
 **vNumber** | **Number**| Version Number | 

### Return type

[**ArticleConfidentiality**](ArticleConfidentiality.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articleVersionDetails

> ArticleComplete articleVersionDetails(articleId, vNumber)

Article details for version

Article with specified version

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article Unique identifier
let vNumber = 789; // Number | Article Version Number
apiInstance.articleVersionDetails(articleId, vNumber, (error, data, response) => {
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
 **articleId** | **Number**| Article Unique identifier | 
 **vNumber** | **Number**| Article Version Number | 

### Return type

[**ArticleComplete**](ArticleComplete.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articleVersionEmbargo

> ArticleEmbargo articleVersionEmbargo(articleId, vNumber)

Public Article Embargo for article version

Embargo for article version

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article Unique identifier
let vNumber = 789; // Number | Version Number
apiInstance.articleVersionEmbargo(articleId, vNumber, (error, data, response) => {
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
 **articleId** | **Number**| Article Unique identifier | 
 **vNumber** | **Number**| Version Number | 

### Return type

[**ArticleEmbargo**](ArticleEmbargo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articleVersionUpdate

> LocationWarningsUpdate articleVersionUpdate(articleId, versionId, articleUpdate)

Update article version

Updating an article version by passing body parameters; request can also be made with the PATCH method.

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
let versionId = 789; // Number | Article version identifier
let articleUpdate = new FigshareApi.ArticleUpdate(); // ArticleUpdate | Article description
apiInstance.articleVersionUpdate(articleId, versionId, articleUpdate, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 
 **versionId** | **Number**| Article version identifier | 
 **articleUpdate** | [**ArticleUpdate**](ArticleUpdate.md)| Article description | 

### Return type

[**LocationWarningsUpdate**](LocationWarningsUpdate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## articleVersionUpdateThumb

> articleVersionUpdateThumb(articleId, versionId, fileId)

Update article version thumbnail

For a given public article version update the article thumbnail by choosing one of the associated files

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
let versionId = 789; // Number | Article version identifier
let fileId = new FigshareApi.FileId(); // FileId | File ID
apiInstance.articleVersionUpdateThumb(articleId, versionId, fileId, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 
 **versionId** | **Number**| Article version identifier | 
 **fileId** | [**FileId**](FileId.md)| File ID | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## articleVersions

> [ArticleVersions] articleVersions(articleId)

List article versions

List public article versions

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article Unique identifier
apiInstance.articleVersions(articleId, (error, data, response) => {
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
 **articleId** | **Number**| Article Unique identifier | 

### Return type

[**[ArticleVersions]**](ArticleVersions.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articlesList

> [Article] articlesList(opts)

Public Articles

Returns a list of public articles

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.ArticlesApi();
let opts = {
  'xCursor': "xCursor_example", // String | Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected.
  'page': 789, // Number | Page number. Used for pagination with page_size
  'pageSize': 10, // Number | The number of results included on a page. Used for pagination with page
  'limit': 789, // Number | Number of results included on a page. Used for pagination with query
  'offset': 789, // Number | Where to start the listing(the offset of the first result). Used for pagination with limit
  'order': "'published_date'", // String | The field by which to order. Default varies by endpoint/resource.
  'orderDirection': "'desc'", // String | 
  'institution': 789, // Number | only return articles from this institution
  'publishedSince': "publishedSince_example", // String | Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD
  'modifiedSince': "modifiedSince_example", // String | Filter by article modified date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD
  'group': 789, // Number | only return articles from this group
  'resourceDoi': "resourceDoi_example", // String | only return articles with this resource_doi
  'itemType': 789, // Number | Only return articles with the respective type. Mapping for item_type is: 1 - Figure, 2 - Media, 3 - Dataset, 5 - Poster, 6 - Journal contribution, 7 - Presentation, 8 - Thesis, 9 - Software, 11 - Online resource, 12 - Preprint, 13 - Book, 14 - Conference contribution, 15 - Chapter, 16 - Peer review, 17 - Educational resource, 18 - Report, 19 - Standard, 20 - Composition, 21 - Funding, 22 - Physical object, 23 - Data management plan, 24 - Workflow, 25 - Monograph, 26 - Performance, 27 - Event, 28 - Service, 29 - Model
  'doi': "doi_example", // String | only return articles with this doi
  'handle': "handle_example" // String | only return articles with this handle
};
apiInstance.articlesList(opts, (error, data, response) => {
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
 **institution** | **Number**| only return articles from this institution | [optional] 
 **publishedSince** | **String**| Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD | [optional] 
 **modifiedSince** | **String**| Filter by article modified date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD | [optional] 
 **group** | **Number**| only return articles from this group | [optional] 
 **resourceDoi** | **String**| only return articles with this resource_doi | [optional] 
 **itemType** | **Number**| Only return articles with the respective type. Mapping for item_type is: 1 - Figure, 2 - Media, 3 - Dataset, 5 - Poster, 6 - Journal contribution, 7 - Presentation, 8 - Thesis, 9 - Software, 11 - Online resource, 12 - Preprint, 13 - Book, 14 - Conference contribution, 15 - Chapter, 16 - Peer review, 17 - Educational resource, 18 - Report, 19 - Standard, 20 - Composition, 21 - Funding, 22 - Physical object, 23 - Data management plan, 24 - Workflow, 25 - Monograph, 26 - Performance, 27 - Event, 28 - Service, 29 - Model | [optional] 
 **doi** | **String**| only return articles with this doi | [optional] 
 **handle** | **String**| only return articles with this handle | [optional] 

### Return type

[**[Article]**](Article.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articlesSearch

> [ArticleWithProject] articlesSearch(opts)

Public Articles Search

Returns a list of public articles, filtered by the search parameters

### Example

```javascript
import FigshareApi from 'figshare_api';

let apiInstance = new FigshareApi.ArticlesApi();
let opts = {
  'xCursor': "xCursor_example", // String | Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected.
  'articleSearch': new FigshareApi.ArticleSearch() // ArticleSearch | Search Parameters
};
apiInstance.articlesSearch(opts, (error, data, response) => {
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
 **articleSearch** | [**ArticleSearch**](ArticleSearch.md)| Search Parameters | [optional] 

### Return type

[**[ArticleWithProject]**](ArticleWithProject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateArticleAuthorDelete

> privateArticleAuthorDelete(articleId, authorId)

Delete article author

De-associate author from article

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
let authorId = 789; // Number | Article Author unique identifier
apiInstance.privateArticleAuthorDelete(articleId, authorId, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 
 **authorId** | **Number**| Article Author unique identifier | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateArticleAuthorsAdd

> privateArticleAuthorsAdd(articleId, authorsCreator)

Add article authors

Associate new authors with the article. This will add new authors to the list of already associated authors

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
let authorsCreator = new FigshareApi.AuthorsCreator(); // AuthorsCreator | Authors description
apiInstance.privateArticleAuthorsAdd(articleId, authorsCreator, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 
 **authorsCreator** | [**AuthorsCreator**](AuthorsCreator.md)| Authors description | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateArticleAuthorsList

> [Author] privateArticleAuthorsList(articleId)

List article authors

List article authors

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
apiInstance.privateArticleAuthorsList(articleId, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 

### Return type

[**[Author]**](Author.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateArticleAuthorsReplace

> privateArticleAuthorsReplace(articleId, authorsCreator)

Replace article authors

Associate new authors with the article. This will remove all already associated authors and add these new ones

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
let authorsCreator = new FigshareApi.AuthorsCreator(); // AuthorsCreator | Authors description
apiInstance.privateArticleAuthorsReplace(articleId, authorsCreator, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 
 **authorsCreator** | [**AuthorsCreator**](AuthorsCreator.md)| Authors description | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateArticleCategoriesAdd

> privateArticleCategoriesAdd(articleId, categoriesCreator)

Add article categories

Associate new categories with the article. This will add new categories to the list of already associated categories

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
let categoriesCreator = new FigshareApi.CategoriesCreator(); // CategoriesCreator | 
apiInstance.privateArticleCategoriesAdd(articleId, categoriesCreator, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 
 **categoriesCreator** | [**CategoriesCreator**](CategoriesCreator.md)|  | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateArticleCategoriesList

> [Category] privateArticleCategoriesList(articleId)

List article categories

List article categories

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
apiInstance.privateArticleCategoriesList(articleId, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 

### Return type

[**[Category]**](Category.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateArticleCategoriesReplace

> privateArticleCategoriesReplace(articleId, categoriesCreator)

Replace article categories

Associate new categories with the article. This will remove all already associated categories and add these new ones

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
let categoriesCreator = new FigshareApi.CategoriesCreator(); // CategoriesCreator | 
apiInstance.privateArticleCategoriesReplace(articleId, categoriesCreator, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 
 **categoriesCreator** | [**CategoriesCreator**](CategoriesCreator.md)|  | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateArticleCategoryDelete

> privateArticleCategoryDelete(articleId, categoryId)

Delete article category

De-associate category from article

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
let categoryId = 789; // Number | Category unique identifier
apiInstance.privateArticleCategoryDelete(articleId, categoryId, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 
 **categoryId** | **Number**| Category unique identifier | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateArticleConfidentialityDelete

> privateArticleConfidentialityDelete(articleId)

Delete article confidentiality

Delete confidentiality settings. The confidentiality feature is now deprecated. This has been replaced by the new extended embargo functionality and all items that used to be confidential have now been migrated to items with a permanent embargo on files. All API endpoints related to this functionality will remain for backwards compatibility, but will now be attached to the new extended embargo workflows.

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
apiInstance.privateArticleConfidentialityDelete(articleId, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateArticleConfidentialityDetails

> ArticleConfidentiality privateArticleConfidentialityDetails(articleId)

Article confidentiality details

View confidentiality settings. The confidentiality feature is now deprecated. This has been replaced by the new extended embargo functionality and all items that used to be confidential have now been migrated to items with a permanent embargo on files. All API endpoints related to this functionality will remain for backwards compatibility, but will now be attached to the new extended embargo workflows.

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
apiInstance.privateArticleConfidentialityDetails(articleId, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 

### Return type

[**ArticleConfidentiality**](ArticleConfidentiality.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateArticleConfidentialityUpdate

> privateArticleConfidentialityUpdate(articleId, confidentialityCreator)

Update article confidentiality

Update confidentiality settings. The confidentiality feature is now deprecated. This has been replaced by the new extended embargo functionality and all items that used to be confidential have now been migrated to items with a permanent embargo on files. All API endpoints related to this functionality will remain for backwards compatibility, but will now be attached to the new extended embargo workflows.

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
let confidentialityCreator = new FigshareApi.ConfidentialityCreator(); // ConfidentialityCreator | 
apiInstance.privateArticleConfidentialityUpdate(articleId, confidentialityCreator, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 
 **confidentialityCreator** | [**ConfidentialityCreator**](ConfidentialityCreator.md)|  | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateArticleCreate

> LocationWarnings privateArticleCreate(articleCreate)

Create new Article

Create a new Article by sending article information

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleCreate = new FigshareApi.ArticleCreate(); // ArticleCreate | Article description
apiInstance.privateArticleCreate(articleCreate, (error, data, response) => {
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
 **articleCreate** | [**ArticleCreate**](ArticleCreate.md)| Article description | 

### Return type

[**LocationWarnings**](LocationWarnings.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateArticleDelete

> privateArticleDelete(articleId)

Delete article

Delete an article

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
apiInstance.privateArticleDelete(articleId, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateArticleDetails

> ArticleCompletePrivate privateArticleDetails(articleId)

Article details

View a private article

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
apiInstance.privateArticleDetails(articleId, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 

### Return type

[**ArticleCompletePrivate**](ArticleCompletePrivate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateArticleEmbargoDelete

> privateArticleEmbargoDelete(articleId)

Delete Article Embargo

Will lift the embargo for the specified article

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
apiInstance.privateArticleEmbargoDelete(articleId, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateArticleEmbargoDetails

> ArticleEmbargo privateArticleEmbargoDetails(articleId)

Article Embargo Details

View a private article embargo details

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
apiInstance.privateArticleEmbargoDetails(articleId, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 

### Return type

[**ArticleEmbargo**](ArticleEmbargo.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateArticleEmbargoUpdate

> privateArticleEmbargoUpdate(articleId, articleEmbargoUpdater)

Update Article Embargo

Note: setting an article under whole embargo does not imply that the article will be published when the embargo will expire. You must explicitly call the publish endpoint to enable this functionality.

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
let articleEmbargoUpdater = new FigshareApi.ArticleEmbargoUpdater(); // ArticleEmbargoUpdater | Embargo description
apiInstance.privateArticleEmbargoUpdate(articleId, articleEmbargoUpdater, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 
 **articleEmbargoUpdater** | [**ArticleEmbargoUpdater**](ArticleEmbargoUpdater.md)| Embargo description | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateArticleFile

> PrivateFile privateArticleFile(articleId, fileId)

Single File

View details of file for specified article

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
let fileId = 789; // Number | File unique identifier
apiInstance.privateArticleFile(articleId, fileId, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 
 **fileId** | **Number**| File unique identifier | 

### Return type

[**PrivateFile**](PrivateFile.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateArticleFileDelete

> privateArticleFileDelete(articleId, fileId)

File Delete

Complete file upload

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
let fileId = 789; // Number | File unique identifier
apiInstance.privateArticleFileDelete(articleId, fileId, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 
 **fileId** | **Number**| File unique identifier | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateArticleFilesList

> [PrivateFile] privateArticleFilesList(articleId)

List article files

List private files

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
apiInstance.privateArticleFilesList(articleId, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 

### Return type

[**[PrivateFile]**](PrivateFile.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateArticlePrivateLink

> [PrivateLink] privateArticlePrivateLink(articleId)

List private links

List private links

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
apiInstance.privateArticlePrivateLink(articleId, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 

### Return type

[**[PrivateLink]**](PrivateLink.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateArticlePrivateLinkCreate

> PrivateLinkResponse privateArticlePrivateLinkCreate(articleId, opts)

Create private link

Create new private link for this article

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
let opts = {
  'privateLinkCreator': new FigshareApi.PrivateLinkCreator() // PrivateLinkCreator | 
};
apiInstance.privateArticlePrivateLinkCreate(articleId, opts, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 
 **privateLinkCreator** | [**PrivateLinkCreator**](PrivateLinkCreator.md)|  | [optional] 

### Return type

[**PrivateLinkResponse**](PrivateLinkResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateArticlePrivateLinkDelete

> privateArticlePrivateLinkDelete(articleId, linkId)

Disable private link

Disable/delete private link for this article

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
let linkId = "linkId_example"; // String | Private link token
apiInstance.privateArticlePrivateLinkDelete(articleId, linkId, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 
 **linkId** | **String**| Private link token | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateArticlePrivateLinkUpdate

> privateArticlePrivateLinkUpdate(articleId, linkId, opts)

Update private link

Update existing private link for this article

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
let linkId = "linkId_example"; // String | Private link token
let opts = {
  'privateLinkCreator': new FigshareApi.PrivateLinkCreator() // PrivateLinkCreator | 
};
apiInstance.privateArticlePrivateLinkUpdate(articleId, linkId, opts, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 
 **linkId** | **String**| Private link token | 
 **privateLinkCreator** | [**PrivateLinkCreator**](PrivateLinkCreator.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateArticlePublish

> Location privateArticlePublish(articleId)

Private Article Publish

- If the whole article is under embargo, it will not be published immediately, but when the embargo expires or is lifted. - When an article is published, a new public version will be generated. Any further updates to the article will affect the private article data. In order to make these changes publicly visible, an explicit publish operation is needed.

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
apiInstance.privateArticlePublish(articleId, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateArticleReserveDoi

> ArticleDOI privateArticleReserveDoi(articleId)

Private Article Reserve DOI

Reserve DOI for article

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
apiInstance.privateArticleReserveDoi(articleId, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 

### Return type

[**ArticleDOI**](ArticleDOI.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateArticleReserveHandle

> ArticleHandle privateArticleReserveHandle(articleId)

Private Article Reserve Handle

Reserve Handle for article

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
apiInstance.privateArticleReserveHandle(articleId, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 

### Return type

[**ArticleHandle**](ArticleHandle.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateArticleResource

> Location privateArticleResource(articleId, resource)

Private Article Resource

Edit article resource data.

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
let resource = new FigshareApi.Resource(); // Resource | Resource data
apiInstance.privateArticleResource(articleId, resource, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 
 **resource** | [**Resource**](Resource.md)| Resource data | 

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateArticleUpdate

> LocationWarningsUpdate privateArticleUpdate(articleId, articleUpdate)

Update article

Updating an article by passing body parameters; request can also be made with the PATCH method.

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
let articleUpdate = new FigshareApi.ArticleUpdate(); // ArticleUpdate | Article description
apiInstance.privateArticleUpdate(articleId, articleUpdate, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 
 **articleUpdate** | [**ArticleUpdate**](ArticleUpdate.md)| Article description | 

### Return type

[**LocationWarningsUpdate**](LocationWarningsUpdate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateArticleUploadComplete

> privateArticleUploadComplete(articleId, fileId)

Complete Upload

Complete file upload

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
let fileId = 789; // Number | File unique identifier
apiInstance.privateArticleUploadComplete(articleId, fileId, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 
 **fileId** | **Number**| File unique identifier | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateArticleUploadInitiate

> Location privateArticleUploadInitiate(articleId, fileCreator)

Initiate Upload

Initiate a new file upload within the article. Either use the link property to point to an existing file that resides elsewhere and will not be uploaded to Figshare or use the other 3 parameters (md5, name, size).

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let articleId = 789; // Number | Article unique identifier
let fileCreator = new FigshareApi.FileCreator(); // FileCreator | 
apiInstance.privateArticleUploadInitiate(articleId, fileCreator, (error, data, response) => {
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
 **articleId** | **Number**| Article unique identifier | 
 **fileCreator** | [**FileCreator**](FileCreator.md)|  | 

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateArticlesList

> [Article] privateArticlesList(opts)

Private Articles

Get Own Articles

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let opts = {
  'page': 789, // Number | Page number. Used for pagination with page_size
  'pageSize': 10, // Number | The number of results included on a page. Used for pagination with page
  'limit': 789, // Number | Number of results included on a page. Used for pagination with query
  'offset': 789 // Number | Where to start the listing(the offset of the first result). Used for pagination with limit
};
apiInstance.privateArticlesList(opts, (error, data, response) => {
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

### Return type

[**[Article]**](Article.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateArticlesSearch

> [ArticleWithProject] privateArticlesSearch(privateArticleSearch)

Private Articles search

Returns a list of private articles filtered by the search parameters

### Example

```javascript
import FigshareApi from 'figshare_api';
let defaultClient = FigshareApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FigshareApi.ArticlesApi();
let privateArticleSearch = new FigshareApi.PrivateArticleSearch(); // PrivateArticleSearch | Search Parameters
apiInstance.privateArticlesSearch(privateArticleSearch, (error, data, response) => {
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
 **privateArticleSearch** | [**PrivateArticleSearch**](PrivateArticleSearch.md)| Search Parameters | 

### Return type

[**[ArticleWithProject]**](ArticleWithProject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

