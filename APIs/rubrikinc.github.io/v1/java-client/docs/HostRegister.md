

# HostRegister


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alias** | **String** | A user-specified string that returns this host in searches. |  [optional] |
|**hasAgent** | **Boolean** |  |  [optional] |
|**hdfsConfig** | [**HdfsConfig**](HdfsConfig.md) |  |  [optional] |
|**hostname** | **String** |  |  |
|**isOracleHost** | **Boolean** | A Boolean that specifies whether to discover Oracle information at registration. A value of &#39;true&#39; discovers Oracle information at registration.  |  [optional] |
|**nasConfig** | [**NasConfig**](NasConfig.md) |  |  [optional] |
|**oracleQueryUser** | **String** | Specifies the Oracle username for an account with query privileges. The account must have query privileges for a specified Oracle installation to enable Oracle discovery queries for that installation.  |  [optional] |
|**oracleSysDbaUser** | **String** | Specifies the Oracle username for an account with sysdba privileges. The account must have sysdba privileges for a specified Oracle installation to enable Oracle discovery queries for that installation. This field overrides the configured global sysdba user for the specified Oracle installation. |  [optional] |
|**organizationId** | **String** | The ID of the organization to which the host is assigned. |  [optional] |



