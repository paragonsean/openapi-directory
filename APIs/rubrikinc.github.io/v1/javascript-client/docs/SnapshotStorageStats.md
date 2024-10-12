# RubrikRestApi.SnapshotStorageStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**historicIngestedBytes** | **Number** | Amount of bytes actually ingested for the snapshot. This value reflects the amount of bytes ingested during snapshot capture and remains consistent across different physical representations. | 
**ingestedBytes** | **Number** | Amount of bytes inferred to be ingested to our system for the snapshot. This may change for existing logical content, as physical representation of content changes. | 
**logicalBytes** | **Number** | Amount of logical bytes the snapshot represents. | 
**physicalBytes** | **Number** | Amount of bytes physically stored for the snapshot. | 


