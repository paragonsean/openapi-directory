# AddsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adDomainServiceMembersList**](AddsApi.md#adDomainServiceMembersList) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/addomainservicemembers |  |
| [**addsServiceGetMetrics**](AddsApi.md#addsServiceGetMetrics) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/metrics/{metricName}/groups/{groupName} |  |
| [**addsServiceMembersDelete**](AddsApi.md#addsServiceMembersDelete) | **DELETE** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/servicemembers/{serviceMemberId} |  |
| [**addsServiceMembersGet**](AddsApi.md#addsServiceMembersGet) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/servicemembers/{serviceMemberId} |  |
| [**addsServiceMembersList**](AddsApi.md#addsServiceMembersList) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/addsservicemembers |  |
| [**addsServiceMembersListCredentials**](AddsApi.md#addsServiceMembersListCredentials) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/servicemembers/{serviceMemberId}/credentials |  |
| [**addsServicesAdd**](AddsApi.md#addsServicesAdd) | **POST** /providers/Microsoft.ADHybridHealthService/addsservices |  |
| [**addsServicesGetForestSummary**](AddsApi.md#addsServicesGetForestSummary) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/forestsummary |  |
| [**addsServicesGetMetricMetadata**](AddsApi.md#addsServicesGetMetricMetadata) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/metricmetadata/{metricName} |  |
| [**addsServicesGetMetricMetadataForGroup**](AddsApi.md#addsServicesGetMetricMetadataForGroup) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/metricmetadata/{metricName}/groups/{groupName} |  |
| [**addsServicesList**](AddsApi.md#addsServicesList) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices |  |
| [**addsServicesListMetricMetadata**](AddsApi.md#addsServicesListMetricMetadata) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/metricmetadata |  |
| [**addsServicesListMetricsAverage**](AddsApi.md#addsServicesListMetricsAverage) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/metrics/{metricName}/groups/{groupName}/average |  |
| [**addsServicesListMetricsSum**](AddsApi.md#addsServicesListMetricsSum) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/metrics/{metricName}/groups/{groupName}/sum |  |
| [**addsServicesListReplicationDetails**](AddsApi.md#addsServicesListReplicationDetails) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/replicationdetails |  |
| [**addsServicesListReplicationSummary**](AddsApi.md#addsServicesListReplicationSummary) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/replicationsummary |  |
| [**addsServicesListServerAlerts**](AddsApi.md#addsServicesListServerAlerts) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/servicemembers/{serviceMemberId}/alerts |  |
| [**addsServicesReplicationStatusGet**](AddsApi.md#addsServicesReplicationStatusGet) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/replicationstatus |  |
| [**addsServicesServiceMembersAdd**](AddsApi.md#addsServicesServiceMembersAdd) | **POST** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/servicemembers |  |
| [**addsServicesServiceMembersList**](AddsApi.md#addsServicesServiceMembersList) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/servicemembers |  |
| [**addsServicesUserPreferenceAdd**](AddsApi.md#addsServicesUserPreferenceAdd) | **POST** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/features/{featureName}/userpreference |  |
| [**addsServicesUserPreferenceDelete**](AddsApi.md#addsServicesUserPreferenceDelete) | **DELETE** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/features/{featureName}/userpreference |  |
| [**addsServicesUserPreferenceGet**](AddsApi.md#addsServicesUserPreferenceGet) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/features/{featureName}/userpreference |  |
| [**alertsListAddsAlerts**](AddsApi.md#alertsListAddsAlerts) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/alerts |  |
| [**configurationListAddsConfigurations**](AddsApi.md#configurationListAddsConfigurations) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/configuration |  |
| [**dimensionsListAddsDimensions**](AddsApi.md#dimensionsListAddsDimensions) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/dimensions/{dimension} |  |


<a id="adDomainServiceMembersList"></a>
# **adDomainServiceMembersList**
> AddsServiceMembers adDomainServiceMembersList(serviceName, isGroupbySite, nextPartitionKey, nextRowKey, apiVersion, $filter, query, takeCount)



Gets the details of the servers, for a given Active Directory Domain Service, that are onboarded to Azure Active Directory Connect Health.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    Boolean isGroupbySite = true; // Boolean | Indicates if the result should be grouped by site or not.
    String nextPartitionKey = " "; // String | The next partition key to query for.
    String nextRowKey = " "; // String | The next row key to query for.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | The server property filter to apply.
    String query = "query_example"; // String | The custom query.
    Integer takeCount = 56; // Integer | The take count , which specifies the number of elements that can be returned from a sequence.
    try {
      AddsServiceMembers result = apiInstance.adDomainServiceMembersList(serviceName, isGroupbySite, nextPartitionKey, nextRowKey, apiVersion, $filter, query, takeCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#adDomainServiceMembersList");
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
| **isGroupbySite** | **Boolean**| Indicates if the result should be grouped by site or not. | |
| **nextPartitionKey** | **String**| The next partition key to query for. | [enum:  ] |
| **nextRowKey** | **String**| The next row key to query for. | [enum:  ] |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **$filter** | **String**| The server property filter to apply. | [optional] |
| **query** | **String**| The custom query. | [optional] |
| **takeCount** | **Integer**| The take count , which specifies the number of elements that can be returned from a sequence. | [optional] |

### Return type

[**AddsServiceMembers**](AddsServiceMembers.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of Active Directory Domain Servers. |  -  |

<a id="addsServiceGetMetrics"></a>
# **addsServiceGetMetrics**
> MetricSets addsServiceGetMetrics(serviceName, metricName, groupName, apiVersion, groupKey, fromDate, toDate)



Gets the server related metrics for a given metric and group combination.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String metricName = "metricName_example"; // String | The metric name
    String groupName = "groupName_example"; // String | The group name
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String groupKey = "groupKey_example"; // String | The group key
    OffsetDateTime fromDate = OffsetDateTime.now(); // OffsetDateTime | The start date.
    OffsetDateTime toDate = OffsetDateTime.now(); // OffsetDateTime | The end date.
    try {
      MetricSets result = apiInstance.addsServiceGetMetrics(serviceName, metricName, groupName, apiVersion, groupKey, fromDate, toDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServiceGetMetrics");
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
| **metricName** | **String**| The metric name | |
| **groupName** | **String**| The group name | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **groupKey** | **String**| The group key | [optional] |
| **fromDate** | **OffsetDateTime**| The start date. | [optional] |
| **toDate** | **OffsetDateTime**| The end date. | [optional] |

### Return type

[**MetricSets**](MetricSets.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The metric sets for the service.  |  -  |

<a id="addsServiceMembersDelete"></a>
# **addsServiceMembersDelete**
> addsServiceMembersDelete(serviceName, serviceMemberId, apiVersion, confirm)



Deletes a Active Directory Domain Controller server that has been onboarded to Azure Active Directory Connect Health Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    UUID serviceMemberId = UUID.randomUUID(); // UUID | The server Id.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    Boolean confirm = true; // Boolean | Indicates if the server will be permanently deleted or disabled. True indicates that the server will be permanently deleted and False indicates that the server will be marked disabled and then deleted after 30 days, if it is not re-registered.
    try {
      apiInstance.addsServiceMembersDelete(serviceName, serviceMemberId, apiVersion, confirm);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServiceMembersDelete");
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

<a id="addsServiceMembersGet"></a>
# **addsServiceMembersGet**
> ServiceMember addsServiceMembersGet(serviceName, serviceMemberId, apiVersion)



Gets the details of a server, for a given Active Directory Domain Controller service, that are onboarded to Azure Active Directory Connect Health Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    UUID serviceMemberId = UUID.randomUUID(); // UUID | The server Id.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      ServiceMember result = apiInstance.addsServiceMembersGet(serviceName, serviceMemberId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServiceMembersGet");
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
| **200** | The service member details for a given service.  |  -  |

<a id="addsServiceMembersList"></a>
# **addsServiceMembersList**
> AddsServiceMembers addsServiceMembersList(serviceName, apiVersion, $filter)



Gets the details of the Active Directory Domain servers, for a given Active Directory Domain Service, that are onboarded to Azure Active Directory Connect Health.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | The server property filter to apply.
    try {
      AddsServiceMembers result = apiInstance.addsServiceMembersList(serviceName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServiceMembersList");
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

### Return type

[**AddsServiceMembers**](AddsServiceMembers.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of Active Directory Domain Servers.  |  -  |

<a id="addsServiceMembersListCredentials"></a>
# **addsServiceMembersListCredentials**
> Credentials addsServiceMembersListCredentials(serviceName, serviceMemberId, apiVersion, $filter)



Gets the credentials of the server which is needed by the agent to connect to Azure Active Directory Connect Health Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    UUID serviceMemberId = UUID.randomUUID(); // UUID | The server Id.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | The property filter to apply.
    try {
      Credentials result = apiInstance.addsServiceMembersListCredentials(serviceName, serviceMemberId, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServiceMembersListCredentials");
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
| **200** | The list of server credentials. |  -  |

<a id="addsServicesAdd"></a>
# **addsServicesAdd**
> ServiceProperties addsServicesAdd(apiVersion, service)



Onboards a service for a given tenant in Azure Active Directory Connect Health.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    ServiceProperties service = new ServiceProperties(); // ServiceProperties | The service object.
    try {
      ServiceProperties result = apiInstance.addsServicesAdd(apiVersion, service);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServicesAdd");
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
| **200** | Adds the Active Directory Domain Controller Services. |  -  |

<a id="addsServicesGetForestSummary"></a>
# **addsServicesGetForestSummary**
> ForestSummary addsServicesGetForestSummary(serviceName, apiVersion)



Gets the forest summary for a given Active Directory Domain Service, that is onboarded to Azure Active Directory Connect Health.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      ForestSummary result = apiInstance.addsServicesGetForestSummary(serviceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServicesGetForestSummary");
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

[**ForestSummary**](ForestSummary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of forest summary for the service.  |  -  |

<a id="addsServicesGetMetricMetadata"></a>
# **addsServicesGetMetricMetadata**
> MetricMetadata addsServicesGetMetricMetadata(serviceName, metricName, apiVersion)



Gets the service related metric information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String metricName = "metricName_example"; // String | The metric name
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      MetricMetadata result = apiInstance.addsServicesGetMetricMetadata(serviceName, metricName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServicesGetMetricMetadata");
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
| **metricName** | **String**| The metric name | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**MetricMetadata**](MetricMetadata.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  The metric metadata for the service. |  -  |

<a id="addsServicesGetMetricMetadataForGroup"></a>
# **addsServicesGetMetricMetadataForGroup**
> MetricSets addsServicesGetMetricMetadataForGroup(serviceName, metricName, groupName, apiVersion, groupKey, fromDate, toDate)



Gets the service related metrics for a given metric and group combination.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String metricName = "metricName_example"; // String | The metric name
    String groupName = "groupName_example"; // String | The group name
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String groupKey = "groupKey_example"; // String | The group key
    OffsetDateTime fromDate = OffsetDateTime.now(); // OffsetDateTime | The start date.
    OffsetDateTime toDate = OffsetDateTime.now(); // OffsetDateTime | The end date.
    try {
      MetricSets result = apiInstance.addsServicesGetMetricMetadataForGroup(serviceName, metricName, groupName, apiVersion, groupKey, fromDate, toDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServicesGetMetricMetadataForGroup");
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
| **metricName** | **String**| The metric name | |
| **groupName** | **String**| The group name | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **groupKey** | **String**| The group key | [optional] |
| **fromDate** | **OffsetDateTime**| The start date. | [optional] |
| **toDate** | **OffsetDateTime**| The end date. | [optional] |

### Return type

[**MetricSets**](MetricSets.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The metric sets for a given service and group.  |  -  |

<a id="addsServicesList"></a>
# **addsServicesList**
> Services addsServicesList(apiVersion, $filter, serviceType, skipCount, takeCount)



Gets the details of Active Directory Domain Service, for a tenant, that are onboarded to Azure Active Directory Connect Health.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | The service property filter to apply.
    String serviceType = "serviceType_example"; // String | The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService.
    Integer skipCount = 56; // Integer | The skip count, which specifies the number of elements that can be bypassed from a sequence and then return the remaining elements.
    Integer takeCount = 56; // Integer | The take count , which specifies the number of elements that can be returned from a sequence.
    try {
      Services result = apiInstance.addsServicesList(apiVersion, $filter, serviceType, skipCount, takeCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServicesList");
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
| **200** |  The list of Active Directory Domain Controller services. |  -  |

<a id="addsServicesListMetricMetadata"></a>
# **addsServicesListMetricMetadata**
> MetricMetadataList addsServicesListMetricMetadata(serviceName, apiVersion, $filter, perfCounter)



Gets the service related metrics information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | The metric metadata property filter to apply.
    Boolean perfCounter = true; // Boolean | Indicates if only performance counter metrics are requested.
    try {
      MetricMetadataList result = apiInstance.addsServicesListMetricMetadata(serviceName, apiVersion, $filter, perfCounter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServicesListMetricMetadata");
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
| **$filter** | **String**| The metric metadata property filter to apply. | [optional] |
| **perfCounter** | **Boolean**| Indicates if only performance counter metrics are requested. | [optional] |

### Return type

[**MetricMetadataList**](MetricMetadataList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of metric metadata for a service.  |  -  |

<a id="addsServicesListMetricsAverage"></a>
# **addsServicesListMetricsAverage**
> Metrics addsServicesListMetricsAverage(serviceName, metricName, groupName, apiVersion)



Gets the average of the metric values for a given metric and group combination.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String metricName = "metricName_example"; // String | The metric name
    String groupName = "groupName_example"; // String | The group name
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      Metrics result = apiInstance.addsServicesListMetricsAverage(serviceName, metricName, groupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServicesListMetricsAverage");
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
| **metricName** | **String**| The metric name | |
| **groupName** | **String**| The group name | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**Metrics**](Metrics.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of metrics.  |  -  |

<a id="addsServicesListMetricsSum"></a>
# **addsServicesListMetricsSum**
> Metrics addsServicesListMetricsSum(serviceName, metricName, groupName, apiVersion)



Gets the sum of the metric values for a given metric and group combination.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String metricName = "metricName_example"; // String | The metric name
    String groupName = "groupName_example"; // String | The group name
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      Metrics result = apiInstance.addsServicesListMetricsSum(serviceName, metricName, groupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServicesListMetricsSum");
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
| **metricName** | **String**| The metric name | |
| **groupName** | **String**| The group name | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**Metrics**](Metrics.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of aum of the metric values for a given service.  |  -  |

<a id="addsServicesListReplicationDetails"></a>
# **addsServicesListReplicationDetails**
> ReplicationDetailsList addsServicesListReplicationDetails(serviceName, apiVersion, $filter, withDetails)



Gets complete domain controller list along with replication details for a given Active Directory Domain Service, that is onboarded to Azure Active Directory Connect Health.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | The server property filter to apply.
    Boolean withDetails = true; // Boolean | Indicates if InboundReplicationNeighbor details are required or not.
    try {
      ReplicationDetailsList result = apiInstance.addsServicesListReplicationDetails(serviceName, apiVersion, $filter, withDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServicesListReplicationDetails");
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
| **withDetails** | **Boolean**| Indicates if InboundReplicationNeighbor details are required or not. | [optional] |

### Return type

[**ReplicationDetailsList**](ReplicationDetailsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of replication details for a service.  |  -  |

<a id="addsServicesListReplicationSummary"></a>
# **addsServicesListReplicationSummary**
> ReplicationSummaryList addsServicesListReplicationSummary(serviceName, isGroupbySite, query, nextPartitionKey, nextRowKey, apiVersion, $filter, takeCount)



Gets complete domain controller list along with replication details for a given Active Directory Domain Service, that is onboarded to Azure Active Directory Connect Health.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    Boolean isGroupbySite = true; // Boolean | Indicates if the result should be grouped by site or not.
    String query = "query_example"; // String | The custom query.
    String nextPartitionKey = " "; // String | The next partition key to query for.
    String nextRowKey = " "; // String | The next row key to query for.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | The server property filter to apply.
    Integer takeCount = 56; // Integer | The take count , which specifies the number of elements that can be returned from a sequence.
    try {
      ReplicationSummaryList result = apiInstance.addsServicesListReplicationSummary(serviceName, isGroupbySite, query, nextPartitionKey, nextRowKey, apiVersion, $filter, takeCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServicesListReplicationSummary");
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
| **isGroupbySite** | **Boolean**| Indicates if the result should be grouped by site or not. | |
| **query** | **String**| The custom query. | |
| **nextPartitionKey** | **String**| The next partition key to query for. | [enum:  ] |
| **nextRowKey** | **String**| The next row key to query for. | [enum:  ] |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **$filter** | **String**| The server property filter to apply. | [optional] |
| **takeCount** | **Integer**| The take count , which specifies the number of elements that can be returned from a sequence. | [optional] |

### Return type

[**ReplicationSummaryList**](ReplicationSummaryList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of replication summary for a service.  |  -  |

<a id="addsServicesListServerAlerts"></a>
# **addsServicesListServerAlerts**
> Alerts addsServicesListServerAlerts(serviceMemberId, serviceName, apiVersion, $filter, state, from, to)



Gets the details of an alert for a given Active Directory Domain Controller service and server combination.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    UUID serviceMemberId = UUID.randomUUID(); // UUID | The server Id for which the alert details needs to be queried.
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | The alert property filter to apply.
    String state = "state_example"; // String | The alert state to query for.
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | The start date to query for.
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | The end date till when to query for.
    try {
      Alerts result = apiInstance.addsServicesListServerAlerts(serviceMemberId, serviceName, apiVersion, $filter, state, from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServicesListServerAlerts");
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
| **serviceMemberId** | **UUID**| The server Id for which the alert details needs to be queried. | |
| **serviceName** | **String**| The name of the service. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **$filter** | **String**| The alert property filter to apply. | [optional] |
| **state** | **String**| The alert state to query for. | [optional] |
| **from** | **OffsetDateTime**| The start date to query for. | [optional] |
| **to** | **OffsetDateTime**| The end date till when to query for. | [optional] |

### Return type

[**Alerts**](Alerts.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of server alerts. |  -  |

<a id="addsServicesReplicationStatusGet"></a>
# **addsServicesReplicationStatusGet**
> ReplicationStatus addsServicesReplicationStatusGet(serviceName, apiVersion)



Gets Replication status for a given Active Directory Domain Service, that is onboarded to Azure Active Directory Connect Health.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      ReplicationStatus result = apiInstance.addsServicesReplicationStatusGet(serviceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServicesReplicationStatusGet");
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

[**ReplicationStatus**](ReplicationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The replication status for a service.  |  -  |

<a id="addsServicesServiceMembersAdd"></a>
# **addsServicesServiceMembersAdd**
> ServiceMember addsServicesServiceMembersAdd(serviceName, apiVersion, serviceMember)



Onboards  a server, for a given Active Directory Domain Controller service, to Azure Active Directory Connect Health Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service under which the server is to be onboarded.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    ServiceMember serviceMember = new ServiceMember(); // ServiceMember | The server object.
    try {
      ServiceMember result = apiInstance.addsServicesServiceMembersAdd(serviceName, apiVersion, serviceMember);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServicesServiceMembersAdd");
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

<a id="addsServicesServiceMembersList"></a>
# **addsServicesServiceMembersList**
> ServiceMembers addsServicesServiceMembersList(serviceName, apiVersion, $filter, dimensionType, dimensionSignature)



Gets the details of the servers, for a given Active Directory Domain Controller service, that are onboarded to Azure Active Directory Connect Health Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | The server property filter to apply.
    String dimensionType = "dimensionType_example"; // String | The server specific dimension.
    String dimensionSignature = "dimensionSignature_example"; // String | The value of the dimension.
    try {
      ServiceMembers result = apiInstance.addsServicesServiceMembersList(serviceName, apiVersion, $filter, dimensionType, dimensionSignature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServicesServiceMembersList");
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
| **200** | The list of service members for a given service. |  -  |

<a id="addsServicesUserPreferenceAdd"></a>
# **addsServicesUserPreferenceAdd**
> addsServicesUserPreferenceAdd(serviceName, featureName, apiVersion, setting)



Adds the user preferences for a given feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String featureName = "featureName_example"; // String | The name of the feature.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    UserPreference setting = new UserPreference(); // UserPreference | The user preference setting.
    try {
      apiInstance.addsServicesUserPreferenceAdd(serviceName, featureName, apiVersion, setting);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServicesUserPreferenceAdd");
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
| **setting** | [**UserPreference**](UserPreference.md)| The user preference setting. | |

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
| **200** |  Successfully added the user preference settings.  |  -  |

<a id="addsServicesUserPreferenceDelete"></a>
# **addsServicesUserPreferenceDelete**
> addsServicesUserPreferenceDelete(serviceName, featureName, apiVersion)



Deletes the user preferences for a given feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String featureName = "featureName_example"; // String | The name of the feature.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      apiInstance.addsServicesUserPreferenceDelete(serviceName, featureName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServicesUserPreferenceDelete");
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

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted the user preference settings.  |  -  |

<a id="addsServicesUserPreferenceGet"></a>
# **addsServicesUserPreferenceGet**
> UserPreference addsServicesUserPreferenceGet(serviceName, featureName, apiVersion)



Gets the user preferences for a given feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String featureName = "featureName_example"; // String | The name of the feature.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      UserPreference result = apiInstance.addsServicesUserPreferenceGet(serviceName, featureName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#addsServicesUserPreferenceGet");
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

[**UserPreference**](UserPreference.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The user preference settings.  |  -  |

<a id="alertsListAddsAlerts"></a>
# **alertsListAddsAlerts**
> Alerts alertsListAddsAlerts(serviceName, apiVersion, $filter, state, from, to)



Gets the alerts for a given Active Directory Domain Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | The alert property filter to apply.
    String state = "state_example"; // String | The alert state to query for.
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | The start date to query for.
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | The end date till when to query for.
    try {
      Alerts result = apiInstance.alertsListAddsAlerts(serviceName, apiVersion, $filter, state, from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#alertsListAddsAlerts");
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
| **$filter** | **String**| The alert property filter to apply. | [optional] |
| **state** | **String**| The alert state to query for. | [optional] |
| **from** | **OffsetDateTime**| The start date to query for. | [optional] |
| **to** | **OffsetDateTime**| The end date till when to query for. | [optional] |

### Return type

[**Alerts**](Alerts.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of alerts for the given service. |  -  |

<a id="configurationListAddsConfigurations"></a>
# **configurationListAddsConfigurations**
> AddsConfiguration configurationListAddsConfigurations(serviceName, grouping)



Gets the service configurations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String grouping = "grouping_example"; // String | The grouping for configurations.
    try {
      AddsConfiguration result = apiInstance.configurationListAddsConfigurations(serviceName, grouping);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#configurationListAddsConfigurations");
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
| **grouping** | **String**| The grouping for configurations. | [optional] |

### Return type

[**AddsConfiguration**](AddsConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Active Directory Domain Controller service configuration.  |  -  |

<a id="dimensionsListAddsDimensions"></a>
# **dimensionsListAddsDimensions**
> Dimensions dimensionsListAddsDimensions(serviceName, dimension, apiVersion)



Gets the dimensions for a given dimension type in a server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AddsApi apiInstance = new AddsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String dimension = "dimension_example"; // String | The dimension type.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      Dimensions result = apiInstance.dimensionsListAddsDimensions(serviceName, dimension, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddsApi#dimensionsListAddsDimensions");
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
| **dimension** | **String**| The dimension type. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**Dimensions**](Dimensions.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of dimensions for a server.  |  -  |

