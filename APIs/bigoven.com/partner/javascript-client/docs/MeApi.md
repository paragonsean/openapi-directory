# 1000000RecipeAndGroceryListApiV2.MeApi

All URIs are relative to *https://api2.bigoven.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meGetOptions**](MeApi.md#meGetOptions) | **GET** /me/preferences/options | Gets the options.
[**meIndex**](MeApi.md#meIndex) | **GET** /me | Indexes this instance.
[**meProfilePut**](MeApi.md#meProfilePut) | **PUT** /me/profile | Puts me.
[**mePutMe**](MeApi.md#mePutMe) | **PUT** /me | Puts me.
[**mePutMePersonal**](MeApi.md#mePutMePersonal) | **PUT** /me/personal | Puts me personal.
[**mePutMePreferences**](MeApi.md#mePutMePreferences) | **PUT** /me/preferences | Puts me preferences.
[**meSkinny**](MeApi.md#meSkinny) | **GET** /me/skinny | Skinnies this instance.



## meGetOptions

> API2ControllersWebAPIMeControllerPreferenceOptions meGetOptions()

Gets the options.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.MeApi();
apiInstance.meGetOptions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**API2ControllersWebAPIMeControllerPreferenceOptions**](API2ControllersWebAPIMeControllerPreferenceOptions.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## meIndex

> API2ModelsBigOvenUser meIndex()

Indexes this instance.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.MeApi();
apiInstance.meIndex((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**API2ModelsBigOvenUser**](API2ModelsBigOvenUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## meProfilePut

> API2ModelsBigOvenUser meProfilePut(aPI2ModelsProfile)

Puts me.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.MeApi();
let aPI2ModelsProfile = new 1000000RecipeAndGroceryListApiV2.API2ModelsProfile(); // API2ModelsProfile | The req.
apiInstance.meProfilePut(aPI2ModelsProfile, (error, data, response) => {
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
 **aPI2ModelsProfile** | [**API2ModelsProfile**](API2ModelsProfile.md)| The req. | 

### Return type

[**API2ModelsBigOvenUser**](API2ModelsBigOvenUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## mePutMe

> API2ModelsBigOvenUser mePutMe(aPI2ModelsBigOvenUser)

Puts me.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.MeApi();
let aPI2ModelsBigOvenUser = new 1000000RecipeAndGroceryListApiV2.API2ModelsBigOvenUser(); // API2ModelsBigOvenUser | The req.
apiInstance.mePutMe(aPI2ModelsBigOvenUser, (error, data, response) => {
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
 **aPI2ModelsBigOvenUser** | [**API2ModelsBigOvenUser**](API2ModelsBigOvenUser.md)| The req. | 

### Return type

[**API2ModelsBigOvenUser**](API2ModelsBigOvenUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## mePutMePersonal

> API2ModelsBigOvenUser mePutMePersonal(aPI2ModelsPersonal)

Puts me personal.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.MeApi();
let aPI2ModelsPersonal = new 1000000RecipeAndGroceryListApiV2.API2ModelsPersonal(); // API2ModelsPersonal | The req.
apiInstance.mePutMePersonal(aPI2ModelsPersonal, (error, data, response) => {
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
 **aPI2ModelsPersonal** | [**API2ModelsPersonal**](API2ModelsPersonal.md)| The req. | 

### Return type

[**API2ModelsBigOvenUser**](API2ModelsBigOvenUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## mePutMePreferences

> API2ModelsBigOvenUser mePutMePreferences(aPI2ModelsPreference)

Puts me preferences.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.MeApi();
let aPI2ModelsPreference = new 1000000RecipeAndGroceryListApiV2.API2ModelsPreference(); // API2ModelsPreference | The req.
apiInstance.mePutMePreferences(aPI2ModelsPreference, (error, data, response) => {
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
 **aPI2ModelsPreference** | [**API2ModelsPreference**](API2ModelsPreference.md)| The req. | 

### Return type

[**API2ModelsBigOvenUser**](API2ModelsBigOvenUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## meSkinny

> API2ModelsBigOvenUser meSkinny()

Skinnies this instance.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.MeApi();
apiInstance.meSkinny((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**API2ModelsBigOvenUser**](API2ModelsBigOvenUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

