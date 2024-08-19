# ElmahIoApi.Deployment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Date** | When was this deployment created. | [optional] 
**createdBy** | **String** | The elmah.io id of the user creating this deployment. Since deployments are created on a subscription,  the CreatedBy will contain the id of the user with the subscription. | [optional] 
**description** | **String** | Sescription of this deployment in markdown or clear text. | [optional] 
**id** | **String** | The ID of this deployment. | [optional] 
**logId** | **String** | If the deployment is attached a single log, this property is set to the ID of that log.  If null, the deployment is attached all logs on the organization. | [optional] 
**userEmail** | **String** | The email of the person responsible for creating this deployment. | [optional] 
**userName** | **String** | The name of the person responsible for creating this deployment. | [optional] 
**version** | **String** | The version number of this deployment. The value of version can be a SemVer compliant string or any other  syntax that you are using as your version numbering scheme. | [optional] 


