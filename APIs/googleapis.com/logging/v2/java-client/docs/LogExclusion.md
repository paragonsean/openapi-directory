

# LogExclusion

Specifies a set of log entries that are filtered out by a sink. If your Google Cloud resource receives a large volume of log entries, you can use exclusions to reduce your chargeable logs. Note that exclusions on organization-level and folder-level sinks don't apply to child resources. Note also that you cannot modify the _Required sink or exclude logs from it.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The creation timestamp of the exclusion.This field may not be present for older exclusions. |  [optional] [readonly] |
|**description** | **String** | Optional. A description of this exclusion. |  [optional] |
|**disabled** | **Boolean** | Optional. If set to True, then this exclusion is disabled and it does not exclude any log entries. You can update an exclusion to change the value of this field. |  [optional] |
|**filter** | **String** | Required. An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced-queries) that matches the log entries to be excluded. By using the sample function (https://cloud.google.com/logging/docs/view/advanced-queries#sample), you can exclude less than 100% of the matching log entries.For example, the following query matches 99% of low-severity log entries from Google Cloud Storage buckets:resource.type&#x3D;gcs_bucket severity&lt;ERROR sample(insertId, 0.99) |  [optional] |
|**name** | **String** | Output only. A client-assigned identifier, such as \&quot;load-balancer-exclusion\&quot;. Identifiers are limited to 100 characters and can include only letters, digits, underscores, hyphens, and periods. First character has to be alphanumeric. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The last update timestamp of the exclusion.This field may not be present for older exclusions. |  [optional] [readonly] |



