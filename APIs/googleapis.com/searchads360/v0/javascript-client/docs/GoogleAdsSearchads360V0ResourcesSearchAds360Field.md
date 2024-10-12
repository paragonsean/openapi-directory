# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesSearchAds360Field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributeResources** | **[String]** | Output only. The names of all resources that are selectable with the described artifact. Fields from these resources do not segment metrics when included in search queries. This field is only set for artifacts whose category is RESOURCE. | [optional] [readonly] 
**category** | **String** | Output only. The category of the artifact. | [optional] [readonly] 
**dataType** | **String** | Output only. This field determines the operators that can be used with the artifact in WHERE clauses. | [optional] [readonly] 
**enumValues** | **[String]** | Output only. Values the artifact can assume if it is a field of type ENUM. This field is only set for artifacts of category SEGMENT or ATTRIBUTE. | [optional] [readonly] 
**filterable** | **Boolean** | Output only. Whether the artifact can be used in a WHERE clause in search queries. | [optional] [readonly] 
**isRepeated** | **Boolean** | Output only. Whether the field artifact is repeated. | [optional] [readonly] 
**metrics** | **[String]** | Output only. This field lists the names of all metrics that are selectable with the described artifact when it is used in the FROM clause. It is only set for artifacts whose category is RESOURCE. | [optional] [readonly] 
**name** | **String** | Output only. The name of the artifact. | [optional] [readonly] 
**resourceName** | **String** | Output only. The resource name of the artifact. Artifact resource names have the form: &#x60;SearchAds360Fields/{name}&#x60; | [optional] [readonly] 
**segments** | **[String]** | Output only. This field lists the names of all artifacts, whether a segment or another resource, that segment metrics when included in search queries and when the described artifact is used in the FROM clause. It is only set for artifacts whose category is RESOURCE. | [optional] [readonly] 
**selectable** | **Boolean** | Output only. Whether the artifact can be used in a SELECT clause in search queries. | [optional] [readonly] 
**selectableWith** | **[String]** | Output only. The names of all resources, segments, and metrics that are selectable with the described artifact. | [optional] [readonly] 
**sortable** | **Boolean** | Output only. Whether the artifact can be used in a ORDER BY clause in search queries. | [optional] [readonly] 
**typeUrl** | **String** | Output only. The URL of proto describing the artifact&#39;s data type. | [optional] [readonly] 



## Enum: CategoryEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `RESOURCE` (value: `"RESOURCE"`)

* `ATTRIBUTE` (value: `"ATTRIBUTE"`)

* `SEGMENT` (value: `"SEGMENT"`)

* `METRIC` (value: `"METRIC"`)





## Enum: DataTypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `BOOLEAN` (value: `"BOOLEAN"`)

* `DATE` (value: `"DATE"`)

* `DOUBLE` (value: `"DOUBLE"`)

* `ENUM` (value: `"ENUM"`)

* `FLOAT` (value: `"FLOAT"`)

* `INT32` (value: `"INT32"`)

* `INT64` (value: `"INT64"`)

* `MESSAGE` (value: `"MESSAGE"`)

* `RESOURCE_NAME` (value: `"RESOURCE_NAME"`)

* `STRING` (value: `"STRING"`)

* `UINT64` (value: `"UINT64"`)




