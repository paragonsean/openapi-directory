# Vimeo.PortfoliosVideosApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addVideoToPortfolio**](PortfoliosVideosApi.md#addVideoToPortfolio) | **PUT** /users/{user_id}/portfolios/{portfolio_id}/videos/{video_id} | Add a video to a portfolio
[**addVideoToPortfolioAlt1**](PortfoliosVideosApi.md#addVideoToPortfolioAlt1) | **PUT** /me/portfolios/{portfolio_id}/videos/{video_id} | Add a video to a portfolio
[**deleteVideoFromPortfolio**](PortfoliosVideosApi.md#deleteVideoFromPortfolio) | **DELETE** /users/{user_id}/portfolios/{portfolio_id}/videos/{video_id} | Remove a video from a portfolio
[**deleteVideoFromPortfolioAlt1**](PortfoliosVideosApi.md#deleteVideoFromPortfolioAlt1) | **DELETE** /me/portfolios/{portfolio_id}/videos/{video_id} | Remove a video from a portfolio
[**getPortfolioVideo**](PortfoliosVideosApi.md#getPortfolioVideo) | **GET** /users/{user_id}/portfolios/{portfolio_id}/videos/{video_id} | Get a specific video in a portfolio
[**getPortfolioVideoAlt1**](PortfoliosVideosApi.md#getPortfolioVideoAlt1) | **GET** /me/portfolios/{portfolio_id}/videos/{video_id} | Get a specific video in a portfolio
[**getPortfolioVideos**](PortfoliosVideosApi.md#getPortfolioVideos) | **GET** /users/{user_id}/portfolios/{portfolio_id}/videos | Get all the videos in a portfolio
[**getPortfolioVideosAlt1**](PortfoliosVideosApi.md#getPortfolioVideosAlt1) | **GET** /me/portfolios/{portfolio_id}/videos | Get all the videos in a portfolio



## addVideoToPortfolio

> addVideoToPortfolio(portfolioId, userId, videoId)

Add a video to a portfolio

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.PortfoliosVideosApi();
let portfolioId = 12345; // Number | The ID of the portfolio.
let userId = 152184; // Number | The ID of the user.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.addVideoToPortfolio(portfolioId, userId, videoId, (error, data, response) => {
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
 **portfolioId** | **Number**| The ID of the portfolio. | 
 **userId** | **Number**| The ID of the user. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addVideoToPortfolioAlt1

> addVideoToPortfolioAlt1(portfolioId, videoId)

Add a video to a portfolio

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.PortfoliosVideosApi();
let portfolioId = 12345; // Number | The ID of the portfolio.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.addVideoToPortfolioAlt1(portfolioId, videoId, (error, data, response) => {
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
 **portfolioId** | **Number**| The ID of the portfolio. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVideoFromPortfolio

> deleteVideoFromPortfolio(portfolioId, userId, videoId)

Remove a video from a portfolio

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.PortfoliosVideosApi();
let portfolioId = 12345; // Number | The ID of the portfolio.
let userId = 152184; // Number | The ID of the user.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.deleteVideoFromPortfolio(portfolioId, userId, videoId, (error, data, response) => {
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
 **portfolioId** | **Number**| The ID of the portfolio. | 
 **userId** | **Number**| The ID of the user. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVideoFromPortfolioAlt1

> deleteVideoFromPortfolioAlt1(portfolioId, videoId)

Remove a video from a portfolio

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.PortfoliosVideosApi();
let portfolioId = 12345; // Number | The ID of the portfolio.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.deleteVideoFromPortfolioAlt1(portfolioId, videoId, (error, data, response) => {
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
 **portfolioId** | **Number**| The ID of the portfolio. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPortfolioVideo

> Video getPortfolioVideo(portfolioId, userId, videoId)

Get a specific video in a portfolio

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.PortfoliosVideosApi();
let portfolioId = 12345; // Number | The ID of the portfolio.
let userId = 152184; // Number | The ID of the user.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.getPortfolioVideo(portfolioId, userId, videoId, (error, data, response) => {
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
 **portfolioId** | **Number**| The ID of the portfolio. | 
 **userId** | **Number**| The ID of the user. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

[**Video**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.video+json


## getPortfolioVideoAlt1

> Video getPortfolioVideoAlt1(portfolioId, videoId)

Get a specific video in a portfolio

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.PortfoliosVideosApi();
let portfolioId = 12345; // Number | The ID of the portfolio.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.getPortfolioVideoAlt1(portfolioId, videoId, (error, data, response) => {
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
 **portfolioId** | **Number**| The ID of the portfolio. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

[**Video**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.video+json


## getPortfolioVideos

> [Video] getPortfolioVideos(portfolioId, userId, opts)

Get all the videos in a portfolio

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.PortfoliosVideosApi();
let portfolioId = 12345; // Number | The ID of the portfolio.
let userId = 152184; // Number | The ID of the user.
let opts = {
  'containingUri': "/videos/258684937", // String | The page that contains the video URI.
  'filter': "filter_example", // String | The attribute by which to filter the results.
  'filterEmbeddable': true, // Boolean | Whether to filter the results by embeddable videos (`true`) or non-embeddable videos (`false`). Required only if **filter** is `embeddable`.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'sort': "sort_example" // String | The way to sort the results.  Option descriptions:  * `default` - This will sort to the default sort set on the portfolio. 
};
apiInstance.getPortfolioVideos(portfolioId, userId, opts, (error, data, response) => {
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
 **portfolioId** | **Number**| The ID of the portfolio. | 
 **userId** | **Number**| The ID of the user. | 
 **containingUri** | **String**| The page that contains the video URI. | [optional] 
 **filter** | **String**| The attribute by which to filter the results. | [optional] 
 **filterEmbeddable** | **Boolean**| Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 
 **sort** | **String**| The way to sort the results.  Option descriptions:  * &#x60;default&#x60; - This will sort to the default sort set on the portfolio.  | [optional] 

### Return type

[**[Video]**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.video+json


## getPortfolioVideosAlt1

> [Video] getPortfolioVideosAlt1(portfolioId, opts)

Get all the videos in a portfolio

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.PortfoliosVideosApi();
let portfolioId = 12345; // Number | The ID of the portfolio.
let opts = {
  'containingUri': "/videos/258684937", // String | The page that contains the video URI.
  'filter': "filter_example", // String | The attribute by which to filter the results.
  'filterEmbeddable': true, // Boolean | Whether to filter the results by embeddable videos (`true`) or non-embeddable videos (`false`). Required only if **filter** is `embeddable`.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'sort': "sort_example" // String | The way to sort the results.  Option descriptions:  * `default` - This will sort to the default sort set on the portfolio. 
};
apiInstance.getPortfolioVideosAlt1(portfolioId, opts, (error, data, response) => {
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
 **portfolioId** | **Number**| The ID of the portfolio. | 
 **containingUri** | **String**| The page that contains the video URI. | [optional] 
 **filter** | **String**| The attribute by which to filter the results. | [optional] 
 **filterEmbeddable** | **Boolean**| Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 
 **sort** | **String**| The way to sort the results.  Option descriptions:  * &#x60;default&#x60; - This will sort to the default sort set on the portfolio.  | [optional] 

### Return type

[**[Video]**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.video+json

