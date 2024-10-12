# LabAccountsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**labAccountsCreateLab**](LabAccountsApi.md#labAccountsCreateLab) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/createLab |  |
| [**labAccountsCreateOrUpdate**](LabAccountsApi.md#labAccountsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName} |  |
| [**labAccountsDelete**](LabAccountsApi.md#labAccountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName} |  |
| [**labAccountsGet**](LabAccountsApi.md#labAccountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName} |  |
| [**labAccountsGetRegionalAvailability**](LabAccountsApi.md#labAccountsGetRegionalAvailability) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/getRegionalAvailability |  |
| [**labAccountsListByResourceGroup**](LabAccountsApi.md#labAccountsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts |  |
| [**labAccountsListBySubscription**](LabAccountsApi.md#labAccountsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.LabServices/labaccounts |  |
| [**labAccountsUpdate**](LabAccountsApi.md#labAccountsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName} |  |


<a id="labAccountsCreateLab"></a>
# **labAccountsCreateLab**
> labAccountsCreateLab(subscriptionId, resourceGroupName, labAccountName, apiVersion, createLabProperties)



Create a lab in a lab account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LabAccountsApi apiInstance = new LabAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String apiVersion = "2018-10-15"; // String | Client API version.
    CreateLabProperties createLabProperties = new CreateLabProperties(); // CreateLabProperties | Properties for creating a managed lab and a default environment setting
    try {
      apiInstance.labAccountsCreateLab(subscriptionId, resourceGroupName, labAccountName, apiVersion, createLabProperties);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabAccountsApi#labAccountsCreateLab");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **createLabProperties** | [**CreateLabProperties**](CreateLabProperties.md)| Properties for creating a managed lab and a default environment setting | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="labAccountsCreateOrUpdate"></a>
# **labAccountsCreateOrUpdate**
> LabAccount labAccountsCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, apiVersion, labAccount)



Create or replace an existing Lab Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LabAccountsApi apiInstance = new LabAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String apiVersion = "2018-10-15"; // String | Client API version.
    LabAccount labAccount = new LabAccount(); // LabAccount | Represents a lab account.
    try {
      LabAccount result = apiInstance.labAccountsCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, apiVersion, labAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabAccountsApi#labAccountsCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **labAccount** | [**LabAccount**](LabAccount.md)| Represents a lab account. | |

### Return type

[**LabAccount**](LabAccount.md)

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
| **0** | BadRequest |  -  |

<a id="labAccountsDelete"></a>
# **labAccountsDelete**
> labAccountsDelete(subscriptionId, resourceGroupName, labAccountName, apiVersion)



Delete lab account. This operation can take a while to complete

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LabAccountsApi apiInstance = new LabAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String apiVersion = "2018-10-15"; // String | Client API version.
    try {
      apiInstance.labAccountsDelete(subscriptionId, resourceGroupName, labAccountName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabAccountsApi#labAccountsDelete");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |

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
| **202** | Accepted |  -  |
| **204** | No Content |  -  |
| **0** | BadRequest |  -  |

<a id="labAccountsGet"></a>
# **labAccountsGet**
> LabAccount labAccountsGet(subscriptionId, resourceGroupName, labAccountName, apiVersion, $expand)



Get lab account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LabAccountsApi apiInstance = new LabAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String apiVersion = "2018-10-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($expand=sizeConfiguration)'
    try {
      LabAccount result = apiInstance.labAccountsGet(subscriptionId, resourceGroupName, labAccountName, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabAccountsApi#labAccountsGet");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($expand&#x3D;sizeConfiguration)&#39; | [optional] |

### Return type

[**LabAccount**](LabAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="labAccountsGetRegionalAvailability"></a>
# **labAccountsGetRegionalAvailability**
> GetRegionalAvailabilityResponse labAccountsGetRegionalAvailability(subscriptionId, resourceGroupName, labAccountName, apiVersion)



Get regional availability information for each size category configured under a lab account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LabAccountsApi apiInstance = new LabAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String apiVersion = "2018-10-15"; // String | Client API version.
    try {
      GetRegionalAvailabilityResponse result = apiInstance.labAccountsGetRegionalAvailability(subscriptionId, resourceGroupName, labAccountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabAccountsApi#labAccountsGetRegionalAvailability");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |

### Return type

[**GetRegionalAvailabilityResponse**](GetRegionalAvailabilityResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="labAccountsListByResourceGroup"></a>
# **labAccountsListByResourceGroup**
> ResponseWithContinuationLabAccount labAccountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $expand, $filter, $top, $orderby)



List lab accounts in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LabAccountsApi apiInstance = new LabAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "2018-10-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($expand=sizeConfiguration)'
    String $filter = "$filter_example"; // String | The filter to apply to the operation.
    Integer $top = 56; // Integer | The maximum number of resources to return from the operation.
    String $orderby = "$orderby_example"; // String | The ordering expression for the results, using OData notation.
    try {
      ResponseWithContinuationLabAccount result = apiInstance.labAccountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $expand, $filter, $top, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabAccountsApi#labAccountsListByResourceGroup");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($expand&#x3D;sizeConfiguration)&#39; | [optional] |
| **$filter** | **String**| The filter to apply to the operation. | [optional] |
| **$top** | **Integer**| The maximum number of resources to return from the operation. | [optional] |
| **$orderby** | **String**| The ordering expression for the results, using OData notation. | [optional] |

### Return type

[**ResponseWithContinuationLabAccount**](ResponseWithContinuationLabAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="labAccountsListBySubscription"></a>
# **labAccountsListBySubscription**
> ResponseWithContinuationLabAccount labAccountsListBySubscription(subscriptionId, apiVersion, $expand, $filter, $top, $orderby)



List lab accounts in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LabAccountsApi apiInstance = new LabAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String apiVersion = "2018-10-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($expand=sizeConfiguration)'
    String $filter = "$filter_example"; // String | The filter to apply to the operation.
    Integer $top = 56; // Integer | The maximum number of resources to return from the operation.
    String $orderby = "$orderby_example"; // String | The ordering expression for the results, using OData notation.
    try {
      ResponseWithContinuationLabAccount result = apiInstance.labAccountsListBySubscription(subscriptionId, apiVersion, $expand, $filter, $top, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabAccountsApi#labAccountsListBySubscription");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($expand&#x3D;sizeConfiguration)&#39; | [optional] |
| **$filter** | **String**| The filter to apply to the operation. | [optional] |
| **$top** | **Integer**| The maximum number of resources to return from the operation. | [optional] |
| **$orderby** | **String**| The ordering expression for the results, using OData notation. | [optional] |

### Return type

[**ResponseWithContinuationLabAccount**](ResponseWithContinuationLabAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="labAccountsUpdate"></a>
# **labAccountsUpdate**
> LabAccount labAccountsUpdate(subscriptionId, resourceGroupName, labAccountName, apiVersion, labAccount)



Modify properties of lab accounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LabAccountsApi apiInstance = new LabAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String apiVersion = "2018-10-15"; // String | Client API version.
    LabAccountFragment labAccount = new LabAccountFragment(); // LabAccountFragment | Represents a lab account.
    try {
      LabAccount result = apiInstance.labAccountsUpdate(subscriptionId, resourceGroupName, labAccountName, apiVersion, labAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabAccountsApi#labAccountsUpdate");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **labAccount** | [**LabAccountFragment**](LabAccountFragment.md)| Represents a lab account. | |

### Return type

[**LabAccount**](LabAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

