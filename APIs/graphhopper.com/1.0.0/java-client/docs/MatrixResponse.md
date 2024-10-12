

# MatrixResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**distances** | **List&lt;List&lt;BigDecimal&gt;&gt;** | The distance matrix for the specified points in the same order as the time matrix. The distances are in meters. If &#x60;fail_fast&#x3D;false&#x60; the matrix will contain &#x60;null&#x60; for connections that could not be found. |  [optional] |
|**hints** | [**List&lt;MatrixResponseHintsInner&gt;**](MatrixResponseHintsInner.md) | Optional. Additional response data. |  [optional] |
|**info** | [**ResponseInfo**](ResponseInfo.md) |  |  [optional] |
|**times** | **List&lt;List&lt;BigDecimal&gt;&gt;** | The time matrix for the specified points in the order [[from1-&gt;to1, from1-&gt;to2, ...], [from2-&gt;to1, from2-&gt;to2, ...], ...]. The times are in seconds. If &#x60;fail_fast&#x3D;false&#x60; the matrix will contain &#x60;null&#x60; for connections that could not be found. |  [optional] |
|**weights** | **List&lt;List&lt;Double&gt;&gt;** | The weight matrix for the specified points in the same order as the time matrix. The weights for different vehicles can have a different unit but the weights array is perfectly suited as input for Vehicle Routing Problems as it is currently faster to calculate. If &#x60;fail_fast&#x3D;false&#x60; the matrix will contain &#x60;null&#x60; for connections that could not be found. |  [optional] |



