

# ProtectionPolicy

The base class for a backup policy. Workload-specific backup policies are derived from this class.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupManagementType** | **String** | This property is used as the discriminator for deciding the specific types in the polymorphic chain of types. |  [optional] |
|**protectedItemsCount** | **Integer** | The number of items associated with this policy. |  [optional] |



