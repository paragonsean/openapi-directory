# ShipmentApi

All URIs are relative to *https://api.ebay.com/sell/logistics/v1_beta*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelShipment**](ShipmentApi.md#cancelShipment) | **POST** /shipment/{shipmentId}/cancel |  |
| [**createFromShippingQuote**](ShipmentApi.md#createFromShippingQuote) | **POST** /shipment/create_from_shipping_quote |  |
| [**downloadLabelFile**](ShipmentApi.md#downloadLabelFile) | **GET** /shipment/{shipmentId}/download_label_file |  |
| [**getShipment**](ShipmentApi.md#getShipment) | **GET** /shipment/{shipmentId} |  |


<a id="cancelShipment"></a>
# **cancelShipment**
> Shipment cancelShipment(shipmentId)



This method cancels the shipment associated with the specified shipment ID and the associated shipping label is deleted. When you cancel a shipment, the &lt;b&gt;totalShippingCost&lt;/b&gt; of the canceled shipment is refunded to the account established by the user&#39;s billing agreement.  &lt;br&gt;&lt;br&gt;Note that you cannot cancel a shipment if you have used the associated shipping label.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/sell/logistics/v1_beta");
    
    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShipmentApi apiInstance = new ShipmentApi(defaultClient);
    String shipmentId = "shipmentId_example"; // String | This path parameter specifies the unique eBay-assigned ID of the shipment to be canceled. The <b>shipmentId</b> value is generated and returned by a call to <b>createFromShippingQuote</b>.
    try {
      Shipment result = apiInstance.cancelShipment(shipmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentApi#cancelShipment");
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
| **shipmentId** | **String**| This path parameter specifies the unique eBay-assigned ID of the shipment to be canceled. The &lt;b&gt;shipmentId&lt;/b&gt; value is generated and returned by a call to &lt;b&gt;createFromShippingQuote&lt;/b&gt;. | |

### Return type

[**Shipment**](Shipment.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **500** | Internal Server Error |  -  |

<a id="createFromShippingQuote"></a>
# **createFromShippingQuote**
> Shipment createFromShippingQuote(createShipmentFromQuoteRequest)



This method creates a \&quot;shipment\&quot; based on the &lt;b&gt;shippingQuoteId&lt;/b&gt; and &lt;b&gt;rateId&lt;/b&gt; values supplied in the request. The rate identified by the &lt;b&gt;rateId&lt;/b&gt; value specifies the carrier and service for the package shipment, and the rate ID must be contained in the shipping quote identified by the &lt;b&gt;shippingQuoteId&lt;/b&gt; value. Call &lt;b&gt;createShippingQuote&lt;/b&gt; to retrieve a set of live shipping rates.  &lt;br&gt;&lt;br&gt;When you create a shipment, eBay generates a shipping label that you can download and use to ship your package.  &lt;br&gt;&lt;br&gt;In a &lt;b&gt;createFromShippingQuote&lt;/b&gt; request, sellers can include a list of shipping options they want to add to the base service quoted in the selected rate. The list of available shipping options is specific to each quoted rate and if available, the options are listed in the rate container of the of the shipping quote.  &lt;br&gt;&lt;br&gt;In addition to a configurable return-to location and other details about the shipment, the response to this method includes:  &lt;ul&gt;&lt;li&gt;The shipping carrier and service to be used for the package shipment&lt;/li&gt; &lt;li&gt;A list of selected shipping options, if any&lt;/li&gt; &lt;li&gt;The shipment tracking number&lt;/li&gt; &lt;li&gt;The total shipping cost (the sum cost of the base shipping service and any added options)&lt;/li&gt;&lt;/ul&gt; When you create a shipment, your billing agreement account is charged the sum of the &lt;b&gt;baseShippingCost&lt;/b&gt; and the total cost of any additional shipping options you might have selected. Use the URL returned in &lt;b&gt;labelDownloadUrl&lt;/b&gt; field, or call &lt;b&gt;downloadLabelFile&lt;/b&gt; with the &lt;b&gt;shipmentId&lt;/b&gt; value from the response, to download a shipping label for your package. &lt;p class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Important!&lt;/b&gt; Sellers must set up their payment method with eBay before they can use this method to create a shipment and the associated shipping label.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/sell/logistics/v1_beta");
    
    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShipmentApi apiInstance = new ShipmentApi(defaultClient);
    CreateShipmentFromQuoteRequest createShipmentFromQuoteRequest = new CreateShipmentFromQuoteRequest(); // CreateShipmentFromQuoteRequest | The create shipment from quote request.
    try {
      Shipment result = apiInstance.createFromShippingQuote(createShipmentFromQuoteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentApi#createFromShippingQuote");
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
| **createShipmentFromQuoteRequest** | [**CreateShipmentFromQuoteRequest**](CreateShipmentFromQuoteRequest.md)| The create shipment from quote request. | |

### Return type

[**Shipment**](Shipment.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **409** | Conflict |  -  |
| **500** | Internal Server Error |  -  |

<a id="downloadLabelFile"></a>
# **downloadLabelFile**
> List&lt;String&gt; downloadLabelFile(shipmentId)



This method returns the shipping label file that was generated for the &lt;b&gt;shipmentId&lt;/b&gt; value specified in the request. Call &lt;b&gt;createFromShippingQuote&lt;/b&gt; to generate a shipment ID.  &lt;br&gt;&lt;br&gt;Use the &lt;code&gt;Accept&lt;/code&gt; HTTP header to specify the format of the returned file. The default file format is a PDF file. &lt;!-- Are other options available? --&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/sell/logistics/v1_beta");
    
    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShipmentApi apiInstance = new ShipmentApi(defaultClient);
    String shipmentId = "shipmentId_example"; // String | This path parameter specifies the unique eBay-assigned ID of the shipment associated with the shipping label you want to download. The <b>shipmentId</b> value is generated and returned by a call to <b>createFromShippingQuote</b>.
    try {
      List<String> result = apiInstance.downloadLabelFile(shipmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentApi#downloadLabelFile");
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
| **shipmentId** | **String**| This path parameter specifies the unique eBay-assigned ID of the shipment associated with the shipping label you want to download. The &lt;b&gt;shipmentId&lt;/b&gt; value is generated and returned by a call to &lt;b&gt;createFromShippingQuote&lt;/b&gt;. | |

### Return type

**List&lt;String&gt;**

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getShipment"></a>
# **getShipment**
> Shipment getShipment(shipmentId)



This method retrieves the shipment details for the specified shipment ID. Call &lt;b&gt;createFromShippingQuote&lt;/b&gt; to generate a shipment ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/sell/logistics/v1_beta");
    
    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShipmentApi apiInstance = new ShipmentApi(defaultClient);
    String shipmentId = "shipmentId_example"; // String | This path parameter specifies the unique eBay-assigned ID of the shipment you want to retrieve. The <b>shipmentId</b> value is generated and returned by a call to <b>createFromShippingQuote</b>.
    try {
      Shipment result = apiInstance.getShipment(shipmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentApi#getShipment");
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
| **shipmentId** | **String**| This path parameter specifies the unique eBay-assigned ID of the shipment you want to retrieve. The &lt;b&gt;shipmentId&lt;/b&gt; value is generated and returned by a call to &lt;b&gt;createFromShippingQuote&lt;/b&gt;. | |

### Return type

[**Shipment**](Shipment.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

