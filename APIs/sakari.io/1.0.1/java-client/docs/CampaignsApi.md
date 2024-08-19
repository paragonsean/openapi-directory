# CampaignsApi

All URIs are relative to *https://api.sakari.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**campaignsCreate**](CampaignsApi.md#campaignsCreate) | **POST** /v1/accounts/{accountId}/campaigns | Create campaign |
| [**campaignsFetch**](CampaignsApi.md#campaignsFetch) | **GET** /v1/accounts/{accountId}/campaigns/{campaignId} | Fetch campaign by ID |
| [**campaignsFetchAll**](CampaignsApi.md#campaignsFetchAll) | **GET** /v1/accounts/{accountId}/campaigns | Fetch campaigns |
| [**campaignsRemove**](CampaignsApi.md#campaignsRemove) | **DELETE** /v1/accounts/{accountId}/campaigns/{campaignId} | Deletes a campaign |
| [**campaignsUpdate**](CampaignsApi.md#campaignsUpdate) | **PUT** /v1/accounts/{accountId}/campaigns/{campaignId} | Updates a campaign |


<a id="campaignsCreate"></a>
# **campaignsCreate**
> CampaignResponse campaignsCreate(accountId, campaignRequest)

Create campaign

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    CampaignsApi apiInstance = new CampaignsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    CampaignRequest campaignRequest = new CampaignRequest(); // CampaignRequest | 
    try {
      CampaignResponse result = apiInstance.campaignsCreate(accountId, campaignRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignsApi#campaignsCreate");
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
| **accountId** | **String**| Account to apply operations to | |
| **campaignRequest** | [**CampaignRequest**](CampaignRequest.md)|  | [optional] |

### Return type

[**CampaignResponse**](CampaignResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | successful operation |  -  |

<a id="campaignsFetch"></a>
# **campaignsFetch**
> CampaignResponse campaignsFetch(accountId, campaignId)

Fetch campaign by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    CampaignsApi apiInstance = new CampaignsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    String campaignId = "campaignId_example"; // String | ID of campaign to return
    try {
      CampaignResponse result = apiInstance.campaignsFetch(accountId, campaignId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignsApi#campaignsFetch");
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
| **accountId** | **String**| Account to apply operations to | |
| **campaignId** | **String**| ID of campaign to return | |

### Return type

[**CampaignResponse**](CampaignResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="campaignsFetchAll"></a>
# **campaignsFetchAll**
> CampaignsResponse campaignsFetchAll(accountId, offset, limit, name)

Fetch campaigns

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    CampaignsApi apiInstance = new CampaignsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    Long offset = 56L; // Long | Results to skip when paginating through a result set
    Long limit = 56L; // Long | Maximum number of results to return
    String name = "name_example"; // String | Filter by name or part of
    try {
      CampaignsResponse result = apiInstance.campaignsFetchAll(accountId, offset, limit, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignsApi#campaignsFetchAll");
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
| **accountId** | **String**| Account to apply operations to | |
| **offset** | **Long**| Results to skip when paginating through a result set | [optional] |
| **limit** | **Long**| Maximum number of results to return | [optional] |
| **name** | **String**| Filter by name or part of | [optional] |

### Return type

[**CampaignsResponse**](CampaignsResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **4XX** | invalid request |  -  |
| **5XX** | invalid request |  -  |

<a id="campaignsRemove"></a>
# **campaignsRemove**
> CampaignsRemove200Response campaignsRemove(accountId, campaignId)

Deletes a campaign

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    CampaignsApi apiInstance = new CampaignsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    String campaignId = "campaignId_example"; // String | Campaign id to delete
    try {
      CampaignsRemove200Response result = apiInstance.campaignsRemove(accountId, campaignId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignsApi#campaignsRemove");
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
| **accountId** | **String**| Account to apply operations to | |
| **campaignId** | **String**| Campaign id to delete | |

### Return type

[**CampaignsRemove200Response**](CampaignsRemove200Response.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="campaignsUpdate"></a>
# **campaignsUpdate**
> CampaignResponse campaignsUpdate(accountId, campaignId)

Updates a campaign

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampaignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    CampaignsApi apiInstance = new CampaignsApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    String campaignId = "campaignId_example"; // String | ID of campaign
    try {
      CampaignResponse result = apiInstance.campaignsUpdate(accountId, campaignId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampaignsApi#campaignsUpdate");
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
| **accountId** | **String**| Account to apply operations to | |
| **campaignId** | **String**| ID of campaign | |

### Return type

[**CampaignResponse**](CampaignResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

