# DefaultApi

All URIs are relative to *https://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applicationHealthsGet**](DefaultApi.md#applicationHealthsGet) | **GET** /Applications/{applicationName}/$/GetHealth |  |
| [**applicationHealthsSend**](DefaultApi.md#applicationHealthsSend) | **POST** /Applications/{applicationName}/$/ReportHealth |  |
| [**applicationManifestsGet**](DefaultApi.md#applicationManifestsGet) | **GET** /ApplicationTypes/{applicationTypeName}/$/GetApplicationManifest |  |
| [**applicationTypesGet**](DefaultApi.md#applicationTypesGet) | **GET** /ApplicationTypes/{applicationTypeName} |  |
| [**applicationTypesList**](DefaultApi.md#applicationTypesList) | **GET** /ApplicationTypes |  |
| [**applicationTypesRegister**](DefaultApi.md#applicationTypesRegister) | **POST** /ApplicationTypes/$/Provision |  |
| [**applicationTypesUnregister**](DefaultApi.md#applicationTypesUnregister) | **POST** /ApplicationTypes/{applicationTypeName}/$/Unprovision |  |
| [**applicationUpgradeRollbacksStart**](DefaultApi.md#applicationUpgradeRollbacksStart) | **POST** /Applications/{applicationName}/$/RollbackUpgrade |  |
| [**applicationUpgradesGet**](DefaultApi.md#applicationUpgradesGet) | **GET** /Applications/{applicationName}/$/GetUpgradeProgress |  |
| [**applicationUpgradesResume**](DefaultApi.md#applicationUpgradesResume) | **POST** /Applications/{applicationName}/$/MoveNextUpgradeDomain |  |
| [**applicationUpgradesStart**](DefaultApi.md#applicationUpgradesStart) | **POST** /Applications/{applicationName}/$/Upgrade |  |
| [**applicationUpgradesUpdate**](DefaultApi.md#applicationUpgradesUpdate) | **POST** /Applications/{applicationName}/$/UpdateUpgrade |  |
| [**applicationsCreate**](DefaultApi.md#applicationsCreate) | **POST** /Applications/$/Create |  |
| [**applicationsGet**](DefaultApi.md#applicationsGet) | **GET** /Applications/{applicationName} |  |
| [**applicationsList**](DefaultApi.md#applicationsList) | **GET** /Applications |  |
| [**applicationsRemove**](DefaultApi.md#applicationsRemove) | **POST** /Applications/{applicationName}/$/Delete |  |
| [**clusterHealthsGet**](DefaultApi.md#clusterHealthsGet) | **GET** /$/GetClusterHealth |  |
| [**clusterHealthsSend**](DefaultApi.md#clusterHealthsSend) | **POST** /$/ReportClusterHealth |  |
| [**clusterLoadInformationsGet**](DefaultApi.md#clusterLoadInformationsGet) | **GET** /$/GetLoadInformation |  |
| [**clusterManifestsGet**](DefaultApi.md#clusterManifestsGet) | **GET** /$/GetClusterManifest |  |
| [**clusterPackagesRegister**](DefaultApi.md#clusterPackagesRegister) | **POST** /$/Provision |  |
| [**clusterPackagesUnregister**](DefaultApi.md#clusterPackagesUnregister) | **POST** /$/Unprovision |  |
| [**clusterUpgradesResume**](DefaultApi.md#clusterUpgradesResume) | **POST** /$/MoveToNextUpgradeDomain |  |
| [**clusterUpgradesRollback**](DefaultApi.md#clusterUpgradesRollback) | **POST** /$/RollbackUpgrade |  |
| [**clusterUpgradesStart**](DefaultApi.md#clusterUpgradesStart) | **POST** /$/Upgrade |  |
| [**clusterUpgradesUpdate**](DefaultApi.md#clusterUpgradesUpdate) | **POST** /$/UpdateUpgrade |  |
| [**deployedApplicationHealthsGet**](DefaultApi.md#deployedApplicationHealthsGet) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationName}/$/GetHealth |  |
| [**deployedApplicationHealthsSend**](DefaultApi.md#deployedApplicationHealthsSend) | **POST** /Nodes/{nodeName}/$/GetApplications/{applicationName}/$/ReportHealth |  |
| [**deployedApplicationsGet**](DefaultApi.md#deployedApplicationsGet) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationName} |  |
| [**deployedApplicationsList**](DefaultApi.md#deployedApplicationsList) | **GET** /Nodes/{nodeName}/$/GetApplications |  |
| [**deployedCodePackagesGet**](DefaultApi.md#deployedCodePackagesGet) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationName}/$/GetCodePackages |  |
| [**deployedReplicaDetailsGet**](DefaultApi.md#deployedReplicaDetailsGet) | **GET** /Nodes/{nodeName}/$/GetPartitions/{partitionName}/$/GetReplicas/{replicaId}/$/GetDetail |  |
| [**deployedReplicasGet**](DefaultApi.md#deployedReplicasGet) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationName}/$/GetReplicas |  |
| [**deployedServicePackageHealthsGet**](DefaultApi.md#deployedServicePackageHealthsGet) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationName}/$/GetServicePackages/{servicePackageName}/$/GetHealth |  |
| [**deployedServicePackageHealthsSend**](DefaultApi.md#deployedServicePackageHealthsSend) | **POST** /Nodes/{nodeName}/$/GetApplications/{applicationName}/$/GetServicePackages/{serviceManifestName}/$/ReportHealth |  |
| [**deployedServicePackagesGet**](DefaultApi.md#deployedServicePackagesGet) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationName}/$/GetServicePackages |  |
| [**deployedServiceTypesGet**](DefaultApi.md#deployedServiceTypesGet) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationName}/$/GetServiceTypes |  |
| [**nodeHealthsGet**](DefaultApi.md#nodeHealthsGet) | **GET** /Nodes/{nodeName}/$/GetHealth |  |
| [**nodeHealthsSend**](DefaultApi.md#nodeHealthsSend) | **POST** /Nodes/{nodeName}/$/ReportHealth |  |
| [**nodeLoadInformationsGet**](DefaultApi.md#nodeLoadInformationsGet) | **GET** /Nodes/{nodeName}/$/GetLoadInformation |  |
| [**nodeStatesRemove**](DefaultApi.md#nodeStatesRemove) | **POST** /Nodes/{nodeName}/$/RemoveNodeState |  |
| [**nodesDisable**](DefaultApi.md#nodesDisable) | **POST** /Nodes/{nodeName}/$/Deactivate |  |
| [**nodesEnable**](DefaultApi.md#nodesEnable) | **POST** /Nodes/{nodeName}/$/Activate |  |
| [**nodesGet**](DefaultApi.md#nodesGet) | **GET** /Nodes/{nodeName} |  |
| [**nodesList**](DefaultApi.md#nodesList) | **GET** /Nodes |  |
| [**partitionHealthsGet**](DefaultApi.md#partitionHealthsGet) | **GET** /Partitions/{partitionId}/$/GetHealth |  |
| [**partitionHealthsSend**](DefaultApi.md#partitionHealthsSend) | **POST** /Partitions/{partitionId}/$/ReportHealth |  |
| [**partitionListsRepair**](DefaultApi.md#partitionListsRepair) | **POST** /Services/{serviceName}/$/GetPartitions/$/Recover |  |
| [**partitionLoadInformationsGet**](DefaultApi.md#partitionLoadInformationsGet) | **GET** /Partitions/{partitionId}/$/GetLoadInformation |  |
| [**partitionLoadsReset**](DefaultApi.md#partitionLoadsReset) | **POST** /Partitions/{partitionId}/$/ResetLoad |  |
| [**partitionsGet**](DefaultApi.md#partitionsGet) | **GET** /Services/{serviceName}/$/GetPartitions/{partitionId} |  |
| [**partitionsList**](DefaultApi.md#partitionsList) | **GET** /Services/{serviceName}/$/GetPartitions |  |
| [**partitionsRepair**](DefaultApi.md#partitionsRepair) | **POST** /Partitions/{partitionId}/$/Recover |  |
| [**replicaHealthsGet**](DefaultApi.md#replicaHealthsGet) | **GET** /Partitions/{partitionId}/$/GetReplicas/{replicaId}/$/GetHealth |  |
| [**replicaHealthsSend**](DefaultApi.md#replicaHealthsSend) | **POST** /Partitions/{partitionId}/$/GetReplicas/{replicaId}/$/ReportHealth |  |
| [**replicaLoadInformationsGet**](DefaultApi.md#replicaLoadInformationsGet) | **GET** /Partitions/{partitionId}/$/GetReplicas/{replicaId}/$/GetLoadInformation |  |
| [**replicasGet**](DefaultApi.md#replicasGet) | **GET** /Partitions/{partitionId}/$/GetReplicas/{replicaId} |  |
| [**replicasList**](DefaultApi.md#replicasList) | **GET** /Partitions/{partitionId}/$/GetReplicas |  |
| [**serviceDescriptionsGet**](DefaultApi.md#serviceDescriptionsGet) | **GET** /Services/{serviceName}/$/GetDescription |  |
| [**serviceFromTemplatesCreate**](DefaultApi.md#serviceFromTemplatesCreate) | **POST** /Applications/{applicationName}/$/GetServices/$/CreateFromTemplate |  |
| [**serviceGroupDescriptionsGet**](DefaultApi.md#serviceGroupDescriptionsGet) | **GET** /Applications/{applicationName}/$/GetServices/{serviceName}/$/GetServiceGroupDescription |  |
| [**serviceGroupFromTemplatesCreate**](DefaultApi.md#serviceGroupFromTemplatesCreate) | **POST** /Applications/{applicationName}/$/GetServiceGroups/$/CreateServiceGroupFromTemplate |  |
| [**serviceGroupMembersGet**](DefaultApi.md#serviceGroupMembersGet) | **GET** /Applications/{applicationName}/$/GetServices/{serviceName}/$/GetServiceGroupMembers |  |
| [**serviceGroupsCreate**](DefaultApi.md#serviceGroupsCreate) | **POST** /Applications/{applicationName}/$/GetServices/$/CreateServiceGroup |  |
| [**serviceGroupsRemove**](DefaultApi.md#serviceGroupsRemove) | **POST** /Applications/{applicationName}/$/GetServiceGroups/{serviceName}/$/Delete |  |
| [**serviceGroupsUpdate**](DefaultApi.md#serviceGroupsUpdate) | **POST** /Applications/{applicationName}/$/GetServices/{serviceName}/$/UpdateServiceGroup |  |
| [**serviceHealthsGet**](DefaultApi.md#serviceHealthsGet) | **GET** /Services/{serviceName}/$/GetHealth |  |
| [**serviceHealthsSend**](DefaultApi.md#serviceHealthsSend) | **POST** /Services/{serviceName}/$/ReportHealth |  |
| [**serviceManifestsGet**](DefaultApi.md#serviceManifestsGet) | **GET** /ApplicationTypes/{applicationTypeName}/$/GetServiceManifest |  |
| [**serviceTypesGet**](DefaultApi.md#serviceTypesGet) | **GET** /ApplicationTypes/{applicationTypeName}/$/GetServiceTypes |  |
| [**servicesCreate**](DefaultApi.md#servicesCreate) | **POST** /Applications/{applicationName}/$/GetServices/$/Create |  |
| [**servicesGet**](DefaultApi.md#servicesGet) | **GET** /Applications/{applicationName}/$/GetServices/{serviceName} |  |
| [**servicesList**](DefaultApi.md#servicesList) | **GET** /Applications/{applicationName}/$/GetServices |  |
| [**servicesRemove**](DefaultApi.md#servicesRemove) | **POST** /Services/{serviceName}/$/Delete |  |
| [**servicesResolve**](DefaultApi.md#servicesResolve) | **GET** /Services/{serviceName}/$/ResolvePartition |  |
| [**servicesUpdate**](DefaultApi.md#servicesUpdate) | **POST** /Services/{serviceName}/$/Update |  |
| [**upgradeProgressesGet**](DefaultApi.md#upgradeProgressesGet) | **GET** /$/GetUpgradeProgress |  |


<a id="applicationHealthsGet"></a>
# **applicationHealthsGet**
> ApplicationHealth applicationHealthsGet(applicationName, apiVersion, eventsHealthStateFilter, deployedApplicationsHealthStateFilter, timeout)



Get application healths

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationName = "applicationName_example"; // String | The name of the application
    String apiVersion = "apiVersion_example"; // String | The version of the api
    String eventsHealthStateFilter = "eventsHealthStateFilter_example"; // String | The filter of the events health state
    String deployedApplicationsHealthStateFilter = "deployedApplicationsHealthStateFilter_example"; // String | The filter of the deployed application health state
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      ApplicationHealth result = apiInstance.applicationHealthsGet(applicationName, apiVersion, eventsHealthStateFilter, deployedApplicationsHealthStateFilter, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#applicationHealthsGet");
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
| **applicationName** | **String**| The name of the application | |
| **apiVersion** | **String**| The version of the api | |
| **eventsHealthStateFilter** | **String**| The filter of the events health state | [optional] |
| **deployedApplicationsHealthStateFilter** | **String**| The filter of the deployed application health state | [optional] |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**ApplicationHealth**](ApplicationHealth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The application health |  -  |
| **0** | Error |  -  |

<a id="applicationHealthsSend"></a>
# **applicationHealthsSend**
> String applicationHealthsSend(applicationName, apiVersion, applicationHealthReport, timeout)



Send application health

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationName = "applicationName_example"; // String | The name of the application
    String apiVersion = "apiVersion_example"; // String | The version of the api
    ApplicationHealthReport applicationHealthReport = new ApplicationHealthReport(); // ApplicationHealthReport | The report of the application health
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.applicationHealthsSend(applicationName, apiVersion, applicationHealthReport, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#applicationHealthsSend");
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
| **applicationName** | **String**| The name of the application | |
| **apiVersion** | **String**| The version of the api | |
| **applicationHealthReport** | [**ApplicationHealthReport**](ApplicationHealthReport.md)| The report of the application health | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The application health |  -  |
| **0** | Error |  -  |

<a id="applicationManifestsGet"></a>
# **applicationManifestsGet**
> ApplicationManifest applicationManifestsGet(applicationTypeName, applicationTypeVersion, apiVersion, timeout)



Get application manifests

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationTypeName = "applicationTypeName_example"; // String | The name of the application type
    String applicationTypeVersion = "applicationTypeVersion_example"; // String | The version of the application type
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      ApplicationManifest result = apiInstance.applicationManifestsGet(applicationTypeName, applicationTypeVersion, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#applicationManifestsGet");
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
| **applicationTypeName** | **String**| The name of the application type | |
| **applicationTypeVersion** | **String**| The version of the application type | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**ApplicationManifest**](ApplicationManifest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The application manifest |  -  |
| **0** | Error |  -  |

<a id="applicationTypesGet"></a>
# **applicationTypesGet**
> List&lt;ApplicationType&gt; applicationTypesGet(applicationTypeName, apiVersion, timeout)



Get application types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationTypeName = "applicationTypeName_example"; // String | The name of the application type
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      List<ApplicationType> result = apiInstance.applicationTypesGet(applicationTypeName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#applicationTypesGet");
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
| **applicationTypeName** | **String**| The name of the application type | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**List&lt;ApplicationType&gt;**](ApplicationType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The application type |  -  |
| **0** | Error |  -  |

<a id="applicationTypesList"></a>
# **applicationTypesList**
> List&lt;ApplicationType&gt; applicationTypesList(apiVersion, timeout)



List application types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      List<ApplicationType> result = apiInstance.applicationTypesList(apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#applicationTypesList");
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
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**List&lt;ApplicationType&gt;**](ApplicationType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The application type |  -  |
| **0** | Error |  -  |

<a id="applicationTypesRegister"></a>
# **applicationTypesRegister**
> String applicationTypesRegister(apiVersion, registerApplicationType, timeout)



Register application types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the api
    RegisterApplicationType registerApplicationType = new RegisterApplicationType(); // RegisterApplicationType | The type of the register application
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.applicationTypesRegister(apiVersion, registerApplicationType, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#applicationTypesRegister");
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
| **apiVersion** | **String**| The version of the api | |
| **registerApplicationType** | [**RegisterApplicationType**](RegisterApplicationType.md)| The type of the register application | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The application type |  -  |
| **0** | Error |  -  |

<a id="applicationTypesUnregister"></a>
# **applicationTypesUnregister**
> String applicationTypesUnregister(applicationTypeName, apiVersion, unregisterApplicationType, timeout)



Unregister application types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationTypeName = "applicationTypeName_example"; // String | The name of the application type
    String apiVersion = "apiVersion_example"; // String | The version of the api
    UnregisterApplicationType unregisterApplicationType = new UnregisterApplicationType(); // UnregisterApplicationType | The type of the unregister application
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.applicationTypesUnregister(applicationTypeName, apiVersion, unregisterApplicationType, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#applicationTypesUnregister");
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
| **applicationTypeName** | **String**| The name of the application type | |
| **apiVersion** | **String**| The version of the api | |
| **unregisterApplicationType** | [**UnregisterApplicationType**](UnregisterApplicationType.md)| The type of the unregister application | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The application type |  -  |
| **0** | Error |  -  |

<a id="applicationUpgradeRollbacksStart"></a>
# **applicationUpgradeRollbacksStart**
> String applicationUpgradeRollbacksStart(applicationName, apiVersion, timeout)



Start application upgrade rollbacks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationName = "applicationName_example"; // String | The name of the application
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.applicationUpgradeRollbacksStart(applicationName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#applicationUpgradeRollbacksStart");
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
| **applicationName** | **String**| The name of the application | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The application upgrade rollback |  -  |
| **0** | Error |  -  |

<a id="applicationUpgradesGet"></a>
# **applicationUpgradesGet**
> ApplicationUpgrade applicationUpgradesGet(applicationName, apiVersion, timeout)



Get application upgrades

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationName = "applicationName_example"; // String | The name of the application
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      ApplicationUpgrade result = apiInstance.applicationUpgradesGet(applicationName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#applicationUpgradesGet");
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
| **applicationName** | **String**| The name of the application | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**ApplicationUpgrade**](ApplicationUpgrade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The application upgrade |  -  |
| **0** | Error |  -  |

<a id="applicationUpgradesResume"></a>
# **applicationUpgradesResume**
> String applicationUpgradesResume(applicationName, apiVersion, resumeApplicationUpgrade, timeout)



Resume application upgrades

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationName = "applicationName_example"; // String | The name of the application
    String apiVersion = "apiVersion_example"; // String | The version of the api
    ResumeApplicationUpgrade resumeApplicationUpgrade = new ResumeApplicationUpgrade(); // ResumeApplicationUpgrade | The upgrade of the resume application
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.applicationUpgradesResume(applicationName, apiVersion, resumeApplicationUpgrade, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#applicationUpgradesResume");
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
| **applicationName** | **String**| The name of the application | |
| **apiVersion** | **String**| The version of the api | |
| **resumeApplicationUpgrade** | [**ResumeApplicationUpgrade**](ResumeApplicationUpgrade.md)| The upgrade of the resume application | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The resume application upgrade |  -  |
| **0** | Error |  -  |

<a id="applicationUpgradesStart"></a>
# **applicationUpgradesStart**
> String applicationUpgradesStart(applicationName, apiVersion, startApplicationUpgrade, timeout)



Start application upgrades

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationName = "applicationName_example"; // String | The name of the application
    String apiVersion = "apiVersion_example"; // String | The version of the api
    StartApplicationUpgrade startApplicationUpgrade = new StartApplicationUpgrade(); // StartApplicationUpgrade | The description of the start application upgrade
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.applicationUpgradesStart(applicationName, apiVersion, startApplicationUpgrade, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#applicationUpgradesStart");
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
| **applicationName** | **String**| The name of the application | |
| **apiVersion** | **String**| The version of the api | |
| **startApplicationUpgrade** | [**StartApplicationUpgrade**](StartApplicationUpgrade.md)| The description of the start application upgrade | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The start application upgrade |  -  |
| **0** | Error |  -  |

<a id="applicationUpgradesUpdate"></a>
# **applicationUpgradesUpdate**
> String applicationUpgradesUpdate(applicationName, apiVersion, updateApplicationUpgrade, timeout)



Update application upgrades

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationName = "applicationName_example"; // String | The name of the application
    String apiVersion = "apiVersion_example"; // String | The version of the api
    UpdateApplicationUpgrade updateApplicationUpgrade = new UpdateApplicationUpgrade(); // UpdateApplicationUpgrade | The description of the update application upgrade
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.applicationUpgradesUpdate(applicationName, apiVersion, updateApplicationUpgrade, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#applicationUpgradesUpdate");
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
| **applicationName** | **String**| The name of the application | |
| **apiVersion** | **String**| The version of the api | |
| **updateApplicationUpgrade** | [**UpdateApplicationUpgrade**](UpdateApplicationUpgrade.md)| The description of the update application upgrade | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The update application upgrade |  -  |
| **0** | Error |  -  |

<a id="applicationsCreate"></a>
# **applicationsCreate**
> String applicationsCreate(apiVersion, applicationDescription, timeout)



Create applications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the api
    ApplicationDescription applicationDescription = new ApplicationDescription(); // ApplicationDescription | The description of the application
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.applicationsCreate(apiVersion, applicationDescription, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#applicationsCreate");
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
| **apiVersion** | **String**| The version of the api | |
| **applicationDescription** | [**ApplicationDescription**](ApplicationDescription.md)| The description of the application | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The application description |  -  |
| **201** | The application description |  -  |
| **202** | The application description |  -  |
| **0** | Error |  -  |

<a id="applicationsGet"></a>
# **applicationsGet**
> Application applicationsGet(applicationName, apiVersion, timeout)



Get applications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationName = "applicationName_example"; // String | The name of the application
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      Application result = apiInstance.applicationsGet(applicationName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#applicationsGet");
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
| **applicationName** | **String**| The name of the application | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The application |  -  |
| **0** | Error |  -  |

<a id="applicationsList"></a>
# **applicationsList**
> ApplicationList applicationsList(apiVersion, timeout, continuationToken)



List applications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    String continuationToken = "continuationToken_example"; // String | The token of the continuation
    try {
      ApplicationList result = apiInstance.applicationsList(apiVersion, timeout, continuationToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#applicationsList");
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
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |
| **continuationToken** | **String**| The token of the continuation | [optional] |

### Return type

[**ApplicationList**](ApplicationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The application list |  -  |
| **0** | Error |  -  |

<a id="applicationsRemove"></a>
# **applicationsRemove**
> String applicationsRemove(applicationName, apiVersion, forceRemove, timeout)



Remove applications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationName = "applicationName_example"; // String | The name of the application
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Boolean forceRemove = true; // Boolean | The force remove flag to skip services check
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.applicationsRemove(applicationName, apiVersion, forceRemove, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#applicationsRemove");
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
| **applicationName** | **String**| The name of the application | |
| **apiVersion** | **String**| The version of the api | |
| **forceRemove** | **Boolean**| The force remove flag to skip services check | [optional] |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service |  -  |
| **0** | Error |  -  |

<a id="clusterHealthsGet"></a>
# **clusterHealthsGet**
> ClusterHealth clusterHealthsGet(apiVersion, eventsHealthStateFilter, nodesHealthStateFilter, applicationsHealthStateFilter, timeout)



Get cluster healths

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the api
    String eventsHealthStateFilter = "eventsHealthStateFilter_example"; // String | The filter of the events health state
    String nodesHealthStateFilter = "nodesHealthStateFilter_example"; // String | The filter of the nodes health state
    String applicationsHealthStateFilter = "applicationsHealthStateFilter_example"; // String | The filter of the applications health state
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      ClusterHealth result = apiInstance.clusterHealthsGet(apiVersion, eventsHealthStateFilter, nodesHealthStateFilter, applicationsHealthStateFilter, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#clusterHealthsGet");
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
| **apiVersion** | **String**| The version of the api | |
| **eventsHealthStateFilter** | **String**| The filter of the events health state | [optional] |
| **nodesHealthStateFilter** | **String**| The filter of the nodes health state | [optional] |
| **applicationsHealthStateFilter** | **String**| The filter of the applications health state | [optional] |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**ClusterHealth**](ClusterHealth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cluster health |  -  |
| **0** | Error |  -  |

<a id="clusterHealthsSend"></a>
# **clusterHealthsSend**
> String clusterHealthsSend(apiVersion, clusterHealthReport, timeout)



Report cluster healths

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the api
    ClusterHealthReport clusterHealthReport = new ClusterHealthReport(); // ClusterHealthReport | The report of the cluster health
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.clusterHealthsSend(apiVersion, clusterHealthReport, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#clusterHealthsSend");
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
| **apiVersion** | **String**| The version of the api | |
| **clusterHealthReport** | [**ClusterHealthReport**](ClusterHealthReport.md)| The report of the cluster health | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cluster health |  -  |
| **0** | Error |  -  |

<a id="clusterLoadInformationsGet"></a>
# **clusterLoadInformationsGet**
> ClusterLoadInformation clusterLoadInformationsGet(apiVersion, timeout)



Get cluster load informations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      ClusterLoadInformation result = apiInstance.clusterLoadInformationsGet(apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#clusterLoadInformationsGet");
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
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**ClusterLoadInformation**](ClusterLoadInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The load information |  -  |
| **0** | Error |  -  |

<a id="clusterManifestsGet"></a>
# **clusterManifestsGet**
> String clusterManifestsGet(apiVersion, timeout)



Get cluster manifests

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.clusterManifestsGet(apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#clusterManifestsGet");
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
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cluster manifest |  -  |
| **0** | Error |  -  |

<a id="clusterPackagesRegister"></a>
# **clusterPackagesRegister**
> String clusterPackagesRegister(apiVersion, registerClusterPackage, timeout)



Register cluster packages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the api
    RegisterClusterPackage registerClusterPackage = new RegisterClusterPackage(); // RegisterClusterPackage | The package of the register cluster
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.clusterPackagesRegister(apiVersion, registerClusterPackage, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#clusterPackagesRegister");
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
| **apiVersion** | **String**| The version of the api | |
| **registerClusterPackage** | [**RegisterClusterPackage**](RegisterClusterPackage.md)| The package of the register cluster | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cluster upgrade |  -  |
| **0** | Error |  -  |

<a id="clusterPackagesUnregister"></a>
# **clusterPackagesUnregister**
> String clusterPackagesUnregister(apiVersion, unregisterClusterPackage, timeout)



Unregister cluster packages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the api
    UnregisterClusterPackage unregisterClusterPackage = new UnregisterClusterPackage(); // UnregisterClusterPackage | The package of the unregister cluster
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.clusterPackagesUnregister(apiVersion, unregisterClusterPackage, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#clusterPackagesUnregister");
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
| **apiVersion** | **String**| The version of the api | |
| **unregisterClusterPackage** | [**UnregisterClusterPackage**](UnregisterClusterPackage.md)| The package of the unregister cluster | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cluster upgrade |  -  |
| **0** | Error |  -  |

<a id="clusterUpgradesResume"></a>
# **clusterUpgradesResume**
> String clusterUpgradesResume(apiVersion, resumeClusterUpgrade, timeout)



Resume cluster upgrades

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the api
    ResumeClusterUpgrade resumeClusterUpgrade = new ResumeClusterUpgrade(); // ResumeClusterUpgrade | The upgrade of the cluster
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.clusterUpgradesResume(apiVersion, resumeClusterUpgrade, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#clusterUpgradesResume");
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
| **apiVersion** | **String**| The version of the api | |
| **resumeClusterUpgrade** | [**ResumeClusterUpgrade**](ResumeClusterUpgrade.md)| The upgrade of the cluster | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cluster upgrade |  -  |
| **0** | Error |  -  |

<a id="clusterUpgradesRollback"></a>
# **clusterUpgradesRollback**
> String clusterUpgradesRollback(apiVersion, timeout)



Rollback cluster upgrades

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.clusterUpgradesRollback(apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#clusterUpgradesRollback");
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
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cluster upgrade |  -  |
| **0** | Error |  -  |

<a id="clusterUpgradesStart"></a>
# **clusterUpgradesStart**
> String clusterUpgradesStart(apiVersion, startClusterUpgrade, timeout)



Start cluster upgrades

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the api
    StartClusterUpgrade startClusterUpgrade = new StartClusterUpgrade(); // StartClusterUpgrade | The description of the start cluster upgrade
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.clusterUpgradesStart(apiVersion, startClusterUpgrade, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#clusterUpgradesStart");
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
| **apiVersion** | **String**| The version of the api | |
| **startClusterUpgrade** | [**StartClusterUpgrade**](StartClusterUpgrade.md)| The description of the start cluster upgrade | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cluster upgrade |  -  |
| **0** | Error |  -  |

<a id="clusterUpgradesUpdate"></a>
# **clusterUpgradesUpdate**
> String clusterUpgradesUpdate(apiVersion, updateClusterUpgrade, timeout)



Update cluster upgrades

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the api
    UpdateClusterUpgrade updateClusterUpgrade = new UpdateClusterUpgrade(); // UpdateClusterUpgrade | The description of the update cluster upgrade
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.clusterUpgradesUpdate(apiVersion, updateClusterUpgrade, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#clusterUpgradesUpdate");
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
| **apiVersion** | **String**| The version of the api | |
| **updateClusterUpgrade** | [**UpdateClusterUpgrade**](UpdateClusterUpgrade.md)| The description of the update cluster upgrade | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cluster upgrade |  -  |
| **0** | Error |  -  |

<a id="deployedApplicationHealthsGet"></a>
# **deployedApplicationHealthsGet**
> DeployedApplicationHealth deployedApplicationHealthsGet(nodeName, applicationName, apiVersion, eventsHealthStateFilter, deployedServicePackagesHealthStateFilter, timeout)



Get deployed application healths

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String nodeName = "nodeName_example"; // String | The name of the node
    String applicationName = "applicationName_example"; // String | The name of the application
    String apiVersion = "apiVersion_example"; // String | The version of the api
    String eventsHealthStateFilter = "eventsHealthStateFilter_example"; // String | The filter of the events health state
    String deployedServicePackagesHealthStateFilter = "deployedServicePackagesHealthStateFilter_example"; // String | The filter of the deployed service packages health state
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      DeployedApplicationHealth result = apiInstance.deployedApplicationHealthsGet(nodeName, applicationName, apiVersion, eventsHealthStateFilter, deployedServicePackagesHealthStateFilter, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deployedApplicationHealthsGet");
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
| **nodeName** | **String**| The name of the node | |
| **applicationName** | **String**| The name of the application | |
| **apiVersion** | **String**| The version of the api | |
| **eventsHealthStateFilter** | **String**| The filter of the events health state | [optional] |
| **deployedServicePackagesHealthStateFilter** | **String**| The filter of the deployed service packages health state | [optional] |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**DeployedApplicationHealth**](DeployedApplicationHealth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deployed application health |  -  |
| **0** | Error |  -  |

<a id="deployedApplicationHealthsSend"></a>
# **deployedApplicationHealthsSend**
> String deployedApplicationHealthsSend(nodeName, applicationName, apiVersion, deployedApplicationHealthReport, timeout)



Send deployed application health

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String nodeName = "nodeName_example"; // String | The name of the node
    String applicationName = "applicationName_example"; // String | The name of the application
    String apiVersion = "apiVersion_example"; // String | The version of the api
    DeployedApplicationHealthReport deployedApplicationHealthReport = new DeployedApplicationHealthReport(); // DeployedApplicationHealthReport | The report of the deployed application health
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.deployedApplicationHealthsSend(nodeName, applicationName, apiVersion, deployedApplicationHealthReport, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deployedApplicationHealthsSend");
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
| **nodeName** | **String**| The name of the node | |
| **applicationName** | **String**| The name of the application | |
| **apiVersion** | **String**| The version of the api | |
| **deployedApplicationHealthReport** | [**DeployedApplicationHealthReport**](DeployedApplicationHealthReport.md)| The report of the deployed application health | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deployed application health |  -  |
| **0** | Error |  -  |

<a id="deployedApplicationsGet"></a>
# **deployedApplicationsGet**
> DeployedApplication deployedApplicationsGet(nodeName, applicationName, apiVersion, timeout)



Get deployed applications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String nodeName = "nodeName_example"; // String | The name of the node
    String applicationName = "applicationName_example"; // String | The name of the application
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      DeployedApplication result = apiInstance.deployedApplicationsGet(nodeName, applicationName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deployedApplicationsGet");
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
| **nodeName** | **String**| The name of the node | |
| **applicationName** | **String**| The name of the application | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**DeployedApplication**](DeployedApplication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deployed application |  -  |
| **0** | Error |  -  |

<a id="deployedApplicationsList"></a>
# **deployedApplicationsList**
> List&lt;DeployedApplication&gt; deployedApplicationsList(nodeName, apiVersion, timeout)



List deployed applications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String nodeName = "nodeName_example"; // String | The name of the node
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      List<DeployedApplication> result = apiInstance.deployedApplicationsList(nodeName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deployedApplicationsList");
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
| **nodeName** | **String**| The name of the node | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**List&lt;DeployedApplication&gt;**](DeployedApplication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deployed application list |  -  |
| **0** | Error |  -  |

<a id="deployedCodePackagesGet"></a>
# **deployedCodePackagesGet**
> List&lt;DeployedCodePackage&gt; deployedCodePackagesGet(nodeName, applicationName, apiVersion, timeout)



Get deployed code packages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String nodeName = "nodeName_example"; // String | The name of the node
    String applicationName = "applicationName_example"; // String | The name of the application
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      List<DeployedCodePackage> result = apiInstance.deployedCodePackagesGet(nodeName, applicationName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deployedCodePackagesGet");
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
| **nodeName** | **String**| The name of the node | |
| **applicationName** | **String**| The name of the application | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**List&lt;DeployedCodePackage&gt;**](DeployedCodePackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deployed code package |  -  |
| **0** | Error |  -  |

<a id="deployedReplicaDetailsGet"></a>
# **deployedReplicaDetailsGet**
> DeployedReplicaDetail deployedReplicaDetailsGet(nodeName, partitionName, replicaId, apiVersion, timeout)



Get deployed replica details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String nodeName = "nodeName_example"; // String | The name of the node
    String partitionName = "partitionName_example"; // String | The name of the partition
    String replicaId = "replicaId_example"; // String | The id of the replica
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      DeployedReplicaDetail result = apiInstance.deployedReplicaDetailsGet(nodeName, partitionName, replicaId, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deployedReplicaDetailsGet");
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
| **nodeName** | **String**| The name of the node | |
| **partitionName** | **String**| The name of the partition | |
| **replicaId** | **String**| The id of the replica | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**DeployedReplicaDetail**](DeployedReplicaDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deployed replica detail |  -  |
| **0** | Error |  -  |

<a id="deployedReplicasGet"></a>
# **deployedReplicasGet**
> List&lt;DeployedReplica&gt; deployedReplicasGet(nodeName, applicationName, apiVersion, timeout)



Get deployed replicas

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String nodeName = "nodeName_example"; // String | The name of the node
    String applicationName = "applicationName_example"; // String | The name of the application
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      List<DeployedReplica> result = apiInstance.deployedReplicasGet(nodeName, applicationName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deployedReplicasGet");
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
| **nodeName** | **String**| The name of the node | |
| **applicationName** | **String**| The name of the application | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**List&lt;DeployedReplica&gt;**](DeployedReplica.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deployed replica |  -  |
| **0** | Error |  -  |

<a id="deployedServicePackageHealthsGet"></a>
# **deployedServicePackageHealthsGet**
> DeployedServicePackageHealth deployedServicePackageHealthsGet(nodeName, applicationName, servicePackageName, apiVersion, eventsHealthStateFilter, timeout)



Get deployed service package healths

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String nodeName = "nodeName_example"; // String | The name of the node
    String applicationName = "applicationName_example"; // String | The name of the application
    String servicePackageName = "servicePackageName_example"; // String | The name of the service package
    String apiVersion = "apiVersion_example"; // String | The version of the api
    String eventsHealthStateFilter = "eventsHealthStateFilter_example"; // String | The filter of the events health state
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      DeployedServicePackageHealth result = apiInstance.deployedServicePackageHealthsGet(nodeName, applicationName, servicePackageName, apiVersion, eventsHealthStateFilter, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deployedServicePackageHealthsGet");
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
| **nodeName** | **String**| The name of the node | |
| **applicationName** | **String**| The name of the application | |
| **servicePackageName** | **String**| The name of the service package | |
| **apiVersion** | **String**| The version of the api | |
| **eventsHealthStateFilter** | **String**| The filter of the events health state | [optional] |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**DeployedServicePackageHealth**](DeployedServicePackageHealth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deployed service package health |  -  |
| **0** | Error |  -  |

<a id="deployedServicePackageHealthsSend"></a>
# **deployedServicePackageHealthsSend**
> String deployedServicePackageHealthsSend(nodeName, applicationName, serviceManifestName, apiVersion, deployedServicePackageHealthReport, timeout)



Send deployed service package health

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String nodeName = "nodeName_example"; // String | The name of the node
    String applicationName = "applicationName_example"; // String | The name of the application
    String serviceManifestName = "serviceManifestName_example"; // String | The name of the service manifest
    String apiVersion = "apiVersion_example"; // String | The version of the api
    DeployedServiceHealthReport deployedServicePackageHealthReport = new DeployedServiceHealthReport(); // DeployedServiceHealthReport | The report of the deployed service package health
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.deployedServicePackageHealthsSend(nodeName, applicationName, serviceManifestName, apiVersion, deployedServicePackageHealthReport, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deployedServicePackageHealthsSend");
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
| **nodeName** | **String**| The name of the node | |
| **applicationName** | **String**| The name of the application | |
| **serviceManifestName** | **String**| The name of the service manifest | |
| **apiVersion** | **String**| The version of the api | |
| **deployedServicePackageHealthReport** | [**DeployedServiceHealthReport**](DeployedServiceHealthReport.md)| The report of the deployed service package health | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deployed service package health |  -  |
| **0** | Error |  -  |

<a id="deployedServicePackagesGet"></a>
# **deployedServicePackagesGet**
> List&lt;DeployedServicePackage&gt; deployedServicePackagesGet(nodeName, applicationName, apiVersion, timeout)



Get deployed service packages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String nodeName = "nodeName_example"; // String | The name of the node
    String applicationName = "applicationName_example"; // String | The name of the application
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      List<DeployedServicePackage> result = apiInstance.deployedServicePackagesGet(nodeName, applicationName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deployedServicePackagesGet");
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
| **nodeName** | **String**| The name of the node | |
| **applicationName** | **String**| The name of the application | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**List&lt;DeployedServicePackage&gt;**](DeployedServicePackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deployed service package |  -  |
| **0** | Error |  -  |

<a id="deployedServiceTypesGet"></a>
# **deployedServiceTypesGet**
> List&lt;DeployedServiceType&gt; deployedServiceTypesGet(nodeName, applicationName, apiVersion, timeout)



Get deployed service types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String nodeName = "nodeName_example"; // String | The name of the node
    String applicationName = "applicationName_example"; // String | The name of the application
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      List<DeployedServiceType> result = apiInstance.deployedServiceTypesGet(nodeName, applicationName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deployedServiceTypesGet");
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
| **nodeName** | **String**| The name of the node | |
| **applicationName** | **String**| The name of the application | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**List&lt;DeployedServiceType&gt;**](DeployedServiceType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deployed service type |  -  |
| **0** | Error |  -  |

<a id="nodeHealthsGet"></a>
# **nodeHealthsGet**
> NodeHealth nodeHealthsGet(nodeName, apiVersion, eventsHealthStateFilter, timeout)



Get node healths

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String nodeName = "nodeName_example"; // String | The name of the node
    String apiVersion = "apiVersion_example"; // String | The version of the api
    String eventsHealthStateFilter = "eventsHealthStateFilter_example"; // String | The filter of the events health state
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      NodeHealth result = apiInstance.nodeHealthsGet(nodeName, apiVersion, eventsHealthStateFilter, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nodeHealthsGet");
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
| **nodeName** | **String**| The name of the node | |
| **apiVersion** | **String**| The version of the api | |
| **eventsHealthStateFilter** | **String**| The filter of the events health state | [optional] |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**NodeHealth**](NodeHealth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The node health |  -  |
| **0** | Error |  -  |

<a id="nodeHealthsSend"></a>
# **nodeHealthsSend**
> String nodeHealthsSend(nodeName, apiVersion, nodeHealthReport, timeout)



Send node health

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String nodeName = "nodeName_example"; // String | The name of the node
    String apiVersion = "apiVersion_example"; // String | The version of the api
    NodeHealthReport nodeHealthReport = new NodeHealthReport(); // NodeHealthReport | The report of the node health
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.nodeHealthsSend(nodeName, apiVersion, nodeHealthReport, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nodeHealthsSend");
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
| **nodeName** | **String**| The name of the node | |
| **apiVersion** | **String**| The version of the api | |
| **nodeHealthReport** | [**NodeHealthReport**](NodeHealthReport.md)| The report of the node health | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The node health |  -  |
| **0** | Error |  -  |

<a id="nodeLoadInformationsGet"></a>
# **nodeLoadInformationsGet**
> NodeLoadInformation nodeLoadInformationsGet(nodeName, apiVersion, timeout)



Get node load informations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String nodeName = "nodeName_example"; // String | The name of the node
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      NodeLoadInformation result = apiInstance.nodeLoadInformationsGet(nodeName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nodeLoadInformationsGet");
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
| **nodeName** | **String**| The name of the node | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**NodeLoadInformation**](NodeLoadInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The node load information |  -  |
| **0** | Error |  -  |

<a id="nodeStatesRemove"></a>
# **nodeStatesRemove**
> String nodeStatesRemove(nodeName, apiVersion, timeout)



Remove node states

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String nodeName = "nodeName_example"; // String | The name of the node
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.nodeStatesRemove(nodeName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nodeStatesRemove");
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
| **nodeName** | **String**| The name of the node | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The node state |  -  |
| **0** | Error |  -  |

<a id="nodesDisable"></a>
# **nodesDisable**
> String nodesDisable(nodeName, apiVersion, disableNode, timeout)



Disable nodes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String nodeName = "nodeName_example"; // String | The name of the node
    String apiVersion = "apiVersion_example"; // String | The version of the api
    DisableNode disableNode = new DisableNode(); // DisableNode | The node
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.nodesDisable(nodeName, apiVersion, disableNode, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nodesDisable");
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
| **nodeName** | **String**| The name of the node | |
| **apiVersion** | **String**| The version of the api | |
| **disableNode** | [**DisableNode**](DisableNode.md)| The node | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The node |  -  |
| **0** | Error |  -  |

<a id="nodesEnable"></a>
# **nodesEnable**
> String nodesEnable(nodeName, apiVersion, timeout)



Enable nodes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String nodeName = "nodeName_example"; // String | The name of the node
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.nodesEnable(nodeName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nodesEnable");
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
| **nodeName** | **String**| The name of the node | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The node |  -  |
| **0** | Error |  -  |

<a id="nodesGet"></a>
# **nodesGet**
> Node nodesGet(nodeName, apiVersion, timeout)



Get nodes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String nodeName = "nodeName_example"; // String | The name of the node
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      Node result = apiInstance.nodesGet(nodeName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nodesGet");
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
| **nodeName** | **String**| The name of the node | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**Node**](Node.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The node |  -  |
| **0** | Error |  -  |

<a id="nodesList"></a>
# **nodesList**
> NodeList nodesList(apiVersion, timeout, continuationToken)



List nodes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    String continuationToken = "continuationToken_example"; // String | The token of the continuation
    try {
      NodeList result = apiInstance.nodesList(apiVersion, timeout, continuationToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nodesList");
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
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |
| **continuationToken** | **String**| The token of the continuation | [optional] |

### Return type

[**NodeList**](NodeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The node list |  -  |
| **0** | Error |  -  |

<a id="partitionHealthsGet"></a>
# **partitionHealthsGet**
> PartitionHealth partitionHealthsGet(partitionId, apiVersion, eventsHealthStateFilter, replicasHealthStateFilter, timeout)



Get partition healths

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String partitionId = "partitionId_example"; // String | The id of the partition
    String apiVersion = "apiVersion_example"; // String | The version of the api
    String eventsHealthStateFilter = "eventsHealthStateFilter_example"; // String | The filter of the events health state
    String replicasHealthStateFilter = "replicasHealthStateFilter_example"; // String | The filter of the replicas health state
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      PartitionHealth result = apiInstance.partitionHealthsGet(partitionId, apiVersion, eventsHealthStateFilter, replicasHealthStateFilter, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#partitionHealthsGet");
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
| **partitionId** | **String**| The id of the partition | |
| **apiVersion** | **String**| The version of the api | |
| **eventsHealthStateFilter** | **String**| The filter of the events health state | [optional] |
| **replicasHealthStateFilter** | **String**| The filter of the replicas health state | [optional] |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**PartitionHealth**](PartitionHealth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The partition health |  -  |
| **0** | Error |  -  |

<a id="partitionHealthsSend"></a>
# **partitionHealthsSend**
> String partitionHealthsSend(partitionId, apiVersion, partitionHealthReport, timeout)



Send partition health

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String partitionId = "partitionId_example"; // String | The id of the partition
    String apiVersion = "apiVersion_example"; // String | The version of the api
    PartitionHealthReport partitionHealthReport = new PartitionHealthReport(); // PartitionHealthReport | The report of the partition health
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.partitionHealthsSend(partitionId, apiVersion, partitionHealthReport, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#partitionHealthsSend");
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
| **partitionId** | **String**| The id of the partition | |
| **apiVersion** | **String**| The version of the api | |
| **partitionHealthReport** | [**PartitionHealthReport**](PartitionHealthReport.md)| The report of the partition health | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The partition health |  -  |
| **0** | Error |  -  |

<a id="partitionListsRepair"></a>
# **partitionListsRepair**
> String partitionListsRepair(serviceName, apiVersion, timeout)



Repair partition lists

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.partitionListsRepair(serviceName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#partitionListsRepair");
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
| **serviceName** | **String**| The name of the service | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The repair partition |  -  |
| **0** | Error |  -  |

<a id="partitionLoadInformationsGet"></a>
# **partitionLoadInformationsGet**
> PartitionLoadInformation partitionLoadInformationsGet(partitionId, apiVersion, timeout)



Get partition load informations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String partitionId = "partitionId_example"; // String | The id of the partition
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      PartitionLoadInformation result = apiInstance.partitionLoadInformationsGet(partitionId, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#partitionLoadInformationsGet");
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
| **partitionId** | **String**| The id of the partition | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**PartitionLoadInformation**](PartitionLoadInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The partition load information |  -  |
| **0** | Error |  -  |

<a id="partitionLoadsReset"></a>
# **partitionLoadsReset**
> String partitionLoadsReset(partitionId, apiVersion, timeout)



Reset partition loads

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String partitionId = "partitionId_example"; // String | The id of the partition
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.partitionLoadsReset(partitionId, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#partitionLoadsReset");
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
| **partitionId** | **String**| The id of the partition | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The reset partition load |  -  |
| **0** | Error |  -  |

<a id="partitionsGet"></a>
# **partitionsGet**
> Partition partitionsGet(serviceName, partitionId, apiVersion, timeout)



Get partitions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service
    String partitionId = "partitionId_example"; // String | The id of the partition
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      Partition result = apiInstance.partitionsGet(serviceName, partitionId, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#partitionsGet");
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
| **serviceName** | **String**| The name of the service | |
| **partitionId** | **String**| The id of the partition | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**Partition**](Partition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The partitions |  -  |
| **0** | Error |  -  |

<a id="partitionsList"></a>
# **partitionsList**
> PartitionList partitionsList(serviceName, apiVersion, timeout)



List partitions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      PartitionList result = apiInstance.partitionsList(serviceName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#partitionsList");
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
| **serviceName** | **String**| The name of the service | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**PartitionList**](PartitionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The partitions |  -  |
| **0** | Error |  -  |

<a id="partitionsRepair"></a>
# **partitionsRepair**
> String partitionsRepair(partitionId, apiVersion, timeout)



Repair partitions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String partitionId = "partitionId_example"; // String | The id of the partition
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.partitionsRepair(partitionId, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#partitionsRepair");
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
| **partitionId** | **String**| The id of the partition | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The repair partition |  -  |
| **0** | Error |  -  |

<a id="replicaHealthsGet"></a>
# **replicaHealthsGet**
> ReplicaHealth replicaHealthsGet(partitionId, replicaId, apiVersion, eventsHealthStateFilter, timeout)



Get replica healths

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String partitionId = "partitionId_example"; // String | The id of the partition
    String replicaId = "replicaId_example"; // String | The id of the replica
    String apiVersion = "apiVersion_example"; // String | The version of the api
    String eventsHealthStateFilter = "eventsHealthStateFilter_example"; // String | The filter of the events health state
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      ReplicaHealth result = apiInstance.replicaHealthsGet(partitionId, replicaId, apiVersion, eventsHealthStateFilter, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#replicaHealthsGet");
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
| **partitionId** | **String**| The id of the partition | |
| **replicaId** | **String**| The id of the replica | |
| **apiVersion** | **String**| The version of the api | |
| **eventsHealthStateFilter** | **String**| The filter of the events health state | [optional] |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**ReplicaHealth**](ReplicaHealth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The replica health |  -  |
| **0** | Error |  -  |

<a id="replicaHealthsSend"></a>
# **replicaHealthsSend**
> String replicaHealthsSend(partitionId, replicaId, apiVersion, replicaHealthReport, timeout)



Send replica healths

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String partitionId = "partitionId_example"; // String | The id of the partition
    String replicaId = "replicaId_example"; // String | The id of the replica
    String apiVersion = "apiVersion_example"; // String | The version of the api
    ReplicaHealthReport replicaHealthReport = new ReplicaHealthReport(); // ReplicaHealthReport | The report of the replica health
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.replicaHealthsSend(partitionId, replicaId, apiVersion, replicaHealthReport, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#replicaHealthsSend");
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
| **partitionId** | **String**| The id of the partition | |
| **replicaId** | **String**| The id of the replica | |
| **apiVersion** | **String**| The version of the api | |
| **replicaHealthReport** | [**ReplicaHealthReport**](ReplicaHealthReport.md)| The report of the replica health | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The replica health |  -  |
| **0** | Error |  -  |

<a id="replicaLoadInformationsGet"></a>
# **replicaLoadInformationsGet**
> ReplicaLoadInformation replicaLoadInformationsGet(partitionId, replicaId, apiVersion, timeout)



Get replica load informations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String partitionId = "partitionId_example"; // String | The id of the partition
    String replicaId = "replicaId_example"; // String | The id of the replica
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      ReplicaLoadInformation result = apiInstance.replicaLoadInformationsGet(partitionId, replicaId, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#replicaLoadInformationsGet");
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
| **partitionId** | **String**| The id of the partition | |
| **replicaId** | **String**| The id of the replica | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**ReplicaLoadInformation**](ReplicaLoadInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The replica load information |  -  |
| **0** | Error |  -  |

<a id="replicasGet"></a>
# **replicasGet**
> Replica replicasGet(partitionId, replicaId, apiVersion, timeout)



Get replicas

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String partitionId = "partitionId_example"; // String | The id of the partition
    String replicaId = "replicaId_example"; // String | The id of the replica
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      Replica result = apiInstance.replicasGet(partitionId, replicaId, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#replicasGet");
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
| **partitionId** | **String**| The id of the partition | |
| **replicaId** | **String**| The id of the replica | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**Replica**](Replica.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The replica |  -  |
| **0** | Error |  -  |

<a id="replicasList"></a>
# **replicasList**
> ReplicaList replicasList(partitionId, apiVersion, timeout)



List replicas

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String partitionId = "partitionId_example"; // String | The id of the partition
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      ReplicaList result = apiInstance.replicasList(partitionId, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#replicasList");
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
| **partitionId** | **String**| The id of the partition | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**ReplicaList**](ReplicaList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The replica list |  -  |
| **0** | Error |  -  |

<a id="serviceDescriptionsGet"></a>
# **serviceDescriptionsGet**
> ServiceDescription serviceDescriptionsGet(serviceName, apiVersion, timeout)



Get service descriptions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      ServiceDescription result = apiInstance.serviceDescriptionsGet(serviceName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#serviceDescriptionsGet");
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
| **serviceName** | **String**| The name of the service | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**ServiceDescription**](ServiceDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service description |  -  |
| **0** | Error |  -  |

<a id="serviceFromTemplatesCreate"></a>
# **serviceFromTemplatesCreate**
> String serviceFromTemplatesCreate(applicationName, apiVersion, serviceDescriptionTemplate, timeout)



Create service from templates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationName = "applicationName_example"; // String | The name of the application
    String apiVersion = "apiVersion_example"; // String | The version of the api
    ServiceDescriptionTemplate serviceDescriptionTemplate = new ServiceDescriptionTemplate(); // ServiceDescriptionTemplate | The template of the service description
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.serviceFromTemplatesCreate(applicationName, apiVersion, serviceDescriptionTemplate, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#serviceFromTemplatesCreate");
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
| **applicationName** | **String**| The name of the application | |
| **apiVersion** | **String**| The version of the api | |
| **serviceDescriptionTemplate** | [**ServiceDescriptionTemplate**](ServiceDescriptionTemplate.md)| The template of the service description | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service description template |  -  |
| **201** | The service description template |  -  |
| **202** | The service description template |  -  |
| **0** | Error |  -  |

<a id="serviceGroupDescriptionsGet"></a>
# **serviceGroupDescriptionsGet**
> ServiceGroupDescription serviceGroupDescriptionsGet(applicationName, serviceName, apiVersion, timeout)



Get service group descriptions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationName = "applicationName_example"; // String | The name of the application
    String serviceName = "serviceName_example"; // String | The name of the service
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      ServiceGroupDescription result = apiInstance.serviceGroupDescriptionsGet(applicationName, serviceName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#serviceGroupDescriptionsGet");
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
| **applicationName** | **String**| The name of the application | |
| **serviceName** | **String**| The name of the service | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**ServiceGroupDescription**](ServiceGroupDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service group description |  -  |
| **0** | Error |  -  |

<a id="serviceGroupFromTemplatesCreate"></a>
# **serviceGroupFromTemplatesCreate**
> String serviceGroupFromTemplatesCreate(applicationName, apiVersion, serviceDescriptionTemplate, timeout)



Create service group from templates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationName = "applicationName_example"; // String | The name of the application
    String apiVersion = "apiVersion_example"; // String | The version of the api
    ServiceDescriptionTemplate serviceDescriptionTemplate = new ServiceDescriptionTemplate(); // ServiceDescriptionTemplate | The template of the service description
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.serviceGroupFromTemplatesCreate(applicationName, apiVersion, serviceDescriptionTemplate, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#serviceGroupFromTemplatesCreate");
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
| **applicationName** | **String**| The name of the application | |
| **apiVersion** | **String**| The version of the api | |
| **serviceDescriptionTemplate** | [**ServiceDescriptionTemplate**](ServiceDescriptionTemplate.md)| The template of the service description | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service group description template |  -  |
| **201** | The service group description template |  -  |
| **202** | The service group description template |  -  |
| **0** | Error |  -  |

<a id="serviceGroupMembersGet"></a>
# **serviceGroupMembersGet**
> ServiceGroupMember serviceGroupMembersGet(applicationName, serviceName, apiVersion, timeout)



Get service group members

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationName = "applicationName_example"; // String | The name of the application
    String serviceName = "serviceName_example"; // String | The name of the service
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      ServiceGroupMember result = apiInstance.serviceGroupMembersGet(applicationName, serviceName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#serviceGroupMembersGet");
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
| **applicationName** | **String**| The name of the application | |
| **serviceName** | **String**| The name of the service | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**ServiceGroupMember**](ServiceGroupMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service group description |  -  |
| **0** | Error |  -  |

<a id="serviceGroupsCreate"></a>
# **serviceGroupsCreate**
> String serviceGroupsCreate(applicationName, apiVersion, createServiceGroupDescription, timeout)



Create service groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationName = "applicationName_example"; // String | The name of the service group
    String apiVersion = "apiVersion_example"; // String | The version of the api
    CreateServiceGroupDescription createServiceGroupDescription = new CreateServiceGroupDescription(); // CreateServiceGroupDescription | The description of the service group
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.serviceGroupsCreate(applicationName, apiVersion, createServiceGroupDescription, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#serviceGroupsCreate");
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
| **applicationName** | **String**| The name of the service group | |
| **apiVersion** | **String**| The version of the api | |
| **createServiceGroupDescription** | [**CreateServiceGroupDescription**](CreateServiceGroupDescription.md)| The description of the service group | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service description |  -  |
| **201** | The service description |  -  |
| **202** | The service description |  -  |
| **0** | Error |  -  |

<a id="serviceGroupsRemove"></a>
# **serviceGroupsRemove**
> String serviceGroupsRemove(applicationName, serviceName, apiVersion, timeout)



Remove service groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationName = "applicationName_example"; // String | The name of the application
    String serviceName = "serviceName_example"; // String | The name of the service
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.serviceGroupsRemove(applicationName, serviceName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#serviceGroupsRemove");
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
| **applicationName** | **String**| The name of the application | |
| **serviceName** | **String**| The name of the service | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service |  -  |
| **0** | Error |  -  |

<a id="serviceGroupsUpdate"></a>
# **serviceGroupsUpdate**
> String serviceGroupsUpdate(applicationName, serviceName, apiVersion, updateServiceGroupDescription, timeout)



Update service groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationName = "applicationName_example"; // String | The name of the application
    String serviceName = "serviceName_example"; // String | The name of the service
    String apiVersion = "apiVersion_example"; // String | The version of the api
    UpdateServiceGroupDescription updateServiceGroupDescription = new UpdateServiceGroupDescription(); // UpdateServiceGroupDescription | The description of the service group update
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.serviceGroupsUpdate(applicationName, serviceName, apiVersion, updateServiceGroupDescription, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#serviceGroupsUpdate");
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
| **applicationName** | **String**| The name of the application | |
| **serviceName** | **String**| The name of the service | |
| **apiVersion** | **String**| The version of the api | |
| **updateServiceGroupDescription** | [**UpdateServiceGroupDescription**](UpdateServiceGroupDescription.md)| The description of the service group update | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service group update description |  -  |
| **0** | Error |  -  |

<a id="serviceHealthsGet"></a>
# **serviceHealthsGet**
> ServiceHealth serviceHealthsGet(serviceName, apiVersion, timeout)



Get service healths

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      ServiceHealth result = apiInstance.serviceHealthsGet(serviceName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#serviceHealthsGet");
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
| **serviceName** | **String**| The name of the service | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**ServiceHealth**](ServiceHealth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service health |  -  |
| **0** | Error |  -  |

<a id="serviceHealthsSend"></a>
# **serviceHealthsSend**
> String serviceHealthsSend(serviceName, apiVersion, serviceHealthReport, timeout)



Send service healths

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service
    String apiVersion = "apiVersion_example"; // String | The version of the api
    ServiceHealthReport serviceHealthReport = new ServiceHealthReport(); // ServiceHealthReport | The report of the service health
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.serviceHealthsSend(serviceName, apiVersion, serviceHealthReport, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#serviceHealthsSend");
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
| **serviceName** | **String**| The name of the service | |
| **apiVersion** | **String**| The version of the api | |
| **serviceHealthReport** | [**ServiceHealthReport**](ServiceHealthReport.md)| The report of the service health | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service health |  -  |
| **0** | Error |  -  |

<a id="serviceManifestsGet"></a>
# **serviceManifestsGet**
> ServiceManifest serviceManifestsGet(applicationTypeName, applicationTypeVersion, serviceManifestName, apiVersion, timeout)



Get service manifests

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationTypeName = "applicationTypeName_example"; // String | The name of the application type
    String applicationTypeVersion = "applicationTypeVersion_example"; // String | The version of the application type
    String serviceManifestName = "serviceManifestName_example"; // String | The name of the service manifest
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      ServiceManifest result = apiInstance.serviceManifestsGet(applicationTypeName, applicationTypeVersion, serviceManifestName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#serviceManifestsGet");
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
| **applicationTypeName** | **String**| The name of the application type | |
| **applicationTypeVersion** | **String**| The version of the application type | |
| **serviceManifestName** | **String**| The name of the service manifest | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**ServiceManifest**](ServiceManifest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service manifest |  -  |
| **0** | Error |  -  |

<a id="serviceTypesGet"></a>
# **serviceTypesGet**
> List&lt;ServiceType&gt; serviceTypesGet(applicationTypeName, applicationTypeVersion, apiVersion, timeout)



Get service types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationTypeName = "applicationTypeName_example"; // String | The name of the application type
    String applicationTypeVersion = "applicationTypeVersion_example"; // String | The version of the application type
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      List<ServiceType> result = apiInstance.serviceTypesGet(applicationTypeName, applicationTypeVersion, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#serviceTypesGet");
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
| **applicationTypeName** | **String**| The name of the application type | |
| **applicationTypeVersion** | **String**| The version of the application type | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**List&lt;ServiceType&gt;**](ServiceType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service type |  -  |
| **0** | Error |  -  |

<a id="servicesCreate"></a>
# **servicesCreate**
> String servicesCreate(applicationName, apiVersion, createServiceDescription, timeout)



Create services

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationName = "applicationName_example"; // String | The name of the application
    String apiVersion = "apiVersion_example"; // String | The version of the api
    CreateServiceDescription createServiceDescription = new CreateServiceDescription(); // CreateServiceDescription | The description of the service
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.servicesCreate(applicationName, apiVersion, createServiceDescription, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#servicesCreate");
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
| **applicationName** | **String**| The name of the application | |
| **apiVersion** | **String**| The version of the api | |
| **createServiceDescription** | [**CreateServiceDescription**](CreateServiceDescription.md)| The description of the service | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service description |  -  |
| **201** | The service description |  -  |
| **202** | The service description |  -  |
| **0** | Error |  -  |

<a id="servicesGet"></a>
# **servicesGet**
> Service servicesGet(applicationName, serviceName, apiVersion, timeout)



Get services

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationName = "applicationName_example"; // String | The name of the application
    String serviceName = "serviceName_example"; // String | The name of the service
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      Service result = apiInstance.servicesGet(applicationName, serviceName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#servicesGet");
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
| **applicationName** | **String**| The name of the application | |
| **serviceName** | **String**| The name of the service | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**Service**](Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service |  -  |
| **0** | Error |  -  |

<a id="servicesList"></a>
# **servicesList**
> ServiceList servicesList(applicationName, apiVersion, timeout)



List services

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String applicationName = "applicationName_example"; // String | The name of the application
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      ServiceList result = apiInstance.servicesList(applicationName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#servicesList");
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
| **applicationName** | **String**| The name of the application | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**ServiceList**](ServiceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service list |  -  |
| **0** | Error |  -  |

<a id="servicesRemove"></a>
# **servicesRemove**
> String servicesRemove(serviceName, apiVersion, timeout)



Remove services

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.servicesRemove(serviceName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#servicesRemove");
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
| **serviceName** | **String**| The name of the service | |
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service |  -  |
| **0** | Error |  -  |

<a id="servicesResolve"></a>
# **servicesResolve**
> ResolvedServicePartition servicesResolve(serviceName, apiVersion, partitionKeyType, partitionKeyValue, previousRspVersion, timeout)



Resolve services

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer partitionKeyType = 56; // Integer | The type of the partition key
    String partitionKeyValue = "partitionKeyValue_example"; // String | The value of the partition key
    String previousRspVersion = "previousRspVersion_example"; // String | The version of the previous rsp
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      ResolvedServicePartition result = apiInstance.servicesResolve(serviceName, apiVersion, partitionKeyType, partitionKeyValue, previousRspVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#servicesResolve");
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
| **serviceName** | **String**| The name of the service | |
| **apiVersion** | **String**| The version of the api | |
| **partitionKeyType** | **Integer**| The type of the partition key | [optional] |
| **partitionKeyValue** | **String**| The value of the partition key | [optional] |
| **previousRspVersion** | **String**| The version of the previous rsp | [optional] |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**ResolvedServicePartition**](ResolvedServicePartition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The partition |  -  |
| **0** | Error |  -  |

<a id="servicesUpdate"></a>
# **servicesUpdate**
> String servicesUpdate(serviceName, apiVersion, updateServiceDescription, timeout)



Update services

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service
    String apiVersion = "apiVersion_example"; // String | The version of the api
    UpdateServiceDescription updateServiceDescription = new UpdateServiceDescription(); // UpdateServiceDescription | The description of the service update
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      String result = apiInstance.servicesUpdate(serviceName, apiVersion, updateServiceDescription, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#servicesUpdate");
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
| **serviceName** | **String**| The name of the service | |
| **apiVersion** | **String**| The version of the api | |
| **updateServiceDescription** | [**UpdateServiceDescription**](UpdateServiceDescription.md)| The description of the service update | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service update description |  -  |
| **0** | Error |  -  |

<a id="upgradeProgressesGet"></a>
# **upgradeProgressesGet**
> ClusterUpgradeProgress upgradeProgressesGet(apiVersion, timeout)



Get upgrade progresses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local:19080");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the api
    Integer timeout = 56; // Integer | The timeout in seconds
    try {
      ClusterUpgradeProgress result = apiInstance.upgradeProgressesGet(apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#upgradeProgressesGet");
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
| **apiVersion** | **String**| The version of the api | |
| **timeout** | **Integer**| The timeout in seconds | [optional] |

### Return type

[**ClusterUpgradeProgress**](ClusterUpgradeProgress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The upgrade progress |  -  |
| **0** | Error |  -  |

