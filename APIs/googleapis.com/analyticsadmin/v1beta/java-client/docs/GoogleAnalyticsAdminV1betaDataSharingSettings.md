

# GoogleAnalyticsAdminV1betaDataSharingSettings

A resource message representing data sharing settings of a Google Analytics account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Output only. Resource name. Format: accounts/{account}/dataSharingSettings Example: \&quot;accounts/1000/dataSharingSettings\&quot; |  [optional] [readonly] |
|**sharingWithGoogleAnySalesEnabled** | **Boolean** | Allows any of Google sales to access the data in order to suggest configuration changes to improve results. |  [optional] |
|**sharingWithGoogleAssignedSalesEnabled** | **Boolean** | Allows Google sales teams that are assigned to the customer to access the data in order to suggest configuration changes to improve results. Sales team restrictions still apply when enabled. |  [optional] |
|**sharingWithGoogleProductsEnabled** | **Boolean** | Allows Google to use the data to improve other Google products or services. |  [optional] |
|**sharingWithGoogleSupportEnabled** | **Boolean** | Allows Google support to access the data in order to help troubleshoot issues. |  [optional] |
|**sharingWithOthersEnabled** | **Boolean** | Allows Google to share the data anonymously in aggregate form with others. |  [optional] |



