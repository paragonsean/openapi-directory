

# LogAnalyticsQueryPackQueryProperties

Properties that define an Log Analytics QueryPack-Query resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**author** | **String** | Object Id of user creating the query. |  [optional] [readonly] |
|**body** | **String** | Body of the query. |  |
|**categories** | **List&lt;String&gt;** | Categories associated with the query. |  [optional] |
|**description** | **String** | Description of the query. |  [optional] |
|**displayName** | **String** | Unique display name for your query within the Query Pack. |  |
|**labels** | **List&lt;String&gt;** | Labels associated with the query. |  [optional] |
|**linkedResourceId** | **String** | Resource id associated with the query. |  [optional] |
|**queryId** | **String** | The unique ID of your application. This field cannot be changed. |  [optional] [readonly] |
|**resourceTypes** | **List&lt;String&gt;** | Resource Types associated with the query. |  [optional] |
|**timeCreated** | **OffsetDateTime** | Creation Date for the Log Analytics Query, in ISO 8601 format. |  [optional] [readonly] |
|**timeModified** | **OffsetDateTime** | Last modified date of the Log Analytics Query, in ISO 8601 format. |  [optional] [readonly] |



