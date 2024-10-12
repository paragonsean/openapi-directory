# TraktApi.CheckinApi

All URIs are relative to *https://api.trakt.tv*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkIntoAnItem**](CheckinApi.md#checkIntoAnItem) | **POST** /checkin | Check into an item
[**deleteAnyActiveCheckins**](CheckinApi.md#deleteAnyActiveCheckins) | **DELETE** /checkin | Delete any active checkins



## checkIntoAnItem

> checkIntoAnItem(opts)

Check into an item

#### &amp;#128274; OAuth Required  Check into a movie or episode. This should be tied to a user action to manually indicate they are watching something. The item will display as *watching* on the site, then automatically switch to *watched* status once the duration has elapsed. A unique history &#x60;id&#x60; (64-bit integer) will be returned and can be used to reference this checkin directly.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | item &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | object | &#x60;movie&#x60; or &#x60;episode&#x60; object. (see examples &amp;#8594;) | | &#x60;sharing&#x60;  | object | Control sharing to any connected social networks. (see below &amp;#8595;) | | &#x60;message&#x60;  | string | Message used for sharing. If not sent, it will use the watching string in the user settings. | | &#x60;venue_id&#x60; | string | Foursquare venue ID. | | &#x60;venue_name&#x60; | string | Foursquare venue name. | | &#x60;app_version&#x60; | string | Version number of the app. | | &#x60;app_date&#x60; | string | Build date of the app. |  #### Sharing  The &#x60;sharing&#x60; object is optional and will apply the user&#39;s settings if not sent. If &#x60;sharing&#x60; is sent, each key will override the user&#39;s setting for that social network. Send &#x60;true&#x60; to post or &#x60;false&#x60; to not post on the indicated social network. You can see which social networks a user has connected with the [**_/users/settings**](/reference/users/settings) method.  | Key | Type | |---|---| | &#x60;twitter&#x60; | boolean | | &#x60;mastodon&#x60; | boolean | | &#x60;tumblr&#x60; | boolean |  **Note:** If a checkin is already in progress, a &#x60;409&#x60; HTTP status code will returned. The response will contain an &#x60;expires_at&#x60; timestamp which is when the user can check in again.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.CheckinApi();
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]", // String | e.g. [client_id]
  'checkIntoAnItemRequest': new TraktApi.CheckIntoAnItemRequest() // CheckIntoAnItemRequest | 
};
apiInstance.checkIntoAnItem(opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 
 **checkIntoAnItemRequest** | [**CheckIntoAnItemRequest**](CheckIntoAnItemRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAnyActiveCheckins

> deleteAnyActiveCheckins(opts)

Delete any active checkins

#### &amp;#128274; OAuth Required  Removes any active checkins, no need to provide a specific item.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.CheckinApi();
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.deleteAnyActiveCheckins(opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

