# IntegrationAccountCertificatesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**certificatesCreateOrUpdate**](IntegrationAccountCertificatesApi.md#certificatesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/certificates/{certificateName} |  |
| [**certificatesDelete**](IntegrationAccountCertificatesApi.md#certificatesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/certificates/{certificateName} |  |
| [**certificatesGet**](IntegrationAccountCertificatesApi.md#certificatesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/certificates/{certificateName} |  |
| [**certificatesListByIntegrationAccounts**](IntegrationAccountCertificatesApi.md#certificatesListByIntegrationAccounts) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/certificates |  |


<a id="certificatesCreateOrUpdate"></a>
# **certificatesCreateOrUpdate**
> IntegrationAccountCertificate certificatesCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, certificateName, apiVersion, certificate)



Creates or updates an integration account certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountCertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountCertificatesApi apiInstance = new IntegrationAccountCertificatesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String certificateName = "certificateName_example"; // String | The integration account certificate name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    IntegrationAccountCertificate certificate = new IntegrationAccountCertificate(); // IntegrationAccountCertificate | The integration account certificate.
    try {
      IntegrationAccountCertificate result = apiInstance.certificatesCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, certificateName, apiVersion, certificate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountCertificatesApi#certificatesCreateOrUpdate");
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

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |

<a id="certificatesDelete"></a>
# **certificatesDelete**
> certificatesDelete(subscriptionId, resourceGroupName, integrationAccountName, certificateName, apiVersion)



Deletes an integration account certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountCertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountCertificatesApi apiInstance = new IntegrationAccountCertificatesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String certificateName = "certificateName_example"; // String | The integration account certificate name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.certificatesDelete(subscriptionId, resourceGroupName, integrationAccountName, certificateName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountCertificatesApi#certificatesDelete");
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

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |

<a id="certificatesGet"></a>
# **certificatesGet**
> IntegrationAccountCertificate certificatesGet(subscriptionId, resourceGroupName, integrationAccountName, certificateName, apiVersion)



Gets an integration account certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountCertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountCertificatesApi apiInstance = new IntegrationAccountCertificatesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String certificateName = "certificateName_example"; // String | The integration account certificate name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      IntegrationAccountCertificate result = apiInstance.certificatesGet(subscriptionId, resourceGroupName, integrationAccountName, certificateName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountCertificatesApi#certificatesGet");
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

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificatesListByIntegrationAccounts"></a>
# **certificatesListByIntegrationAccounts**
> IntegrationAccountCertificateListResult certificatesListByIntegrationAccounts(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, $top)



Gets a list of integration account certificates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountCertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountCertificatesApi apiInstance = new IntegrationAccountCertificatesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    Integer $top = 56; // Integer | The number of items to be included in the result.
    try {
      IntegrationAccountCertificateListResult result = apiInstance.certificatesListByIntegrationAccounts(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountCertificatesApi#certificatesListByIntegrationAccounts");
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

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

