# GameSparksGameDetailsApi.SegmentQueryFiltersApi

All URIs are relative to *http://config2.gamesparks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSegmentQueryFiltersConfigUsingGET**](SegmentQueryFiltersApi.md#getSegmentQueryFiltersConfigUsingGET) | **GET** /restv2/game/{apiKey}/admin/segmentQueryFilters/config | getSegmentQueryFiltersConfig
[**getSegmentQueryFiltersUsingGET**](SegmentQueryFiltersApi.md#getSegmentQueryFiltersUsingGET) | **GET** /restv2/game/{apiKey}/admin/segmentQueryFilters | getSegmentQueryFilters
[**getSegmentQueryStandardFiltersUsingGET**](SegmentQueryFiltersApi.md#getSegmentQueryStandardFiltersUsingGET) | **GET** /restv2/game/{apiKey}/admin/segmentQueryFilters/standardFilters | getSegmentQueryStandardFilters
[**updateSegmentQueryFiltersConfigUsingPUT**](SegmentQueryFiltersApi.md#updateSegmentQueryFiltersConfigUsingPUT) | **PUT** /restv2/game/{apiKey}/admin/segmentQueryFilters/config | updateSegmentQueryFiltersConfig



## getSegmentQueryFiltersConfigUsingGET

> SegmentQueryFilterConfigModel getSegmentQueryFiltersConfigUsingGET(apiKey)

getSegmentQueryFiltersConfig

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.SegmentQueryFiltersApi();
let apiKey = "apiKey_example"; // String | apiKey
apiInstance.getSegmentQueryFiltersConfigUsingGET(apiKey, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 

### Return type

[**SegmentQueryFilterConfigModel**](SegmentQueryFilterConfigModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getSegmentQueryFiltersUsingGET

> SegmentQueryFilterListModel getSegmentQueryFiltersUsingGET(apiKey)

getSegmentQueryFilters

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.SegmentQueryFiltersApi();
let apiKey = "apiKey_example"; // String | apiKey
apiInstance.getSegmentQueryFiltersUsingGET(apiKey, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 

### Return type

[**SegmentQueryFilterListModel**](SegmentQueryFilterListModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getSegmentQueryStandardFiltersUsingGET

> SegmentQueryFilterListModel getSegmentQueryStandardFiltersUsingGET(apiKey)

getSegmentQueryStandardFilters

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.SegmentQueryFiltersApi();
let apiKey = "apiKey_example"; // String | apiKey
apiInstance.getSegmentQueryStandardFiltersUsingGET(apiKey, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 

### Return type

[**SegmentQueryFilterListModel**](SegmentQueryFilterListModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## updateSegmentQueryFiltersConfigUsingPUT

> SegmentQueryFilterConfigModel updateSegmentQueryFiltersConfigUsingPUT(apiKey, segmentQueryFilterConfigModel)

updateSegmentQueryFiltersConfig

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.SegmentQueryFiltersApi();
let apiKey = "apiKey_example"; // String | apiKey
let segmentQueryFilterConfigModel = new GameSparksGameDetailsApi.SegmentQueryFilterConfigModel(); // SegmentQueryFilterConfigModel | segmentQueryConfig
apiInstance.updateSegmentQueryFiltersConfigUsingPUT(apiKey, segmentQueryFilterConfigModel, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 
 **segmentQueryFilterConfigModel** | [**SegmentQueryFilterConfigModel**](SegmentQueryFilterConfigModel.md)| segmentQueryConfig | 

### Return type

[**SegmentQueryFilterConfigModel**](SegmentQueryFilterConfigModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8

