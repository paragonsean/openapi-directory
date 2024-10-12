# GroceryListApi

All URIs are relative to *https://api2.bigoven.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**groceryListAddRecipe**](GroceryListApi.md#groceryListAddRecipe) | **POST** /grocerylist/recipe | Add a Recipe to the grocery list.  In the request data, pass in recipeId, scale (scale&#x3D;1.0 says to keep the recipe the same size as originally posted), markAsPending (true/false) to indicate that              the lines in the recipe should be marked in a \&quot;pending\&quot; (unconfirmed by user) state. |
| [**groceryListDelete**](GroceryListApi.md#groceryListDelete) | **DELETE** /grocerylist | Delete all the items on a grocery list; faster operation than a sync with deleted items. |
| [**groceryListDeleteItemByGuid**](GroceryListApi.md#groceryListDeleteItemByGuid) | **DELETE** /grocerylist/item/{guid} | /grocerylist/item/{guid}  DELETE will delete this item assuming you own it. |
| [**groceryListDepartment**](GroceryListApi.md#groceryListDepartment) | **POST** /grocerylist/department | Departmentalize a list of strings -- used for ad-hoc grocery list item addition |
| [**groceryListGet**](GroceryListApi.md#groceryListGet) | **GET** /grocerylist | Get the user&#39;s grocery list.  User is determined by Basic Authentication. |
| [**groceryListGroceryListItemGuid**](GroceryListApi.md#groceryListGroceryListItemGuid) | **PUT** /grocerylist/item/{guid} | Update a grocery item by GUID |
| [**groceryListGroceryListRemoveMarkedItems**](GroceryListApi.md#groceryListGroceryListRemoveMarkedItems) | **POST** /grocerylist/clearcheckedlines | Clears the checked lines. |
| [**groceryListPost**](GroceryListApi.md#groceryListPost) | **POST** /grocerylist/line | Add a single line item to the grocery list |
| [**groceryListPostGroceryListSync**](GroceryListApi.md#groceryListPostGroceryListSync) | **POST** /grocerylist/sync | Synchronize the grocery list.  Call this with a POST to /grocerylist/sync |
| [**grocerylistItemPost**](GroceryListApi.md#grocerylistItemPost) | **POST** /grocerylist/item | Add a single line item to the grocery list |


<a id="groceryListAddRecipe"></a>
# **groceryListAddRecipe**
> Object groceryListAddRecipe(apI2ControllersWebAPIGroceryListControllerPostGroceryListRecipeRequest)

Add a Recipe to the grocery list.  In the request data, pass in recipeId, scale (scale&#x3D;1.0 says to keep the recipe the same size as originally posted), markAsPending (true/false) to indicate that              the lines in the recipe should be marked in a \&quot;pending\&quot; (unconfirmed by user) state.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroceryListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    GroceryListApi apiInstance = new GroceryListApi(defaultClient);
    API2ControllersWebAPIGroceryListControllerPostGroceryListRecipeRequest apI2ControllersWebAPIGroceryListControllerPostGroceryListRecipeRequest = new API2ControllersWebAPIGroceryListControllerPostGroceryListRecipeRequest(); // API2ControllersWebAPIGroceryListControllerPostGroceryListRecipeRequest | 
    try {
      Object result = apiInstance.groceryListAddRecipe(apI2ControllersWebAPIGroceryListControllerPostGroceryListRecipeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroceryListApi#groceryListAddRecipe");
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
| **apI2ControllersWebAPIGroceryListControllerPostGroceryListRecipeRequest** | [**API2ControllersWebAPIGroceryListControllerPostGroceryListRecipeRequest**](API2ControllersWebAPIGroceryListControllerPostGroceryListRecipeRequest.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="groceryListDelete"></a>
# **groceryListDelete**
> Object groceryListDelete()

Delete all the items on a grocery list; faster operation than a sync with deleted items.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroceryListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    GroceryListApi apiInstance = new GroceryListApi(defaultClient);
    try {
      Object result = apiInstance.groceryListDelete();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroceryListApi#groceryListDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="groceryListDeleteItemByGuid"></a>
# **groceryListDeleteItemByGuid**
> Object groceryListDeleteItemByGuid(guid)

/grocerylist/item/{guid}  DELETE will delete this item assuming you own it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroceryListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    GroceryListApi apiInstance = new GroceryListApi(defaultClient);
    String guid = "guid_example"; // String | 
    try {
      Object result = apiInstance.groceryListDeleteItemByGuid(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroceryListApi#groceryListDeleteItemByGuid");
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
| **guid** | **String**|  | |

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

<a id="groceryListDepartment"></a>
# **groceryListDepartment**
> List&lt;API2GroceryListDepartmentResult&gt; groceryListDepartment(apI2ControllersWebAPIGroceryListControllerDepartmentModel)

Departmentalize a list of strings -- used for ad-hoc grocery list item addition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroceryListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    GroceryListApi apiInstance = new GroceryListApi(defaultClient);
    API2ControllersWebAPIGroceryListControllerDepartmentModel apI2ControllersWebAPIGroceryListControllerDepartmentModel = new API2ControllersWebAPIGroceryListControllerDepartmentModel(); // API2ControllersWebAPIGroceryListControllerDepartmentModel | see DepartmentModel for the request payload
    try {
      List<API2GroceryListDepartmentResult> result = apiInstance.groceryListDepartment(apI2ControllersWebAPIGroceryListControllerDepartmentModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroceryListApi#groceryListDepartment");
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
| **apI2ControllersWebAPIGroceryListControllerDepartmentModel** | [**API2ControllersWebAPIGroceryListControllerDepartmentModel**](API2ControllersWebAPIGroceryListControllerDepartmentModel.md)| see DepartmentModel for the request payload | |

### Return type

[**List&lt;API2GroceryListDepartmentResult&gt;**](API2GroceryListDepartmentResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="groceryListGet"></a>
# **groceryListGet**
> BigOvenModelAPI2GroceryList groceryListGet()

Get the user&#39;s grocery list.  User is determined by Basic Authentication.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroceryListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    GroceryListApi apiInstance = new GroceryListApi(defaultClient);
    try {
      BigOvenModelAPI2GroceryList result = apiInstance.groceryListGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroceryListApi#groceryListGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="groceryListGroceryListItemGuid"></a>
# **groceryListGroceryListItemGuid**
> Object groceryListGroceryListItemGuid(guid, apI2ControllersWebAPIGroceryListControllerUpdateItemByGuidRequest)

Update a grocery item by GUID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroceryListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    GroceryListApi apiInstance = new GroceryListApi(defaultClient);
    String guid = "guid_example"; // String | 
    API2ControllersWebAPIGroceryListControllerUpdateItemByGuidRequest apI2ControllersWebAPIGroceryListControllerUpdateItemByGuidRequest = new API2ControllersWebAPIGroceryListControllerUpdateItemByGuidRequest(); // API2ControllersWebAPIGroceryListControllerUpdateItemByGuidRequest | 
    try {
      Object result = apiInstance.groceryListGroceryListItemGuid(guid, apI2ControllersWebAPIGroceryListControllerUpdateItemByGuidRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroceryListApi#groceryListGroceryListItemGuid");
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
| **guid** | **String**|  | |
| **apI2ControllersWebAPIGroceryListControllerUpdateItemByGuidRequest** | [**API2ControllersWebAPIGroceryListControllerUpdateItemByGuidRequest**](API2ControllersWebAPIGroceryListControllerUpdateItemByGuidRequest.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="groceryListGroceryListRemoveMarkedItems"></a>
# **groceryListGroceryListRemoveMarkedItems**
> BigOvenModelAPI2GroceryList groceryListGroceryListRemoveMarkedItems()

Clears the checked lines.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroceryListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    GroceryListApi apiInstance = new GroceryListApi(defaultClient);
    try {
      BigOvenModelAPI2GroceryList result = apiInstance.groceryListGroceryListRemoveMarkedItems();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroceryListApi#groceryListGroceryListRemoveMarkedItems");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="groceryListPost"></a>
# **groceryListPost**
> BigOvenModelShoppingListLine groceryListPost(apI2ControllersWebAPIGroceryListControllerPostGroceryListAddLineRequest)

Add a single line item to the grocery list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroceryListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    GroceryListApi apiInstance = new GroceryListApi(defaultClient);
    API2ControllersWebAPIGroceryListControllerPostGroceryListAddLineRequest apI2ControllersWebAPIGroceryListControllerPostGroceryListAddLineRequest = new API2ControllersWebAPIGroceryListControllerPostGroceryListAddLineRequest(); // API2ControllersWebAPIGroceryListControllerPostGroceryListAddLineRequest | name, quantity, unit, notes, department
    try {
      BigOvenModelShoppingListLine result = apiInstance.groceryListPost(apI2ControllersWebAPIGroceryListControllerPostGroceryListAddLineRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroceryListApi#groceryListPost");
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
| **apI2ControllersWebAPIGroceryListControllerPostGroceryListAddLineRequest** | [**API2ControllersWebAPIGroceryListControllerPostGroceryListAddLineRequest**](API2ControllersWebAPIGroceryListControllerPostGroceryListAddLineRequest.md)| name, quantity, unit, notes, department | |

### Return type

[**BigOvenModelShoppingListLine**](BigOvenModelShoppingListLine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="groceryListPostGroceryListSync"></a>
# **groceryListPostGroceryListSync**
> Object groceryListPostGroceryListSync(apI2ControllersWebAPIGroceryListControllerPostGroceryListSyncRequest)

Synchronize the grocery list.  Call this with a POST to /grocerylist/sync

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroceryListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    GroceryListApi apiInstance = new GroceryListApi(defaultClient);
    API2ControllersWebAPIGroceryListControllerPostGroceryListSyncRequest apI2ControllersWebAPIGroceryListControllerPostGroceryListSyncRequest = new API2ControllersWebAPIGroceryListControllerPostGroceryListSyncRequest(); // API2ControllersWebAPIGroceryListControllerPostGroceryListSyncRequest | 
    try {
      Object result = apiInstance.groceryListPostGroceryListSync(apI2ControllersWebAPIGroceryListControllerPostGroceryListSyncRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroceryListApi#groceryListPostGroceryListSync");
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
| **apI2ControllersWebAPIGroceryListControllerPostGroceryListSyncRequest** | [**API2ControllersWebAPIGroceryListControllerPostGroceryListSyncRequest**](API2ControllersWebAPIGroceryListControllerPostGroceryListSyncRequest.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="grocerylistItemPost"></a>
# **grocerylistItemPost**
> BigOvenModelShoppingListLine grocerylistItemPost(apI2ControllersWebAPIGroceryListControllerPostToGroceryListRecipeRequest)

Add a single line item to the grocery list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroceryListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    GroceryListApi apiInstance = new GroceryListApi(defaultClient);
    API2ControllersWebAPIGroceryListControllerPostToGroceryListRecipeRequest apI2ControllersWebAPIGroceryListControllerPostToGroceryListRecipeRequest = new API2ControllersWebAPIGroceryListControllerPostToGroceryListRecipeRequest(); // API2ControllersWebAPIGroceryListControllerPostToGroceryListRecipeRequest | name, quantity, unit, notes, department
    try {
      BigOvenModelShoppingListLine result = apiInstance.grocerylistItemPost(apI2ControllersWebAPIGroceryListControllerPostToGroceryListRecipeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroceryListApi#grocerylistItemPost");
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
| **apI2ControllersWebAPIGroceryListControllerPostToGroceryListRecipeRequest** | [**API2ControllersWebAPIGroceryListControllerPostToGroceryListRecipeRequest**](API2ControllersWebAPIGroceryListControllerPostToGroceryListRecipeRequest.md)| name, quantity, unit, notes, department | |

### Return type

[**BigOvenModelShoppingListLine**](BigOvenModelShoppingListLine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

