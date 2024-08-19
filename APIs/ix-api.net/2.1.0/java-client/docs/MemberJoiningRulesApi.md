# MemberJoiningRulesApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**memberJoiningRulesCreate**](MemberJoiningRulesApi.md#memberJoiningRulesCreate) | **POST** /member-joining-rules |  |
| [**memberJoiningRulesDestroy**](MemberJoiningRulesApi.md#memberJoiningRulesDestroy) | **DELETE** /member-joining-rules/{id} |  |
| [**memberJoiningRulesList**](MemberJoiningRulesApi.md#memberJoiningRulesList) | **GET** /member-joining-rules |  |
| [**memberJoiningRulesPartialUpdate**](MemberJoiningRulesApi.md#memberJoiningRulesPartialUpdate) | **PATCH** /member-joining-rules/{id} |  |
| [**memberJoiningRulesRead**](MemberJoiningRulesApi.md#memberJoiningRulesRead) | **GET** /member-joining-rules/{id} |  |
| [**memberJoiningRulesUpdate**](MemberJoiningRulesApi.md#memberJoiningRulesUpdate) | **PUT** /member-joining-rules/{id} |  |


<a id="memberJoiningRulesCreate"></a>
# **memberJoiningRulesCreate**
> MemberJoiningRule memberJoiningRulesCreate(memberJoiningRuleRequest)



Create a member joining rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberJoiningRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    MemberJoiningRulesApi apiInstance = new MemberJoiningRulesApi(defaultClient);
    MemberJoiningRuleRequest memberJoiningRuleRequest = new MemberJoiningRuleRequest(); // MemberJoiningRuleRequest | Polymorphic Member Joining Rule Request
    try {
      MemberJoiningRule result = apiInstance.memberJoiningRulesCreate(memberJoiningRuleRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberJoiningRulesApi#memberJoiningRulesCreate");
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
| **memberJoiningRuleRequest** | [**MemberJoiningRuleRequest**](MemberJoiningRuleRequest.md)| Polymorphic Member Joining Rule Request | [optional] |

### Return type

[**MemberJoiningRule**](MemberJoiningRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Polymorphic Member Joining Rule |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="memberJoiningRulesDestroy"></a>
# **memberJoiningRulesDestroy**
> MemberJoiningRule memberJoiningRulesDestroy(id)



Delete a joining rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberJoiningRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    MemberJoiningRulesApi apiInstance = new MemberJoiningRulesApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      MemberJoiningRule result = apiInstance.memberJoiningRulesDestroy(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberJoiningRulesApi#memberJoiningRulesDestroy");
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
| **id** | **String**| Get by id | |

### Return type

[**MemberJoiningRule**](MemberJoiningRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Polymorphic Member Joining Rule |  -  |
| **400** | UnableToFulfill |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="memberJoiningRulesList"></a>
# **memberJoiningRulesList**
> List&lt;MemberJoiningRule&gt; memberJoiningRulesList(id, networkService)



Get a list of joining rules

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberJoiningRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    MemberJoiningRulesApi apiInstance = new MemberJoiningRulesApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Filter by id
    String networkService = "networkService_example"; // String | Filter by network_service
    try {
      List<MemberJoiningRule> result = apiInstance.memberJoiningRulesList(id, networkService);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberJoiningRulesApi#memberJoiningRulesList");
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
| **id** | [**List&lt;String&gt;**](String.md)| Filter by id | [optional] |
| **networkService** | **String**| Filter by network_service | [optional] |

### Return type

[**List&lt;MemberJoiningRule&gt;**](MemberJoiningRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of: Polymorphic Member Joining Rule |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="memberJoiningRulesPartialUpdate"></a>
# **memberJoiningRulesPartialUpdate**
> MemberJoiningRule memberJoiningRulesPartialUpdate(id, memberJoiningRuleUpdatePartial)



Partially update a joining rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberJoiningRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    MemberJoiningRulesApi apiInstance = new MemberJoiningRulesApi(defaultClient);
    String id = "id_example"; // String | Get by id
    MemberJoiningRuleUpdatePartial memberJoiningRuleUpdatePartial = new MemberJoiningRuleUpdatePartial(); // MemberJoiningRuleUpdatePartial | Polymorphic Member Joining Rule Update
    try {
      MemberJoiningRule result = apiInstance.memberJoiningRulesPartialUpdate(id, memberJoiningRuleUpdatePartial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberJoiningRulesApi#memberJoiningRulesPartialUpdate");
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
| **id** | **String**| Get by id | |
| **memberJoiningRuleUpdatePartial** | [**MemberJoiningRuleUpdatePartial**](MemberJoiningRuleUpdatePartial.md)| Polymorphic Member Joining Rule Update | [optional] |

### Return type

[**MemberJoiningRule**](MemberJoiningRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Polymorphic Member Joining Rule |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="memberJoiningRulesRead"></a>
# **memberJoiningRulesRead**
> MemberJoiningRule memberJoiningRulesRead(id)



Get a single rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberJoiningRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    MemberJoiningRulesApi apiInstance = new MemberJoiningRulesApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      MemberJoiningRule result = apiInstance.memberJoiningRulesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberJoiningRulesApi#memberJoiningRulesRead");
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
| **id** | **String**| Get by id | |

### Return type

[**MemberJoiningRule**](MemberJoiningRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Polymorphic Member Joining Rule |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="memberJoiningRulesUpdate"></a>
# **memberJoiningRulesUpdate**
> MemberJoiningRule memberJoiningRulesUpdate(id, memberJoiningRuleUpdate)



Update a joining rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberJoiningRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    MemberJoiningRulesApi apiInstance = new MemberJoiningRulesApi(defaultClient);
    String id = "id_example"; // String | Get by id
    MemberJoiningRuleUpdate memberJoiningRuleUpdate = new MemberJoiningRuleUpdate(); // MemberJoiningRuleUpdate | Polymorphic Member Joining Rule Update
    try {
      MemberJoiningRule result = apiInstance.memberJoiningRulesUpdate(id, memberJoiningRuleUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberJoiningRulesApi#memberJoiningRulesUpdate");
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
| **id** | **String**| Get by id | |
| **memberJoiningRuleUpdate** | [**MemberJoiningRuleUpdate**](MemberJoiningRuleUpdate.md)| Polymorphic Member Joining Rule Update | [optional] |

### Return type

[**MemberJoiningRule**](MemberJoiningRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Polymorphic Member Joining Rule |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

