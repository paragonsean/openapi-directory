# CommandsApi

All URIs are relative to *http://api.edrv.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelreservation**](CommandsApi.md#cancelreservation) | **POST** /v1/commands/cancelreservation |  |
| [**getCommands**](CommandsApi.md#getCommands) | **GET** /v1/commands |  |
| [**getVariables**](CommandsApi.md#getVariables) | **GET** /v1/commands/{id}/variables |  |
| [**patchChargeStationVariable**](CommandsApi.md#patchChargeStationVariable) | **PATCH** /v1/commands/{id}/variables |  |
| [**remotestart**](CommandsApi.md#remotestart) | **POST** /v1/commands/remotestart |  |
| [**remotestop**](CommandsApi.md#remotestop) | **POST** /v1/commands/remotestop |  |
| [**reserve**](CommandsApi.md#reserve) | **POST** /v1/commands/reserve |  |
| [**reset**](CommandsApi.md#reset) | **POST** /v1/commands/reset |  |
| [**unlockconnector**](CommandsApi.md#unlockconnector) | **POST** /v1/commands/unlockconnector |  |


<a id="cancelreservation"></a>
# **cancelreservation**
> PatchChargeStation200Response cancelreservation(cancelreservationRequest)



Use to request a delete an existing reservation. The request will wait for the charge station to process the command. It will timeout after 60 seconds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommandsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CommandsApi apiInstance = new CommandsApi(defaultClient);
    CancelreservationRequest cancelreservationRequest = new CancelreservationRequest(); // CancelreservationRequest | 
    try {
      PatchChargeStation200Response result = apiInstance.cancelreservation(cancelreservationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommandsApi#cancelreservation");
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
| **cancelreservationRequest** | [**CancelreservationRequest**](CancelreservationRequest.md)|  | |

### Return type

[**PatchChargeStation200Response**](PatchChargeStation200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A successful response |  -  |
| **400** | A failure response |  -  |

<a id="getCommands"></a>
# **getCommands**
> getCommands(paginateLimit, paginatePage, paginateEnabled, sortBy, sortOrder, createdAt$gte, createdAt$lte, updatedAt$gte, updatedAt$lte, includeChargestation, includeDriver, includeTransaction, includeOrganization)



Get Commands data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommandsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CommandsApi apiInstance = new CommandsApi(defaultClient);
    Integer paginateLimit = 20; // Integer | Number of results per page
    String paginatePage = "paginatePage_example"; // String | The queried page index
    Boolean paginateEnabled = true; // Boolean | Enable pagination
    String sortBy = "createdAt"; // String | Sort data by this key
    String sortOrder = "desc"; // String | asc to sort ascending (default is desc - descending)
    OffsetDateTime createdAt$gte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime createdAt$lte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime updatedAt$gte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    OffsetDateTime updatedAt$lte = OffsetDateTime.now(); // OffsetDateTime | Date as ISO String
    Boolean includeChargestation = true; // Boolean | Populate chargestation
    Boolean includeDriver = true; // Boolean | Populate driver
    Boolean includeTransaction = true; // Boolean | Populate transaction
    Boolean includeOrganization = true; // Boolean | Populate organization
    try {
      apiInstance.getCommands(paginateLimit, paginatePage, paginateEnabled, sortBy, sortOrder, createdAt$gte, createdAt$lte, updatedAt$gte, updatedAt$lte, includeChargestation, includeDriver, includeTransaction, includeOrganization);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommandsApi#getCommands");
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
| **paginateLimit** | **Integer**| Number of results per page | [optional] [default to 20] |
| **paginatePage** | **String**| The queried page index | [optional] |
| **paginateEnabled** | **Boolean**| Enable pagination | [optional] [default to true] |
| **sortBy** | **String**| Sort data by this key | [optional] [default to createdAt] |
| **sortOrder** | **String**| asc to sort ascending (default is desc - descending) | [optional] [default to desc] [enum: desc, asc] |
| **createdAt$gte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **createdAt$lte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **updatedAt$gte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **updatedAt$lte** | **OffsetDateTime**| Date as ISO String | [optional] |
| **includeChargestation** | **Boolean**| Populate chargestation | [optional] |
| **includeDriver** | **Boolean**| Populate driver | [optional] |
| **includeTransaction** | **Boolean**| Populate transaction | [optional] |
| **includeOrganization** | **Boolean**| Populate organization | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getVariables"></a>
# **getVariables**
> getVariables(id)



Get a charge station&#39;s config variables

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommandsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CommandsApi apiInstance = new CommandsApi(defaultClient);
    String id = "id_example"; // String | The chargestation id
    try {
      apiInstance.getVariables(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommandsApi#getVariables");
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
| **id** | **String**| The chargestation id | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns Cs configurations array |  -  |

<a id="patchChargeStationVariable"></a>
# **patchChargeStationVariable**
> PatchChargeStation200Response patchChargeStationVariable(id, patchChargeStationVariableRequest)



Update config variables for a chargestation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommandsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CommandsApi apiInstance = new CommandsApi(defaultClient);
    String id = "id_example"; // String | ID of charge station
    PatchChargeStationVariableRequest patchChargeStationVariableRequest = new PatchChargeStationVariableRequest(); // PatchChargeStationVariableRequest | Charge Station Variable to set
    try {
      PatchChargeStation200Response result = apiInstance.patchChargeStationVariable(id, patchChargeStationVariableRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommandsApi#patchChargeStationVariable");
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
| **id** | **String**| ID of charge station | |
| **patchChargeStationVariableRequest** | [**PatchChargeStationVariableRequest**](PatchChargeStationVariableRequest.md)| Charge Station Variable to set | |

### Return type

[**PatchChargeStation200Response**](PatchChargeStation200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A successful response |  -  |
| **400** | A failure response |  -  |

<a id="remotestart"></a>
# **remotestart**
> Setchargingschedule201Response remotestart(remotestartRequest)



Use to request a remote start command. The request will wait for the charge station to process the command. It will timeout after 60 seconds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommandsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CommandsApi apiInstance = new CommandsApi(defaultClient);
    RemotestartRequest remotestartRequest = new RemotestartRequest(); // RemotestartRequest | 
    try {
      Setchargingschedule201Response result = apiInstance.remotestart(remotestartRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommandsApi#remotestart");
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
| **remotestartRequest** | [**RemotestartRequest**](RemotestartRequest.md)|  | |

### Return type

[**Setchargingschedule201Response**](Setchargingschedule201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A successful response |  -  |
| **400** | A failure response |  -  |

<a id="remotestop"></a>
# **remotestop**
> remotestop(remotestopRequest)



Use to request a remote stop command. The request will wait for the charge station to process the command. It will timeout after 60 seconds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommandsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CommandsApi apiInstance = new CommandsApi(defaultClient);
    RemotestopRequest remotestopRequest = new RemotestopRequest(); // RemotestopRequest | Remote stop transaction info here.
    try {
      apiInstance.remotestop(remotestopRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommandsApi#remotestop");
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
| **remotestopRequest** | [**RemotestopRequest**](RemotestopRequest.md)| Remote stop transaction info here. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A successful response |  -  |
| **400** | A failure response |  -  |

<a id="reserve"></a>
# **reserve**
> Setchargingschedule201Response reserve(reserveRequest)



Use to request a reserve command. The request will wait for the charge station to process the command. It will timeout after 60 seconds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommandsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CommandsApi apiInstance = new CommandsApi(defaultClient);
    ReserveRequest reserveRequest = new ReserveRequest(); // ReserveRequest | 
    try {
      Setchargingschedule201Response result = apiInstance.reserve(reserveRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommandsApi#reserve");
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
| **reserveRequest** | [**ReserveRequest**](ReserveRequest.md)|  | |

### Return type

[**Setchargingschedule201Response**](Setchargingschedule201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A successful response |  -  |
| **400** | A failure response |  -  |

<a id="reset"></a>
# **reset**
> PatchChargeStation200Response reset(resetRequest)



Use to request a reset command. The request will wait for the charge station to process the command. It will timeout after 60 seconds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommandsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CommandsApi apiInstance = new CommandsApi(defaultClient);
    ResetRequest resetRequest = new ResetRequest(); // ResetRequest | 
    try {
      PatchChargeStation200Response result = apiInstance.reset(resetRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommandsApi#reset");
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
| **resetRequest** | [**ResetRequest**](ResetRequest.md)|  | |

### Return type

[**PatchChargeStation200Response**](PatchChargeStation200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A successful response |  -  |
| **400** | A failure response |  -  |

<a id="unlockconnector"></a>
# **unlockconnector**
> Setchargingschedule201Response unlockconnector(unlockconnectorRequest)



Use to request an unlock command for a connector. The request will wait for the charge station to process the command. It will timeout after 60 seconds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommandsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CommandsApi apiInstance = new CommandsApi(defaultClient);
    UnlockconnectorRequest unlockconnectorRequest = new UnlockconnectorRequest(); // UnlockconnectorRequest | 
    try {
      Setchargingschedule201Response result = apiInstance.unlockconnector(unlockconnectorRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommandsApi#unlockconnector");
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
| **unlockconnectorRequest** | [**UnlockconnectorRequest**](UnlockconnectorRequest.md)|  | |

### Return type

[**Setchargingschedule201Response**](Setchargingschedule201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A successful response |  -  |
| **400** | A failure response |  -  |

