

# UpdateMacieSessionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**findingPublishingFrequency** | [**FindingPublishingFrequencyEnum**](#FindingPublishingFrequencyEnum) | The frequency with which Amazon Macie publishes updates to policy findings for an account. This includes publishing updates to Security Hub and Amazon EventBridge (formerly Amazon CloudWatch Events). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/macie/latest/user/findings-monitor.html\&quot;&gt;Monitoring and processing findings&lt;/a&gt; in the &lt;i&gt;Amazon Macie User Guide&lt;/i&gt;. Valid values are: |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of an Amazon Macie account. Valid values are: |  [optional] |



## Enum: FindingPublishingFrequencyEnum

| Name | Value |
|---- | -----|
| FIFTEEN_MINUTES | &quot;FIFTEEN_MINUTES&quot; |
| ONE_HOUR | &quot;ONE_HOUR&quot; |
| SIX_HOURS | &quot;SIX_HOURS&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PAUSED | &quot;PAUSED&quot; |
| ENABLED | &quot;ENABLED&quot; |



