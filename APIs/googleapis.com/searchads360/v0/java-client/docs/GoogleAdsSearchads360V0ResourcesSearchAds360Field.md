

# GoogleAdsSearchads360V0ResourcesSearchAds360Field

A field or resource (artifact) used by SearchAds360Service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributeResources** | **List&lt;String&gt;** | Output only. The names of all resources that are selectable with the described artifact. Fields from these resources do not segment metrics when included in search queries. This field is only set for artifacts whose category is RESOURCE. |  [optional] [readonly] |
|**category** | [**CategoryEnum**](#CategoryEnum) | Output only. The category of the artifact. |  [optional] [readonly] |
|**dataType** | [**DataTypeEnum**](#DataTypeEnum) | Output only. This field determines the operators that can be used with the artifact in WHERE clauses. |  [optional] [readonly] |
|**enumValues** | **List&lt;String&gt;** | Output only. Values the artifact can assume if it is a field of type ENUM. This field is only set for artifacts of category SEGMENT or ATTRIBUTE. |  [optional] [readonly] |
|**filterable** | **Boolean** | Output only. Whether the artifact can be used in a WHERE clause in search queries. |  [optional] [readonly] |
|**isRepeated** | **Boolean** | Output only. Whether the field artifact is repeated. |  [optional] [readonly] |
|**metrics** | **List&lt;String&gt;** | Output only. This field lists the names of all metrics that are selectable with the described artifact when it is used in the FROM clause. It is only set for artifacts whose category is RESOURCE. |  [optional] [readonly] |
|**name** | **String** | Output only. The name of the artifact. |  [optional] [readonly] |
|**resourceName** | **String** | Output only. The resource name of the artifact. Artifact resource names have the form: &#x60;SearchAds360Fields/{name}&#x60; |  [optional] [readonly] |
|**segments** | **List&lt;String&gt;** | Output only. This field lists the names of all artifacts, whether a segment or another resource, that segment metrics when included in search queries and when the described artifact is used in the FROM clause. It is only set for artifacts whose category is RESOURCE. |  [optional] [readonly] |
|**selectable** | **Boolean** | Output only. Whether the artifact can be used in a SELECT clause in search queries. |  [optional] [readonly] |
|**selectableWith** | **List&lt;String&gt;** | Output only. The names of all resources, segments, and metrics that are selectable with the described artifact. |  [optional] [readonly] |
|**sortable** | **Boolean** | Output only. Whether the artifact can be used in a ORDER BY clause in search queries. |  [optional] [readonly] |
|**typeUrl** | **String** | Output only. The URL of proto describing the artifact&#39;s data type. |  [optional] [readonly] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| RESOURCE | &quot;RESOURCE&quot; |
| ATTRIBUTE | &quot;ATTRIBUTE&quot; |
| SEGMENT | &quot;SEGMENT&quot; |
| METRIC | &quot;METRIC&quot; |



## Enum: DataTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| BOOLEAN | &quot;BOOLEAN&quot; |
| DATE | &quot;DATE&quot; |
| DOUBLE | &quot;DOUBLE&quot; |
| ENUM | &quot;ENUM&quot; |
| FLOAT | &quot;FLOAT&quot; |
| INT32 | &quot;INT32&quot; |
| INT64 | &quot;INT64&quot; |
| MESSAGE | &quot;MESSAGE&quot; |
| RESOURCE_NAME | &quot;RESOURCE_NAME&quot; |
| STRING | &quot;STRING&quot; |
| UINT64 | &quot;UINT64&quot; |



