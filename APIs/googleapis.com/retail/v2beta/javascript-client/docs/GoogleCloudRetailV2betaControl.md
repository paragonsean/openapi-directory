# VertexAiSearchForRetailApi.GoogleCloudRetailV2betaControl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associatedServingConfigIds** | **[String]** | Output only. List of serving config ids that are associated with this control in the same Catalog. Note the association is managed via the ServingConfig, this is an output only denormalized view. | [optional] [readonly] 
**displayName** | **String** | Required. The human readable control display name. Used in Retail UI. This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is thrown. | [optional] 
**facetSpec** | [**GoogleCloudRetailV2betaSearchRequestFacetSpec**](GoogleCloudRetailV2betaSearchRequestFacetSpec.md) |  | [optional] 
**name** | **String** | Immutable. Fully qualified name &#x60;projects/_*_/locations/global/catalogs/_*_/controls/_*&#x60; | [optional] 
**rule** | [**GoogleCloudRetailV2betaRule**](GoogleCloudRetailV2betaRule.md) |  | [optional] 
**searchSolutionUseCase** | **[String]** | Specifies the use case for the control. Affects what condition fields can be set. Only settable by search controls. Will default to SEARCH_SOLUTION_USE_CASE_SEARCH if not specified. Currently only allow one search_solution_use_case per control. | [optional] 
**solutionTypes** | **[String]** | Required. Immutable. The solution types that the control is used for. Currently we support setting only one type of solution at creation time. Only &#x60;SOLUTION_TYPE_SEARCH&#x60; value is supported at the moment. If no solution type is provided at creation time, will default to SOLUTION_TYPE_SEARCH. | [optional] 



## Enum: [SearchSolutionUseCaseEnum]


* `UNSPECIFIED` (value: `"SEARCH_SOLUTION_USE_CASE_UNSPECIFIED"`)

* `SEARCH` (value: `"SEARCH_SOLUTION_USE_CASE_SEARCH"`)

* `BROWSE` (value: `"SEARCH_SOLUTION_USE_CASE_BROWSE"`)





## Enum: [SolutionTypesEnum]


* `UNSPECIFIED` (value: `"SOLUTION_TYPE_UNSPECIFIED"`)

* `RECOMMENDATION` (value: `"SOLUTION_TYPE_RECOMMENDATION"`)

* `SEARCH` (value: `"SOLUTION_TYPE_SEARCH"`)




