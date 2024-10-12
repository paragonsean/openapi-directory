# OauthApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createToken**](OauthApi.md#createToken) | **POST** /oauth/token | Create an oauth token |
| [**fetchTokenGroups**](OauthApi.md#fetchTokenGroups) | **GET** /oauth/token/{id}/groups | Get the groups for a token |
| [**fetchTokenOrganization**](OauthApi.md#fetchTokenOrganization) | **GET** /oauth/token/{id}/organization | Get the organization for a token |


<a id="createToken"></a>
# **createToken**
> CreateTokenResponse createToken(createTokenRequest, include)

Create an oauth token

Create an OAuth 2.0 Bearer token. A valid bearer token is required for all other API requests.  Be sure to set the header &#x60;Content-Type: \&quot;application/vnd.api+json\&quot;&#x60;. Otherwise, you will get an error 403 Forbidden. Using &#x60;Content-Type: \&quot;application/json\&quot;&#x60; is permitted (to support older oauth clients) but when using &#x60;application/json&#x60; the body should have a body in the following format instead of nesting under &#x60;data.attributes&#x60;: &#x60;&#x60;&#x60; {   \&quot;grant_type\&quot;: \&quot;client_credentials\&quot;,   \&quot;client_id\&quot;: \&quot;95c78ab2-167f-40b8-8bec-8398d4b87454\&quot;,   \&quot;client_secret\&quot;: \&quot;35d18dc9-a3dd-4948-b787-063a490b9354\&quot; } &#x60;&#x60;&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    OauthApi apiInstance = new OauthApi(defaultClient);
    CreateTokenRequest createTokenRequest = new CreateTokenRequest(); // CreateTokenRequest | 
    String include = "groups"; // String | List of related resources to include in the response
    try {
      CreateTokenResponse result = apiInstance.createToken(createTokenRequest, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#createToken");
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
| **createTokenRequest** | [**CreateTokenRequest**](CreateTokenRequest.md)|  | |
| **include** | **String**| List of related resources to include in the response | [optional] [enum: groups, organization] |

### Return type

[**CreateTokenResponse**](CreateTokenResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **409** | Invalid Request |  -  |

<a id="fetchTokenGroups"></a>
# **fetchTokenGroups**
> FetchGroupsResponse fetchTokenGroups(id)

Get the groups for a token

Get the list of groups a token can be used to access.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    OauthApi apiInstance = new OauthApi(defaultClient);
    String id = "id_example"; // String | Token identifier
    try {
      FetchGroupsResponse result = apiInstance.fetchTokenGroups(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#fetchTokenGroups");
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
| **id** | **String**| Token identifier | |

### Return type

[**FetchGroupsResponse**](FetchGroupsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="fetchTokenOrganization"></a>
# **fetchTokenOrganization**
> FetchOrganizationResponse fetchTokenOrganization(id)

Get the organization for a token

Get the organization a token can be used to access.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    OauthApi apiInstance = new OauthApi(defaultClient);
    String id = "id_example"; // String | Token identifier
    try {
      FetchOrganizationResponse result = apiInstance.fetchTokenOrganization(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#fetchTokenOrganization");
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
| **id** | **String**| Token identifier | |

### Return type

[**FetchOrganizationResponse**](FetchOrganizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

