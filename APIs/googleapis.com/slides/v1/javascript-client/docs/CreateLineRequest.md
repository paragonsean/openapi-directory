# GoogleSlidesApi.CreateLineRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | The category of the line to be created. The exact line type created is determined based on the category and how it&#39;s routed to connect to other page elements. If you specify both a &#x60;category&#x60; and a &#x60;line_category&#x60;, the &#x60;category&#x60; takes precedence. If you do not specify a value for &#x60;category&#x60;, but specify a value for &#x60;line_category&#x60;, then the specified &#x60;line_category&#x60; value is used. If you do not specify either, then STRAIGHT is used. | [optional] 
**elementProperties** | [**PageElementProperties**](PageElementProperties.md) |  | [optional] 
**lineCategory** | **String** | The category of the line to be created. *Deprecated*: use &#x60;category&#x60; instead. The exact line type created is determined based on the category and how it&#39;s routed to connect to other page elements. If you specify both a &#x60;category&#x60; and a &#x60;line_category&#x60;, the &#x60;category&#x60; takes precedence. | [optional] 
**objectId** | **String** | A user-supplied object ID. If you specify an ID, it must be unique among all pages and page elements in the presentation. The ID must start with an alphanumeric character or an underscore (matches regex &#x60;[a-zA-Z0-9_]&#x60;); remaining characters may include those as well as a hyphen or colon (matches regex &#x60;[a-zA-Z0-9_-:]&#x60;). The length of the ID must not be less than 5 or greater than 50. If you don&#39;t specify an ID, a unique one is generated. | [optional] 



## Enum: CategoryEnum


* `LINE_CATEGORY_UNSPECIFIED` (value: `"LINE_CATEGORY_UNSPECIFIED"`)

* `STRAIGHT` (value: `"STRAIGHT"`)

* `BENT` (value: `"BENT"`)

* `CURVED` (value: `"CURVED"`)





## Enum: LineCategoryEnum


* `STRAIGHT` (value: `"STRAIGHT"`)

* `BENT` (value: `"BENT"`)

* `CURVED` (value: `"CURVED"`)




