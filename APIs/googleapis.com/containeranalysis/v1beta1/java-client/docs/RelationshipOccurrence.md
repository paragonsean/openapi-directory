

# RelationshipOccurrence

RelationshipOccurrence represents an SPDX Relationship section: https://spdx.github.io/spdx-spec/7-relationships-between-SPDX-elements/

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comment** | **String** | A place for the SPDX file creator to record any general comments about the relationship |  [optional] |
|**source** | **String** | Also referred to as SPDXRef-A The source SPDX element (file, package, etc) |  [optional] |
|**target** | **String** | Also referred to as SPDXRef-B The target SPDC element (file, package, etc) In cases where there are \&quot;known unknowns\&quot;, the use of the keyword NOASSERTION can be used The keywords NONE can be used to indicate that an SPDX element (package/file/snippet) has no other elements connected by some relationship to it |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. The type of relationship between the source and target SPDX elements |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| RELATIONSHIP_TYPE_UNSPECIFIED | &quot;RELATIONSHIP_TYPE_UNSPECIFIED&quot; |
| DESCRIBES | &quot;DESCRIBES&quot; |
| DESCRIBED_BY | &quot;DESCRIBED_BY&quot; |
| CONTAINS | &quot;CONTAINS&quot; |
| CONTAINED_BY | &quot;CONTAINED_BY&quot; |
| DEPENDS_ON | &quot;DEPENDS_ON&quot; |
| DEPENDENCY_OF | &quot;DEPENDENCY_OF&quot; |
| DEPENDENCY_MANIFEST_OF | &quot;DEPENDENCY_MANIFEST_OF&quot; |
| BUILD_DEPENDENCY_OF | &quot;BUILD_DEPENDENCY_OF&quot; |
| DEV_DEPENDENCY_OF | &quot;DEV_DEPENDENCY_OF&quot; |
| OPTIONAL_DEPENDENCY_OF | &quot;OPTIONAL_DEPENDENCY_OF&quot; |
| PROVIDED_DEPENDENCY_OF | &quot;PROVIDED_DEPENDENCY_OF&quot; |
| TEST_DEPENDENCY_OF | &quot;TEST_DEPENDENCY_OF&quot; |
| RUNTIME_DEPENDENCY_OF | &quot;RUNTIME_DEPENDENCY_OF&quot; |
| EXAMPLE_OF | &quot;EXAMPLE_OF&quot; |
| GENERATES | &quot;GENERATES&quot; |
| GENERATED_FROM | &quot;GENERATED_FROM&quot; |
| ANCESTOR_OF | &quot;ANCESTOR_OF&quot; |
| DESCENDANT_OF | &quot;DESCENDANT_OF&quot; |
| VARIANT_OF | &quot;VARIANT_OF&quot; |
| DISTRIBUTION_ARTIFACT | &quot;DISTRIBUTION_ARTIFACT&quot; |
| PATCH_FOR | &quot;PATCH_FOR&quot; |
| PATCH_APPLIED | &quot;PATCH_APPLIED&quot; |
| COPY_OF | &quot;COPY_OF&quot; |
| FILE_ADDED | &quot;FILE_ADDED&quot; |
| FILE_DELETED | &quot;FILE_DELETED&quot; |
| FILE_MODIFIED | &quot;FILE_MODIFIED&quot; |
| EXPANDED_FROM_ARCHIVE | &quot;EXPANDED_FROM_ARCHIVE&quot; |
| DYNAMIC_LINK | &quot;DYNAMIC_LINK&quot; |
| STATIC_LINK | &quot;STATIC_LINK&quot; |
| DATA_FILE_OF | &quot;DATA_FILE_OF&quot; |
| TEST_CASE_OF | &quot;TEST_CASE_OF&quot; |
| BUILD_TOOL_OF | &quot;BUILD_TOOL_OF&quot; |
| DEV_TOOL_OF | &quot;DEV_TOOL_OF&quot; |
| TEST_OF | &quot;TEST_OF&quot; |
| TEST_TOOL_OF | &quot;TEST_TOOL_OF&quot; |
| DOCUMENTATION_OF | &quot;DOCUMENTATION_OF&quot; |
| OPTIONAL_COMPONENT_OF | &quot;OPTIONAL_COMPONENT_OF&quot; |
| METAFILE_OF | &quot;METAFILE_OF&quot; |
| PACKAGE_OF | &quot;PACKAGE_OF&quot; |
| AMENDS | &quot;AMENDS&quot; |
| PREREQUISITE_FOR | &quot;PREREQUISITE_FOR&quot; |
| HAS_PREREQUISITE | &quot;HAS_PREREQUISITE&quot; |
| OTHER | &quot;OTHER&quot; |



