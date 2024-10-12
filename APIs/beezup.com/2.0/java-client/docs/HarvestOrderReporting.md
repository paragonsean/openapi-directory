

# HarvestOrderReporting

The reporting related to a harvest order operation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**beezUPForcedStatus** | **String** | The marketplace order status forced by BeezUP during the order change oepration. This could happend when there is no status on the marketplace side. |  [optional] |
|**beezUPStatus** | **String** | BeezUP order status. Unified for all marketplaces. |  [optional] |
|**creationUtcDate** | **OffsetDateTime** | The creation UTC date of the execution |  [optional] |
|**errorMessage** | **String** | The warning message during the execution |  [optional] |
|**executionUUID** | **UUID** | The execution identifier |  [optional] |
|**lastUpdateUtcDate** | **OffsetDateTime** | The last update UTC date of the execution |  [optional] |
|**marketplaceStatus** | **String** | The order marketplace status |  [optional] |
|**processingStatus** | **String** | The processing status of the execution |  [optional] |
|**warningMessage** | **String** | The warning message during the execution |  [optional] |



