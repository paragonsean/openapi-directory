

# AutoScaleRun

The results and errors from an execution of a pool autoscale formula.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | [**AutoScaleRunError**](AutoScaleRunError.md) |  |  [optional] |
|**results** | **String** | Gets or sets the final values of all variables used in the evaluation of the autoscale formula.  Each variable value is returned in the form $variable&#x3D;value, and variables are separated by semicolons. |  [optional] |
|**timestamp** | **OffsetDateTime** | Gets or sets the time at which the autoscale formula was last evaluated. |  |



