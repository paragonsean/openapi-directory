# GoogleSlidesApi.UpdatePageElementsZOrderRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **String** | The Z-order operation to apply on the page elements. When applying the operation on multiple page elements, the relative Z-orders within these page elements before the operation is maintained. | [optional] 
**pageElementObjectIds** | **[String]** | The object IDs of the page elements to update. All the page elements must be on the same page and must not be grouped. | [optional] 



## Enum: OperationEnum


* `Z_ORDER_OPERATION_UNSPECIFIED` (value: `"Z_ORDER_OPERATION_UNSPECIFIED"`)

* `BRING_TO_FRONT` (value: `"BRING_TO_FRONT"`)

* `BRING_FORWARD` (value: `"BRING_FORWARD"`)

* `SEND_BACKWARD` (value: `"SEND_BACKWARD"`)

* `SEND_TO_BACK` (value: `"SEND_TO_BACK"`)




