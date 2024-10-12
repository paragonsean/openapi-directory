

# ValueConstraint

This type contains a list of the dependencies that identify when a particular value is available for a given aspect of a given category. Each dependency specifies the values of another aspect of the same category (the <i>control</i> aspect), for which the given value of the given aspect can also be selected by the seller. This container consists of constraint information for the corresponding product aspect value.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicableForLocalizedAspectName** | **String** | The name of the control aspect on which the current aspect value depends. |  [optional] |
|**applicableForLocalizedAspectValues** | **List&lt;String&gt;** | Contains a list of the values of the control aspect on which this aspect&#39;s value depends. When the control aspect has any of the specified values, the current value of the current aspect will also be available. |  [optional] |



