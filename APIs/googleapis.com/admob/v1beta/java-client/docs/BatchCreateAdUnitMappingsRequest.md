

# BatchCreateAdUnitMappingsRequest

Request to create a batch of ad unit mappings under the specific AdMob account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requests** | [**List&lt;CreateAdUnitMappingRequest&gt;**](CreateAdUnitMappingRequest.md) | Required. The request message specifying the ad unit mappings to create. A maximum of 100 ad unit mappings can be created in a batch. If the number of ad unit mappings in the batch request exceed 100, the entire request will be rejected and no ad unit mappings will be created. |  [optional] |



