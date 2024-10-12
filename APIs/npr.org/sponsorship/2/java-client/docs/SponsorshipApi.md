# SponsorshipApi

All URIs are relative to *https://sponsorship.api.npr.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAds**](SponsorshipApi.md#getAds) | **GET** /v2/ads | Request VAST sponsorship units |
| [**receiveAdTracking**](SponsorshipApi.md#receiveAdTracking) | **POST** /v2/ads | Record tracking data for VAST sponsorship units |


<a id="getAds"></a>
# **getAds**
> VASTXml getAds(authorization, xAdvertisingID, forceResult, adCount)

Request VAST sponsorship units

**Not** for use by NPR One clients (for whom sponsorship is already integrated into the Listening Service), this endpoint is designed to be used by our other client applications to request sponsorship on behalf of a user. Sponsorship units are returned in the form of VAST XML. It is worth noting that this endpoint attempts to always return XML, even in the case of exceptions.  The default behavior of this endpoint is asynchronous; on an initial request, a call to our external sponsorship provider is placed on a queue, which is typically processed within 3 minutes. Once the sponsorship call is received and processed, the returned sponsorship units are placed in a cache on our server for the current user. Subsequent calls to this endpoint will return VAST sponsorship units from this cache until tracking information is submitted, which removes the ad from the cache and will automatically request additional ads asynchronously if there are fewer than a certain number remaining in the cache.  For development purposes, it&#39;s worth noting that there is currently no way to clear a user&#39;s cache without submitting some form of tracking.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SponsorshipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sponsorship.api.npr.org");

    SponsorshipApi apiInstance = new SponsorshipApi(defaultClient);
    String authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
    String xAdvertisingID = "xAdvertisingID_example"; // String | A device-specific advertising identifier, if possible. Apple's IDFA is an example.
    Boolean forceResult = true; // Boolean | Whether to force a synchronous call to our external sponsorship provider; the default behavior is asynchronous.
    Integer adCount = 56; // Integer | How many sponsorship units to request in one call; if left unspecified, the default behavior is to return only 1.
    try {
      VASTXml result = apiInstance.getAds(authorization, xAdvertisingID, forceResult, adCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SponsorshipApi#getAds");
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
| **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | |
| **xAdvertisingID** | **String**| A device-specific advertising identifier, if possible. Apple&#39;s IDFA is an example. | [optional] |
| **forceResult** | **Boolean**| Whether to force a synchronous call to our external sponsorship provider; the default behavior is asynchronous. | [optional] |
| **adCount** | **Integer**| How many sponsorship units to request in one call; if left unspecified, the default behavior is to return only 1. | [optional] |

### Return type

[**VASTXml**](VASTXml.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request completed successfully; a VAST XML document is returned. Note that this response will only be returned if either &#x60;force&#x3D;true&#x60; was passed in the querystring, or a call to get sponsorship was previously made, and ads now exist in the cache for this user; otherwise, the 202 response is returned. |  -  |
| **202** | Request accepted. Check back later for actual ads. |  -  |
| **400** | A bad request; generally, one or more parameters passed in were incorrect or missing |  -  |
| **500** | A server error |  -  |

<a id="receiveAdTracking"></a>
# **receiveAdTracking**
> receiveAdTracking(authorization, body, xAdvertisingID)

Record tracking data for VAST sponsorship units

**Not** for use by NPR One clients (for whom sponsorship is already integrated into the Listening Service), this endpoint is designed to be used by our other client applications to submit tracking information for sponsorship units obtained from the &#x60;GET /sponsorship/v2/ads&#x60; endpoint.  The tracking information should be submitted in the body of the request in the form of a JSON object following the Collection.Doc+JSON specification.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SponsorshipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sponsorship.api.npr.org");

    SponsorshipApi apiInstance = new SponsorshipApi(defaultClient);
    String authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
    UserAdDocument body = new UserAdDocument(); // UserAdDocument | A JSON object representing sponsorship tracking data to submit to our external provider.
    String xAdvertisingID = "xAdvertisingID_example"; // String | A device-specific advertising identifier, if possible. Apple's IDFA is an example.
    try {
      apiInstance.receiveAdTracking(authorization, body, xAdvertisingID);
    } catch (ApiException e) {
      System.err.println("Exception when calling SponsorshipApi#receiveAdTracking");
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
| **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | |
| **body** | [**UserAdDocument**](UserAdDocument.md)| A JSON object representing sponsorship tracking data to submit to our external provider. | |
| **xAdvertisingID** | **String**| A device-specific advertising identifier, if possible. Apple&#39;s IDFA is an example. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Request completed successfully, but there is nothing that we need to return to the caller. |  -  |
| **400** | A bad request; generally, one or more parameters passed in were incorrect or missing |  -  |
| **500** | A server error |  -  |

