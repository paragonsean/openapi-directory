

# ControlScope

<p>A framework consists of one or more controls. Each control has its own control scope. The control scope can include one or more resource types, a combination of a tag key and value, or a combination of one resource type and one resource ID. If no scope is specified, evaluations for the rule are triggered when any resource in your recording group changes in configuration.</p> <note> <p>To set a control scope that includes all of a particular resource, leave the <code>ControlScope</code> empty or do not pass it when calling <code>CreateFramework</code>.</p> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**complianceResourceIds** | [**List**](List.md) |  |  [optional] |
|**complianceResourceTypes** | [**List**](List.md) |  |  [optional] |
|**tags** | [**Map**](Map.md) |  |  [optional] |



