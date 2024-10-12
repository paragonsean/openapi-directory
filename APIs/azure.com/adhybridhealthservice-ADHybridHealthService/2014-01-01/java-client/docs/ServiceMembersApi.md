# ServiceMembersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serviceMembersAdd**](ServiceMembersApi.md#serviceMembersAdd) | **POST** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers |  |
| [**serviceMembersDelete**](ServiceMembersApi.md#serviceMembersDelete) | **DELETE** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId} |  |
| [**serviceMembersDeleteData**](ServiceMembersApi.md#serviceMembersDeleteData) | **DELETE** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId}/data |  |
| [**serviceMembersGet**](ServiceMembersApi.md#serviceMembersGet) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId} |  |
| [**serviceMembersGetServiceConfiguration**](ServiceMembersApi.md#serviceMembersGetServiceConfiguration) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId}/serviceconfiguration |  |
| [**serviceMembersList**](ServiceMembersApi.md#serviceMembersList) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers |  |
| [**serviceMembersListConnectors**](ServiceMembersApi.md#serviceMembersListConnectors) | **GET** /providers/Microsoft.ADHybridHealthService/service/{serviceName}/servicemembers/{serviceMemberId}/connectors |  |
| [**serviceMembersListCredentials**](ServiceMembersApi.md#serviceMembersListCredentials) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId}/credentials |  |
| [**serviceMembersListDataFreshness**](ServiceMembersApi.md#serviceMembersListDataFreshness) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId}/datafreshness |  |
| [**serviceMembersListExportStatus**](ServiceMembersApi.md#serviceMembersListExportStatus) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId}/exportstatus |  |
| [**serviceMembersListGlobalConfiguration**](ServiceMembersApi.md#serviceMembersListGlobalConfiguration) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId}/globalconfiguration |  |


<a id="serviceMembersAdd"></a>
# **serviceMembersAdd**
> ServiceMember serviceMembersAdd(serviceName, apiVersion, serviceMember)



Onboards  a server, for a given service, to Azure Active Directory Connect Health Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceMembersApi apiInstance = new ServiceMembersApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service under which the server is to be onboarded.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    ServiceMember serviceMember = new ServiceMember(); // ServiceMember | The server object.
    try {
      ServiceMember result = apiInstance.serviceMembersAdd(serviceName, apiVersion, serviceMember);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceMembersApi#serviceMembersAdd");
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
| **serviceName** | **String**| The name of the service under which the server is to be onboarded. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **serviceMember** | [**ServiceMember**](ServiceMember.md)| The server object. | |

### Return type

[**ServiceMember**](ServiceMember.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully added the service member. |  -  |

<a id="serviceMembersDelete"></a>
# **serviceMembersDelete**
> serviceMembersDelete(serviceName, serviceMemberId, apiVersion, confirm)



Deletes a server that has been onboarded to Azure Active Directory Connect Health Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceMembersApi apiInstance = new ServiceMembersApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    UUID serviceMemberId = UUID.randomUUID(); // UUID | The server Id.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    Boolean confirm = true; // Boolean | Indicates if the server will be permanently deleted or disabled. True indicates that the server will be permanently deleted and False indicates that the server will be marked disabled and then deleted after 30 days, if it is not re-registered.
    try {
      apiInstance.serviceMembersDelete(serviceName, serviceMemberId, apiVersion, confirm);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceMembersApi#serviceMembersDelete");
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
| **serviceName** | **String**| The name of the service. | |
| **serviceMemberId** | **UUID**| The server Id. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **confirm** | **Boolean**| Indicates if the server will be permanently deleted or disabled. True indicates that the server will be permanently deleted and False indicates that the server will be marked disabled and then deleted after 30 days, if it is not re-registered. | [optional] |

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
| **200** | Successfully deleted the service member. |  -  |

<a id="serviceMembersDeleteData"></a>
# **serviceMembersDeleteData**
> serviceMembersDeleteData(serviceName, serviceMemberId, apiVersion)



Deletes the data uploaded by the server to Azure Active Directory Connect Health Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceMembersApi apiInstance = new ServiceMembersApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    UUID serviceMemberId = UUID.randomUUID(); // UUID | The server Id.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      apiInstance.serviceMembersDeleteData(serviceName, serviceMemberId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceMembersApi#serviceMembersDeleteData");
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
| **serviceName** | **String**| The name of the service. | |
| **serviceMemberId** | **UUID**| The server Id. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

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
| **200** | Successfully deleted the service member. |  -  |

<a id="serviceMembersGet"></a>
# **serviceMembersGet**
> ServiceMember serviceMembersGet(serviceName, serviceMemberId, apiVersion)



Gets the details of a server, for a given service, that are onboarded to Azure Active Directory Connect Health Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceMembersApi apiInstance = new ServiceMembersApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    UUID serviceMemberId = UUID.randomUUID(); // UUID | The server Id.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      ServiceMember result = apiInstance.serviceMembersGet(serviceName, serviceMemberId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceMembersApi#serviceMembersGet");
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
| **serviceName** | **String**| The name of the service. | |
| **serviceMemberId** | **UUID**| The server Id. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**ServiceMember**](ServiceMember.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specific service member. |  -  |

<a id="serviceMembersGetServiceConfiguration"></a>
# **serviceMembersGetServiceConfiguration**
> ServiceConfiguration serviceMembersGetServiceConfiguration(serviceName, serviceMemberId, apiVersion)



Gets the service configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceMembersApi apiInstance = new ServiceMembersApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String serviceMemberId = "serviceMemberId_example"; // String | The server Id.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      ServiceConfiguration result = apiInstance.serviceMembersGetServiceConfiguration(serviceName, serviceMemberId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceMembersApi#serviceMembersGetServiceConfiguration");
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
| **serviceName** | **String**| The name of the service. | |
| **serviceMemberId** | **String**| The server Id. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**ServiceConfiguration**](ServiceConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service configuration. |  -  |

<a id="serviceMembersList"></a>
# **serviceMembersList**
> ServiceMembers serviceMembersList(serviceName, apiVersion, $filter, dimensionType, dimensionSignature)



Gets the details of the servers, for a given service, that are onboarded to Azure Active Directory Connect Health Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceMembersApi apiInstance = new ServiceMembersApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | The server property filter to apply.
    String dimensionType = "dimensionType_example"; // String | The server specific dimension.
    String dimensionSignature = "dimensionSignature_example"; // String | The value of the dimension.
    try {
      ServiceMembers result = apiInstance.serviceMembersList(serviceName, apiVersion, $filter, dimensionType, dimensionSignature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceMembersApi#serviceMembersList");
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
| **serviceName** | **String**| The name of the service. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **$filter** | **String**| The server property filter to apply. | [optional] |
| **dimensionType** | **String**| The server specific dimension. | [optional] |
| **dimensionSignature** | **String**| The value of the dimension. | [optional] |

### Return type

[**ServiceMembers**](ServiceMembers.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of service members. |  -  |

<a id="serviceMembersListConnectors"></a>
# **serviceMembersListConnectors**
> Connectors serviceMembersListConnectors(serviceName, serviceMemberId, apiVersion)



Gets the connector details for a service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceMembersApi apiInstance = new ServiceMembersApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    UUID serviceMemberId = UUID.randomUUID(); // UUID | The server Id.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      Connectors result = apiInstance.serviceMembersListConnectors(serviceName, serviceMemberId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceMembersApi#serviceMembersListConnectors");
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
| **serviceName** | **String**| The name of the service. | |
| **serviceMemberId** | **UUID**| The server Id. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**Connectors**](Connectors.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of connector details. |  -  |

<a id="serviceMembersListCredentials"></a>
# **serviceMembersListCredentials**
> Credentials serviceMembersListCredentials(serviceName, serviceMemberId, apiVersion, $filter)



Gets the credentials of the server which is needed by the agent to connect to Azure Active Directory Connect Health Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceMembersApi apiInstance = new ServiceMembersApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    UUID serviceMemberId = UUID.randomUUID(); // UUID | The server Id.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | The property filter to apply.
    try {
      Credentials result = apiInstance.serviceMembersListCredentials(serviceName, serviceMemberId, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceMembersApi#serviceMembersListCredentials");
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
| **serviceName** | **String**| The name of the service. | |
| **serviceMemberId** | **UUID**| The server Id. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **$filter** | **String**| The property filter to apply. | [optional] |

### Return type

[**Credentials**](Credentials.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of service member credentials. |  -  |

<a id="serviceMembersListDataFreshness"></a>
# **serviceMembersListDataFreshness**
> DataFreshnessDetails serviceMembersListDataFreshness(serviceName, serviceMemberId, apiVersion)



Gets the last time when the server uploaded data to Azure Active Directory Connect Health Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceMembersApi apiInstance = new ServiceMembersApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    UUID serviceMemberId = UUID.randomUUID(); // UUID | The server Id.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      DataFreshnessDetails result = apiInstance.serviceMembersListDataFreshness(serviceName, serviceMemberId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceMembersApi#serviceMembersListDataFreshness");
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
| **serviceName** | **String**| The name of the service. | |
| **serviceMemberId** | **UUID**| The server Id. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**DataFreshnessDetails**](DataFreshnessDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of datafreshness details for a server. |  -  |

<a id="serviceMembersListExportStatus"></a>
# **serviceMembersListExportStatus**
> ExportStatuses serviceMembersListExportStatus(serviceName, serviceMemberId, apiVersion)



Gets the export status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceMembersApi apiInstance = new ServiceMembersApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    UUID serviceMemberId = UUID.randomUUID(); // UUID | The server Id.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      ExportStatuses result = apiInstance.serviceMembersListExportStatus(serviceName, serviceMemberId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceMembersApi#serviceMembersListExportStatus");
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
| **serviceName** | **String**| The name of the service. | |
| **serviceMemberId** | **UUID**| The server Id. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**ExportStatuses**](ExportStatuses.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of export statuses. |  -  |

<a id="serviceMembersListGlobalConfiguration"></a>
# **serviceMembersListGlobalConfiguration**
> GlobalConfigurations serviceMembersListGlobalConfiguration(serviceName, serviceMemberId, apiVersion)



Gets the global configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceMembersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceMembersApi apiInstance = new ServiceMembersApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String serviceMemberId = "serviceMemberId_example"; // String | The server id.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      GlobalConfigurations result = apiInstance.serviceMembersListGlobalConfiguration(serviceName, serviceMemberId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceMembersApi#serviceMembersListGlobalConfiguration");
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
| **serviceName** | **String**| The name of the service. | |
| **serviceMemberId** | **String**| The server id. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**GlobalConfigurations**](GlobalConfigurations.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of global configurations. |  -  |

