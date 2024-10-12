# ActionApi

All URIs are relative to *https://ioe2api.ijenko.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deviceRun**](ActionApi.md#deviceRun) | **POST** /devices/{deviceId}/run/{action} | Run actions |
| [**functionalityRun**](ActionApi.md#functionalityRun) | **POST** /functionalities/{functionalityId}/run/{action} | Run an action |
| [**placeRun**](ActionApi.md#placeRun) | **POST** /places/{placeId}/run/{action} | Run actions |


<a id="deviceRun"></a>
# **deviceRun**
> List&lt;ActionResult&gt; deviceRun(deviceId, action, functionalities, arguments)

Run actions

Run an *Action* on zero, one or multiple Functionalities selected with tags. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique identifier of a *Device*.
    String action = "action_example"; // String | Identifier of an *Action* inside a *Functionality*.
    String functionalities = "functionalities_example"; // String | Functionality selector: Functionality tags or functionality class (optionally, '@' followed by a endpoint in decimal) or '*' for all. Multiple values are separated by '|' and are interpreted as « OR ». 
    List<Object> arguments = null; // List<Object> | 
    try {
      List<ActionResult> result = apiInstance.deviceRun(deviceId, action, functionalities, arguments);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#deviceRun");
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
| **deviceId** | **String**| Unique identifier of a *Device*. | |
| **action** | **String**| Identifier of an *Action* inside a *Functionality*. | |
| **functionalities** | **String**| Functionality selector: Functionality tags or functionality class (optionally, &#39;@&#39; followed by a endpoint in decimal) or &#39;*&#39; for all. Multiple values are separated by &#39;|&#39; and are interpreted as « OR ».  | |
| **arguments** | [**List&lt;Object&gt;**](Object.md)|  | |

### Return type

[**List&lt;ActionResult&gt;**](ActionResult.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **450** | The gateway of the Place is not reachable. |  -  |
| **0** | Other error. |  -  |

<a id="functionalityRun"></a>
# **functionalityRun**
> ActionResult functionalityRun(functionalityId, action, arguments)

Run an action

Run an action on the Functionality. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String functionalityId = "functionalityId_example"; // String | Unique identifier of a *Functionality*.
    String action = "action_example"; // String | Identifier of an *Action* inside a *Functionality*.
    List<Object> arguments = null; // List<Object> | 
    try {
      ActionResult result = apiInstance.functionalityRun(functionalityId, action, arguments);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#functionalityRun");
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
| **functionalityId** | **String**| Unique identifier of a *Functionality*. | |
| **action** | **String**| Identifier of an *Action* inside a *Functionality*. | |
| **arguments** | [**List&lt;Object&gt;**](Object.md)|  | |

### Return type

[**ActionResult**](ActionResult.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **450** | The gateway of the Place is not reachable. |  -  |
| **0** | Other error. |  -  |

<a id="placeRun"></a>
# **placeRun**
> List&lt;ActionResult&gt; placeRun(placeId, action, devices, functionalities, arguments)

Run actions

Run an *Action* on zero, one or multiple *Functionalities* selected with tags.  *Device* and *Functionality* selection are combined with « AND ».  If no functionality is matched by the device/functionality selection, an empty array is returned. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    ActionApi apiInstance = new ActionApi(defaultClient);
    String placeId = "placeId_example"; // String | Unique identifier of a *Place*.
    String action = "action_example"; // String | Identifier of an *Action* inside a *Functionality*.
    String devices = "devices_example"; // String | Devices selector. Device tags or device classes or device ids or '*' for any. Multiple values are separated by '|' and interpreted as « OR ».
    String functionalities = "functionalities_example"; // String | Functionality selector: Functionality tags or functionality class (optionally, '@' followed by a endpoint in decimal) or '*' for all. Multiple values are separated by '|' and are interpreted as « OR ». 
    List<Object> arguments = null; // List<Object> | 
    try {
      List<ActionResult> result = apiInstance.placeRun(placeId, action, devices, functionalities, arguments);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionApi#placeRun");
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
| **placeId** | **String**| Unique identifier of a *Place*. | |
| **action** | **String**| Identifier of an *Action* inside a *Functionality*. | |
| **devices** | **String**| Devices selector. Device tags or device classes or device ids or &#39;*&#39; for any. Multiple values are separated by &#39;|&#39; and interpreted as « OR ». | |
| **functionalities** | **String**| Functionality selector: Functionality tags or functionality class (optionally, &#39;@&#39; followed by a endpoint in decimal) or &#39;*&#39; for all. Multiple values are separated by &#39;|&#39; and are interpreted as « OR ».  | |
| **arguments** | [**List&lt;Object&gt;**](Object.md)|  | |

### Return type

[**List&lt;ActionResult&gt;**](ActionResult.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **450** | The gateway of the Place is not reachable. |  -  |
| **0** | Other error. |  -  |

