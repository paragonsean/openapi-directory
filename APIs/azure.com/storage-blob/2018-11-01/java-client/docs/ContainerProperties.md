

# ContainerProperties

The properties of a container.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hasImmutabilityPolicy** | **Boolean** | The hasImmutabilityPolicy public property is set to true by SRP if ImmutabilityPolicy has been created for this container. The hasImmutabilityPolicy public property is set to false by SRP if ImmutabilityPolicy has not been created for this container. |  [optional] [readonly] |
|**hasLegalHold** | **Boolean** | The hasLegalHold public property is set to true by SRP if there are at least one existing tag. The hasLegalHold public property is set to false by SRP if all existing legal hold tags are cleared out. There can be a maximum of 1000 blob containers with hasLegalHold&#x3D;true for a given account. |  [optional] [readonly] |
|**immutabilityPolicy** | [**ImmutabilityPolicyProperties**](ImmutabilityPolicyProperties.md) |  |  [optional] |
|**lastModifiedTime** | **OffsetDateTime** | Returns the date and time the container was last modified. |  [optional] [readonly] |
|**leaseDuration** | [**LeaseDurationEnum**](#LeaseDurationEnum) | Specifies whether the lease on a container is of infinite or fixed duration, only when the container is leased. |  [optional] [readonly] |
|**leaseState** | [**LeaseStateEnum**](#LeaseStateEnum) | Lease state of the container. |  [optional] [readonly] |
|**leaseStatus** | [**LeaseStatusEnum**](#LeaseStatusEnum) | The lease status of the container. |  [optional] [readonly] |
|**legalHold** | [**LegalHoldProperties**](LegalHoldProperties.md) |  |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | A name-value pair to associate with the container as metadata. |  [optional] |
|**publicAccess** | [**PublicAccessEnum**](#PublicAccessEnum) | Specifies whether data in the container may be accessed publicly and the level of access. |  [optional] |



## Enum: LeaseDurationEnum

| Name | Value |
|---- | -----|
| INFINITE | &quot;Infinite&quot; |
| FIXED | &quot;Fixed&quot; |



## Enum: LeaseStateEnum

| Name | Value |
|---- | -----|
| AVAILABLE | &quot;Available&quot; |
| LEASED | &quot;Leased&quot; |
| EXPIRED | &quot;Expired&quot; |
| BREAKING | &quot;Breaking&quot; |
| BROKEN | &quot;Broken&quot; |



## Enum: LeaseStatusEnum

| Name | Value |
|---- | -----|
| LOCKED | &quot;Locked&quot; |
| UNLOCKED | &quot;Unlocked&quot; |



## Enum: PublicAccessEnum

| Name | Value |
|---- | -----|
| CONTAINER | &quot;Container&quot; |
| BLOB | &quot;Blob&quot; |
| NONE | &quot;None&quot; |



