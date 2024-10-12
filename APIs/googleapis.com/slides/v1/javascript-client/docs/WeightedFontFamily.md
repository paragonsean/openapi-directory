# GoogleSlidesApi.WeightedFontFamily

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fontFamily** | **String** | The font family of the text. The font family can be any font from the Font menu in Slides or from [Google Fonts] (https://fonts.google.com/). If the font name is unrecognized, the text is rendered in &#x60;Arial&#x60;. | [optional] 
**weight** | **Number** | The rendered weight of the text. This field can have any value that is a multiple of &#x60;100&#x60; between &#x60;100&#x60; and &#x60;900&#x60;, inclusive. This range corresponds to the numerical values described in the CSS 2.1 Specification, [section 15.6](https://www.w3.org/TR/CSS21/fonts.html#font-boldness), with non-numerical values disallowed. Weights greater than or equal to &#x60;700&#x60; are considered bold, and weights less than &#x60;700&#x60;are not bold. The default value is &#x60;400&#x60; (\&quot;normal\&quot;). | [optional] 


