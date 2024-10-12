# PayorHierarchyApi

All URIs are relative to *https://api.sandbox.velopayments.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**payorLinksV1**](PayorHierarchyApi.md#payorLinksV1) | **GET** /v1/payorLinks | List Payor Links |


<a id="payorLinksV1"></a>
# **payorLinksV1**
> PayorLinksResponse payorLinksV1(descendantsOfPayor, parentOfPayor, fields)

List Payor Links

&lt;p&gt;If the payor is set up as part of a hierarchy you can use this API to traverse the hierarchy&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayorHierarchyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PayorHierarchyApi apiInstance = new PayorHierarchyApi(defaultClient);
    UUID descendantsOfPayor = UUID.randomUUID(); // UUID | The Payor ID from which to start the query to show all descendants
    UUID parentOfPayor = UUID.randomUUID(); // UUID | Query for the parent payor details for this payor id
    String fields = "fields_example"; // String | <p>List of additional Payor fields to include in the response for each Payor</p> <p>The values of payorId and payorName are always included for each Payor by default</p> <p>You can add fields to the response for each payor by including them in the fields parameter separated by commas</p> <p>The supported fields are any combination of: primaryContactEmail,kycState</p> 
    try {
      PayorLinksResponse result = apiInstance.payorLinksV1(descendantsOfPayor, parentOfPayor, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayorHierarchyApi#payorLinksV1");
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
| **descendantsOfPayor** | **UUID**| The Payor ID from which to start the query to show all descendants | [optional] |
| **parentOfPayor** | **UUID**| Query for the parent payor details for this payor id | [optional] |
| **fields** | **String**| &lt;p&gt;List of additional Payor fields to include in the response for each Payor&lt;/p&gt; &lt;p&gt;The values of payorId and payorName are always included for each Payor by default&lt;/p&gt; &lt;p&gt;You can add fields to the response for each payor by including them in the fields parameter separated by commas&lt;/p&gt; &lt;p&gt;The supported fields are any combination of: primaryContactEmail,kycState&lt;/p&gt;  | [optional] |

### Return type

[**PayorLinksResponse**](PayorLinksResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of Payor Links |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

