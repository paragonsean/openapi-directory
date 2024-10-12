

# SnapshotStorageStats


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**historicIngestedBytes** | **Long** | Amount of bytes actually ingested for the snapshot. This value reflects the amount of bytes ingested during snapshot capture and remains consistent across different physical representations. |  |
|**ingestedBytes** | **Long** | Amount of bytes inferred to be ingested to our system for the snapshot. This may change for existing logical content, as physical representation of content changes. |  |
|**logicalBytes** | **Long** | Amount of logical bytes the snapshot represents. |  |
|**physicalBytes** | **Long** | Amount of bytes physically stored for the snapshot. |  |



