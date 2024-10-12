

# RegionalBasePlanConfig

Configuration for a base plan specific to a region.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**newSubscriberAvailability** | **Boolean** | Whether the base plan in the specified region is available for new subscribers. Existing subscribers will not have their subscription canceled if this value is set to false. If not specified, this will default to false. |  [optional] |
|**price** | [**Money**](Money.md) |  |  [optional] |
|**regionCode** | **String** | Required. Region code this configuration applies to, as defined by ISO 3166-2, e.g. \&quot;US\&quot;. |  [optional] |



