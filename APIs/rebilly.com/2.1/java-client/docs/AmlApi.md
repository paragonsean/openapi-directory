# AmlApi

All URIs are relative to *https://api-sandbox.rebilly.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAmlEntry**](AmlApi.md#getAmlEntry) | **GET** /aml | Search PEP/Sanctions/Adverse Media lists |


<a id="getAmlEntry"></a>
# **getAmlEntry**
> List&lt;AML&gt; getAmlEntry(firstName, lastName, organizationId, dob, country)

Search PEP/Sanctions/Adverse Media lists

Search multiple PEP/Sanctions/Adverse Media lists with first and last name to find any blocklisted identities. Performs a fuzzy search including soundex. Not all fields are guaranteed to be filled. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AmlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    AmlApi apiInstance = new AmlApi(defaultClient);
    String firstName = "firstName_example"; // String | First name of individual to search.
    String lastName = "lastName_example"; // String | Last name of individual to search.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    String dob = "dob_example"; // String | Date of birth in format YYYY-MM-DD.
    String country = "country_example"; // String | Country of individual as an ISO Alpha-2 code.
    try {
      List<AML> result = apiInstance.getAmlEntry(firstName, lastName, organizationId, dob, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AmlApi#getAmlEntry");
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
| **firstName** | **String**| First name of individual to search. | |
| **lastName** | **String**| Last name of individual to search. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |
| **dob** | **String**| Date of birth in format YYYY-MM-DD. | [optional] |
| **country** | **String**| Country of individual as an ISO Alpha-2 code. | [optional] |

### Return type

[**List&lt;AML&gt;**](AML.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of objects representing hits, or an empty array if none are found. |  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |

