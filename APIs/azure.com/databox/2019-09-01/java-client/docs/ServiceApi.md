# ServiceApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serviceListAvailableSkus**](ServiceApi.md#serviceListAvailableSkus) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DataBox/locations/{location}/availableSkus |  |
| [**serviceListAvailableSkusByResourceGroup**](ServiceApi.md#serviceListAvailableSkusByResourceGroup) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/locations/{location}/availableSkus |  |
| [**serviceRegionConfiguration**](ServiceApi.md#serviceRegionConfiguration) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DataBox/locations/{location}/regionConfiguration |  |
| [**serviceValidateAddress**](ServiceApi.md#serviceValidateAddress) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DataBox/locations/{location}/validateAddress |  |
| [**serviceValidateInputs**](ServiceApi.md#serviceValidateInputs) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DataBox/locations/{location}/validateInputs |  |
| [**serviceValidateInputsByResourceGroup**](ServiceApi.md#serviceValidateInputsByResourceGroup) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBox/locations/{location}/validateInputs |  |


<a id="serviceListAvailableSkus"></a>
# **serviceListAvailableSkus**
> AvailableSkusResult serviceListAvailableSkus(subscriptionId, location, apiVersion, availableSkuRequest)



This method provides the list of available skus for the given subscription and location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceApi apiInstance = new ServiceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String location = "location_example"; // String | The location of the resource
    String apiVersion = "apiVersion_example"; // String | The API Version
    AvailableSkuRequest availableSkuRequest = new AvailableSkuRequest(); // AvailableSkuRequest | Filters for showing the available skus.
    try {
      AvailableSkusResult result = apiInstance.serviceListAvailableSkus(subscriptionId, location, apiVersion, availableSkuRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceApi#serviceListAvailableSkus");
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
| **subscriptionId** | **String**| The Subscription Id | |
| **location** | **String**| The location of the resource | |
| **apiVersion** | **String**| The API Version | |
| **availableSkuRequest** | [**AvailableSkuRequest**](AvailableSkuRequest.md)| Filters for showing the available skus. | |

### Return type

[**AvailableSkusResult**](AvailableSkusResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of available skus under subscription. |  -  |
| **0** | Error response describing reason for operation failure. |  -  |

<a id="serviceListAvailableSkusByResourceGroup"></a>
# **serviceListAvailableSkusByResourceGroup**
> AvailableSkusResult serviceListAvailableSkusByResourceGroup(subscriptionId, resourceGroupName, location, apiVersion, availableSkuRequest)



This method provides the list of available skus for the given subscription, resource group and location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceApi apiInstance = new ServiceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String location = "location_example"; // String | The location of the resource
    String apiVersion = "apiVersion_example"; // String | The API Version
    AvailableSkuRequest availableSkuRequest = new AvailableSkuRequest(); // AvailableSkuRequest | Filters for showing the available skus.
    try {
      AvailableSkusResult result = apiInstance.serviceListAvailableSkusByResourceGroup(subscriptionId, resourceGroupName, location, apiVersion, availableSkuRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceApi#serviceListAvailableSkusByResourceGroup");
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
| **subscriptionId** | **String**| The Subscription Id | |
| **resourceGroupName** | **String**| The Resource Group Name | |
| **location** | **String**| The location of the resource | |
| **apiVersion** | **String**| The API Version | |
| **availableSkuRequest** | [**AvailableSkuRequest**](AvailableSkuRequest.md)| Filters for showing the available skus. | |

### Return type

[**AvailableSkusResult**](AvailableSkusResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of available skus under Resource group. |  -  |
| **0** | Error response describing reason for operation failure. |  -  |

<a id="serviceRegionConfiguration"></a>
# **serviceRegionConfiguration**
> RegionConfigurationResponse serviceRegionConfiguration(subscriptionId, location, apiVersion, regionConfigurationRequest)



This API provides configuration details specific to given region/location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceApi apiInstance = new ServiceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String location = "location_example"; // String | The location of the resource
    String apiVersion = "apiVersion_example"; // String | The API Version
    RegionConfigurationRequest regionConfigurationRequest = new RegionConfigurationRequest(); // RegionConfigurationRequest | Request body to get the configuration for the region.
    try {
      RegionConfigurationResponse result = apiInstance.serviceRegionConfiguration(subscriptionId, location, apiVersion, regionConfigurationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceApi#serviceRegionConfiguration");
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
| **subscriptionId** | **String**| The Subscription Id | |
| **location** | **String**| The location of the resource | |
| **apiVersion** | **String**| The API Version | |
| **regionConfigurationRequest** | [**RegionConfigurationRequest**](RegionConfigurationRequest.md)| Request body to get the configuration for the region. | |

### Return type

[**RegionConfigurationResponse**](RegionConfigurationResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Region configuration response. |  -  |
| **0** | Error response describing reason for operation failure. |  -  |

<a id="serviceValidateAddress"></a>
# **serviceValidateAddress**
> AddressValidationOutput serviceValidateAddress(subscriptionId, location, apiVersion, validateAddress)



[DEPRECATED NOTICE: This operation will soon be removed] This method validates the customer shipping address and provide alternate addresses if any.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceApi apiInstance = new ServiceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String location = "location_example"; // String | The location of the resource
    String apiVersion = "apiVersion_example"; // String | The API Version
    ValidateAddress validateAddress = new ValidateAddress(); // ValidateAddress | Shipping address of the customer.
    try {
      AddressValidationOutput result = apiInstance.serviceValidateAddress(subscriptionId, location, apiVersion, validateAddress);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceApi#serviceValidateAddress");
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
| **subscriptionId** | **String**| The Subscription Id | |
| **location** | **String**| The location of the resource | |
| **apiVersion** | **String**| The API Version | |
| **validateAddress** | [**ValidateAddress**](ValidateAddress.md)| Shipping address of the customer. | |

### Return type

[**AddressValidationOutput**](AddressValidationOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The valid and alternate addresses. |  -  |
| **0** | Error response describing reason for operation failure. |  -  |

<a id="serviceValidateInputs"></a>
# **serviceValidateInputs**
> ValidationResponse serviceValidateInputs(subscriptionId, location, apiVersion, validationRequest)



This method does all necessary pre-job creation validation under subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceApi apiInstance = new ServiceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String location = "location_example"; // String | The location of the resource
    String apiVersion = "apiVersion_example"; // String | The API Version
    ValidationRequest validationRequest = new ValidationRequest(); // ValidationRequest | Inputs of the customer.
    try {
      ValidationResponse result = apiInstance.serviceValidateInputs(subscriptionId, location, apiVersion, validationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceApi#serviceValidateInputs");
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
| **subscriptionId** | **String**| The Subscription Id | |
| **location** | **String**| The location of the resource | |
| **apiVersion** | **String**| The API Version | |
| **validationRequest** | [**ValidationRequest**](ValidationRequest.md)| Inputs of the customer. | |

### Return type

[**ValidationResponse**](ValidationResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The validation status and responses of each validating parameter. |  -  |
| **0** | Error response describing reason for operation failure. |  -  |

<a id="serviceValidateInputsByResourceGroup"></a>
# **serviceValidateInputsByResourceGroup**
> ValidationResponse serviceValidateInputsByResourceGroup(subscriptionId, resourceGroupName, location, apiVersion, validationRequest)



This method does all necessary pre-job creation validation under resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceApi apiInstance = new ServiceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String location = "location_example"; // String | The location of the resource
    String apiVersion = "apiVersion_example"; // String | The API Version
    ValidationRequest validationRequest = new ValidationRequest(); // ValidationRequest | Inputs of the customer.
    try {
      ValidationResponse result = apiInstance.serviceValidateInputsByResourceGroup(subscriptionId, resourceGroupName, location, apiVersion, validationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceApi#serviceValidateInputsByResourceGroup");
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
| **subscriptionId** | **String**| The Subscription Id | |
| **resourceGroupName** | **String**| The Resource Group Name | |
| **location** | **String**| The location of the resource | |
| **apiVersion** | **String**| The API Version | |
| **validationRequest** | [**ValidationRequest**](ValidationRequest.md)| Inputs of the customer. | |

### Return type

[**ValidationResponse**](ValidationResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The validation status and responses of each validating parameter. |  -  |
| **0** | Error response describing reason for operation failure. |  -  |

