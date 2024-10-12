# ElectricityApi

All URIs are relative to *https://ioe2api.ijenko.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**placeElectricityAutonomy**](ElectricityApi.md#placeElectricityAutonomy) | **GET** /places/{placeId}/electricity/autonomy | Get autonomy rate of the place |
| [**placeElectricityGetFlows**](ElectricityApi.md#placeElectricityGetFlows) | **GET** /places/{placeId}/electricity/flows | Get electricity virtual flows |
| [**placeElectricityGetFlowsSetup**](ElectricityApi.md#placeElectricityGetFlowsSetup) | **GET** /places/{placeId}/electricity/flows/setup | Get electricity flows setup |
| [**placeElectricitySelfConsumption**](ElectricityApi.md#placeElectricitySelfConsumption) | **GET** /places/{placeId}/electricity/self-consumption | Get self-consumption rate of the place |


<a id="placeElectricityAutonomy"></a>
# **placeElectricityAutonomy**
> ElectricityAutonomy placeElectricityAutonomy(placeId, when, span)

Get autonomy rate of the place

Compute the autonomy rate of the *Place* on a time period.  &#x60;autonomy &#x3D; 1 - (elec_drawn / elec_total_usage)&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ElectricityApi;

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

    ElectricityApi apiInstance = new ElectricityApi(defaultClient);
    String placeId = "placeId_example"; // String | Unique identifier of a *Place*.
    OffsetDateTime when = OffsetDateTime.now(); // OffsetDateTime | A time part of the time span.
    String span = "H"; // String | Timespan: H (hour), D (day), Wmo (week starting on Monday), Wsu (week starting on Sunday), M (month), Y (year)
    try {
      ElectricityAutonomy result = apiInstance.placeElectricityAutonomy(placeId, when, span);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ElectricityApi#placeElectricityAutonomy");
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
| **when** | **OffsetDateTime**| A time part of the time span. | |
| **span** | **String**| Timespan: H (hour), D (day), Wmo (week starting on Monday), Wsu (week starting on Sunday), M (month), Y (year) | [enum: H, D, Wmo, Wsu, M, Y] |

### Return type

[**ElectricityAutonomy**](ElectricityAutonomy.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **0** | Other error. |  -  |

<a id="placeElectricityGetFlows"></a>
# **placeElectricityGetFlows**
> ElectricityFlows placeElectricityGetFlows(placeId, flows)

Get electricity virtual flows

Get the mapping of virtual electricity flows to functionalities.  Some rules are applied to expand the virtual flows using the concrete flows available.  The &#x60;factor&#x60; tells how each energy value coming from a functionality must be added with values from other functionality to compute the energy of the virtual flow. Factors are usually &#x60;1&#x60; or &#x60;-1&#x60;.  The &#x60;code&#x60; property gives the result which may be partial: - If all flows are available, &#x60;200000&#x60; is returned. - If no flows are available (indicating that the place has no   electricity functionality or that no functionality has been attached   to a flow), the &#x60;code&#x60; is &#x60;200001&#x60;. The &#x60;missing&#x60; property contains   all the requested flows. - If some flows are missing, the &#x60;code&#x60; is &#x60;200002&#x60; and the &#x60;missing&#x60;   property lists them. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ElectricityApi;

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

    ElectricityApi apiInstance = new ElectricityApi(defaultClient);
    String placeId = "placeId_example"; // String | Unique identifier of a *Place*.
    List<String> flows = Arrays.asList(); // List<String> | Names of the flows requested
    try {
      ElectricityFlows result = apiInstance.placeElectricityGetFlows(placeId, flows);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ElectricityApi#placeElectricityGetFlows");
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
| **flows** | [**List&lt;String&gt;**](String.md)| Names of the flows requested | [enum: battery_charge, battery_discharge, battery_grid, elec_total_gen, elec_total_usage, elec_feed_in, elec_drawn, elec_local, elec_from_household, elec_to_pv, elec_usage] |

### Return type

[**ElectricityFlows**](ElectricityFlows.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Place is available. &#x60;code&#x60; gives the functional result. |  -  |
| **0** | Other error. |  -  |

<a id="placeElectricityGetFlowsSetup"></a>
# **placeElectricityGetFlowsSetup**
> ElectricityFlowsSetup placeElectricityGetFlowsSetup(placeId)

Get electricity flows setup

Get the mapping of functionalities to electricity flows.  A functionality is attached to *at most* one flow. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ElectricityApi;

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

    ElectricityApi apiInstance = new ElectricityApi(defaultClient);
    String placeId = "placeId_example"; // String | Unique identifier of a *Place*.
    try {
      ElectricityFlowsSetup result = apiInstance.placeElectricityGetFlowsSetup(placeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ElectricityApi#placeElectricityGetFlowsSetup");
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

### Return type

[**ElectricityFlowsSetup**](ElectricityFlowsSetup.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **0** | Other error. |  -  |

<a id="placeElectricitySelfConsumption"></a>
# **placeElectricitySelfConsumption**
> ElectricitySelfConsumption placeElectricitySelfConsumption(placeId, when, span)

Get self-consumption rate of the place

Compute the self-consumption rate of the *Place* on a time period.  &#x60;selfConsumption &#x3D; 1 - (elec_feed_in / elec_total_usage)&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ElectricityApi;

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

    ElectricityApi apiInstance = new ElectricityApi(defaultClient);
    String placeId = "placeId_example"; // String | Unique identifier of a *Place*.
    OffsetDateTime when = OffsetDateTime.now(); // OffsetDateTime | A time part of the time span.
    String span = "H"; // String | Timespan: H (hour), D (day), Wmo (week starting on Monday), Wsu (week starting on Sunday), M (month), Y (year)
    try {
      ElectricitySelfConsumption result = apiInstance.placeElectricitySelfConsumption(placeId, when, span);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ElectricityApi#placeElectricitySelfConsumption");
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
| **when** | **OffsetDateTime**| A time part of the time span. | |
| **span** | **String**| Timespan: H (hour), D (day), Wmo (week starting on Monday), Wsu (week starting on Sunday), M (month), Y (year) | [enum: H, D, Wmo, Wsu, M, Y] |

### Return type

[**ElectricitySelfConsumption**](ElectricitySelfConsumption.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **0** | Other error. |  -  |

