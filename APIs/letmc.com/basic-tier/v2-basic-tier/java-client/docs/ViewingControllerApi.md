# ViewingControllerApi

All URIs are relative to *https://live-api.letmc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**viewingControllerGetBookings**](ViewingControllerApi.md#viewingControllerGetBookings) | **GET** /v2/tier2/{shortName}/viewing/bookings | Gets a list of available viewing slots for one or more properties |
| [**viewingControllerMakeBooking**](ViewingControllerApi.md#viewingControllerMakeBooking) | **POST** /v2/tier2/{shortName}/viewing/bookings | Book an appointment for a viewing slot returned from the GET verb |


<a id="viewingControllerGetBookings"></a>
# **viewingControllerGetBookings**
> List&lt;ViewingBookingModel&gt; viewingControllerGetBookings(shortName, preferredDate, propertyIDsToView)

Gets a list of available viewing slots for one or more properties

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewingControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    ViewingControllerApi apiInstance = new ViewingControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    OffsetDateTime preferredDate = OffsetDateTime.now(); // OffsetDateTime | The preferred date for a viewing
    List<String> propertyIDsToView = Arrays.asList(); // List<String> | An array of unique IDs of properties to view
    try {
      List<ViewingBookingModel> result = apiInstance.viewingControllerGetBookings(shortName, preferredDate, propertyIDsToView);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewingControllerApi#viewingControllerGetBookings");
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
| **shortName** | **String**| The unique client short-name | |
| **preferredDate** | **OffsetDateTime**| The preferred date for a viewing | |
| **propertyIDsToView** | [**List&lt;String&gt;**](String.md)| An array of unique IDs of properties to view | |

### Return type

[**List&lt;ViewingBookingModel&gt;**](ViewingBookingModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="viewingControllerMakeBooking"></a>
# **viewingControllerMakeBooking**
> Boolean viewingControllerMakeBooking(shortName, forename, surname, mobilePhone, emailAddress, propertyIDsToView, selectedViewingSlot, wantRoomInSharedProperty, alertMinRent, alertMaxRent, alertNumberOfBeds, alertAreaID, alertTenantType, subscribeToEmailAlerts, subscribeToSMSAlerts)

Book an appointment for a viewing slot returned from the GET verb

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewingControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    ViewingControllerApi apiInstance = new ViewingControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String forename = "forename_example"; // String | The forename of the prospect
    String surname = "surname_example"; // String | The surname of the prospect
    String mobilePhone = "mobilePhone_example"; // String | The mobile phone number of the prospect
    String emailAddress = "emailAddress_example"; // String | The email address of the prospect
    List<String> propertyIDsToView = Arrays.asList(); // List<String> | An array of unique IDs of properties to view
    ViewingBookingModel selectedViewingSlot = new ViewingBookingModel(); // ViewingBookingModel | The prospect's selected viewing slot
    Boolean wantRoomInSharedProperty = true; // Boolean | Whether the prospect wants a shared property
    Double alertMinRent = 3.4D; // Double | The minimum rent amount the prospect is looking for
    Double alertMaxRent = 3.4D; // Double | The maximum rent amount the prospect is looking for
    Integer alertNumberOfBeds = 56; // Integer | The minimum number of beds the prospect is looking for
    String alertAreaID = "alertAreaID_example"; // String | The unique ID of the area the prospect is looking for
    String alertTenantType = "Employed"; // String | The tenanct type the prospect is looking for
    Boolean subscribeToEmailAlerts = true; // Boolean | Whether to subscribe the prospect to email alerts
    Boolean subscribeToSMSAlerts = true; // Boolean | Whether to subscribe the prospect to SMS alerts
    try {
      Boolean result = apiInstance.viewingControllerMakeBooking(shortName, forename, surname, mobilePhone, emailAddress, propertyIDsToView, selectedViewingSlot, wantRoomInSharedProperty, alertMinRent, alertMaxRent, alertNumberOfBeds, alertAreaID, alertTenantType, subscribeToEmailAlerts, subscribeToSMSAlerts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewingControllerApi#viewingControllerMakeBooking");
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
| **shortName** | **String**| The unique client short-name | |
| **forename** | **String**| The forename of the prospect | |
| **surname** | **String**| The surname of the prospect | |
| **mobilePhone** | **String**| The mobile phone number of the prospect | |
| **emailAddress** | **String**| The email address of the prospect | |
| **propertyIDsToView** | [**List&lt;String&gt;**](String.md)| An array of unique IDs of properties to view | |
| **selectedViewingSlot** | [**ViewingBookingModel**](ViewingBookingModel.md)| The prospect&#39;s selected viewing slot | |
| **wantRoomInSharedProperty** | **Boolean**| Whether the prospect wants a shared property | [optional] |
| **alertMinRent** | **Double**| The minimum rent amount the prospect is looking for | [optional] |
| **alertMaxRent** | **Double**| The maximum rent amount the prospect is looking for | [optional] |
| **alertNumberOfBeds** | **Integer**| The minimum number of beds the prospect is looking for | [optional] |
| **alertAreaID** | **String**| The unique ID of the area the prospect is looking for | [optional] |
| **alertTenantType** | **String**| The tenanct type the prospect is looking for | [optional] [enum: Employed, SelfEmployed, Unemployed, Student, OwnMeans, Retired, Company, Council] |
| **subscribeToEmailAlerts** | **Boolean**| Whether to subscribe the prospect to email alerts | [optional] |
| **subscribeToSMSAlerts** | **Boolean**| Whether to subscribe the prospect to SMS alerts | [optional] |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

