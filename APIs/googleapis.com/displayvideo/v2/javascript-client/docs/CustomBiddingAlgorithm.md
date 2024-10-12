# DisplayVideo360Api.CustomBiddingAlgorithm

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiserId** | **String** | Immutable. The unique ID of the advertiser that owns the custom bidding algorithm. | [optional] 
**customBiddingAlgorithmId** | **String** | Output only. The unique ID of the custom bidding algorithm. Assigned by the system. | [optional] [readonly] 
**customBiddingAlgorithmType** | **String** | Required. Immutable. The type of custom bidding algorithm. | [optional] 
**displayName** | **String** | Required. The display name of the custom bidding algorithm. Must be UTF-8 encoded with a maximum size of 240 bytes. | [optional] 
**entityStatus** | **String** | Controls whether or not the custom bidding algorithm can be used as a bidding strategy. Accepted values are: * &#x60;ENTITY_STATUS_ACTIVE&#x60; * &#x60;ENTITY_STATUS_ARCHIVED&#x60; | [optional] 
**modelDetails** | [**[CustomBiddingModelDetails]**](CustomBiddingModelDetails.md) | Output only. The details of custom bidding models for each advertiser who has access. This field may only include the details of the queried advertiser if the algorithm [&#x60;owner&#x60;](/display-video/api/reference/rest/v1/customBiddingAlgorithms#CustomBiddingAlgorithm.FIELDS.oneof_owner) is a partner and is being retrieved using an advertiser [&#x60;accessor&#x60;](/display-video/api/reference/rest/v1/customBiddingAlgorithms/list#body.QUERY_PARAMETERS.oneof_accessor). | [optional] [readonly] 
**name** | **String** | Output only. The resource name of the custom bidding algorithm. | [optional] [readonly] 
**partnerId** | **String** | Immutable. The unique ID of the partner that owns the custom bidding algorithm. | [optional] 
**sharedAdvertiserIds** | **[String]** | The IDs of the advertisers who have access to this algorithm. If advertiser_id is set, this field will only consist of that value. This field will not be set if the algorithm [&#x60;owner&#x60;](/display-video/api/reference/rest/v1/customBiddingAlgorithms#CustomBiddingAlgorithm.FIELDS.oneof_owner) is a partner and is being retrieved using an advertiser [&#x60;accessor&#x60;](/display-video/api/reference/rest/v1/customBiddingAlgorithms/list#body.QUERY_PARAMETERS.oneof_accessor). | [optional] 



## Enum: CustomBiddingAlgorithmTypeEnum


* `CUSTOM_BIDDING_ALGORITHM_TYPE_UNSPECIFIED` (value: `"CUSTOM_BIDDING_ALGORITHM_TYPE_UNSPECIFIED"`)

* `SCRIPT_BASED` (value: `"SCRIPT_BASED"`)

* `ADS_DATA_HUB_BASED` (value: `"ADS_DATA_HUB_BASED"`)

* `GOAL_BUILDER_BASED` (value: `"GOAL_BUILDER_BASED"`)





## Enum: EntityStatusEnum


* `UNSPECIFIED` (value: `"ENTITY_STATUS_UNSPECIFIED"`)

* `ACTIVE` (value: `"ENTITY_STATUS_ACTIVE"`)

* `ARCHIVED` (value: `"ENTITY_STATUS_ARCHIVED"`)

* `DRAFT` (value: `"ENTITY_STATUS_DRAFT"`)

* `PAUSED` (value: `"ENTITY_STATUS_PAUSED"`)

* `SCHEDULED_FOR_DELETION` (value: `"ENTITY_STATUS_SCHEDULED_FOR_DELETION"`)




