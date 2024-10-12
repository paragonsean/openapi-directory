# VoiceV1ConnectionPolicyTargetApi

All URIs are relative to *https://voice.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createConnectionPolicyTarget**](VoiceV1ConnectionPolicyTargetApi.md#createConnectionPolicyTarget) | **POST** /v1/ConnectionPolicies/{ConnectionPolicySid}/Targets |  |
| [**deleteConnectionPolicyTarget**](VoiceV1ConnectionPolicyTargetApi.md#deleteConnectionPolicyTarget) | **DELETE** /v1/ConnectionPolicies/{ConnectionPolicySid}/Targets/{Sid} |  |
| [**fetchConnectionPolicyTarget**](VoiceV1ConnectionPolicyTargetApi.md#fetchConnectionPolicyTarget) | **GET** /v1/ConnectionPolicies/{ConnectionPolicySid}/Targets/{Sid} |  |
| [**listConnectionPolicyTarget**](VoiceV1ConnectionPolicyTargetApi.md#listConnectionPolicyTarget) | **GET** /v1/ConnectionPolicies/{ConnectionPolicySid}/Targets |  |
| [**updateConnectionPolicyTarget**](VoiceV1ConnectionPolicyTargetApi.md#updateConnectionPolicyTarget) | **POST** /v1/ConnectionPolicies/{ConnectionPolicySid}/Targets/{Sid} |  |


<a id="createConnectionPolicyTarget"></a>
# **createConnectionPolicyTarget**
> VoiceV1ConnectionPolicyConnectionPolicyTarget createConnectionPolicyTarget(connectionPolicySid, target, enabled, friendlyName, priority, weight)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceV1ConnectionPolicyTargetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://voice.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VoiceV1ConnectionPolicyTargetApi apiInstance = new VoiceV1ConnectionPolicyTargetApi(defaultClient);
    String connectionPolicySid = "connectionPolicySid_example"; // String | The SID of the Connection Policy that owns the Target.
    URI target = new URI(); // URI | The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.
    Boolean enabled = true; // Boolean | Whether the Target is enabled. The default is `true`.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    Integer priority = 56; // Integer | The relative importance of the target. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important target.
    Integer weight = 56; // Integer | The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. Targets with higher values receive more load than those with lower ones with the same priority.
    try {
      VoiceV1ConnectionPolicyConnectionPolicyTarget result = apiInstance.createConnectionPolicyTarget(connectionPolicySid, target, enabled, friendlyName, priority, weight);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceV1ConnectionPolicyTargetApi#createConnectionPolicyTarget");
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
| **connectionPolicySid** | **String**| The SID of the Connection Policy that owns the Target. | |
| **target** | **URI**| The SIP address you want Twilio to route your calls to. This must be a &#x60;sip:&#x60; schema. &#x60;sips&#x60; is NOT supported. | |
| **enabled** | **Boolean**| Whether the Target is enabled. The default is &#x60;true&#x60;. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long. | [optional] |
| **priority** | **Integer**| The relative importance of the target. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important target. | [optional] |
| **weight** | **Integer**| The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. Targets with higher values receive more load than those with lower ones with the same priority. | [optional] |

### Return type

[**VoiceV1ConnectionPolicyConnectionPolicyTarget**](VoiceV1ConnectionPolicyConnectionPolicyTarget.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteConnectionPolicyTarget"></a>
# **deleteConnectionPolicyTarget**
> deleteConnectionPolicyTarget(connectionPolicySid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceV1ConnectionPolicyTargetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://voice.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VoiceV1ConnectionPolicyTargetApi apiInstance = new VoiceV1ConnectionPolicyTargetApi(defaultClient);
    String connectionPolicySid = "connectionPolicySid_example"; // String | The SID of the Connection Policy that owns the Target.
    String sid = "sid_example"; // String | The unique string that we created to identify the Target resource to delete.
    try {
      apiInstance.deleteConnectionPolicyTarget(connectionPolicySid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceV1ConnectionPolicyTargetApi#deleteConnectionPolicyTarget");
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
| **connectionPolicySid** | **String**| The SID of the Connection Policy that owns the Target. | |
| **sid** | **String**| The unique string that we created to identify the Target resource to delete. | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchConnectionPolicyTarget"></a>
# **fetchConnectionPolicyTarget**
> VoiceV1ConnectionPolicyConnectionPolicyTarget fetchConnectionPolicyTarget(connectionPolicySid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceV1ConnectionPolicyTargetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://voice.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VoiceV1ConnectionPolicyTargetApi apiInstance = new VoiceV1ConnectionPolicyTargetApi(defaultClient);
    String connectionPolicySid = "connectionPolicySid_example"; // String | The SID of the Connection Policy that owns the Target.
    String sid = "sid_example"; // String | The unique string that we created to identify the Target resource to fetch.
    try {
      VoiceV1ConnectionPolicyConnectionPolicyTarget result = apiInstance.fetchConnectionPolicyTarget(connectionPolicySid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceV1ConnectionPolicyTargetApi#fetchConnectionPolicyTarget");
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
| **connectionPolicySid** | **String**| The SID of the Connection Policy that owns the Target. | |
| **sid** | **String**| The unique string that we created to identify the Target resource to fetch. | |

### Return type

[**VoiceV1ConnectionPolicyConnectionPolicyTarget**](VoiceV1ConnectionPolicyConnectionPolicyTarget.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listConnectionPolicyTarget"></a>
# **listConnectionPolicyTarget**
> ListConnectionPolicyTargetResponse listConnectionPolicyTarget(connectionPolicySid, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceV1ConnectionPolicyTargetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://voice.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VoiceV1ConnectionPolicyTargetApi apiInstance = new VoiceV1ConnectionPolicyTargetApi(defaultClient);
    String connectionPolicySid = "connectionPolicySid_example"; // String | The SID of the Connection Policy from which to read the Targets.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListConnectionPolicyTargetResponse result = apiInstance.listConnectionPolicyTarget(connectionPolicySid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceV1ConnectionPolicyTargetApi#listConnectionPolicyTarget");
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
| **connectionPolicySid** | **String**| The SID of the Connection Policy from which to read the Targets. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListConnectionPolicyTargetResponse**](ListConnectionPolicyTargetResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateConnectionPolicyTarget"></a>
# **updateConnectionPolicyTarget**
> VoiceV1ConnectionPolicyConnectionPolicyTarget updateConnectionPolicyTarget(connectionPolicySid, sid, enabled, friendlyName, priority, target, weight)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceV1ConnectionPolicyTargetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://voice.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VoiceV1ConnectionPolicyTargetApi apiInstance = new VoiceV1ConnectionPolicyTargetApi(defaultClient);
    String connectionPolicySid = "connectionPolicySid_example"; // String | The SID of the Connection Policy that owns the Target.
    String sid = "sid_example"; // String | The unique string that we created to identify the Target resource to update.
    Boolean enabled = true; // Boolean | Whether the Target is enabled.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    Integer priority = 56; // Integer | The relative importance of the target. Can be an integer from 0 to 65535, inclusive. The lowest number represents the most important target.
    URI target = new URI(); // URI | The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.
    Integer weight = 56; // Integer | The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive. Targets with higher values receive more load than those with lower ones with the same priority.
    try {
      VoiceV1ConnectionPolicyConnectionPolicyTarget result = apiInstance.updateConnectionPolicyTarget(connectionPolicySid, sid, enabled, friendlyName, priority, target, weight);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceV1ConnectionPolicyTargetApi#updateConnectionPolicyTarget");
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
| **connectionPolicySid** | **String**| The SID of the Connection Policy that owns the Target. | |
| **sid** | **String**| The unique string that we created to identify the Target resource to update. | |
| **enabled** | **Boolean**| Whether the Target is enabled. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long. | [optional] |
| **priority** | **Integer**| The relative importance of the target. Can be an integer from 0 to 65535, inclusive. The lowest number represents the most important target. | [optional] |
| **target** | **URI**| The SIP address you want Twilio to route your calls to. This must be a &#x60;sip:&#x60; schema. &#x60;sips&#x60; is NOT supported. | [optional] |
| **weight** | **Integer**| The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive. Targets with higher values receive more load than those with lower ones with the same priority. | [optional] |

### Return type

[**VoiceV1ConnectionPolicyConnectionPolicyTarget**](VoiceV1ConnectionPolicyConnectionPolicyTarget.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

