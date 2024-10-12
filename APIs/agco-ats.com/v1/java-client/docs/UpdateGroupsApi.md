# UpdateGroupsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV2UpdateGroupsIDGet**](UpdateGroupsApi.md#apiV2UpdateGroupsIDGet) | **GET** /api/v2/UpdateGroups/{ID} | Get a specific Update Group by ID. |
| [**updateGroupsAddUpdateGroupUser**](UpdateGroupsApi.md#updateGroupsAddUpdateGroupUser) | **POST** /api/v2/UpdateGroups/{id}/Users/{userID} | Add an updateGroup that a user can see. |
| [**updateGroupsDelete**](UpdateGroupsApi.md#updateGroupsDelete) | **DELETE** /api/v2/UpdateGroups/{ID} | Delete an Update Group. |
| [**updateGroupsGet**](UpdateGroupsApi.md#updateGroupsGet) | **GET** /api/v2/UpdateGroups | Get a list of Update Groups.  Update Groups are used by the client to register for a specific type of update. |
| [**updateGroupsGetUpdateGroupBundles**](UpdateGroupsApi.md#updateGroupsGetUpdateGroupBundles) | **GET** /api/v2/UpdateGroups/{ID}/Bundles | Get a list of bundles for UpdateGroup. |
| [**updateGroupsPost**](UpdateGroupsApi.md#updateGroupsPost) | **POST** /api/v2/UpdateGroups | Add a new Update Group.  The report field is a string that has a dot based request for a specific piece of submitted data. |
| [**updateGroupsPut**](UpdateGroupsApi.md#updateGroupsPut) | **PUT** /api/v2/UpdateGroups/{ID} | Modify an Update Group. |
| [**updateGroupsRemoveUpdateGroupUser**](UpdateGroupsApi.md#updateGroupsRemoveUpdateGroupUser) | **DELETE** /api/v2/UpdateGroups/{id}/Users/{userID} | Deletes an update group a user could see. |


<a id="apiV2UpdateGroupsIDGet"></a>
# **apiV2UpdateGroupsIDGet**
> UpdateSystemModelsUpdateGroup apiV2UpdateGroupsIDGet(ID)

Get a specific Update Group by ID.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateGroupsApi apiInstance = new UpdateGroupsApi(defaultClient);
    String ID = "ID_example"; // String | The ID of the Update Group
    try {
      UpdateSystemModelsUpdateGroup result = apiInstance.apiV2UpdateGroupsIDGet(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateGroupsApi#apiV2UpdateGroupsIDGet");
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
| **ID** | **String**| The ID of the Update Group | |

### Return type

[**UpdateSystemModelsUpdateGroup**](UpdateSystemModelsUpdateGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="updateGroupsAddUpdateGroupUser"></a>
# **updateGroupsAddUpdateGroupUser**
> updateGroupsAddUpdateGroupUser(id, userID)

Add an updateGroup that a user can see.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateGroupsApi apiInstance = new UpdateGroupsApi(defaultClient);
    String id = "id_example"; // String | The ID of the update group
    Integer userID = 56; // Integer | The userID to link to the update group
    try {
      apiInstance.updateGroupsAddUpdateGroupUser(id, userID);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateGroupsApi#updateGroupsAddUpdateGroupUser");
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
| **id** | **String**| The ID of the update group | |
| **userID** | **Integer**| The userID to link to the update group | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="updateGroupsDelete"></a>
# **updateGroupsDelete**
> updateGroupsDelete(ID)

Delete an Update Group.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateGroupsApi apiInstance = new UpdateGroupsApi(defaultClient);
    String ID = "ID_example"; // String | The ID of the Update Group to Delete
    try {
      apiInstance.updateGroupsDelete(ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateGroupsApi#updateGroupsDelete");
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
| **ID** | **String**| The ID of the Update Group to Delete | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="updateGroupsGet"></a>
# **updateGroupsGet**
> APIPagedResponseUpdateSystemModelsUpdateGroup updateGroupsGet(limit, offset, userID)

Get a list of Update Groups.  Update Groups are used by the client to register for a specific type of update.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateGroupsApi apiInstance = new UpdateGroupsApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    Integer userID = 56; // Integer | Optional. The user ID to sort update groups by the user's access
    try {
      APIPagedResponseUpdateSystemModelsUpdateGroup result = apiInstance.updateGroupsGet(limit, offset, userID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateGroupsApi#updateGroupsGet");
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
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |
| **userID** | **Integer**| Optional. The user ID to sort update groups by the user&#39;s access | [optional] |

### Return type

[**APIPagedResponseUpdateSystemModelsUpdateGroup**](APIPagedResponseUpdateSystemModelsUpdateGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="updateGroupsGetUpdateGroupBundles"></a>
# **updateGroupsGetUpdateGroupBundles**
> APIPagedResponseUpdateSystemModelsBundle updateGroupsGetUpdateGroupBundles(ID, includeInactive, limit, offset)

Get a list of bundles for UpdateGroup.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateGroupsApi apiInstance = new UpdateGroupsApi(defaultClient);
    String ID = "ID_example"; // String | The UpdateGroupID
    Boolean includeInactive = true; // Boolean | Include Inactive Bundles (true|false)
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIPagedResponseUpdateSystemModelsBundle result = apiInstance.updateGroupsGetUpdateGroupBundles(ID, includeInactive, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateGroupsApi#updateGroupsGetUpdateGroupBundles");
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
| **ID** | **String**| The UpdateGroupID | |
| **includeInactive** | **Boolean**| Include Inactive Bundles (true|false) | |
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseUpdateSystemModelsBundle**](APIPagedResponseUpdateSystemModelsBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="updateGroupsPost"></a>
# **updateGroupsPost**
> String updateGroupsPost(updateSystemModelsUpdateGroup)

Add a new Update Group.  The report field is a string that has a dot based request for a specific piece of submitted data.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateGroupsApi apiInstance = new UpdateGroupsApi(defaultClient);
    UpdateSystemModelsUpdateGroup updateSystemModelsUpdateGroup = new UpdateSystemModelsUpdateGroup(); // UpdateSystemModelsUpdateGroup | 
    try {
      String result = apiInstance.updateGroupsPost(updateSystemModelsUpdateGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateGroupsApi#updateGroupsPost");
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
| **updateSystemModelsUpdateGroup** | [**UpdateSystemModelsUpdateGroup**](UpdateSystemModelsUpdateGroup.md)|  | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="updateGroupsPut"></a>
# **updateGroupsPut**
> updateGroupsPut(ID, updateSystemModelsUpdateGroup)

Modify an Update Group.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateGroupsApi apiInstance = new UpdateGroupsApi(defaultClient);
    String ID = "ID_example"; // String | ID of the Update Group
    UpdateSystemModelsUpdateGroup updateSystemModelsUpdateGroup = new UpdateSystemModelsUpdateGroup(); // UpdateSystemModelsUpdateGroup | The Update Group to update.
    try {
      apiInstance.updateGroupsPut(ID, updateSystemModelsUpdateGroup);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateGroupsApi#updateGroupsPut");
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
| **ID** | **String**| ID of the Update Group | |
| **updateSystemModelsUpdateGroup** | [**UpdateSystemModelsUpdateGroup**](UpdateSystemModelsUpdateGroup.md)| The Update Group to update. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="updateGroupsRemoveUpdateGroupUser"></a>
# **updateGroupsRemoveUpdateGroupUser**
> updateGroupsRemoveUpdateGroupUser(id, userID)

Deletes an update group a user could see.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateGroupsApi apiInstance = new UpdateGroupsApi(defaultClient);
    String id = "id_example"; // String | The ID of the update group
    Integer userID = 56; // Integer | The userID to link to the update group
    try {
      apiInstance.updateGroupsRemoveUpdateGroupUser(id, userID);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateGroupsApi#updateGroupsRemoveUpdateGroupUser");
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
| **id** | **String**| The ID of the update group | |
| **userID** | **Integer**| The userID to link to the update group | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

