# CloudStorageApi

All URIs are relative to *https://app.billbee.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cloudStorageApiGetList**](CloudStorageApi.md#cloudStorageApiGetList) | **GET** /api/v1/cloudstorages | Gets a list of all connected cloud storage devices |


<a id="cloudStorageApiGetList"></a>
# **cloudStorageApiGetList**
> RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCloudStorageApiModel cloudStorageApiGetList()

Gets a list of all connected cloud storage devices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudStorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    CloudStorageApi apiInstance = new CloudStorageApi(defaultClient);
    try {
      RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCloudStorageApiModel result = apiInstance.cloudStorageApiGetList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudStorageApi#cloudStorageApiGetList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCloudStorageApiModel**](RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCloudStorageApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

