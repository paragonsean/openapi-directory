# FleetApi

All URIs are relative to *https://phantauth.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fleetFleetnameGet**](FleetApi.md#fleetFleetnameGet) | **GET** /fleet/{fleetname} | Get a Fleet |


<a id="fleetFleetnameGet"></a>
# **fleetFleetnameGet**
> FleetFleetnameGet200Response fleetFleetnameGet(fleetname)

Get a Fleet

Use this endpoint to generate a random group of clients. The feleet is generated in a deterministic way, on the basis of a fleet name given as a path parameter. In the case of identical fleet names, the endpoint will generate the same fleet object. The properties of the generated fleet object are randomly generated on the basis of the fleet name. In lack of a fleet name, all calls generate a different fleet object to the randomly generated fleet name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FleetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://phantauth.net");

    FleetApi apiInstance = new FleetApi(defaultClient);
    String fleetname = "fleetname_example"; // String |  The identifier or email address of the fleet; it is integrated in the `sub` property and is the basis of the other generated properties. 
    try {
      FleetFleetnameGet200Response result = apiInstance.fleetFleetnameGet(fleetname);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FleetApi#fleetFleetnameGet");
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
| **fleetname** | **String**|  The identifier or email address of the fleet; it is integrated in the &#x60;sub&#x60; property and is the basis of the other generated properties.  | |

### Return type

[**FleetFleetnameGet200Response**](FleetFleetnameGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

