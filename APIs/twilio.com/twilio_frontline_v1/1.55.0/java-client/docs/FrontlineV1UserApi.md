# FrontlineV1UserApi

All URIs are relative to *https://frontline-api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchUser**](FrontlineV1UserApi.md#fetchUser) | **GET** /v1/Users/{Sid} |  |
| [**updateUser**](FrontlineV1UserApi.md#updateUser) | **POST** /v1/Users/{Sid} |  |


<a id="fetchUser"></a>
# **fetchUser**
> FrontlineV1User fetchUser(sid)



Fetch a frontline user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FrontlineV1UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://frontline-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FrontlineV1UserApi apiInstance = new FrontlineV1UserApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the User resource to fetch. This value can be either the `sid` or the `identity` of the User resource to fetch.
    try {
      FrontlineV1User result = apiInstance.fetchUser(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FrontlineV1UserApi#fetchUser");
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
| **sid** | **String**| The SID of the User resource to fetch. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to fetch. | |

### Return type

[**FrontlineV1User**](FrontlineV1User.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateUser"></a>
# **updateUser**
> FrontlineV1User updateUser(sid, avatar, friendlyName, isAvailable, state)



Update an existing frontline user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FrontlineV1UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://frontline-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FrontlineV1UserApi apiInstance = new FrontlineV1UserApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
    String avatar = "avatar_example"; // String | The avatar URL which will be shown in Frontline application.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the User.
    Boolean isAvailable = true; // Boolean | Whether the User is available for new conversations. Set to `false` to prevent User from receiving new inbound conversations if you are using [Pool Routing](https://www.twilio.com/docs/frontline/handle-incoming-conversations#3-pool-routing).
    UserEnumStateType state = UserEnumStateType.fromValue("active"); // UserEnumStateType | 
    try {
      FrontlineV1User result = apiInstance.updateUser(sid, avatar, friendlyName, isAvailable, state);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FrontlineV1UserApi#updateUser");
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
| **sid** | **String**| The SID of the User resource to update. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to update. | |
| **avatar** | **String**| The avatar URL which will be shown in Frontline application. | [optional] |
| **friendlyName** | **String**| The string that you assigned to describe the User. | [optional] |
| **isAvailable** | **Boolean**| Whether the User is available for new conversations. Set to &#x60;false&#x60; to prevent User from receiving new inbound conversations if you are using [Pool Routing](https://www.twilio.com/docs/frontline/handle-incoming-conversations#3-pool-routing). | [optional] |
| **state** | **UserEnumStateType**|  | [optional] [enum: active, deactivated] |

### Return type

[**FrontlineV1User**](FrontlineV1User.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

