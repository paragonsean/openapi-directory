# ClientsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV2ClientsIDGet**](ClientsApi.md#apiV2ClientsIDGet) | **GET** /api/v2/Clients/{ID} | Get a Client in the Update System. |
| [**clientsGet**](ClientsApi.md#clientsGet) | **GET** /api/v2/Clients | Get a List of Clients in the Update System. |
| [**clientsGetAvailableSubscriptions**](ClientsApi.md#clientsGetAvailableSubscriptions) | **GET** /api/v2/Clients/{ID}/AvailableUpdateGroupSubscriptions | Get a Client&#39;s Available Update Group Subscriptions |
| [**clientsGetSubscriptions**](ClientsApi.md#clientsGetSubscriptions) | **GET** /api/v2/Clients/{ID}/UpdateGroupSubscriptions | Get a Client&#39;s Current Update Group Subscriptions |
| [**clientsPut**](ClientsApi.md#clientsPut) | **PUT** /api/v2/Clients/{ID} | Update a Client. |


<a id="apiV2ClientsIDGet"></a>
# **apiV2ClientsIDGet**
> UpdateSystemModelsClient apiV2ClientsIDGet(ID)

Get a Client in the Update System.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String ID = "ID_example"; // String | The Client ID
    try {
      UpdateSystemModelsClient result = apiInstance.apiV2ClientsIDGet(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#apiV2ClientsIDGet");
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
| **ID** | **String**| The Client ID | |

### Return type

[**UpdateSystemModelsClient**](UpdateSystemModelsClient.md)

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

<a id="clientsGet"></a>
# **clientsGet**
> APIPagedResponseUpdateSystemModelsClient clientsGet(tag, limit, offset)

Get a List of Clients in the Update System.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String tag = "tag_example"; // String | Optional. Filter clients by Tag. Wildcards are supported (*).
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIPagedResponseUpdateSystemModelsClient result = apiInstance.clientsGet(tag, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#clientsGet");
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
| **tag** | **String**| Optional. Filter clients by Tag. Wildcards are supported (*). | [optional] |
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseUpdateSystemModelsClient**](APIPagedResponseUpdateSystemModelsClient.md)

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

<a id="clientsGetAvailableSubscriptions"></a>
# **clientsGetAvailableSubscriptions**
> APIPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription clientsGetAvailableSubscriptions(ID, updateGroupID, limit, offset)

Get a Client&#39;s Available Update Group Subscriptions

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String ID = "ID_example"; // String | The Client ID
    String updateGroupID = "updateGroupID_example"; // String | Optional. Filter by Update Group.
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription result = apiInstance.clientsGetAvailableSubscriptions(ID, updateGroupID, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#clientsGetAvailableSubscriptions");
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
| **ID** | **String**| The Client ID | |
| **updateGroupID** | **String**| Optional. Filter by Update Group. | [optional] |
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription**](APIPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription.md)

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

<a id="clientsGetSubscriptions"></a>
# **clientsGetSubscriptions**
> APIPagedResponseUpdateSystemModelsUpdateGroupSubscription clientsGetSubscriptions(ID, updateGroupID, limit, offset)

Get a Client&#39;s Current Update Group Subscriptions

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String ID = "ID_example"; // String | The Client ID
    String updateGroupID = "updateGroupID_example"; // String | Optional. Filter by Update Group.
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIPagedResponseUpdateSystemModelsUpdateGroupSubscription result = apiInstance.clientsGetSubscriptions(ID, updateGroupID, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#clientsGetSubscriptions");
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
| **ID** | **String**| The Client ID | |
| **updateGroupID** | **String**| Optional. Filter by Update Group. | [optional] |
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseUpdateSystemModelsUpdateGroupSubscription**](APIPagedResponseUpdateSystemModelsUpdateGroupSubscription.md)

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

<a id="clientsPut"></a>
# **clientsPut**
> clientsPut(ID, updateSystemModelsClient)

Update a Client.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String ID = "ID_example"; // String | The Client ID
    UpdateSystemModelsClient updateSystemModelsClient = new UpdateSystemModelsClient(); // UpdateSystemModelsClient | Updated Client Object.
    try {
      apiInstance.clientsPut(ID, updateSystemModelsClient);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#clientsPut");
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
| **ID** | **String**| The Client ID | |
| **updateSystemModelsClient** | [**UpdateSystemModelsClient**](UpdateSystemModelsClient.md)| Updated Client Object. | |

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

