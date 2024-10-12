# NoteApi

All URIs are relative to *https://api2.bigoven.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**noteDelete**](NoteApi.md#noteDelete) | **DELETE** /recipe/{recipeId}/note/{noteId} | Delete a review                  do a DELETE Http request of /note/{ID} |
| [**noteGet**](NoteApi.md#noteGet) | **GET** /recipe/{recipeId}/note/{noteId} | Get a given note. Make sure you&#39;re passing authentication information in the header for the user who owns the note. |
| [**noteGetNotes**](NoteApi.md#noteGetNotes) | **GET** /recipe/{recipeId}/notes | recipe/100/notes |
| [**notePost**](NoteApi.md#notePost) | **POST** /recipe/{recipeId}/note | HTTP POST a new note into the system. |
| [**notePut**](NoteApi.md#notePut) | **PUT** /recipe/{recipeId}/note/{noteId} | HTTP PUT (update) a Recipe note (RecipeNote). |


<a id="noteDelete"></a>
# **noteDelete**
> Object noteDelete(recipeId, noteId)

Delete a review                  do a DELETE Http request of /note/{ID}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    NoteApi apiInstance = new NoteApi(defaultClient);
    Integer recipeId = 56; // Integer | recipeId (int)
    Integer noteId = 56; // Integer | noteId (int)
    try {
      Object result = apiInstance.noteDelete(recipeId, noteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NoteApi#noteDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **recipeId** | **Integer**| recipeId (int) | |
| **noteId** | **Integer**| noteId (int) | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="noteGet"></a>
# **noteGet**
> BigOvenModelAPIRecipeNote noteGet(recipeId, noteId)

Get a given note. Make sure you&#39;re passing authentication information in the header for the user who owns the note.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    NoteApi apiInstance = new NoteApi(defaultClient);
    Integer recipeId = 56; // Integer | recipe identifier (integer)
    Integer noteId = 56; // Integer | The note ID (note -- it's not the RecipeID)
    try {
      BigOvenModelAPIRecipeNote result = apiInstance.noteGet(recipeId, noteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NoteApi#noteGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **recipeId** | **Integer**| recipe identifier (integer) | |
| **noteId** | **Integer**| The note ID (note -- it&#39;s not the RecipeID) | |

### Return type

[**BigOvenModelAPIRecipeNote**](BigOvenModelAPIRecipeNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="noteGetNotes"></a>
# **noteGetNotes**
> BigOvenModelAPIRecipeNoteList noteGetNotes(recipeId, pg, rpp)

recipe/100/notes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    NoteApi apiInstance = new NoteApi(defaultClient);
    Integer recipeId = 56; // Integer | recipeId (int)
    Integer pg = 56; // Integer | page (int, starting from 1)
    Integer rpp = 56; // Integer | recipeId
    try {
      BigOvenModelAPIRecipeNoteList result = apiInstance.noteGetNotes(recipeId, pg, rpp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NoteApi#noteGetNotes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **recipeId** | **Integer**| recipeId (int) | |
| **pg** | **Integer**| page (int, starting from 1) | [optional] |
| **rpp** | **Integer**| recipeId | [optional] |

### Return type

[**BigOvenModelAPIRecipeNoteList**](BigOvenModelAPIRecipeNoteList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="notePost"></a>
# **notePost**
> BigOvenModelAPI2RecipeNote notePost(recipeId, apI2ControllersWebAPINoteControllerNoteRequest)

HTTP POST a new note into the system.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    NoteApi apiInstance = new NoteApi(defaultClient);
    Integer recipeId = 56; // Integer | recipeId (int)
    API2ControllersWebAPINoteControllerNoteRequest apI2ControllersWebAPINoteControllerNoteRequest = new API2ControllersWebAPINoteControllerNoteRequest(); // API2ControllersWebAPINoteControllerNoteRequest | a recipe note, with fields: Date (YYYY-MM-DD string), Notes (string), People (string), Variations (string), RecipeID (int?)
    try {
      BigOvenModelAPI2RecipeNote result = apiInstance.notePost(recipeId, apI2ControllersWebAPINoteControllerNoteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NoteApi#notePost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **recipeId** | **Integer**| recipeId (int) | |
| **apI2ControllersWebAPINoteControllerNoteRequest** | [**API2ControllersWebAPINoteControllerNoteRequest**](API2ControllersWebAPINoteControllerNoteRequest.md)| a recipe note, with fields: Date (YYYY-MM-DD string), Notes (string), People (string), Variations (string), RecipeID (int?) | |

### Return type

[**BigOvenModelAPI2RecipeNote**](BigOvenModelAPI2RecipeNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="notePut"></a>
# **notePut**
> BigOvenModelAPIRecipeNote notePut(recipeId, noteId, apI2ControllersWebAPINoteControllerNoteRequest)

HTTP PUT (update) a Recipe note (RecipeNote).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    NoteApi apiInstance = new NoteApi(defaultClient);
    Integer recipeId = 56; // Integer | 
    Integer noteId = 56; // Integer | 
    API2ControllersWebAPINoteControllerNoteRequest apI2ControllersWebAPINoteControllerNoteRequest = new API2ControllersWebAPINoteControllerNoteRequest(); // API2ControllersWebAPINoteControllerNoteRequest | 
    try {
      BigOvenModelAPIRecipeNote result = apiInstance.notePut(recipeId, noteId, apI2ControllersWebAPINoteControllerNoteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NoteApi#notePut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **recipeId** | **Integer**|  | |
| **noteId** | **Integer**|  | |
| **apI2ControllersWebAPINoteControllerNoteRequest** | [**API2ControllersWebAPINoteControllerNoteRequest**](API2ControllersWebAPINoteControllerNoteRequest.md)|  | |

### Return type

[**BigOvenModelAPIRecipeNote**](BigOvenModelAPIRecipeNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

