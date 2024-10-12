# IntegrationAccountCertificatesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**integrationAccountCertificatesCreateOrUpdate**](IntegrationAccountCertificatesApi.md#integrationAccountCertificatesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/certificates/{certificateName} |  |
| [**integrationAccountCertificatesDelete**](IntegrationAccountCertificatesApi.md#integrationAccountCertificatesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/certificates/{certificateName} |  |
| [**integrationAccountCertificatesGet**](IntegrationAccountCertificatesApi.md#integrationAccountCertificatesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/certificates/{certificateName} |  |
| [**integrationAccountCertificatesList**](IntegrationAccountCertificatesApi.md#integrationAccountCertificatesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/certificates |  |


<a id="integrationAccountCertificatesCreateOrUpdate"></a>
# **integrationAccountCertificatesCreateOrUpdate**
> IntegrationAccountCertificate integrationAccountCertificatesCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, certificateName, apiVersion, certificate)



Creates or updates an integration account certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountCertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    IntegrationAccountCertificatesApi apiInstance = new IntegrationAccountCertificatesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String certificateName = "certificateName_example"; // String | The integration account certificate name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    IntegrationAccountCertificate certificate = new IntegrationAccountCertificate(); // IntegrationAccountCertificate | The integration account certificate.
    try {
      IntegrationAccountCertificate result = apiInstance.integrationAccountCertificatesCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, certificateName, apiVersion, certificate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountCertificatesApi#integrationAccountCertificatesCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **certificateName** | **String**| The integration account certificate name. | |
| **apiVersion** | **String**| The API version. | |
| **certificate** | [**IntegrationAccountCertificate**](IntegrationAccountCertificate.md)| The integration account certificate. | |

### Return type

[**IntegrationAccountCertificate**](IntegrationAccountCertificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |

<a id="integrationAccountCertificatesDelete"></a>
# **integrationAccountCertificatesDelete**
> integrationAccountCertificatesDelete(subscriptionId, resourceGroupName, integrationAccountName, certificateName, apiVersion)



Deletes an integration account certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountCertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    IntegrationAccountCertificatesApi apiInstance = new IntegrationAccountCertificatesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String certificateName = "certificateName_example"; // String | The integration account certificate name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.integrationAccountCertificatesDelete(subscriptionId, resourceGroupName, integrationAccountName, certificateName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountCertificatesApi#integrationAccountCertificatesDelete");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **certificateName** | **String**| The integration account certificate name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |

<a id="integrationAccountCertificatesGet"></a>
# **integrationAccountCertificatesGet**
> IntegrationAccountCertificate integrationAccountCertificatesGet(subscriptionId, resourceGroupName, integrationAccountName, certificateName, apiVersion)



Gets an integration account certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountCertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    IntegrationAccountCertificatesApi apiInstance = new IntegrationAccountCertificatesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String certificateName = "certificateName_example"; // String | The integration account certificate name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      IntegrationAccountCertificate result = apiInstance.integrationAccountCertificatesGet(subscriptionId, resourceGroupName, integrationAccountName, certificateName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountCertificatesApi#integrationAccountCertificatesGet");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **certificateName** | **String**| The integration account certificate name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**IntegrationAccountCertificate**](IntegrationAccountCertificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="integrationAccountCertificatesList"></a>
# **integrationAccountCertificatesList**
> IntegrationAccountCertificateListResult integrationAccountCertificatesList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, $top)



Gets a list of integration account certificates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountCertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    IntegrationAccountCertificatesApi apiInstance = new IntegrationAccountCertificatesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    Integer $top = 56; // Integer | The number of items to be included in the result.
    try {
      IntegrationAccountCertificateListResult result = apiInstance.integrationAccountCertificatesList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountCertificatesApi#integrationAccountCertificatesList");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **apiVersion** | **String**| The API version. | |
| **$top** | **Integer**| The number of items to be included in the result. | [optional] |

### Return type

[**IntegrationAccountCertificateListResult**](IntegrationAccountCertificateListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

