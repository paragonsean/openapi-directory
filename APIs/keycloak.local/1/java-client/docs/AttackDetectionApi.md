# AttackDetectionApi

All URIs are relative to *http://keycloak.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**realmAttackDetectionBruteForceUsersDelete**](AttackDetectionApi.md#realmAttackDetectionBruteForceUsersDelete) | **DELETE** /{realm}/attack-detection/brute-force/users | Clear any user login failures for all users   This can release temporary disabled users |
| [**realmAttackDetectionBruteForceUsersUserIdDelete**](AttackDetectionApi.md#realmAttackDetectionBruteForceUsersUserIdDelete) | **DELETE** /{realm}/attack-detection/brute-force/users/{userId} | Clear any user login failures for the user   This can release temporary disabled user |
| [**realmAttackDetectionBruteForceUsersUserIdGet**](AttackDetectionApi.md#realmAttackDetectionBruteForceUsersUserIdGet) | **GET** /{realm}/attack-detection/brute-force/users/{userId} | Get status of a username in brute force detection |


<a id="realmAttackDetectionBruteForceUsersDelete"></a>
# **realmAttackDetectionBruteForceUsersDelete**
> realmAttackDetectionBruteForceUsersDelete(realm)

Clear any user login failures for all users   This can release temporary disabled users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttackDetectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AttackDetectionApi apiInstance = new AttackDetectionApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      apiInstance.realmAttackDetectionBruteForceUsersDelete(realm);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttackDetectionApi#realmAttackDetectionBruteForceUsersDelete");
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
| **realm** | **String**| realm name (not id!) | |

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmAttackDetectionBruteForceUsersUserIdDelete"></a>
# **realmAttackDetectionBruteForceUsersUserIdDelete**
> realmAttackDetectionBruteForceUsersUserIdDelete(realm, userId)

Clear any user login failures for the user   This can release temporary disabled user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttackDetectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AttackDetectionApi apiInstance = new AttackDetectionApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String userId = "userId_example"; // String | 
    try {
      apiInstance.realmAttackDetectionBruteForceUsersUserIdDelete(realm, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttackDetectionApi#realmAttackDetectionBruteForceUsersUserIdDelete");
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
| **realm** | **String**| realm name (not id!) | |
| **userId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmAttackDetectionBruteForceUsersUserIdGet"></a>
# **realmAttackDetectionBruteForceUsersUserIdGet**
> Map&lt;String, Object&gt; realmAttackDetectionBruteForceUsersUserIdGet(realm, userId)

Get status of a username in brute force detection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttackDetectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AttackDetectionApi apiInstance = new AttackDetectionApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String userId = "userId_example"; // String | 
    try {
      Map<String, Object> result = apiInstance.realmAttackDetectionBruteForceUsersUserIdGet(realm, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttackDetectionApi#realmAttackDetectionBruteForceUsersUserIdGet");
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
| **realm** | **String**| realm name (not id!) | |
| **userId** | **String**|  | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

