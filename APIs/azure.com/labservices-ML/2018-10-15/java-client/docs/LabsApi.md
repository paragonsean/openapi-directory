# LabsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**labsAddUsers**](LabsApi.md#labsAddUsers) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/addUsers |  |
| [**labsCreateOrUpdate**](LabsApi.md#labsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName} |  |
| [**labsDelete**](LabsApi.md#labsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName} |  |
| [**labsGet**](LabsApi.md#labsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName} |  |
| [**labsList**](LabsApi.md#labsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs |  |
| [**labsRegister**](LabsApi.md#labsRegister) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/register |  |
| [**labsUpdate**](LabsApi.md#labsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName} |  |


<a id="labsAddUsers"></a>
# **labsAddUsers**
> labsAddUsers(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, addUsersPayload)



Add users to a lab

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LabsApi apiInstance = new LabsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String apiVersion = "2018-10-15"; // String | Client API version.
    AddUsersPayload addUsersPayload = new AddUsersPayload(); // AddUsersPayload | Payload for Add Users operation on a Lab.
    try {
      apiInstance.labsAddUsers(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, addUsersPayload);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabsApi#labsAddUsers");
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
| **labName** | **String**| The name of the lab. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **addUsersPayload** | [**AddUsersPayload**](AddUsersPayload.md)| Payload for Add Users operation on a Lab. | |

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

<a id="labsCreateOrUpdate"></a>
# **labsCreateOrUpdate**
> Lab labsCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, lab)



Create or replace an existing Lab.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LabsApi apiInstance = new LabsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String apiVersion = "2018-10-15"; // String | Client API version.
    Lab lab = new Lab(); // Lab | Represents a lab.
    try {
      Lab result = apiInstance.labsCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, lab);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabsApi#labsCreateOrUpdate");
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
| **labName** | **String**| The name of the lab. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **lab** | [**Lab**](Lab.md)| Represents a lab. | |

### Return type

[**Lab**](Lab.md)

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

<a id="labsDelete"></a>
# **labsDelete**
> labsDelete(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion)



Delete lab. This operation can take a while to complete

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LabsApi apiInstance = new LabsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String apiVersion = "2018-10-15"; // String | Client API version.
    try {
      apiInstance.labsDelete(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabsApi#labsDelete");
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
| **labName** | **String**| The name of the lab. | |
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

<a id="labsGet"></a>
# **labsGet**
> Lab labsGet(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, $expand)



Get lab

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LabsApi apiInstance = new LabsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String apiVersion = "2018-10-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($select=maxUsersInLab)'
    try {
      Lab result = apiInstance.labsGet(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabsApi#labsGet");
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
| **labName** | **String**| The name of the lab. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;maxUsersInLab)&#39; | [optional] |

### Return type

[**Lab**](Lab.md)

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

<a id="labsList"></a>
# **labsList**
> ResponseWithContinuationLab labsList(subscriptionId, resourceGroupName, labAccountName, apiVersion, $expand, $filter, $top, $orderby)



List labs in a given lab account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LabsApi apiInstance = new LabsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String apiVersion = "2018-10-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($select=maxUsersInLab)'
    String $filter = "$filter_example"; // String | The filter to apply to the operation.
    Integer $top = 56; // Integer | The maximum number of resources to return from the operation.
    String $orderby = "$orderby_example"; // String | The ordering expression for the results, using OData notation.
    try {
      ResponseWithContinuationLab result = apiInstance.labsList(subscriptionId, resourceGroupName, labAccountName, apiVersion, $expand, $filter, $top, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabsApi#labsList");
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
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;maxUsersInLab)&#39; | [optional] |
| **$filter** | **String**| The filter to apply to the operation. | [optional] |
| **$top** | **Integer**| The maximum number of resources to return from the operation. | [optional] |
| **$orderby** | **String**| The ordering expression for the results, using OData notation. | [optional] |

### Return type

[**ResponseWithContinuationLab**](ResponseWithContinuationLab.md)

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

<a id="labsRegister"></a>
# **labsRegister**
> labsRegister(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion)



Register to managed lab.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LabsApi apiInstance = new LabsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String apiVersion = "2018-10-15"; // String | Client API version.
    try {
      apiInstance.labsRegister(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabsApi#labsRegister");
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
| **labName** | **String**| The name of the lab. | |
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
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="labsUpdate"></a>
# **labsUpdate**
> Lab labsUpdate(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, lab)



Modify properties of labs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LabsApi apiInstance = new LabsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String apiVersion = "2018-10-15"; // String | Client API version.
    LabFragment lab = new LabFragment(); // LabFragment | Represents a lab.
    try {
      Lab result = apiInstance.labsUpdate(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, lab);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabsApi#labsUpdate");
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
| **labName** | **String**| The name of the lab. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **lab** | [**LabFragment**](LabFragment.md)| Represents a lab. | |

### Return type

[**Lab**](Lab.md)

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

