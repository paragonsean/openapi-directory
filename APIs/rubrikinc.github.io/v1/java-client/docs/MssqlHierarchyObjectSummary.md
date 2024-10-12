

# MssqlHierarchyObjectSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configuredSlaDomainId** | **String** | The ID of the SLA Domain configured directly on the Rubrik object. |  |
|**configuredSlaDomainName** | **String** | The name of the SLA Domain configured directly on the Rubrik object. |  |
|**configuredSlaDomainType** | **ConfiguredSlaType** |  |  [optional] |
|**id** | **String** | The ID of the Rubrik object. |  |
|**isConfiguredSlaDomainRetentionLocked** | **Boolean** | Indicates whether the configured SLA Domain is Retention Locked. When this value is &#39;true&#39;, the configured SLA Domain is a Retention Lock SLA Domain. |  [optional] |
|**name** | **String** | The name of the Rubrik object. |  |
|**primaryClusterId** | **String** | The ID of the cluster that manages the Rubrik object. |  |
|**slaLastUpdateTime** | **OffsetDateTime** | The UTC time when the SLA Domain was last updated. |  [optional] |
|**effectiveSlaDomainId** | **String** | The ID of the SLA Domain that controls the protection of the Rubrik object. |  |
|**effectiveSlaDomainName** | **String** | The name of the SLA Domain that controls the protection of the Rubrik object. |  |
|**effectiveSlaDomainPolarisManagedId** | **String** | Optional. This field contains the managed ID of of the Polaris-managed effective SLA Domain. |  [optional] |
|**effectiveSlaSourceObjectId** | **String** | The ID of the parent of the Rubrik object from which the SLA Domain that controls the protection of Rubrik object is inherited. |  [optional] |
|**effectiveSlaSourceObjectName** | **String** | The name of the parent of the Rubrik object from which the SLA Domain that controls the protection of Rubrik object is inherited. |  [optional] |
|**isEffectiveSlaDomainRetentionLocked** | **Boolean** | Indicates whether the effective SLA Domain is Retention Locked. When this value is &#39;true&#39;, the effective SLA domain is a Retention Lock SLA Domain. |  [optional] |
|**retentionSlaDomainId** | **String** | The ID of the SLA Domain whose retention policy is in use. |  [optional] |
|**slaAssignment** | [**SlaAssignmentEnum**](#SlaAssignmentEnum) | The SLA assignment type. Direct SLA assignment means that a SLA Domain was configured directly on the Rubrik object by the user. Derived SLA assignment means that the Rubrik object inherits an SLA Domain from its parent Rubrik object. |  |
|**infraPath** | [**List&lt;ManagedHierarchyObjectAncestor&gt;**](ManagedHierarchyObjectAncestor.md) |  |  [optional] |
|**isDeleted** | **Boolean** | Indicates whether the managed hierarchy object is deleted. |  |
|**isRelic** | **Boolean** | Whether this managed object is a relic (an archived snappable with unexpired snapshots). |  |
|**slaPath** | [**List&lt;ManagedHierarchyObjectAncestor&gt;**](ManagedHierarchyObjectAncestor.md) |  |  [optional] |
|**copyOnly** | **Boolean** | Boolean value that specifies whether or not to perform copy-only backups of the database. When true, database backups are copy-only backups. When false, database backups are full backups. |  [optional] |
|**logBackupFrequencyInSeconds** | **Integer** | Seconds between two log backups. A value of 0 disables log backup. |  [optional] |
|**logRetentionHours** | **Integer** | Number of hours to retain a log backup. When the value is set to -1 the Rubrik cluster retains the log backup until the database snapshots that precede the log backup have expired. |  [optional] |
|**cbtEffectiveStatus** | **MssqlHostCbtEffectiveStatusType** |  |  [optional] |
|**cbtEnabled** | **MssqlHostCbtStatusType** |  |  [optional] |
|**clusterInstanceAddress** | **String** | Property that indicates the address of the instance in a Windows Server failover cluster. This property is only set when the value of objectType is MssqlInstance, when the instance belongs to a Windows Server failover cluster, and when the address is known.  |  [optional] |
|**descendantCount** | [**MssqlHierarchyObjectDescendantCount**](MssqlHierarchyObjectDescendantCount.md) |  |  |
|**descendantSlaDomains** | [**List&lt;MssqlSlaDomainInfo&gt;**](MssqlSlaDomainInfo.md) | Lists the effective SLA Domains of this object&#39;s child SQL Server instances. This property is set when the value of objectType is Host or WindowsCluster.  |  [optional] |
|**hasInstances** | **Boolean** | A Boolean that specifies whether the object has children of type MssqlInstance. This property is only set when the value of objectType is Host or WindowsCluster.  |  [optional] |
|**hasPermissions** | **Boolean** | Boolean value that specifies whether the cluster has permission to back up the database. This property is only set when the value of objectType is MssqlDatabase. |  [optional] |
|**hostStatus** | **String** | Property that indicates the current connection status of a Windows host.This property is only set when the value of objectType is Host. |  [optional] |
|**hosts** | [**List&lt;MssqlRootProperties&gt;**](MssqlRootProperties.md) | This property is only used with SQL Server availability groups. Every object in a SQL Server availability group has the Host rootType.  |  [optional] |
|**instanceChildren** | **List&lt;String&gt;** | A list of children of type MssqlInstance. This property is only set when the value of objectType is Host or WindowsCluster.  |  [optional] |
|**instanceChildrenInfo** | [**List&lt;MssqlInstanceShortSummary&gt;**](MssqlInstanceShortSummary.md) | MssqlInstanceShortSummary list providing information about MssqlInstance children. This property is set only when the value of objectType is WindowsCluster.  |  [optional] |
|**isClustered** | **Boolean** | A Boolean that specifies whether the object is clustered. This property is only set when the value of objectType is MssqlInstance or MssqlDatabase.  |  [optional] |
|**isInAvailabilityGroup** | **Boolean** | Boolean value that specifies whether this database is part of an availability group. This property is only set when the value of objectType is MssqlDatabase. |  [optional] |
|**isLiveMount** | **Boolean** | Boolean value that specifies whether a database object is a Live Mount. Value is &#39;true&#39; when the database object is a Live Mount. This property is only set when the value of objectType is MssqlDatabase. |  [optional] |
|**isLogShippingSecondary** | **Boolean** | Boolean value that specifies whether a database object represents a secondary database. Value is &#39;true&#39; when the database object represents a secondary database in a log shipping configuration. This property is only set when the value of objectType is MssqlDatabase. |  [optional] |
|**objectType** | **MssqlHierarchyObjectType** |  |  |
|**pendingSlaDomain** | [**ManagedObjectPendingSlaInfo**](ManagedObjectPendingSlaInfo.md) |  |  [optional] |
|**replicas** | [**List&lt;MssqlDbReplica&gt;**](MssqlDbReplica.md) | A list of the replicas available for the specified database. Databases that are not in an availability group have only a single replica. This property is only set when the value of objectType is MssqlDatabase.  |  [optional] |
|**unprotectableReasons** | **List&lt;String&gt;** | A list of reasons that a SQL Server database cannot be protected by the Rubrik CDM. This property is only set when the value of objectType is MssqlDatabase. |  [optional] |



## Enum: SlaAssignmentEnum

| Name | Value |
|---- | -----|
| DERIVED | &quot;Derived&quot; |
| DIRECT | &quot;Direct&quot; |
| UNASSIGNED | &quot;Unassigned&quot; |



