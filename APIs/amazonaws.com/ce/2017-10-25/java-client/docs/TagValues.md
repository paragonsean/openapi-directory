

# TagValues

<p>The values that are available for a tag.</p> <p>If <code>Values</code> and <code>Key</code> aren't specified, the <code>ABSENT</code> <code>MatchOption</code> is applied to all tags. That is, it's filtered on resources with no tags.</p> <p>If <code>Key</code> is provided and <code>Values</code> isn't specified, the <code>ABSENT</code> <code>MatchOption</code> is applied to the tag <code>Key</code> only. That is, it's filtered on resources without the given tag key.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | [**String**](String.md) |  |  [optional] |
|**values** | [**List**](List.md) |  |  [optional] |
|**matchOptions** | [**List**](List.md) |  |  [optional] |



