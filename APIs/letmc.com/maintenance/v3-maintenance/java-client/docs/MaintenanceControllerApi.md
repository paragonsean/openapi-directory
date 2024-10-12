# MaintenanceControllerApi

All URIs are relative to *https://live-api.letmc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**maintenanceControllerCreateMaintenanceJob**](MaintenanceControllerApi.md#maintenanceControllerCreateMaintenanceJob) | **POST** /v3/maintenance/{shortName}/maintenance/{branchID}/createmaintenancejob | Create a maintenance job for a specific branch |


<a id="maintenanceControllerCreateMaintenanceJob"></a>
# **maintenanceControllerCreateMaintenanceJob**
> Object maintenanceControllerCreateMaintenanceJob(shortName, branchID, maintenanceIssueModel)

Create a maintenance job for a specific branch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MaintenanceControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    MaintenanceControllerApi apiInstance = new MaintenanceControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String branchID = "branchID_example"; // String | The unique ID of the Branch
    MaintenanceIssueModel maintenanceIssueModel = new MaintenanceIssueModel(); // MaintenanceIssueModel | A JSON object containing details of the maintenance job
    try {
      Object result = apiInstance.maintenanceControllerCreateMaintenanceJob(shortName, branchID, maintenanceIssueModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MaintenanceControllerApi#maintenanceControllerCreateMaintenanceJob");
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
| **branchID** | **String**| The unique ID of the Branch | |
| **maintenanceIssueModel** | [**MaintenanceIssueModel**](MaintenanceIssueModel.md)| A JSON object containing details of the maintenance job | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

