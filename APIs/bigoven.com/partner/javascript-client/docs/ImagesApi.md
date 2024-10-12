# 1000000RecipeAndGroceryListApiV2.ImagesApi

All URIs are relative to *https://api2.bigoven.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**imagesGet**](ImagesApi.md#imagesGet) | **GET** /recipe/{recipeId}/images | Get all the images for a recipe. DEPRECATED. Please use /recipe/{recipeId}/photos.
[**imagesGetPendingByUser**](ImagesApi.md#imagesGetPendingByUser) | **GET** /recipe/photos/pending | Gets the pending by user.
[**imagesGetRecipePhotos**](ImagesApi.md#imagesGetRecipePhotos) | **GET** /recipe/{recipeId}/photos | Get all the photos for a recipe
[**imagesGetScanImages**](ImagesApi.md#imagesGetScanImages) | **GET** /recipe/{recipeId}/scans | Gets a list of RecipeScan images for the recipe. There will be at most 3 per recipe.
[**imagesUploadRecipeImage**](ImagesApi.md#imagesUploadRecipeImage) | **POST** /recipe/{recipeId}/image | POST: /recipe/{recipeId}/image?lat&#x3D;42&amp;amp;lng&#x3D;21&amp;amp;caption&#x3D;this%20is%20my%20caption                              Note that caption, lng and lat are all optional, but must go on the request URI as params because this endpoint               needs a multipart/mime content header and will not parse JSON in the body along with it.                             Testing with Postman (validated 11/20/2015):               1) Remove the Content-Type header; add authentication information               2) On the request, click Body and choose \&quot;form-data\&quot;, then add a line item with \&quot;key\&quot; column set to \&quot;file\&quot; and on the right,               change the type of the input from Text to File.  Browse and choose a JPG.
[**imagesUploadUserAvatar**](ImagesApi.md#imagesUploadUserAvatar) | **POST** /image/avatar | POST: /image/avatar                             Testing with Postman (validated 11/20/2015):              1) Remove the Content-Type header; add authentication information              2) On the request, click Body and choose \&quot;form-data\&quot;, then add a line item with \&quot;key\&quot; column set to \&quot;file\&quot; and on the right,              change the type of the input from Text to File.  Browse and choose a JPG.



## imagesGet

> [BigOvenModelAPIImage] imagesGet(recipeId)

Get all the images for a recipe. DEPRECATED. Please use /recipe/{recipeId}/photos.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.ImagesApi();
let recipeId = 56; // Number | Recipe ID (required)
apiInstance.imagesGet(recipeId, (error, data, response) => {
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
 **recipeId** | **Number**| Recipe ID (required) | 

### Return type

[**[BigOvenModelAPIImage]**](BigOvenModelAPIImage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## imagesGetPendingByUser

> API2ControllersWebAPIImagesControllerRecipePhotosResponse imagesGetPendingByUser()

Gets the pending by user.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.ImagesApi();
apiInstance.imagesGetPendingByUser((error, data, response) => {
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

[**API2ControllersWebAPIImagesControllerRecipePhotosResponse**](API2ControllersWebAPIImagesControllerRecipePhotosResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## imagesGetRecipePhotos

> API2ControllersWebAPIImagesControllerRecipePhotosResponse imagesGetRecipePhotos(recipeId, opts)

Get all the photos for a recipe

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.ImagesApi();
let recipeId = 56; // Number | Recipe ID (required)
let opts = {
  'pg': 56, // Number | 
  'rpp': 56 // Number | 
};
apiInstance.imagesGetRecipePhotos(recipeId, opts, (error, data, response) => {
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
 **recipeId** | **Number**| Recipe ID (required) | 
 **pg** | **Number**|  | [optional] 
 **rpp** | **Number**|  | [optional] 

### Return type

[**API2ControllersWebAPIImagesControllerRecipePhotosResponse**](API2ControllersWebAPIImagesControllerRecipePhotosResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## imagesGetScanImages

> [BigOvenModelAPIImage] imagesGetScanImages(recipeId)

Gets a list of RecipeScan images for the recipe. There will be at most 3 per recipe.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.ImagesApi();
let recipeId = 56; // Number | the recipe identifier (int)
apiInstance.imagesGetScanImages(recipeId, (error, data, response) => {
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
 **recipeId** | **Number**| the recipe identifier (int) | 

### Return type

[**[BigOvenModelAPIImage]**](BigOvenModelAPIImage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## imagesUploadRecipeImage

> Object imagesUploadRecipeImage(recipeId, opts)

POST: /recipe/{recipeId}/image?lat&#x3D;42&amp;amp;lng&#x3D;21&amp;amp;caption&#x3D;this%20is%20my%20caption                              Note that caption, lng and lat are all optional, but must go on the request URI as params because this endpoint               needs a multipart/mime content header and will not parse JSON in the body along with it.                             Testing with Postman (validated 11/20/2015):               1) Remove the Content-Type header; add authentication information               2) On the request, click Body and choose \&quot;form-data\&quot;, then add a line item with \&quot;key\&quot; column set to \&quot;file\&quot; and on the right,               change the type of the input from Text to File.  Browse and choose a JPG.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.ImagesApi();
let recipeId = "recipeId_example"; // String | 
let opts = {
  'caption': "caption_example", // String | 
  'lat': 3.4, // Number | 
  'lng': 3.4 // Number | 
};
apiInstance.imagesUploadRecipeImage(recipeId, opts, (error, data, response) => {
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
 **recipeId** | **String**|  | 
 **caption** | **String**|  | [optional] 
 **lat** | **Number**|  | [optional] 
 **lng** | **Number**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## imagesUploadUserAvatar

> Object imagesUploadUserAvatar()

POST: /image/avatar                             Testing with Postman (validated 11/20/2015):              1) Remove the Content-Type header; add authentication information              2) On the request, click Body and choose \&quot;form-data\&quot;, then add a line item with \&quot;key\&quot; column set to \&quot;file\&quot; and on the right,              change the type of the input from Text to File.  Browse and choose a JPG.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.ImagesApi();
apiInstance.imagesUploadUserAvatar((error, data, response) => {
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

