# AwsBackup.UpdateReportPlanRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reportPlanDescription** | **String** | An optional description of the report plan with a maximum 1,024 characters. | [optional] 
**reportDeliveryChannel** | [**CreateReportPlanRequestReportDeliveryChannel**](CreateReportPlanRequestReportDeliveryChannel.md) |  | [optional] 
**reportSetting** | [**CreateReportPlanRequestReportSetting**](CreateReportPlanRequestReportSetting.md) |  | [optional] 
**idempotencyToken** | **String** | A customer-chosen string that you can use to distinguish between otherwise identical calls to &lt;code&gt;UpdateReportPlanInput&lt;/code&gt;. Retrying a successful request with the same idempotency token results in a success message with no action taken. | [optional] 


