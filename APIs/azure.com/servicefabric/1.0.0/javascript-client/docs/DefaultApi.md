# ServiceFabricClient.DefaultApi

All URIs are relative to *https://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicationHealthsGet**](DefaultApi.md#applicationHealthsGet) | **GET** /Applications/{applicationName}/$/GetHealth | 
[**applicationHealthsSend**](DefaultApi.md#applicationHealthsSend) | **POST** /Applications/{applicationName}/$/ReportHealth | 
[**applicationManifestsGet**](DefaultApi.md#applicationManifestsGet) | **GET** /ApplicationTypes/{applicationTypeName}/$/GetApplicationManifest | 
[**applicationTypesGet**](DefaultApi.md#applicationTypesGet) | **GET** /ApplicationTypes/{applicationTypeName} | 
[**applicationTypesList**](DefaultApi.md#applicationTypesList) | **GET** /ApplicationTypes | 
[**applicationTypesRegister**](DefaultApi.md#applicationTypesRegister) | **POST** /ApplicationTypes/$/Provision | 
[**applicationTypesUnregister**](DefaultApi.md#applicationTypesUnregister) | **POST** /ApplicationTypes/{applicationTypeName}/$/Unprovision | 
[**applicationUpgradeRollbacksStart**](DefaultApi.md#applicationUpgradeRollbacksStart) | **POST** /Applications/{applicationName}/$/RollbackUpgrade | 
[**applicationUpgradesGet**](DefaultApi.md#applicationUpgradesGet) | **GET** /Applications/{applicationName}/$/GetUpgradeProgress | 
[**applicationUpgradesResume**](DefaultApi.md#applicationUpgradesResume) | **POST** /Applications/{applicationName}/$/MoveNextUpgradeDomain | 
[**applicationUpgradesStart**](DefaultApi.md#applicationUpgradesStart) | **POST** /Applications/{applicationName}/$/Upgrade | 
[**applicationUpgradesUpdate**](DefaultApi.md#applicationUpgradesUpdate) | **POST** /Applications/{applicationName}/$/UpdateUpgrade | 
[**applicationsCreate**](DefaultApi.md#applicationsCreate) | **POST** /Applications/$/Create | 
[**applicationsGet**](DefaultApi.md#applicationsGet) | **GET** /Applications/{applicationName} | 
[**applicationsList**](DefaultApi.md#applicationsList) | **GET** /Applications | 
[**applicationsRemove**](DefaultApi.md#applicationsRemove) | **POST** /Applications/{applicationName}/$/Delete | 
[**clusterHealthsGet**](DefaultApi.md#clusterHealthsGet) | **GET** /$/GetClusterHealth | 
[**clusterHealthsSend**](DefaultApi.md#clusterHealthsSend) | **POST** /$/ReportClusterHealth | 
[**clusterLoadInformationsGet**](DefaultApi.md#clusterLoadInformationsGet) | **GET** /$/GetLoadInformation | 
[**clusterManifestsGet**](DefaultApi.md#clusterManifestsGet) | **GET** /$/GetClusterManifest | 
[**clusterPackagesRegister**](DefaultApi.md#clusterPackagesRegister) | **POST** /$/Provision | 
[**clusterPackagesUnregister**](DefaultApi.md#clusterPackagesUnregister) | **POST** /$/Unprovision | 
[**clusterUpgradesResume**](DefaultApi.md#clusterUpgradesResume) | **POST** /$/MoveToNextUpgradeDomain | 
[**clusterUpgradesRollback**](DefaultApi.md#clusterUpgradesRollback) | **POST** /$/RollbackUpgrade | 
[**clusterUpgradesStart**](DefaultApi.md#clusterUpgradesStart) | **POST** /$/Upgrade | 
[**clusterUpgradesUpdate**](DefaultApi.md#clusterUpgradesUpdate) | **POST** /$/UpdateUpgrade | 
[**deployedApplicationHealthsGet**](DefaultApi.md#deployedApplicationHealthsGet) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationName}/$/GetHealth | 
[**deployedApplicationHealthsSend**](DefaultApi.md#deployedApplicationHealthsSend) | **POST** /Nodes/{nodeName}/$/GetApplications/{applicationName}/$/ReportHealth | 
[**deployedApplicationsGet**](DefaultApi.md#deployedApplicationsGet) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationName} | 
[**deployedApplicationsList**](DefaultApi.md#deployedApplicationsList) | **GET** /Nodes/{nodeName}/$/GetApplications | 
[**deployedCodePackagesGet**](DefaultApi.md#deployedCodePackagesGet) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationName}/$/GetCodePackages | 
[**deployedReplicaDetailsGet**](DefaultApi.md#deployedReplicaDetailsGet) | **GET** /Nodes/{nodeName}/$/GetPartitions/{partitionName}/$/GetReplicas/{replicaId}/$/GetDetail | 
[**deployedReplicasGet**](DefaultApi.md#deployedReplicasGet) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationName}/$/GetReplicas | 
[**deployedServicePackageHealthsGet**](DefaultApi.md#deployedServicePackageHealthsGet) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationName}/$/GetServicePackages/{servicePackageName}/$/GetHealth | 
[**deployedServicePackageHealthsSend**](DefaultApi.md#deployedServicePackageHealthsSend) | **POST** /Nodes/{nodeName}/$/GetApplications/{applicationName}/$/GetServicePackages/{serviceManifestName}/$/ReportHealth | 
[**deployedServicePackagesGet**](DefaultApi.md#deployedServicePackagesGet) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationName}/$/GetServicePackages | 
[**deployedServiceTypesGet**](DefaultApi.md#deployedServiceTypesGet) | **GET** /Nodes/{nodeName}/$/GetApplications/{applicationName}/$/GetServiceTypes | 
[**nodeHealthsGet**](DefaultApi.md#nodeHealthsGet) | **GET** /Nodes/{nodeName}/$/GetHealth | 
[**nodeHealthsSend**](DefaultApi.md#nodeHealthsSend) | **POST** /Nodes/{nodeName}/$/ReportHealth | 
[**nodeLoadInformationsGet**](DefaultApi.md#nodeLoadInformationsGet) | **GET** /Nodes/{nodeName}/$/GetLoadInformation | 
[**nodeStatesRemove**](DefaultApi.md#nodeStatesRemove) | **POST** /Nodes/{nodeName}/$/RemoveNodeState | 
[**nodesDisable**](DefaultApi.md#nodesDisable) | **POST** /Nodes/{nodeName}/$/Deactivate | 
[**nodesEnable**](DefaultApi.md#nodesEnable) | **POST** /Nodes/{nodeName}/$/Activate | 
[**nodesGet**](DefaultApi.md#nodesGet) | **GET** /Nodes/{nodeName} | 
[**nodesList**](DefaultApi.md#nodesList) | **GET** /Nodes | 
[**partitionHealthsGet**](DefaultApi.md#partitionHealthsGet) | **GET** /Partitions/{partitionId}/$/GetHealth | 
[**partitionHealthsSend**](DefaultApi.md#partitionHealthsSend) | **POST** /Partitions/{partitionId}/$/ReportHealth | 
[**partitionListsRepair**](DefaultApi.md#partitionListsRepair) | **POST** /Services/{serviceName}/$/GetPartitions/$/Recover | 
[**partitionLoadInformationsGet**](DefaultApi.md#partitionLoadInformationsGet) | **GET** /Partitions/{partitionId}/$/GetLoadInformation | 
[**partitionLoadsReset**](DefaultApi.md#partitionLoadsReset) | **POST** /Partitions/{partitionId}/$/ResetLoad | 
[**partitionsGet**](DefaultApi.md#partitionsGet) | **GET** /Services/{serviceName}/$/GetPartitions/{partitionId} | 
[**partitionsList**](DefaultApi.md#partitionsList) | **GET** /Services/{serviceName}/$/GetPartitions | 
[**partitionsRepair**](DefaultApi.md#partitionsRepair) | **POST** /Partitions/{partitionId}/$/Recover | 
[**replicaHealthsGet**](DefaultApi.md#replicaHealthsGet) | **GET** /Partitions/{partitionId}/$/GetReplicas/{replicaId}/$/GetHealth | 
[**replicaHealthsSend**](DefaultApi.md#replicaHealthsSend) | **POST** /Partitions/{partitionId}/$/GetReplicas/{replicaId}/$/ReportHealth | 
[**replicaLoadInformationsGet**](DefaultApi.md#replicaLoadInformationsGet) | **GET** /Partitions/{partitionId}/$/GetReplicas/{replicaId}/$/GetLoadInformation | 
[**replicasGet**](DefaultApi.md#replicasGet) | **GET** /Partitions/{partitionId}/$/GetReplicas/{replicaId} | 
[**replicasList**](DefaultApi.md#replicasList) | **GET** /Partitions/{partitionId}/$/GetReplicas | 
[**serviceDescriptionsGet**](DefaultApi.md#serviceDescriptionsGet) | **GET** /Services/{serviceName}/$/GetDescription | 
[**serviceFromTemplatesCreate**](DefaultApi.md#serviceFromTemplatesCreate) | **POST** /Applications/{applicationName}/$/GetServices/$/CreateFromTemplate | 
[**serviceGroupDescriptionsGet**](DefaultApi.md#serviceGroupDescriptionsGet) | **GET** /Applications/{applicationName}/$/GetServices/{serviceName}/$/GetServiceGroupDescription | 
[**serviceGroupFromTemplatesCreate**](DefaultApi.md#serviceGroupFromTemplatesCreate) | **POST** /Applications/{applicationName}/$/GetServiceGroups/$/CreateServiceGroupFromTemplate | 
[**serviceGroupMembersGet**](DefaultApi.md#serviceGroupMembersGet) | **GET** /Applications/{applicationName}/$/GetServices/{serviceName}/$/GetServiceGroupMembers | 
[**serviceGroupsCreate**](DefaultApi.md#serviceGroupsCreate) | **POST** /Applications/{applicationName}/$/GetServices/$/CreateServiceGroup | 
[**serviceGroupsRemove**](DefaultApi.md#serviceGroupsRemove) | **POST** /Applications/{applicationName}/$/GetServiceGroups/{serviceName}/$/Delete | 
[**serviceGroupsUpdate**](DefaultApi.md#serviceGroupsUpdate) | **POST** /Applications/{applicationName}/$/GetServices/{serviceName}/$/UpdateServiceGroup | 
[**serviceHealthsGet**](DefaultApi.md#serviceHealthsGet) | **GET** /Services/{serviceName}/$/GetHealth | 
[**serviceHealthsSend**](DefaultApi.md#serviceHealthsSend) | **POST** /Services/{serviceName}/$/ReportHealth | 
[**serviceManifestsGet**](DefaultApi.md#serviceManifestsGet) | **GET** /ApplicationTypes/{applicationTypeName}/$/GetServiceManifest | 
[**serviceTypesGet**](DefaultApi.md#serviceTypesGet) | **GET** /ApplicationTypes/{applicationTypeName}/$/GetServiceTypes | 
[**servicesCreate**](DefaultApi.md#servicesCreate) | **POST** /Applications/{applicationName}/$/GetServices/$/Create | 
[**servicesGet**](DefaultApi.md#servicesGet) | **GET** /Applications/{applicationName}/$/GetServices/{serviceName} | 
[**servicesList**](DefaultApi.md#servicesList) | **GET** /Applications/{applicationName}/$/GetServices | 
[**servicesRemove**](DefaultApi.md#servicesRemove) | **POST** /Services/{serviceName}/$/Delete | 
[**servicesResolve**](DefaultApi.md#servicesResolve) | **GET** /Services/{serviceName}/$/ResolvePartition | 
[**servicesUpdate**](DefaultApi.md#servicesUpdate) | **POST** /Services/{serviceName}/$/Update | 
[**upgradeProgressesGet**](DefaultApi.md#upgradeProgressesGet) | **GET** /$/GetUpgradeProgress | 



## applicationHealthsGet

> ApplicationHealth applicationHealthsGet(applicationName, apiVersion, opts)



Get application healths

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationName = "applicationName_example"; // String | The name of the application
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'eventsHealthStateFilter': "eventsHealthStateFilter_example", // String | The filter of the events health state
  'deployedApplicationsHealthStateFilter': "deployedApplicationsHealthStateFilter_example", // String | The filter of the deployed application health state
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.applicationHealthsGet(applicationName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationName** | **String**| The name of the application | 
 **apiVersion** | **String**| The version of the api | 
 **eventsHealthStateFilter** | **String**| The filter of the events health state | [optional] 
 **deployedApplicationsHealthStateFilter** | **String**| The filter of the deployed application health state | [optional] 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**ApplicationHealth**](ApplicationHealth.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationHealthsSend

> String applicationHealthsSend(applicationName, apiVersion, applicationHealthReport, opts)



Send application health

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationName = "applicationName_example"; // String | The name of the application
let apiVersion = "apiVersion_example"; // String | The version of the api
let applicationHealthReport = new ServiceFabricClient.ApplicationHealthReport(); // ApplicationHealthReport | The report of the application health
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.applicationHealthsSend(applicationName, apiVersion, applicationHealthReport, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationName** | **String**| The name of the application | 
 **apiVersion** | **String**| The version of the api | 
 **applicationHealthReport** | [**ApplicationHealthReport**](ApplicationHealthReport.md)| The report of the application health | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationManifestsGet

> ApplicationManifest applicationManifestsGet(applicationTypeName, applicationTypeVersion, apiVersion, opts)



Get application manifests

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationTypeName = "applicationTypeName_example"; // String | The name of the application type
let applicationTypeVersion = "applicationTypeVersion_example"; // String | The version of the application type
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.applicationManifestsGet(applicationTypeName, applicationTypeVersion, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationTypeName** | **String**| The name of the application type | 
 **applicationTypeVersion** | **String**| The version of the application type | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**ApplicationManifest**](ApplicationManifest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationTypesGet

> [ApplicationType] applicationTypesGet(applicationTypeName, apiVersion, opts)



Get application types

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationTypeName = "applicationTypeName_example"; // String | The name of the application type
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.applicationTypesGet(applicationTypeName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationTypeName** | **String**| The name of the application type | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**[ApplicationType]**](ApplicationType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationTypesList

> [ApplicationType] applicationTypesList(apiVersion, opts)



List application types

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.applicationTypesList(apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**[ApplicationType]**](ApplicationType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationTypesRegister

> String applicationTypesRegister(apiVersion, registerApplicationType, opts)



Register application types

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The version of the api
let registerApplicationType = new ServiceFabricClient.RegisterApplicationType(); // RegisterApplicationType | The type of the register application
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.applicationTypesRegister(apiVersion, registerApplicationType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| The version of the api | 
 **registerApplicationType** | [**RegisterApplicationType**](RegisterApplicationType.md)| The type of the register application | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationTypesUnregister

> String applicationTypesUnregister(applicationTypeName, apiVersion, unregisterApplicationType, opts)



Unregister application types

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationTypeName = "applicationTypeName_example"; // String | The name of the application type
let apiVersion = "apiVersion_example"; // String | The version of the api
let unregisterApplicationType = new ServiceFabricClient.UnregisterApplicationType(); // UnregisterApplicationType | The type of the unregister application
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.applicationTypesUnregister(applicationTypeName, apiVersion, unregisterApplicationType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationTypeName** | **String**| The name of the application type | 
 **apiVersion** | **String**| The version of the api | 
 **unregisterApplicationType** | [**UnregisterApplicationType**](UnregisterApplicationType.md)| The type of the unregister application | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationUpgradeRollbacksStart

> String applicationUpgradeRollbacksStart(applicationName, apiVersion, opts)



Start application upgrade rollbacks

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationName = "applicationName_example"; // String | The name of the application
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.applicationUpgradeRollbacksStart(applicationName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationName** | **String**| The name of the application | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationUpgradesGet

> ApplicationUpgrade applicationUpgradesGet(applicationName, apiVersion, opts)



Get application upgrades

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationName = "applicationName_example"; // String | The name of the application
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.applicationUpgradesGet(applicationName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationName** | **String**| The name of the application | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**ApplicationUpgrade**](ApplicationUpgrade.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationUpgradesResume

> String applicationUpgradesResume(applicationName, apiVersion, resumeApplicationUpgrade, opts)



Resume application upgrades

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationName = "applicationName_example"; // String | The name of the application
let apiVersion = "apiVersion_example"; // String | The version of the api
let resumeApplicationUpgrade = new ServiceFabricClient.ResumeApplicationUpgrade(); // ResumeApplicationUpgrade | The upgrade of the resume application
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.applicationUpgradesResume(applicationName, apiVersion, resumeApplicationUpgrade, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationName** | **String**| The name of the application | 
 **apiVersion** | **String**| The version of the api | 
 **resumeApplicationUpgrade** | [**ResumeApplicationUpgrade**](ResumeApplicationUpgrade.md)| The upgrade of the resume application | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationUpgradesStart

> String applicationUpgradesStart(applicationName, apiVersion, startApplicationUpgrade, opts)



Start application upgrades

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationName = "applicationName_example"; // String | The name of the application
let apiVersion = "apiVersion_example"; // String | The version of the api
let startApplicationUpgrade = new ServiceFabricClient.StartApplicationUpgrade(); // StartApplicationUpgrade | The description of the start application upgrade
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.applicationUpgradesStart(applicationName, apiVersion, startApplicationUpgrade, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationName** | **String**| The name of the application | 
 **apiVersion** | **String**| The version of the api | 
 **startApplicationUpgrade** | [**StartApplicationUpgrade**](StartApplicationUpgrade.md)| The description of the start application upgrade | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationUpgradesUpdate

> String applicationUpgradesUpdate(applicationName, apiVersion, updateApplicationUpgrade, opts)



Update application upgrades

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationName = "applicationName_example"; // String | The name of the application
let apiVersion = "apiVersion_example"; // String | The version of the api
let updateApplicationUpgrade = new ServiceFabricClient.UpdateApplicationUpgrade(); // UpdateApplicationUpgrade | The description of the update application upgrade
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.applicationUpgradesUpdate(applicationName, apiVersion, updateApplicationUpgrade, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationName** | **String**| The name of the application | 
 **apiVersion** | **String**| The version of the api | 
 **updateApplicationUpgrade** | [**UpdateApplicationUpgrade**](UpdateApplicationUpgrade.md)| The description of the update application upgrade | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationsCreate

> String applicationsCreate(apiVersion, applicationDescription, opts)



Create applications

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The version of the api
let applicationDescription = new ServiceFabricClient.ApplicationDescription(); // ApplicationDescription | The description of the application
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.applicationsCreate(apiVersion, applicationDescription, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| The version of the api | 
 **applicationDescription** | [**ApplicationDescription**](ApplicationDescription.md)| The description of the application | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationsGet

> Application applicationsGet(applicationName, apiVersion, opts)



Get applications

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationName = "applicationName_example"; // String | The name of the application
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.applicationsGet(applicationName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationName** | **String**| The name of the application | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationsList

> ApplicationList applicationsList(apiVersion, opts)



List applications

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56, // Number | The timeout in seconds
  'continuationToken': "continuationToken_example" // String | The token of the continuation
};
apiInstance.applicationsList(apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 
 **continuationToken** | **String**| The token of the continuation | [optional] 

### Return type

[**ApplicationList**](ApplicationList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationsRemove

> String applicationsRemove(applicationName, apiVersion, opts)



Remove applications

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationName = "applicationName_example"; // String | The name of the application
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'forceRemove': true, // Boolean | The force remove flag to skip services check
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.applicationsRemove(applicationName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationName** | **String**| The name of the application | 
 **apiVersion** | **String**| The version of the api | 
 **forceRemove** | **Boolean**| The force remove flag to skip services check | [optional] 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clusterHealthsGet

> ClusterHealth clusterHealthsGet(apiVersion, opts)



Get cluster healths

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'eventsHealthStateFilter': "eventsHealthStateFilter_example", // String | The filter of the events health state
  'nodesHealthStateFilter': "nodesHealthStateFilter_example", // String | The filter of the nodes health state
  'applicationsHealthStateFilter': "applicationsHealthStateFilter_example", // String | The filter of the applications health state
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.clusterHealthsGet(apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| The version of the api | 
 **eventsHealthStateFilter** | **String**| The filter of the events health state | [optional] 
 **nodesHealthStateFilter** | **String**| The filter of the nodes health state | [optional] 
 **applicationsHealthStateFilter** | **String**| The filter of the applications health state | [optional] 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**ClusterHealth**](ClusterHealth.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clusterHealthsSend

> String clusterHealthsSend(apiVersion, clusterHealthReport, opts)



Report cluster healths

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The version of the api
let clusterHealthReport = new ServiceFabricClient.ClusterHealthReport(); // ClusterHealthReport | The report of the cluster health
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.clusterHealthsSend(apiVersion, clusterHealthReport, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| The version of the api | 
 **clusterHealthReport** | [**ClusterHealthReport**](ClusterHealthReport.md)| The report of the cluster health | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clusterLoadInformationsGet

> ClusterLoadInformation clusterLoadInformationsGet(apiVersion, opts)



Get cluster load informations

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.clusterLoadInformationsGet(apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**ClusterLoadInformation**](ClusterLoadInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clusterManifestsGet

> String clusterManifestsGet(apiVersion, opts)



Get cluster manifests

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.clusterManifestsGet(apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clusterPackagesRegister

> String clusterPackagesRegister(apiVersion, registerClusterPackage, opts)



Register cluster packages

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The version of the api
let registerClusterPackage = new ServiceFabricClient.RegisterClusterPackage(); // RegisterClusterPackage | The package of the register cluster
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.clusterPackagesRegister(apiVersion, registerClusterPackage, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| The version of the api | 
 **registerClusterPackage** | [**RegisterClusterPackage**](RegisterClusterPackage.md)| The package of the register cluster | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clusterPackagesUnregister

> String clusterPackagesUnregister(apiVersion, unregisterClusterPackage, opts)



Unregister cluster packages

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The version of the api
let unregisterClusterPackage = new ServiceFabricClient.UnregisterClusterPackage(); // UnregisterClusterPackage | The package of the unregister cluster
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.clusterPackagesUnregister(apiVersion, unregisterClusterPackage, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| The version of the api | 
 **unregisterClusterPackage** | [**UnregisterClusterPackage**](UnregisterClusterPackage.md)| The package of the unregister cluster | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clusterUpgradesResume

> String clusterUpgradesResume(apiVersion, resumeClusterUpgrade, opts)



Resume cluster upgrades

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The version of the api
let resumeClusterUpgrade = new ServiceFabricClient.ResumeClusterUpgrade(); // ResumeClusterUpgrade | The upgrade of the cluster
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.clusterUpgradesResume(apiVersion, resumeClusterUpgrade, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| The version of the api | 
 **resumeClusterUpgrade** | [**ResumeClusterUpgrade**](ResumeClusterUpgrade.md)| The upgrade of the cluster | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clusterUpgradesRollback

> String clusterUpgradesRollback(apiVersion, opts)



Rollback cluster upgrades

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.clusterUpgradesRollback(apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clusterUpgradesStart

> String clusterUpgradesStart(apiVersion, startClusterUpgrade, opts)



Start cluster upgrades

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The version of the api
let startClusterUpgrade = new ServiceFabricClient.StartClusterUpgrade(); // StartClusterUpgrade | The description of the start cluster upgrade
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.clusterUpgradesStart(apiVersion, startClusterUpgrade, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| The version of the api | 
 **startClusterUpgrade** | [**StartClusterUpgrade**](StartClusterUpgrade.md)| The description of the start cluster upgrade | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clusterUpgradesUpdate

> String clusterUpgradesUpdate(apiVersion, updateClusterUpgrade, opts)



Update cluster upgrades

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The version of the api
let updateClusterUpgrade = new ServiceFabricClient.UpdateClusterUpgrade(); // UpdateClusterUpgrade | The description of the update cluster upgrade
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.clusterUpgradesUpdate(apiVersion, updateClusterUpgrade, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| The version of the api | 
 **updateClusterUpgrade** | [**UpdateClusterUpgrade**](UpdateClusterUpgrade.md)| The description of the update cluster upgrade | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deployedApplicationHealthsGet

> DeployedApplicationHealth deployedApplicationHealthsGet(nodeName, applicationName, apiVersion, opts)



Get deployed application healths

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let nodeName = "nodeName_example"; // String | The name of the node
let applicationName = "applicationName_example"; // String | The name of the application
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'eventsHealthStateFilter': "eventsHealthStateFilter_example", // String | The filter of the events health state
  'deployedServicePackagesHealthStateFilter': "deployedServicePackagesHealthStateFilter_example", // String | The filter of the deployed service packages health state
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.deployedApplicationHealthsGet(nodeName, applicationName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeName** | **String**| The name of the node | 
 **applicationName** | **String**| The name of the application | 
 **apiVersion** | **String**| The version of the api | 
 **eventsHealthStateFilter** | **String**| The filter of the events health state | [optional] 
 **deployedServicePackagesHealthStateFilter** | **String**| The filter of the deployed service packages health state | [optional] 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**DeployedApplicationHealth**](DeployedApplicationHealth.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deployedApplicationHealthsSend

> String deployedApplicationHealthsSend(nodeName, applicationName, apiVersion, deployedApplicationHealthReport, opts)



Send deployed application health

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let nodeName = "nodeName_example"; // String | The name of the node
let applicationName = "applicationName_example"; // String | The name of the application
let apiVersion = "apiVersion_example"; // String | The version of the api
let deployedApplicationHealthReport = new ServiceFabricClient.DeployedApplicationHealthReport(); // DeployedApplicationHealthReport | The report of the deployed application health
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.deployedApplicationHealthsSend(nodeName, applicationName, apiVersion, deployedApplicationHealthReport, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeName** | **String**| The name of the node | 
 **applicationName** | **String**| The name of the application | 
 **apiVersion** | **String**| The version of the api | 
 **deployedApplicationHealthReport** | [**DeployedApplicationHealthReport**](DeployedApplicationHealthReport.md)| The report of the deployed application health | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deployedApplicationsGet

> DeployedApplication deployedApplicationsGet(nodeName, applicationName, apiVersion, opts)



Get deployed applications

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let nodeName = "nodeName_example"; // String | The name of the node
let applicationName = "applicationName_example"; // String | The name of the application
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.deployedApplicationsGet(nodeName, applicationName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeName** | **String**| The name of the node | 
 **applicationName** | **String**| The name of the application | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**DeployedApplication**](DeployedApplication.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deployedApplicationsList

> [DeployedApplication] deployedApplicationsList(nodeName, apiVersion, opts)



List deployed applications

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let nodeName = "nodeName_example"; // String | The name of the node
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.deployedApplicationsList(nodeName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeName** | **String**| The name of the node | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**[DeployedApplication]**](DeployedApplication.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deployedCodePackagesGet

> [DeployedCodePackage] deployedCodePackagesGet(nodeName, applicationName, apiVersion, opts)



Get deployed code packages

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let nodeName = "nodeName_example"; // String | The name of the node
let applicationName = "applicationName_example"; // String | The name of the application
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.deployedCodePackagesGet(nodeName, applicationName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeName** | **String**| The name of the node | 
 **applicationName** | **String**| The name of the application | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**[DeployedCodePackage]**](DeployedCodePackage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deployedReplicaDetailsGet

> DeployedReplicaDetail deployedReplicaDetailsGet(nodeName, partitionName, replicaId, apiVersion, opts)



Get deployed replica details

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let nodeName = "nodeName_example"; // String | The name of the node
let partitionName = "partitionName_example"; // String | The name of the partition
let replicaId = "replicaId_example"; // String | The id of the replica
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.deployedReplicaDetailsGet(nodeName, partitionName, replicaId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeName** | **String**| The name of the node | 
 **partitionName** | **String**| The name of the partition | 
 **replicaId** | **String**| The id of the replica | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**DeployedReplicaDetail**](DeployedReplicaDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deployedReplicasGet

> [DeployedReplica] deployedReplicasGet(nodeName, applicationName, apiVersion, opts)



Get deployed replicas

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let nodeName = "nodeName_example"; // String | The name of the node
let applicationName = "applicationName_example"; // String | The name of the application
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.deployedReplicasGet(nodeName, applicationName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeName** | **String**| The name of the node | 
 **applicationName** | **String**| The name of the application | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**[DeployedReplica]**](DeployedReplica.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deployedServicePackageHealthsGet

> DeployedServicePackageHealth deployedServicePackageHealthsGet(nodeName, applicationName, servicePackageName, apiVersion, opts)



Get deployed service package healths

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let nodeName = "nodeName_example"; // String | The name of the node
let applicationName = "applicationName_example"; // String | The name of the application
let servicePackageName = "servicePackageName_example"; // String | The name of the service package
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'eventsHealthStateFilter': "eventsHealthStateFilter_example", // String | The filter of the events health state
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.deployedServicePackageHealthsGet(nodeName, applicationName, servicePackageName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeName** | **String**| The name of the node | 
 **applicationName** | **String**| The name of the application | 
 **servicePackageName** | **String**| The name of the service package | 
 **apiVersion** | **String**| The version of the api | 
 **eventsHealthStateFilter** | **String**| The filter of the events health state | [optional] 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**DeployedServicePackageHealth**](DeployedServicePackageHealth.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deployedServicePackageHealthsSend

> String deployedServicePackageHealthsSend(nodeName, applicationName, serviceManifestName, apiVersion, deployedServicePackageHealthReport, opts)



Send deployed service package health

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let nodeName = "nodeName_example"; // String | The name of the node
let applicationName = "applicationName_example"; // String | The name of the application
let serviceManifestName = "serviceManifestName_example"; // String | The name of the service manifest
let apiVersion = "apiVersion_example"; // String | The version of the api
let deployedServicePackageHealthReport = new ServiceFabricClient.DeployedServiceHealthReport(); // DeployedServiceHealthReport | The report of the deployed service package health
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.deployedServicePackageHealthsSend(nodeName, applicationName, serviceManifestName, apiVersion, deployedServicePackageHealthReport, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeName** | **String**| The name of the node | 
 **applicationName** | **String**| The name of the application | 
 **serviceManifestName** | **String**| The name of the service manifest | 
 **apiVersion** | **String**| The version of the api | 
 **deployedServicePackageHealthReport** | [**DeployedServiceHealthReport**](DeployedServiceHealthReport.md)| The report of the deployed service package health | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deployedServicePackagesGet

> [DeployedServicePackage] deployedServicePackagesGet(nodeName, applicationName, apiVersion, opts)



Get deployed service packages

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let nodeName = "nodeName_example"; // String | The name of the node
let applicationName = "applicationName_example"; // String | The name of the application
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.deployedServicePackagesGet(nodeName, applicationName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeName** | **String**| The name of the node | 
 **applicationName** | **String**| The name of the application | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**[DeployedServicePackage]**](DeployedServicePackage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deployedServiceTypesGet

> [DeployedServiceType] deployedServiceTypesGet(nodeName, applicationName, apiVersion, opts)



Get deployed service types

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let nodeName = "nodeName_example"; // String | The name of the node
let applicationName = "applicationName_example"; // String | The name of the application
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.deployedServiceTypesGet(nodeName, applicationName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeName** | **String**| The name of the node | 
 **applicationName** | **String**| The name of the application | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**[DeployedServiceType]**](DeployedServiceType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nodeHealthsGet

> NodeHealth nodeHealthsGet(nodeName, apiVersion, opts)



Get node healths

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let nodeName = "nodeName_example"; // String | The name of the node
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'eventsHealthStateFilter': "eventsHealthStateFilter_example", // String | The filter of the events health state
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.nodeHealthsGet(nodeName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeName** | **String**| The name of the node | 
 **apiVersion** | **String**| The version of the api | 
 **eventsHealthStateFilter** | **String**| The filter of the events health state | [optional] 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**NodeHealth**](NodeHealth.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nodeHealthsSend

> String nodeHealthsSend(nodeName, apiVersion, nodeHealthReport, opts)



Send node health

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let nodeName = "nodeName_example"; // String | The name of the node
let apiVersion = "apiVersion_example"; // String | The version of the api
let nodeHealthReport = new ServiceFabricClient.NodeHealthReport(); // NodeHealthReport | The report of the node health
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.nodeHealthsSend(nodeName, apiVersion, nodeHealthReport, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeName** | **String**| The name of the node | 
 **apiVersion** | **String**| The version of the api | 
 **nodeHealthReport** | [**NodeHealthReport**](NodeHealthReport.md)| The report of the node health | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nodeLoadInformationsGet

> NodeLoadInformation nodeLoadInformationsGet(nodeName, apiVersion, opts)



Get node load informations

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let nodeName = "nodeName_example"; // String | The name of the node
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.nodeLoadInformationsGet(nodeName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeName** | **String**| The name of the node | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**NodeLoadInformation**](NodeLoadInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nodeStatesRemove

> String nodeStatesRemove(nodeName, apiVersion, opts)



Remove node states

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let nodeName = "nodeName_example"; // String | The name of the node
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.nodeStatesRemove(nodeName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeName** | **String**| The name of the node | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nodesDisable

> String nodesDisable(nodeName, apiVersion, disableNode, opts)



Disable nodes

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let nodeName = "nodeName_example"; // String | The name of the node
let apiVersion = "apiVersion_example"; // String | The version of the api
let disableNode = new ServiceFabricClient.DisableNode(); // DisableNode | The node
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.nodesDisable(nodeName, apiVersion, disableNode, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeName** | **String**| The name of the node | 
 **apiVersion** | **String**| The version of the api | 
 **disableNode** | [**DisableNode**](DisableNode.md)| The node | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nodesEnable

> String nodesEnable(nodeName, apiVersion, opts)



Enable nodes

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let nodeName = "nodeName_example"; // String | The name of the node
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.nodesEnable(nodeName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeName** | **String**| The name of the node | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nodesGet

> Node nodesGet(nodeName, apiVersion, opts)



Get nodes

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let nodeName = "nodeName_example"; // String | The name of the node
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.nodesGet(nodeName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodeName** | **String**| The name of the node | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**Node**](Node.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nodesList

> NodeList nodesList(apiVersion, opts)



List nodes

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56, // Number | The timeout in seconds
  'continuationToken': "continuationToken_example" // String | The token of the continuation
};
apiInstance.nodesList(apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 
 **continuationToken** | **String**| The token of the continuation | [optional] 

### Return type

[**NodeList**](NodeList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## partitionHealthsGet

> PartitionHealth partitionHealthsGet(partitionId, apiVersion, opts)



Get partition healths

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let partitionId = "partitionId_example"; // String | The id of the partition
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'eventsHealthStateFilter': "eventsHealthStateFilter_example", // String | The filter of the events health state
  'replicasHealthStateFilter': "replicasHealthStateFilter_example", // String | The filter of the replicas health state
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.partitionHealthsGet(partitionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partitionId** | **String**| The id of the partition | 
 **apiVersion** | **String**| The version of the api | 
 **eventsHealthStateFilter** | **String**| The filter of the events health state | [optional] 
 **replicasHealthStateFilter** | **String**| The filter of the replicas health state | [optional] 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**PartitionHealth**](PartitionHealth.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## partitionHealthsSend

> String partitionHealthsSend(partitionId, apiVersion, partitionHealthReport, opts)



Send partition health

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let partitionId = "partitionId_example"; // String | The id of the partition
let apiVersion = "apiVersion_example"; // String | The version of the api
let partitionHealthReport = new ServiceFabricClient.PartitionHealthReport(); // PartitionHealthReport | The report of the partition health
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.partitionHealthsSend(partitionId, apiVersion, partitionHealthReport, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partitionId** | **String**| The id of the partition | 
 **apiVersion** | **String**| The version of the api | 
 **partitionHealthReport** | [**PartitionHealthReport**](PartitionHealthReport.md)| The report of the partition health | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## partitionListsRepair

> String partitionListsRepair(serviceName, apiVersion, opts)



Repair partition lists

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let serviceName = "serviceName_example"; // String | The name of the service
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.partitionListsRepair(serviceName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceName** | **String**| The name of the service | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## partitionLoadInformationsGet

> PartitionLoadInformation partitionLoadInformationsGet(partitionId, apiVersion, opts)



Get partition load informations

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let partitionId = "partitionId_example"; // String | The id of the partition
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.partitionLoadInformationsGet(partitionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partitionId** | **String**| The id of the partition | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**PartitionLoadInformation**](PartitionLoadInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## partitionLoadsReset

> String partitionLoadsReset(partitionId, apiVersion, opts)



Reset partition loads

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let partitionId = "partitionId_example"; // String | The id of the partition
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.partitionLoadsReset(partitionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partitionId** | **String**| The id of the partition | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## partitionsGet

> Partition partitionsGet(serviceName, partitionId, apiVersion, opts)



Get partitions

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let serviceName = "serviceName_example"; // String | The name of the service
let partitionId = "partitionId_example"; // String | The id of the partition
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.partitionsGet(serviceName, partitionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceName** | **String**| The name of the service | 
 **partitionId** | **String**| The id of the partition | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**Partition**](Partition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## partitionsList

> PartitionList partitionsList(serviceName, apiVersion, opts)



List partitions

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let serviceName = "serviceName_example"; // String | The name of the service
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.partitionsList(serviceName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceName** | **String**| The name of the service | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**PartitionList**](PartitionList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## partitionsRepair

> String partitionsRepair(partitionId, apiVersion, opts)



Repair partitions

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let partitionId = "partitionId_example"; // String | The id of the partition
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.partitionsRepair(partitionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partitionId** | **String**| The id of the partition | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicaHealthsGet

> ReplicaHealth replicaHealthsGet(partitionId, replicaId, apiVersion, opts)



Get replica healths

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let partitionId = "partitionId_example"; // String | The id of the partition
let replicaId = "replicaId_example"; // String | The id of the replica
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'eventsHealthStateFilter': "eventsHealthStateFilter_example", // String | The filter of the events health state
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.replicaHealthsGet(partitionId, replicaId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partitionId** | **String**| The id of the partition | 
 **replicaId** | **String**| The id of the replica | 
 **apiVersion** | **String**| The version of the api | 
 **eventsHealthStateFilter** | **String**| The filter of the events health state | [optional] 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**ReplicaHealth**](ReplicaHealth.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicaHealthsSend

> String replicaHealthsSend(partitionId, replicaId, apiVersion, replicaHealthReport, opts)



Send replica healths

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let partitionId = "partitionId_example"; // String | The id of the partition
let replicaId = "replicaId_example"; // String | The id of the replica
let apiVersion = "apiVersion_example"; // String | The version of the api
let replicaHealthReport = new ServiceFabricClient.ReplicaHealthReport(); // ReplicaHealthReport | The report of the replica health
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.replicaHealthsSend(partitionId, replicaId, apiVersion, replicaHealthReport, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partitionId** | **String**| The id of the partition | 
 **replicaId** | **String**| The id of the replica | 
 **apiVersion** | **String**| The version of the api | 
 **replicaHealthReport** | [**ReplicaHealthReport**](ReplicaHealthReport.md)| The report of the replica health | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicaLoadInformationsGet

> ReplicaLoadInformation replicaLoadInformationsGet(partitionId, replicaId, apiVersion, opts)



Get replica load informations

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let partitionId = "partitionId_example"; // String | The id of the partition
let replicaId = "replicaId_example"; // String | The id of the replica
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.replicaLoadInformationsGet(partitionId, replicaId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partitionId** | **String**| The id of the partition | 
 **replicaId** | **String**| The id of the replica | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**ReplicaLoadInformation**](ReplicaLoadInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicasGet

> Replica replicasGet(partitionId, replicaId, apiVersion, opts)



Get replicas

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let partitionId = "partitionId_example"; // String | The id of the partition
let replicaId = "replicaId_example"; // String | The id of the replica
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.replicasGet(partitionId, replicaId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partitionId** | **String**| The id of the partition | 
 **replicaId** | **String**| The id of the replica | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**Replica**](Replica.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicasList

> ReplicaList replicasList(partitionId, apiVersion, opts)



List replicas

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let partitionId = "partitionId_example"; // String | The id of the partition
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.replicasList(partitionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partitionId** | **String**| The id of the partition | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**ReplicaList**](ReplicaList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceDescriptionsGet

> ServiceDescription serviceDescriptionsGet(serviceName, apiVersion, opts)



Get service descriptions

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let serviceName = "serviceName_example"; // String | The name of the service
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.serviceDescriptionsGet(serviceName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceName** | **String**| The name of the service | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**ServiceDescription**](ServiceDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceFromTemplatesCreate

> String serviceFromTemplatesCreate(applicationName, apiVersion, serviceDescriptionTemplate, opts)



Create service from templates

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationName = "applicationName_example"; // String | The name of the application
let apiVersion = "apiVersion_example"; // String | The version of the api
let serviceDescriptionTemplate = new ServiceFabricClient.ServiceDescriptionTemplate(); // ServiceDescriptionTemplate | The template of the service description
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.serviceFromTemplatesCreate(applicationName, apiVersion, serviceDescriptionTemplate, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationName** | **String**| The name of the application | 
 **apiVersion** | **String**| The version of the api | 
 **serviceDescriptionTemplate** | [**ServiceDescriptionTemplate**](ServiceDescriptionTemplate.md)| The template of the service description | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceGroupDescriptionsGet

> ServiceGroupDescription serviceGroupDescriptionsGet(applicationName, serviceName, apiVersion, opts)



Get service group descriptions

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationName = "applicationName_example"; // String | The name of the application
let serviceName = "serviceName_example"; // String | The name of the service
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.serviceGroupDescriptionsGet(applicationName, serviceName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationName** | **String**| The name of the application | 
 **serviceName** | **String**| The name of the service | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**ServiceGroupDescription**](ServiceGroupDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceGroupFromTemplatesCreate

> String serviceGroupFromTemplatesCreate(applicationName, apiVersion, serviceDescriptionTemplate, opts)



Create service group from templates

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationName = "applicationName_example"; // String | The name of the application
let apiVersion = "apiVersion_example"; // String | The version of the api
let serviceDescriptionTemplate = new ServiceFabricClient.ServiceDescriptionTemplate(); // ServiceDescriptionTemplate | The template of the service description
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.serviceGroupFromTemplatesCreate(applicationName, apiVersion, serviceDescriptionTemplate, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationName** | **String**| The name of the application | 
 **apiVersion** | **String**| The version of the api | 
 **serviceDescriptionTemplate** | [**ServiceDescriptionTemplate**](ServiceDescriptionTemplate.md)| The template of the service description | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceGroupMembersGet

> ServiceGroupMember serviceGroupMembersGet(applicationName, serviceName, apiVersion, opts)



Get service group members

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationName = "applicationName_example"; // String | The name of the application
let serviceName = "serviceName_example"; // String | The name of the service
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.serviceGroupMembersGet(applicationName, serviceName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationName** | **String**| The name of the application | 
 **serviceName** | **String**| The name of the service | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**ServiceGroupMember**](ServiceGroupMember.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceGroupsCreate

> String serviceGroupsCreate(applicationName, apiVersion, createServiceGroupDescription, opts)



Create service groups

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationName = "applicationName_example"; // String | The name of the service group
let apiVersion = "apiVersion_example"; // String | The version of the api
let createServiceGroupDescription = new ServiceFabricClient.CreateServiceGroupDescription(); // CreateServiceGroupDescription | The description of the service group
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.serviceGroupsCreate(applicationName, apiVersion, createServiceGroupDescription, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationName** | **String**| The name of the service group | 
 **apiVersion** | **String**| The version of the api | 
 **createServiceGroupDescription** | [**CreateServiceGroupDescription**](CreateServiceGroupDescription.md)| The description of the service group | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceGroupsRemove

> String serviceGroupsRemove(applicationName, serviceName, apiVersion, opts)



Remove service groups

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationName = "applicationName_example"; // String | The name of the application
let serviceName = "serviceName_example"; // String | The name of the service
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.serviceGroupsRemove(applicationName, serviceName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationName** | **String**| The name of the application | 
 **serviceName** | **String**| The name of the service | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceGroupsUpdate

> String serviceGroupsUpdate(applicationName, serviceName, apiVersion, updateServiceGroupDescription, opts)



Update service groups

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationName = "applicationName_example"; // String | The name of the application
let serviceName = "serviceName_example"; // String | The name of the service
let apiVersion = "apiVersion_example"; // String | The version of the api
let updateServiceGroupDescription = new ServiceFabricClient.UpdateServiceGroupDescription(); // UpdateServiceGroupDescription | The description of the service group update
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.serviceGroupsUpdate(applicationName, serviceName, apiVersion, updateServiceGroupDescription, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationName** | **String**| The name of the application | 
 **serviceName** | **String**| The name of the service | 
 **apiVersion** | **String**| The version of the api | 
 **updateServiceGroupDescription** | [**UpdateServiceGroupDescription**](UpdateServiceGroupDescription.md)| The description of the service group update | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceHealthsGet

> ServiceHealth serviceHealthsGet(serviceName, apiVersion, opts)



Get service healths

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let serviceName = "serviceName_example"; // String | The name of the service
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.serviceHealthsGet(serviceName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceName** | **String**| The name of the service | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**ServiceHealth**](ServiceHealth.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceHealthsSend

> String serviceHealthsSend(serviceName, apiVersion, serviceHealthReport, opts)



Send service healths

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let serviceName = "serviceName_example"; // String | The name of the service
let apiVersion = "apiVersion_example"; // String | The version of the api
let serviceHealthReport = new ServiceFabricClient.ServiceHealthReport(); // ServiceHealthReport | The report of the service health
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.serviceHealthsSend(serviceName, apiVersion, serviceHealthReport, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceName** | **String**| The name of the service | 
 **apiVersion** | **String**| The version of the api | 
 **serviceHealthReport** | [**ServiceHealthReport**](ServiceHealthReport.md)| The report of the service health | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceManifestsGet

> ServiceManifest serviceManifestsGet(applicationTypeName, applicationTypeVersion, serviceManifestName, apiVersion, opts)



Get service manifests

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationTypeName = "applicationTypeName_example"; // String | The name of the application type
let applicationTypeVersion = "applicationTypeVersion_example"; // String | The version of the application type
let serviceManifestName = "serviceManifestName_example"; // String | The name of the service manifest
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.serviceManifestsGet(applicationTypeName, applicationTypeVersion, serviceManifestName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationTypeName** | **String**| The name of the application type | 
 **applicationTypeVersion** | **String**| The version of the application type | 
 **serviceManifestName** | **String**| The name of the service manifest | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**ServiceManifest**](ServiceManifest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceTypesGet

> [ServiceType] serviceTypesGet(applicationTypeName, applicationTypeVersion, apiVersion, opts)



Get service types

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationTypeName = "applicationTypeName_example"; // String | The name of the application type
let applicationTypeVersion = "applicationTypeVersion_example"; // String | The version of the application type
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.serviceTypesGet(applicationTypeName, applicationTypeVersion, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationTypeName** | **String**| The name of the application type | 
 **applicationTypeVersion** | **String**| The version of the application type | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**[ServiceType]**](ServiceType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesCreate

> String servicesCreate(applicationName, apiVersion, createServiceDescription, opts)



Create services

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationName = "applicationName_example"; // String | The name of the application
let apiVersion = "apiVersion_example"; // String | The version of the api
let createServiceDescription = new ServiceFabricClient.CreateServiceDescription(); // CreateServiceDescription | The description of the service
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.servicesCreate(applicationName, apiVersion, createServiceDescription, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationName** | **String**| The name of the application | 
 **apiVersion** | **String**| The version of the api | 
 **createServiceDescription** | [**CreateServiceDescription**](CreateServiceDescription.md)| The description of the service | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesGet

> Service servicesGet(applicationName, serviceName, apiVersion, opts)



Get services

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationName = "applicationName_example"; // String | The name of the application
let serviceName = "serviceName_example"; // String | The name of the service
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.servicesGet(applicationName, serviceName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationName** | **String**| The name of the application | 
 **serviceName** | **String**| The name of the service | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**Service**](Service.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesList

> ServiceList servicesList(applicationName, apiVersion, opts)



List services

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let applicationName = "applicationName_example"; // String | The name of the application
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.servicesList(applicationName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationName** | **String**| The name of the application | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**ServiceList**](ServiceList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesRemove

> String servicesRemove(serviceName, apiVersion, opts)



Remove services

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let serviceName = "serviceName_example"; // String | The name of the service
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.servicesRemove(serviceName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceName** | **String**| The name of the service | 
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesResolve

> ResolvedServicePartition servicesResolve(serviceName, apiVersion, opts)



Resolve services

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let serviceName = "serviceName_example"; // String | The name of the service
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'partitionKeyType': 56, // Number | The type of the partition key
  'partitionKeyValue': "partitionKeyValue_example", // String | The value of the partition key
  'previousRspVersion': "previousRspVersion_example", // String | The version of the previous rsp
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.servicesResolve(serviceName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceName** | **String**| The name of the service | 
 **apiVersion** | **String**| The version of the api | 
 **partitionKeyType** | **Number**| The type of the partition key | [optional] 
 **partitionKeyValue** | **String**| The value of the partition key | [optional] 
 **previousRspVersion** | **String**| The version of the previous rsp | [optional] 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**ResolvedServicePartition**](ResolvedServicePartition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesUpdate

> String servicesUpdate(serviceName, apiVersion, updateServiceDescription, opts)



Update services

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let serviceName = "serviceName_example"; // String | The name of the service
let apiVersion = "apiVersion_example"; // String | The version of the api
let updateServiceDescription = new ServiceFabricClient.UpdateServiceDescription(); // UpdateServiceDescription | The description of the service update
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.servicesUpdate(serviceName, apiVersion, updateServiceDescription, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serviceName** | **String**| The name of the service | 
 **apiVersion** | **String**| The version of the api | 
 **updateServiceDescription** | [**UpdateServiceDescription**](UpdateServiceDescription.md)| The description of the service update | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## upgradeProgressesGet

> ClusterUpgradeProgress upgradeProgressesGet(apiVersion, opts)



Get upgrade progresses

### Example

```javascript
import ServiceFabricClient from 'service_fabric_client';

let apiInstance = new ServiceFabricClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The version of the api
let opts = {
  'timeout': 56 // Number | The timeout in seconds
};
apiInstance.upgradeProgressesGet(apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| The version of the api | 
 **timeout** | **Number**| The timeout in seconds | [optional] 

### Return type

[**ClusterUpgradeProgress**](ClusterUpgradeProgress.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

