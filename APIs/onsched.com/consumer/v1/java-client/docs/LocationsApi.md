# LocationsApi

All URIs are relative to *https://sandbox-api.onsched.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**consumerV1LocationsGet**](LocationsApi.md#consumerV1LocationsGet) | **GET** /consumer/v1/locations | List Locations |
| [**consumerV1LocationsIdGet**](LocationsApi.md#consumerV1LocationsIdGet) | **GET** /consumer/v1/locations/{id} | Get Location |


<a id="consumerV1LocationsGet"></a>
# **consumerV1LocationsGet**
> LocationListViewModel consumerV1LocationsGet(name, nearestTo, proximity, units, serviceId, friendlyId, regionId, ignorePrimary, offset, limit)

List Locations

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Business Locations&lt;/b&gt;. The results are returned in pages. Use the offset and limit parameters to control the page start and size. Default offset is 0, and limit is 20 and maximum is 100. Use the other query parameters to filter the results further. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;IMPORTANT DEPRECATION NOTICE&lt;/b&gt;: The following online settings parameters were intended for internal use in our Portal application only. They will be deprecated on &lt;b&gt;OCTOBER 15, 2022&lt;/b&gt;. These fields are currently part of the &lt;b&gt;SETTINGS&lt;/b&gt; object in all location endpoints: &lt;b&gt;businessId, enabled, familyMembersEnabled, serviceLabel, resourceLabel, resourceAnyLabel, resourceSelection, liveMode, formFlow, availabilityForm, showServiceGroups, showOnSchedLogo, showBusinessLogo, disableAuthorization, hideNavBar, hideLocationNav, hideServiceGroupsNav, hideServicesNav, hideContinueBooking, returnToService, returnToAvailability, hideBreadCrumbNav.&lt;/b&gt; If you are using these fields, please adjust your code to handle the deprecation or let us know by submitting a ticket to: &lt;b&gt;&lt;i&gt;support@onsched.com&lt;/i&gt;&lt;/b&gt; as we do not want to interrupt your existing workflows.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String name = "name_example"; // String | Location name (full or partial)
    String nearestTo = "nearestTo_example"; // String | Search by distance nearest Geocoords, City, Postal/Zip Code
    Integer proximity = 56; // Integer | Maximum distance to display
    String units = "units_example"; // String | Distance either imperial(miles), metric(kilometers)
    String serviceId = "serviceId_example"; // String | Locations that offer this service
    String friendlyId = "friendlyId_example"; // String | Frienldy Id of location
    String regionId = "regionId_example"; // String | Locations within a specific region
    Boolean ignorePrimary = true; // Boolean | Don't include the Primary Location
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit, default 20, max 100
    try {
      LocationListViewModel result = apiInstance.consumerV1LocationsGet(name, nearestTo, proximity, units, serviceId, friendlyId, regionId, ignorePrimary, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#consumerV1LocationsGet");
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
| **name** | **String**| Location name (full or partial) | [optional] |
| **nearestTo** | **String**| Search by distance nearest Geocoords, City, Postal/Zip Code | [optional] |
| **proximity** | **Integer**| Maximum distance to display | [optional] |
| **units** | **String**| Distance either imperial(miles), metric(kilometers) | [optional] |
| **serviceId** | **String**| Locations that offer this service | [optional] |
| **friendlyId** | **String**| Frienldy Id of location | [optional] |
| **regionId** | **String**| Locations within a specific region | [optional] |
| **ignorePrimary** | **Boolean**| Don&#39;t include the Primary Location | [optional] |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit, default 20, max 100 | [optional] |

### Return type

[**LocationListViewModel**](LocationListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="consumerV1LocationsIdGet"></a>
# **consumerV1LocationsIdGet**
> LocationViewModel consumerV1LocationsIdGet(id)

Get Location

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Location&lt;/b&gt; object. A valid business &lt;b&gt;location id&lt;/b&gt; is required. Find all location id&#39;s by using the &lt;i&gt;GET /consumer/v1/locations&lt;/i&gt; endpoint.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;IMPORTANT DEPRECATION NOTICE&lt;/b&gt;: The following online settings parameters were intended for internal use in our Portal application only. They will be deprecated on &lt;b&gt;OCTOBER 15, 2022&lt;/b&gt;. These fields are currently part of the &lt;b&gt;SETTINGS&lt;/b&gt; object in all location endpoints: &lt;b&gt;businessId, enabled, familyMembersEnabled, serviceLabel, resourceLabel, resourceAnyLabel, resourceSelection, liveMode, formFlow, availabilityForm, showServiceGroups, showOnSchedLogo, showBusinessLogo, disableAuthorization, hideNavBar, hideLocationNav, hideServiceGroupsNav, hideServicesNav, hideContinueBooking, returnToService, returnToAvailability, hideBreadCrumbNav.&lt;/b&gt; If you are using these fields, please adjust your code to handle the deprecation or let us know by submitting a ticket to: &lt;b&gt;&lt;i&gt;support@onsched.com&lt;/i&gt;&lt;/b&gt; as we do not want to interrupt your existing workflows.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String id = "id_example"; // String | id of business location
    try {
      LocationViewModel result = apiInstance.consumerV1LocationsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#consumerV1LocationsIdGet");
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
| **id** | **String**| id of business location | |

### Return type

[**LocationViewModel**](LocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

