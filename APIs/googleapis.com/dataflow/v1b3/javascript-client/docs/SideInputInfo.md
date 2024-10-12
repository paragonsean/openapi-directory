# DataflowApi.SideInputInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **{String: Object}** | How to interpret the source element(s) as a side input value. | [optional] 
**sources** | [**[Source]**](Source.md) | The source(s) to read element(s) from to get the value of this side input. If more than one source, then the elements are taken from the sources, in the specified order if order matters. At least one source is required. | [optional] 
**tag** | **String** | The id of the tag the user code will access this side input by; this should correspond to the tag of some MultiOutputInfo. | [optional] 


