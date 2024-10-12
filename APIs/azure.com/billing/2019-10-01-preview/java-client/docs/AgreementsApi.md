# AgreementsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**agreementsGet**](AgreementsApi.md#agreementsGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/agreements/{agreementName} |  |
| [**agreementsListByBillingAccount**](AgreementsApi.md#agreementsListByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/agreements |  |


<a id="agreementsGet"></a>
# **agreementsGet**
> Agreement agreementsGet(apiVersion, billingAccountName, agreementName, $expand)



Get the agreement by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgreementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AgreementsApi apiInstance = new AgreementsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String agreementName = "agreementName_example"; // String | Agreement Id.
    String $expand = "$expand_example"; // String | May be used to expand the participants.
    try {
      Agreement result = apiInstance.agreementsGet(apiVersion, billingAccountName, agreementName, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgreementsApi#agreementsGet");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |
| **billingAccountName** | **String**| billing Account Id. | |
| **agreementName** | **String**| Agreement Id. | |
| **$expand** | **String**| May be used to expand the participants. | [optional] |

### Return type

[**Agreement**](Agreement.md)

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

<a id="agreementsListByBillingAccount"></a>
# **agreementsListByBillingAccount**
> AgreementListResult agreementsListByBillingAccount(apiVersion, billingAccountName, $expand)



Lists all agreements for a billing account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgreementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AgreementsApi apiInstance = new AgreementsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String $expand = "$expand_example"; // String | May be used to expand the participants.
    try {
      AgreementListResult result = apiInstance.agreementsListByBillingAccount(apiVersion, billingAccountName, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgreementsApi#agreementsListByBillingAccount");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |
| **billingAccountName** | **String**| billing Account Id. | |
| **$expand** | **String**| May be used to expand the participants. | [optional] |

### Return type

[**AgreementListResult**](AgreementListResult.md)

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

