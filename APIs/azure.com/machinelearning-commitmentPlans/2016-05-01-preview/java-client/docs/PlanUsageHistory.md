

# PlanUsageHistory

Represents historical information about usage of the Azure resources associated with a commitment plan.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**planDeletionOverage** | **Map&lt;String, Double&gt;** | Overage incurred as a result of deleting a commitment plan. |  [optional] |
|**planMigrationOverage** | **Map&lt;String, Double&gt;** | Overage incurred as a result of migrating a commitment plan from one SKU to another. |  [optional] |
|**planQuantitiesAfterUsage** | **Map&lt;String, Double&gt;** | Included quantities remaining after usage against the commitment plan&#39;s associated resources was calculated. |  [optional] |
|**planQuantitiesBeforeUsage** | **Map&lt;String, Double&gt;** | Included quantities remaining before usage against the commitment plan&#39;s associated resources was calculated. |  [optional] |
|**planUsageOverage** | **Map&lt;String, Double&gt;** | Usage against the commitment plan&#39;s associated resources which was not covered by included quantities and is therefore overage. |  [optional] |
|**usage** | **Map&lt;String, Double&gt;** | Usage against the commitment plan&#39;s associated resources. |  [optional] |
|**usageDate** | **OffsetDateTime** | The date of usage, in ISO 8601 format. |  [optional] |



