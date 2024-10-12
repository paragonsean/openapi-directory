# SiteRecoveryManagementClient.ReplicationRecoveryPlansApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replicationRecoveryPlansCreate**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansCreate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName} | Creates a recovery plan with the given details.
[**replicationRecoveryPlansDelete**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansDelete) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName} | Deletes the specified recovery plan.
[**replicationRecoveryPlansFailoverCommit**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansFailoverCommit) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName}/failoverCommit | Execute commit failover of the recovery plan.
[**replicationRecoveryPlansGet**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName} | Gets the requested recovery plan.
[**replicationRecoveryPlansList**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans | Gets the list of recovery plans.
[**replicationRecoveryPlansPlannedFailover**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansPlannedFailover) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName}/plannedFailover | Execute planned failover of the recovery plan.
[**replicationRecoveryPlansReprotect**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansReprotect) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName}/reProtect | Execute reprotect of the recovery plan.
[**replicationRecoveryPlansTestFailover**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansTestFailover) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName}/testFailover | Execute test failover of the recovery plan.
[**replicationRecoveryPlansTestFailoverCleanup**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansTestFailoverCleanup) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName}/testFailoverCleanup | Execute test failover cleanup of the recovery plan.
[**replicationRecoveryPlansUnplannedFailover**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansUnplannedFailover) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName}/unplannedFailover | Execute unplanned failover of the recovery plan.
[**replicationRecoveryPlansUpdate**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansUpdate) | **PATCH** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName} | Updates the given recovery plan.



## replicationRecoveryPlansCreate

> RecoveryPlan replicationRecoveryPlansCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input)

Creates a recovery plan with the given details.

The operation to create a recovery plan.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationRecoveryPlansApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let recoveryPlanName = "recoveryPlanName_example"; // String | Recovery plan name.
let input = new SiteRecoveryManagementClient.CreateRecoveryPlanInput(); // CreateRecoveryPlanInput | Recovery Plan creation input.
apiInstance.replicationRecoveryPlansCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **recoveryPlanName** | **String**| Recovery plan name. | 
 **input** | [**CreateRecoveryPlanInput**](CreateRecoveryPlanInput.md)| Recovery Plan creation input. | 

### Return type

[**RecoveryPlan**](RecoveryPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationRecoveryPlansDelete

> replicationRecoveryPlansDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName)

Deletes the specified recovery plan.

Delete a recovery plan.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationRecoveryPlansApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let recoveryPlanName = "recoveryPlanName_example"; // String | Recovery plan name.
apiInstance.replicationRecoveryPlansDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **recoveryPlanName** | **String**| Recovery plan name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## replicationRecoveryPlansFailoverCommit

> RecoveryPlan replicationRecoveryPlansFailoverCommit(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName)

Execute commit failover of the recovery plan.

The operation to commit the fail over of a recovery plan.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationRecoveryPlansApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let recoveryPlanName = "recoveryPlanName_example"; // String | Recovery plan name.
apiInstance.replicationRecoveryPlansFailoverCommit(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **recoveryPlanName** | **String**| Recovery plan name. | 

### Return type

[**RecoveryPlan**](RecoveryPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationRecoveryPlansGet

> RecoveryPlan replicationRecoveryPlansGet(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName)

Gets the requested recovery plan.

Gets the details of the recovery plan.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationRecoveryPlansApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let recoveryPlanName = "recoveryPlanName_example"; // String | Name of the recovery plan.
apiInstance.replicationRecoveryPlansGet(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **recoveryPlanName** | **String**| Name of the recovery plan. | 

### Return type

[**RecoveryPlan**](RecoveryPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationRecoveryPlansList

> RecoveryPlanCollection replicationRecoveryPlansList(apiVersion, resourceName, resourceGroupName, subscriptionId)

Gets the list of recovery plans.

Lists the recovery plans in the vault.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationRecoveryPlansApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
apiInstance.replicationRecoveryPlansList(apiVersion, resourceName, resourceGroupName, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 

### Return type

[**RecoveryPlanCollection**](RecoveryPlanCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationRecoveryPlansPlannedFailover

> RecoveryPlan replicationRecoveryPlansPlannedFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input)

Execute planned failover of the recovery plan.

The operation to start the planned failover of a recovery plan.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationRecoveryPlansApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let recoveryPlanName = "recoveryPlanName_example"; // String | Recovery plan name.
let input = new SiteRecoveryManagementClient.RecoveryPlanPlannedFailoverInput(); // RecoveryPlanPlannedFailoverInput | Failover input.
apiInstance.replicationRecoveryPlansPlannedFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **recoveryPlanName** | **String**| Recovery plan name. | 
 **input** | [**RecoveryPlanPlannedFailoverInput**](RecoveryPlanPlannedFailoverInput.md)| Failover input. | 

### Return type

[**RecoveryPlan**](RecoveryPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationRecoveryPlansReprotect

> RecoveryPlan replicationRecoveryPlansReprotect(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName)

Execute reprotect of the recovery plan.

The operation to reprotect(reverse replicate) a recovery plan.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationRecoveryPlansApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let recoveryPlanName = "recoveryPlanName_example"; // String | Recovery plan name.
apiInstance.replicationRecoveryPlansReprotect(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **recoveryPlanName** | **String**| Recovery plan name. | 

### Return type

[**RecoveryPlan**](RecoveryPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationRecoveryPlansTestFailover

> RecoveryPlan replicationRecoveryPlansTestFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input)

Execute test failover of the recovery plan.

The operation to start the test failover of a recovery plan.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationRecoveryPlansApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let recoveryPlanName = "recoveryPlanName_example"; // String | Recovery plan name.
let input = new SiteRecoveryManagementClient.RecoveryPlanTestFailoverInput(); // RecoveryPlanTestFailoverInput | Failover input.
apiInstance.replicationRecoveryPlansTestFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **recoveryPlanName** | **String**| Recovery plan name. | 
 **input** | [**RecoveryPlanTestFailoverInput**](RecoveryPlanTestFailoverInput.md)| Failover input. | 

### Return type

[**RecoveryPlan**](RecoveryPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationRecoveryPlansTestFailoverCleanup

> RecoveryPlan replicationRecoveryPlansTestFailoverCleanup(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input)

Execute test failover cleanup of the recovery plan.

The operation to cleanup test failover of a recovery plan.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationRecoveryPlansApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let recoveryPlanName = "recoveryPlanName_example"; // String | Recovery plan name.
let input = new SiteRecoveryManagementClient.RecoveryPlanTestFailoverCleanupInput(); // RecoveryPlanTestFailoverCleanupInput | Test failover cleanup input.
apiInstance.replicationRecoveryPlansTestFailoverCleanup(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **recoveryPlanName** | **String**| Recovery plan name. | 
 **input** | [**RecoveryPlanTestFailoverCleanupInput**](RecoveryPlanTestFailoverCleanupInput.md)| Test failover cleanup input. | 

### Return type

[**RecoveryPlan**](RecoveryPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationRecoveryPlansUnplannedFailover

> RecoveryPlan replicationRecoveryPlansUnplannedFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input)

Execute unplanned failover of the recovery plan.

The operation to start the failover of a recovery plan.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationRecoveryPlansApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let recoveryPlanName = "recoveryPlanName_example"; // String | Recovery plan name.
let input = new SiteRecoveryManagementClient.RecoveryPlanUnplannedFailoverInput(); // RecoveryPlanUnplannedFailoverInput | Failover input.
apiInstance.replicationRecoveryPlansUnplannedFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **recoveryPlanName** | **String**| Recovery plan name. | 
 **input** | [**RecoveryPlanUnplannedFailoverInput**](RecoveryPlanUnplannedFailoverInput.md)| Failover input. | 

### Return type

[**RecoveryPlan**](RecoveryPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationRecoveryPlansUpdate

> RecoveryPlan replicationRecoveryPlansUpdate(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input)

Updates the given recovery plan.

The operation to update a recovery plan.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationRecoveryPlansApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let recoveryPlanName = "recoveryPlanName_example"; // String | Recovery plan name.
let input = new SiteRecoveryManagementClient.UpdateRecoveryPlanInput(); // UpdateRecoveryPlanInput | Update recovery plan input
apiInstance.replicationRecoveryPlansUpdate(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **recoveryPlanName** | **String**| Recovery plan name. | 
 **input** | [**UpdateRecoveryPlanInput**](UpdateRecoveryPlanInput.md)| Update recovery plan input | 

### Return type

[**RecoveryPlan**](RecoveryPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

