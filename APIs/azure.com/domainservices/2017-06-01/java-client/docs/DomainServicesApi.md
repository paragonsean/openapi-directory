# DomainServicesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**domainServiceOperationsList**](DomainServicesApi.md#domainServiceOperationsList) | **GET** /providers/Microsoft.AAD/operations |  |
| [**domainServicesCreateOrUpdate**](DomainServicesApi.md#domainServicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AAD/domainServices/{domainServiceName} | Create or Update Domain Service (PUT Resource) |
| [**domainServicesDelete**](DomainServicesApi.md#domainServicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AAD/domainServices/{domainServiceName} | Delete Domain Service (DELETE Resource) |
| [**domainServicesGet**](DomainServicesApi.md#domainServicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AAD/domainServices/{domainServiceName} | Get Domain Service |
| [**domainServicesList**](DomainServicesApi.md#domainServicesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AAD/domainServices | List Domain Services in Subscription |
| [**domainServicesListByResourceGroup**](DomainServicesApi.md#domainServicesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AAD/domainServices | List Domain Services in Resource Group |
| [**domainServicesUpdate**](DomainServicesApi.md#domainServicesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AAD/domainServices/{domainServiceName} | Update Domain Service (PATCH Resource) |


<a id="domainServiceOperationsList"></a>
# **domainServiceOperationsList**
> OperationEntityListResult domainServiceOperationsList(apiVersion)



Lists all the available Domain Services operations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DomainServicesApi apiInstance = new DomainServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      OperationEntityListResult result = apiInstance.domainServiceOperationsList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainServicesApi#domainServiceOperationsList");
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
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**OperationEntityListResult**](OperationEntityListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | HTTP 200 (OK) if the operation was successful. |  -  |

<a id="domainServicesCreateOrUpdate"></a>
# **domainServicesCreateOrUpdate**
> DomainService domainServicesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, domainServiceName, domainService)

Create or Update Domain Service (PUT Resource)

The Create Domain Service operation creates a new domain service with the specified parameters. If the specific service already exists, then any patchable properties will be updated and any immutable properties will remain unchanged.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DomainServicesApi apiInstance = new DomainServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String domainServiceName = "domainServiceName_example"; // String | The name of the domain service.
    DomainService domainService = new DomainService(); // DomainService | Properties supplied to the Create or Update a Domain Service operation.
    try {
      DomainService result = apiInstance.domainServicesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, domainServiceName, domainService);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainServicesApi#domainServicesCreateOrUpdate");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **domainServiceName** | **String**| The name of the domain service. | |
| **domainService** | [**DomainService**](DomainService.md)| Properties supplied to the Create or Update a Domain Service operation. | |

### Return type

[**DomainService**](DomainService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | HTTP 200 (OK) if the operation was successful. |  -  |
| **201** | HTTP 201 (Created) if the operation completed successfully. |  -  |
| **202** | HTTP 202 (Accepted) if the operation was successfully started and will complete asynchronously. |  -  |

<a id="domainServicesDelete"></a>
# **domainServicesDelete**
> domainServicesDelete(apiVersion, subscriptionId, resourceGroupName, domainServiceName)

Delete Domain Service (DELETE Resource)

The Delete Domain Service operation deletes an existing Domain Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DomainServicesApi apiInstance = new DomainServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String domainServiceName = "domainServiceName_example"; // String | The name of the domain service.
    try {
      apiInstance.domainServicesDelete(apiVersion, subscriptionId, resourceGroupName, domainServiceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainServicesApi#domainServicesDelete");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **domainServiceName** | **String**| The name of the domain service. | |

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
| **202** | HTTP 202 (Accepted) if the operation was successfully started and will complete asynchronously. |  -  |
| **204** | HTTP 204 (Not Content) should be used if the resource does not exist and the request is well formed. |  -  |

<a id="domainServicesGet"></a>
# **domainServicesGet**
> DomainService domainServicesGet(apiVersion, subscriptionId, resourceGroupName, domainServiceName)

Get Domain Service

The Get Domain Service operation retrieves a json representation of the Domain Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DomainServicesApi apiInstance = new DomainServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String domainServiceName = "domainServiceName_example"; // String | The name of the domain service.
    try {
      DomainService result = apiInstance.domainServicesGet(apiVersion, subscriptionId, resourceGroupName, domainServiceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainServicesApi#domainServicesGet");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **domainServiceName** | **String**| The name of the domain service. | |

### Return type

[**DomainService**](DomainService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | HTTP 200 (OK) if the operation was successful. |  -  |

<a id="domainServicesList"></a>
# **domainServicesList**
> DomainServiceListResult domainServicesList(apiVersion, subscriptionId)

List Domain Services in Subscription

The List Domain Services in Subscription operation lists all the domain services available under the given subscription (and across all resource groups within that subscription).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DomainServicesApi apiInstance = new DomainServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      DomainServiceListResult result = apiInstance.domainServicesList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainServicesApi#domainServicesList");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**DomainServiceListResult**](DomainServiceListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | HTTP 200 (OK) if the operation was successful. |  -  |

<a id="domainServicesListByResourceGroup"></a>
# **domainServicesListByResourceGroup**
> DomainServiceListResult domainServicesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)

List Domain Services in Resource Group

The List Domain Services in Resource Group operation lists all the domain services available under the given resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DomainServicesApi apiInstance = new DomainServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    try {
      DomainServiceListResult result = apiInstance.domainServicesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainServicesApi#domainServicesListByResourceGroup");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |

### Return type

[**DomainServiceListResult**](DomainServiceListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | HTTP 200 (OK) if the operation was successful. |  -  |

<a id="domainServicesUpdate"></a>
# **domainServicesUpdate**
> DomainService domainServicesUpdate(apiVersion, subscriptionId, resourceGroupName, domainServiceName, domainService)

Update Domain Service (PATCH Resource)

The Update Domain Service operation can be used to update the existing deployment. The update call only supports the properties listed in the PATCH body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DomainServicesApi apiInstance = new DomainServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String domainServiceName = "domainServiceName_example"; // String | The name of the domain service.
    DomainService domainService = new DomainService(); // DomainService | Properties supplied to the Update a Domain Service operation.
    try {
      DomainService result = apiInstance.domainServicesUpdate(apiVersion, subscriptionId, resourceGroupName, domainServiceName, domainService);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainServicesApi#domainServicesUpdate");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **domainServiceName** | **String**| The name of the domain service. | |
| **domainService** | [**DomainService**](DomainService.md)| Properties supplied to the Update a Domain Service operation. | |

### Return type

[**DomainService**](DomainService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | HTTP 200 (OK) if the operation was successful. |  -  |
| **202** | HTTP 202 (Accepted) if the operation was successfully started and will complete asynchronously. |  -  |

