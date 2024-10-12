# RubrikRestApi.SapHanaDatabaseSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuredSlaDomainId** | **String** | The ID of the SLA Domain configured directly on the Rubrik object. | 
**configuredSlaDomainName** | **String** | The name of the SLA Domain configured directly on the Rubrik object. | 
**configuredSlaDomainType** | [**ConfiguredSlaType**](ConfiguredSlaType.md) |  | [optional] 
**id** | **String** | The ID of the SAP HANA database. | 
**isConfiguredSlaDomainRetentionLocked** | **Boolean** | Indicates whether the configured SLA Domain is Retention Locked. When this value is &#39;true&#39;, the configured SLA Domain is a Retention Lock SLA Domain. | [optional] 
**name** | **String** | The name of the SAP HANA database. | 
**primaryClusterId** | **String** | The ID of the cluster that manages the Rubrik object. | 
**slaLastUpdateTime** | **Date** | The UTC time when the SLA Domain was last updated. | [optional] 
**effectiveSlaDomainId** | **String** | The ID of the SLA Domain that controls the protection of the Rubrik object. | 
**effectiveSlaDomainName** | **String** | The name of the SLA Domain that controls the protection of the Rubrik object. | 
**effectiveSlaDomainPolarisManagedId** | **String** | Optional. This field contains the managed ID of of the Polaris-managed effective SLA Domain. | [optional] 
**effectiveSlaSourceObjectId** | **String** | The ID of the parent of the Rubrik object from which the SLA Domain that controls the protection of Rubrik object is inherited. | [optional] 
**effectiveSlaSourceObjectName** | **String** | The name of the parent of the Rubrik object from which the SLA Domain that controls the protection of Rubrik object is inherited. | [optional] 
**isEffectiveSlaDomainRetentionLocked** | **Boolean** | Indicates whether the effective SLA Domain is Retention Locked. When this value is &#39;true&#39;, the effective SLA domain is a Retention Lock SLA Domain. | [optional] 
**retentionSlaDomainId** | **String** | The ID of the SLA Domain whose retention policy is in use. | [optional] 
**slaAssignment** | **String** | The SLA assignment type. Direct SLA assignment means that a SLA Domain was configured directly on the Rubrik object by the user. Derived SLA assignment means that the Rubrik object inherits an SLA Domain from its parent Rubrik object. | 
**dataPathType** | [**SapHanaDataPathType**](SapHanaDataPathType.md) |  | 
**dbStatus** | **String** | Whether the database is in an ACTIVE,INACTIVE, or UNKNOWN state. | 
**dbType** | **String** | The type of SAP HANA database. Possible values are SYSTEM or TENANT. The SYSTEM database stores information about SAP HANA users and central system management. The TENANT database contains databases used by applications. | 
**isRelic** | **Boolean** | Specifies whether the SAP HANA database is accessible on the CDM cluster. | 
**logBackupIntervalInSecs** | **Number** | The log backup interval in seconds. | [optional] 
**primaryClusterUuid** | **String** | The ID of the CDM cluster that protects the SAP HANA database. | 
**protectionDate** | **Date** | The UTC timestamp for when the SAP HANA database was first protected. | [optional] 
**sapHanaSystemId** | **String** | The ID of the SAP HANA system that owns the database. | 
**sapHanaSystemName** | **String** | Name of the SAP HANA system that owns the database. | 



## Enum: SlaAssignmentEnum


* `Derived` (value: `"Derived"`)

* `Direct` (value: `"Direct"`)

* `Unassigned` (value: `"Unassigned"`)





## Enum: DbStatusEnum


* `ACTIVE` (value: `"ACTIVE"`)

* `INACTIVE` (value: `"INACTIVE"`)

* `UNKNOWN` (value: `"UNKNOWN"`)





## Enum: DbTypeEnum


* `SYSTEM` (value: `"SYSTEM"`)

* `TENANT` (value: `"TENANT"`)




