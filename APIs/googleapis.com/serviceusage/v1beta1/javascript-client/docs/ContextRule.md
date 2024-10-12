# ServiceUsageApi.ContextRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedRequestExtensions** | **[String]** | A list of full type names or extension IDs of extensions allowed in grpc side channel from client to backend. | [optional] 
**allowedResponseExtensions** | **[String]** | A list of full type names or extension IDs of extensions allowed in grpc side channel from backend to client. | [optional] 
**provided** | **[String]** | A list of full type names of provided contexts. | [optional] 
**requested** | **[String]** | A list of full type names of requested contexts. | [optional] 
**selector** | **String** | Selects the methods to which this rule applies. Refer to selector for syntax details. | [optional] 


