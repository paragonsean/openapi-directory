

# UpdateBordersRequest

Updates the borders of a range. If a field is not set in the request, that means the border remains as-is. For example, with two subsequent UpdateBordersRequest: 1. range: A1:A5 `{ top: RED, bottom: WHITE }` 2. range: A1:A5 `{ left: BLUE }` That would result in A1:A5 having a borders of `{ top: RED, bottom: WHITE, left: BLUE }`. If you want to clear a border, explicitly set the style to NONE.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bottom** | [**Border**](Border.md) |  |  [optional] |
|**innerHorizontal** | [**Border**](Border.md) |  |  [optional] |
|**innerVertical** | [**Border**](Border.md) |  |  [optional] |
|**left** | [**Border**](Border.md) |  |  [optional] |
|**range** | [**GridRange**](GridRange.md) |  |  [optional] |
|**right** | [**Border**](Border.md) |  |  [optional] |
|**top** | [**Border**](Border.md) |  |  [optional] |



