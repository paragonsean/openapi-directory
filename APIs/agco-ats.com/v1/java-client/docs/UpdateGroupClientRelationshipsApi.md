# UpdateGroupClientRelationshipsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**updateGroupClientRelationshipsGetSubscription**](UpdateGroupClientRelationshipsApi.md#updateGroupClientRelationshipsGetSubscription) | **GET** /api/v2/UpdateGroupClientRelationships/{RelationshipID} | Get a subscription by RelationshipID |
| [**updateGroupClientRelationshipsGetSubscriptions**](UpdateGroupClientRelationshipsApi.md#updateGroupClientRelationshipsGetSubscriptions) | **GET** /api/v2/UpdateGroupClientRelationships | Get a list of current Client Subscriptions. |
| [**updateGroupClientRelationshipsPostSubscription**](UpdateGroupClientRelationshipsApi.md#updateGroupClientRelationshipsPostSubscription) | **POST** /api/v2/UpdateGroupClientRelationships | Add a subscription |
| [**updateGroupClientRelationshipsPutSubscription**](UpdateGroupClientRelationshipsApi.md#updateGroupClientRelationshipsPutSubscription) | **PUT** /api/v2/UpdateGroupClientRelationships/{RelationshipID} | Updates a Subscription |
| [**updateGroupClientRelationshipsPutSubscriptionByClientIDUpdateGroupID**](UpdateGroupClientRelationshipsApi.md#updateGroupClientRelationshipsPutSubscriptionByClientIDUpdateGroupID) | **PUT** /api/v2/UpdateGroupClientRelationships | DEPRECATED. Set client subscription status for an update group. |


<a id="updateGroupClientRelationshipsGetSubscription"></a>
# **updateGroupClientRelationshipsGetSubscription**
> UpdateSystemModelsUpdateGroupClientRelationship updateGroupClientRelationshipsGetSubscription(relationshipID)

Get a subscription by RelationshipID

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateGroupClientRelationshipsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateGroupClientRelationshipsApi apiInstance = new UpdateGroupClientRelationshipsApi(defaultClient);
    String relationshipID = "relationshipID_example"; // String | The RelationshipID.
    try {
      UpdateSystemModelsUpdateGroupClientRelationship result = apiInstance.updateGroupClientRelationshipsGetSubscription(relationshipID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateGroupClientRelationshipsApi#updateGroupClientRelationshipsGetSubscription");
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
| **relationshipID** | **String**| The RelationshipID. | |

### Return type

[**UpdateSystemModelsUpdateGroupClientRelationship**](UpdateSystemModelsUpdateGroupClientRelationship.md)

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

<a id="updateGroupClientRelationshipsGetSubscriptions"></a>
# **updateGroupClientRelationshipsGetSubscriptions**
> APIPagedResponseUpdateSystemModelsUpdateGroupClientRelationship updateGroupClientRelationshipsGetSubscriptions(clientID, updateGroupID, limit, offset, active)

Get a list of current Client Subscriptions.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateGroupClientRelationshipsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateGroupClientRelationshipsApi apiInstance = new UpdateGroupClientRelationshipsApi(defaultClient);
    String clientID = "clientID_example"; // String | Optional. Filter by Client ID
    String updateGroupID = "updateGroupID_example"; // String | Optional. Filter by Update Group ID
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    Boolean active = true; // Boolean | Optional. Filter by Active
    try {
      APIPagedResponseUpdateSystemModelsUpdateGroupClientRelationship result = apiInstance.updateGroupClientRelationshipsGetSubscriptions(clientID, updateGroupID, limit, offset, active);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateGroupClientRelationshipsApi#updateGroupClientRelationshipsGetSubscriptions");
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
| **clientID** | **String**| Optional. Filter by Client ID | [optional] |
| **updateGroupID** | **String**| Optional. Filter by Update Group ID | [optional] |
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |
| **active** | **Boolean**| Optional. Filter by Active | [optional] |

### Return type

[**APIPagedResponseUpdateSystemModelsUpdateGroupClientRelationship**](APIPagedResponseUpdateSystemModelsUpdateGroupClientRelationship.md)

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

<a id="updateGroupClientRelationshipsPostSubscription"></a>
# **updateGroupClientRelationshipsPostSubscription**
> String updateGroupClientRelationshipsPostSubscription(updateSystemModelsUpdateGroupClientRelationship)

Add a subscription

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateGroupClientRelationshipsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateGroupClientRelationshipsApi apiInstance = new UpdateGroupClientRelationshipsApi(defaultClient);
    UpdateSystemModelsUpdateGroupClientRelationship updateSystemModelsUpdateGroupClientRelationship = new UpdateSystemModelsUpdateGroupClientRelationship(); // UpdateSystemModelsUpdateGroupClientRelationship | The UpdateGroupClientRelationship to add.
    try {
      String result = apiInstance.updateGroupClientRelationshipsPostSubscription(updateSystemModelsUpdateGroupClientRelationship);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateGroupClientRelationshipsApi#updateGroupClientRelationshipsPostSubscription");
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
| **updateSystemModelsUpdateGroupClientRelationship** | [**UpdateSystemModelsUpdateGroupClientRelationship**](UpdateSystemModelsUpdateGroupClientRelationship.md)| The UpdateGroupClientRelationship to add. | |

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

<a id="updateGroupClientRelationshipsPutSubscription"></a>
# **updateGroupClientRelationshipsPutSubscription**
> updateGroupClientRelationshipsPutSubscription(relationshipID, updateSystemModelsUpdateGroupClientRelationship)

Updates a Subscription

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateGroupClientRelationshipsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateGroupClientRelationshipsApi apiInstance = new UpdateGroupClientRelationshipsApi(defaultClient);
    String relationshipID = "relationshipID_example"; // String | The relationship id of the UpdateGroupClientRelationship
    UpdateSystemModelsUpdateGroupClientRelationship updateSystemModelsUpdateGroupClientRelationship = new UpdateSystemModelsUpdateGroupClientRelationship(); // UpdateSystemModelsUpdateGroupClientRelationship | The updated UpdateGroupClientRelationship
    try {
      apiInstance.updateGroupClientRelationshipsPutSubscription(relationshipID, updateSystemModelsUpdateGroupClientRelationship);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateGroupClientRelationshipsApi#updateGroupClientRelationshipsPutSubscription");
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
| **relationshipID** | **String**| The relationship id of the UpdateGroupClientRelationship | |
| **updateSystemModelsUpdateGroupClientRelationship** | [**UpdateSystemModelsUpdateGroupClientRelationship**](UpdateSystemModelsUpdateGroupClientRelationship.md)| The updated UpdateGroupClientRelationship | |

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

<a id="updateGroupClientRelationshipsPutSubscriptionByClientIDUpdateGroupID"></a>
# **updateGroupClientRelationshipsPutSubscriptionByClientIDUpdateGroupID**
> updateGroupClientRelationshipsPutSubscriptionByClientIDUpdateGroupID(clientID, updateGroupID, active)

DEPRECATED. Set client subscription status for an update group.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateGroupClientRelationshipsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateGroupClientRelationshipsApi apiInstance = new UpdateGroupClientRelationshipsApi(defaultClient);
    String clientID = "clientID_example"; // String | The Client ID.  This can be a client ID that has not been registered yet.
    String updateGroupID = "updateGroupID_example"; // String | The Update Group ID
    Boolean active = true; // Boolean | Subscribe the client to the Update Group.
    try {
      apiInstance.updateGroupClientRelationshipsPutSubscriptionByClientIDUpdateGroupID(clientID, updateGroupID, active);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateGroupClientRelationshipsApi#updateGroupClientRelationshipsPutSubscriptionByClientIDUpdateGroupID");
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
| **clientID** | **String**| The Client ID.  This can be a client ID that has not been registered yet. | |
| **updateGroupID** | **String**| The Update Group ID | |
| **active** | **Boolean**| Subscribe the client to the Update Group. | |

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

