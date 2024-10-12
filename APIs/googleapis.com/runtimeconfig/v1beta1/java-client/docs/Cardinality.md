

# Cardinality

A Cardinality condition for the Waiter resource. A cardinality condition is met when the number of variables under a specified path prefix reaches a predefined number. For example, if you set a Cardinality condition where the `path` is set to `/foo` and the number of paths is set to `2`, the following variables would meet the condition in a RuntimeConfig resource: + `/foo/variable1 = \"value1\"` + `/foo/variable2 = \"value2\"` + `/bar/variable3 = \"value3\"` It would not satisfy the same condition with the `number` set to `3`, however, because there is only 2 paths that start with `/foo`. Cardinality conditions are recursive; all subtrees under the specific path prefix are counted.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**number** | **Integer** | The number variables under the &#x60;path&#x60; that must exist to meet this condition. Defaults to 1 if not specified. |  [optional] |
|**path** | **String** | The root of the variable subtree to monitor. For example, &#x60;/foo&#x60;. |  [optional] |



