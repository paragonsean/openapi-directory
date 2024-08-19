

# Metadata

Additional non-user-editable information about the location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**canDelete** | **Boolean** | Output only. Indicates whether the location can be deleted using the API. |  [optional] [readonly] |
|**canHaveBusinessCalls** | **Boolean** | Output only. Indicates if the listing is eligible for business calls. |  [optional] [readonly] |
|**canHaveFoodMenus** | **Boolean** | Output only. Indicates if the listing is eligible for food menu. |  [optional] [readonly] |
|**canModifyServiceList** | **Boolean** | Output only. Indicates if the listing can modify the service list. |  [optional] [readonly] |
|**canOperateHealthData** | **Boolean** | Output only. Indicates whether the location can operate on Health data. |  [optional] [readonly] |
|**canOperateLocalPost** | **Boolean** | Output only. Indicates if the listing can manage local posts. |  [optional] [readonly] |
|**canOperateLodgingData** | **Boolean** | Output only. Indicates whether the location can operate on Lodging data. |  [optional] [readonly] |
|**duplicateLocation** | **String** | Output only. The location resource that this location duplicates. |  [optional] [readonly] |
|**hasGoogleUpdated** | **Boolean** | Output only. Indicates whether the place ID associated with this location has updates that need to be updated or rejected by the client. If this boolean is set, you should call the &#x60;getGoogleUpdated&#x60; method to lookup information that&#39;s needs to be verified. |  [optional] [readonly] |
|**hasPendingEdits** | **Boolean** | Output only. Indicates whether any of this Location&#39;s properties are in the edit pending state. |  [optional] [readonly] |
|**hasVoiceOfMerchant** | **Boolean** | Output only. Indicates if the listing has Voice of Merchant. If this boolean is false, you should call the locations.getVoiceOfMerchantState API to get details as to why they do not have Voice of Merchant. |  [optional] [readonly] |
|**mapsUri** | **String** | Output only. A link to the location on Maps. |  [optional] [readonly] |
|**newReviewUri** | **String** | Output only. A link to the page on Google Search where a customer can leave a review for the location. |  [optional] [readonly] |
|**placeId** | **String** | Output only. If this locationappears on Google Maps, this field is populated with the place ID for the location. This ID can be used in various Places APIs. This field can be set during Create calls, but not for Update. |  [optional] [readonly] |



