# UserInterfaceApi

All URIs are relative to *https://esi.evetech.net/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postUiAutopilotWaypoint**](UserInterfaceApi.md#postUiAutopilotWaypoint) | **POST** /ui/autopilot/waypoint/ | Set Autopilot Waypoint |
| [**postUiOpenwindowContract**](UserInterfaceApi.md#postUiOpenwindowContract) | **POST** /ui/openwindow/contract/ | Open Contract Window |
| [**postUiOpenwindowInformation**](UserInterfaceApi.md#postUiOpenwindowInformation) | **POST** /ui/openwindow/information/ | Open Information Window |
| [**postUiOpenwindowMarketdetails**](UserInterfaceApi.md#postUiOpenwindowMarketdetails) | **POST** /ui/openwindow/marketdetails/ | Open Market Details |
| [**postUiOpenwindowNewmail**](UserInterfaceApi.md#postUiOpenwindowNewmail) | **POST** /ui/openwindow/newmail/ | Open New Mail Window |


<a id="postUiAutopilotWaypoint"></a>
# **postUiAutopilotWaypoint**
> postUiAutopilotWaypoint(addToBeginning, clearOtherWaypoints, destinationId, datasource, token)

Set Autopilot Waypoint

Set a solar system as autopilot waypoint  --- Alternate route: &#x60;/dev/ui/autopilot/waypoint/&#x60;  Alternate route: &#x60;/v2/ui/autopilot/waypoint/&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserInterfaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    UserInterfaceApi apiInstance = new UserInterfaceApi(defaultClient);
    Boolean addToBeginning = false; // Boolean | Whether this solar system should be added to the beginning of all waypoints
    Boolean clearOtherWaypoints = false; // Boolean | Whether clean other waypoints beforing adding this one
    Long destinationId = 56L; // Long | The destination to travel to, can be solar system, station or structure's id
    String datasource = "tranquility"; // String | The server name you would like data from
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      apiInstance.postUiAutopilotWaypoint(addToBeginning, clearOtherWaypoints, destinationId, datasource, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserInterfaceApi#postUiAutopilotWaypoint");
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
| **addToBeginning** | **Boolean**| Whether this solar system should be added to the beginning of all waypoints | [default to false] |
| **clearOtherWaypoints** | **Boolean**| Whether clean other waypoints beforing adding this one | [default to false] |
| **destinationId** | **Long**| The destination to travel to, can be solar system, station or structure&#39;s id | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Open window request received |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="postUiOpenwindowContract"></a>
# **postUiOpenwindowContract**
> postUiOpenwindowContract(contractId, datasource, token)

Open Contract Window

Open the contract window inside the client  --- Alternate route: &#x60;/dev/ui/openwindow/contract/&#x60;  Alternate route: &#x60;/legacy/ui/openwindow/contract/&#x60;  Alternate route: &#x60;/v1/ui/openwindow/contract/&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserInterfaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    UserInterfaceApi apiInstance = new UserInterfaceApi(defaultClient);
    Integer contractId = 56; // Integer | The contract to open
    String datasource = "tranquility"; // String | The server name you would like data from
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      apiInstance.postUiOpenwindowContract(contractId, datasource, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserInterfaceApi#postUiOpenwindowContract");
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
| **contractId** | **Integer**| The contract to open | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Open window request received |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="postUiOpenwindowInformation"></a>
# **postUiOpenwindowInformation**
> postUiOpenwindowInformation(targetId, datasource, token)

Open Information Window

Open the information window for a character, corporation or alliance inside the client  --- Alternate route: &#x60;/dev/ui/openwindow/information/&#x60;  Alternate route: &#x60;/legacy/ui/openwindow/information/&#x60;  Alternate route: &#x60;/v1/ui/openwindow/information/&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserInterfaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    UserInterfaceApi apiInstance = new UserInterfaceApi(defaultClient);
    Integer targetId = 56; // Integer | The target to open
    String datasource = "tranquility"; // String | The server name you would like data from
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      apiInstance.postUiOpenwindowInformation(targetId, datasource, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserInterfaceApi#postUiOpenwindowInformation");
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
| **targetId** | **Integer**| The target to open | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Open window request received |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="postUiOpenwindowMarketdetails"></a>
# **postUiOpenwindowMarketdetails**
> postUiOpenwindowMarketdetails(typeId, datasource, token)

Open Market Details

Open the market details window for a specific typeID inside the client  --- Alternate route: &#x60;/dev/ui/openwindow/marketdetails/&#x60;  Alternate route: &#x60;/legacy/ui/openwindow/marketdetails/&#x60;  Alternate route: &#x60;/v1/ui/openwindow/marketdetails/&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserInterfaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    UserInterfaceApi apiInstance = new UserInterfaceApi(defaultClient);
    Integer typeId = 56; // Integer | The item type to open in market window
    String datasource = "tranquility"; // String | The server name you would like data from
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      apiInstance.postUiOpenwindowMarketdetails(typeId, datasource, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserInterfaceApi#postUiOpenwindowMarketdetails");
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
| **typeId** | **Integer**| The item type to open in market window | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Open window request received |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="postUiOpenwindowNewmail"></a>
# **postUiOpenwindowNewmail**
> postUiOpenwindowNewmail(newMail, datasource, token)

Open New Mail Window

Open the New Mail window, according to settings from the request if applicable  --- Alternate route: &#x60;/dev/ui/openwindow/newmail/&#x60;  Alternate route: &#x60;/legacy/ui/openwindow/newmail/&#x60;  Alternate route: &#x60;/v1/ui/openwindow/newmail/&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserInterfaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");
    
    // Configure OAuth2 access token for authorization: evesso
    OAuth evesso = (OAuth) defaultClient.getAuthentication("evesso");
    evesso.setAccessToken("YOUR ACCESS TOKEN");

    UserInterfaceApi apiInstance = new UserInterfaceApi(defaultClient);
    PostUiOpenwindowNewmailNewMail newMail = new PostUiOpenwindowNewmailNewMail(); // PostUiOpenwindowNewmailNewMail | The details of mail to create
    String datasource = "tranquility"; // String | The server name you would like data from
    String token = "token_example"; // String | Access token to use if unable to set a header
    try {
      apiInstance.postUiOpenwindowNewmail(newMail, datasource, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserInterfaceApi#postUiOpenwindowNewmail");
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
| **newMail** | [**PostUiOpenwindowNewmailNewMail**](PostUiOpenwindowNewmailNewMail.md)| The details of mail to create | |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **token** | **String**| Access token to use if unable to set a header | [optional] |

### Return type

null (empty response body)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Open window request received |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **420** | Error limited |  -  |
| **422** | Invalid request |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

