

# Site

Contains properties of a site.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Account ID of this site. This is a read-only field that can be left blank. |  [optional] |
|**approved** | **Boolean** | Whether this site is approved. |  [optional] |
|**directorySiteId** | **String** | Directory site associated with this site. This is a required field that is read-only after insertion. |  [optional] |
|**directorySiteIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**id** | **String** | ID of this site. This is a read-only, auto-generated field. |  [optional] |
|**idDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**keyName** | **String** | Key name of this site. This is a read-only, auto-generated field. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#site\&quot;. |  [optional] |
|**name** | **String** | Name of this site.This is a required field. Must be less than 128 characters long. If this site is under a subaccount, the name must be unique among sites of the same subaccount. Otherwise, this site is a top-level site, and the name must be unique among top-level sites of the same account. |  [optional] |
|**siteContacts** | [**List&lt;SiteContact&gt;**](SiteContact.md) | Site contacts. |  [optional] |
|**siteSettings** | [**SiteSettings**](SiteSettings.md) |  |  [optional] |
|**subaccountId** | **String** | Subaccount ID of this site. This is a read-only field that can be left blank. |  [optional] |
|**videoSettings** | [**SiteVideoSettings**](SiteVideoSettings.md) |  |  [optional] |



