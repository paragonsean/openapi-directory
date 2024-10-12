# SupersimV1SimApi

All URIs are relative to *https://supersim.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSim**](SupersimV1SimApi.md#createSim) | **POST** /v1/Sims |  |
| [**fetchSim**](SupersimV1SimApi.md#fetchSim) | **GET** /v1/Sims/{Sid} |  |
| [**listSim**](SupersimV1SimApi.md#listSim) | **GET** /v1/Sims |  |
| [**updateSim**](SupersimV1SimApi.md#updateSim) | **POST** /v1/Sims/{Sid} |  |


<a id="createSim"></a>
# **createSim**
> SupersimV1Sim createSim(iccid, registrationCode)



Register a Super SIM to your Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1SimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1SimApi apiInstance = new SupersimV1SimApi(defaultClient);
    String iccid = "iccid_example"; // String | The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) of the Super SIM to be added to your Account.
    String registrationCode = "registrationCode_example"; // String | The 10-digit code required to claim the Super SIM for your Account.
    try {
      SupersimV1Sim result = apiInstance.createSim(iccid, registrationCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1SimApi#createSim");
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
| **iccid** | **String**| The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) of the Super SIM to be added to your Account. | |
| **registrationCode** | **String**| The 10-digit code required to claim the Super SIM for your Account. | |

### Return type

[**SupersimV1Sim**](SupersimV1Sim.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchSim"></a>
# **fetchSim**
> SupersimV1Sim fetchSim(sid)



Fetch a Super SIM instance from your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1SimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1SimApi apiInstance = new SupersimV1SimApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Sim resource to fetch.
    try {
      SupersimV1Sim result = apiInstance.fetchSim(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1SimApi#fetchSim");
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
| **sid** | **String**| The SID of the Sim resource to fetch. | |

### Return type

[**SupersimV1Sim**](SupersimV1Sim.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSim"></a>
# **listSim**
> ListSimResponse listSim(status, fleet, iccid, pageSize, page, pageToken)



Retrieve a list of Super SIMs from your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1SimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1SimApi apiInstance = new SupersimV1SimApi(defaultClient);
    SimEnumStatus status = SimEnumStatus.fromValue("new"); // SimEnumStatus | The status of the Sim resources to read. Can be `new`, `ready`, `active`, `inactive`, or `scheduled`.
    String fleet = "fleet_example"; // String | The SID or unique name of the Fleet to which a list of Sims are assigned.
    String iccid = "iccid_example"; // String | The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with a Super SIM to filter the list by. Passing this parameter will always return a list containing zero or one SIMs.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSimResponse result = apiInstance.listSim(status, fleet, iccid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1SimApi#listSim");
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
| **status** | **SimEnumStatus**| The status of the Sim resources to read. Can be &#x60;new&#x60;, &#x60;ready&#x60;, &#x60;active&#x60;, &#x60;inactive&#x60;, or &#x60;scheduled&#x60;. | [optional] [enum: new, ready, active, inactive, scheduled] |
| **fleet** | **String**| The SID or unique name of the Fleet to which a list of Sims are assigned. | [optional] |
| **iccid** | **String**| The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with a Super SIM to filter the list by. Passing this parameter will always return a list containing zero or one SIMs. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSimResponse**](ListSimResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSim"></a>
# **updateSim**
> SupersimV1Sim updateSim(sid, accountSid, callbackMethod, callbackUrl, fleet, status, uniqueName)



Updates the given properties of a Super SIM instance from your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1SimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1SimApi apiInstance = new SupersimV1SimApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Sim resource to update.
    String accountSid = "accountSid_example"; // String | The SID of the Account to which the Sim resource should belong. The Account SID can only be that of the requesting Account or that of a Subaccount of the requesting Account. Only valid when the Sim resource's status is new.
    String callbackMethod = "HEAD"; // String | The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is POST.
    URI callbackUrl = new URI(); // URI | The URL we should call using the `callback_method` after an asynchronous update has finished.
    String fleet = "fleet_example"; // String | The SID or unique name of the Fleet to which the SIM resource should be assigned.
    SimEnumStatusUpdate status = SimEnumStatusUpdate.fromValue("ready"); // SimEnumStatusUpdate | 
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
    try {
      SupersimV1Sim result = apiInstance.updateSim(sid, accountSid, callbackMethod, callbackUrl, fleet, status, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1SimApi#updateSim");
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
| **sid** | **String**| The SID of the Sim resource to update. | |
| **accountSid** | **String**| The SID of the Account to which the Sim resource should belong. The Account SID can only be that of the requesting Account or that of a Subaccount of the requesting Account. Only valid when the Sim resource&#39;s status is new. | [optional] |
| **callbackMethod** | **String**| The HTTP method we should use to call &#x60;callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is POST. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **callbackUrl** | **URI**| The URL we should call using the &#x60;callback_method&#x60; after an asynchronous update has finished. | [optional] |
| **fleet** | **String**| The SID or unique name of the Fleet to which the SIM resource should be assigned. | [optional] |
| **status** | **SimEnumStatusUpdate**|  | [optional] [enum: ready, active, inactive] |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource. | [optional] |

### Return type

[**SupersimV1Sim**](SupersimV1Sim.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

