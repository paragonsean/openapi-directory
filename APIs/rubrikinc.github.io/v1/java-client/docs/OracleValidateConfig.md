

# OracleValidateConfig


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**numChannels** | **Integer** | Number of channels used during backup validation. |  [optional] |
|**recoveryPoint** | [**OracleRecoveryPoint**](OracleRecoveryPoint.md) |  |  |
|**sgaMaxSizeInMb** | **Long** | System Global Area(SGA) size used to create the instance on the target host with unit in MB. SGA is a group of shared memory structures for one Oracle Database instance. |  [optional] |
|**targetMountPath** | **String** | The full path on the target host where the NFS share with the snapshot files will be mounted. |  [optional] |
|**targetOracleHome** | **String** | The full path on the target host for the Oracle Home which is the directory location where all Oracle software is installed. |  [optional] |
|**targetOracleHostOrRacId** | **String** | ID of the Oracle host or Oracle RAC object that is the target for the validation job. The referenced Oracle host or Oracle RAC must have the Rubrik Backup Service (RBS) installed and connected. |  |



