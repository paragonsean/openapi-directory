# UpdateGroupSubscriptionsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**updateGroupSubscriptionsDeleteUpdateGroupSubscription**](UpdateGroupSubscriptionsApi.md#updateGroupSubscriptionsDeleteUpdateGroupSubscription) | **DELETE** /api/v2/UpdateGroupSubscriptions/{UpdateGroupSubscriptionID} | Delete an Update Group Subscription |
| [**updateGroupSubscriptionsGetUpdateGroupSubscription**](UpdateGroupSubscriptionsApi.md#updateGroupSubscriptionsGetUpdateGroupSubscription) | **GET** /api/v2/UpdateGroupSubscriptions/{UpdateGroupSubscriptionID} | Get an Update Group Subscription |
| [**updateGroupSubscriptionsGetUpdateGroupSubscriptions**](UpdateGroupSubscriptionsApi.md#updateGroupSubscriptionsGetUpdateGroupSubscriptions) | **GET** /api/v2/UpdateGroupSubscriptions | Get Update Group Subscriptions |
| [**updateGroupSubscriptionsPostUpdateGroupSubscription**](UpdateGroupSubscriptionsApi.md#updateGroupSubscriptionsPostUpdateGroupSubscription) | **POST** /api/v2/UpdateGroupSubscriptions | Add an Update Group Subscription |
| [**updateGroupSubscriptionsPostUpdateGroupSubscriptions**](UpdateGroupSubscriptionsApi.md#updateGroupSubscriptionsPostUpdateGroupSubscriptions) | **POST** /api/v2/UpdateGroupSubscriptions/Batch | No Documentation Found. |
| [**updateGroupSubscriptionsPutUpdateGroupSubscription**](UpdateGroupSubscriptionsApi.md#updateGroupSubscriptionsPutUpdateGroupSubscription) | **PUT** /api/v2/UpdateGroupSubscriptions/{UpdateGroupSubscriptionID} | Update an Update Group Subscription |
| [**updateGroupSubscriptionsPutUpdateGroupSubscriptions**](UpdateGroupSubscriptionsApi.md#updateGroupSubscriptionsPutUpdateGroupSubscriptions) | **PUT** /api/v2/UpdateGroupSubscriptions/Batch | No Documentation Found. |


<a id="updateGroupSubscriptionsDeleteUpdateGroupSubscription"></a>
# **updateGroupSubscriptionsDeleteUpdateGroupSubscription**
> updateGroupSubscriptionsDeleteUpdateGroupSubscription(updateGroupSubscriptionID)

Delete an Update Group Subscription

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateGroupSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateGroupSubscriptionsApi apiInstance = new UpdateGroupSubscriptionsApi(defaultClient);
    Integer updateGroupSubscriptionID = 56; // Integer | The Update Group Subscription ID to delete
    try {
      apiInstance.updateGroupSubscriptionsDeleteUpdateGroupSubscription(updateGroupSubscriptionID);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateGroupSubscriptionsApi#updateGroupSubscriptionsDeleteUpdateGroupSubscription");
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
| **updateGroupSubscriptionID** | **Integer**| The Update Group Subscription ID to delete | |

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

<a id="updateGroupSubscriptionsGetUpdateGroupSubscription"></a>
# **updateGroupSubscriptionsGetUpdateGroupSubscription**
> UpdateSystemModelsUpdateGroupSubscription updateGroupSubscriptionsGetUpdateGroupSubscription(updateGroupSubscriptionID)

Get an Update Group Subscription

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateGroupSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateGroupSubscriptionsApi apiInstance = new UpdateGroupSubscriptionsApi(defaultClient);
    Integer updateGroupSubscriptionID = 56; // Integer | The Update Group Subscription ID
    try {
      UpdateSystemModelsUpdateGroupSubscription result = apiInstance.updateGroupSubscriptionsGetUpdateGroupSubscription(updateGroupSubscriptionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateGroupSubscriptionsApi#updateGroupSubscriptionsGetUpdateGroupSubscription");
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
| **updateGroupSubscriptionID** | **Integer**| The Update Group Subscription ID | |

### Return type

[**UpdateSystemModelsUpdateGroupSubscription**](UpdateSystemModelsUpdateGroupSubscription.md)

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

<a id="updateGroupSubscriptionsGetUpdateGroupSubscriptions"></a>
# **updateGroupSubscriptionsGetUpdateGroupSubscriptions**
> APIPagedResponseUpdateSystemModelsUpdateGroupSubscription updateGroupSubscriptionsGetUpdateGroupSubscriptions(updateGroupID, packageTypeID, clientID, limit, offset)

Get Update Group Subscriptions

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateGroupSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateGroupSubscriptionsApi apiInstance = new UpdateGroupSubscriptionsApi(defaultClient);
    String updateGroupID = "updateGroupID_example"; // String | Optional. Filter by Update Group ID.
    String packageTypeID = "packageTypeID_example"; // String | Optional. Filter by Package Type ID.
    String clientID = "clientID_example"; // String | Optional. Filter by Client ID.
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIPagedResponseUpdateSystemModelsUpdateGroupSubscription result = apiInstance.updateGroupSubscriptionsGetUpdateGroupSubscriptions(updateGroupID, packageTypeID, clientID, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateGroupSubscriptionsApi#updateGroupSubscriptionsGetUpdateGroupSubscriptions");
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
| **updateGroupID** | **String**| Optional. Filter by Update Group ID. | [optional] |
| **packageTypeID** | **String**| Optional. Filter by Package Type ID. | [optional] |
| **clientID** | **String**| Optional. Filter by Client ID. | [optional] |
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

<a id="updateGroupSubscriptionsPostUpdateGroupSubscription"></a>
# **updateGroupSubscriptionsPostUpdateGroupSubscription**
> Integer updateGroupSubscriptionsPostUpdateGroupSubscription(updateSystemModelsUpdateGroupSubscription)

Add an Update Group Subscription

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateGroupSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateGroupSubscriptionsApi apiInstance = new UpdateGroupSubscriptionsApi(defaultClient);
    UpdateSystemModelsUpdateGroupSubscription updateSystemModelsUpdateGroupSubscription = new UpdateSystemModelsUpdateGroupSubscription(); // UpdateSystemModelsUpdateGroupSubscription | The Update Group Subscription to add
    try {
      Integer result = apiInstance.updateGroupSubscriptionsPostUpdateGroupSubscription(updateSystemModelsUpdateGroupSubscription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateGroupSubscriptionsApi#updateGroupSubscriptionsPostUpdateGroupSubscription");
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
| **updateSystemModelsUpdateGroupSubscription** | [**UpdateSystemModelsUpdateGroupSubscription**](UpdateSystemModelsUpdateGroupSubscription.md)| The Update Group Subscription to add | |

### Return type

**Integer**

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

<a id="updateGroupSubscriptionsPostUpdateGroupSubscriptions"></a>
# **updateGroupSubscriptionsPostUpdateGroupSubscriptions**
> updateGroupSubscriptionsPostUpdateGroupSubscriptions(updateSystemModelsUpdateGroupSubscription)

No Documentation Found.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateGroupSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateGroupSubscriptionsApi apiInstance = new UpdateGroupSubscriptionsApi(defaultClient);
    List<UpdateSystemModelsUpdateGroupSubscription> updateSystemModelsUpdateGroupSubscription = Arrays.asList(); // List<UpdateSystemModelsUpdateGroupSubscription> | 
    try {
      apiInstance.updateGroupSubscriptionsPostUpdateGroupSubscriptions(updateSystemModelsUpdateGroupSubscription);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateGroupSubscriptionsApi#updateGroupSubscriptionsPostUpdateGroupSubscriptions");
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
| **updateSystemModelsUpdateGroupSubscription** | [**List&lt;UpdateSystemModelsUpdateGroupSubscription&gt;**](UpdateSystemModelsUpdateGroupSubscription.md)|  | |

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

<a id="updateGroupSubscriptionsPutUpdateGroupSubscription"></a>
# **updateGroupSubscriptionsPutUpdateGroupSubscription**
> updateGroupSubscriptionsPutUpdateGroupSubscription(updateGroupSubscriptionID, updateSystemModelsUpdateGroupSubscription)

Update an Update Group Subscription

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateGroupSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateGroupSubscriptionsApi apiInstance = new UpdateGroupSubscriptionsApi(defaultClient);
    Integer updateGroupSubscriptionID = 56; // Integer | The Update Group Subscription ID
    UpdateSystemModelsUpdateGroupSubscription updateSystemModelsUpdateGroupSubscription = new UpdateSystemModelsUpdateGroupSubscription(); // UpdateSystemModelsUpdateGroupSubscription | The updated Update Group Subscription
    try {
      apiInstance.updateGroupSubscriptionsPutUpdateGroupSubscription(updateGroupSubscriptionID, updateSystemModelsUpdateGroupSubscription);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateGroupSubscriptionsApi#updateGroupSubscriptionsPutUpdateGroupSubscription");
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
| **updateGroupSubscriptionID** | **Integer**| The Update Group Subscription ID | |
| **updateSystemModelsUpdateGroupSubscription** | [**UpdateSystemModelsUpdateGroupSubscription**](UpdateSystemModelsUpdateGroupSubscription.md)| The updated Update Group Subscription | |

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

<a id="updateGroupSubscriptionsPutUpdateGroupSubscriptions"></a>
# **updateGroupSubscriptionsPutUpdateGroupSubscriptions**
> updateGroupSubscriptionsPutUpdateGroupSubscriptions(updateSystemModelsUpdateGroupSubscription)

No Documentation Found.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateGroupSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateGroupSubscriptionsApi apiInstance = new UpdateGroupSubscriptionsApi(defaultClient);
    List<UpdateSystemModelsUpdateGroupSubscription> updateSystemModelsUpdateGroupSubscription = Arrays.asList(); // List<UpdateSystemModelsUpdateGroupSubscription> | 
    try {
      apiInstance.updateGroupSubscriptionsPutUpdateGroupSubscriptions(updateSystemModelsUpdateGroupSubscription);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateGroupSubscriptionsApi#updateGroupSubscriptionsPutUpdateGroupSubscriptions");
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
| **updateSystemModelsUpdateGroupSubscription** | [**List&lt;UpdateSystemModelsUpdateGroupSubscription&gt;**](UpdateSystemModelsUpdateGroupSubscription.md)|  | |

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

