# InvoiceSectionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**invoiceSectionsCreate**](InvoiceSectionsApi.md#invoiceSectionsCreate) | **PUT** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName} |  |
| [**invoiceSectionsElevateToBillingProfile**](InvoiceSectionsApi.md#invoiceSectionsElevateToBillingProfile) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/elevate |  |
| [**invoiceSectionsGet**](InvoiceSectionsApi.md#invoiceSectionsGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName} |  |
| [**invoiceSectionsListByBillingProfile**](InvoiceSectionsApi.md#invoiceSectionsListByBillingProfile) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections |  |
| [**invoiceSectionsUpdate**](InvoiceSectionsApi.md#invoiceSectionsUpdate) | **PATCH** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName} |  |


<a id="invoiceSectionsCreate"></a>
# **invoiceSectionsCreate**
> InvoiceSection invoiceSectionsCreate(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, parameters)



The operation to create an invoice section.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceSectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InvoiceSectionsApi apiInstance = new InvoiceSectionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    InvoiceSectionCreationRequest parameters = new InvoiceSectionCreationRequest(); // InvoiceSectionCreationRequest | Request parameters supplied to the Create InvoiceSection operation.
    try {
      InvoiceSection result = apiInstance.invoiceSectionsCreate(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceSectionsApi#invoiceSectionsCreate");
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
| **billingProfileName** | **String**| Billing Profile Id. | |
| **invoiceSectionName** | **String**| InvoiceSection Id. | |
| **parameters** | [**InvoiceSectionCreationRequest**](InvoiceSectionCreationRequest.md)| Request parameters supplied to the Create InvoiceSection operation. | |

### Return type

[**InvoiceSection**](InvoiceSection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted |  * Retry-After - Recommends the retryable time after receiving this. <br>  * Location - Location URI to poll for result. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="invoiceSectionsElevateToBillingProfile"></a>
# **invoiceSectionsElevateToBillingProfile**
> invoiceSectionsElevateToBillingProfile(billingAccountName, billingProfileName, invoiceSectionName)



Elevates the caller&#39;s access to match their billing profile access.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceSectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InvoiceSectionsApi apiInstance = new InvoiceSectionsApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    try {
      apiInstance.invoiceSectionsElevateToBillingProfile(billingAccountName, billingProfileName, invoiceSectionName);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceSectionsApi#invoiceSectionsElevateToBillingProfile");
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
| **billingAccountName** | **String**| billing Account Id. | |
| **billingProfileName** | **String**| Billing Profile Id. | |
| **invoiceSectionName** | **String**| InvoiceSection Id. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Elevated the caller&#39;s access to the invoice section. |  -  |
| **0** | Unexpected error. |  -  |

<a id="invoiceSectionsGet"></a>
# **invoiceSectionsGet**
> InvoiceSection invoiceSectionsGet(apiVersion, billingAccountName, billingProfileName, invoiceSectionName)



Get the InvoiceSection by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceSectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InvoiceSectionsApi apiInstance = new InvoiceSectionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    try {
      InvoiceSection result = apiInstance.invoiceSectionsGet(apiVersion, billingAccountName, billingProfileName, invoiceSectionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceSectionsApi#invoiceSectionsGet");
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
| **billingProfileName** | **String**| Billing Profile Id. | |
| **invoiceSectionName** | **String**| InvoiceSection Id. | |

### Return type

[**InvoiceSection**](InvoiceSection.md)

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

<a id="invoiceSectionsListByBillingProfile"></a>
# **invoiceSectionsListByBillingProfile**
> InvoiceSectionListResult invoiceSectionsListByBillingProfile(apiVersion, billingAccountName, billingProfileName)



Lists all invoice sections for a user which he has access to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceSectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InvoiceSectionsApi apiInstance = new InvoiceSectionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    try {
      InvoiceSectionListResult result = apiInstance.invoiceSectionsListByBillingProfile(apiVersion, billingAccountName, billingProfileName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceSectionsApi#invoiceSectionsListByBillingProfile");
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
| **billingProfileName** | **String**| Billing Profile Id. | |

### Return type

[**InvoiceSectionListResult**](InvoiceSectionListResult.md)

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

<a id="invoiceSectionsUpdate"></a>
# **invoiceSectionsUpdate**
> InvoiceSection invoiceSectionsUpdate(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, parameters)



The operation to update a InvoiceSection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceSectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InvoiceSectionsApi apiInstance = new InvoiceSectionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    InvoiceSection parameters = new InvoiceSection(); // InvoiceSection | Request parameters supplied to the Create InvoiceSection operation.
    try {
      InvoiceSection result = apiInstance.invoiceSectionsUpdate(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceSectionsApi#invoiceSectionsUpdate");
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
| **billingProfileName** | **String**| Billing Profile Id. | |
| **invoiceSectionName** | **String**| InvoiceSection Id. | |
| **parameters** | [**InvoiceSection**](InvoiceSection.md)| Request parameters supplied to the Create InvoiceSection operation. | |

### Return type

[**InvoiceSection**](InvoiceSection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted. InvoiceSection update is in progress. |  * Retry-After - The amount of delay to use while the status of the operation is checked. The value is expressed in seconds. <br>  * Location - Location URI to poll for result. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

