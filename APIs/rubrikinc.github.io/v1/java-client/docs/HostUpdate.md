

# HostUpdate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alias** | **String** | A user-specified string that returns this host in searches. |  [optional] |
|**compressionEnabled** | **Boolean** |  |  [optional] |
|**hdfsConfig** | [**HdfsConfig**](HdfsConfig.md) |  |  [optional] |
|**hostVfdDriverInstalled** | **Boolean** | When VFD is disabled on the specified Windows host, set this property to false to instruct the Rubrik cluster to remove the VFD driver from a specified Windows host. Before using this property, disable VFD on the specified Windows host by setting the value of HostVfdEnabled to Disabled. |  [optional] |
|**hostVfdEnabled** | **HostVfdInstallConfig** |  |  [optional] |
|**hostname** | **String** |  |  [optional] |
|**isOracleHost** | **Boolean** | A Boolean that specifies whether to discover Oracle information during host refresh. A value of &#39;true&#39; discovers Oracle information during host refresh.  |  [optional] |
|**mssqlCbtDriverInstalled** | **Boolean** | When CBT is disabled on the specified Windows host, set this property to false to instruct the Rubrik cluster to remove the CBT driver from a specified Windows host. Before using this property, disable CBT on the specified Windows host by setting the value of mssqlCbtEnabled to Disabled. |  [optional] |
|**mssqlCbtEnabled** | **MssqlCbtStatusType** |  |  [optional] |
|**nasConfig** | [**NasConfig**](NasConfig.md) |  |  [optional] |
|**oracleQueryUser** | **String** | Specifies the Oracle username for an account with query privileges. The account must have query privileges for a specified Oracle installation to enable Oracle discovery queries for that installation.  |  [optional] |
|**oracleSysDbaUser** | **String** | Specifies the Oracle username for an account with sysdba privileges. The account must have sysdba privileges for a specified Oracle installation to enable Oracle discovery queries for that installation. This field overrides the configured global sysdba user for the specified Oracle installation.  |  [optional] |



