

# StackDriftInformationSummary

Contains information about whether the stack's actual configuration differs, or has <i>drifted</i>, from its expected configuration, as defined in the stack template and any values specified as template parameters. A stack is considered to have drifted if one or more of its resources have drifted.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stackDriftStatus** | [**StackDriftStatus**](StackDriftStatus.md) |  |  |
|**lastCheckTimestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



