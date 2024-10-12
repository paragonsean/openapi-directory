

# TimePartitioning


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expirationMs** | **String** | Optional. Number of milliseconds for which to keep the storage for a partition. A wrapper is used here because 0 is an invalid value. |  [optional] |
|**field** | **String** | Optional. If not set, the table is partitioned by pseudo column &#39;_PARTITIONTIME&#39;; if set, the table is partitioned by this field. The field must be a top-level TIMESTAMP or DATE field. Its mode must be NULLABLE or REQUIRED. A wrapper is used here because an empty string is an invalid value. |  [optional] |
|**requirePartitionFilter** | **Boolean** | If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified. This field is deprecated; please set the field with the same name on the table itself instead. This field needs a wrapper because we want to output the default value, false, if the user explicitly set it. |  [optional] |
|**type** | **String** | Required. The supported types are DAY, HOUR, MONTH, and YEAR, which will generate one partition per day, hour, month, and year, respectively. |  [optional] |



