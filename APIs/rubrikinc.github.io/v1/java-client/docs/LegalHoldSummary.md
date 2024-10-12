

# LegalHoldSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**objectId** | **String** |  |  |
|**objectName** | **String** |  |  |
|**objectType** | **String** |  |  |
|**expectedExpirationDateWithoutLegalHold** | **OffsetDateTime** | Date at which the snapshot will expire if the legal hold is dissolved.  |  [optional] |
|**isCustomRetentionApplied** | **Boolean** | A Boolean value that indicates whether custom retention is applied to the specified snapshot. Value is true when custom retention is applied to the snapshot.  |  |
|**isOnDemandSnapshot** | **Boolean** | A Boolean that specifies whether a snapshot is an On Demand snapshot. When this value is &#39;true,&#39; the snapshot is an On Demand snapshot. |  |
|**locationsPresent** | **List&lt;String&gt;** | Current locations of the snapshot. |  |
|**placeOnHoldTime** | **OffsetDateTime** | Time at which the snapshot was put on hold. |  |
|**snapshotId** | **String** |  |  |
|**snapshotTime** | **OffsetDateTime** | Time at which the snapshot was taken. |  |



