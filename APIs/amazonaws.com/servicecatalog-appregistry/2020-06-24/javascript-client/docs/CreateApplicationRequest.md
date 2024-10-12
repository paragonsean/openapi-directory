# AwsServiceCatalogAppRegistry.CreateApplicationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the application. The name must be unique in the region in which you are creating the application. | 
**description** | **String** | The description of the application. | [optional] 
**tags** | **{String: String}** | Key-value pairs you can use to associate with the application. | [optional] 
**clientToken** | **String** | A unique identifier that you provide to ensure idempotency. If you retry a request that completed successfully using the same client token and the same parameters, the retry succeeds without performing any further actions. If you retry a successful request using the same client token, but one or more of the parameters are different, the retry fails. | 


