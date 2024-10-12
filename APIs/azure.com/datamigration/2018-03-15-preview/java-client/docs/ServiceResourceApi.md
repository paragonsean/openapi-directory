# ServiceResourceApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**servicesCheckStatus**](ServiceResourceApi.md#servicesCheckStatus) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/checkStatus | Check service health status |
| [**servicesCreateOrUpdate**](ServiceResourceApi.md#servicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName} | Create or update DMS Instance |
| [**servicesDelete**](ServiceResourceApi.md#servicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName} | Delete DMS Service Instance |
| [**servicesGet**](ServiceResourceApi.md#servicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName} | Get DMS Service Instance |
| [**servicesList**](ServiceResourceApi.md#servicesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DataMigration/services | Get services in subscription |
| [**servicesListByResourceGroup**](ServiceResourceApi.md#servicesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services | Get services in resource group |
| [**servicesListSkus**](ServiceResourceApi.md#servicesListSkus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/skus | Get compatible SKUs |
| [**servicesStart**](ServiceResourceApi.md#servicesStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/start | Start service |
| [**servicesStop**](ServiceResourceApi.md#servicesStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/stop | Stop service |
| [**servicesUpdate**](ServiceResourceApi.md#servicesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName} | Create or update DMS Service Instance |
| [**tasksList**](ServiceResourceApi.md#tasksList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks | Get tasks in a service |


<a id="servicesCheckStatus"></a>
# **servicesCheckStatus**
> ServicesCheckStatus200Response servicesCheckStatus(subscriptionId, groupName, serviceName, apiVersion)

Check service health status

The services resource is the top-level resource that represents the Data Migration Service. This action performs a health check and returns the status of the service and virtual machine size.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceResourceApi apiInstance = new ServiceResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String apiVersion = "apiVersion_example"; // String | Version of the API
    try {
      ServicesCheckStatus200Response result = apiInstance.servicesCheckStatus(subscriptionId, groupName, serviceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceResourceApi#servicesCheckStatus");
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
| **subscriptionId** | **String**| Identifier of the subscription | |
| **groupName** | **String**| Name of the resource group | |
| **serviceName** | **String**| Name of the service | |
| **apiVersion** | **String**| Version of the API | |

### Return type

[**ServicesCheckStatus200Response**](ServicesCheckStatus200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Health checked |  -  |
| **0** | Error |  -  |

<a id="servicesCreateOrUpdate"></a>
# **servicesCreateOrUpdate**
> ServicesGet200Response servicesCreateOrUpdate(subscriptionId, groupName, serviceName, apiVersion, parameters)

Create or update DMS Instance

The services resource is the top-level resource that represents the Data Migration Service. The PUT method creates a new service or updates an existing one. When a service is updated, existing child resources (i.e. tasks) are unaffected. Services currently support a single kind, \&quot;vm\&quot;, which refers to a VM-based service, although other kinds may be added in the future. This method can change the kind, SKU, and network of the service, but if tasks are currently running (i.e. the service is busy), this will fail with 400 Bad Request (\&quot;ServiceIsBusy\&quot;). The provider will reply when successful with 200 OK or 201 Created. Long-running operations use the provisioningState property.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceResourceApi apiInstance = new ServiceResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String apiVersion = "apiVersion_example"; // String | Version of the API
    ServicesGet200Response parameters = new ServicesGet200Response(); // ServicesGet200Response | Information about the service
    try {
      ServicesGet200Response result = apiInstance.servicesCreateOrUpdate(subscriptionId, groupName, serviceName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceResourceApi#servicesCreateOrUpdate");
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
| **subscriptionId** | **String**| Identifier of the subscription | |
| **groupName** | **String**| Name of the resource group | |
| **serviceName** | **String**| Name of the service | |
| **apiVersion** | **String**| Version of the API | |
| **parameters** | [**ServicesGet200Response**](ServicesGet200Response.md)| Information about the service | |

### Return type

[**ServicesGet200Response**](ServicesGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service updated |  -  |
| **201** | Service created (use provisioningState) |  -  |
| **202** | Update accepted |  -  |
| **0** | Error |  -  |

<a id="servicesDelete"></a>
# **servicesDelete**
> servicesDelete(subscriptionId, groupName, serviceName, apiVersion, deleteRunningTasks)

Delete DMS Service Instance

The services resource is the top-level resource that represents the Data Migration Service. The DELETE method deletes a service. Any running tasks will be canceled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceResourceApi apiInstance = new ServiceResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String apiVersion = "apiVersion_example"; // String | Version of the API
    Boolean deleteRunningTasks = true; // Boolean | Delete the resource even if it contains running tasks
    try {
      apiInstance.servicesDelete(subscriptionId, groupName, serviceName, apiVersion, deleteRunningTasks);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceResourceApi#servicesDelete");
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
| **subscriptionId** | **String**| Identifier of the subscription | |
| **groupName** | **String**| Name of the resource group | |
| **serviceName** | **String**| Name of the service | |
| **apiVersion** | **String**| Version of the API | |
| **deleteRunningTasks** | **Boolean**| Delete the resource even if it contains running tasks | [optional] |

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
| **200** | Service resource deleted |  -  |
| **202** | Deletion accepted |  -  |
| **204** | Service not found |  -  |
| **0** | Error |  -  |

<a id="servicesGet"></a>
# **servicesGet**
> ServicesGet200Response servicesGet(subscriptionId, groupName, serviceName, apiVersion)

Get DMS Service Instance

The services resource is the top-level resource that represents the Data Migration Service. The GET method retrieves information about a service instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceResourceApi apiInstance = new ServiceResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String apiVersion = "apiVersion_example"; // String | Version of the API
    try {
      ServicesGet200Response result = apiInstance.servicesGet(subscriptionId, groupName, serviceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceResourceApi#servicesGet");
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
| **subscriptionId** | **String**| Identifier of the subscription | |
| **groupName** | **String**| Name of the resource group | |
| **serviceName** | **String**| Name of the service | |
| **apiVersion** | **String**| Version of the API | |

### Return type

[**ServicesGet200Response**](ServicesGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A service instance resource |  -  |
| **0** | Error |  -  |

<a id="servicesList"></a>
# **servicesList**
> ServicesList200Response servicesList(subscriptionId, apiVersion)

Get services in subscription

The services resource is the top-level resource that represents the Data Migration Service. This method returns a list of service resources in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceResourceApi apiInstance = new ServiceResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String apiVersion = "apiVersion_example"; // String | Version of the API
    try {
      ServicesList200Response result = apiInstance.servicesList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceResourceApi#servicesList");
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
| **subscriptionId** | **String**| Identifier of the subscription | |
| **apiVersion** | **String**| Version of the API | |

### Return type

[**ServicesList200Response**](ServicesList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Got services |  -  |
| **0** | Error |  -  |

<a id="servicesListByResourceGroup"></a>
# **servicesListByResourceGroup**
> ServicesList200Response servicesListByResourceGroup(subscriptionId, groupName, apiVersion)

Get services in resource group

The Services resource is the top-level resource that represents the Data Migration Service. This method returns a list of service resources in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceResourceApi apiInstance = new ServiceResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String apiVersion = "apiVersion_example"; // String | Version of the API
    try {
      ServicesList200Response result = apiInstance.servicesListByResourceGroup(subscriptionId, groupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceResourceApi#servicesListByResourceGroup");
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
| **subscriptionId** | **String**| Identifier of the subscription | |
| **groupName** | **String**| Name of the resource group | |
| **apiVersion** | **String**| Version of the API | |

### Return type

[**ServicesList200Response**](ServicesList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Got services |  -  |
| **0** | Error |  -  |

<a id="servicesListSkus"></a>
# **servicesListSkus**
> ServicesListSkus200Response servicesListSkus(subscriptionId, groupName, serviceName, apiVersion)

Get compatible SKUs

The services resource is the top-level resource that represents the Data Migration Service. The skus action returns the list of SKUs that a service resource can be updated to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceResourceApi apiInstance = new ServiceResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String apiVersion = "apiVersion_example"; // String | Version of the API
    try {
      ServicesListSkus200Response result = apiInstance.servicesListSkus(subscriptionId, groupName, serviceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceResourceApi#servicesListSkus");
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
| **subscriptionId** | **String**| Identifier of the subscription | |
| **groupName** | **String**| Name of the resource group | |
| **serviceName** | **String**| Name of the service | |
| **apiVersion** | **String**| Version of the API | |

### Return type

[**ServicesListSkus200Response**](ServicesListSkus200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Got SKUs |  -  |
| **0** | Error |  -  |

<a id="servicesStart"></a>
# **servicesStart**
> servicesStart(subscriptionId, groupName, serviceName, apiVersion)

Start service

The services resource is the top-level resource that represents the Data Migration Service. This action starts the service and the service can be used for data migration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceResourceApi apiInstance = new ServiceResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String apiVersion = "apiVersion_example"; // String | Version of the API
    try {
      apiInstance.servicesStart(subscriptionId, groupName, serviceName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceResourceApi#servicesStart");
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
| **subscriptionId** | **String**| Identifier of the subscription | |
| **groupName** | **String**| Name of the resource group | |
| **serviceName** | **String**| Name of the service | |
| **apiVersion** | **String**| Version of the API | |

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
| **200** | The service has already been started. |  -  |
| **202** | The request to start service is accepted. |  -  |
| **0** | Error |  -  |

<a id="servicesStop"></a>
# **servicesStop**
> servicesStop(subscriptionId, groupName, serviceName, apiVersion)

Stop service

The services resource is the top-level resource that represents the Data Migration Service. This action stops the service and the service cannot be used for data migration. The service owner won&#39;t be billed when the service is stopped.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceResourceApi apiInstance = new ServiceResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String apiVersion = "apiVersion_example"; // String | Version of the API
    try {
      apiInstance.servicesStop(subscriptionId, groupName, serviceName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceResourceApi#servicesStop");
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
| **subscriptionId** | **String**| Identifier of the subscription | |
| **groupName** | **String**| Name of the resource group | |
| **serviceName** | **String**| Name of the service | |
| **apiVersion** | **String**| Version of the API | |

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
| **200** | The service has already been stopped. |  -  |
| **202** | The request to stop service is accepted. |  -  |
| **0** | Error |  -  |

<a id="servicesUpdate"></a>
# **servicesUpdate**
> ServicesGet200Response servicesUpdate(subscriptionId, groupName, serviceName, apiVersion, parameters)

Create or update DMS Service Instance

The services resource is the top-level resource that represents the Data Migration Service. The PATCH method updates an existing service. This method can change the kind, SKU, and network of the service, but if tasks are currently running (i.e. the service is busy), this will fail with 400 Bad Request (\&quot;ServiceIsBusy\&quot;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceResourceApi apiInstance = new ServiceResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String apiVersion = "apiVersion_example"; // String | Version of the API
    ServicesGet200Response parameters = new ServicesGet200Response(); // ServicesGet200Response | Information about the service
    try {
      ServicesGet200Response result = apiInstance.servicesUpdate(subscriptionId, groupName, serviceName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceResourceApi#servicesUpdate");
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
| **subscriptionId** | **String**| Identifier of the subscription | |
| **groupName** | **String**| Name of the resource group | |
| **serviceName** | **String**| Name of the service | |
| **apiVersion** | **String**| Version of the API | |
| **parameters** | [**ServicesGet200Response**](ServicesGet200Response.md)| Information about the service | |

### Return type

[**ServicesGet200Response**](ServicesGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service resource updated |  -  |
| **202** | Update accepted |  -  |
| **0** | Error |  -  |

<a id="tasksList"></a>
# **tasksList**
> TasksList200Response tasksList(subscriptionId, groupName, serviceName, projectName, apiVersion, taskType)

Get tasks in a service

The services resource is the top-level resource that represents the Data Migration Service. This method returns a list of tasks owned by a service resource. Some tasks may have a status of Unknown, which indicates that an error occurred while querying the status of that task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceResourceApi apiInstance = new ServiceResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
    String groupName = "groupName_example"; // String | Name of the resource group
    String serviceName = "serviceName_example"; // String | Name of the service
    String projectName = "projectName_example"; // String | Name of the project
    String apiVersion = "apiVersion_example"; // String | Version of the API
    String taskType = "taskType_example"; // String | Filter tasks by task type
    try {
      TasksList200Response result = apiInstance.tasksList(subscriptionId, groupName, serviceName, projectName, apiVersion, taskType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceResourceApi#tasksList");
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
| **subscriptionId** | **String**| Identifier of the subscription | |
| **groupName** | **String**| Name of the resource group | |
| **serviceName** | **String**| Name of the service | |
| **projectName** | **String**| Name of the project | |
| **apiVersion** | **String**| Version of the API | |
| **taskType** | **String**| Filter tasks by task type | [optional] |

### Return type

[**TasksList200Response**](TasksList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Got tasks |  -  |
| **0** | Error |  -  |

