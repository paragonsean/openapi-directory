# ElmahIoApi.CreateDeployment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Date** | When was this deployment created in UTC. Defaults to current time if not specified. | [optional] 
**description** | **String** | Optional description of this deployment. Can be markdown or clear text. | [optional] 
**logId** | **String** | As default, deployments are attached all logs of the organization. If you want a deployment to  attach to a single log only, set this to the ID of that log. | [optional] 
**userEmail** | **String** | The email of the person responsible for creating this deployment. This can be the email taken from  your deployment server (like Azure DevOps or Octopus). | [optional] 
**userName** | **String** | The name of the person responsible for creating this deployment. This can be the name taken from  your deployment server (like Azure DevOps or Octopus). | [optional] 
**version** | **String** | The version number of this deployment. The value of version can be a SemVer compliant string or any other  syntax that you are using as your version numbering scheme. | 


