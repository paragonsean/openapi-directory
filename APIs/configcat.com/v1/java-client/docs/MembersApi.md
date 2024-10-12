# MembersApi

All URIs are relative to *https://api.configcat.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addMemberToGroup**](MembersApi.md#addMemberToGroup) | **POST** /v1/organizations/{organizationId}/members/{userId} | Update Member Permissions |
| [**deleteOrganizationMember**](MembersApi.md#deleteOrganizationMember) | **DELETE** /v1/organizations/{organizationId}/members/{userId} | Delete Member from Organization |
| [**deleteProductMember**](MembersApi.md#deleteProductMember) | **DELETE** /v1/products/{productId}/members/{userId} | Delete Member from Product |
| [**getOrganizationMembers**](MembersApi.md#getOrganizationMembers) | **GET** /v1/organizations/{organizationId}/members | List Organization Members |
| [**getProductMembers**](MembersApi.md#getProductMembers) | **GET** /v1/products/{productId}/members | List Product Members |
| [**inviteMember**](MembersApi.md#inviteMember) | **POST** /v1/products/{productId}/members/invite | Invite Member |


<a id="addMemberToGroup"></a>
# **addMemberToGroup**
> addMemberToGroup(organizationId, userId, addUserToGroupRequest)

Update Member Permissions

This endpoint adds a Member identified by the &#x60;userId&#x60; to one or more Permission Groups.  This endpoint can also be used to move a Member between Permission Groups within a Product. Only a single Permission Group can be set per Product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.configcat.com");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    MembersApi apiInstance = new MembersApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | The identifier of the Organization.
    String userId = "userId_example"; // String | The identifier of the Member.
    AddUserToGroupRequest addUserToGroupRequest = new AddUserToGroupRequest(); // AddUserToGroupRequest | 
    try {
      apiInstance.addMemberToGroup(organizationId, userId, addUserToGroupRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#addMemberToGroup");
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
| **organizationId** | **UUID**| The identifier of the Organization. | |
| **userId** | **String**| The identifier of the Member. | |
| **addUserToGroupRequest** | [**AddUserToGroupRequest**](AddUserToGroupRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | When the addition was successful. |  -  |
| **400** | Bad request. |  -  |
| **401** | Unauthorized. In case of the Public Management API credentials are invalid. |  -  |
| **404** | Not found. |  -  |
| **429** | Too many requests. In case of the request rate exceeds the rate limits. |  -  |

<a id="deleteOrganizationMember"></a>
# **deleteOrganizationMember**
> deleteOrganizationMember(organizationId, userId)

Delete Member from Organization

This endpoint removes a Member identified by the &#x60;userId&#x60; from the  given Organization identified by the &#x60;organizationId&#x60; parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.configcat.com");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    MembersApi apiInstance = new MembersApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | The identifier of the Organization.
    String userId = "userId_example"; // String | The identifier of the Member.
    try {
      apiInstance.deleteOrganizationMember(organizationId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#deleteOrganizationMember");
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
| **organizationId** | **UUID**| The identifier of the Organization. | |
| **userId** | **String**| The identifier of the Member. | |

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | When the delete was successful. |  -  |
| **400** | Bad request. |  -  |
| **401** | Unauthorized. In case of the Public Management API credentials are invalid. |  -  |
| **404** | Not found. |  -  |
| **429** | Too many requests. In case of the request rate exceeds the rate limits. |  -  |

<a id="deleteProductMember"></a>
# **deleteProductMember**
> deleteProductMember(productId, userId)

Delete Member from Product

This endpoint removes a Member identified by the &#x60;userId&#x60; from the  given Product identified by the &#x60;productId&#x60; parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.configcat.com");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    MembersApi apiInstance = new MembersApi(defaultClient);
    UUID productId = UUID.randomUUID(); // UUID | The identifier of the Product.
    String userId = "userId_example"; // String | The identifier of the Member.
    try {
      apiInstance.deleteProductMember(productId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#deleteProductMember");
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
| **productId** | **UUID**| The identifier of the Product. | |
| **userId** | **String**| The identifier of the Member. | |

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | When the delete was successful. |  -  |
| **400** | Bad request. |  -  |
| **401** | Unauthorized. In case of the Public Management API credentials are invalid. |  -  |
| **404** | Not found. |  -  |
| **429** | Too many requests. In case of the request rate exceeds the rate limits. |  -  |

<a id="getOrganizationMembers"></a>
# **getOrganizationMembers**
> List&lt;UserModel&gt; getOrganizationMembers(organizationId)

List Organization Members

This endpoint returns the list of Members that belongs  to the given Organization, identified by the &#x60;organizationId&#x60; parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.configcat.com");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    MembersApi apiInstance = new MembersApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | The identifier of the Organization.
    try {
      List<UserModel> result = apiInstance.getOrganizationMembers(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#getOrganizationMembers");
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
| **organizationId** | **UUID**| The identifier of the Organization. | |

### Return type

[**List&lt;UserModel&gt;**](UserModel.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Bad request. |  -  |
| **401** | Unauthorized. In case of the Public Management API credentials are invalid. |  -  |
| **404** | Not found. |  -  |
| **429** | Too many requests. In case of the request rate exceeds the rate limits. |  -  |

<a id="getProductMembers"></a>
# **getProductMembers**
> List&lt;MemberModel&gt; getProductMembers(productId)

List Product Members

This endpoint returns the list of Members that belongs  to the given Product, identified by the &#x60;productId&#x60; parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.configcat.com");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    MembersApi apiInstance = new MembersApi(defaultClient);
    UUID productId = UUID.randomUUID(); // UUID | The identifier of the Product.
    try {
      List<MemberModel> result = apiInstance.getProductMembers(productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#getProductMembers");
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
| **productId** | **UUID**| The identifier of the Product. | |

### Return type

[**List&lt;MemberModel&gt;**](MemberModel.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Bad request. |  -  |
| **401** | Unauthorized. In case of the Public Management API credentials are invalid. |  -  |
| **404** | Not found. |  -  |
| **429** | Too many requests. In case of the request rate exceeds the rate limits. |  -  |

<a id="inviteMember"></a>
# **inviteMember**
> inviteMember(productId, inviteMembersRequest)

Invite Member

This endpoint invites a Member into the given Product identified by the &#x60;productId&#x60; parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.configcat.com");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    MembersApi apiInstance = new MembersApi(defaultClient);
    UUID productId = UUID.randomUUID(); // UUID | The identifier of the Product.
    InviteMembersRequest inviteMembersRequest = new InviteMembersRequest(); // InviteMembersRequest | 
    try {
      apiInstance.inviteMember(productId, inviteMembersRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#inviteMember");
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
| **productId** | **UUID**| The identifier of the Product. | |
| **inviteMembersRequest** | [**InviteMembersRequest**](InviteMembersRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | When the invite was successful. |  -  |
| **400** | Bad request. |  -  |
| **401** | Unauthorized. In case of the Public Management API credentials are invalid. |  -  |
| **404** | Not found. |  -  |
| **429** | Too many requests. In case of the request rate exceeds the rate limits. |  -  |

