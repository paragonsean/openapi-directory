# AzureMigrate.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assessedMachinesGet**](DefaultApi.md#assessedMachinesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName}/assessments/{assessmentName}/assessedMachines/{assessedMachineName} | Get an assessed machine.
[**assessedMachinesListByAssessment**](DefaultApi.md#assessedMachinesListByAssessment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName}/assessments/{assessmentName}/assessedMachines | Get assessed machines for assessment.
[**assessmentsCreate**](DefaultApi.md#assessmentsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName}/assessments/{assessmentName} | Create or Update assessment.
[**assessmentsDelete**](DefaultApi.md#assessmentsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName}/assessments/{assessmentName} | Deletes an assessment from the project.
[**assessmentsGet**](DefaultApi.md#assessmentsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName}/assessments/{assessmentName} | Get an assessment.
[**assessmentsGetReportDownloadUrl**](DefaultApi.md#assessmentsGetReportDownloadUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName}/assessments/{assessmentName}/downloadUrl | Get download URL for the assessment report.
[**assessmentsListByGroup**](DefaultApi.md#assessmentsListByGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName}/assessments | Get all assessments created for the specified group.
[**assessmentsListByProject**](DefaultApi.md#assessmentsListByProject) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/assessments | Get all assessments created in the project.
[**groupsCreate**](DefaultApi.md#groupsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName} | Create a new group with specified settings. If group with the name provided already exists, then the existing group is updated.
[**groupsDelete**](DefaultApi.md#groupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName} | Delete the group
[**groupsGet**](DefaultApi.md#groupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName} | Get a specific group.
[**groupsListByProject**](DefaultApi.md#groupsListByProject) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups | Get all groups
[**machinesGet**](DefaultApi.md#machinesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/machines/{machineName} | Get a specific machine.
[**machinesListByProject**](DefaultApi.md#machinesListByProject) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/machines | Get all machines in the project
[**operationsList**](DefaultApi.md#operationsList) | **GET** /providers/Microsoft.Migrate/operations | Get list of operations supported in the API.
[**projectsCreate**](DefaultApi.md#projectsCreate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName} | Create or update project.
[**projectsDelete**](DefaultApi.md#projectsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName} | Delete the project
[**projectsGet**](DefaultApi.md#projectsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName} | Get the specified project.
[**projectsGetKeys**](DefaultApi.md#projectsGetKeys) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/keys | Get shared keys for the project.
[**projectsList**](DefaultApi.md#projectsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/projects | Get all projects.
[**projectsUpdate**](DefaultApi.md#projectsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName} | Update project.



## assessedMachinesGet

> AssessedMachine assessedMachinesGet(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, assessedMachineName, apiVersion, opts)

Get an assessed machine.

Get an assessed machine with its size &amp; cost estimate that was evaluated in the specified assessment.

### Example

```javascript
import AzureMigrate from 'azure_migrate';
let defaultClient = AzureMigrate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrate.DefaultApi();
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
import AzureMigrate from 'azure_migrate';
let defaultClient = AzureMigrate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrate.DefaultApi();
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
import AzureMigrate from 'azure_migrate';
let defaultClient = AzureMigrate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrate.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let groupName = "groupName_example"; // String | Unique name of a group within a project.
let assessmentName = "assessmentName_example"; // String | Unique name of an assessment within a project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Standard request header. Used by service to respond to client in appropriate language.
  'assessment': new AzureMigrate.Assessment() // Assessment | New or Updated Assessment object.
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
import AzureMigrate from 'azure_migrate';
let defaultClient = AzureMigrate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrate.DefaultApi();
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
- **Accept**: Not defined


## assessmentsGet

> Assessment assessmentsGet(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, apiVersion, opts)

Get an assessment.

Get an existing assessment with the specified name. Returns a json object of type &#39;assessment&#39; as specified in Models section.

### Example

```javascript
import AzureMigrate from 'azure_migrate';
let defaultClient = AzureMigrate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrate.DefaultApi();
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
import AzureMigrate from 'azure_migrate';
let defaultClient = AzureMigrate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrate.DefaultApi();
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
import AzureMigrate from 'azure_migrate';
let defaultClient = AzureMigrate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrate.DefaultApi();
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
import AzureMigrate from 'azure_migrate';
let defaultClient = AzureMigrate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrate.DefaultApi();
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

Create a new group with specified settings. If group with the name provided already exists, then the existing group is updated.

Create a new group by sending a json object of type &#39;group&#39; as given in Models section as part of the Request Body. The group name in a project is unique. Labels can be applied on a group as part of creation.  If a group with the groupName specified in the URL already exists, then this call acts as an update.  This operation is Idempotent. 

### Example

```javascript
import AzureMigrate from 'azure_migrate';
let defaultClient = AzureMigrate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrate.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let groupName = "groupName_example"; // String | Unique name of a group within a project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Standard request header. Used by service to respond to client in appropriate language.
  'group': new AzureMigrate.Group() // Group | New or Updated Group object.
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
import AzureMigrate from 'azure_migrate';
let defaultClient = AzureMigrate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrate.DefaultApi();
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
- **Accept**: Not defined


## groupsGet

> Group groupsGet(subscriptionId, resourceGroupName, projectName, groupName, apiVersion, opts)

Get a specific group.

Get information related to a specific group in the project. Returns a json object of type &#39;group&#39; as specified in the models section.

### Example

```javascript
import AzureMigrate from 'azure_migrate';
let defaultClient = AzureMigrate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrate.DefaultApi();
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
import AzureMigrate from 'azure_migrate';
let defaultClient = AzureMigrate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrate.DefaultApi();
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


## machinesGet

> Machine machinesGet(subscriptionId, resourceGroupName, projectName, machineName, apiVersion, opts)

Get a specific machine.

Get the machine with the specified name. Returns a json object of type &#39;machine&#39; defined in Models section.

### Example

```javascript
import AzureMigrate from 'azure_migrate';
let defaultClient = AzureMigrate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrate.DefaultApi();
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
import AzureMigrate from 'azure_migrate';
let defaultClient = AzureMigrate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrate.DefaultApi();
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
import AzureMigrate from 'azure_migrate';
let defaultClient = AzureMigrate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrate.DefaultApi();
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


## projectsCreate

> Project projectsCreate(subscriptionId, resourceGroupName, projectName, apiVersion, opts)

Create or update project.

Create a project with specified name. If a project already exists, update it.

### Example

```javascript
import AzureMigrate from 'azure_migrate';
let defaultClient = AzureMigrate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrate.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Standard request header. Used by service to respond to client in appropriate language.
  'project': new AzureMigrate.Project() // Project | New or Updated project object.
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
import AzureMigrate from 'azure_migrate';
let defaultClient = AzureMigrate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrate.DefaultApi();
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
- **Accept**: Not defined


## projectsGet

> Project projectsGet(subscriptionId, resourceGroupName, projectName, apiVersion, opts)

Get the specified project.

Get the project with the specified name.

### Example

```javascript
import AzureMigrate from 'azure_migrate';
let defaultClient = AzureMigrate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrate.DefaultApi();
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


## projectsGetKeys

> ProjectKey projectsGetKeys(subscriptionId, resourceGroupName, projectName, apiVersion, opts)

Get shared keys for the project.

Gets the Log Analytics Workspace ID and Primary Key for the specified project.

### Example

```javascript
import AzureMigrate from 'azure_migrate';
let defaultClient = AzureMigrate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrate.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example" // String | Standard request header. Used by service to respond to client in appropriate language.
};
apiInstance.projectsGetKeys(subscriptionId, resourceGroupName, projectName, apiVersion, opts, (error, data, response) => {
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

[**ProjectKey**](ProjectKey.md)

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
import AzureMigrate from 'azure_migrate';
let defaultClient = AzureMigrate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrate.DefaultApi();
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


## projectsUpdate

> Project projectsUpdate(subscriptionId, resourceGroupName, projectName, apiVersion, opts)

Update project.

Update a project with specified name. Supports partial updates, for example only tags can be provided.

### Example

```javascript
import AzureMigrate from 'azure_migrate';
let defaultClient = AzureMigrate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMigrate.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
let projectName = "projectName_example"; // String | Name of the Azure Migrate project.
let apiVersion = "apiVersion_example"; // String | Standard request header. Used by service to identify API version used by client.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Standard request header. Used by service to respond to client in appropriate language.
  'project': new AzureMigrate.Project() // Project | Updated project object.
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

