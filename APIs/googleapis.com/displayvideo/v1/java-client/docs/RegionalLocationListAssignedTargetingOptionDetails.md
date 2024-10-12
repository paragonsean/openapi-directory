

# RegionalLocationListAssignedTargetingOptionDetails

Targeting details for regional location list. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_REGIONAL_LOCATION_LIST`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**negative** | **Boolean** | Indicates if this option is being negatively targeted. |  [optional] |
|**regionalLocationListId** | **String** | Required. ID of the regional location list. Should refer to the location_list_id field of a LocationList resource whose type is &#x60;TARGETING_LOCATION_TYPE_REGIONAL&#x60;. |  [optional] |



