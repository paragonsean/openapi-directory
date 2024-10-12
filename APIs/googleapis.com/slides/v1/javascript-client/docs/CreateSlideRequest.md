# GoogleSlidesApi.CreateSlideRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**insertionIndex** | **Number** | The optional zero-based index indicating where to insert the slides. If you don&#39;t specify an index, the slide is created at the end. | [optional] 
**objectId** | **String** | A user-supplied object ID. If you specify an ID, it must be unique among all pages and page elements in the presentation. The ID must start with an alphanumeric character or an underscore (matches regex &#x60;[a-zA-Z0-9_]&#x60;); remaining characters may include those as well as a hyphen or colon (matches regex &#x60;[a-zA-Z0-9_-:]&#x60;). The ID length must be between 5 and 50 characters, inclusive. If you don&#39;t specify an ID, a unique one is generated. | [optional] 
**placeholderIdMappings** | [**[LayoutPlaceholderIdMapping]**](LayoutPlaceholderIdMapping.md) | An optional list of object ID mappings from the placeholder(s) on the layout to the placeholders that are created on the slide from the specified layout. Can only be used when &#x60;slide_layout_reference&#x60; is specified. | [optional] 
**slideLayoutReference** | [**LayoutReference**](LayoutReference.md) |  | [optional] 


