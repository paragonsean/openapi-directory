# FactionsApi

All URIs are relative to *https://api.spacetraders.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getFaction**](FactionsApi.md#getFaction) | **GET** /factions/{factionSymbol} | Get Faction |
| [**getFactions**](FactionsApi.md#getFactions) | **GET** /factions | List Factions |


<a id="getFaction"></a>
# **getFaction**
> GetFaction200Response getFaction(factionSymbol)

Get Faction

View the details of a faction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spacetraders.io/v2");
    
    // Configure HTTP bearer authorization: AgentToken
    HttpBearerAuth AgentToken = (HttpBearerAuth) defaultClient.getAuthentication("AgentToken");
    AgentToken.setBearerToken("BEARER TOKEN");

    FactionsApi apiInstance = new FactionsApi(defaultClient);
    String factionSymbol = "CGR"; // String | The faction symbol
    try {
      GetFaction200Response result = apiInstance.getFaction(factionSymbol);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FactionsApi#getFaction");
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
| **factionSymbol** | **String**| The faction symbol | [default to CGR] |

### Return type

[**GetFaction200Response**](GetFaction200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getFactions"></a>
# **getFactions**
> GetFactions200Response getFactions(page, limit)

List Factions

List all discovered factions in the game.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spacetraders.io/v2");
    
    // Configure HTTP bearer authorization: AgentToken
    HttpBearerAuth AgentToken = (HttpBearerAuth) defaultClient.getAuthentication("AgentToken");
    AgentToken.setBearerToken("BEARER TOKEN");

    FactionsApi apiInstance = new FactionsApi(defaultClient);
    Integer page = 56; // Integer | What entry offset to request
    Integer limit = 56; // Integer | How many entries to return per page
    try {
      GetFactions200Response result = apiInstance.getFactions(page, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FactionsApi#getFactions");
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
| **page** | **Integer**| What entry offset to request | [optional] |
| **limit** | **Integer**| How many entries to return per page | [optional] |

### Return type

[**GetFactions200Response**](GetFactions200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

