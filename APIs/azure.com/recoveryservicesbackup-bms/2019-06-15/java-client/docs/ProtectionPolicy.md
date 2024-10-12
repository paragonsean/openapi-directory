

# ProtectionPolicy

Base class for backup policy. Workload-specific backup policies are derived from this class.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupManagementType** | **String** | This property will be used as the discriminator for deciding the specific types in the polymorphic chain of types. |  |
|**protectedItemsCount** | **Integer** | Number of items associated with this policy. |  [optional] |



