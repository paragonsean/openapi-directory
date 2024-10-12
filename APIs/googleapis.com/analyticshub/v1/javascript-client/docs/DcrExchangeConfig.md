# AnalyticsHubApi.DcrExchangeConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**singleLinkedDatasetPerCleanroom** | **Boolean** | Output only. If True, when subscribing to this DCR, it will create only one linked dataset containing all resources shared within the cleanroom. If False, when subscribing to this DCR, it will create 1 linked dataset per listing. This is not configurable, and by default, all new DCRs will have the restriction set to True. | [optional] [readonly] 
**singleSelectedResourceSharingRestriction** | **Boolean** | Output only. If True, this DCR restricts the contributors to sharing only a single resource in a Listing. And no two resources should have the same IDs. So if a contributor adds a view with a conflicting name, the CreateListing API will reject the request. if False, the data contributor can publish an entire dataset (as before). This is not configurable, and by default, all new DCRs will have the restriction set to True. | [optional] [readonly] 


