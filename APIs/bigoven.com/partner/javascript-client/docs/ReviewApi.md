# 1000000RecipeAndGroceryListApiV2.ReviewApi

All URIs are relative to *https://api2.bigoven.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recipeRecipeIdReviewGet**](ReviewApi.md#recipeRecipeIdReviewGet) | **GET** /recipe/{recipeId}/review | Get *my* review for the recipe {recipeId}, where \&quot;me\&quot; is determined by standard authentication headers
[**recipeReviewReviewIdGet**](ReviewApi.md#recipeReviewReviewIdGet) | **GET** /recipe/review/{reviewId} | Get a given review by string-style ID. This will return a payload with FeaturedReply, ReplyCount.              Recommended display is to list top-level reviews with one featured reply underneath.               Currently, the FeaturedReply is the most recent one for that rating.
[**reviewDelete**](ReviewApi.md#reviewDelete) | **DELETE** /recipe/{recipeId}/review/{reviewId} | DEPRECATED! - Deletes a review by recipeId and reviewId. Please use recipe/review/{reviewId} instead.
[**reviewDeleteReply**](ReviewApi.md#reviewDeleteReply) | **DELETE** /recipe/review/replies/{replyId} | DELETE a reply to a given review. Authenticated user must be the one who originally posted the reply.
[**reviewGet**](ReviewApi.md#reviewGet) | **GET** /recipe/{recipeId}/review/{reviewId} | Get a given review - DEPRECATED. See recipe/review/{reviewId} for the current usage.              Beginning in January 2017, BigOven moded from an integer-based ID system to a GUID-style string-based ID system for reviews and replies.              We are also supporting more of a \&quot;Google Play\&quot; style model for Reviews and Replies. That is, there are top-level Reviews and then              an unlimited list of replies (which do not carry star ratings) underneath existing reviews. Also, a given user can only have one review               per recipe. Existing legacy endpoints will continue to work, but we strongly recommend you migrate to using the newer endpoints listed              which do NOT carry the \&quot;DEPRECATED\&quot; flag.
[**reviewGetReplies**](ReviewApi.md#reviewGetReplies) | **GET** /recipe/review/{reviewId}/replies | Get a paged list of replies for a given review.
[**reviewGetReviews**](ReviewApi.md#reviewGetReviews) | **GET** /recipe/{recipeId}/reviews | Get paged list of reviews for a recipe. Each review will have at most one FeaturedReply, as well as a ReplyCount.
[**reviewPost**](ReviewApi.md#reviewPost) | **POST** /recipe/{recipeId}/review | Add a new review. Only one review can be provided per {userId, recipeId} pair. Otherwise your review will be updated.
[**reviewPostReply**](ReviewApi.md#reviewPostReply) | **POST** /recipe/review/{reviewId}/replies | POST a reply to a given review. The date will be set by server. Note that replies no longer have star ratings, only top-level reviews do.
[**reviewPut**](ReviewApi.md#reviewPut) | **PUT** /recipe/review/{reviewId} | Update a given top-level review.
[**reviewPutLegacy**](ReviewApi.md#reviewPutLegacy) | **PUT** /recipe/{recipeId}/review/{reviewId} | HTTP PUT (update) a recipe review. DEPRECATED. Please see recipe/review/{reviewId} PUT for the new endpoint.              We are moving to a string-based primary key system, no longer integers, for reviews and replies.
[**reviewPutReply**](ReviewApi.md#reviewPutReply) | **PUT** /recipe/review/replies/{replyId} | Update (PUT) a reply to a given review. Authenticated user must be the original one that posted the reply.



## recipeRecipeIdReviewGet

> BigOvenModelAPIReview recipeRecipeIdReviewGet(recipeId)

Get *my* review for the recipe {recipeId}, where \&quot;me\&quot; is determined by standard authentication headers

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.ReviewApi();
let recipeId = 56; // Number | 
apiInstance.recipeRecipeIdReviewGet(recipeId, (error, data, response) => {
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
 **recipeId** | **Number**|  | 

### Return type

[**BigOvenModelAPIReview**](BigOvenModelAPIReview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## recipeReviewReviewIdGet

> BigOvenModelAPIReview recipeReviewReviewIdGet(reviewId)

Get a given review by string-style ID. This will return a payload with FeaturedReply, ReplyCount.              Recommended display is to list top-level reviews with one featured reply underneath.               Currently, the FeaturedReply is the most recent one for that rating.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.ReviewApi();
let reviewId = "reviewId_example"; // String | 
apiInstance.recipeReviewReviewIdGet(reviewId, (error, data, response) => {
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
 **reviewId** | **String**|  | 

### Return type

[**BigOvenModelAPIReview**](BigOvenModelAPIReview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## reviewDelete

> Object reviewDelete(recipeId, reviewId)

DEPRECATED! - Deletes a review by recipeId and reviewId. Please use recipe/review/{reviewId} instead.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.ReviewApi();
let recipeId = 56; // Number | 
let reviewId = 789; // Number | 
apiInstance.reviewDelete(recipeId, reviewId, (error, data, response) => {
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
 **recipeId** | **Number**|  | 
 **reviewId** | **Number**|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## reviewDeleteReply

> Object reviewDeleteReply(replyId)

DELETE a reply to a given review. Authenticated user must be the one who originally posted the reply.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.ReviewApi();
let replyId = "replyId_example"; // String | 
apiInstance.reviewDeleteReply(replyId, (error, data, response) => {
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
 **replyId** | **String**|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## reviewGet

> BigOvenModelAPIReview reviewGet(reviewId, recipeId)

Get a given review - DEPRECATED. See recipe/review/{reviewId} for the current usage.              Beginning in January 2017, BigOven moded from an integer-based ID system to a GUID-style string-based ID system for reviews and replies.              We are also supporting more of a \&quot;Google Play\&quot; style model for Reviews and Replies. That is, there are top-level Reviews and then              an unlimited list of replies (which do not carry star ratings) underneath existing reviews. Also, a given user can only have one review               per recipe. Existing legacy endpoints will continue to work, but we strongly recommend you migrate to using the newer endpoints listed              which do NOT carry the \&quot;DEPRECATED\&quot; flag.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.ReviewApi();
let reviewId = 56; // Number | int
let recipeId = 56; // Number | int
apiInstance.reviewGet(reviewId, recipeId, (error, data, response) => {
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
 **reviewId** | **Number**| int | 
 **recipeId** | **Number**| int | 

### Return type

[**BigOvenModelAPIReview**](BigOvenModelAPIReview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## reviewGetReplies

> [BigOvenModelAPIReply] reviewGetReplies(reviewId, opts)

Get a paged list of replies for a given review.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.ReviewApi();
let reviewId = "reviewId_example"; // String | 
let opts = {
  'pg': 56, // Number | the page (int), starting with 1
  'rpp': 56 // Number | results per page (int)
};
apiInstance.reviewGetReplies(reviewId, opts, (error, data, response) => {
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
 **reviewId** | **String**|  | 
 **pg** | **Number**| the page (int), starting with 1 | [optional] 
 **rpp** | **Number**| results per page (int) | [optional] 

### Return type

[**[BigOvenModelAPIReply]**](BigOvenModelAPIReply.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## reviewGetReviews

> [BigOvenModelAPIReview] reviewGetReviews(recipeId, opts)

Get paged list of reviews for a recipe. Each review will have at most one FeaturedReply, as well as a ReplyCount.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.ReviewApi();
let recipeId = 56; // Number | recipe id (int)
let opts = {
  'pg': 56, // Number | the page (int), starting with 1
  'rpp': 56 // Number | results per page (int)
};
apiInstance.reviewGetReviews(recipeId, opts, (error, data, response) => {
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
 **recipeId** | **Number**| recipe id (int) | 
 **pg** | **Number**| the page (int), starting with 1 | [optional] 
 **rpp** | **Number**| results per page (int) | [optional] 

### Return type

[**[BigOvenModelAPIReview]**](BigOvenModelAPIReview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## reviewPost

> Object reviewPost(recipeId, aPI2ControllersWebAPIReviewControllerReviewRequest)

Add a new review. Only one review can be provided per {userId, recipeId} pair. Otherwise your review will be updated.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.ReviewApi();
let recipeId = 56; // Number | 
let aPI2ControllersWebAPIReviewControllerReviewRequest = new 1000000RecipeAndGroceryListApiV2.API2ControllersWebAPIReviewControllerReviewRequest(); // API2ControllersWebAPIReviewControllerReviewRequest | 
apiInstance.reviewPost(recipeId, aPI2ControllersWebAPIReviewControllerReviewRequest, (error, data, response) => {
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
 **recipeId** | **Number**|  | 
 **aPI2ControllersWebAPIReviewControllerReviewRequest** | [**API2ControllersWebAPIReviewControllerReviewRequest**](API2ControllersWebAPIReviewControllerReviewRequest.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## reviewPostReply

> BigOvenModelAPIReply reviewPostReply(reviewId, aPI2ControllersWebAPIReviewControllerPostReplyReq)

POST a reply to a given review. The date will be set by server. Note that replies no longer have star ratings, only top-level reviews do.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.ReviewApi();
let reviewId = "reviewId_example"; // String | 
let aPI2ControllersWebAPIReviewControllerPostReplyReq = new 1000000RecipeAndGroceryListApiV2.API2ControllersWebAPIReviewControllerPostReplyReq(); // API2ControllersWebAPIReviewControllerPostReplyReq | 
apiInstance.reviewPostReply(reviewId, aPI2ControllersWebAPIReviewControllerPostReplyReq, (error, data, response) => {
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
 **reviewId** | **String**|  | 
 **aPI2ControllersWebAPIReviewControllerPostReplyReq** | [**API2ControllersWebAPIReviewControllerPostReplyReq**](API2ControllersWebAPIReviewControllerPostReplyReq.md)|  | 

### Return type

[**BigOvenModelAPIReply**](BigOvenModelAPIReply.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## reviewPut

> BigOvenModelAPIReview reviewPut(reviewId, aPI2ControllersWebAPIReviewControllerReviewRequest)

Update a given top-level review.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.ReviewApi();
let reviewId = "reviewId_example"; // String | 
let aPI2ControllersWebAPIReviewControllerReviewRequest = new 1000000RecipeAndGroceryListApiV2.API2ControllersWebAPIReviewControllerReviewRequest(); // API2ControllersWebAPIReviewControllerReviewRequest | 
apiInstance.reviewPut(reviewId, aPI2ControllersWebAPIReviewControllerReviewRequest, (error, data, response) => {
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
 **reviewId** | **String**|  | 
 **aPI2ControllersWebAPIReviewControllerReviewRequest** | [**API2ControllersWebAPIReviewControllerReviewRequest**](API2ControllersWebAPIReviewControllerReviewRequest.md)|  | 

### Return type

[**BigOvenModelAPIReview**](BigOvenModelAPIReview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## reviewPutLegacy

> BigOvenModelAPIReview reviewPutLegacy(reviewId, recipeId, aPI2ControllersWebAPIReviewControllerReviewRequestLegacy)

HTTP PUT (update) a recipe review. DEPRECATED. Please see recipe/review/{reviewId} PUT for the new endpoint.              We are moving to a string-based primary key system, no longer integers, for reviews and replies.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.ReviewApi();
let reviewId = 56; // Number | reviewId (int)
let recipeId = 56; // Number | recipeId (int)
let aPI2ControllersWebAPIReviewControllerReviewRequestLegacy = new 1000000RecipeAndGroceryListApiV2.API2ControllersWebAPIReviewControllerReviewRequestLegacy(); // API2ControllersWebAPIReviewControllerReviewRequestLegacy | 
apiInstance.reviewPutLegacy(reviewId, recipeId, aPI2ControllersWebAPIReviewControllerReviewRequestLegacy, (error, data, response) => {
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
 **reviewId** | **Number**| reviewId (int) | 
 **recipeId** | **Number**| recipeId (int) | 
 **aPI2ControllersWebAPIReviewControllerReviewRequestLegacy** | [**API2ControllersWebAPIReviewControllerReviewRequestLegacy**](API2ControllersWebAPIReviewControllerReviewRequestLegacy.md)|  | 

### Return type

[**BigOvenModelAPIReview**](BigOvenModelAPIReview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## reviewPutReply

> BigOvenModelAPIReply reviewPutReply(replyId, aPI2ControllersWebAPIReviewControllerPostReplyReq)

Update (PUT) a reply to a given review. Authenticated user must be the original one that posted the reply.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.ReviewApi();
let replyId = "replyId_example"; // String | 
let aPI2ControllersWebAPIReviewControllerPostReplyReq = new 1000000RecipeAndGroceryListApiV2.API2ControllersWebAPIReviewControllerPostReplyReq(); // API2ControllersWebAPIReviewControllerPostReplyReq | 
apiInstance.reviewPutReply(replyId, aPI2ControllersWebAPIReviewControllerPostReplyReq, (error, data, response) => {
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
 **replyId** | **String**|  | 
 **aPI2ControllersWebAPIReviewControllerPostReplyReq** | [**API2ControllersWebAPIReviewControllerPostReplyReq**](API2ControllersWebAPIReviewControllerPostReplyReq.md)|  | 

### Return type

[**BigOvenModelAPIReply**](BigOvenModelAPIReply.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

