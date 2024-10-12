

# BillingResponseListResult

The response for the operation to get regional billingSpecs for a subscription.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingResources** | [**List&lt;BillingResources&gt;**](BillingResources.md) | The billing and managed disk billing resources for a region. |  [optional] |
|**vmSizeFilters** | [**List&lt;VmSizeCompatibilityFilterV2&gt;**](VmSizeCompatibilityFilterV2.md) | The virtual machine filtering mode. Effectively this can enabling or disabling the virtual machine sizes in a particular set. |  [optional] |
|**vmSizes** | **List&lt;String&gt;** | The virtual machine sizes to include or exclude. |  [optional] |



