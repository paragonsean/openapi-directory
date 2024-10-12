# ReviewsAndRatingsApi.ReviewApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteMultipleReviews**](ReviewApi.md#deleteMultipleReviews) | **DELETE** /reviews | Delete Multiple Reviews
[**deleteReview**](ReviewApi.md#deleteReview) | **DELETE** /review/{reviewId} | Delete Review
[**editReview**](ReviewApi.md#editReview) | **PATCH** /review/{reviewId} | Update a Review
[**getReviewbyReviewId**](ReviewApi.md#getReviewbyReviewId) | **GET** /review/{reviewId} | Get Review by Review ID
[**getalistofReviews**](ReviewApi.md#getalistofReviews) | **GET** /reviews | Get a list of Reviews
[**saveMultipleReviews**](ReviewApi.md#saveMultipleReviews) | **POST** /reviews | Create Multiple Reviews
[**saveReview**](ReviewApi.md#saveReview) | **POST** /review | Create a Review



## deleteMultipleReviews

> Boolean deleteMultipleReviews(contentType, accept, opts)

Delete Multiple Reviews

Deletes multiple reviews at once.

### Example

```javascript
import ReviewsAndRatingsApi from 'reviews_and_ratings_api';
let defaultClient = ReviewsAndRatingsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new ReviewsAndRatingsApi.ReviewApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'requestBody': ["babefcf4-e0f7-11ec-835d-16c4e59c4351","qweqweee-e0f7-11ec-835d-16c4e59c4351","asdffggg-e0f7-11ec-835d-16c4e59c4351"] // [String] | 
};
apiInstance.deleteMultipleReviews(contentType, accept, opts, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **requestBody** | [**[String]**](String.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteReview

> Boolean deleteReview(reviewId, contentType, accept)

Delete Review

Deletes an existing review.

### Example

```javascript
import ReviewsAndRatingsApi from 'reviews_and_ratings_api';
let defaultClient = ReviewsAndRatingsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new ReviewsAndRatingsApi.ReviewApi();
let reviewId = "1"; // String | Review ID.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
apiInstance.deleteReview(reviewId, contentType, accept, (error, data, response) => {
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
 **reviewId** | **String**| Review ID. | 
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

**Boolean**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## editReview

> GetReviewbyReviewId200Response editReview(reviewId, contentType, accept, editReviewRequest)

Update a Review

Updates the information of a review.

### Example

```javascript
import ReviewsAndRatingsApi from 'reviews_and_ratings_api';
let defaultClient = ReviewsAndRatingsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new ReviewsAndRatingsApi.ReviewApi();
let reviewId = "5323fdaa-c012-11ec-835d-0ebee58edbb3"; // String | Review ID.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let editReviewRequest = new ReviewsAndRatingsApi.EditReviewRequest(); // EditReviewRequest | 
apiInstance.editReview(reviewId, contentType, accept, editReviewRequest, (error, data, response) => {
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
 **reviewId** | **String**| Review ID. | 
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **editReviewRequest** | [**EditReviewRequest**](EditReviewRequest.md)|  | 

### Return type

[**GetReviewbyReviewId200Response**](GetReviewbyReviewId200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getReviewbyReviewId

> GetReviewbyReviewId200Response getReviewbyReviewId(reviewId, contentType, accept)

Get Review by Review ID

Retrieves information of a product review by its ID.

### Example

```javascript
import ReviewsAndRatingsApi from 'reviews_and_ratings_api';
let defaultClient = ReviewsAndRatingsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new ReviewsAndRatingsApi.ReviewApi();
let reviewId = "1"; // String | Review ID.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
apiInstance.getReviewbyReviewId(reviewId, contentType, accept, (error, data, response) => {
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
 **reviewId** | **String**| Review ID. | 
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

[**GetReviewbyReviewId200Response**](GetReviewbyReviewId200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getalistofReviews

> GetalistofReviews200Response getalistofReviews(searchTerm, from, to, orderBy, status, productId, contentType, accept)

Get a list of Reviews

Retrieves a list of reviews.

### Example

```javascript
import ReviewsAndRatingsApi from 'reviews_and_ratings_api';
let defaultClient = ReviewsAndRatingsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new ReviewsAndRatingsApi.ReviewApi();
let searchTerm = "search_term"; // String | Returns Reviews that contain the search term in `productId`, `sku`, `shopperId`, or `reviewerName`.
let from = "0"; // String | Zero base starting record number, `0` is the default value.
let to = "3"; // String | Zero base ending record number, `3` is the default value.
let orderBy = ":asc"; // String | Case-sensitive fieldName to order records (optionally add `:asc` or `:desc`).
let status = true; // Boolean | Status of the review, approved (`true`) or not (`false`).
let productId = "1"; // String | Filter the reviews by product ID.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
apiInstance.getalistofReviews(searchTerm, from, to, orderBy, status, productId, contentType, accept, (error, data, response) => {
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
 **searchTerm** | **String**| Returns Reviews that contain the search term in &#x60;productId&#x60;, &#x60;sku&#x60;, &#x60;shopperId&#x60;, or &#x60;reviewerName&#x60;. | 
 **from** | **String**| Zero base starting record number, &#x60;0&#x60; is the default value. | 
 **to** | **String**| Zero base ending record number, &#x60;3&#x60; is the default value. | 
 **orderBy** | **String**| Case-sensitive fieldName to order records (optionally add &#x60;:asc&#x60; or &#x60;:desc&#x60;). | 
 **status** | **Boolean**| Status of the review, approved (&#x60;true&#x60;) or not (&#x60;false&#x60;). | 
 **productId** | **String**| Filter the reviews by product ID. | 
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

[**GetalistofReviews200Response**](GetalistofReviews200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## saveMultipleReviews

> [String] saveMultipleReviews(contentType, accept, saveMultipleReviewsRequest)

Create Multiple Reviews

Creates multiple reviews.

### Example

```javascript
import ReviewsAndRatingsApi from 'reviews_and_ratings_api';
let defaultClient = ReviewsAndRatingsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new ReviewsAndRatingsApi.ReviewApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let saveMultipleReviewsRequest = [{"approved":false,"productId":"1","rating":4,"reviewerName":"Arturo","text":"test multiple reviews","title":"test multiple reviews","verifiedPurchaser":false},{"approved":false,"productId":"2","rating":4,"reviewerName":"Arturo","text":"test review 2 multiple reviews","title":"test review 2 multiple reviews","verifiedPurchaser":false}]; // [SaveMultipleReviewsRequest] | 
apiInstance.saveMultipleReviews(contentType, accept, saveMultipleReviewsRequest, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **saveMultipleReviewsRequest** | [**[SaveMultipleReviewsRequest]**](SaveMultipleReviewsRequest.md)|  | 

### Return type

**[String]**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## saveReview

> SaveReview200Response saveReview(contentType, accept, saveReviewRequest)

Create a Review

Creates a single review

### Example

```javascript
import ReviewsAndRatingsApi from 'reviews_and_ratings_api';
let defaultClient = ReviewsAndRatingsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new ReviewsAndRatingsApi.ReviewApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let saveReviewRequest = {"productId":"65444","rating":5,"reviewerName":"Arturo","text":"It is the best product that I have seen","title":"Good Product"}; // SaveReviewRequest | 
apiInstance.saveReview(contentType, accept, saveReviewRequest, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **saveReviewRequest** | [**SaveReviewRequest**](SaveReviewRequest.md)|  | 

### Return type

[**SaveReview200Response**](SaveReview200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

