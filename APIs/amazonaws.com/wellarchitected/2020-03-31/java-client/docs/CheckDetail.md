

# CheckDetail

Account details for a Well-Architected best practice in relation to Trusted Advisor checks.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**String**](String.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**description** | [**String**](String.md) |  |  [optional] |
|**provider** | [**CheckProvider**](CheckProvider.md) |  |  [optional] |
|**lensArn** | [**String**](String.md) |  |  [optional] |
|**pillarId** | **String** | &lt;p&gt;The ID used to identify a pillar, for example, &lt;code&gt;security&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;A pillar is identified by its &lt;a&gt;PillarReviewSummary$PillarId&lt;/a&gt;.&lt;/p&gt; |  [optional] |
|**questionId** | **String** | The ID of the question. |  [optional] |
|**choiceId** | **String** | The ID of a choice. |  [optional] |
|**status** | [**CheckStatus**](CheckStatus.md) |  |  [optional] |
|**accountId** | **String** | An Amazon Web Services account ID. |  [optional] |
|**flaggedResources** | [**Integer**](Integer.md) |  |  [optional] |
|**reason** | [**CheckFailureReason**](CheckFailureReason.md) |  |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time recorded. |  [optional] |



