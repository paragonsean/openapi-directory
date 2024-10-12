

# CustomAttribute

Custom attribute values that are either filterable or non-filterable.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filterable** | **Boolean** | If the &#x60;filterable&#x60; flag is true, the custom field values may be used for custom attribute filters JobQuery.custom_attribute_filter. If false, these values may not be used for custom attribute filters. Default is false. |  [optional] |
|**keywordSearchable** | **Boolean** | If the &#x60;keyword_searchable&#x60; flag is true, the keywords in custom fields are searchable by keyword match. If false, the values are not searchable by keyword match. Default is false. |  [optional] |
|**longValues** | **List&lt;String&gt;** | Exactly one of string_values or long_values must be specified. This field is used to perform number range search. (&#x60;EQ&#x60;, &#x60;GT&#x60;, &#x60;GE&#x60;, &#x60;LE&#x60;, &#x60;LT&#x60;) over filterable &#x60;long_value&#x60;. Currently at most 1 long_values is supported. |  [optional] |
|**stringValues** | **List&lt;String&gt;** | Exactly one of string_values or long_values must be specified. This field is used to perform a string match (&#x60;CASE_SENSITIVE_MATCH&#x60; or &#x60;CASE_INSENSITIVE_MATCH&#x60;) search. For filterable &#x60;string_value&#x60;s, a maximum total number of 200 values is allowed, with each &#x60;string_value&#x60; has a byte size of no more than 500B. For unfilterable &#x60;string_values&#x60;, the maximum total byte size of unfilterable &#x60;string_values&#x60; is 50KB. Empty string isn&#39;t allowed. |  [optional] |



