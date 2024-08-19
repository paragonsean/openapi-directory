

# GoogleAnalyticsAdminV1alphaSetAutomatedGa4ConfigurationOptOutRequest

Request for setting the opt out status for the automated GA4 setup process.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**optOut** | **Boolean** | The status to set. |  [optional] |
|**property** | **String** | Required. The UA property to set the opt out status. Note this request uses the internal property ID, not the tracking ID of the form UA-XXXXXX-YY. Format: properties/{internalWebPropertyId} Example: properties/1234 |  [optional] |



