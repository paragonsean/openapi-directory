# TdeCertificatesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tdeCertificatesCreate**](TdeCertificatesApi.md#tdeCertificatesCreate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/tdeCertificates |  |


<a id="tdeCertificatesCreate"></a>
# **tdeCertificatesCreate**
> tdeCertificatesCreate(resourceGroupName, serverName, subscriptionId, apiVersion, parameters)



Creates a TDE certificate for a given server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TdeCertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    TdeCertificatesApi apiInstance = new TdeCertificatesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    TdeCertificate parameters = new TdeCertificate(); // TdeCertificate | The requested TDE certificate to be created or updated.
    try {
      apiInstance.tdeCertificatesCreate(resourceGroupName, serverName, subscriptionId, apiVersion, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling TdeCertificatesApi#tdeCertificatesCreate");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**TdeCertificate**](TdeCertificate.md)| The requested TDE certificate to be created or updated. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully created the TDE certificate. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 MissingPrivateBlob - The private blob is missing.   * 400 InvalidPrivateBlobOrPassword - Invalid private blob or password specified.   * 400 InvalidResourceRequestBody - The resource or resource properties in the request body is empty or invalid.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

