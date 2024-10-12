# ServicesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addsServicesDelete**](ServicesApi.md#addsServicesDelete) | **DELETE** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName} |  |
| [**addsServicesGet**](ServicesApi.md#addsServicesGet) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName} |  |
| [**addsServicesListPremiumServices**](ServicesApi.md#addsServicesListPremiumServices) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/premiumCheck |  |
| [**addsServicesUpdate**](ServicesApi.md#addsServicesUpdate) | **PATCH** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName} |  |
| [**servicesAdd**](ServicesApi.md#servicesAdd) | **POST** /providers/Microsoft.ADHybridHealthService/services |  |
| [**servicesDelete**](ServicesApi.md#servicesDelete) | **DELETE** /providers/Microsoft.ADHybridHealthService/services/{serviceName} |  |
| [**servicesGet**](ServicesApi.md#servicesGet) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName} |  |
| [**servicesGetFeatureAvailibility**](ServicesApi.md#servicesGetFeatureAvailibility) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/checkServiceFeatureAvailibility/{featureName} |  |
| [**servicesGetTenantWhitelisting**](ServicesApi.md#servicesGetTenantWhitelisting) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/TenantWhitelisting/{featureName} |  |
| [**servicesList**](ServicesApi.md#servicesList) | **GET** /providers/Microsoft.ADHybridHealthService/services |  |
| [**servicesListExportErrors**](ServicesApi.md#servicesListExportErrors) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/exporterrors/counts |  |
| [**servicesListExportErrorsV2**](ServicesApi.md#servicesListExportErrorsV2) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/exporterrors/listV2 |  |
| [**servicesListExportStatus**](ServicesApi.md#servicesListExportStatus) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/exportstatus |  |
| [**servicesListMonitoringConfigurations**](ServicesApi.md#servicesListMonitoringConfigurations) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/monitoringconfigurations |  |
| [**servicesListPremium**](ServicesApi.md#servicesListPremium) | **GET** /providers/Microsoft.ADHybridHealthService/services/premiumCheck |  |
| [**servicesUpdate**](ServicesApi.md#servicesUpdate) | **PATCH** /providers/Microsoft.ADHybridHealthService/services/{serviceName} |  |
| [**servicesUpdateMonitoringConfiguration**](ServicesApi.md#servicesUpdateMonitoringConfiguration) | **PATCH** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/monitoringconfiguration |  |


<a id="addsServicesDelete"></a>
# **addsServicesDelete**
> addsServicesDelete(serviceName, apiVersion, confirm)



Deletes an Active Directory Domain Service which is onboarded to Azure Active Directory Connect Health.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service which needs to be deleted.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    Boolean confirm = true; // Boolean | Indicates if the service will be permanently deleted or disabled. True indicates that the service will be permanently deleted and False indicates that the service will be marked disabled and then deleted after 30 days, if it is not re-registered.
    try {
      apiInstance.addsServicesDelete(serviceName, apiVersion, confirm);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#addsServicesDelete");
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
| **serviceName** | **String**| The name of the service which needs to be deleted. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **confirm** | **Boolean**| Indicates if the service will be permanently deleted or disabled. True indicates that the service will be permanently deleted and False indicates that the service will be marked disabled and then deleted after 30 days, if it is not re-registered. | [optional] |

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
| **204** | Successfully deleted the service. |  -  |

<a id="addsServicesGet"></a>
# **addsServicesGet**
> ServiceProperties addsServicesGet(serviceName, apiVersion)



Gets the details of an Active Directory Domain Service for a tenant having Azure AD Premium license and is onboarded to Azure Active Directory Connect Health.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      ServiceProperties result = apiInstance.addsServicesGet(serviceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#addsServicesGet");
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

### Return type

[**ServiceProperties**](ServiceProperties.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Active Directory Domain Controller service as specified by the serviceName property.  |  -  |

<a id="addsServicesListPremiumServices"></a>
# **addsServicesListPremiumServices**
> Services addsServicesListPremiumServices(apiVersion, $filter, serviceType, skipCount, takeCount)



Gets the details of Active Directory Domain Services for a tenant having Azure AD Premium license and is onboarded to Azure Active Directory Connect Health.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | The service property filter to apply.
    String serviceType = "serviceType_example"; // String | The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService.
    Integer skipCount = 56; // Integer | The skip count, which specifies the number of elements that can be bypassed from a sequence and then return the remaining elements.
    Integer takeCount = 56; // Integer | The take count , which specifies the number of elements that can be returned from a sequence.
    try {
      Services result = apiInstance.addsServicesListPremiumServices(apiVersion, $filter, serviceType, skipCount, takeCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#addsServicesListPremiumServices");
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
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **$filter** | **String**| The service property filter to apply. | [optional] |
| **serviceType** | **String**| The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService. | [optional] |
| **skipCount** | **Integer**| The skip count, which specifies the number of elements that can be bypassed from a sequence and then return the remaining elements. | [optional] |
| **takeCount** | **Integer**| The take count , which specifies the number of elements that can be returned from a sequence. | [optional] |

### Return type

[**Services**](Services.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of premium services. |  -  |

<a id="addsServicesUpdate"></a>
# **addsServicesUpdate**
> ServiceProperties addsServicesUpdate(serviceName, apiVersion, service)



Updates an Active Directory Domain Service properties of an onboarded service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service which needs to be deleted.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    ServiceProperties service = new ServiceProperties(); // ServiceProperties | The service object.
    try {
      ServiceProperties result = apiInstance.addsServicesUpdate(serviceName, apiVersion, service);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#addsServicesUpdate");
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
| **serviceName** | **String**| The name of the service which needs to be deleted. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **service** | [**ServiceProperties**](ServiceProperties.md)| The service object. | |

### Return type

[**ServiceProperties**](ServiceProperties.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated service. |  -  |

<a id="servicesAdd"></a>
# **servicesAdd**
> ServiceProperties servicesAdd(apiVersion, service)



Onboards a service for a given tenant in Azure Active Directory Connect Health.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    ServiceProperties service = new ServiceProperties(); // ServiceProperties | The service object.
    try {
      ServiceProperties result = apiInstance.servicesAdd(apiVersion, service);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#servicesAdd");
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
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **service** | [**ServiceProperties**](ServiceProperties.md)| The service object. | |

### Return type

[**ServiceProperties**](ServiceProperties.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully added the service. |  -  |

<a id="servicesDelete"></a>
# **servicesDelete**
> servicesDelete(serviceName, apiVersion, confirm)



Deletes a service which is onboarded to Azure Active Directory Connect Health.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service which needs to be deleted.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    Boolean confirm = true; // Boolean | Indicates if the service will be permanently deleted or disabled. True indicates that the service will be permanently deleted and False indicates that the service will be marked disabled and then deleted after 30 days, if it is not re-registered.
    try {
      apiInstance.servicesDelete(serviceName, apiVersion, confirm);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#servicesDelete");
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
| **serviceName** | **String**| The name of the service which needs to be deleted. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **confirm** | **Boolean**| Indicates if the service will be permanently deleted or disabled. True indicates that the service will be permanently deleted and False indicates that the service will be marked disabled and then deleted after 30 days, if it is not re-registered. | [optional] |

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
| **204** | Successfully deleted the service. |  -  |

<a id="servicesGet"></a>
# **servicesGet**
> ServiceProperties servicesGet(serviceName, apiVersion)



Gets the details of a service for a tenant having Azure AD Premium license and is onboarded to Azure Active Directory Connect Health.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      ServiceProperties result = apiInstance.servicesGet(serviceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#servicesGet");
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

### Return type

[**ServiceProperties**](ServiceProperties.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of services. |  -  |

<a id="servicesGetFeatureAvailibility"></a>
# **servicesGetFeatureAvailibility**
> Result servicesGetFeatureAvailibility(serviceName, featureName, apiVersion)



Checks if the service has all the pre-requisites met to use a feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String featureName = "featureName_example"; // String | The name of the feature.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      Result result = apiInstance.servicesGetFeatureAvailibility(serviceName, featureName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#servicesGetFeatureAvailibility");
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
| **featureName** | **String**| The name of the feature. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**Result**](Result.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Indicates if the feature is available or not. |  -  |

<a id="servicesGetTenantWhitelisting"></a>
# **servicesGetTenantWhitelisting**
> Result servicesGetTenantWhitelisting(serviceName, featureName, apiVersion)



Checks if the tenant, to which a service is registered, is whitelisted to use a feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String featureName = "featureName_example"; // String | The name of the feature.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      Result result = apiInstance.servicesGetTenantWhitelisting(serviceName, featureName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#servicesGetTenantWhitelisting");
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
| **featureName** | **String**| The name of the feature. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**Result**](Result.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Indicates if a tenant is whitelisted for a feature or not. |  -  |

<a id="servicesList"></a>
# **servicesList**
> Services servicesList(apiVersion, $filter, serviceType, skipCount, takeCount)



Gets the details of services, for a tenant, that are onboarded to Azure Active Directory Connect Health.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | The service property filter to apply.
    String serviceType = "serviceType_example"; // String | The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService.
    Integer skipCount = 56; // Integer | The skip count, which specifies the number of elements that can be bypassed from a sequence and then return the remaining elements.
    Integer takeCount = 56; // Integer | The take count , which specifies the number of elements that can be returned from a sequence.
    try {
      Services result = apiInstance.servicesList(apiVersion, $filter, serviceType, skipCount, takeCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#servicesList");
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
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **$filter** | **String**| The service property filter to apply. | [optional] |
| **serviceType** | **String**| The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService. | [optional] |
| **skipCount** | **Integer**| The skip count, which specifies the number of elements that can be bypassed from a sequence and then return the remaining elements. | [optional] |
| **takeCount** | **Integer**| The take count , which specifies the number of elements that can be returned from a sequence. | [optional] |

### Return type

[**Services**](Services.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of services. |  -  |

<a id="servicesListExportErrors"></a>
# **servicesListExportErrors**
> ErrorCounts servicesListExportErrors(serviceName, apiVersion)



Gets the count of latest AAD export errors.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      ErrorCounts result = apiInstance.servicesListExportErrors(serviceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#servicesListExportErrors");
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

### Return type

[**ErrorCounts**](ErrorCounts.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of export errors. |  -  |

<a id="servicesListExportErrorsV2"></a>
# **servicesListExportErrorsV2**
> MergedExportErrors servicesListExportErrorsV2(serviceName, errorBucket, apiVersion)



 Gets the categorized export errors.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String errorBucket = "errorBucket_example"; // String | The error category to query for.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      MergedExportErrors result = apiInstance.servicesListExportErrorsV2(serviceName, errorBucket, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#servicesListExportErrorsV2");
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
| **errorBucket** | **String**| The error category to query for. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**MergedExportErrors**](MergedExportErrors.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of merged export errors. |  -  |

<a id="servicesListExportStatus"></a>
# **servicesListExportStatus**
> ExportStatuses servicesListExportStatus(serviceName, apiVersion)



Gets the export status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      ExportStatuses result = apiInstance.servicesListExportStatus(serviceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#servicesListExportStatus");
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

<a id="servicesListMonitoringConfigurations"></a>
# **servicesListMonitoringConfigurations**
> Items servicesListMonitoringConfigurations(serviceName, apiVersion)



Gets the service level monitoring configurations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      Items result = apiInstance.servicesListMonitoringConfigurations(serviceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#servicesListMonitoringConfigurations");
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

### Return type

[**Items**](Items.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of monitoring configurations. |  -  |

<a id="servicesListPremium"></a>
# **servicesListPremium**
> Services servicesListPremium(apiVersion, $filter, serviceType, skipCount, takeCount)



Gets the details of services for a tenant having Azure AD Premium license and is onboarded to Azure Active Directory Connect Health.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | The service property filter to apply.
    String serviceType = "serviceType_example"; // String | The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService.
    Integer skipCount = 56; // Integer | The skip count, which specifies the number of elements that can be bypassed from a sequence and then return the remaining elements.
    Integer takeCount = 56; // Integer | The take count , which specifies the number of elements that can be returned from a sequence.
    try {
      Services result = apiInstance.servicesListPremium(apiVersion, $filter, serviceType, skipCount, takeCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#servicesListPremium");
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
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **$filter** | **String**| The service property filter to apply. | [optional] |
| **serviceType** | **String**| The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService. | [optional] |
| **skipCount** | **Integer**| The skip count, which specifies the number of elements that can be bypassed from a sequence and then return the remaining elements. | [optional] |
| **takeCount** | **Integer**| The take count , which specifies the number of elements that can be returned from a sequence. | [optional] |

### Return type

[**Services**](Services.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of premium services. |  -  |

<a id="servicesUpdate"></a>
# **servicesUpdate**
> ServiceProperties servicesUpdate(serviceName, apiVersion, service)



Updates the service properties of an onboarded service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service which needs to be deleted.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    ServiceProperties service = new ServiceProperties(); // ServiceProperties | The service object.
    try {
      ServiceProperties result = apiInstance.servicesUpdate(serviceName, apiVersion, service);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#servicesUpdate");
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
| **serviceName** | **String**| The name of the service which needs to be deleted. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **service** | [**ServiceProperties**](ServiceProperties.md)| The service object. | |

### Return type

[**ServiceProperties**](ServiceProperties.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the service. |  -  |

<a id="servicesUpdateMonitoringConfiguration"></a>
# **servicesUpdateMonitoringConfiguration**
> servicesUpdateMonitoringConfiguration(serviceName, apiVersion, configurationSetting)



Updates the service level monitoring configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    Item configurationSetting = new Item(); // Item | The monitoring configuration to update
    try {
      apiInstance.servicesUpdateMonitoringConfiguration(serviceName, apiVersion, configurationSetting);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#servicesUpdateMonitoringConfiguration");
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
| **configurationSetting** | [**Item**](Item.md)| The monitoring configuration to update | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the monitoring configuration. |  -  |

