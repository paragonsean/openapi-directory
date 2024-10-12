# StorageManagementClient.ContainerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hasImmutabilityPolicy** | **Boolean** | The hasImmutabilityPolicy public property is set to true by SRP if ImmutabilityPolicy has been created for this container. The hasImmutabilityPolicy public property is set to false by SRP if ImmutabilityPolicy has not been created for this container. | [optional] [readonly] 
**hasLegalHold** | **Boolean** | The hasLegalHold public property is set to true by SRP if there are at least one existing tag. The hasLegalHold public property is set to false by SRP if all existing legal hold tags are cleared out. There can be a maximum of 1000 blob containers with hasLegalHold&#x3D;true for a given account. | [optional] [readonly] 
**immutabilityPolicy** | [**ImmutabilityPolicyProperties**](ImmutabilityPolicyProperties.md) |  | [optional] 
**lastModifiedTime** | **Date** | Returns the date and time the container was last modified. | [optional] [readonly] 
**leaseDuration** | **String** | Specifies whether the lease on a container is of infinite or fixed duration, only when the container is leased. | [optional] [readonly] 
**leaseState** | **String** | Lease state of the container. | [optional] [readonly] 
**leaseStatus** | **String** | The lease status of the container. | [optional] [readonly] 
**legalHold** | [**LegalHoldProperties**](LegalHoldProperties.md) |  | [optional] 
**metadata** | **{String: String}** | A name-value pair to associate with the container as metadata. | [optional] 
**publicAccess** | **String** | Specifies whether data in the container may be accessed publicly and the level of access. | [optional] 



## Enum: LeaseDurationEnum


* `Infinite` (value: `"Infinite"`)

* `Fixed` (value: `"Fixed"`)





## Enum: LeaseStateEnum


* `Available` (value: `"Available"`)

* `Leased` (value: `"Leased"`)

* `Expired` (value: `"Expired"`)

* `Breaking` (value: `"Breaking"`)

* `Broken` (value: `"Broken"`)





## Enum: LeaseStatusEnum


* `Locked` (value: `"Locked"`)

* `Unlocked` (value: `"Unlocked"`)





## Enum: PublicAccessEnum


* `Container` (value: `"Container"`)

* `Blob` (value: `"Blob"`)

* `None` (value: `"None"`)




