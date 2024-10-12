# MovieReviewsApi.DefaultApi

All URIs are relative to *http://api.nytimes.com/svc/movies/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**criticsResourceTypeJsonGet**](DefaultApi.md#criticsResourceTypeJsonGet) | **GET** /critics/{resource-type}.json | 
[**reviewsResourceTypeJsonGet**](DefaultApi.md#reviewsResourceTypeJsonGet) | **GET** /reviews/{resource-type}.json | 
[**reviewsSearchJsonGet**](DefaultApi.md#reviewsSearchJsonGet) | **GET** /reviews/search.json | 



## criticsResourceTypeJsonGet

> CriticsResourceTypeJsonGet200Response criticsResourceTypeJsonGet(resourceType)



### Example

```javascript
import MovieReviewsApi from 'movie_reviews_api';
let defaultClient = MovieReviewsApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new MovieReviewsApi.DefaultApi();
let resourceType = "resourceType_example"; // String | all | full-time | part-time | [reviewer-name]  Specify all to get all Times reviewers, or specify full-time or part-time to get that subset. Specify a reviewer's name to get details about a particular reviewer. 
apiInstance.criticsResourceTypeJsonGet(resourceType, (error, data, response) => {
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
 **resourceType** | **String**| all | full-time | part-time | [reviewer-name]  Specify all to get all Times reviewers, or specify full-time or part-time to get that subset. Specify a reviewer&#39;s name to get details about a particular reviewer.  | 

### Return type

[**CriticsResourceTypeJsonGet200Response**](CriticsResourceTypeJsonGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reviewsResourceTypeJsonGet

> ReviewsSearchJsonGet200Response reviewsResourceTypeJsonGet(resourceType, opts)



### Example

```javascript
import MovieReviewsApi from 'movie_reviews_api';
let defaultClient = MovieReviewsApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new MovieReviewsApi.DefaultApi();
let resourceType = "resourceType_example"; // String | Specify all to retrieve all reviews, including NYT Critics' Picks.  Specify picks to get NYT Critics' Picks currently in theaters.  
let opts = {
  'offset': 20, // Number | Positive integer, multiple of 20
  'order': "'by-publication-date'" // String | Sets the sort order of the results.  Results ordered by-title are in ascending alphabetical order. Results ordered by one of the date parameters are in reverse chronological order.  If you do not specify a sort order, the results will be ordered by publication-date. 
};
apiInstance.reviewsResourceTypeJsonGet(resourceType, opts, (error, data, response) => {
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
 **resourceType** | **String**| Specify all to retrieve all reviews, including NYT Critics&#39; Picks.  Specify picks to get NYT Critics&#39; Picks currently in theaters.   | 
 **offset** | **Number**| Positive integer, multiple of 20 | [optional] [default to 20]
 **order** | **String**| Sets the sort order of the results.  Results ordered by-title are in ascending alphabetical order. Results ordered by one of the date parameters are in reverse chronological order.  If you do not specify a sort order, the results will be ordered by publication-date.  | [optional] [default to &#39;by-publication-date&#39;]

### Return type

[**ReviewsSearchJsonGet200Response**](ReviewsSearchJsonGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reviewsSearchJsonGet

> ReviewsSearchJsonGet200Response reviewsSearchJsonGet(opts)



### Example

```javascript
import MovieReviewsApi from 'movie_reviews_api';
let defaultClient = MovieReviewsApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new MovieReviewsApi.DefaultApi();
let opts = {
  'query': "query_example", // String | Search keywords; matches movie title and indexed terms  To limit your search to exact matches only, surround your search string with single quotation marks (e.g., query='28+days+later'). Otherwise, responses will include partial matches (\"head words\") as well as exact matches (e.g., president will match president, presidents and presidential).      If you specify multiple terms without quotation marks, they will be combined in an OR search.      If you omit the query parameter, your request will be equivalent to a reviews and NYT Critics' Picks request. 
  'criticsPick': "criticsPick_example", // String | Set this parameter to Y to limit the results to NYT Critics' Picks. To get only those movies that have not been highlighted by Times critics, specify critics-pick=N. (To get all reviews regardless of critics-pick status, simply omit this parameter.) 
  'reviewer': "reviewer_example", // String | Include this parameter to limit your results to reviews by a specific critic. Reviewer names should be formatted like this: Manohla Dargis. 
  'publicationDate': "publicationDate_example", // String | Single date: YYYY-MM-DD  Start and end date: YYYY-MM-DD;YYYY-MM-DD  The publication-date is the date the review was first published in The Times. 
  'openingDate': "openingDate_example", // String | Single date: YYYY-MM-DD  Start and end date: YYYY-MM-DD;YYYY-MM-DD  The opening-date is the date the movie's opening date in the New York region. 
  'offset': 20, // Number | Positive integer, multiple of 20
  'order': "order_example" // String | Sets the sort order of the results.  Results ordered by-title are in ascending alphabetical order. Results ordered by one of the date parameters are in reverse chronological order.  If you do not specify a sort order, the results will be ordered by publication-date. 
};
apiInstance.reviewsSearchJsonGet(opts, (error, data, response) => {
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
 **query** | **String**| Search keywords; matches movie title and indexed terms  To limit your search to exact matches only, surround your search string with single quotation marks (e.g., query&#x3D;&#39;28+days+later&#39;). Otherwise, responses will include partial matches (\&quot;head words\&quot;) as well as exact matches (e.g., president will match president, presidents and presidential).      If you specify multiple terms without quotation marks, they will be combined in an OR search.      If you omit the query parameter, your request will be equivalent to a reviews and NYT Critics&#39; Picks request.  | [optional] 
 **criticsPick** | **String**| Set this parameter to Y to limit the results to NYT Critics&#39; Picks. To get only those movies that have not been highlighted by Times critics, specify critics-pick&#x3D;N. (To get all reviews regardless of critics-pick status, simply omit this parameter.)  | [optional] 
 **reviewer** | **String**| Include this parameter to limit your results to reviews by a specific critic. Reviewer names should be formatted like this: Manohla Dargis.  | [optional] 
 **publicationDate** | **String**| Single date: YYYY-MM-DD  Start and end date: YYYY-MM-DD;YYYY-MM-DD  The publication-date is the date the review was first published in The Times.  | [optional] 
 **openingDate** | **String**| Single date: YYYY-MM-DD  Start and end date: YYYY-MM-DD;YYYY-MM-DD  The opening-date is the date the movie&#39;s opening date in the New York region.  | [optional] 
 **offset** | **Number**| Positive integer, multiple of 20 | [optional] [default to 20]
 **order** | **String**| Sets the sort order of the results.  Results ordered by-title are in ascending alphabetical order. Results ordered by one of the date parameters are in reverse chronological order.  If you do not specify a sort order, the results will be ordered by publication-date.  | [optional] 

### Return type

[**ReviewsSearchJsonGet200Response**](ReviewsSearchJsonGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

