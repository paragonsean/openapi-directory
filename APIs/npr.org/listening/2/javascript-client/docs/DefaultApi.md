# NprListeningService.DefaultApi

All URIs are relative to *https://listening.api.npr.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAggRecommendations**](DefaultApi.md#getAggRecommendations) | **GET** /v2/aggregation/{aggId}/recommendations | Get a set of recommendations for an aggregation independent of the user&#39;s listening history
[**getChannels**](DefaultApi.md#getChannels) | **GET** /v2/channels | Get the list of available channels
[**getHistory**](DefaultApi.md#getHistory) | **GET** /v2/history | Get recent ratings the logged-in user has submitted
[**getOrganizationCategory**](DefaultApi.md#getOrganizationCategory) | **GET** /v2/organizations/{orgId}/categories/{category}/recommendations | Get a list of recommendations from a category of content from an organization
[**getOrganizationOverview**](DefaultApi.md#getOrganizationOverview) | **GET** /v2/organizations/{orgId}/recommendations | Get a variety of details about an organization including various lists of recent audio items
[**getPromo**](DefaultApi.md#getPromo) | **GET** /v2/promo/recommendations | Retrieve the most recent promo audio heard by the logged-in user
[**getRecommendations**](DefaultApi.md#getRecommendations) | **GET** /v2/recommendations | Get a list of media for the logged-in user from NPR&#39;s recommendation engine
[**getSearchRecommendations**](DefaultApi.md#getSearchRecommendations) | **GET** /v2/search/recommendations | Get a list of recent audio and aggregation items associated with search terms
[**postRating**](DefaultApi.md#postRating) | **POST** /v2/ratings | Collect new ratings for media previously recommended to the logged-in user



## getAggRecommendations

> AggregationAudioItemListDocument getAggRecommendations(aggId, authorization, opts)

Get a set of recommendations for an aggregation independent of the user&#39;s listening history

This endpoint provides a list of recent audio items associated with the aggregation along with metadata about the aggregation.

### Example

```javascript
import NprListeningService from 'npr_listening_service';
let defaultClient = NprListeningService.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NprListeningService.DefaultApi();
let aggId = 789; // Number | ID of an aggregation such as a program or podcast. If the specified ID is a program that publishes rundowns, the latest rundown will be returned.
let authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
let opts = {
  'startNum': 0 // Number | The result to start with. Allows paging through the episodes of a podcast or program, with the default, `startNum=0`, being the most recent episode. Ignored for programs that publish a rundown.
};
apiInstance.getAggRecommendations(aggId, authorization, opts, (error, data, response) => {
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
 **aggId** | **Number**| ID of an aggregation such as a program or podcast. If the specified ID is a program that publishes rundowns, the latest rundown will be returned. | 
 **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | 
 **startNum** | **Number**| The result to start with. Allows paging through the episodes of a podcast or program, with the default, &#x60;startNum&#x3D;0&#x60;, being the most recent episode. Ignored for programs that publish a rundown. | [optional] [default to 0]

### Return type

[**AggregationAudioItemListDocument**](AggregationAudioItemListDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.collection.doc+json


## getChannels

> ChannelsDocument getChannels(authorization, opts)

Get the list of available channels

These channels allow the user to specify a focus for the content returned in the recommendations endpoint.

### Example

```javascript
import NprListeningService from 'npr_listening_service';
let defaultClient = NprListeningService.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NprListeningService.DefaultApi();
let authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
let opts = {
  'exploreOnly': false // Boolean | If set to `true`, this call will return only channels that should be shown in the client's `Explore` view
};
apiInstance.getChannels(authorization, opts, (error, data, response) => {
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
 **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | 
 **exploreOnly** | **Boolean**| If set to &#x60;true&#x60;, this call will return only channels that should be shown in the client&#39;s &#x60;Explore&#x60; view | [optional] [default to false]

### Return type

[**ChannelsDocument**](ChannelsDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.collection.doc+json


## getHistory

> AudioItemListDocument getHistory(authorization)

Get recent ratings the logged-in user has submitted

This endpoint provides the list of recently-rated audio recommendations that the logged-in user has consumed. Some rated recommendations are filtered, such as sponsorship and donation.

### Example

```javascript
import NprListeningService from 'npr_listening_service';
let defaultClient = NprListeningService.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NprListeningService.DefaultApi();
let authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
apiInstance.getHistory(authorization, (error, data, response) => {
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
 **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | 

### Return type

[**AudioItemListDocument**](AudioItemListDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.collection.doc+json


## getOrganizationCategory

> OrganizationCategoryAudioListDocument getOrganizationCategory(orgId, category, authorization)

Get a list of recommendations from a category of content from an organization

This endpoint provides a list of recommendations from a category of content from  an organization.

### Example

```javascript
import NprListeningService from 'npr_listening_service';
let defaultClient = NprListeningService.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NprListeningService.DefaultApi();
let orgId = 789; // Number | ID of an organization, such as an NPR One station
let category = "'story'"; // String | One of the three categories of content - newscast, story, or podcast
let authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
apiInstance.getOrganizationCategory(orgId, category, authorization, (error, data, response) => {
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
 **orgId** | **Number**| ID of an organization, such as an NPR One station | 
 **category** | **String**| One of the three categories of content - newscast, story, or podcast | [default to &#39;story&#39;]
 **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | 

### Return type

[**OrganizationCategoryAudioListDocument**](OrganizationCategoryAudioListDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.collection.doc+json


## getOrganizationOverview

> OrganizationOverviewDocument getOrganizationOverview(orgId, authorization)

Get a variety of details about an organization including various lists of recent audio items

This endpoint provides a variety of details about an organization including various lists of recent audio items.

### Example

```javascript
import NprListeningService from 'npr_listening_service';
let defaultClient = NprListeningService.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NprListeningService.DefaultApi();
let orgId = 789; // Number | ID of an organization, such as an NPR One station
let authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
apiInstance.getOrganizationOverview(orgId, authorization, (error, data, response) => {
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
 **orgId** | **Number**| ID of an organization, such as an NPR One station | 
 **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | 

### Return type

[**OrganizationOverviewDocument**](OrganizationOverviewDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.collection.doc+json


## getPromo

> AudioItemListDocument getPromo(authorization)

Retrieve the most recent promo audio heard by the logged-in user

Gets the most recently played promo for which the user has neither tapped through the promo or listened to the target story.

### Example

```javascript
import NprListeningService from 'npr_listening_service';
let defaultClient = NprListeningService.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NprListeningService.DefaultApi();
let authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
apiInstance.getPromo(authorization, (error, data, response) => {
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
 **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | 

### Return type

[**AudioItemListDocument**](AudioItemListDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.collection.doc+json


## getRecommendations

> AudioItemListDocument getRecommendations(authorization, opts)

Get a list of media for the logged-in user from NPR&#39;s recommendation engine

This endpoint returns a list of audio recommendations. It is designed to be used for an initial list of recommendations, and then &#x60;POST /v2/ratings?recommend&#x3D;true&#x60; should be used for subsequent requests for recommendations.  A fully-populated link to the ratings endpoint is returned with each individual recommendation and is located in the AudioItemDocument under the &#x60;links[&#39;recommendations&#39;]&#x60; object. The query parameters in this link should not be modified. Be sure to copy and send back the entire ratings object (RatingData), as new fields may be added to it in the future.  A 500 will be returned if there are no eligible remaining recommendations.

### Example

```javascript
import NprListeningService from 'npr_listening_service';
let defaultClient = NprListeningService.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NprListeningService.DefaultApi();
let authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
let opts = {
  'xAdvertisingID': "xAdvertisingID_example", // String | A device-specific advertising identifier, if possible. Apple's IDFA is an example.
  'channel': "'npr'", // String | Determines the focus of the recommendations returned. Channel `npr` is recommended for most use cases.
  'sharedMediaId': "sharedMediaId_example", // String | This media was shared directly with the user; if provided, the service will add this recommendation to the top of the list
  'notifiedMediaId': "notifiedMediaId_example" // String | The user received a push notification about this media; if provided, the service will add this recommendation to the top of the list
};
apiInstance.getRecommendations(authorization, opts, (error, data, response) => {
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
 **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | 
 **xAdvertisingID** | **String**| A device-specific advertising identifier, if possible. Apple&#39;s IDFA is an example. | [optional] 
 **channel** | **String**| Determines the focus of the recommendations returned. Channel &#x60;npr&#x60; is recommended for most use cases. | [optional] [default to &#39;npr&#39;]
 **sharedMediaId** | **String**| This media was shared directly with the user; if provided, the service will add this recommendation to the top of the list | [optional] 
 **notifiedMediaId** | **String**| The user received a push notification about this media; if provided, the service will add this recommendation to the top of the list | [optional] 

### Return type

[**AudioItemListDocument**](AudioItemListDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.collection.doc+json


## getSearchRecommendations

> SearchListDocument getSearchRecommendations(authorization, searchTerms)

Get a list of recent audio and aggregation items associated with search terms

In the schema shown below, SearchItemDocument is not an actual type of returned object; the object returned by a search will be either an AggregationAudioItemListDocument or an AudioItemDocument.

### Example

```javascript
import NprListeningService from 'npr_listening_service';
let defaultClient = NprListeningService.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NprListeningService.DefaultApi();
let authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
let searchTerms = "searchTerms_example"; // String | Search terms to search on; can include URL-encoded punctuation
apiInstance.getSearchRecommendations(authorization, searchTerms, (error, data, response) => {
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
 **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | 
 **searchTerms** | **String**| Search terms to search on; can include URL-encoded punctuation | 

### Return type

[**SearchListDocument**](SearchListDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.collection.doc+json


## postRating

> AudioItemListDocument postRating(authorization, body, opts)

Collect new ratings for media previously recommended to the logged-in user

This endpoint is the main mechanism for providing feedback from the user to NPR about the recommendations that are obtained from &#x60;GET /listening/v2/recommendations&#x60;.  A fully-populated link to this endpoint is returned with each individual recommendation and is located in the AudioItemDocument under the &#x60;links[&#39;recommendations&#39;]&#x60; object. The query parameters in this link should not be modified. Be sure to copy and send back the entire ratings object (RatingData), as new fields may be added to it in the future.  This endpoint can return a blank JSON.doc or AudioItemDocument depending on the &#x60;recommend&#x3D;true|false&#x60; parameter. The &#x60;recommend&#x3D;true&#x60; flag allows this endpoint to both receive ratings and send back recommendations in the same call.

### Example

```javascript
import NprListeningService from 'npr_listening_service';
let defaultClient = NprListeningService.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NprListeningService.DefaultApi();
let authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
let body = [new NprListeningService.RatingData()]; // [RatingData] | A list of RatingData objects which contains data about ratings such as the id of the content, the rating value, elapsed time and more.
let opts = {
  'xAdvertisingID': "xAdvertisingID_example", // String | A device-specific advertising identifier, if possible. Apple's IDFA is an example.
  'channel': "'npr'", // String | Determines the focus of the recommendations returned. Channel `npr` is recommended for most use cases.
  'recommend': true // Boolean | If set to `false`, this call will return a blank document; otherwise it will return a new recommendation object
};
apiInstance.postRating(authorization, body, opts, (error, data, response) => {
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
 **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | 
 **body** | [**[RatingData]**](RatingData.md)| A list of RatingData objects which contains data about ratings such as the id of the content, the rating value, elapsed time and more. | 
 **xAdvertisingID** | **String**| A device-specific advertising identifier, if possible. Apple&#39;s IDFA is an example. | [optional] 
 **channel** | **String**| Determines the focus of the recommendations returned. Channel &#x60;npr&#x60; is recommended for most use cases. | [optional] [default to &#39;npr&#39;]
 **recommend** | **Boolean**| If set to &#x60;false&#x60;, this call will return a blank document; otherwise it will return a new recommendation object | [optional] [default to true]

### Return type

[**AudioItemListDocument**](AudioItemListDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/vnd.collection.doc+json

