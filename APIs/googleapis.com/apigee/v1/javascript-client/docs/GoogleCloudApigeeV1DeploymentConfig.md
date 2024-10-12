# ApigeeApi.GoogleCloudApigeeV1DeploymentConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **{String: String}** | Additional key-value metadata for the deployment. | [optional] 
**basePath** | **String** | Base path where the application will be hosted. Defaults to \&quot;/\&quot;. | [optional] 
**deploymentGroups** | **[String]** | The list of deployment groups in which this proxy should be deployed. Not currently populated for shared flows. | [optional] 
**endpoints** | **{String: String}** | A mapping from basepaths to proxy endpoint names in this proxy. Not populated for shared flows. | [optional] 
**location** | **String** | Location of the API proxy bundle as a URI. | [optional] 
**name** | **String** | Name of the API or shared flow revision to be deployed in the following format: &#x60;organizations/{org}/apis/{api}/revisions/{rev}&#x60; or &#x60;organizations/{org}/sharedflows/{sharedflow}/revisions/{rev}&#x60; | [optional] 
**proxyUid** | **String** | Unique ID of the API proxy revision. | [optional] 
**serviceAccount** | **String** | The service account identity associated with this deployment. If non-empty, will be in the following format: &#x60;projects/-/serviceAccounts/{account_email}&#x60; | [optional] 
**uid** | **String** | Unique ID. The ID will only change if the deployment is deleted and recreated. | [optional] 


