# MemberApi

All URIs are relative to *https://api.nexmo.com/v0.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createMember**](MemberApi.md#createMember) | **POST** /conversations/{conversation_id}/members | Create a member |
| [**deleteMember**](MemberApi.md#deleteMember) | **DELETE** /conversations/{conversation_id}/members/{member_id} | Delete a member |
| [**getMember**](MemberApi.md#getMember) | **GET** /conversations/{conversation_id}/members/{member_id} | Retrieve a member |
| [**getMembers**](MemberApi.md#getMembers) | **GET** /conversations/{conversation_id}/members | List members |
| [**updateMember**](MemberApi.md#updateMember) | **PUT** /conversations/{conversation_id}/members/{member_id} | Update a member |


<a id="createMember"></a>
# **createMember**
> CreateMember201Response createMember(conversationId, createMemberRequest)

Create a member

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v0.1");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    MemberApi apiInstance = new MemberApi(defaultClient);
    String conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
    CreateMemberRequest createMemberRequest = new CreateMemberRequest(); // CreateMemberRequest | 
    try {
      CreateMember201Response result = apiInstance.createMember(conversationId, createMemberRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#createMember");
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
| **conversationId** | **String**| Conversation ID | |
| **createMemberRequest** | [**CreateMemberRequest**](CreateMemberRequest.md)|  | [optional] |

### Return type

[**CreateMember201Response**](CreateMember201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Create or invite Member in invite state  |  -  |

<a id="deleteMember"></a>
# **deleteMember**
> Object deleteMember(conversationId, memberId)

Delete a member

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v0.1");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    MemberApi apiInstance = new MemberApi(defaultClient);
    String conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
    String memberId = "memberId_example"; // String | Member ID
    try {
      Object result = apiInstance.deleteMember(conversationId, memberId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#deleteMember");
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
| **conversationId** | **String**| Conversation ID | |
| **memberId** | **String**| Member ID | |

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success response with empty JSON |  -  |

<a id="getMember"></a>
# **getMember**
> GetMember200Response getMember(conversationId, memberId)

Retrieve a member

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v0.1");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    MemberApi apiInstance = new MemberApi(defaultClient);
    String conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
    String memberId = "memberId_example"; // String | Member ID
    try {
      GetMember200Response result = apiInstance.getMember(conversationId, memberId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMember");
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
| **conversationId** | **String**| Conversation ID | |
| **memberId** | **String**| Member ID | |

### Return type

[**GetMember200Response**](GetMember200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieve member payload |  -  |

<a id="getMembers"></a>
# **getMembers**
> List&lt;GetMembers200ResponseInner&gt; getMembers(conversationId)

List members

This endpoint is **DEPRECATED**. Please use [/v0.2/members](/api/conversation.v2#get-members).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v0.1");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    MemberApi apiInstance = new MemberApi(defaultClient);
    String conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
    try {
      List<GetMembers200ResponseInner> result = apiInstance.getMembers(conversationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembers");
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
| **conversationId** | **String**| Conversation ID | |

### Return type

[**List&lt;GetMembers200ResponseInner&gt;**](GetMembers200ResponseInner.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Members List Object |  -  |

<a id="updateMember"></a>
# **updateMember**
> GetMember200Response updateMember(conversationId, memberId, updateMemberRequest)

Update a member

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v0.1");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    MemberApi apiInstance = new MemberApi(defaultClient);
    String conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
    String memberId = "memberId_example"; // String | Member ID
    UpdateMemberRequest updateMemberRequest = new UpdateMemberRequest(); // UpdateMemberRequest | 
    try {
      GetMember200Response result = apiInstance.updateMember(conversationId, memberId, updateMemberRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#updateMember");
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
| **conversationId** | **String**| Conversation ID | |
| **memberId** | **String**| Member ID | |
| **updateMemberRequest** | [**UpdateMemberRequest**](UpdateMemberRequest.md)|  | [optional] |

### Return type

[**GetMember200Response**](GetMember200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Member retrieved |  -  |

