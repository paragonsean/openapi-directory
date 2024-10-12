# PlacesApiNew.GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionFormattableText

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matches** | [**[GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStringRange]**](GoogleMapsPlacesV1AutocompletePlacesResponseSuggestionStringRange.md) | A list of string ranges identifying where the input request matched in &#x60;text&#x60;. The ranges can be used to format specific parts of &#x60;text&#x60;. The substrings may not be exact matches of &#x60;input&#x60; if the matching was determined by criteria other than string matching (for example, spell corrections or transliterations). These values are Unicode character offsets of &#x60;text&#x60;. The ranges are guaranteed to be ordered in increasing offset values. | [optional] 
**text** | **String** | Text that may be used as is or formatted with &#x60;matches&#x60;. | [optional] 


