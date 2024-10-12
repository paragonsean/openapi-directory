

# ConditionalSplitActivity

<p>Specifies the settings for a yes/no split activity in a journey. This type of activity sends participants down one of two paths in a journey, based on conditions that you specify.</p> <note><p>To create yes/no split activities that send participants down different paths based on push notification events (such as Open or Received events), your mobile app has to specify the User ID and Endpoint ID values. For more information, see <a href=\"https://docs.aws.amazon.com/pinpoint/latest/developerguide/integrate.html\">Integrating Amazon Pinpoint with your application</a> in the <i>Amazon Pinpoint Developer Guide</i>.</p></note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**condition** | [**ConditionalSplitActivityCondition**](ConditionalSplitActivityCondition.md) |  |  [optional] |
|**evaluationWaitTime** | [**ConditionalSplitActivityEvaluationWaitTime**](ConditionalSplitActivityEvaluationWaitTime.md) |  |  [optional] |
|**falseActivity** | [**String**](String.md) |  |  [optional] |
|**trueActivity** | [**String**](String.md) |  |  [optional] |



