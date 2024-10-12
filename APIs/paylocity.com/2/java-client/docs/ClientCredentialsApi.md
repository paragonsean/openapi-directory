# ClientCredentialsApi

All URIs are relative to *https://api.paylocity.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addClientSecret**](ClientCredentialsApi.md#addClientSecret) | **POST** /v2/credentials/secrets | Obtain new client secret. |


<a id="addClientSecret"></a>
# **addClientSecret**
> List&lt;ClientCredentialsResponse&gt; addClientSecret(addClientSecret)

Obtain new client secret.

Obtain new client secret for Paylocity-issued client id. See Setup section for details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientCredentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    ClientCredentialsApi apiInstance = new ClientCredentialsApi(defaultClient);
    AddClientSecret addClientSecret = new AddClientSecret(); // AddClientSecret | Add Client Secret Model
    try {
      List<ClientCredentialsResponse> result = apiInstance.addClientSecret(addClientSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientCredentialsApi#addClientSecret");
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
| **addClientSecret** | [**AddClientSecret**](AddClientSecret.md)| Add Client Secret Model | |

### Return type

[**List&lt;ClientCredentialsResponse&gt;**](ClientCredentialsResponse.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully added |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

