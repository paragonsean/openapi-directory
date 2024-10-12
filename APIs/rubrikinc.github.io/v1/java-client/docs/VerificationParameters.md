

# VerificationParameters


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**locationIdOpt** | **String** | Snapshot stored in the provided data location id will be verified. If not provided, we will use Rubrik cluster ID. Currently it only verifies Snapshot present Rubrik cluster.  |  [optional] |
|**objectId** | **String** | ID assigned to the object. This objectId will be used to fetch the associated object.  |  |
|**shouldVerifyAfterOpt** | **OffsetDateTime** | The backup should be verified exactly once after the given timestamp. The date-time string should be in ISO8601 format, such as \&quot;2016-01-01T01:23:45.678\&quot;. If not provided, it will default to \&quot;1970-01-01T00:00:00.000\&quot;.  |  [optional] |
|**snapshotIdsOpt** | **List&lt;String&gt;** | ID assigned to a snapshot. This snapshotId will be used to fetch the associated snapshot. The scheduled job will verify this snapshot.  |  [optional] |



