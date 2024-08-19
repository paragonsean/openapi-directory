# NeoWsNearEarthObjectWebService.NeosentryApi

All URIs are relative to *http://www.neowsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieveSentryRiskData**](NeosentryApi.md#retrieveSentryRiskData) | **GET** /rest/v1/neo/sentry | Retrieve Sentry (Impact Risk ) Near Earth Objects
[**retrieveSentryRiskDataById**](NeosentryApi.md#retrieveSentryRiskDataById) | **GET** /rest/v1/neo/sentry/{asteroid_id} | Retrieve Sentry (Impact Risk ) Near Earth Objectby ID 



## retrieveSentryRiskData

> SentryObjectPagingDto retrieveSentryRiskData(opts)

Retrieve Sentry (Impact Risk ) Near Earth Objects

Retrieves Near Earth Objects listed in the NASA sentry data set

### Example

```javascript
import NeoWsNearEarthObjectWebService from 'neo_ws__near_earth_object_web_service';

let apiInstance = new NeoWsNearEarthObjectWebService.NeosentryApi();
let opts = {
  'isActive': true, // Boolean | show current list of Sentry objects, or show removed Sentry objects
  'page': 0, // Number | page
  'size': 50 // Number | size
};
apiInstance.retrieveSentryRiskData(opts, (error, data, response) => {
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
 **isActive** | **Boolean**| show current list of Sentry objects, or show removed Sentry objects | [optional] [default to true]
 **page** | **Number**| page | [optional] [default to 0]
 **size** | **Number**| size | [optional] [default to 50]

### Return type

[**SentryObjectPagingDto**](SentryObjectPagingDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveSentryRiskDataById

> SentryImpactRiskObject retrieveSentryRiskDataById(asteroidId)

Retrieve Sentry (Impact Risk ) Near Earth Objectby ID 

Retrieves Sentry Near Earth Object by ID

### Example

```javascript
import NeoWsNearEarthObjectWebService from 'neo_ws__near_earth_object_web_service';

let apiInstance = new NeoWsNearEarthObjectWebService.NeosentryApi();
let asteroidId = "asteroidId_example"; // String | ID of NearEarth object.  ID can be SPK_ID, Asteroid des (designation) or Sentry ID
apiInstance.retrieveSentryRiskDataById(asteroidId, (error, data, response) => {
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
 **asteroidId** | **String**| ID of NearEarth object.  ID can be SPK_ID, Asteroid des (designation) or Sentry ID | 

### Return type

[**SentryImpactRiskObject**](SentryImpactRiskObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

