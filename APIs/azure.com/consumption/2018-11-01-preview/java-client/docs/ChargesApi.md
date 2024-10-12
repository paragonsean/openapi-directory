# ChargesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chargesByBillingAccountList**](ChargesApi.md#chargesByBillingAccountList) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.Consumption/charges |  |
| [**chargesByBillingProfileList**](ChargesApi.md#chargesByBillingProfileList) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/providers/Microsoft.Consumption/charges |  |
| [**chargesByInvoiceSectionList**](ChargesApi.md#chargesByInvoiceSectionList) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}/providers/Microsoft.Consumption/charges |  |


<a id="chargesByBillingAccountList"></a>
# **chargesByBillingAccountList**
> ChargesListByBillingAccount chargesByBillingAccountList(billingAccountId, apiVersion, startDate, endDate, $apply)



Lists the charges by billingAccountId for given start and end date. Start and end date are used to determine the billing period. For current month, the data will be provided from month to date. If there are no charges for a month then that month will show all zeroes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChargesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ChargesApi apiInstance = new ChargesApi(defaultClient);
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String startDate = "startDate_example"; // String | Start date
    String endDate = "endDate_example"; // String | End date
    String $apply = "$apply_example"; // String | May be used to group charges by properties/billingProfileId, or properties/invoiceSectionId.
    try {
      ChargesListByBillingAccount result = apiInstance.chargesByBillingAccountList(billingAccountId, apiVersion, startDate, endDate, $apply);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChargesApi#chargesByBillingAccountList");
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
| **billingAccountId** | **String**| BillingAccount ID | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **startDate** | **String**| Start date | |
| **endDate** | **String**| End date | |
| **$apply** | **String**| May be used to group charges by properties/billingProfileId, or properties/invoiceSectionId. | [optional] |

### Return type

[**ChargesListByBillingAccount**](ChargesListByBillingAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="chargesByBillingProfileList"></a>
# **chargesByBillingProfileList**
> ChargesListByBillingProfile chargesByBillingProfileList(billingAccountId, billingProfileId, apiVersion, startDate, endDate)



Lists the charges by billing profile id for given start and end date. Start and end date are used to determine the billing period. For current month, the data will be provided from month to date. If there are no charges for a month then that month will show all zeroes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChargesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ChargesApi apiInstance = new ChargesApi(defaultClient);
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String billingProfileId = "billingProfileId_example"; // String | Billing Profile Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String startDate = "startDate_example"; // String | Start date
    String endDate = "endDate_example"; // String | End date
    try {
      ChargesListByBillingProfile result = apiInstance.chargesByBillingProfileList(billingAccountId, billingProfileId, apiVersion, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChargesApi#chargesByBillingProfileList");
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
| **billingAccountId** | **String**| BillingAccount ID | |
| **billingProfileId** | **String**| Billing Profile Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **startDate** | **String**| Start date | |
| **endDate** | **String**| End date | |

### Return type

[**ChargesListByBillingProfile**](ChargesListByBillingProfile.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="chargesByInvoiceSectionList"></a>
# **chargesByInvoiceSectionList**
> ChargesListByInvoiceSection chargesByInvoiceSectionList(billingAccountId, invoiceSectionId, apiVersion, startDate, endDate, $apply)



Lists the charges by invoice section id for given start and end date. Start and end date are used to determine the billing period. For current month, the data will be provided from month to date. If there are no charges for a month then that month will show all zeroes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChargesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ChargesApi apiInstance = new ChargesApi(defaultClient);
    String billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
    String invoiceSectionId = "invoiceSectionId_example"; // String | Invoice Section Id.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String startDate = "startDate_example"; // String | Start date
    String endDate = "endDate_example"; // String | End date
    String $apply = "$apply_example"; // String | May be used to group charges by properties/productName.
    try {
      ChargesListByInvoiceSection result = apiInstance.chargesByInvoiceSectionList(billingAccountId, invoiceSectionId, apiVersion, startDate, endDate, $apply);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChargesApi#chargesByInvoiceSectionList");
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
| **billingAccountId** | **String**| BillingAccount ID | |
| **invoiceSectionId** | **String**| Invoice Section Id. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **startDate** | **String**| Start date | |
| **endDate** | **String**| End date | |
| **$apply** | **String**| May be used to group charges by properties/productName. | [optional] |

### Return type

[**ChargesListByInvoiceSection**](ChargesListByInvoiceSection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

