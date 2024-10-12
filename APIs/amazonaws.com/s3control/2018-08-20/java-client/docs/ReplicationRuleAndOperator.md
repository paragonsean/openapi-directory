

# ReplicationRuleAndOperator

<p>A container for specifying rule filters. The filters determine the subset of objects to which the rule applies. This element is required only if you specify more than one filter. </p> <p>For example:</p> <ul> <li> <p>If you specify both a <code>Prefix</code> and a <code>Tag</code> filter, wrap these filters in an <code>And</code> element. </p> </li> <li> <p>If you specify a filter based on multiple tags, wrap the <code>Tag</code> elements in an <code>And</code> element.</p> </li> </ul>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**prefix** | [**String**](String.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |



