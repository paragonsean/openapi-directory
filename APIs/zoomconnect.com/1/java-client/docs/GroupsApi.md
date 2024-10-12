# GroupsApi

All URIs are relative to *https://www.zoomconnect.com/app*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiRestV1GroupsAllGet**](GroupsApi.md#apiRestV1GroupsAllGet) | **GET** /api/rest/v1/groups/all | all |
| [**apiRestV1GroupsCreatePost**](GroupsApi.md#apiRestV1GroupsCreatePost) | **POST** /api/rest/v1/groups/create | create |
| [**apiRestV1GroupsGroupIdAddContactContactIdGet**](GroupsApi.md#apiRestV1GroupsGroupIdAddContactContactIdGet) | **GET** /api/rest/v1/groups/{groupId}/addContact/{contactId} | addContact |
| [**apiRestV1GroupsGroupIdAddContactContactIdPost**](GroupsApi.md#apiRestV1GroupsGroupIdAddContactContactIdPost) | **POST** /api/rest/v1/groups/{groupId}/addContact/{contactId} | addContact |
| [**apiRestV1GroupsGroupIdDelete**](GroupsApi.md#apiRestV1GroupsGroupIdDelete) | **DELETE** /api/rest/v1/groups/{groupId} | delete |
| [**apiRestV1GroupsGroupIdGet**](GroupsApi.md#apiRestV1GroupsGroupIdGet) | **GET** /api/rest/v1/groups/{groupId} | get |
| [**apiRestV1GroupsGroupIdPost**](GroupsApi.md#apiRestV1GroupsGroupIdPost) | **POST** /api/rest/v1/groups/{groupId} | update |
| [**apiRestV1GroupsGroupIdRemoveContactContactIdGet**](GroupsApi.md#apiRestV1GroupsGroupIdRemoveContactContactIdGet) | **GET** /api/rest/v1/groups/{groupId}/removeContact/{contactId} | removeContact |
| [**apiRestV1GroupsGroupIdRemoveContactContactIdPost**](GroupsApi.md#apiRestV1GroupsGroupIdRemoveContactContactIdPost) | **POST** /api/rest/v1/groups/{groupId}/removeContact/{contactId} | removeContact |


<a id="apiRestV1GroupsAllGet"></a>
# **apiRestV1GroupsAllGet**
> WebServiceGroups apiRestV1GroupsAllGet()

all

Returns all groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    try {
      WebServiceGroups result = apiInstance.apiRestV1GroupsAllGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#apiRestV1GroupsAllGet");
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

[**WebServiceGroups**](WebServiceGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="apiRestV1GroupsCreatePost"></a>
# **apiRestV1GroupsCreatePost**
> WebServiceGroup apiRestV1GroupsCreatePost(body)

create

Create a  group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    WebServiceGroup body = new WebServiceGroup(); // WebServiceGroup | webServiceGroup
    try {
      WebServiceGroup result = apiInstance.apiRestV1GroupsCreatePost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#apiRestV1GroupsCreatePost");
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
| **body** | [**WebServiceGroup**](WebServiceGroup.md)| webServiceGroup | [optional] |

### Return type

[**WebServiceGroup**](WebServiceGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="apiRestV1GroupsGroupIdAddContactContactIdGet"></a>
# **apiRestV1GroupsGroupIdAddContactContactIdGet**
> apiRestV1GroupsGroupIdAddContactContactIdGet(groupId, contactId)

addContact

Add a contact to a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String groupId = "groupId_example"; // String | groupId
    String contactId = "contactId_example"; // String | contactId
    try {
      apiInstance.apiRestV1GroupsGroupIdAddContactContactIdGet(groupId, contactId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#apiRestV1GroupsGroupIdAddContactContactIdGet");
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
| **groupId** | **String**| groupId | |
| **contactId** | **String**| contactId | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="apiRestV1GroupsGroupIdAddContactContactIdPost"></a>
# **apiRestV1GroupsGroupIdAddContactContactIdPost**
> apiRestV1GroupsGroupIdAddContactContactIdPost(groupId, contactId)

addContact

Add a contact to a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String groupId = "groupId_example"; // String | groupId
    String contactId = "contactId_example"; // String | contactId
    try {
      apiInstance.apiRestV1GroupsGroupIdAddContactContactIdPost(groupId, contactId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#apiRestV1GroupsGroupIdAddContactContactIdPost");
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
| **groupId** | **String**| groupId | |
| **contactId** | **String**| contactId | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="apiRestV1GroupsGroupIdDelete"></a>
# **apiRestV1GroupsGroupIdDelete**
> apiRestV1GroupsGroupIdDelete(groupId)

delete

Deletes a  group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String groupId = "groupId_example"; // String | groupId
    try {
      apiInstance.apiRestV1GroupsGroupIdDelete(groupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#apiRestV1GroupsGroupIdDelete");
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
| **groupId** | **String**| groupId | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="apiRestV1GroupsGroupIdGet"></a>
# **apiRestV1GroupsGroupIdGet**
> WebServiceGroup apiRestV1GroupsGroupIdGet(groupId)

get

Returns details for a single group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String groupId = "groupId_example"; // String | groupId
    try {
      WebServiceGroup result = apiInstance.apiRestV1GroupsGroupIdGet(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#apiRestV1GroupsGroupIdGet");
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
| **groupId** | **String**| groupId | |

### Return type

[**WebServiceGroup**](WebServiceGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="apiRestV1GroupsGroupIdPost"></a>
# **apiRestV1GroupsGroupIdPost**
> WebServiceGroup apiRestV1GroupsGroupIdPost(groupId, body)

update

Update a  group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String groupId = "groupId_example"; // String | groupId
    WebServiceGroup body = new WebServiceGroup(); // WebServiceGroup | webServiceGroup
    try {
      WebServiceGroup result = apiInstance.apiRestV1GroupsGroupIdPost(groupId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#apiRestV1GroupsGroupIdPost");
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
| **groupId** | **String**| groupId | |
| **body** | [**WebServiceGroup**](WebServiceGroup.md)| webServiceGroup | [optional] |

### Return type

[**WebServiceGroup**](WebServiceGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="apiRestV1GroupsGroupIdRemoveContactContactIdGet"></a>
# **apiRestV1GroupsGroupIdRemoveContactContactIdGet**
> apiRestV1GroupsGroupIdRemoveContactContactIdGet(groupId, contactId)

removeContact

Remove a contact from a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String groupId = "groupId_example"; // String | groupId
    String contactId = "contactId_example"; // String | contactId
    try {
      apiInstance.apiRestV1GroupsGroupIdRemoveContactContactIdGet(groupId, contactId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#apiRestV1GroupsGroupIdRemoveContactContactIdGet");
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
| **groupId** | **String**| groupId | |
| **contactId** | **String**| contactId | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="apiRestV1GroupsGroupIdRemoveContactContactIdPost"></a>
# **apiRestV1GroupsGroupIdRemoveContactContactIdPost**
> apiRestV1GroupsGroupIdRemoveContactContactIdPost(groupId, contactId)

removeContact

Remove a contact from a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String groupId = "groupId_example"; // String | groupId
    String contactId = "contactId_example"; // String | contactId
    try {
      apiInstance.apiRestV1GroupsGroupIdRemoveContactContactIdPost(groupId, contactId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#apiRestV1GroupsGroupIdRemoveContactContactIdPost");
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
| **groupId** | **String**| groupId | |
| **contactId** | **String**| contactId | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

