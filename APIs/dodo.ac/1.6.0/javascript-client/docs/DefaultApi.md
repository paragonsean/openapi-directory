# Nookipedia.DefaultApi

All URIs are relative to *https://api.nookipedia.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nhArtArtworkGet**](DefaultApi.md#nhArtArtworkGet) | **GET** /nh/art/{artwork} | Single New Horizons artwork
[**nhArtGet**](DefaultApi.md#nhArtGet) | **GET** /nh/art | All New Horizons artwork
[**nhBugsBugGet**](DefaultApi.md#nhBugsBugGet) | **GET** /nh/bugs/{bug} | Single New Horizons bug
[**nhBugsGet**](DefaultApi.md#nhBugsGet) | **GET** /nh/bugs | All New Horizons bugs
[**nhClothingClothingGet**](DefaultApi.md#nhClothingClothingGet) | **GET** /nh/clothing/{clothing} | Single New Horizons clothing
[**nhClothingGet**](DefaultApi.md#nhClothingGet) | **GET** /nh/clothing | All New Horizons clothing
[**nhEventsGet**](DefaultApi.md#nhEventsGet) | **GET** /nh/events | All New Horizons events
[**nhFishFishGet**](DefaultApi.md#nhFishFishGet) | **GET** /nh/fish/{fish} | Single New Horizons fish
[**nhFishGet**](DefaultApi.md#nhFishGet) | **GET** /nh/fish | All New Horizons fish
[**nhFossilsAllFossilGet**](DefaultApi.md#nhFossilsAllFossilGet) | **GET** /nh/fossils/all/{fossil} | Single New Horizons fossil group with individual fossils
[**nhFossilsAllGet**](DefaultApi.md#nhFossilsAllGet) | **GET** /nh/fossils/all | All New Horizons fossil groups or individual fossil
[**nhFossilsGroupsFossilGroupGet**](DefaultApi.md#nhFossilsGroupsFossilGroupGet) | **GET** /nh/fossils/groups/{fossil_group} | Single New Horizons fossil group
[**nhFossilsGroupsGet**](DefaultApi.md#nhFossilsGroupsGet) | **GET** /nh/fossils/groups | All New Horizons fossil groups
[**nhFossilsIndividualsFossilGet**](DefaultApi.md#nhFossilsIndividualsFossilGet) | **GET** /nh/fossils/individuals/{fossil} | Single New Horizons fossil
[**nhFossilsIndividualsGet**](DefaultApi.md#nhFossilsIndividualsGet) | **GET** /nh/fossils/individuals | All New Horizons fossils
[**nhFurnitureFurnitureGet**](DefaultApi.md#nhFurnitureFurnitureGet) | **GET** /nh/furniture/{furniture} | Single New Horizons furniture
[**nhFurnitureGet**](DefaultApi.md#nhFurnitureGet) | **GET** /nh/furniture | All New Horizons furniture
[**nhInteriorGet**](DefaultApi.md#nhInteriorGet) | **GET** /nh/interior | All New Horizons interior items
[**nhInteriorItemGet**](DefaultApi.md#nhInteriorItemGet) | **GET** /nh/interior/{item} | Single New Horizons interior item
[**nhItemsGet**](DefaultApi.md#nhItemsGet) | **GET** /nh/items | Miscellaneous New Horizons items
[**nhItemsItemGet**](DefaultApi.md#nhItemsItemGet) | **GET** /nh/items/{item} | Single New Horizons miscellaneous item
[**nhPhotosGet**](DefaultApi.md#nhPhotosGet) | **GET** /nh/photos | All New Horizons photos and posters
[**nhPhotosItemGet**](DefaultApi.md#nhPhotosItemGet) | **GET** /nh/photos/{item} | Single New Horizons photo or poster
[**nhRecipesGet**](DefaultApi.md#nhRecipesGet) | **GET** /nh/recipes | All New Horizons recipes
[**nhRecipesItemGet**](DefaultApi.md#nhRecipesItemGet) | **GET** /nh/recipes/{item} | Single New Horizons recipe
[**nhSeaGet**](DefaultApi.md#nhSeaGet) | **GET** /nh/sea | All New Horizons sea creatures
[**nhSeaSeaCreatureGet**](DefaultApi.md#nhSeaSeaCreatureGet) | **GET** /nh/sea/{sea_creature} | Single New Horizons sea creature
[**nhToolsGet**](DefaultApi.md#nhToolsGet) | **GET** /nh/tools | All New Horizons tools
[**nhToolsToolGet**](DefaultApi.md#nhToolsToolGet) | **GET** /nh/tools/{tool} | Single New Horizons tool
[**villagersGet**](DefaultApi.md#villagersGet) | **GET** /villagers | Villagers



## nhArtArtworkGet

> NHArtwork nhArtArtworkGet(artwork, X_API_KEY, acceptVersion, opts)

Single New Horizons artwork

Retrieve information about a specific artwork in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let artwork = "artwork_example"; // String | The name of the artwork you wish to retrieve information about.
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
};
apiInstance.nhArtArtworkGet(artwork, X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **artwork** | **String**| The name of the artwork you wish to retrieve information about. | 
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] 

### Return type

[**NHArtwork**](NHArtwork.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhArtGet

> [NHArtwork] nhArtGet(X_API_KEY, acceptVersion, opts)

All New Horizons artwork

Get a list of all artwork and their details in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'hasfake': "hasfake_example", // String | When set to `true`, only artwork that has a fake will be returned. When set to `false`, only artwork without fakes will be returned.
  'excludedetails': "excludedetails_example", // String | When set to `true`, only artwork names are returned. Instead of an array of objects with all details, the return will be an array of strings.
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time.
};
apiInstance.nhArtGet(X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **hasfake** | **String**| When set to &#x60;true&#x60;, only artwork that has a fake will be returned. When set to &#x60;false&#x60;, only artwork without fakes will be returned. | [optional] 
 **excludedetails** | **String**| When set to &#x60;true&#x60;, only artwork names are returned. Instead of an array of objects with all details, the return will be an array of strings. | [optional] 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time. | [optional] 

### Return type

[**[NHArtwork]**](NHArtwork.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhBugsBugGet

> NHBug nhBugsBugGet(bug, X_API_KEY, acceptVersion, opts)

Single New Horizons bug

Retrieve information about a specific bug in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let bug = "bug_example"; // String | The name of the bug you wish to retrieve information about.
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
};
apiInstance.nhBugsBugGet(bug, X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **bug** | **String**| The name of the bug you wish to retrieve information about. | 
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] 

### Return type

[**NHBug**](NHBug.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhBugsGet

> [NHBug] nhBugsGet(X_API_KEY, acceptVersion, opts)

All New Horizons bugs

Get a list of all bugs and their details in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'month': "month_example", // String | Retrive only the bug that are available in a specific month. Value may be the month's name (`jan`, `january`), the integer representing the month (`01`, `1`), or `current` for the current month. When `current` is specified, the return body will be an object with two arrays inside, one called `north` and the other `south` containing the bug available in each respective hemisphere. Note that the current month is calculated based off the API server's time, so it may be slightly off for you at the beginning or end of the month.
  'excludedetails': "excludedetails_example", // String | When set to `true`, only bug names are returned. Instead of an array of objects with all details, the return will be an array of strings. This is particularly useful when used with the `month` filter, for users who want just a list of bugs in a given month but not all their respective details.
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time.
};
apiInstance.nhBugsGet(X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **month** | **String**| Retrive only the bug that are available in a specific month. Value may be the month&#39;s name (&#x60;jan&#x60;, &#x60;january&#x60;), the integer representing the month (&#x60;01&#x60;, &#x60;1&#x60;), or &#x60;current&#x60; for the current month. When &#x60;current&#x60; is specified, the return body will be an object with two arrays inside, one called &#x60;north&#x60; and the other &#x60;south&#x60; containing the bug available in each respective hemisphere. Note that the current month is calculated based off the API server&#39;s time, so it may be slightly off for you at the beginning or end of the month. | [optional] 
 **excludedetails** | **String**| When set to &#x60;true&#x60;, only bug names are returned. Instead of an array of objects with all details, the return will be an array of strings. This is particularly useful when used with the &#x60;month&#x60; filter, for users who want just a list of bugs in a given month but not all their respective details. | [optional] 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time. | [optional] 

### Return type

[**[NHBug]**](NHBug.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhClothingClothingGet

> NHClothing nhClothingClothingGet(clothing, X_API_KEY, acceptVersion, opts)

Single New Horizons clothing

Retrieve information about a specific clothing item in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let clothing = "clothing_example"; // String | The name of the clothing you wish to retrieve information about.
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
};
apiInstance.nhClothingClothingGet(clothing, X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **clothing** | **String**| The name of the clothing you wish to retrieve information about. | 
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] 

### Return type

[**NHClothing**](NHClothing.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhClothingGet

> [NHClothing] nhClothingGet(X_API_KEY, acceptVersion, opts)

All New Horizons clothing

Get a list of all clothing items and their details in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'category': "category_example", // String | Specify the category of clothing to return.
  'color': ["null"], // [String] | Return clothing that matches the provided colors (may specify one or two colors). Colors are used for gifting villagers.
  'style': ["null"], // [String] | Return clothing that matches the provided styles (may specify one or two styles). Styles are used for gifting villagers.
  'labeltheme': "labeltheme_example", // String | Return clothing that have the specified Label theme. This is used for completing the requested outfit theme for [Label](https://nookipedia.com/wiki/Label) when she visits the player's island.
  'excludedetails': "excludedetails_example" // String | When set to `true`, only clothing names are returned. Instead of an array of objects with all details, the return will be an array of strings.
};
apiInstance.nhClothingGet(X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **category** | **String**| Specify the category of clothing to return. | [optional] 
 **color** | [**[String]**](String.md)| Return clothing that matches the provided colors (may specify one or two colors). Colors are used for gifting villagers. | [optional] 
 **style** | [**[String]**](String.md)| Return clothing that matches the provided styles (may specify one or two styles). Styles are used for gifting villagers. | [optional] 
 **labeltheme** | **String**| Return clothing that have the specified Label theme. This is used for completing the requested outfit theme for [Label](https://nookipedia.com/wiki/Label) when she visits the player&#39;s island. | [optional] 
 **excludedetails** | **String**| When set to &#x60;true&#x60;, only clothing names are returned. Instead of an array of objects with all details, the return will be an array of strings. | [optional] 

### Return type

[**[NHClothing]**](NHClothing.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhEventsGet

> [NHEvent] nhEventsGet(X_API_KEY, acceptVersion, opts)

All New Horizons events

Get a list of events and dates in *Animal Crossing: New Horizons*, filterable to specific years, months, or days. Data is available for the current and next year.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'date': "date_example", // String | Specify a specific date (in the current or next year) to retrieve events for. Accepts many date formats, such as `YYYY-MM-DD` or `Month Day, Year`, as well as `today` to retrieve the current day's events (UTC time).
  'year': "year_example", // String | Specify the year to retrieve events for. Must be the current or next year.
  'month': "month_example", // String | Specify the month to retrieve events for (accepts multiple formats, such as `Oct`, `October`, or `10`). Most likely want to use alongside `year`, otherwise events in both the current and next year are returned.
  'day': 56 // Number | Specify the day of the month to retrieve events for.
};
apiInstance.nhEventsGet(X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **date** | **String**| Specify a specific date (in the current or next year) to retrieve events for. Accepts many date formats, such as &#x60;YYYY-MM-DD&#x60; or &#x60;Month Day, Year&#x60;, as well as &#x60;today&#x60; to retrieve the current day&#39;s events (UTC time). | [optional] 
 **year** | **String**| Specify the year to retrieve events for. Must be the current or next year. | [optional] 
 **month** | **String**| Specify the month to retrieve events for (accepts multiple formats, such as &#x60;Oct&#x60;, &#x60;October&#x60;, or &#x60;10&#x60;). Most likely want to use alongside &#x60;year&#x60;, otherwise events in both the current and next year are returned. | [optional] 
 **day** | **Number**| Specify the day of the month to retrieve events for. | [optional] 

### Return type

[**[NHEvent]**](NHEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhFishFishGet

> NHFish nhFishFishGet(fish, X_API_KEY, acceptVersion, opts)

Single New Horizons fish

Retrieve information about a specific fish in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let fish = "fish_example"; // String | The name of the fish you wish to retrieve information about.
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
};
apiInstance.nhFishFishGet(fish, X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **fish** | **String**| The name of the fish you wish to retrieve information about. | 
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] 

### Return type

[**NHFish**](NHFish.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhFishGet

> [NHFish] nhFishGet(X_API_KEY, acceptVersion, opts)

All New Horizons fish

Get a list of all fish and their details in *New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'month': "month_example", // String | Retrive only the fish that are available in a specific month. Value may be the month's name (`jan`, `january`), the integer representing the month (`01`, `1`), or `current` for the current month. When `current` is specified, the return body will be an object with two arrays inside, one called `north` and the other `south` containing the fish available in each respective hemisphere. Note that the current month is calculated based off the API server's time, so it may be slightly off for you at the beginning or end of the month.
  'excludedetails': "excludedetails_example", // String | When set to `true`, only fish names are returned. Instead of an array of objects with all details, the return will be an array of strings. This is particularly useful when used with the `month` filter, for users who want just a list of fish in a given month but not all their respective details.
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time.
};
apiInstance.nhFishGet(X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **month** | **String**| Retrive only the fish that are available in a specific month. Value may be the month&#39;s name (&#x60;jan&#x60;, &#x60;january&#x60;), the integer representing the month (&#x60;01&#x60;, &#x60;1&#x60;), or &#x60;current&#x60; for the current month. When &#x60;current&#x60; is specified, the return body will be an object with two arrays inside, one called &#x60;north&#x60; and the other &#x60;south&#x60; containing the fish available in each respective hemisphere. Note that the current month is calculated based off the API server&#39;s time, so it may be slightly off for you at the beginning or end of the month. | [optional] 
 **excludedetails** | **String**| When set to &#x60;true&#x60;, only fish names are returned. Instead of an array of objects with all details, the return will be an array of strings. This is particularly useful when used with the &#x60;month&#x60; filter, for users who want just a list of fish in a given month but not all their respective details. | [optional] 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time. | [optional] 

### Return type

[**[NHFish]**](NHFish.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhFossilsAllFossilGet

> NHFossilGroupWithIndividualFossils nhFossilsAllFossilGet(fossil, X_API_KEY, acceptVersion, opts)

Single New Horizons fossil group with individual fossils

Retrieve information about a specific fossil group with their respective individual fossils in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let fossil = "fossil_example"; // String | The name of the fossil OR fossil group you wish to retrieve information about. If a fossil is provided, a fossil group that the specified fossil belongs to will be returned.
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
};
apiInstance.nhFossilsAllFossilGet(fossil, X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **fossil** | **String**| The name of the fossil OR fossil group you wish to retrieve information about. If a fossil is provided, a fossil group that the specified fossil belongs to will be returned. | 
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] 

### Return type

[**NHFossilGroupWithIndividualFossils**](NHFossilGroupWithIndividualFossils.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhFossilsAllGet

> [NHFossilGroupWithIndividualFossilsNoMatched] nhFossilsAllGet(X_API_KEY, acceptVersion, opts)

All New Horizons fossil groups or individual fossil

Get a list of all the fossil groups with their respective individual fossils in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
};
apiInstance.nhFossilsAllGet(X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] 

### Return type

[**[NHFossilGroupWithIndividualFossilsNoMatched]**](NHFossilGroupWithIndividualFossilsNoMatched.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhFossilsGroupsFossilGroupGet

> NHFossilGroup nhFossilsGroupsFossilGroupGet(fossilGroup, X_API_KEY, acceptVersion, opts)

Single New Horizons fossil group

Retrieve information about a specific fossil group in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let fossilGroup = "fossilGroup_example"; // String | The name of the fossil group you wish to retrieve information about.
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
};
apiInstance.nhFossilsGroupsFossilGroupGet(fossilGroup, X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **fossilGroup** | **String**| The name of the fossil group you wish to retrieve information about. | 
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] 

### Return type

[**NHFossilGroup**](NHFossilGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhFossilsGroupsGet

> [NHFossilGroup] nhFossilsGroupsGet(X_API_KEY, acceptVersion, opts)

All New Horizons fossil groups

Get a list of all the fossil groups in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
};
apiInstance.nhFossilsGroupsGet(X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] 

### Return type

[**[NHFossilGroup]**](NHFossilGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhFossilsIndividualsFossilGet

> NHIndividualFossil nhFossilsIndividualsFossilGet(fossil, X_API_KEY, acceptVersion, opts)

Single New Horizons fossil

Retrieve information about a specific individual fossil in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let fossil = "fossil_example"; // String | The name of the individual fossil you wish to retrieve fossil information about.
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
};
apiInstance.nhFossilsIndividualsFossilGet(fossil, X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **fossil** | **String**| The name of the individual fossil you wish to retrieve fossil information about. | 
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] 

### Return type

[**NHIndividualFossil**](NHIndividualFossil.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhFossilsIndividualsGet

> [NHIndividualFossil] nhFossilsIndividualsGet(X_API_KEY, acceptVersion, opts)

All New Horizons fossils

Get a list of all the individual fossils in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
};
apiInstance.nhFossilsIndividualsGet(X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] 

### Return type

[**[NHIndividualFossil]**](NHIndividualFossil.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhFurnitureFurnitureGet

> NHFurniture nhFurnitureFurnitureGet(furniture, X_API_KEY, acceptVersion, opts)

Single New Horizons furniture

Retrieve information about a specific furniture in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let furniture = "furniture_example"; // String | The name of the furniture you wish to retrieve information about.
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
};
apiInstance.nhFurnitureFurnitureGet(furniture, X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **furniture** | **String**| The name of the furniture you wish to retrieve information about. | 
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] 

### Return type

[**NHFurniture**](NHFurniture.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhFurnitureGet

> [NHFurniture] nhFurnitureGet(X_API_KEY, acceptVersion, opts)

All New Horizons furniture

Get a list of all furniture and their details in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'category': "category_example", // String | Specify the category of furniture to return (houswares, miscellaneous, or wall-mounted).
  'color': ["null"], // [String] | Return furniture that matches the provided colors (may specify one or two colors).
  'excludedetails': "excludedetails_example" // String | When set to `true`, only furniture names are returned. Instead of an array of objects with all details, the return will be an array of strings.
};
apiInstance.nhFurnitureGet(X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **category** | **String**| Specify the category of furniture to return (houswares, miscellaneous, or wall-mounted). | [optional] 
 **color** | [**[String]**](String.md)| Return furniture that matches the provided colors (may specify one or two colors). | [optional] 
 **excludedetails** | **String**| When set to &#x60;true&#x60;, only furniture names are returned. Instead of an array of objects with all details, the return will be an array of strings. | [optional] 

### Return type

[**[NHFurniture]**](NHFurniture.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhInteriorGet

> [NHInterior] nhInteriorGet(X_API_KEY, acceptVersion, opts)

All New Horizons interior items

Get a list of all interior items (flooring, wallpaper, and rugs) and their details in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'color': ["null"], // [String] | Return furniture that matches the provided colors (may specify one or two colors).
  'excludedetails': "excludedetails_example" // String | When set to `true`, only interior item names are returned. Instead of an array of objects with all details, the return will be an array of strings.
};
apiInstance.nhInteriorGet(X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **color** | [**[String]**](String.md)| Return furniture that matches the provided colors (may specify one or two colors). | [optional] 
 **excludedetails** | **String**| When set to &#x60;true&#x60;, only interior item names are returned. Instead of an array of objects with all details, the return will be an array of strings. | [optional] 

### Return type

[**[NHInterior]**](NHInterior.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhInteriorItemGet

> NHInterior nhInteriorItemGet(item, X_API_KEY, acceptVersion, opts)

Single New Horizons interior item

Retrieve information about a specific interior item in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let item = "item_example"; // String | The name of the interior item you wish to retrieve information about.
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'color': ["null"], // [String] | Return furniture that matches the provided colors (may specify one or two colors).
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
};
apiInstance.nhInteriorItemGet(item, X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **item** | **String**| The name of the interior item you wish to retrieve information about. | 
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **color** | [**[String]**](String.md)| Return furniture that matches the provided colors (may specify one or two colors). | [optional] 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] 

### Return type

[**NHInterior**](NHInterior.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhItemsGet

> [NHItem] nhItemsGet(X_API_KEY, acceptVersion, opts)

Miscellaneous New Horizons items

Get a list of all miscellaneous items (such as materials, star fragments, fruits, fences, and plants) and their details in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'excludedetails': "excludedetails_example" // String | When set to `true`, only item names are returned. Instead of an array of objects with all details, the return will be an array of strings.
};
apiInstance.nhItemsGet(X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **excludedetails** | **String**| When set to &#x60;true&#x60;, only item names are returned. Instead of an array of objects with all details, the return will be an array of strings. | [optional] 

### Return type

[**[NHItem]**](NHItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhItemsItemGet

> NHItem nhItemsItemGet(item, X_API_KEY, acceptVersion, opts)

Single New Horizons miscellaneous item

Retrieve information about a miscellaneous item (such as materials, star fragments, fruits, fences, and plants) in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let item = "item_example"; // String | The name of the interior item you wish to retrieve information about.
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
};
apiInstance.nhItemsItemGet(item, X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **item** | **String**| The name of the interior item you wish to retrieve information about. | 
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] 

### Return type

[**NHItem**](NHItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhPhotosGet

> [NHPhoto] nhPhotosGet(X_API_KEY, acceptVersion, opts)

All New Horizons photos and posters

Get a list of all character photos+posters and their details in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'excludedetails': "excludedetails_example" // String | When set to `true`, only item names are returned. Instead of an array of objects with all details, the return will be an array of strings.
};
apiInstance.nhPhotosGet(X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **excludedetails** | **String**| When set to &#x60;true&#x60;, only item names are returned. Instead of an array of objects with all details, the return will be an array of strings. | [optional] 

### Return type

[**[NHPhoto]**](NHPhoto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhPhotosItemGet

> NHPhoto nhPhotosItemGet(item, X_API_KEY, acceptVersion, opts)

Single New Horizons photo or poster

Retrieve information about a character photo or poster in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let item = "item_example"; // String | The name of the photo or poster you wish to retrieve information about.
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
};
apiInstance.nhPhotosItemGet(item, X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **item** | **String**| The name of the photo or poster you wish to retrieve information about. | 
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] 

### Return type

[**NHPhoto**](NHPhoto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhRecipesGet

> [NHRecipe] nhRecipesGet(X_API_KEY, acceptVersion, opts)

All New Horizons recipes

Get a list of all recipes and their details in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'material': "material_example", // String | Specify a material to only get recipes that use that material. You can specify `material` up to six times (no recipe uses more than six materials).
  'excludedetails': "excludedetails_example", // String | When set to `true`, only recipe names are returned. Instead of an array of objects with all details, the return will be an array of strings.
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time.
};
apiInstance.nhRecipesGet(X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **material** | **String**| Specify a material to only get recipes that use that material. You can specify &#x60;material&#x60; up to six times (no recipe uses more than six materials). | [optional] 
 **excludedetails** | **String**| When set to &#x60;true&#x60;, only recipe names are returned. Instead of an array of objects with all details, the return will be an array of strings. | [optional] 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time. | [optional] 

### Return type

[**[NHRecipe]**](NHRecipe.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhRecipesItemGet

> NHRecipe nhRecipesItemGet(item, X_API_KEY, acceptVersion, opts)

Single New Horizons recipe

Retrieve information about a specific recipe in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let item = "item_example"; // String | The name of the item you wish to retrieve recipe information about.
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
};
apiInstance.nhRecipesItemGet(item, X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **item** | **String**| The name of the item you wish to retrieve recipe information about. | 
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] 

### Return type

[**NHRecipe**](NHRecipe.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhSeaGet

> [NHSeaCreature] nhSeaGet(X_API_KEY, acceptVersion, opts)

All New Horizons sea creatures

Get a list of all sea creatures and their details in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'month': "month_example", // String | Retrive only the sea creature that are available in a specific month. Value may be the month's name (`jan`, `january`), the integer representing the month (`01`, `1`), or `current` for the current month. When `current` is specified, the return body will be an object with two arrays inside, one called `north` and the other `south` containing the sea creature available in each respective hemisphere. Note that the current month is calculated based off the API server's time, so it may be slightly off for you at the beginning or end of the month.
  'excludedetails': "excludedetails_example", // String | When set to `true`, only sea creature names are returned. Instead of an array of objects with all details, the return will be an array of strings. This is particularly useful when used with the `month` filter, for users who want just a list of sea creatures in a given month but not all their respective details.
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time.
};
apiInstance.nhSeaGet(X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **month** | **String**| Retrive only the sea creature that are available in a specific month. Value may be the month&#39;s name (&#x60;jan&#x60;, &#x60;january&#x60;), the integer representing the month (&#x60;01&#x60;, &#x60;1&#x60;), or &#x60;current&#x60; for the current month. When &#x60;current&#x60; is specified, the return body will be an object with two arrays inside, one called &#x60;north&#x60; and the other &#x60;south&#x60; containing the sea creature available in each respective hemisphere. Note that the current month is calculated based off the API server&#39;s time, so it may be slightly off for you at the beginning or end of the month. | [optional] 
 **excludedetails** | **String**| When set to &#x60;true&#x60;, only sea creature names are returned. Instead of an array of objects with all details, the return will be an array of strings. This is particularly useful when used with the &#x60;month&#x60; filter, for users who want just a list of sea creatures in a given month but not all their respective details. | [optional] 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time. | [optional] 

### Return type

[**[NHSeaCreature]**](NHSeaCreature.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhSeaSeaCreatureGet

> NHSeaCreature nhSeaSeaCreatureGet(seaCreature, X_API_KEY, acceptVersion, opts)

Single New Horizons sea creature

Retrieve information about a specific sea creature in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let seaCreature = "seaCreature_example"; // String | The name of the sea creature you wish to retrieve information about.
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
};
apiInstance.nhSeaSeaCreatureGet(seaCreature, X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **seaCreature** | **String**| The name of the sea creature you wish to retrieve information about. | 
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] 

### Return type

[**NHSeaCreature**](NHSeaCreature.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhToolsGet

> [NHTool] nhToolsGet(X_API_KEY, acceptVersion, opts)

All New Horizons tools

Get a list of all tools and their details in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'excludedetails': "excludedetails_example" // String | When set to `true`, only tool names are returned. Instead of an array of objects with all details, the return will be an array of strings.
};
apiInstance.nhToolsGet(X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **excludedetails** | **String**| When set to &#x60;true&#x60;, only tool names are returned. Instead of an array of objects with all details, the return will be an array of strings. | [optional] 

### Return type

[**[NHTool]**](NHTool.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nhToolsToolGet

> NHTool nhToolsToolGet(tool, X_API_KEY, acceptVersion, opts)

Single New Horizons tool

Retrieve information about a specific tool in *Animal Crossing: New Horizons*.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let tool = "tool_example"; // String | The name of the interior item you wish to retrieve information about.
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL.
};
apiInstance.nhToolsToolGet(tool, X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **tool** | **String**| The name of the interior item you wish to retrieve information about. | 
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. | [optional] 

### Return type

[**NHTool**](NHTool.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## villagersGet

> [Villager] villagersGet(X_API_KEY, acceptVersion, opts)

Villagers

This endpoint retrieves villager information from the entire *Animal Crossing* series, with the option to filter by species, personality, game, and/or birthday. Filters use the AND operator (e.g. asking for villagers who have species &#x60;frog&#x60; and personality &#x60;smug&#x60; will return all smug frogs). Note that villagers only include the animals that act as residents. Special characters, such as Tom Nook and Isabelle, are not accessed through this endpoint.

### Example

```javascript
import Nookipedia from 'nookipedia';

let apiInstance = new Nookipedia.DefaultApi();
let X_API_KEY = "X_API_KEY_example"; // String | Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API.
let acceptVersion = "acceptVersion_example"; // String | The version of the API you are calling, written as `1.0.0`. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes.
let opts = {
  'name': "name_example", // String | Villager name. For most names you will get back an array with one object, but note that names are not a unique identifier across the series, as there are 3 names that are shared by multiple villagers (Lulu, Petunia, Carmen). For those 3 names you will get back an array with 2 objects. How you disambiguate between these villagers is up to you.
  'species': "species_example", // String | Retrieve villagers of a certain species.
  'personality': "personality_example", // String | Retrieve villagers with a certain personality. For 'sisterly', note that the community often also calls it 'uchi' or 'big sister'.
  'game': ["null"], // [String] | Retrieve villagers that appear in all listed games. For example, if you want only villagers that appear in both *New Horizons* and *Pocket Camp*, you would send in `?game=nh&game=pc`.
  'birthmonth': "birthmonth_example", // String | Retrieve villagers born in a specific month. Value may be the month's name (`jan`, `january`) or the integer representing the month (`01`, `1`).
  'birthday': "birthday_example", // String | Use with `birthmonth` to get villager(s) born on a specific day. Value should be an int, 1 through 31.
  'nhdetails': "nhdetails_example", // String | When set to `true`, an `nh_details` object will be included that contains *New Horizons* details about the villager. If the villager does not appear in *New Horizons*, the returned `nh_details` field will be set to null.
  'excludedetails': "excludedetails_example", // String | When set to `true`, only villager names are returned. Instead of an array of objects with all details, the return will be an array of strings.
  'thumbsize': 56 // Number | Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time.
};
apiInstance.villagersGet(X_API_KEY, acceptVersion, opts, (error, data, response) => {
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
 **X_API_KEY** | **String**| Your UUID secret key, granted to you by the Nookipedia team. Required for accessing the API. | 
 **acceptVersion** | **String**| The version of the API you are calling, written as &#x60;1.0.0&#x60;. This is specified as required as good practice, but it is not actually enforced by the API. If you do not specify a version, you will be served the latest version, which may eventually result in breaking changes. | 
 **name** | **String**| Villager name. For most names you will get back an array with one object, but note that names are not a unique identifier across the series, as there are 3 names that are shared by multiple villagers (Lulu, Petunia, Carmen). For those 3 names you will get back an array with 2 objects. How you disambiguate between these villagers is up to you. | [optional] 
 **species** | **String**| Retrieve villagers of a certain species. | [optional] 
 **personality** | **String**| Retrieve villagers with a certain personality. For &#39;sisterly&#39;, note that the community often also calls it &#39;uchi&#39; or &#39;big sister&#39;. | [optional] 
 **game** | [**[String]**](String.md)| Retrieve villagers that appear in all listed games. For example, if you want only villagers that appear in both *New Horizons* and *Pocket Camp*, you would send in &#x60;?game&#x3D;nh&amp;game&#x3D;pc&#x60;. | [optional] 
 **birthmonth** | **String**| Retrieve villagers born in a specific month. Value may be the month&#39;s name (&#x60;jan&#x60;, &#x60;january&#x60;) or the integer representing the month (&#x60;01&#x60;, &#x60;1&#x60;). | [optional] 
 **birthday** | **String**| Use with &#x60;birthmonth&#x60; to get villager(s) born on a specific day. Value should be an int, 1 through 31. | [optional] 
 **nhdetails** | **String**| When set to &#x60;true&#x60;, an &#x60;nh_details&#x60; object will be included that contains *New Horizons* details about the villager. If the villager does not appear in *New Horizons*, the returned &#x60;nh_details&#x60; field will be set to null. | [optional] 
 **excludedetails** | **String**| When set to &#x60;true&#x60;, only villager names are returned. Instead of an array of objects with all details, the return will be an array of strings. | [optional] 
 **thumbsize** | **Number**| Specify the desired width of returned image URLs. When unspecified, the linked image(s) returned by the API will be full-resolution. Note that images can only be reduced in size; specifying a width greater than than the maximum size will return the default full-size image URL. Note that requesting specific image sizes for long lists may result in a very long response time. | [optional] 

### Return type

[**[Villager]**](Villager.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

