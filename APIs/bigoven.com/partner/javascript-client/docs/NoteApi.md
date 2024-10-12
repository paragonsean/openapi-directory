# 1000000RecipeAndGroceryListApiV2.NoteApi

All URIs are relative to *https://api2.bigoven.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**noteDelete**](NoteApi.md#noteDelete) | **DELETE** /recipe/{recipeId}/note/{noteId} | Delete a review                  do a DELETE Http request of /note/{ID}
[**noteGet**](NoteApi.md#noteGet) | **GET** /recipe/{recipeId}/note/{noteId} | Get a given note. Make sure you&#39;re passing authentication information in the header for the user who owns the note.
[**noteGetNotes**](NoteApi.md#noteGetNotes) | **GET** /recipe/{recipeId}/notes | recipe/100/notes
[**notePost**](NoteApi.md#notePost) | **POST** /recipe/{recipeId}/note | HTTP POST a new note into the system.
[**notePut**](NoteApi.md#notePut) | **PUT** /recipe/{recipeId}/note/{noteId} | HTTP PUT (update) a Recipe note (RecipeNote).



## noteDelete

> Object noteDelete(recipeId, noteId)

Delete a review                  do a DELETE Http request of /note/{ID}

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.NoteApi();
let recipeId = 56; // Number | recipeId (int)
let noteId = 56; // Number | noteId (int)
apiInstance.noteDelete(recipeId, noteId, (error, data, response) => {
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
 **recipeId** | **Number**| recipeId (int) | 
 **noteId** | **Number**| noteId (int) | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## noteGet

> BigOvenModelAPIRecipeNote noteGet(recipeId, noteId)

Get a given note. Make sure you&#39;re passing authentication information in the header for the user who owns the note.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.NoteApi();
let recipeId = 56; // Number | recipe identifier (integer)
let noteId = 56; // Number | The note ID (note -- it's not the RecipeID)
apiInstance.noteGet(recipeId, noteId, (error, data, response) => {
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
 **recipeId** | **Number**| recipe identifier (integer) | 
 **noteId** | **Number**| The note ID (note -- it&#39;s not the RecipeID) | 

### Return type

[**BigOvenModelAPIRecipeNote**](BigOvenModelAPIRecipeNote.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## noteGetNotes

> BigOvenModelAPIRecipeNoteList noteGetNotes(recipeId, opts)

recipe/100/notes

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.NoteApi();
let recipeId = 56; // Number | recipeId (int)
let opts = {
  'pg': 56, // Number | page (int, starting from 1)
  'rpp': 56 // Number | recipeId
};
apiInstance.noteGetNotes(recipeId, opts, (error, data, response) => {
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
 **recipeId** | **Number**| recipeId (int) | 
 **pg** | **Number**| page (int, starting from 1) | [optional] 
 **rpp** | **Number**| recipeId | [optional] 

### Return type

[**BigOvenModelAPIRecipeNoteList**](BigOvenModelAPIRecipeNoteList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## notePost

> BigOvenModelAPI2RecipeNote notePost(recipeId, aPI2ControllersWebAPINoteControllerNoteRequest)

HTTP POST a new note into the system.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.NoteApi();
let recipeId = 56; // Number | recipeId (int)
let aPI2ControllersWebAPINoteControllerNoteRequest = new 1000000RecipeAndGroceryListApiV2.API2ControllersWebAPINoteControllerNoteRequest(); // API2ControllersWebAPINoteControllerNoteRequest | a recipe note, with fields: Date (YYYY-MM-DD string), Notes (string), People (string), Variations (string), RecipeID (int?)
apiInstance.notePost(recipeId, aPI2ControllersWebAPINoteControllerNoteRequest, (error, data, response) => {
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
 **recipeId** | **Number**| recipeId (int) | 
 **aPI2ControllersWebAPINoteControllerNoteRequest** | [**API2ControllersWebAPINoteControllerNoteRequest**](API2ControllersWebAPINoteControllerNoteRequest.md)| a recipe note, with fields: Date (YYYY-MM-DD string), Notes (string), People (string), Variations (string), RecipeID (int?) | 

### Return type

[**BigOvenModelAPI2RecipeNote**](BigOvenModelAPI2RecipeNote.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## notePut

> BigOvenModelAPIRecipeNote notePut(recipeId, noteId, aPI2ControllersWebAPINoteControllerNoteRequest)

HTTP PUT (update) a Recipe note (RecipeNote).

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.NoteApi();
let recipeId = 56; // Number | 
let noteId = 56; // Number | 
let aPI2ControllersWebAPINoteControllerNoteRequest = new 1000000RecipeAndGroceryListApiV2.API2ControllersWebAPINoteControllerNoteRequest(); // API2ControllersWebAPINoteControllerNoteRequest | 
apiInstance.notePut(recipeId, noteId, aPI2ControllersWebAPINoteControllerNoteRequest, (error, data, response) => {
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
 **recipeId** | **Number**|  | 
 **noteId** | **Number**|  | 
 **aPI2ControllersWebAPINoteControllerNoteRequest** | [**API2ControllersWebAPINoteControllerNoteRequest**](API2ControllersWebAPINoteControllerNoteRequest.md)|  | 

### Return type

[**BigOvenModelAPIRecipeNote**](BigOvenModelAPIRecipeNote.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

