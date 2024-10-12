

# LandingPage

Contains information about where a user's browser is taken after the user clicks an ad.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiserId** | **String** | Advertiser ID of this landing page. This is a required field. |  [optional] |
|**archived** | **Boolean** | Whether this landing page has been archived. |  [optional] |
|**deepLinks** | [**List&lt;DeepLink&gt;**](DeepLink.md) | Links that will direct the user to a mobile app, if installed. |  [optional] |
|**id** | **String** | ID of this landing page. This is a read-only, auto-generated field. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#landingPage\&quot;. |  [optional] |
|**name** | **String** | Name of this landing page. This is a required field. It must be less than 256 characters long. |  [optional] |
|**url** | **String** | URL of this landing page. This is a required field. |  [optional] |



