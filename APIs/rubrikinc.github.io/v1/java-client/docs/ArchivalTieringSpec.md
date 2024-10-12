

# ArchivalTieringSpec


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**coldStorageClass** | **CloudStorageColdTier** |  |  [optional] |
|**isInstantTieringEnabled** | **Boolean** | A Boolean value that determines whether to immediately tier uploaded snapshots to cold storage. When this value is &#39;true,&#39; uploaded snapshots are immediately tiered to cold storage. When this value is &#39;false,&#39; snapshots are marked as eligible for tiering to cold storage after their time on the archival location exceeds the configured minimum accessible duration.  |  |
|**minAccessibleDurationInSeconds** | **Long** | Specifies an interval in seconds. Uploaded snapshots are accessible for instant recovery for the duration of the specified interval. This value is ignored when Instant Tiering is enabled.  |  [optional] |
|**shouldTierExistingSnapshots** | **Boolean** | Indicates if existing snapshots for all objects protected by the SLA should be tiered. If not specified, this defaults to false. Only the snapshots that exist in the archival location associated with the SLA will be tiered.  |  [optional] |



