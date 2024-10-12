

# BulkEditSitesRequest

Request message for SiteService.BulkEditSites.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiserId** | **String** | The ID of the advertiser that owns the parent channel. |  [optional] |
|**createdSites** | [**List&lt;Site&gt;**](Site.md) | The sites to create in batch, specified as a list of Sites. |  [optional] |
|**deletedSites** | **List&lt;String&gt;** | The sites to delete in batch, specified as a list of site url_or_app_ids. |  [optional] |
|**partnerId** | **String** | The ID of the partner that owns the parent channel. |  [optional] |



