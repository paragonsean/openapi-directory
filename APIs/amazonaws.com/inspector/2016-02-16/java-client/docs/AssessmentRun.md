

# AssessmentRun

<p>A snapshot of an Amazon Inspector assessment run that contains the findings of the assessment run .</p> <p>Used as the response element in the <a>DescribeAssessmentRuns</a> action.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arn** | [**String**](String.md) |  |  |
|**name** | [**String**](String.md) |  |  |
|**assessmentTemplateArn** | [**String**](String.md) |  |  |
|**state** | [**AssessmentRunState**](AssessmentRunState.md) |  |  |
|**durationInSeconds** | [**Integer**](Integer.md) |  |  |
|**rulesPackageArns** | [**List**](List.md) |  |  |
|**userAttributesForFindings** | [**List**](List.md) |  |  |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**startedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**completedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**stateChangedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**dataCollected** | [**Boolean**](Boolean.md) |  |  |
|**stateChanges** | [**List**](List.md) |  |  |
|**notifications** | [**List**](List.md) |  |  |
|**findingCounts** | [**Map**](Map.md) |  |  |



