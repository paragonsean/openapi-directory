# GlobalWineScoreApi

All URIs are relative to *https://api.globalwinescore.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**globalwinescoresLatestGet**](GlobalWineScoreApi.md#globalwinescoresLatestGet) | **GET** /globalwinescores/latest/ | List all latest GWS |
| [**listHistoricalGWS**](GlobalWineScoreApi.md#listHistoricalGWS) | **GET** /globalwinescores/ | List all historical GWS |


<a id="globalwinescoresLatestGet"></a>
# **globalwinescoresLatestGet**
> globalwinescoresLatestGet(authorization, wineId, vintage, color, isPrimeurs, lwin, lwin11, limit, offset, ordering)

List all latest GWS

Returns the latest GWS available per wine/vintage.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalWineScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.globalwinescore.com");
    
    // Configure API key authorization: TokenAuthentication
    ApiKeyAuth TokenAuthentication = (ApiKeyAuth) defaultClient.getAuthentication("TokenAuthentication");
    TokenAuthentication.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenAuthentication.setApiKeyPrefix("Token");

    GlobalWineScoreApi apiInstance = new GlobalWineScoreApi(defaultClient);
    String authorization = "Token <YOUR-API-TOKEN>"; // String | 
    List<Integer> wineId = Arrays.asList(); // List<Integer> | The exact `id` of the wine. Can be used multiple times (e.g `?wine_id=114959&wine_id=114952`) <br/> If you need to find the `wine_id` for your wines, use our <a href=\"https://api.globalwinescore.com/search/\" target=\"_blank\">search page</a> 
    String vintage = "2000"; // String | The vintage you want to search against.
    String color = "red"; // String | The lowercase color of the wine.
    Boolean isPrimeurs = false; // Boolean | Only show the <a href=\"See https://en.wikipedia.org/wiki/En_primeur\">en primeur</a> GlobalWineScores 
    String lwin = "1014033"; // String | L-WIN wine identifier (See definition <a href=\"https://www.liv-ex.com/lwin/\" target=\"_blank\">here</a>) 
    String lwin11 = "10140332000"; // String | L-WIN wine/vintage identifier (See definition <a href=\"https://www.liv-ex.com/lwin/\" target=\"_blank\">here</a>) 
    Integer limit = 100; // Integer | Number of results to return per page.
    Integer offset = 100; // Integer | The initial index from which to return the results.
    String ordering = "date"; // String | Which field to use when ordering the results.
    try {
      apiInstance.globalwinescoresLatestGet(authorization, wineId, vintage, color, isPrimeurs, lwin, lwin11, limit, offset, ordering);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalWineScoreApi#globalwinescoresLatestGet");
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
| **authorization** | **String**|  | [optional] |
| **wineId** | [**List&lt;Integer&gt;**](Integer.md)| The exact &#x60;id&#x60; of the wine. Can be used multiple times (e.g &#x60;?wine_id&#x3D;114959&amp;wine_id&#x3D;114952&#x60;) &lt;br/&gt; If you need to find the &#x60;wine_id&#x60; for your wines, use our &lt;a href&#x3D;\&quot;https://api.globalwinescore.com/search/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;search page&lt;/a&gt;  | [optional] |
| **vintage** | **String**| The vintage you want to search against. | [optional] |
| **color** | **String**| The lowercase color of the wine. | [optional] [enum: red, white, pink] |
| **isPrimeurs** | **Boolean**| Only show the &lt;a href&#x3D;\&quot;See https://en.wikipedia.org/wiki/En_primeur\&quot;&gt;en primeur&lt;/a&gt; GlobalWineScores  | [optional] [default to false] |
| **lwin** | **String**| L-WIN wine identifier (See definition &lt;a href&#x3D;\&quot;https://www.liv-ex.com/lwin/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;)  | [optional] |
| **lwin11** | **String**| L-WIN wine/vintage identifier (See definition &lt;a href&#x3D;\&quot;https://www.liv-ex.com/lwin/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;)  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] [default to 100] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |
| **ordering** | **String**| Which field to use when ordering the results. | [optional] [default to -date] [enum: date, -date, score, -score] |

### Return type

null (empty response body)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="listHistoricalGWS"></a>
# **listHistoricalGWS**
> listHistoricalGWS(authorization, wineId, vintage, color, isPrimeurs, lwin, lwin11, limit, offset, ordering)

List all historical GWS

Returns all available GWS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalWineScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.globalwinescore.com");
    
    // Configure API key authorization: TokenAuthentication
    ApiKeyAuth TokenAuthentication = (ApiKeyAuth) defaultClient.getAuthentication("TokenAuthentication");
    TokenAuthentication.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenAuthentication.setApiKeyPrefix("Token");

    GlobalWineScoreApi apiInstance = new GlobalWineScoreApi(defaultClient);
    String authorization = "Token <YOUR-API-TOKEN>"; // String | 
    List<Integer> wineId = Arrays.asList(); // List<Integer> | The exact `id` of the wine. Can be used multiple times (e.g `?wine_id=114959&wine_id=114952`) <br/> If you need to find the `wine_id` for your wines, use our <a href=\"https://api.globalwinescore.com/search/\" target=\"_blank\">search page</a> 
    String vintage = "2000"; // String | The vintage you want to search against.
    String color = "red"; // String | The lowercase color of the wine.
    Boolean isPrimeurs = false; // Boolean | Only show the <a href=\"See https://en.wikipedia.org/wiki/En_primeur\">en primeur</a> GlobalWineScores 
    String lwin = "1014033"; // String | L-WIN wine identifier (See definition <a href=\"https://www.liv-ex.com/lwin/\" target=\"_blank\">here</a>) 
    String lwin11 = "10140332000"; // String | L-WIN wine/vintage identifier (See definition <a href=\"https://www.liv-ex.com/lwin/\" target=\"_blank\">here</a>) 
    Integer limit = 100; // Integer | Number of results to return per page.
    Integer offset = 100; // Integer | The initial index from which to return the results.
    String ordering = "date"; // String | Which field to use when ordering the results.
    try {
      apiInstance.listHistoricalGWS(authorization, wineId, vintage, color, isPrimeurs, lwin, lwin11, limit, offset, ordering);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalWineScoreApi#listHistoricalGWS");
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
| **authorization** | **String**|  | [optional] |
| **wineId** | [**List&lt;Integer&gt;**](Integer.md)| The exact &#x60;id&#x60; of the wine. Can be used multiple times (e.g &#x60;?wine_id&#x3D;114959&amp;wine_id&#x3D;114952&#x60;) &lt;br/&gt; If you need to find the &#x60;wine_id&#x60; for your wines, use our &lt;a href&#x3D;\&quot;https://api.globalwinescore.com/search/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;search page&lt;/a&gt;  | [optional] |
| **vintage** | **String**| The vintage you want to search against. | [optional] |
| **color** | **String**| The lowercase color of the wine. | [optional] [enum: red, white, pink] |
| **isPrimeurs** | **Boolean**| Only show the &lt;a href&#x3D;\&quot;See https://en.wikipedia.org/wiki/En_primeur\&quot;&gt;en primeur&lt;/a&gt; GlobalWineScores  | [optional] [default to false] |
| **lwin** | **String**| L-WIN wine identifier (See definition &lt;a href&#x3D;\&quot;https://www.liv-ex.com/lwin/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;)  | [optional] |
| **lwin11** | **String**| L-WIN wine/vintage identifier (See definition &lt;a href&#x3D;\&quot;https://www.liv-ex.com/lwin/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;)  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] [default to 100] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |
| **ordering** | **String**| Which field to use when ordering the results. | [optional] [default to -date] [enum: date, -date, score, -score] |

### Return type

null (empty response body)

### Authorization

[TokenAuthentication](../README.md#TokenAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

