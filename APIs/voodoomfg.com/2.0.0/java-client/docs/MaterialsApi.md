# MaterialsApi

All URIs are relative to */api/2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**materialsGet**](MaterialsApi.md#materialsGet) | **GET** /materials | Voodoo Manufacturing offers printing in a number of different materials, with different color options for each. Your organization can expose as many or as few material options as you want to your end-customer.  |


<a id="materialsGet"></a>
# **materialsGet**
> List&lt;Material&gt; materialsGet()

Voodoo Manufacturing offers printing in a number of different materials, with different color options for each. Your organization can expose as many or as few material options as you want to your end-customer. 

The Materials endpoint returns a list of materials that are currently available for production for your account. The responses include display details about each material, along with the unique id required to request a print in a specific material. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MaterialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/2");
    
    // Configure API key authorization: Voodoo Manufacturing API Key
    ApiKeyAuth Voodoo Manufacturing API Key = (ApiKeyAuth) defaultClient.getAuthentication("Voodoo Manufacturing API Key");
    Voodoo Manufacturing API Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Voodoo Manufacturing API Key.setApiKeyPrefix("Token");

    MaterialsApi apiInstance = new MaterialsApi(defaultClient);
    try {
      List<Material> result = apiInstance.materialsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MaterialsApi#materialsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Material&gt;**](Material.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of materials |  -  |

