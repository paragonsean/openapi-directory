# Shinobiapi.CalendarTelevisionShowSchedulesApi

All URIs are relative to *https://api.hillbillysoftware.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calendarByShowNameGet**](CalendarTelevisionShowSchedulesApi.md#calendarByShowNameGet) | **GET** /Calendar/Show/{AccessToken}/{Name}/{Year} | Will return show schedule for queried showname and year
[**calendarCountriesGet**](CalendarTelevisionShowSchedulesApi.md#calendarCountriesGet) | **GET** /Calendar/Countries/{AccessToken} | Returns list of available countries in calendar database
[**calendarNetworksGet**](CalendarTelevisionShowSchedulesApi.md#calendarNetworksGet) | **GET** /Calendar/Networks/{AccessToken} | Gets a list of available networks
[**calendarShowSeasonsGet**](CalendarTelevisionShowSchedulesApi.md#calendarShowSeasonsGet) | **GET** /Calendar/Seasons/{AccessToken}/{Name} | Returns list of seasons available in the calendar for show
[**calendarTodayGet**](CalendarTelevisionShowSchedulesApi.md#calendarTodayGet) | **GET** /Calendar/Today/{AccessToken} | Will return show schedule for today for all countries in database
[**calendarbyShownameSeasonGet**](CalendarTelevisionShowSchedulesApi.md#calendarbyShownameSeasonGet) | **GET** /Calendar/Show/Season/{AccessToken}/{Name}/{Season} | Get Calendar by showname and season
[**scheduleByDateGet**](CalendarTelevisionShowSchedulesApi.md#scheduleByDateGet) | **GET** /Calendar/ByDate/{AccessToken}/{Date}/{Country} | Gets TV Schedule for selected data



## calendarByShowNameGet

> [Schedule] calendarByShowNameGet(accessToken, name, year)

Will return show schedule for queried showname and year

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.CalendarTelevisionShowSchedulesApi();
let accessToken = "accessToken_example"; // String | 
let name = "name_example"; // String | 
let year = "year_example"; // String | 
apiInstance.calendarByShowNameGet(accessToken, name, year, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **name** | **String**|  | 
 **year** | **String**|  | 

### Return type

[**[Schedule]**](Schedule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## calendarCountriesGet

> [Country] calendarCountriesGet(accessToken)

Returns list of available countries in calendar database

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.CalendarTelevisionShowSchedulesApi();
let accessToken = "accessToken_example"; // String | 
apiInstance.calendarCountriesGet(accessToken, (error, data, response) => {
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
 **accessToken** | **String**|  | 

### Return type

[**[Country]**](Country.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## calendarNetworksGet

> [Networks] calendarNetworksGet(accessToken)

Gets a list of available networks

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.CalendarTelevisionShowSchedulesApi();
let accessToken = "accessToken_example"; // String | 
apiInstance.calendarNetworksGet(accessToken, (error, data, response) => {
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
 **accessToken** | **String**|  | 

### Return type

[**[Networks]**](Networks.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## calendarShowSeasonsGet

> [ShowSeasons] calendarShowSeasonsGet(accessToken, name)

Returns list of seasons available in the calendar for show

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.CalendarTelevisionShowSchedulesApi();
let accessToken = "accessToken_example"; // String | 
let name = "name_example"; // String | 
apiInstance.calendarShowSeasonsGet(accessToken, name, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **name** | **String**|  | 

### Return type

[**[ShowSeasons]**](ShowSeasons.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## calendarTodayGet

> [Schedule] calendarTodayGet(accessToken)

Will return show schedule for today for all countries in database

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.CalendarTelevisionShowSchedulesApi();
let accessToken = "accessToken_example"; // String | 
apiInstance.calendarTodayGet(accessToken, (error, data, response) => {
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
 **accessToken** | **String**|  | 

### Return type

[**[Schedule]**](Schedule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## calendarbyShownameSeasonGet

> [Schedule] calendarbyShownameSeasonGet(accessToken, name, season)

Get Calendar by showname and season

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.CalendarTelevisionShowSchedulesApi();
let accessToken = "accessToken_example"; // String | 
let name = "name_example"; // String | 
let season = "season_example"; // String | 
apiInstance.calendarbyShownameSeasonGet(accessToken, name, season, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **name** | **String**|  | 
 **season** | **String**|  | 

### Return type

[**[Schedule]**](Schedule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## scheduleByDateGet

> [Schedule] scheduleByDateGet(accessToken, date, country)

Gets TV Schedule for selected data

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.CalendarTelevisionShowSchedulesApi();
let accessToken = "accessToken_example"; // String | 
let date = "date_example"; // String | date format year-month-day
let country = "country_example"; // String | US / CA / NL / BE / DE / GB or FR
apiInstance.scheduleByDateGet(accessToken, date, country, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **date** | **String**| date format year-month-day | 
 **country** | **String**| US / CA / NL / BE / DE / GB or FR | 

### Return type

[**[Schedule]**](Schedule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

