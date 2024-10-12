# ComplaintsApi

All URIs are relative to *https://api.callcontrol.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**complaintsComplaints**](ComplaintsApi.md#complaintsComplaints) | **GET** /api/2015-11-01/Complaints/{phoneNumber} | Complaints: Free service (with registration), providing community and government complaint lookup by phone number for up to 2,000 queries per month.  Details include number complaint rates from (FTC, FCC, IRS, Indiana Attorney  General) and key entity tag extractions from complaints. |


<a id="complaintsComplaints"></a>
# **complaintsComplaints**
> Complaints complaintsComplaints(phoneNumber)

Complaints: Free service (with registration), providing community and government complaint lookup by phone number for up to 2,000 queries per month.  Details include number complaint rates from (FTC, FCC, IRS, Indiana Attorney  General) and key entity tag extractions from complaints.

This is the main funciton to get data out of the call control reporting system&lt;br /&gt;              Try with api_key &#39;demo&#39; and phone numbers 18008472911, 13157244022, 17275567300, 18008276655, and 12061231234 (last one not spam)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComplaintsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.callcontrol.com");

    ComplaintsApi apiInstance = new ComplaintsApi(defaultClient);
    String phoneNumber = "phoneNumber_example"; // String | phone number to search
    try {
      Complaints result = apiInstance.complaintsComplaints(phoneNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComplaintsApi#complaintsComplaints");
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
| **phoneNumber** | **String**| phone number to search | |

### Return type

[**Complaints**](Complaints.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

