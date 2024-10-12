# AzureMlCommitmentPlansManagementClient.PlanUsageHistory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**planDeletionOverage** | **{String: Number}** | Overage incurred as a result of deleting a commitment plan. | [optional] 
**planMigrationOverage** | **{String: Number}** | Overage incurred as a result of migrating a commitment plan from one SKU to another. | [optional] 
**planQuantitiesAfterUsage** | **{String: Number}** | Included quantities remaining after usage against the commitment plan&#39;s associated resources was calculated. | [optional] 
**planQuantitiesBeforeUsage** | **{String: Number}** | Included quantities remaining before usage against the commitment plan&#39;s associated resources was calculated. | [optional] 
**planUsageOverage** | **{String: Number}** | Usage against the commitment plan&#39;s associated resources which was not covered by included quantities and is therefore overage. | [optional] 
**usage** | **{String: Number}** | Usage against the commitment plan&#39;s associated resources. | [optional] 
**usageDate** | **Date** | The date of usage, in ISO 8601 format. | [optional] 


