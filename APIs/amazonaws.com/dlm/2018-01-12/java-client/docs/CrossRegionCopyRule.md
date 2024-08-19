

# CrossRegionCopyRule

<p> <b>[Snapshot and AMI policies only]</b> Specifies a cross-Region copy rule for snapshot and AMI policies.</p> <note> <p>To specify a cross-Region copy action for event-based polices, use <a>CrossRegionCopyAction</a>.</p> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**targetRegion** | [**String**](String.md) |  |  [optional] |
|**target** | [**String**](String.md) |  |  [optional] |
|**encrypted** | [**Boolean**](Boolean.md) |  |  |
|**cmkArn** | [**String**](String.md) |  |  [optional] |
|**copyTags** | [**Boolean**](Boolean.md) |  |  [optional] |
|**retainRule** | [**CrossRegionCopyRuleRetainRule**](CrossRegionCopyRuleRetainRule.md) |  |  [optional] |
|**deprecateRule** | [**CrossRegionCopyRuleDeprecateRule**](CrossRegionCopyRuleDeprecateRule.md) |  |  [optional] |



