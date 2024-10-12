

# UpdatePageElementsZOrderRequest

Updates the Z-order of page elements. Z-order is an ordering of the elements on the page from back to front. The page element in the front may cover the elements that are behind it.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**operation** | [**OperationEnum**](#OperationEnum) | The Z-order operation to apply on the page elements. When applying the operation on multiple page elements, the relative Z-orders within these page elements before the operation is maintained. |  [optional] |
|**pageElementObjectIds** | **List&lt;String&gt;** | The object IDs of the page elements to update. All the page elements must be on the same page and must not be grouped. |  [optional] |



## Enum: OperationEnum

| Name | Value |
|---- | -----|
| Z_ORDER_OPERATION_UNSPECIFIED | &quot;Z_ORDER_OPERATION_UNSPECIFIED&quot; |
| BRING_TO_FRONT | &quot;BRING_TO_FRONT&quot; |
| BRING_FORWARD | &quot;BRING_FORWARD&quot; |
| SEND_BACKWARD | &quot;SEND_BACKWARD&quot; |
| SEND_TO_BACK | &quot;SEND_TO_BACK&quot; |



