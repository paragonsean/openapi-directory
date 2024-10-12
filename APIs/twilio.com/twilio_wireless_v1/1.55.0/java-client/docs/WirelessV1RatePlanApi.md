# WirelessV1RatePlanApi

All URIs are relative to *https://wireless.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRatePlan**](WirelessV1RatePlanApi.md#createRatePlan) | **POST** /v1/RatePlans |  |
| [**deleteRatePlan**](WirelessV1RatePlanApi.md#deleteRatePlan) | **DELETE** /v1/RatePlans/{Sid} |  |
| [**fetchRatePlan**](WirelessV1RatePlanApi.md#fetchRatePlan) | **GET** /v1/RatePlans/{Sid} |  |
| [**listRatePlan**](WirelessV1RatePlanApi.md#listRatePlan) | **GET** /v1/RatePlans |  |
| [**updateRatePlan**](WirelessV1RatePlanApi.md#updateRatePlan) | **POST** /v1/RatePlans/{Sid} |  |


<a id="createRatePlan"></a>
# **createRatePlan**
> WirelessV1RatePlan createRatePlan(dataEnabled, dataLimit, dataMetering, friendlyName, internationalRoaming, internationalRoamingDataLimit, messagingEnabled, nationalRoamingDataLimit, nationalRoamingEnabled, uniqueName, voiceEnabled)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessV1RatePlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wireless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    WirelessV1RatePlanApi apiInstance = new WirelessV1RatePlanApi(defaultClient);
    Boolean dataEnabled = true; // Boolean | Whether SIMs can use GPRS/3G/4G/LTE data connectivity.
    Integer dataLimit = 56; // Integer | The total data usage (download and upload combined) in Megabytes that the Network allows during one month on the home network (T-Mobile USA). The metering period begins the day of activation and ends on the same day in the following month. Can be up to 2TB and the default value is `1000`.
    String dataMetering = "dataMetering_example"; // String | The model used to meter data usage. Can be: `payg` and `quota-1`, `quota-10`, and `quota-50`. Learn more about the available [data metering models](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource#payg-vs-quota-data-plans).
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It does not have to be unique.
    List<String> internationalRoaming = Arrays.asList(); // List<String> | The list of services that SIMs capable of using GPRS/3G/4G/LTE data connectivity can use outside of the United States. Can contain: `data` and `messaging`.
    Integer internationalRoamingDataLimit = 56; // Integer | The total data usage (download and upload combined) in Megabytes that the Network allows during one month when roaming outside the United States. Can be up to 2TB.
    Boolean messagingEnabled = true; // Boolean | Whether SIMs can make, send, and receive SMS using [Commands](https://www.twilio.com/docs/iot/wireless/api/command-resource).
    Integer nationalRoamingDataLimit = 56; // Integer | The total data usage (download and upload combined) in Megabytes that the Network allows during one month on non-home networks in the United States. The metering period begins the day of activation and ends on the same day in the following month. Can be up to 2TB. See [national roaming](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource#national-roaming) for more info.
    Boolean nationalRoamingEnabled = true; // Boolean | Whether SIMs can roam on networks other than the home network (T-Mobile USA) in the United States. See [national roaming](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource#national-roaming).
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
    Boolean voiceEnabled = true; // Boolean | Deprecated.
    try {
      WirelessV1RatePlan result = apiInstance.createRatePlan(dataEnabled, dataLimit, dataMetering, friendlyName, internationalRoaming, internationalRoamingDataLimit, messagingEnabled, nationalRoamingDataLimit, nationalRoamingEnabled, uniqueName, voiceEnabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessV1RatePlanApi#createRatePlan");
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
| **dataEnabled** | **Boolean**| Whether SIMs can use GPRS/3G/4G/LTE data connectivity. | [optional] |
| **dataLimit** | **Integer**| The total data usage (download and upload combined) in Megabytes that the Network allows during one month on the home network (T-Mobile USA). The metering period begins the day of activation and ends on the same day in the following month. Can be up to 2TB and the default value is &#x60;1000&#x60;. | [optional] |
| **dataMetering** | **String**| The model used to meter data usage. Can be: &#x60;payg&#x60; and &#x60;quota-1&#x60;, &#x60;quota-10&#x60;, and &#x60;quota-50&#x60;. Learn more about the available [data metering models](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource#payg-vs-quota-data-plans). | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It does not have to be unique. | [optional] |
| **internationalRoaming** | [**List&lt;String&gt;**](String.md)| The list of services that SIMs capable of using GPRS/3G/4G/LTE data connectivity can use outside of the United States. Can contain: &#x60;data&#x60; and &#x60;messaging&#x60;. | [optional] |
| **internationalRoamingDataLimit** | **Integer**| The total data usage (download and upload combined) in Megabytes that the Network allows during one month when roaming outside the United States. Can be up to 2TB. | [optional] |
| **messagingEnabled** | **Boolean**| Whether SIMs can make, send, and receive SMS using [Commands](https://www.twilio.com/docs/iot/wireless/api/command-resource). | [optional] |
| **nationalRoamingDataLimit** | **Integer**| The total data usage (download and upload combined) in Megabytes that the Network allows during one month on non-home networks in the United States. The metering period begins the day of activation and ends on the same day in the following month. Can be up to 2TB. See [national roaming](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource#national-roaming) for more info. | [optional] |
| **nationalRoamingEnabled** | **Boolean**| Whether SIMs can roam on networks other than the home network (T-Mobile USA) in the United States. See [national roaming](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource#national-roaming). | [optional] |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource. | [optional] |
| **voiceEnabled** | **Boolean**| Deprecated. | [optional] |

### Return type

[**WirelessV1RatePlan**](WirelessV1RatePlan.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteRatePlan"></a>
# **deleteRatePlan**
> deleteRatePlan(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessV1RatePlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wireless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    WirelessV1RatePlanApi apiInstance = new WirelessV1RatePlanApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the RatePlan resource to delete.
    try {
      apiInstance.deleteRatePlan(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessV1RatePlanApi#deleteRatePlan");
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
| **sid** | **String**| The SID of the RatePlan resource to delete. | |

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

<a id="fetchRatePlan"></a>
# **fetchRatePlan**
> WirelessV1RatePlan fetchRatePlan(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessV1RatePlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wireless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    WirelessV1RatePlanApi apiInstance = new WirelessV1RatePlanApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the RatePlan resource to fetch.
    try {
      WirelessV1RatePlan result = apiInstance.fetchRatePlan(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessV1RatePlanApi#fetchRatePlan");
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
| **sid** | **String**| The SID of the RatePlan resource to fetch. | |

### Return type

[**WirelessV1RatePlan**](WirelessV1RatePlan.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listRatePlan"></a>
# **listRatePlan**
> ListRatePlanResponse listRatePlan(pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessV1RatePlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wireless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    WirelessV1RatePlanApi apiInstance = new WirelessV1RatePlanApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListRatePlanResponse result = apiInstance.listRatePlan(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessV1RatePlanApi#listRatePlan");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListRatePlanResponse**](ListRatePlanResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateRatePlan"></a>
# **updateRatePlan**
> WirelessV1RatePlan updateRatePlan(sid, friendlyName, uniqueName)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessV1RatePlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wireless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    WirelessV1RatePlanApi apiInstance = new WirelessV1RatePlanApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the RatePlan resource to update.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It does not have to be unique.
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
    try {
      WirelessV1RatePlan result = apiInstance.updateRatePlan(sid, friendlyName, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessV1RatePlanApi#updateRatePlan");
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
| **sid** | **String**| The SID of the RatePlan resource to update. | |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It does not have to be unique. | [optional] |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource. | [optional] |

### Return type

[**WirelessV1RatePlan**](WirelessV1RatePlan.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

