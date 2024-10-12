# CloudTalentSolutionApi.HistogramFacets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compensationHistogramFacets** | [**[CompensationHistogramRequest]**](CompensationHistogramRequest.md) | Optional. Specifies compensation field-based histogram requests. Duplicate values of CompensationHistogramRequest.type are not allowed. | [optional] 
**customAttributeHistogramFacets** | [**[CustomAttributeHistogramRequest]**](CustomAttributeHistogramRequest.md) | Optional. Specifies the custom attributes histogram requests. Duplicate values of CustomAttributeHistogramRequest.key are not allowed. | [optional] 
**simpleHistogramFacets** | **[String]** | Optional. Specifies the simple type of histogram facets, for example, &#x60;COMPANY_SIZE&#x60;, &#x60;EMPLOYMENT_TYPE&#x60; etc. | [optional] 



## Enum: [SimpleHistogramFacetsEnum]


* `SEARCH_TYPE_UNSPECIFIED` (value: `"SEARCH_TYPE_UNSPECIFIED"`)

* `COMPANY_ID` (value: `"COMPANY_ID"`)

* `EMPLOYMENT_TYPE` (value: `"EMPLOYMENT_TYPE"`)

* `COMPANY_SIZE` (value: `"COMPANY_SIZE"`)

* `DATE_PUBLISHED` (value: `"DATE_PUBLISHED"`)

* `EDUCATION_LEVEL` (value: `"EDUCATION_LEVEL"`)

* `EXPERIENCE_LEVEL` (value: `"EXPERIENCE_LEVEL"`)

* `ADMIN_1` (value: `"ADMIN_1"`)

* `COUNTRY` (value: `"COUNTRY"`)

* `CITY` (value: `"CITY"`)

* `LOCALE` (value: `"LOCALE"`)

* `LANGUAGE` (value: `"LANGUAGE"`)

* `CATEGORY` (value: `"CATEGORY"`)

* `CITY_COORDINATE` (value: `"CITY_COORDINATE"`)

* `ADMIN_1_COUNTRY` (value: `"ADMIN_1_COUNTRY"`)

* `COMPANY_DISPLAY_NAME` (value: `"COMPANY_DISPLAY_NAME"`)

* `BASE_COMPENSATION_UNIT` (value: `"BASE_COMPENSATION_UNIT"`)




