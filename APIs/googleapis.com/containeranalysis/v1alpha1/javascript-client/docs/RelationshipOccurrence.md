# ContainerAnalysisApi.RelationshipOccurrence

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **String** | A place for the SPDX file creator to record any general comments about the relationship | [optional] 
**source** | **String** | Also referred to as SPDXRef-A The source SPDX element (file, package, etc) | [optional] 
**target** | **String** | Also referred to as SPDXRef-B The target SPDC element (file, package, etc) In cases where there are \&quot;known unknowns\&quot;, the use of the keyword NOASSERTION can be used The keywords NONE can be used to indicate that an SPDX element (package/file/snippet) has no other elements connected by some relationship to it | [optional] 
**type** | **String** | Output only. The type of relationship between the source and target SPDX elements | [optional] [readonly] 



## Enum: TypeEnum


* `RELATIONSHIP_TYPE_UNSPECIFIED` (value: `"RELATIONSHIP_TYPE_UNSPECIFIED"`)

* `DESCRIBES` (value: `"DESCRIBES"`)

* `DESCRIBED_BY` (value: `"DESCRIBED_BY"`)

* `CONTAINS` (value: `"CONTAINS"`)

* `CONTAINED_BY` (value: `"CONTAINED_BY"`)

* `DEPENDS_ON` (value: `"DEPENDS_ON"`)

* `DEPENDENCY_OF` (value: `"DEPENDENCY_OF"`)

* `DEPENDENCY_MANIFEST_OF` (value: `"DEPENDENCY_MANIFEST_OF"`)

* `BUILD_DEPENDENCY_OF` (value: `"BUILD_DEPENDENCY_OF"`)

* `DEV_DEPENDENCY_OF` (value: `"DEV_DEPENDENCY_OF"`)

* `OPTIONAL_DEPENDENCY_OF` (value: `"OPTIONAL_DEPENDENCY_OF"`)

* `PROVIDED_DEPENDENCY_OF` (value: `"PROVIDED_DEPENDENCY_OF"`)

* `TEST_DEPENDENCY_OF` (value: `"TEST_DEPENDENCY_OF"`)

* `RUNTIME_DEPENDENCY_OF` (value: `"RUNTIME_DEPENDENCY_OF"`)

* `EXAMPLE_OF` (value: `"EXAMPLE_OF"`)

* `GENERATES` (value: `"GENERATES"`)

* `GENERATED_FROM` (value: `"GENERATED_FROM"`)

* `ANCESTOR_OF` (value: `"ANCESTOR_OF"`)

* `DESCENDANT_OF` (value: `"DESCENDANT_OF"`)

* `VARIANT_OF` (value: `"VARIANT_OF"`)

* `DISTRIBUTION_ARTIFACT` (value: `"DISTRIBUTION_ARTIFACT"`)

* `PATCH_FOR` (value: `"PATCH_FOR"`)

* `PATCH_APPLIED` (value: `"PATCH_APPLIED"`)

* `COPY_OF` (value: `"COPY_OF"`)

* `FILE_ADDED` (value: `"FILE_ADDED"`)

* `FILE_DELETED` (value: `"FILE_DELETED"`)

* `FILE_MODIFIED` (value: `"FILE_MODIFIED"`)

* `EXPANDED_FROM_ARCHIVE` (value: `"EXPANDED_FROM_ARCHIVE"`)

* `DYNAMIC_LINK` (value: `"DYNAMIC_LINK"`)

* `STATIC_LINK` (value: `"STATIC_LINK"`)

* `DATA_FILE_OF` (value: `"DATA_FILE_OF"`)

* `TEST_CASE_OF` (value: `"TEST_CASE_OF"`)

* `BUILD_TOOL_OF` (value: `"BUILD_TOOL_OF"`)

* `DEV_TOOL_OF` (value: `"DEV_TOOL_OF"`)

* `TEST_OF` (value: `"TEST_OF"`)

* `TEST_TOOL_OF` (value: `"TEST_TOOL_OF"`)

* `DOCUMENTATION_OF` (value: `"DOCUMENTATION_OF"`)

* `OPTIONAL_COMPONENT_OF` (value: `"OPTIONAL_COMPONENT_OF"`)

* `METAFILE_OF` (value: `"METAFILE_OF"`)

* `PACKAGE_OF` (value: `"PACKAGE_OF"`)

* `AMENDS` (value: `"AMENDS"`)

* `PREREQUISITE_FOR` (value: `"PREREQUISITE_FOR"`)

* `HAS_PREREQUISITE` (value: `"HAS_PREREQUISITE"`)

* `OTHER` (value: `"OTHER"`)




