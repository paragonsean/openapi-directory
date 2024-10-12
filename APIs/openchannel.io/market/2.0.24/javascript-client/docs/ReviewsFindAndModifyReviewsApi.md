# OpenChannelMarketApi.ReviewsFindAndModifyReviewsApi

All URIs are relative to *https://market.openchannel.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reviewsGet**](ReviewsFindAndModifyReviewsApi.md#reviewsGet) | **GET** /reviews | Find reviews for a particular App and marketplace. Results are automatically paginated when limit is set
[**reviewsPost**](ReviewsFindAndModifyReviewsApi.md#reviewsPost) | **POST** /reviews | Post a review from a User and returns the new post
[**reviewsReviewIdDelete**](ReviewsFindAndModifyReviewsApi.md#reviewsReviewIdDelete) | **DELETE** /reviews/{reviewId} | Remove a review
[**reviewsReviewIdGet**](ReviewsFindAndModifyReviewsApi.md#reviewsReviewIdGet) | **GET** /reviews/{reviewId} | Find a Review within a particular App and marketplace
[**reviewsReviewIdPatch**](ReviewsFindAndModifyReviewsApi.md#reviewsReviewIdPatch) | **PATCH** /reviews/{reviewId} | Update a review fields
[**reviewsReviewIdPost**](ReviewsFindAndModifyReviewsApi.md#reviewsReviewIdPost) | **POST** /reviews/{reviewId} | Update a review from a User and returns the new post



## reviewsGet

> ReviewPages reviewsGet(opts)

Find reviews for a particular App and marketplace. Results are automatically paginated when limit is set

- Results are paginated and the default is value is 100 if no limit is provided 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.ReviewsFindAndModifyReviewsApi();
let opts = {
  'query': "query_example", // String | A query document. Example: {'rating': 500} matches all the reviews that have a rating of 500. 
  'sort': "sort_example", // String | A sort document. Example: {'rating':1} sorts the results by rating in ascending order
  'pageNumber': 56, // Number | The result set page number to be returned
  'limit': 56 // Number | The maximum number of results to return per page
};
apiInstance.reviewsGet(opts, (error, data, response) => {
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
 **query** | **String**| A query document. Example: {&#39;rating&#39;: 500} matches all the reviews that have a rating of 500.  | [optional] 
 **sort** | **String**| A sort document. Example: {&#39;rating&#39;:1} sorts the results by rating in ascending order | [optional] 
 **pageNumber** | **Number**| The result set page number to be returned | [optional] 
 **limit** | **Number**| The maximum number of results to return per page | [optional] 

### Return type

[**ReviewPages**](ReviewPages.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## reviewsPost

> Review reviewsPost(appId, userId, headline, rating, description, opts)

Post a review from a User and returns the new post

- Only authenticated users are able to post reviews - Returns the newly created review 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.ReviewsFindAndModifyReviewsApi();
let appId = "appId_example"; // String | The id of the App that will own this review
let userId = "userId_example"; // String | The id of the User that is posting this review
let headline = "headline_example"; // String | The review's headline. Limited to 50 characters.
let rating = 56; // Number | The rating given within this review. The rating is represented as an integer between 0 and 500 (0 - 5 stars)
let description = "description_example"; // String | The review's description. Limited to 2000 characters.
let opts = {
  'userAccountId': "userAccountId_example", // String | The id of the User account that is posting this review
  'type': "type_example", // String | The type for this review
  'mustOwnApp': true, // Boolean | True if a review can be created only by a user that has owned the app. The default is True.
  'autoApprove': true, // Boolean | True if the review should be automatically approved. The default is False.
  'customData': "customData_example" // String | A custom JSON object that you can create and attach to this record
};
apiInstance.reviewsPost(appId, userId, headline, rating, description, opts, (error, data, response) => {
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
 **appId** | **String**| The id of the App that will own this review | 
 **userId** | **String**| The id of the User that is posting this review | 
 **headline** | **String**| The review&#39;s headline. Limited to 50 characters. | 
 **rating** | **Number**| The rating given within this review. The rating is represented as an integer between 0 and 500 (0 - 5 stars) | 
 **description** | **String**| The review&#39;s description. Limited to 2000 characters. | 
 **userAccountId** | **String**| The id of the User account that is posting this review | [optional] 
 **type** | **String**| The type for this review | [optional] 
 **mustOwnApp** | **Boolean**| True if a review can be created only by a user that has owned the app. The default is True. | [optional] 
 **autoApprove** | **Boolean**| True if the review should be automatically approved. The default is False. | [optional] 
 **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] 

### Return type

[**Review**](Review.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## reviewsReviewIdDelete

> reviewsReviewIdDelete(reviewId, userId, opts)

Remove a review

- Only the review author is able to remove their review 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.ReviewsFindAndModifyReviewsApi();
let reviewId = "reviewId_example"; // String | The id of the Review to be updated
let userId = "userId_example"; // String | The id of the User that is removing this review
let opts = {
  'userAccountId': "userAccountId_example" // String | The id of the User account that is emoving this review
};
apiInstance.reviewsReviewIdDelete(reviewId, userId, opts, (error, data, response) => {
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
 **reviewId** | **String**| The id of the Review to be updated | 
 **userId** | **String**| The id of the User that is removing this review | 
 **userAccountId** | **String**| The id of the User account that is emoving this review | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## reviewsReviewIdGet

> Review reviewsReviewIdGet(reviewId)

Find a Review within a particular App and marketplace

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.ReviewsFindAndModifyReviewsApi();
let reviewId = "reviewId_example"; // String | The id of the review to be located
apiInstance.reviewsReviewIdGet(reviewId, (error, data, response) => {
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
 **reviewId** | **String**| The id of the review to be located | 

### Return type

[**Review**](Review.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## reviewsReviewIdPatch

> Review reviewsReviewIdPatch(reviewId, userId, opts)

Update a review fields

- Only the review author is able to update their review - Returns the newly updated review 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.ReviewsFindAndModifyReviewsApi();
let reviewId = "reviewId_example"; // String | The id of the Review to be updated
let userId = "userId_example"; // String | The id of the User that is updating this review
let opts = {
  'userAccountId': "userAccountId_example", // String | The id of the User account that is posting this review
  'headline': "headline_example", // String | The review's headline. Limited to 50 characters.
  'rating': 56, // Number | The rating given within this review. The rating is represented as an integer between 0 and 500 (0 - 5 stars)
  'description': "description_example", // String | The review's description. Limited to 2000 characters.
  'customData': "customData_example" // String | A custom JSON object that you can create and attach to this record
};
apiInstance.reviewsReviewIdPatch(reviewId, userId, opts, (error, data, response) => {
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
 **reviewId** | **String**| The id of the Review to be updated | 
 **userId** | **String**| The id of the User that is updating this review | 
 **userAccountId** | **String**| The id of the User account that is posting this review | [optional] 
 **headline** | **String**| The review&#39;s headline. Limited to 50 characters. | [optional] 
 **rating** | **Number**| The rating given within this review. The rating is represented as an integer between 0 and 500 (0 - 5 stars) | [optional] 
 **description** | **String**| The review&#39;s description. Limited to 2000 characters. | [optional] 
 **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] 

### Return type

[**Review**](Review.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## reviewsReviewIdPost

> Review reviewsReviewIdPost(reviewId, userId, userAccountId, headline, rating, description, opts)

Update a review from a User and returns the new post

- Only the review author is able to update their review - Returns the newly updated review 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.ReviewsFindAndModifyReviewsApi();
let reviewId = "reviewId_example"; // String | The id of the Review to be updated
let userId = "userId_example"; // String | The id of the User that is updating this review
let userAccountId = "userAccountId_example"; // String | The id of the User account that is posting this review
let headline = "headline_example"; // String | The review's headline. Limited to 50 characters.
let rating = 56; // Number | The rating given within this review. The rating is represented as an integer between 0 and 500 (0 - 5 stars)
let description = "description_example"; // String | The review's description. Limited to 2000 characters.
let opts = {
  'customData': "customData_example" // String | A custom JSON object that you can create and attach to this record
};
apiInstance.reviewsReviewIdPost(reviewId, userId, userAccountId, headline, rating, description, opts, (error, data, response) => {
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
 **reviewId** | **String**| The id of the Review to be updated | 
 **userId** | **String**| The id of the User that is updating this review | 
 **userAccountId** | **String**| The id of the User account that is posting this review | 
 **headline** | **String**| The review&#39;s headline. Limited to 50 characters. | 
 **rating** | **Number**| The rating given within this review. The rating is represented as an integer between 0 and 500 (0 - 5 stars) | 
 **description** | **String**| The review&#39;s description. Limited to 2000 characters. | 
 **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] 

### Return type

[**Review**](Review.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

