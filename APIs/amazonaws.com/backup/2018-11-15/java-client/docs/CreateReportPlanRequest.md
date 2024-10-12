

# CreateReportPlanRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reportPlanName** | **String** | The unique name of the report plan. The name must be between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_). |  |
|**reportPlanDescription** | **String** | An optional description of the report plan with a maximum of 1,024 characters. |  [optional] |
|**reportDeliveryChannel** | [**CreateReportPlanRequestReportDeliveryChannel**](CreateReportPlanRequestReportDeliveryChannel.md) |  |  |
|**reportSetting** | [**CreateReportPlanRequestReportSetting**](CreateReportPlanRequestReportSetting.md) |  |  |
|**reportPlanTags** | **Map&lt;String, String&gt;** | Metadata that you can assign to help organize the report plans that you create. Each tag is a key-value pair. |  [optional] |
|**idempotencyToken** | **String** | A customer-chosen string that you can use to distinguish between otherwise identical calls to &lt;code&gt;CreateReportPlanInput&lt;/code&gt;. Retrying a successful request with the same idempotency token results in a success message with no action taken. |  [optional] |



