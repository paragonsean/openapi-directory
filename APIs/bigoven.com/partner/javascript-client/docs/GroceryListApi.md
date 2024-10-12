# 1000000RecipeAndGroceryListApiV2.GroceryListApi

All URIs are relative to *https://api2.bigoven.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groceryListAddRecipe**](GroceryListApi.md#groceryListAddRecipe) | **POST** /grocerylist/recipe | Add a Recipe to the grocery list.  In the request data, pass in recipeId, scale (scale&#x3D;1.0 says to keep the recipe the same size as originally posted), markAsPending (true/false) to indicate that              the lines in the recipe should be marked in a \&quot;pending\&quot; (unconfirmed by user) state.
[**groceryListDelete**](GroceryListApi.md#groceryListDelete) | **DELETE** /grocerylist | Delete all the items on a grocery list; faster operation than a sync with deleted items.
[**groceryListDeleteItemByGuid**](GroceryListApi.md#groceryListDeleteItemByGuid) | **DELETE** /grocerylist/item/{guid} | /grocerylist/item/{guid}  DELETE will delete this item assuming you own it.
[**groceryListDepartment**](GroceryListApi.md#groceryListDepartment) | **POST** /grocerylist/department | Departmentalize a list of strings -- used for ad-hoc grocery list item addition
[**groceryListGet**](GroceryListApi.md#groceryListGet) | **GET** /grocerylist | Get the user&#39;s grocery list.  User is determined by Basic Authentication.
[**groceryListGroceryListItemGuid**](GroceryListApi.md#groceryListGroceryListItemGuid) | **PUT** /grocerylist/item/{guid} | Update a grocery item by GUID
[**groceryListGroceryListRemoveMarkedItems**](GroceryListApi.md#groceryListGroceryListRemoveMarkedItems) | **POST** /grocerylist/clearcheckedlines | Clears the checked lines.
[**groceryListPost**](GroceryListApi.md#groceryListPost) | **POST** /grocerylist/line | Add a single line item to the grocery list
[**groceryListPostGroceryListSync**](GroceryListApi.md#groceryListPostGroceryListSync) | **POST** /grocerylist/sync | Synchronize the grocery list.  Call this with a POST to /grocerylist/sync
[**grocerylistItemPost**](GroceryListApi.md#grocerylistItemPost) | **POST** /grocerylist/item | Add a single line item to the grocery list



## groceryListAddRecipe

> Object groceryListAddRecipe(aPI2ControllersWebAPIGroceryListControllerPostGroceryListRecipeRequest)

Add a Recipe to the grocery list.  In the request data, pass in recipeId, scale (scale&#x3D;1.0 says to keep the recipe the same size as originally posted), markAsPending (true/false) to indicate that              the lines in the recipe should be marked in a \&quot;pending\&quot; (unconfirmed by user) state.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.GroceryListApi();
let aPI2ControllersWebAPIGroceryListControllerPostGroceryListRecipeRequest = new 1000000RecipeAndGroceryListApiV2.API2ControllersWebAPIGroceryListControllerPostGroceryListRecipeRequest(); // API2ControllersWebAPIGroceryListControllerPostGroceryListRecipeRequest | 
apiInstance.groceryListAddRecipe(aPI2ControllersWebAPIGroceryListControllerPostGroceryListRecipeRequest, (error, data, response) => {
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
 **aPI2ControllersWebAPIGroceryListControllerPostGroceryListRecipeRequest** | [**API2ControllersWebAPIGroceryListControllerPostGroceryListRecipeRequest**](API2ControllersWebAPIGroceryListControllerPostGroceryListRecipeRequest.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## groceryListDelete

> Object groceryListDelete()

Delete all the items on a grocery list; faster operation than a sync with deleted items.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.GroceryListApi();
apiInstance.groceryListDelete((error, data, response) => {
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


## groceryListDeleteItemByGuid

> Object groceryListDeleteItemByGuid(guid)

/grocerylist/item/{guid}  DELETE will delete this item assuming you own it.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.GroceryListApi();
let guid = "guid_example"; // String | 
apiInstance.groceryListDeleteItemByGuid(guid, (error, data, response) => {
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
 **guid** | **String**|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## groceryListDepartment

> [API2GroceryListDepartmentResult] groceryListDepartment(aPI2ControllersWebAPIGroceryListControllerDepartmentModel)

Departmentalize a list of strings -- used for ad-hoc grocery list item addition

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.GroceryListApi();
let aPI2ControllersWebAPIGroceryListControllerDepartmentModel = new 1000000RecipeAndGroceryListApiV2.API2ControllersWebAPIGroceryListControllerDepartmentModel(); // API2ControllersWebAPIGroceryListControllerDepartmentModel | see DepartmentModel for the request payload
apiInstance.groceryListDepartment(aPI2ControllersWebAPIGroceryListControllerDepartmentModel, (error, data, response) => {
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
 **aPI2ControllersWebAPIGroceryListControllerDepartmentModel** | [**API2ControllersWebAPIGroceryListControllerDepartmentModel**](API2ControllersWebAPIGroceryListControllerDepartmentModel.md)| see DepartmentModel for the request payload | 

### Return type

[**[API2GroceryListDepartmentResult]**](API2GroceryListDepartmentResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## groceryListGet

> BigOvenModelAPI2GroceryList groceryListGet()

Get the user&#39;s grocery list.  User is determined by Basic Authentication.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.GroceryListApi();
apiInstance.groceryListGet((error, data, response) => {
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

[**BigOvenModelAPI2GroceryList**](BigOvenModelAPI2GroceryList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## groceryListGroceryListItemGuid

> Object groceryListGroceryListItemGuid(guid, aPI2ControllersWebAPIGroceryListControllerUpdateItemByGuidRequest)

Update a grocery item by GUID

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.GroceryListApi();
let guid = "guid_example"; // String | 
let aPI2ControllersWebAPIGroceryListControllerUpdateItemByGuidRequest = new 1000000RecipeAndGroceryListApiV2.API2ControllersWebAPIGroceryListControllerUpdateItemByGuidRequest(); // API2ControllersWebAPIGroceryListControllerUpdateItemByGuidRequest | 
apiInstance.groceryListGroceryListItemGuid(guid, aPI2ControllersWebAPIGroceryListControllerUpdateItemByGuidRequest, (error, data, response) => {
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
 **guid** | **String**|  | 
 **aPI2ControllersWebAPIGroceryListControllerUpdateItemByGuidRequest** | [**API2ControllersWebAPIGroceryListControllerUpdateItemByGuidRequest**](API2ControllersWebAPIGroceryListControllerUpdateItemByGuidRequest.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## groceryListGroceryListRemoveMarkedItems

> BigOvenModelAPI2GroceryList groceryListGroceryListRemoveMarkedItems()

Clears the checked lines.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.GroceryListApi();
apiInstance.groceryListGroceryListRemoveMarkedItems((error, data, response) => {
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

[**BigOvenModelAPI2GroceryList**](BigOvenModelAPI2GroceryList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## groceryListPost

> BigOvenModelShoppingListLine groceryListPost(aPI2ControllersWebAPIGroceryListControllerPostGroceryListAddLineRequest)

Add a single line item to the grocery list

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.GroceryListApi();
let aPI2ControllersWebAPIGroceryListControllerPostGroceryListAddLineRequest = new 1000000RecipeAndGroceryListApiV2.API2ControllersWebAPIGroceryListControllerPostGroceryListAddLineRequest(); // API2ControllersWebAPIGroceryListControllerPostGroceryListAddLineRequest | name, quantity, unit, notes, department
apiInstance.groceryListPost(aPI2ControllersWebAPIGroceryListControllerPostGroceryListAddLineRequest, (error, data, response) => {
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
 **aPI2ControllersWebAPIGroceryListControllerPostGroceryListAddLineRequest** | [**API2ControllersWebAPIGroceryListControllerPostGroceryListAddLineRequest**](API2ControllersWebAPIGroceryListControllerPostGroceryListAddLineRequest.md)| name, quantity, unit, notes, department | 

### Return type

[**BigOvenModelShoppingListLine**](BigOvenModelShoppingListLine.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## groceryListPostGroceryListSync

> Object groceryListPostGroceryListSync(aPI2ControllersWebAPIGroceryListControllerPostGroceryListSyncRequest)

Synchronize the grocery list.  Call this with a POST to /grocerylist/sync

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.GroceryListApi();
let aPI2ControllersWebAPIGroceryListControllerPostGroceryListSyncRequest = new 1000000RecipeAndGroceryListApiV2.API2ControllersWebAPIGroceryListControllerPostGroceryListSyncRequest(); // API2ControllersWebAPIGroceryListControllerPostGroceryListSyncRequest | 
apiInstance.groceryListPostGroceryListSync(aPI2ControllersWebAPIGroceryListControllerPostGroceryListSyncRequest, (error, data, response) => {
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
 **aPI2ControllersWebAPIGroceryListControllerPostGroceryListSyncRequest** | [**API2ControllersWebAPIGroceryListControllerPostGroceryListSyncRequest**](API2ControllersWebAPIGroceryListControllerPostGroceryListSyncRequest.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## grocerylistItemPost

> BigOvenModelShoppingListLine grocerylistItemPost(aPI2ControllersWebAPIGroceryListControllerPostToGroceryListRecipeRequest)

Add a single line item to the grocery list

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.GroceryListApi();
let aPI2ControllersWebAPIGroceryListControllerPostToGroceryListRecipeRequest = new 1000000RecipeAndGroceryListApiV2.API2ControllersWebAPIGroceryListControllerPostToGroceryListRecipeRequest(); // API2ControllersWebAPIGroceryListControllerPostToGroceryListRecipeRequest | name, quantity, unit, notes, department
apiInstance.grocerylistItemPost(aPI2ControllersWebAPIGroceryListControllerPostToGroceryListRecipeRequest, (error, data, response) => {
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
 **aPI2ControllersWebAPIGroceryListControllerPostToGroceryListRecipeRequest** | [**API2ControllersWebAPIGroceryListControllerPostToGroceryListRecipeRequest**](API2ControllersWebAPIGroceryListControllerPostToGroceryListRecipeRequest.md)| name, quantity, unit, notes, department | 

### Return type

[**BigOvenModelShoppingListLine**](BigOvenModelShoppingListLine.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

