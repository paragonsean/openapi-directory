# ContactsApi

All URIs are relative to *https://www.zoomconnect.com/app*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiRestV1ContactsAllGet**](ContactsApi.md#apiRestV1ContactsAllGet) | **GET** /api/rest/v1/contacts/all | all |
| [**apiRestV1ContactsContactIdAddFromGroupGroupIdGet**](ContactsApi.md#apiRestV1ContactsContactIdAddFromGroupGroupIdGet) | **GET** /api/rest/v1/contacts/{contactId}/addFromGroup/{groupId} | removeFromGroup |
| [**apiRestV1ContactsContactIdAddFromGroupGroupIdPost**](ContactsApi.md#apiRestV1ContactsContactIdAddFromGroupGroupIdPost) | **POST** /api/rest/v1/contacts/{contactId}/addFromGroup/{groupId} | removeFromGroup |
| [**apiRestV1ContactsContactIdAddToGroupGroupIdGet**](ContactsApi.md#apiRestV1ContactsContactIdAddToGroupGroupIdGet) | **GET** /api/rest/v1/contacts/{contactId}/addToGroup/{groupId} | addToGroup |
| [**apiRestV1ContactsContactIdAddToGroupGroupIdPost**](ContactsApi.md#apiRestV1ContactsContactIdAddToGroupGroupIdPost) | **POST** /api/rest/v1/contacts/{contactId}/addToGroup/{groupId} | addToGroup |
| [**apiRestV1ContactsContactIdDelete**](ContactsApi.md#apiRestV1ContactsContactIdDelete) | **DELETE** /api/rest/v1/contacts/{contactId} | delete |
| [**apiRestV1ContactsContactIdGet**](ContactsApi.md#apiRestV1ContactsContactIdGet) | **GET** /api/rest/v1/contacts/{contactId} | get |
| [**apiRestV1ContactsContactIdPost**](ContactsApi.md#apiRestV1ContactsContactIdPost) | **POST** /api/rest/v1/contacts/{contactId} | update |
| [**apiRestV1ContactsCreatePost**](ContactsApi.md#apiRestV1ContactsCreatePost) | **POST** /api/rest/v1/contacts/create | create |


<a id="apiRestV1ContactsAllGet"></a>
# **apiRestV1ContactsAllGet**
> WebServiceContacts apiRestV1ContactsAllGet()

all

Returns all contacts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    try {
      WebServiceContacts result = apiInstance.apiRestV1ContactsAllGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#apiRestV1ContactsAllGet");
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

[**WebServiceContacts**](WebServiceContacts.md)

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

<a id="apiRestV1ContactsContactIdAddFromGroupGroupIdGet"></a>
# **apiRestV1ContactsContactIdAddFromGroupGroupIdGet**
> apiRestV1ContactsContactIdAddFromGroupGroupIdGet(contactId, groupId)

removeFromGroup

Remove a contact from a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    String contactId = "contactId_example"; // String | contactId
    String groupId = "groupId_example"; // String | groupId
    try {
      apiInstance.apiRestV1ContactsContactIdAddFromGroupGroupIdGet(contactId, groupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#apiRestV1ContactsContactIdAddFromGroupGroupIdGet");
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
| **contactId** | **String**| contactId | |
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
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="apiRestV1ContactsContactIdAddFromGroupGroupIdPost"></a>
# **apiRestV1ContactsContactIdAddFromGroupGroupIdPost**
> apiRestV1ContactsContactIdAddFromGroupGroupIdPost(contactId, groupId)

removeFromGroup

Remove a contact from a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    String contactId = "contactId_example"; // String | contactId
    String groupId = "groupId_example"; // String | groupId
    try {
      apiInstance.apiRestV1ContactsContactIdAddFromGroupGroupIdPost(contactId, groupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#apiRestV1ContactsContactIdAddFromGroupGroupIdPost");
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
| **contactId** | **String**| contactId | |
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
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="apiRestV1ContactsContactIdAddToGroupGroupIdGet"></a>
# **apiRestV1ContactsContactIdAddToGroupGroupIdGet**
> apiRestV1ContactsContactIdAddToGroupGroupIdGet(contactId, groupId)

addToGroup

Add a contact to a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    String contactId = "contactId_example"; // String | contactId
    String groupId = "groupId_example"; // String | groupId
    try {
      apiInstance.apiRestV1ContactsContactIdAddToGroupGroupIdGet(contactId, groupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#apiRestV1ContactsContactIdAddToGroupGroupIdGet");
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
| **contactId** | **String**| contactId | |
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
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="apiRestV1ContactsContactIdAddToGroupGroupIdPost"></a>
# **apiRestV1ContactsContactIdAddToGroupGroupIdPost**
> apiRestV1ContactsContactIdAddToGroupGroupIdPost(contactId, groupId)

addToGroup

Add a contact to a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    String contactId = "contactId_example"; // String | contactId
    String groupId = "groupId_example"; // String | groupId
    try {
      apiInstance.apiRestV1ContactsContactIdAddToGroupGroupIdPost(contactId, groupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#apiRestV1ContactsContactIdAddToGroupGroupIdPost");
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
| **contactId** | **String**| contactId | |
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
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="apiRestV1ContactsContactIdDelete"></a>
# **apiRestV1ContactsContactIdDelete**
> apiRestV1ContactsContactIdDelete(contactId)

delete

Deletes a  contact

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    String contactId = "contactId_example"; // String | contactId
    try {
      apiInstance.apiRestV1ContactsContactIdDelete(contactId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#apiRestV1ContactsContactIdDelete");
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
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="apiRestV1ContactsContactIdGet"></a>
# **apiRestV1ContactsContactIdGet**
> WebServiceContact apiRestV1ContactsContactIdGet(contactId)

get

Returns details for a single contact

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    String contactId = "contactId_example"; // String | contactId
    try {
      WebServiceContact result = apiInstance.apiRestV1ContactsContactIdGet(contactId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#apiRestV1ContactsContactIdGet");
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
| **contactId** | **String**| contactId | |

### Return type

[**WebServiceContact**](WebServiceContact.md)

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

<a id="apiRestV1ContactsContactIdPost"></a>
# **apiRestV1ContactsContactIdPost**
> WebServiceContact apiRestV1ContactsContactIdPost(contactId, body)

update

Updates a  contact

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    String contactId = "contactId_example"; // String | contactId
    WebServiceContact body = new WebServiceContact(); // WebServiceContact | webServiceContact
    try {
      WebServiceContact result = apiInstance.apiRestV1ContactsContactIdPost(contactId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#apiRestV1ContactsContactIdPost");
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
| **contactId** | **String**| contactId | |
| **body** | [**WebServiceContact**](WebServiceContact.md)| webServiceContact | [optional] |

### Return type

[**WebServiceContact**](WebServiceContact.md)

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

<a id="apiRestV1ContactsCreatePost"></a>
# **apiRestV1ContactsCreatePost**
> WebServiceContact apiRestV1ContactsCreatePost(body)

create

Creates a  contact

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.zoomconnect.com/app");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    WebServiceContact body = new WebServiceContact(); // WebServiceContact | webServiceContact
    try {
      WebServiceContact result = apiInstance.apiRestV1ContactsCreatePost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#apiRestV1ContactsCreatePost");
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
| **body** | [**WebServiceContact**](WebServiceContact.md)| webServiceContact | [optional] |

### Return type

[**WebServiceContact**](WebServiceContact.md)

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

