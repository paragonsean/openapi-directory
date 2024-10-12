# AgentOsApiV3MaintenanceCallGroup.MaintenanceControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**maintenanceControllerCreateMaintenanceJob**](MaintenanceControllerApi.md#maintenanceControllerCreateMaintenanceJob) | **POST** /v3/maintenance/{shortName}/maintenance/{branchID}/createmaintenancejob | Create a maintenance job for a specific branch



## maintenanceControllerCreateMaintenanceJob

> Object maintenanceControllerCreateMaintenanceJob(shortName, branchID, maintenanceIssueModel)

Create a maintenance job for a specific branch

### Example

```javascript
import AgentOsApiV3MaintenanceCallGroup from 'agent_os_api_v3_maintenance_call_group';

let apiInstance = new AgentOsApiV3MaintenanceCallGroup.MaintenanceControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let branchID = "branchID_example"; // String | The unique ID of the Branch
let maintenanceIssueModel = new AgentOsApiV3MaintenanceCallGroup.MaintenanceIssueModel(); // MaintenanceIssueModel | A JSON object containing details of the maintenance job
apiInstance.maintenanceControllerCreateMaintenanceJob(shortName, branchID, maintenanceIssueModel, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **branchID** | **String**| The unique ID of the Branch | 
 **maintenanceIssueModel** | [**MaintenanceIssueModel**](MaintenanceIssueModel.md)| A JSON object containing details of the maintenance job | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

