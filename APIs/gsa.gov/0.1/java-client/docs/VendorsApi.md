# VendorsApi

All URIs are relative to *https://discovery.gsa.gov*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listVendorsGET**](VendorsApi.md#listVendorsGET) | **GET** /api/vendors/ | This endpoint returns a list of vendors filtered by a NAICS code |


<a id="listVendorsGET"></a>
# **listVendorsGET**
> Object listVendorsGET(naics, setasides, vehicle)

This endpoint returns a list of vendors filtered by a NAICS code

&lt;p&gt;This endpoint returns a list of vendors filtered by a NAICS code. The NAICS code maps to an OASIS pool and is used to retrieve vendors in that pool only.&lt;/p&gt; &lt;p&gt;OASIS pools are groupings of NAICS codes that have the same small business size standard. Because contracts solicited to OASIS vendors can only be issued to one pool, much of the data is presented as part of a pool grouping. Using the NAICS code is a shortcut, so that you don&#39;t have to explicitly map the NAICS code to a pool in OASIS yourself.&lt;/p&gt; &lt;p&gt;Vendors can also be filtered by a particular setaside. Valid values for the setasides are two-character codes which include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt;A6 (8(a))&lt;/li&gt; &lt;li&gt;XX (Hubzone)&lt;/li&gt; &lt;li&gt;QF (service disabled veteran owned)&lt;/li&gt; &lt;li&gt;A2 (women owned)&lt;/li&gt; &lt;li&gt;A5 (veteran owned)&lt;/li&gt; &lt;li&gt;27 (small disadvantaged business).&lt;/li&gt; &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://discovery.gsa.gov");

    VendorsApi apiInstance = new VendorsApi(defaultClient);
    String naics = "naics_example"; // String | a six digit NAICS code (required)
    List<String> setasides = Arrays.asList(); // List<String> | a comma delimited list of two character setaside codes to filter by.  Ex. setasides=A6,A5  will filter by 8a and veteran owned business.
    String vehicle = "vehicle_example"; // String | Choices are either oasis or oasissb. Will filter vendors by their presence in either the OASIS unrestricted vehicle or the OASIS Small Business vehicle.
    try {
      Object result = apiInstance.listVendorsGET(naics, setasides, vehicle);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorsApi#listVendorsGET");
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
| **naics** | **String**| a six digit NAICS code (required) | |
| **setasides** | [**List&lt;String&gt;**](String.md)| a comma delimited list of two character setaside codes to filter by.  Ex. setasides&#x3D;A6,A5  will filter by 8a and veteran owned business. | [optional] |
| **vehicle** | **String**| Choices are either oasis or oasissb. Will filter vendors by their presence in either the OASIS unrestricted vehicle or the OASIS Small Business vehicle. | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

