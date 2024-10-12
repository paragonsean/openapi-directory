# RadioMusicServices.RadioApi

All URIs are relative to *https://rms.api.bbc.co.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletePersonalisedRadioByActivityTypeById**](RadioApi.md#deletePersonalisedRadioByActivityTypeById) | **DELETE** /my/radio/favourites/{type}/{pid} | Favourite Episode or Clip
[**deletePersonalisedRadioFollowsByTypeById**](RadioApi.md#deletePersonalisedRadioFollowsByTypeById) | **DELETE** /my/radio/follows/{type}/{pid} | Followed Brand or Series
[**getPersonalisedRadioByActivityTypeById**](RadioApi.md#getPersonalisedRadioByActivityTypeById) | **GET** /my/radio/favourites/{type}/{pid} | Favourite Episode or Clip
[**getPersonalisedRadioFavourites**](RadioApi.md#getPersonalisedRadioFavourites) | **GET** /my/radio/favourites | Favourite Episodes and Clips
[**getPersonalisedRadioFavouritesByType**](RadioApi.md#getPersonalisedRadioFavouritesByType) | **GET** /my/radio/favourites/{type} | Favourite Episodes and Clips by Type
[**getPersonalisedRadioFollows**](RadioApi.md#getPersonalisedRadioFollows) | **GET** /my/radio/follows | Followed Brands and Series
[**getPersonalisedRadioFollowsByType**](RadioApi.md#getPersonalisedRadioFollowsByType) | **GET** /my/radio/follows/{type} | Followed Brands or Series by Type
[**getPersonalisedRadioFollowsByTypeById**](RadioApi.md#getPersonalisedRadioFollowsByTypeById) | **GET** /my/radio/follows/{type}/{pid} | Followed Brand or Series
[**getPersonalisedRadioPlays**](RadioApi.md#getPersonalisedRadioPlays) | **GET** /my/radio/plays | Played Episode or Clip
[**postPersonalisedRadioBatch**](RadioApi.md#postPersonalisedRadioBatch) | **POST** /my/radio/favourites | Favourite Episodes and Clips
[**postPersonalisedRadioByActivityTypeById**](RadioApi.md#postPersonalisedRadioByActivityTypeById) | **POST** /my/radio/favourites/{type}/{pid} | Favourite Episode or Clip
[**postPersonalisedRadioFollowsBatch**](RadioApi.md#postPersonalisedRadioFollowsBatch) | **POST** /my/radio/follows | Followed Brands and Series
[**postPersonalisedRadioFollowsByTypeById**](RadioApi.md#postPersonalisedRadioFollowsByTypeById) | **POST** /my/radio/follows/{type}/{pid} | Followed Brand or Series
[**putPersonalisedRadioBatch**](RadioApi.md#putPersonalisedRadioBatch) | **PUT** /my/radio/favourites | Favourite Episodes and Clips
[**putPersonalisedRadioByActivityTypeById**](RadioApi.md#putPersonalisedRadioByActivityTypeById) | **PUT** /my/radio/favourites/{type}/{pid} | Favourite Episode or Clip
[**putPersonalisedRadioFollowsBatch**](RadioApi.md#putPersonalisedRadioFollowsBatch) | **PUT** /my/radio/follows | Followed Brands and Series
[**putPersonalisedRadioFollowsByTypeById**](RadioApi.md#putPersonalisedRadioFollowsByTypeById) | **PUT** /my/radio/follows/{type}/{pid} | Followed Brand or Series



## deletePersonalisedRadioByActivityTypeById

> PersonalisedRadioSuccessResponse deletePersonalisedRadioByActivityTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid)

Favourite Episode or Clip

Remove User favourite 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.RadioApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let type = "type_example"; // String | Supported Radio favourite types: Clips or Episodes
let pid = "pid_example"; // String | pid
apiInstance.deletePersonalisedRadioByActivityTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **type** | **String**| Supported Radio favourite types: Clips or Episodes | 
 **pid** | **String**| pid | 

### Return type

[**PersonalisedRadioSuccessResponse**](PersonalisedRadioSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePersonalisedRadioFollowsByTypeById

> PersonalisedRadioSuccessResponse deletePersonalisedRadioFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid)

Followed Brand or Series

Remove &#39;brand&#39; or &#39;series&#39; items from a users iPlayer Radio follows 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.RadioApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let type = "type_example"; // String | Supported Radio follows types: Brands or Series
let pid = "pid_example"; // String | pid
apiInstance.deletePersonalisedRadioFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **type** | **String**| Supported Radio follows types: Brands or Series | 
 **pid** | **String**| pid | 

### Return type

[**PersonalisedRadioSuccessResponse**](PersonalisedRadioSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPersonalisedRadioByActivityTypeById

> PersonalisedRadioResponse getPersonalisedRadioByActivityTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, opts)

Favourite Episode or Clip

Check to see if a single clip or episode entity is in a users favourites - determines UX of add button.  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.RadioApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let type = "type_example"; // String | Supported Radio favourite types: Clips or Episodes
let pid = "pid_example"; // String | pid
let opts = {
  'showAllActivity': true // Boolean | Include items which have been 'soft' unfavourited in response. I.e items with UAS type of 'unfavourited'
};
apiInstance.getPersonalisedRadioByActivityTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **type** | **String**| Supported Radio favourite types: Clips or Episodes | 
 **pid** | **String**| pid | 
 **showAllActivity** | **Boolean**| Include items which have been &#39;soft&#39; unfavourited in response. I.e items with UAS type of &#39;unfavourited&#39; | [optional] 

### Return type

[**PersonalisedRadioResponse**](PersonalisedRadioResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPersonalisedRadioFavourites

> PersonalisedRadioResponse getPersonalisedRadioFavourites(authorization, xAuthenticationProvider, xAPIKey, opts)

Favourite Episodes and Clips

List of favourited episodes and clips for a given user for iPlayer Radio.  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.RadioApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let opts = {
  'offset': 56, // Number | Paginated results offset
  'limit': 56, // Number | Paginated results limit
  'sort': "sort_example", // String | Sort order for Personalised Radio results
  'showAllActivity': true // Boolean | Include items which have been 'soft' unfavourited in response. I.e items with UAS type of 'unfavourited'
};
apiInstance.getPersonalisedRadioFavourites(authorization, xAuthenticationProvider, xAPIKey, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 
 **sort** | **String**| Sort order for Personalised Radio results | [optional] 
 **showAllActivity** | **Boolean**| Include items which have been &#39;soft&#39; unfavourited in response. I.e items with UAS type of &#39;unfavourited&#39; | [optional] 

### Return type

[**PersonalisedRadioResponse**](PersonalisedRadioResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPersonalisedRadioFavouritesByType

> PersonalisedRadioResponse getPersonalisedRadioFavouritesByType(authorization, xAuthenticationProvider, xAPIKey, type, opts)

Favourite Episodes and Clips by Type

List of followed &#39;clips&#39; or &#39;episode&#39; items for a given iPlayer Radio user  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.RadioApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let type = "type_example"; // String | Supported Radio favourite types: Clips or Episodes
let opts = {
  'sort': "sort_example", // String | Sort order for Personalised Radio results
  'showAllActivity': true, // Boolean | Include items which have been 'soft' unfavourited in response. I.e items with UAS type of 'unfavourited'
  'offset': 56, // Number | Paginated results offset
  'limit': 56 // Number | Paginated results limit
};
apiInstance.getPersonalisedRadioFavouritesByType(authorization, xAuthenticationProvider, xAPIKey, type, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **type** | **String**| Supported Radio favourite types: Clips or Episodes | 
 **sort** | **String**| Sort order for Personalised Radio results | [optional] 
 **showAllActivity** | **Boolean**| Include items which have been &#39;soft&#39; unfavourited in response. I.e items with UAS type of &#39;unfavourited&#39; | [optional] 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 

### Return type

[**PersonalisedRadioResponse**](PersonalisedRadioResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPersonalisedRadioFollows

> PersonalisedRadioResponse getPersonalisedRadioFollows(authorization, xAuthenticationProvider, xAPIKey, opts)

Followed Brands and Series

List of favourited brands and series for a given user for iPlayer Radio.  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.RadioApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let opts = {
  'offset': 56, // Number | Paginated results offset
  'limit': 56, // Number | Paginated results limit
  'sort': "sort_example", // String | Sort order for Personalised Radio results
  'showAllActivity': true // Boolean | Include items which have been 'soft' unfollowed in response. I.e items with UAS type of 'unfollowed'
};
apiInstance.getPersonalisedRadioFollows(authorization, xAuthenticationProvider, xAPIKey, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 
 **sort** | **String**| Sort order for Personalised Radio results | [optional] 
 **showAllActivity** | **Boolean**| Include items which have been &#39;soft&#39; unfollowed in response. I.e items with UAS type of &#39;unfollowed&#39; | [optional] 

### Return type

[**PersonalisedRadioResponse**](PersonalisedRadioResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPersonalisedRadioFollowsByType

> PersonalisedRadioResponse getPersonalisedRadioFollowsByType(authorization, xAuthenticationProvider, xAPIKey, type, opts)

Followed Brands or Series by Type

List of followed &#39;brand&#39; or &#39;series&#39; items for a given iPlayer Radio user  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.RadioApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let type = "type_example"; // String | Supported Radio follows types: Brands or Series
let opts = {
  'sort': "sort_example", // String | Sort order for Personalised Radio results
  'offset': 56, // Number | Paginated results offset
  'limit': 56, // Number | Paginated results limit
  'showAllActivity': true // Boolean | Include items which have been 'soft' unfollowed in response. I.e items with UAS type of 'unfollowed'
};
apiInstance.getPersonalisedRadioFollowsByType(authorization, xAuthenticationProvider, xAPIKey, type, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **type** | **String**| Supported Radio follows types: Brands or Series | 
 **sort** | **String**| Sort order for Personalised Radio results | [optional] 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 
 **showAllActivity** | **Boolean**| Include items which have been &#39;soft&#39; unfollowed in response. I.e items with UAS type of &#39;unfollowed&#39; | [optional] 

### Return type

[**PersonalisedRadioResponse**](PersonalisedRadioResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPersonalisedRadioFollowsByTypeById

> PersonalisedRadioResponse getPersonalisedRadioFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid)

Followed Brand or Series

Check to see if a single brand or series entity is in a users follows - determines UX of add button. 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.RadioApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let type = "type_example"; // String | Supported Radio follows types: Brands or Series
let pid = "pid_example"; // String | pid
apiInstance.getPersonalisedRadioFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **type** | **String**| Supported Radio follows types: Brands or Series | 
 **pid** | **String**| pid | 

### Return type

[**PersonalisedRadioResponse**](PersonalisedRadioResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPersonalisedRadioPlays

> PersonalisedRadioResponse getPersonalisedRadioPlays(authorization, xAuthenticationProvider, xAPIKey, opts)

Played Episode or Clip

Returns mixed episode and clip plays for a given BBC iPlayer radio user.  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.RadioApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let opts = {
  'offset': 56, // Number | Paginated results offset
  'limit': 56, // Number | Paginated results limit
  'sort': "sort_example", // String | Sort order for Personalised Radio results
  'showAllActivity': true // Boolean | Include expired/unavailable items
};
apiInstance.getPersonalisedRadioPlays(authorization, xAuthenticationProvider, xAPIKey, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 
 **sort** | **String**| Sort order for Personalised Radio results | [optional] 
 **showAllActivity** | **Boolean**| Include expired/unavailable items | [optional] 

### Return type

[**PersonalisedRadioResponse**](PersonalisedRadioResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postPersonalisedRadioBatch

> PersonalisedRadioSuccessResponse postPersonalisedRadioBatch(authorization, xAuthenticationProvider, xAPIKey, body)

Favourite Episodes and Clips

Add User favourites  N.B. Any HTML tags submitted in metadata will be removed 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.RadioApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let body = [new RadioMusicServices.PersonalisedRadioBatchRequest()]; // [PersonalisedRadioBatchRequest] | Action favourited or unfavourited
apiInstance.postPersonalisedRadioBatch(authorization, xAuthenticationProvider, xAPIKey, body, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **body** | [**[PersonalisedRadioBatchRequest]**](PersonalisedRadioBatchRequest.md)| Action favourited or unfavourited | 

### Return type

[**PersonalisedRadioSuccessResponse**](PersonalisedRadioSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postPersonalisedRadioByActivityTypeById

> PersonalisedRadioSuccessResponse postPersonalisedRadioByActivityTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, body)

Favourite Episode or Clip

Add User favourite  N.B. Any HTML tags submitted in metadata will be removed 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.RadioApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let type = "type_example"; // String | Supported Radio favourite types: Clips or Episodes
let pid = "pid_example"; // String | pid
let body = new RadioMusicServices.PersonalisedRadioRequest(); // PersonalisedRadioRequest | Action favourited or unfavourited
apiInstance.postPersonalisedRadioByActivityTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, body, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **type** | **String**| Supported Radio favourite types: Clips or Episodes | 
 **pid** | **String**| pid | 
 **body** | [**PersonalisedRadioRequest**](PersonalisedRadioRequest.md)| Action favourited or unfavourited | 

### Return type

[**PersonalisedRadioSuccessResponse**](PersonalisedRadioSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postPersonalisedRadioFollowsBatch

> PersonalisedRadioSuccessResponse postPersonalisedRadioFollowsBatch(authorization, xAuthenticationProvider, xAPIKey, body)

Followed Brands and Series

Add &#39;brand&#39; or &#39;series&#39; items to a users iPlayer Radio follows  N.B. Any HTML tags submitted in metadata will be removed 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.RadioApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let body = [new RadioMusicServices.PersonalisedRadioBatchRequest()]; // [PersonalisedRadioBatchRequest] | Action followed or unfollowed
apiInstance.postPersonalisedRadioFollowsBatch(authorization, xAuthenticationProvider, xAPIKey, body, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **body** | [**[PersonalisedRadioBatchRequest]**](PersonalisedRadioBatchRequest.md)| Action followed or unfollowed | 

### Return type

[**PersonalisedRadioSuccessResponse**](PersonalisedRadioSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postPersonalisedRadioFollowsByTypeById

> PersonalisedRadioSuccessResponse postPersonalisedRadioFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, body)

Followed Brand or Series

Add &#39;brand&#39; or &#39;series&#39; items from a users iPlayer Radio follows  N.B. Any HTML tags submitted in metadata will be removed 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.RadioApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let type = "type_example"; // String | Supported Radio follows types: Brands or Series
let pid = "pid_example"; // String | pid
let body = new RadioMusicServices.PersonalisedRadioRequest(); // PersonalisedRadioRequest | Action followed or unfollowed
apiInstance.postPersonalisedRadioFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, body, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **type** | **String**| Supported Radio follows types: Brands or Series | 
 **pid** | **String**| pid | 
 **body** | [**PersonalisedRadioRequest**](PersonalisedRadioRequest.md)| Action followed or unfollowed | 

### Return type

[**PersonalisedRadioSuccessResponse**](PersonalisedRadioSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putPersonalisedRadioBatch

> PersonalisedRadioSuccessResponse putPersonalisedRadioBatch(authorization, xAuthenticationProvider, xAPIKey, body)

Favourite Episodes and Clips

Update user favourites  N.B. Any HTML tags submitted in metadata will be removed 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.RadioApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let body = [new RadioMusicServices.PersonalisedRadioBatchRequest()]; // [PersonalisedRadioBatchRequest] | Action favourited or unfavourited
apiInstance.putPersonalisedRadioBatch(authorization, xAuthenticationProvider, xAPIKey, body, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **body** | [**[PersonalisedRadioBatchRequest]**](PersonalisedRadioBatchRequest.md)| Action favourited or unfavourited | 

### Return type

[**PersonalisedRadioSuccessResponse**](PersonalisedRadioSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putPersonalisedRadioByActivityTypeById

> PersonalisedRadioSuccessResponse putPersonalisedRadioByActivityTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, body)

Favourite Episode or Clip

Update user favourite  N.B. Any HTML tags submitted in metadata will be removed 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.RadioApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let type = "type_example"; // String | Supported Radio favourite types: Clips or Episodes
let pid = "pid_example"; // String | pid
let body = new RadioMusicServices.PersonalisedRadioRequest(); // PersonalisedRadioRequest | Action favourited or unfavourited
apiInstance.putPersonalisedRadioByActivityTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, body, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **type** | **String**| Supported Radio favourite types: Clips or Episodes | 
 **pid** | **String**| pid | 
 **body** | [**PersonalisedRadioRequest**](PersonalisedRadioRequest.md)| Action favourited or unfavourited | 

### Return type

[**PersonalisedRadioSuccessResponse**](PersonalisedRadioSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putPersonalisedRadioFollowsBatch

> PersonalisedRadioSuccessResponse putPersonalisedRadioFollowsBatch(authorization, xAuthenticationProvider, xAPIKey, body)

Followed Brands and Series

Update &#39;brands&#39; or &#39;series&#39; items from a users iPlayer Radio follows  N.B. Any HTML tags submitted in metadata will be removed 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.RadioApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let body = [new RadioMusicServices.PersonalisedRadioBatchRequest()]; // [PersonalisedRadioBatchRequest] | Action followed or unfollowed
apiInstance.putPersonalisedRadioFollowsBatch(authorization, xAuthenticationProvider, xAPIKey, body, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **body** | [**[PersonalisedRadioBatchRequest]**](PersonalisedRadioBatchRequest.md)| Action followed or unfollowed | 

### Return type

[**PersonalisedRadioSuccessResponse**](PersonalisedRadioSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putPersonalisedRadioFollowsByTypeById

> PersonalisedRadioSuccessResponse putPersonalisedRadioFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, body)

Followed Brand or Series

Update &#39;brand&#39; or &#39;series&#39; items from a users iPlayer Radio follows  N.B. Any HTML tags submitted in metadata will be removed 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.RadioApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let type = "type_example"; // String | Supported Radio follows types: Brands or Series
let pid = "pid_example"; // String | pid
let body = new RadioMusicServices.PersonalisedRadioRequest(); // PersonalisedRadioRequest | Action followed or unfollowed
apiInstance.putPersonalisedRadioFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, pid, body, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **type** | **String**| Supported Radio follows types: Brands or Series | 
 **pid** | **String**| pid | 
 **body** | [**PersonalisedRadioRequest**](PersonalisedRadioRequest.md)| Action followed or unfollowed | 

### Return type

[**PersonalisedRadioSuccessResponse**](PersonalisedRadioSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

