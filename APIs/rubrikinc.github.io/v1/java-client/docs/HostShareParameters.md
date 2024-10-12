

# HostShareParameters


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isIsilonChangelistEnabled** | **Boolean** | Indicates if Changelist is enabled on Isilon NAS share. When this value is &#39;true&#39;, metadata fetches during backup operations use the Isilon Changelist feature. The Changelist feature improves incremental backup performance by tracking the difference between two snapshots, reducing the metadata scanning time during a backup job. |  [optional] |
|**isNetAppSnapDiffEnabled** | **Boolean** | Indicates if SnapDiff is enabled on NetApp NAS share. When this value is &#39;true&#39;, metadata fetches during backup operations use the NetApp SnapDiff feature. The SnapDiff feature improves incremental backup performance by tracking the difference between two snapshots, reducing the metadata scanning time during a backup job. |  [optional] |
|**isOnNetAppSnapMirrorDestVolume** | **Boolean** | Indicates whether the share is on a SnapMirror destination volume on a NetApp NAS share. When this value is &#39;true&#39;, fileset backup operations pick the latest Netapp snapshot on the volume, subject to the configured label matching. During share registration, Rubrik checks with NetApp NAS to find out whether the share is on SnapMirror destination and sets this parameter. |  [optional] |



