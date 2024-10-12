# SupersimV1EsimProfileApi

All URIs are relative to *https://supersim.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createEsimProfile**](SupersimV1EsimProfileApi.md#createEsimProfile) | **POST** /v1/ESimProfiles |  |
| [**fetchEsimProfile**](SupersimV1EsimProfileApi.md#fetchEsimProfile) | **GET** /v1/ESimProfiles/{Sid} |  |
| [**listEsimProfile**](SupersimV1EsimProfileApi.md#listEsimProfile) | **GET** /v1/ESimProfiles |  |


<a id="createEsimProfile"></a>
# **createEsimProfile**
> SupersimV1EsimProfile createEsimProfile(callbackMethod, callbackUrl, eid, generateMatchingId)



Order an eSIM Profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1EsimProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1EsimProfileApi apiInstance = new SupersimV1EsimProfileApi(defaultClient);
    String callbackMethod = "HEAD"; // String | The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is POST.
    String callbackUrl = "callbackUrl_example"; // String | The URL we should call using the `callback_method` when the status of the eSIM Profile changes. At this stage of the eSIM Profile pilot, the a request to the URL will only be called when the ESimProfile resource changes from `reserving` to `available`.
    String eid = "eid_example"; // String | Identifier of the eUICC that will claim the eSIM Profile.
    Boolean generateMatchingId = true; // Boolean | When set to `true`, a value for `Eid` does not need to be provided. Instead, when the eSIM profile is reserved, a matching ID will be generated and returned via the `matching_id` property. This identifies the specific eSIM profile that can be used by any capable device to claim and download the profile.
    try {
      SupersimV1EsimProfile result = apiInstance.createEsimProfile(callbackMethod, callbackUrl, eid, generateMatchingId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1EsimProfileApi#createEsimProfile");
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
| **callbackMethod** | **String**| The HTTP method we should use to call &#x60;callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is POST. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **callbackUrl** | **String**| The URL we should call using the &#x60;callback_method&#x60; when the status of the eSIM Profile changes. At this stage of the eSIM Profile pilot, the a request to the URL will only be called when the ESimProfile resource changes from &#x60;reserving&#x60; to &#x60;available&#x60;. | [optional] |
| **eid** | **String**| Identifier of the eUICC that will claim the eSIM Profile. | [optional] |
| **generateMatchingId** | **Boolean**| When set to &#x60;true&#x60;, a value for &#x60;Eid&#x60; does not need to be provided. Instead, when the eSIM profile is reserved, a matching ID will be generated and returned via the &#x60;matching_id&#x60; property. This identifies the specific eSIM profile that can be used by any capable device to claim and download the profile. | [optional] |

### Return type

[**SupersimV1EsimProfile**](SupersimV1EsimProfile.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchEsimProfile"></a>
# **fetchEsimProfile**
> SupersimV1EsimProfile fetchEsimProfile(sid)



Fetch an eSIM Profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1EsimProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1EsimProfileApi apiInstance = new SupersimV1EsimProfileApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the eSIM Profile resource to fetch.
    try {
      SupersimV1EsimProfile result = apiInstance.fetchEsimProfile(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1EsimProfileApi#fetchEsimProfile");
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
| **sid** | **String**| The SID of the eSIM Profile resource to fetch. | |

### Return type

[**SupersimV1EsimProfile**](SupersimV1EsimProfile.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listEsimProfile"></a>
# **listEsimProfile**
> ListEsimProfileResponse listEsimProfile(eid, simSid, status, pageSize, page, pageToken)



Retrieve a list of eSIM Profiles.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1EsimProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1EsimProfileApi apiInstance = new SupersimV1EsimProfileApi(defaultClient);
    String eid = "eid_example"; // String | List the eSIM Profiles that have been associated with an EId.
    String simSid = "simSid_example"; // String | Find the eSIM Profile resource related to a [Sim](https://www.twilio.com/docs/iot/supersim/api/sim-resource) resource by providing the SIM SID. Will always return an array with either 1 or 0 records.
    EsimProfileEnumStatus status = EsimProfileEnumStatus.fromValue("new"); // EsimProfileEnumStatus | List the eSIM Profiles that are in a given status.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListEsimProfileResponse result = apiInstance.listEsimProfile(eid, simSid, status, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1EsimProfileApi#listEsimProfile");
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
| **eid** | **String**| List the eSIM Profiles that have been associated with an EId. | [optional] |
| **simSid** | **String**| Find the eSIM Profile resource related to a [Sim](https://www.twilio.com/docs/iot/supersim/api/sim-resource) resource by providing the SIM SID. Will always return an array with either 1 or 0 records. | [optional] |
| **status** | **EsimProfileEnumStatus**| List the eSIM Profiles that are in a given status. | [optional] [enum: new, reserving, available, downloaded, installed, failed] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListEsimProfileResponse**](ListEsimProfileResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

