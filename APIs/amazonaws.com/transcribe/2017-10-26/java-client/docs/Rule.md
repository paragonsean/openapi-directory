

# Rule

<p>A rule is a set of criteria that you can specify to flag an attribute in your Call Analytics output. Rules define a Call Analytics category.</p> <p>Rules can include these parameters: , , , and .</p> <p>To learn more about Call Analytics rules and categories, see <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-batch.html\">Creating categories for post-call transcriptions</a> and <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-stream.html\">Creating categories for real-time transcriptions</a>.</p> <p>To learn more about Call Analytics, see <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/call-analytics.html\">Analyzing call center audio with Call Analytics</a>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nonTalkTimeFilter** | [**RuleNonTalkTimeFilter**](RuleNonTalkTimeFilter.md) |  |  [optional] |
|**interruptionFilter** | [**RuleInterruptionFilter**](RuleInterruptionFilter.md) |  |  [optional] |
|**transcriptFilter** | [**RuleTranscriptFilter**](RuleTranscriptFilter.md) |  |  [optional] |
|**sentimentFilter** | [**RuleSentimentFilter**](RuleSentimentFilter.md) |  |  [optional] |



