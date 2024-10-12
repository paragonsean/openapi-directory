# V1Api

All URIs are relative to *http://api.ote-godaddy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addExpiryListings**](V1Api.md#addExpiryListings) | **POST** /v1/aftermarket/listings/expiry | Add expiry listings into GoDaddy Auction |
| [**deleteListings**](V1Api.md#deleteListings) | **DELETE** /v1/aftermarket/listings | Remove listings from GoDaddy Auction |


<a id="addExpiryListings"></a>
# **addExpiryListings**
> AftermarketListingAction addExpiryListings(aftermarketListingExpiryCreate)

Add expiry listings into GoDaddy Auction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    List<AftermarketListingExpiryCreate> aftermarketListingExpiryCreate = Arrays.asList(); // List<AftermarketListingExpiryCreate> | An array of expiry listings to be loaded
    try {
      AftermarketListingAction result = apiInstance.addExpiryListings(aftermarketListingExpiryCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#addExpiryListings");
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
| **aftermarketListingExpiryCreate** | [**List&lt;AftermarketListingExpiryCreate&gt;**](AftermarketListingExpiryCreate.md)| An array of expiry listings to be loaded | |

### Return type

[**AftermarketListingAction**](AftermarketListingAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml, text/xml
 - **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request was successful |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **422** | Required parameters must be specified in correct format&lt;br&gt;Too many Listings provided&lt;br&gt;Invalid Losing Registrar Id |  -  |
| **429** | Too many requests received within interval |  -  |
| **500** | Internal server error |  -  |

<a id="deleteListings"></a>
# **deleteListings**
> AftermarketListingAction deleteListings(domains)

Remove listings from GoDaddy Auction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    List<String> domains = Arrays.asList(); // List<String> | A comma separated list of domain names
    try {
      AftermarketListingAction result = apiInstance.deleteListings(domains);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#deleteListings");
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
| **domains** | [**List&lt;String&gt;**](String.md)| A comma separated list of domain names | |

### Return type

[**AftermarketListingAction**](AftermarketListingAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request was successful |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **422** |  Required parameters must be specified in correct format |  -  |
| **429** | Too many requests received within interval |  -  |
| **500** | Internal server error |  -  |

