# PricesheetsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**billingProfilePricesheetDownload**](PricesheetsApi.md#billingProfilePricesheetDownload) | **POST** /providers/Microsoft.Consumption/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/pricesheet/default/download |  |
| [**invoicePricesheetDownload**](PricesheetsApi.md#invoicePricesheetDownload) | **POST** /providers/Microsoft.Consumption/billingAccounts/{billingAccountId}/invoices/{invoiceName}/pricesheet/default/download |  |


<a id="billingProfilePricesheetDownload"></a>
# **billingProfilePricesheetDownload**
> PricesheetDownloadResponse billingProfilePricesheetDownload(apiVersion, billingAccountId, billingProfileId)



Get pricesheet data for invoice id (invoiceName).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricesheetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PricesheetsApi apiInstance = new PricesheetsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountId = "billingAccountId_example"; // String | Azure Billing Account Id.
    String billingProfileId = "billingProfileId_example"; // String | Azure Billing Profile Id.
    try {
      PricesheetDownloadResponse result = apiInstance.billingProfilePricesheetDownload(apiVersion, billingAccountId, billingProfileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricesheetsApi#billingProfilePricesheetDownload");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **billingAccountId** | **String**| Azure Billing Account Id. | |
| **billingProfileId** | **String**| Azure Billing Profile Id. | |

### Return type

[**PricesheetDownloadResponse**](PricesheetDownloadResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted. |  * Retry-After - The amount of delay to use while the status of the operation is checked. The value is expressed in seconds. <br>  * OData-EntityId - The operation entity Id GUID. <br>  * Azure-AsyncOperation - To get the progress of the operation, call GET operation on the URL in Azure-AsyncOperation header field. <br>  * Location - GET this URL to retrieve the status of the asynchronous operation. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="invoicePricesheetDownload"></a>
# **invoicePricesheetDownload**
> PricesheetDownloadResponse invoicePricesheetDownload(apiVersion, billingAccountId, invoiceName)



Get pricesheet data for invoice id (invoiceName).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricesheetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PricesheetsApi apiInstance = new PricesheetsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountId = "billingAccountId_example"; // String | Azure Billing Account Id.
    String invoiceName = "invoiceName_example"; // String | The name of an invoice resource.
    try {
      PricesheetDownloadResponse result = apiInstance.invoicePricesheetDownload(apiVersion, billingAccountId, invoiceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricesheetsApi#invoicePricesheetDownload");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **billingAccountId** | **String**| Azure Billing Account Id. | |
| **invoiceName** | **String**| The name of an invoice resource. | |

### Return type

[**PricesheetDownloadResponse**](PricesheetDownloadResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted. |  * Retry-After - The amount of delay to use while the status of the operation is checked. The value is expressed in seconds. <br>  * OData-EntityId - The operation entity Id GUID. <br>  * Azure-AsyncOperation - To get the progress of the operation, call GET operation on the URL in Azure-AsyncOperation header field. <br>  * Location - GET this URL to retrieve the status of the asynchronous operation. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

