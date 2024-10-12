# GoogleMyBusinessApi.FoodMenuItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**FoodMenuItemAttributes**](FoodMenuItemAttributes.md) |  | [optional] 
**labels** | [**[MenuLabel]**](MenuLabel.md) | Required. Language tagged labels for this menu item. Display names should be 140 characters or less, with descriptions 1,000 characters or less. At least one set of labels is required. | [optional] 
**options** | [**[FoodMenuItemOption]**](FoodMenuItemOption.md) | Optional. This is for an item that comes in multiple different options, and users are required to make choices. E.g. \&quot;regular\&quot; vs. \&quot;large\&quot; pizza. When options are specified, labels and attributes at item level will automatically become the first option&#39;s labels and attributes. Clients only need to specify other additional food options in this field. | [optional] 


