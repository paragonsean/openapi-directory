# MacrosApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**run**](MacrosApi.md#run) | **POST** /macros/{macroId}/run | Executes a macro. |


<a id="run"></a>
# **run**
> ActionStartedDTO run(macroId, macroRequestDTO)

Executes a macro.

Runs a specified macro on a specified list of items (\&quot;list\&quot; variable in the macro code). The list of items can be empty if the macro doesn&#39;t use it. Additional custom parameters can be provided to the macro when necessary (\&quot;params\&quot; variable in the macro code).   &lt;BR&gt;Note: Macros that support parameters can be also run from GUI (Views in Home Portal),so they should also handle the empty parameters map (e.g. by defining default values when parameters are not provided).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MacrosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    MacrosApi apiInstance = new MacrosApi(defaultClient);
    Long macroId = 56L; // Long | macro internal identifier
    MacroRequestDTO macroRequestDTO = new MacroRequestDTO(); // MacroRequestDTO | Generated client invoices documents.
    try {
      ActionStartedDTO result = apiInstance.run(macroId, macroRequestDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MacrosApi#run");
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
| **macroId** | **Long**| macro internal identifier | |
| **macroRequestDTO** | [**MacroRequestDTO**](MacroRequestDTO.md)| Generated client invoices documents. | |

### Return type

[**ActionStartedDTO**](ActionStartedDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

