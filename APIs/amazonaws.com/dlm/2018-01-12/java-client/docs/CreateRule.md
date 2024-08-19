

# CreateRule

<p> <b>[Snapshot and AMI policies only]</b> Specifies when the policy should create snapshots or AMIs.</p> <note> <ul> <li> <p>You must specify either <b>CronExpression</b>, or <b>Interval</b>, <b>IntervalUnit</b>, and <b>Times</b>.</p> </li> <li> <p>If you need to specify an <a>ArchiveRule</a> for the schedule, then you must specify a creation frequency of at least 28 days.</p> </li> </ul> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**location** | [**LocationValues**](LocationValues.md) |  |  [optional] |
|**interval** | [**Integer**](Integer.md) |  |  [optional] |
|**intervalUnit** | [**IntervalUnitValues**](IntervalUnitValues.md) |  |  [optional] |
|**times** | [**List**](List.md) |  |  [optional] |
|**cronExpression** | [**String**](String.md) |  |  [optional] |



