# AwsMainframeModernization.CreateApplicationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientToken** | **String** | Unique, case-sensitive identifier the service generates to ensure the idempotency of the request to create an application. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires.  | [optional] 
**definition** | [**CreateApplicationRequestDefinition**](CreateApplicationRequestDefinition.md) |  | 
**description** | **String** | The description of the application. | [optional] 
**engineType** | **String** | The type of the target platform for this application. | 
**kmsKeyId** | **String** | The identifier of a customer managed key. | [optional] 
**name** | **String** | The unique identifier of the application. | 
**roleArn** | **String** | The Amazon Resource Name (ARN) that identifies a role that the application uses to access Amazon Web Services resources that are not part of the application or are in a different Amazon Web Services account. | [optional] 
**tags** | **{String: String}** | A list of tags to apply to the application. | [optional] 



## Enum: EngineTypeEnum


* `microfocus` (value: `"microfocus"`)

* `bluage` (value: `"bluage"`)




