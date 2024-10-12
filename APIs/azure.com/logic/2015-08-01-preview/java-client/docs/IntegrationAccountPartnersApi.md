# IntegrationAccountPartnersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**integrationAccountPartnersCreateOrUpdate**](IntegrationAccountPartnersApi.md#integrationAccountPartnersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/partners/{partnerName} |  |
| [**integrationAccountPartnersDelete**](IntegrationAccountPartnersApi.md#integrationAccountPartnersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/partners/{partnerName} |  |
| [**integrationAccountPartnersGet**](IntegrationAccountPartnersApi.md#integrationAccountPartnersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/partners/{partnerName} |  |
| [**integrationAccountPartnersList**](IntegrationAccountPartnersApi.md#integrationAccountPartnersList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/partners |  |


<a id="integrationAccountPartnersCreateOrUpdate"></a>
# **integrationAccountPartnersCreateOrUpdate**
> IntegrationAccountPartner integrationAccountPartnersCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, partnerName, apiVersion, partner)



Creates or updates an integration account partner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountPartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    IntegrationAccountPartnersApi apiInstance = new IntegrationAccountPartnersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String partnerName = "partnerName_example"; // String | The integration account partner name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    IntegrationAccountPartner partner = new IntegrationAccountPartner(); // IntegrationAccountPartner | The integration account partner.
    try {
      IntegrationAccountPartner result = apiInstance.integrationAccountPartnersCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, partnerName, apiVersion, partner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountPartnersApi#integrationAccountPartnersCreateOrUpdate");
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
| **partnerName** | **String**| The integration account partner name. | |
| **apiVersion** | **String**| The API version. | |
| **partner** | [**IntegrationAccountPartner**](IntegrationAccountPartner.md)| The integration account partner. | |

### Return type

[**IntegrationAccountPartner**](IntegrationAccountPartner.md)

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

<a id="integrationAccountPartnersDelete"></a>
# **integrationAccountPartnersDelete**
> integrationAccountPartnersDelete(subscriptionId, resourceGroupName, integrationAccountName, partnerName, apiVersion)



Deletes an integration account partner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountPartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    IntegrationAccountPartnersApi apiInstance = new IntegrationAccountPartnersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String partnerName = "partnerName_example"; // String | The integration account partner name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.integrationAccountPartnersDelete(subscriptionId, resourceGroupName, integrationAccountName, partnerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountPartnersApi#integrationAccountPartnersDelete");
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
| **partnerName** | **String**| The integration account partner name. | |
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

<a id="integrationAccountPartnersGet"></a>
# **integrationAccountPartnersGet**
> IntegrationAccountPartner integrationAccountPartnersGet(subscriptionId, resourceGroupName, integrationAccountName, partnerName, apiVersion)



Gets an integration account partner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountPartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    IntegrationAccountPartnersApi apiInstance = new IntegrationAccountPartnersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String partnerName = "partnerName_example"; // String | The integration account partner name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      IntegrationAccountPartner result = apiInstance.integrationAccountPartnersGet(subscriptionId, resourceGroupName, integrationAccountName, partnerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountPartnersApi#integrationAccountPartnersGet");
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
| **partnerName** | **String**| The integration account partner name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**IntegrationAccountPartner**](IntegrationAccountPartner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="integrationAccountPartnersList"></a>
# **integrationAccountPartnersList**
> IntegrationAccountPartnerListResult integrationAccountPartnersList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, $top, $filter)



Gets a list of integration account partners.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountPartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    IntegrationAccountPartnersApi apiInstance = new IntegrationAccountPartnersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    Integer $top = 56; // Integer | The number of items to be included in the result.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    try {
      IntegrationAccountPartnerListResult result = apiInstance.integrationAccountPartnersList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, $top, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountPartnersApi#integrationAccountPartnersList");
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
| **$filter** | **String**| The filter to apply on the operation. | [optional] |

### Return type

[**IntegrationAccountPartnerListResult**](IntegrationAccountPartnerListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

