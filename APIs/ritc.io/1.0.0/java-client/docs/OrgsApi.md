# OrgsApi

All URIs are relative to *https://api.ritc.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addOrganization**](OrgsApi.md#addOrganization) | **POST** /orgs |  |
| [**getMyOrganization**](OrgsApi.md#getMyOrganization) | **GET** /orgs/me |  |


<a id="addOrganization"></a>
# **addOrganization**
> List&lt;OrgResponse&gt; addOrganization(orgObject)



Create an org

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrgsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OrgsApi apiInstance = new OrgsApi(defaultClient);
    Org orgObject = new Org(); // Org | Org information
    try {
      List<OrgResponse> result = apiInstance.addOrganization(orgObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrgsApi#addOrganization");
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
| **orgObject** | [**Org**](Org.md)| Org information | |

### Return type

[**List&lt;OrgResponse&gt;**](OrgResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An org was successfully created |  -  |
| **400** | Invalid input |  -  |
| **0** | Unexpected error |  -  |

<a id="getMyOrganization"></a>
# **getMyOrganization**
> List&lt;OrgResponse&gt; getMyOrganization()



Get org information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrgsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OrgsApi apiInstance = new OrgsApi(defaultClient);
    try {
      List<OrgResponse> result = apiInstance.getMyOrganization();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrgsApi#getMyOrganization");
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

[**List&lt;OrgResponse&gt;**](OrgResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Detailed information about an org |  -  |
| **400** | Invalid input |  -  |
| **0** | Unexpected error |  -  |

