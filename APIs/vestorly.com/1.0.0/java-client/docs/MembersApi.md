# MembersApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createMember**](MembersApi.md#createMember) | **POST** /members |  |
| [**findMemberByID**](MembersApi.md#findMemberByID) | **GET** /members/{id} |  |
| [**findMembers**](MembersApi.md#findMembers) | **GET** /members |  |
| [**updateMemberByID**](MembersApi.md#updateMemberByID) | **PUT** /members/{id} |  |


<a id="createMember"></a>
# **createMember**
> Memberresponse createMember(vestorlyAuth, member, accessToken)



Create a new member in the Vestorly Platform

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
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    MembersApi apiInstance = new MembersApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    Member member = new Member(); // Member | Member you want to create
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Memberresponse result = apiInstance.createMember(vestorlyAuth, member, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#createMember");
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
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **member** | [**Member**](Member.md)| Member you want to create | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**Memberresponse**](Memberresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | member response |  -  |

<a id="findMemberByID"></a>
# **findMemberByID**
> Memberresponse findMemberByID(id, vestorlyAuth, accessToken)



Returns a single member

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
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    MembersApi apiInstance = new MembersApi(defaultClient);
    String id = "id_example"; // String | Mongo ID of member to fetch
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Memberresponse result = apiInstance.findMemberByID(id, vestorlyAuth, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#findMemberByID");
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
| **id** | **String**| Mongo ID of member to fetch | |
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**Memberresponse**](Memberresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Member response |  -  |

<a id="findMembers"></a>
# **findMembers**
> Members findMembers(vestorlyAuth, accessToken, start, limit)



Returns all members

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
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    MembersApi apiInstance = new MembersApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String accessToken = "accessToken_example"; // String | OAuth Token
    Integer start = 56; // Integer | Skips number of members from start
    Integer limit = 56; // Integer | Number of members to return
    try {
      Members result = apiInstance.findMembers(vestorlyAuth, accessToken, start, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#findMembers");
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
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **accessToken** | **String**| OAuth Token | [optional] |
| **start** | **Integer**| Skips number of members from start | [optional] |
| **limit** | **Integer**| Number of members to return | [optional] |

### Return type

[**Members**](Members.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Member response |  -  |

<a id="updateMemberByID"></a>
# **updateMemberByID**
> Memberresponse updateMemberByID(id, vestorlyAuth, member, accessToken)



Updates a single member

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
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    MembersApi apiInstance = new MembersApi(defaultClient);
    String id = "id_example"; // String | Mongo ID of member to fetch
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    Member member = new Member(); // Member | Member you want to update
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Memberresponse result = apiInstance.updateMemberByID(id, vestorlyAuth, member, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MembersApi#updateMemberByID");
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
| **id** | **String**| Mongo ID of member to fetch | |
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **member** | [**Member**](Member.md)| Member you want to update | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**Memberresponse**](Memberresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Member response |  -  |

