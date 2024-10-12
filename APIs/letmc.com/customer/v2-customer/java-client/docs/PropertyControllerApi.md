# PropertyControllerApi

All URIs are relative to *https://live-api.letmc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**propertyControllerGetPropertiesPhotos**](PropertyControllerApi.md#propertyControllerGetPropertiesPhotos) | **GET** /v2/customer/{shortName}/property/{propertyID}/photos | A collection showing all the photos linked to a specific block, property or room |


<a id="propertyControllerGetPropertiesPhotos"></a>
# **propertyControllerGetPropertiesPhotos**
> LandlordPhotoModelResults propertyControllerGetPropertiesPhotos(shortName, token, propertyID, offset, count)

A collection showing all the photos linked to a specific block, property or room

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertyControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    PropertyControllerApi apiInstance = new PropertyControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String token = "token_example"; // String | The login token returned from the /session POST call
    String propertyID = "propertyID_example"; // String | The unique ID of the Property
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      LandlordPhotoModelResults result = apiInstance.propertyControllerGetPropertiesPhotos(shortName, token, propertyID, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertyControllerApi#propertyControllerGetPropertiesPhotos");
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
| **token** | **String**| The login token returned from the /session POST call | |
| **propertyID** | **String**| The unique ID of the Property | |
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |

### Return type

[**LandlordPhotoModelResults**](LandlordPhotoModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

