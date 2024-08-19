# AmazonElasticInference.DescribeAcceleratorOfferingsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locationType** | **String** |  The location type that you want to describe accelerator type offerings for. It can assume the following values: region: will return the accelerator type offering at the regional level. availability-zone: will return the accelerator type offering at the availability zone level. availability-zone-id: will return the accelerator type offering at the availability zone level returning the availability zone id.  | 
**acceleratorTypes** | **[String]** |  The list of accelerator types to describe.  | [optional] 



## Enum: LocationTypeEnum


* `region` (value: `"region"`)

* `availability-zone` (value: `"availability-zone"`)

* `availability-zone-id` (value: `"availability-zone-id"`)




