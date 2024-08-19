# AzureMigrateV2.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assessedMachinesGet**](DefaultApi.md#assessedMachinesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName}/assessments/{assessmentName}/assessedMachines/{assessedMachineName} | Get an assessed machine.
[**assessedMachinesListByAssessment**](DefaultApi.md#assessedMachinesListByAssessment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName}/assessments/{assessmentName}/assessedMachines | Get assessed machines for assessment.
[**assessmentsCreate**](DefaultApi.md#assessmentsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName}/assessments/{assessmentName} | Create or Update assessment.
[**assessmentsDelete**](DefaultApi.md#assessmentsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName}/assessments/{assessmentName} | Deletes an assessment from the project.
[**assessmentsGet**](DefaultApi.md#assessmentsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName}/assessments/{assessmentName} | Get an assessment.
[**assessmentsGetReportDownloadUrl**](DefaultApi.md#assessmentsGetReportDownloadUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName}/assessments/{assessmentName}/downloadUrl | Get download URL for the assessment report.
[**assessmentsListByGroup**](DefaultApi.md#assessmentsListByGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName}/assessments | Get all assessments created for the specified group.
[**assessmentsListByProject**](DefaultApi.md#assessmentsListByProject) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/assessments | Get all assessments created in the project.
[**groupsCreate**](DefaultApi.md#groupsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName} | Create a new group with specified settings.
[**groupsDelete**](DefaultApi.md#groupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName} | Delete the group
[**groupsGet**](DefaultApi.md#groupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName} | Get a specific group.
[**groupsListByProject**](DefaultApi.md#groupsListByProject) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups | Get all groups
[**groupsUpdateMachines**](DefaultApi.md#groupsUpdateMachines) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName}/updateMachines | Update machines in group.
[**hyperVCollectorsCreate**](DefaultApi.md#hyperVCollectorsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/hypervcollectors/{hyperVCollectorName} | Create or Update Hyper-V collector.
[**hyperVCollectorsDelete**](DefaultApi.md#hyperVCollectorsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/hypervcollectors/{hyperVCollectorName} | Deletes Hyper-V collector from the project.
[**hyperVCollectorsGet**](DefaultApi.md#hyperVCollectorsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/hypervcollectors/{hyperVCollectorName} | Get a Hyper-V collector.
[**hyperVCollectorsListByProject**](DefaultApi.md#hyperVCollectorsListByProject) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/hypervcollectors | Get a list of Hyper-V collector.
[**machinesGet**](DefaultApi.md#machinesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/machines/{machineName} | Get a specific machine.
[**machinesListByProject**](DefaultApi.md#machinesListByProject) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/machines | Get all machines in the project
[**operationsList**](DefaultApi.md#operationsList) | **GET** /providers/Microsoft.Migrate/operations | Get list of operations supported in the API.
[**projectAssessmentOptions**](DefaultApi.md#projectAssessmentOptions) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/assessmentOptions/{assessmentOptionsName} | Get all available options for the properties of an assessment on a project.
[**projectAssessmentOptionsList**](DefaultApi.md#projectAssessmentOptionsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/assessmentOptions | Gets list of all available options for the properties of an assessment on a project.
[**projectsCreate**](DefaultApi.md#projectsCreate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName} | Create or update project.
[**projectsDelete**](DefaultApi.md#projectsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName} | Delete the project
[**projectsGet**](DefaultApi.md#projectsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName} | Get the specified project.
[**projectsList**](DefaultApi.md#projectsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects | Get all projects.
[**projectsListBySubscription**](DefaultApi.md#projectsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Migrate/assessmentProjects | Get all projects.
[**projectsUpdate**](DefaultApi.md#projectsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName} | Update project.
[**vMwareCollectorsCreate**](DefaultApi.md#vMwareCollectorsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/vmwarecollectors/{vmWareCollectorName} | Create or Update VMware collector.
[**vMwareCollectorsDelete**](DefaultApi.md#vMwareCollectorsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/vmwarecollectors/{vmWareCollectorName} | Deletes VMware collector from the project.
[**vMwareCollectorsGet**](DefaultApi.md#vMwareCollectorsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/vmwarecollectors/{vmWareCollectorName} | Get a VMware collector.
[**vMwareCollectorsListByProject**](DefaultApi.md#vMwareCollectorsListByProject) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/vmwarecollectors | Get a list of VMware collector.



## assessedMachinesGet

> AssessedMachine assessedMachinesGet(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, assessedMachineName, apiVersion, opts)

Get an assessed machine.

Get an assessed machine with its size &amp; cost estimate that was evaluated in the specified assessment.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let groupName = "groupName_example"; // String | Unique name of a group within a project.
let assessmentName = "assessmentName_example"; // String | Unique name of an assessment within a project.
let assessedMachineName = "assessedMachineName_example"; // String | Unique name of an assessed machine evaluated as part of an assessment.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.assessedMachinesGet(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, assessedMachineName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **groupName** | **String**| Unique name of a group within a project. | 
 **assessmentName** | **String**| Unique name of an assessment within a project. | 
 **assessedMachineName** | **String**| Unique name of an assessed machine evaluated as part of an assessment. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**AssessedMachine**](AssessedMachine.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assessedMachinesListByAssessment

> AssessedMachineResultList assessedMachinesListByAssessment(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, apiVersion, opts)

Get assessed machines for assessment.

Get list of machines that assessed as part of the specified assessment. Returns a json array of objects of type &#39;assessedMachine&#39; as specified in the Models section.  Whenever an assessment is created or updated, it goes under computation. During this phase, the &#39;status&#39; field of Assessment object reports &#39;Computing&#39;. During the period when the assessment is under computation, the list of assessed machines is empty and no assessed machines are returned by this call. 

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let groupName = "groupName_example"; // String | Unique name of a group within a project.
let assessmentName = "assessmentName_example"; // String | Unique name of an assessment within a project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.assessedMachinesListByAssessment(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **groupName** | **String**| Unique name of a group within a project. | 
 **assessmentName** | **String**| Unique name of an assessment within a project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**AssessedMachineResultList**](AssessedMachineResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assessmentsCreate

> Assessment assessmentsCreate(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, apiVersion, opts)

Create or Update assessment.

Create a new assessment with the given name and the specified settings. Since name of an assessment in a project is a unique identifier, if an assessment with the name provided already exists, then the existing assessment is updated.  Any PUT operation, resulting in either create or update on an assessment, will cause the assessment to go in a \&quot;InProgress\&quot; state. This will be indicated by the field &#39;computationState&#39; on the Assessment object. During this time no other PUT operation will be allowed on that assessment object, nor will a Delete operation. Once the computation for the assessment is complete, the field &#39;computationState&#39; will be updated to &#39;Ready&#39;, and then other PUT or DELETE operations can happen on the assessment.  When assessment is under computation, any PUT will lead to a 400 - Bad Request error. 

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let groupName = "groupName_example"; // String | Unique name of a group within a project.
let assessmentName = "assessmentName_example"; // String | Unique name of an assessment within a project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Standard request header. Used by service to respond to client in appropriate language.
  'assessment': new AzureMigrateV2.Assessment() // Assessment | New or Updated Assessment object.
};
apiInstance.assessmentsCreate(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **groupName** | **String**| Unique name of a group within a project. | 
 **assessmentName** | **String**| Unique name of an assessment within a project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 
 **assessment** | [**Assessment**](Assessment.md)| New or Updated Assessment object. | [optional] 

### Return type

[**Assessment**](Assessment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## assessmentsDelete

> assessmentsDelete(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, apiVersion, opts)

Deletes an assessment from the project.

Delete an assessment from the project. The machines remain in the assessment. Deleting a non-existent assessment results in a no-operation.  When an assessment is under computation, as indicated by the &#39;computationState&#39; field, it cannot be deleted. Any such attempt will return a 400 - Bad Request. 

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let groupName = "groupName_example"; // String | Unique name of a group within a project.
let assessmentName = "assessmentName_example"; // String | Unique name of an assessment within a project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.assessmentsDelete(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **groupName** | **String**| Unique name of a group within a project. | 
 **assessmentName** | **String**| Unique name of an assessment within a project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assessmentsGet

> Assessment assessmentsGet(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, apiVersion, opts)

Get an assessment.

Get an existing assessment with the specified name. Returns a json object of type &#39;assessment&#39; as specified in Models section.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let groupName = "groupName_example"; // String | Unique name of a group within a project.
let assessmentName = "assessmentName_example"; // String | Unique name of an assessment within a project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.assessmentsGet(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **groupName** | **String**| Unique name of a group within a project. | 
 **assessmentName** | **String**| Unique name of an assessment within a project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**Assessment**](Assessment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assessmentsGetReportDownloadUrl

> DownloadUrl assessmentsGetReportDownloadUrl(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, apiVersion, opts)

Get download URL for the assessment report.

Get the URL for downloading the assessment in a report format.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let groupName = "groupName_example"; // String | Unique name of a group within a project.
let assessmentName = "assessmentName_example"; // String | Unique name of an assessment within a project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.assessmentsGetReportDownloadUrl(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **groupName** | **String**| Unique name of a group within a project. | 
 **assessmentName** | **String**| Unique name of an assessment within a project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**DownloadUrl**](DownloadUrl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assessmentsListByGroup

> AssessmentResultList assessmentsListByGroup(subscriptionId, resourceGroupName, projectName, groupName, apiVersion, opts)

Get all assessments created for the specified group.

Get all assessments created for the specified group.  Returns a json array of objects of type &#39;assessment&#39; as specified in Models section. 

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let groupName = "groupName_example"; // String | Unique name of a group within a project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.assessmentsListByGroup(subscriptionId, resourceGroupName, projectName, groupName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **groupName** | **String**| Unique name of a group within a project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**AssessmentResultList**](AssessmentResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assessmentsListByProject

> AssessmentResultList assessmentsListByProject(subscriptionId, resourceGroupName, projectName, apiVersion, opts)

Get all assessments created in the project.

Get all assessments created in the project.  Returns a json array of objects of type &#39;assessment&#39; as specified in Models section. 

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.assessmentsListByProject(subscriptionId, resourceGroupName, projectName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**AssessmentResultList**](AssessmentResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupsCreate

> Group groupsCreate(subscriptionId, resourceGroupName, projectName, groupName, apiVersion, opts)

Create a new group with specified settings.

Create a new group by sending a json object of type &#39;group&#39; as given in Models section as part of the Request Body. The group name in a project is unique.  This operation is Idempotent. 

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let groupName = "groupName_example"; // String | Unique name of a group within a project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Standard request header. Used by service to respond to client in appropriate language.
  'group': new AzureMigrateV2.Group() // Group | New or Updated Group object.
};
apiInstance.groupsCreate(subscriptionId, resourceGroupName, projectName, groupName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **groupName** | **String**| Unique name of a group within a project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 
 **group** | [**Group**](Group.md)| New or Updated Group object. | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## groupsDelete

> groupsDelete(subscriptionId, resourceGroupName, projectName, groupName, apiVersion, opts)

Delete the group

Delete the group from the project. The machines remain in the project. Deleting a non-existent group results in a no-operation.  A group is an aggregation mechanism for machines in a project. Therefore, deleting group does not delete machines in it. 

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let groupName = "groupName_example"; // String | Unique name of a group within a project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.groupsDelete(subscriptionId, resourceGroupName, projectName, groupName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **groupName** | **String**| Unique name of a group within a project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupsGet

> Group groupsGet(subscriptionId, resourceGroupName, projectName, groupName, apiVersion, opts)

Get a specific group.

Get information related to a specific group in the project. Returns a json object of type &#39;group&#39; as specified in the models section.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let groupName = "groupName_example"; // String | Unique name of a group within a project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.groupsGet(subscriptionId, resourceGroupName, projectName, groupName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **groupName** | **String**| Unique name of a group within a project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupsListByProject

> GroupResultList groupsListByProject(subscriptionId, resourceGroupName, projectName, apiVersion, opts)

Get all groups

Get all groups created in the project. Returns a json array of objects of type &#39;group&#39; as specified in the Models section.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.groupsListByProject(subscriptionId, resourceGroupName, projectName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**GroupResultList**](GroupResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupsUpdateMachines

> Group groupsUpdateMachines(subscriptionId, resourceGroupName, projectName, groupName, apiVersion, opts)

Update machines in group.

Update machines in group by adding or removing machines.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let groupName = "groupName_example"; // String | Unique name of a group within a project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Standard request header. Used by service to respond to client in appropriate language.
  'groupUpdateProperties': new AzureMigrateV2.UpdateGroupBody() // UpdateGroupBody | Machines list to be added or removed from group.
};
apiInstance.groupsUpdateMachines(subscriptionId, resourceGroupName, projectName, groupName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **groupName** | **String**| Unique name of a group within a project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 
 **groupUpdateProperties** | [**UpdateGroupBody**](UpdateGroupBody.md)| Machines list to be added or removed from group. | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## hyperVCollectorsCreate

> HyperVCollector hyperVCollectorsCreate(subscriptionId, resourceGroupName, projectName, hyperVCollectorName, apiVersion, opts)

Create or Update Hyper-V collector.

Create or Update Hyper-V collector

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let hyperVCollectorName = "hyperVCollectorName_example"; // String | Unique name of a Hyper-V collector within a project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Standard request header. Used by service to respond to client in appropriate language.
  'collectorBody': new AzureMigrateV2.HyperVCollector() // HyperVCollector | New or Updated Hyper-V collector.
};
apiInstance.hyperVCollectorsCreate(subscriptionId, resourceGroupName, projectName, hyperVCollectorName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **hyperVCollectorName** | **String**| Unique name of a Hyper-V collector within a project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 
 **collectorBody** | [**HyperVCollector**](HyperVCollector.md)| New or Updated Hyper-V collector. | [optional] 

### Return type

[**HyperVCollector**](HyperVCollector.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## hyperVCollectorsDelete

> hyperVCollectorsDelete(subscriptionId, resourceGroupName, projectName, hyperVCollectorName, apiVersion, opts)

Deletes Hyper-V collector from the project.

Delete a Hyper-V collector from the project.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let hyperVCollectorName = "hyperVCollectorName_example"; // String | Unique name of a Hyper-V collector within a project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.hyperVCollectorsDelete(subscriptionId, resourceGroupName, projectName, hyperVCollectorName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **hyperVCollectorName** | **String**| Unique name of a Hyper-V collector within a project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hyperVCollectorsGet

> HyperVCollector hyperVCollectorsGet(subscriptionId, resourceGroupName, projectName, hyperVCollectorName, apiVersion, opts)

Get a Hyper-V collector.

Get a Hyper-V collector.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let hyperVCollectorName = "hyperVCollectorName_example"; // String | Unique name of a Hyper-V collector within a project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.hyperVCollectorsGet(subscriptionId, resourceGroupName, projectName, hyperVCollectorName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **hyperVCollectorName** | **String**| Unique name of a Hyper-V collector within a project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**HyperVCollector**](HyperVCollector.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hyperVCollectorsListByProject

> HyperVCollectorList hyperVCollectorsListByProject(subscriptionId, resourceGroupName, projectName, apiVersion, opts)

Get a list of Hyper-V collector.

Get a list of Hyper-V collector.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.hyperVCollectorsListByProject(subscriptionId, resourceGroupName, projectName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**HyperVCollectorList**](HyperVCollectorList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## machinesGet

> Machine machinesGet(subscriptionId, resourceGroupName, projectName, machineName, apiVersion, opts)

Get a specific machine.

Get the machine with the specified name. Returns a json object of type &#39;machine&#39; defined in Models section.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let machineName = "machineName_example"; // String | Unique name of a machine in private datacenter.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.machinesGet(subscriptionId, resourceGroupName, projectName, machineName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **machineName** | **String**| Unique name of a machine in private datacenter. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**Machine**](Machine.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## machinesListByProject

> MachineResultList machinesListByProject(subscriptionId, resourceGroupName, projectName, apiVersion, opts)

Get all machines in the project

Get data of all the machines available in the project. Returns a json array of objects of type &#39;machine&#39; defined in Models section.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.machinesListByProject(subscriptionId, resourceGroupName, projectName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**MachineResultList**](MachineResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## operationsList

> OperationResultList operationsList()

Get list of operations supported in the API.

Get a list of REST API supported by Microsoft.Migrate provider.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
apiInstance.operationsList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**OperationResultList**](OperationResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectAssessmentOptions

> AssessmentOptions projectAssessmentOptions(subscriptionId, resourceGroupName, projectName, assessmentOptionsName, apiVersion, opts)

Get all available options for the properties of an assessment on a project.

Get all available options for the properties of an assessment on a project.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let assessmentOptionsName = "assessmentOptionsName_example"; // String | Name of the assessment options. The only name accepted in default.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.projectAssessmentOptions(subscriptionId, resourceGroupName, projectName, assessmentOptionsName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **assessmentOptionsName** | **String**| Name of the assessment options. The only name accepted in default. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**AssessmentOptions**](AssessmentOptions.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectAssessmentOptionsList

> AssessmentOptionsResultList projectAssessmentOptionsList(subscriptionId, resourceGroupName, projectName, apiVersion, opts)

Gets list of all available options for the properties of an assessment on a project.

Gets list of all available options for the properties of an assessment on a project.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.projectAssessmentOptionsList(subscriptionId, resourceGroupName, projectName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**AssessmentOptionsResultList**](AssessmentOptionsResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsCreate

> Project projectsCreate(subscriptionId, resourceGroupName, projectName, apiVersion, opts)

Create or update project.

Create a project with specified name. If a project already exists, update it.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Standard request header. Used by service to respond to client in appropriate language.
  'project': new AzureMigrateV2.Project() // Project | New or Updated project object.
};
apiInstance.projectsCreate(subscriptionId, resourceGroupName, projectName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 
 **project** | [**Project**](Project.md)| New or Updated project object. | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectsDelete

> projectsDelete(subscriptionId, resourceGroupName, projectName, apiVersion, opts)

Delete the project

Delete the project. Deleting non-existent project is a no-operation.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.projectsDelete(subscriptionId, resourceGroupName, projectName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsGet

> Project projectsGet(subscriptionId, resourceGroupName, projectName, apiVersion, opts)

Get the specified project.

Get the project with the specified name.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.projectsGet(subscriptionId, resourceGroupName, projectName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsList

> ProjectResultList projectsList(subscriptionId, resourceGroupName, apiVersion, opts)

Get all projects.

Get all the projects in the resource group.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.projectsList(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**ProjectResultList**](ProjectResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsListBySubscription

> ProjectResultList projectsListBySubscription(subscriptionId, apiVersion, opts)

Get all projects.

Get all the projects in the subscription.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.projectsListBySubscription(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**ProjectResultList**](ProjectResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsUpdate

> Project projectsUpdate(subscriptionId, resourceGroupName, projectName, apiVersion, opts)

Update project.

Update a project with specified name. Supports partial updates, for example only tags can be provided.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Standard request header. Used by service to respond to client in appropriate language.
  'project': new AzureMigrateV2.Project() // Project | Updated project object.
};
apiInstance.projectsUpdate(subscriptionId, resourceGroupName, projectName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 
 **project** | [**Project**](Project.md)| Updated project object. | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## vMwareCollectorsCreate

> VMwareCollector vMwareCollectorsCreate(subscriptionId, resourceGroupName, projectName, vmWareCollectorName, apiVersion, opts)

Create or Update VMware collector.

Create or Update VMware collector

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let vmWareCollectorName = "vmWareCollectorName_example"; // String | Unique name of a VMware collector within a project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Standard request header. Used by service to respond to client in appropriate language.
  'collectorBody': new AzureMigrateV2.VMwareCollector() // VMwareCollector | New or Updated VMware collector.
};
apiInstance.vMwareCollectorsCreate(subscriptionId, resourceGroupName, projectName, vmWareCollectorName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **vmWareCollectorName** | **String**| Unique name of a VMware collector within a project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 
 **collectorBody** | [**VMwareCollector**](VMwareCollector.md)| New or Updated VMware collector. | [optional] 

### Return type

[**VMwareCollector**](VMwareCollector.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## vMwareCollectorsDelete

> vMwareCollectorsDelete(subscriptionId, resourceGroupName, projectName, vmWareCollectorName, apiVersion, opts)

Deletes VMware collector from the project.

Delete a VMware collector from the project.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let vmWareCollectorName = "vmWareCollectorName_example"; // String | Unique name of a VMware collector within a project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.vMwareCollectorsDelete(subscriptionId, resourceGroupName, projectName, vmWareCollectorName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **vmWareCollectorName** | **String**| Unique name of a VMware collector within a project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vMwareCollectorsGet

> VMwareCollector vMwareCollectorsGet(subscriptionId, resourceGroupName, projectName, vmWareCollectorName, apiVersion, opts)

Get a VMware collector.

Get a VMware collector.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let vmWareCollectorName = "vmWareCollectorName_example"; // String | Unique name of a VMware collector within a project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.vMwareCollectorsGet(subscriptionId, resourceGroupName, projectName, vmWareCollectorName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **vmWareCollectorName** | **String**| Unique name of a VMware collector within a project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**VMwareCollector**](VMwareCollector.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vMwareCollectorsListByProject

> VMwareCollectorList vMwareCollectorsListByProject(subscriptionId, resourceGroupName, projectName, apiVersion, opts)

Get a list of VMware collector.

Get a list of VMware collector.

### Example

```javascript
import AzureMigrateV2 from 'azure_migrate_v2';
let defaultClient = AzureMigrateV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrateV2.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.vMwareCollectorsListByProject(subscriptionId, resourceGroupName, projectName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription Id in which project was created. | 
 **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | 
 **projectName** | **String**| Name of the Azure Migrate project. | 
 **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | 
 **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] 

### Return type

[**VMwareCollectorList**](VMwareCollectorList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

