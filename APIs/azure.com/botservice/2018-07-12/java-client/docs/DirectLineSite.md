

# DirectLineSite

A site for the Direct Line channel

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isEnabled** | **Boolean** | Whether this site is enabled for DirectLine channel. |  |
|**isSecureSiteEnabled** | **Boolean** | Whether this site is enabled for authentication with Bot Framework. |  [optional] |
|**isV1Enabled** | **Boolean** | Whether this site is enabled for Bot Framework V1 protocol. |  |
|**isV3Enabled** | **Boolean** | Whether this site is enabled for Bot Framework V1 protocol. |  |
|**key** | **String** | Primary key. Value only returned through POST to the action Channel List API, otherwise empty. |  [optional] [readonly] |
|**key2** | **String** | Secondary key. Value only returned through POST to the action Channel List API, otherwise empty. |  [optional] [readonly] |
|**siteId** | **String** | Site Id |  [optional] [readonly] |
|**siteName** | **String** | Site name |  |
|**trustedOrigins** | **List&lt;String&gt;** | List of Trusted Origin URLs for this site. This field is applicable only if isSecureSiteEnabled is True. |  [optional] |



