# PaccurateIo.Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **String** | designated color name for the item in pack visualizations. | [optional] 
**dimensions** | [**Point**](Point.md) | the length, width, and height of the item. | 
**name** | **String** | name or description of item for your reference. | [optional] 
**refId** | **Number** | item type reference identifier passed backed from request. | [optional] 
**sequence** | **String** | A sequence value for the item. This is intended for aisle-bin locations, e.g., aisle 11 bin 20 can be &#39;1120&#39;. Combined with maxSequenceDistance, you can restrict cartons to only have contents from within a certain range. This is very helpful for cartonization when picking efficiency is paramount. Sequence can also be used to pre-sort items for efficient packing on any arbitrary number, such as item weight instead of the default item volume. | [optional] 
**weight** | **Number** | weight of this single packed item. | 
**index** | **Number** | the sequence at which the item was packed. | [optional] 
**message** | **String** | any relevant information or warnings about the packing of the item. | [optional] 
**origin** | **Object** | the [x,y,z] placement point of the back-bottom corner of the item. | [optional] 


