# FahrplanFree.DefaultApi

All URIs are relative to *https://api.deutschebahn.com/freeplan/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**arrivalBoardIdGet**](DefaultApi.md#arrivalBoardIdGet) | **GET** /arrivalBoard/{id} | Get arrival board of a location
[**departureBoardIdGet**](DefaultApi.md#departureBoardIdGet) | **GET** /departureBoard/{id} | Get departure board of a location
[**journeyDetailsIdGet**](DefaultApi.md#journeyDetailsIdGet) | **GET** /journeyDetails/{id} | Get details about a single journey
[**locationNameGet**](DefaultApi.md#locationNameGet) | **GET** /location/{name} | Get location information



## arrivalBoardIdGet

> BoardResponse arrivalBoardIdGet(id, date)

Get arrival board of a location

Get arrival board at a given location at a given daten and time.

### Example

```javascript
import FahrplanFree from 'fahrplan_free';

let apiInstance = new FahrplanFree.DefaultApi();
let id = "id_example"; // String | Id of location. Use attribute 'id' from the result of 'location'
let date = "date_example"; // String | Date and time in ISO-8601 format, yyyy-mm-ddThh:mm:ss, example: 2017-04-01 or 2017-04-01T10:30
apiInstance.arrivalBoardIdGet(id, date, (error, data, response) => {
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
 **id** | **String**| Id of location. Use attribute &#39;id&#39; from the result of &#39;location&#39; | 
 **date** | **String**| Date and time in ISO-8601 format, yyyy-mm-ddThh:mm:ss, example: 2017-04-01 or 2017-04-01T10:30 | 

### Return type

[**BoardResponse**](BoardResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## departureBoardIdGet

> BoardResponse departureBoardIdGet(id, date)

Get departure board of a location

Get departure board at a given location at a given daten and time.

### Example

```javascript
import FahrplanFree from 'fahrplan_free';

let apiInstance = new FahrplanFree.DefaultApi();
let id = "id_example"; // String | Id of a location. Use attribute 'id' from the result of 'location'
let date = "date_example"; // String | Date and time in ISO-8601 format, yyyy-mm-ddThh:mm:ss, example: 2017-04-01 or 2017-04-01T10:30
apiInstance.departureBoardIdGet(id, date, (error, data, response) => {
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
 **id** | **String**| Id of a location. Use attribute &#39;id&#39; from the result of &#39;location&#39; | 
 **date** | **String**| Date and time in ISO-8601 format, yyyy-mm-ddThh:mm:ss, example: 2017-04-01 or 2017-04-01T10:30 | 

### Return type

[**BoardResponse**](BoardResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## journeyDetailsIdGet

> JourneyResponse journeyDetailsIdGet(id)

Get details about a single journey

Retrieve details of a journey. The id of journey should come from an arrival board or a departure board.

### Example

```javascript
import FahrplanFree from 'fahrplan_free';

let apiInstance = new FahrplanFree.DefaultApi();
let id = "id_example"; // String | Id of a journey. Use attribute 'detailsId' from the result of  'arrivalBoard' or 'departureBoard'
apiInstance.journeyDetailsIdGet(id, (error, data, response) => {
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
 **id** | **String**| Id of a journey. Use attribute &#39;detailsId&#39; from the result of  &#39;arrivalBoard&#39; or &#39;departureBoard&#39; | 

### Return type

[**JourneyResponse**](JourneyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## locationNameGet

> LocationResponse locationNameGet(name)

Get location information

Get information about locations matching the given name or name fragment

### Example

```javascript
import FahrplanFree from 'fahrplan_free';

let apiInstance = new FahrplanFree.DefaultApi();
let name = "name_example"; // String | Name or name fragment of a location
apiInstance.locationNameGet(name, (error, data, response) => {
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
 **name** | **String**| Name or name fragment of a location | 

### Return type

[**LocationResponse**](LocationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

