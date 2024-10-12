# RubrikRestApi.NasConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiCertificate** | **String** | TLS certification to validate NAS server. | [optional] 
**apiEndpoint** | **String** | API endpoint to access NAS API &#39;FLASHBLADE&#39;. | [optional] 
**apiHostname** | **String** | Hostname or IP used in the NAS API calls. | [optional] 
**apiPassword** | **String** | Password to access NAS API &#39;ISILON/NETAPP&#39;. | [optional] 
**apiToken** | **String** | API token to access NAS API &#39;FLASHBLADE&#39;. | [optional] 
**apiUsername** | **String** | Username to access NAS API &#39;ISILON/NETAPP&#39;. | [optional] 
**isIsilonChangelistEnabled** | **Boolean** | Indicates if Changelist is enabled on Isilon NAS share. When this value is &#39;true&#39;, metadata fetches during backup operations use the Isilon Changelist feature. The Changelist feature improves incremental backup performance by tracking the difference between two snapshots, reducing the metadata scanning time during a backup job. | [optional] 
**isNetAppSnapDiffEnabled** | **Boolean** | Indicates if SnapDiff is enabled on NetApp NAS share. When this value is &#39;true&#39;, metadata fetches during backup operations use the NetApp SnapDiff feature. The SnapDiff feature improves incremental backup performance by tracking the difference between two snapshots, reducing the metadata scanning time during a backup job. | [optional] 
**isShareAutoDiscoveryEnabled** | **Boolean** | Specifies whether shares on the NAS host are automatically discovered. When this value is &#39;true&#39;, Rubrik periodically (every 30 minutes by default) connects to the NAS host to discover NFS and SMB shares. | [optional] 
**vendorType** | **String** | Type of NAS vendor &#39;ISILON/NETAPP/FLASHBLADE&#39;. | 
**zoneName** | **String** | Name of the Isilon zone that data IP belongs to. | [optional] 


