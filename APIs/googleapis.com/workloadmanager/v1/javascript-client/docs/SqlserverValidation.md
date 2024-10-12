# WorkloadManagerApi.SqlserverValidation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentVersion** | **String** | Optional. The agent version collected this data point | [optional] 
**instance** | **String** | Required. The instance_name of the instance that the Insight data comes from. According to https://linter.aip.dev/122/name-suffix: field names should not use the _name suffix unless the field would be ambiguous without it. | [optional] 
**projectId** | **String** | Required. The project_id of the cloud project that the Insight data comes from. | [optional] 
**validationDetails** | [**[SqlserverValidationValidationDetail]**](SqlserverValidationValidationDetail.md) | Optional. A list of SqlServer validation metrics data. | [optional] 


