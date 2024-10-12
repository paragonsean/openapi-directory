# AmazonMacie2.UpdateMacieSessionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**findingPublishingFrequency** | **String** | The frequency with which Amazon Macie publishes updates to policy findings for an account. This includes publishing updates to Security Hub and Amazon EventBridge (formerly Amazon CloudWatch Events). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/macie/latest/user/findings-monitor.html\&quot;&gt;Monitoring and processing findings&lt;/a&gt; in the &lt;i&gt;Amazon Macie User Guide&lt;/i&gt;. Valid values are: | [optional] 
**status** | **String** | The status of an Amazon Macie account. Valid values are: | [optional] 



## Enum: FindingPublishingFrequencyEnum


* `FIFTEEN_MINUTES` (value: `"FIFTEEN_MINUTES"`)

* `ONE_HOUR` (value: `"ONE_HOUR"`)

* `SIX_HOURS` (value: `"SIX_HOURS"`)





## Enum: StatusEnum


* `PAUSED` (value: `"PAUSED"`)

* `ENABLED` (value: `"ENABLED"`)




