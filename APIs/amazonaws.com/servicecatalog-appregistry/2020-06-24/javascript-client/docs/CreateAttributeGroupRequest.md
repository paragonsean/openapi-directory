# AwsServiceCatalogAppRegistry.CreateAttributeGroupRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the attribute group. | 
**description** | **String** | The description of the attribute group that the user provides. | [optional] 
**attributes** | **String** | A JSON string in the form of nested key-value pairs that represent the attributes in the group and describes an application and its components. | 
**tags** | **{String: String}** | Key-value pairs you can use to associate with the attribute group. | [optional] 
**clientToken** | **String** | A unique identifier that you provide to ensure idempotency. If you retry a request that completed successfully using the same client token and the same parameters, the retry succeeds without performing any further actions. If you retry a successful request using the same client token, but one or more of the parameters are different, the retry fails. | 


