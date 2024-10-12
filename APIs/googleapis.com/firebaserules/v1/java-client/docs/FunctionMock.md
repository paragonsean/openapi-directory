

# FunctionMock

Mock function definition. Mocks must refer to a function declared by the target service. The type of the function args and result will be inferred at test time. If either the arg or result values are not compatible with function type declaration, the request will be considered invalid. More than one `FunctionMock` may be provided for a given function name so long as the `Arg` matchers are distinct. There may be only one function for a given overload where all `Arg` values are `Arg.any_value`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**args** | [**List&lt;Arg&gt;**](Arg.md) | The list of &#x60;Arg&#x60; values to match. The order in which the arguments are provided is the order in which they must appear in the function invocation. |  [optional] |
|**function** | **String** | The name of the function. The function name must match one provided by a service declaration. |  [optional] |
|**result** | [**Result**](Result.md) |  |  [optional] |



