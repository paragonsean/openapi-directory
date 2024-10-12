# InfluxOssApiService.ScraperTargetResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowInsecure** | **Boolean** | Skip TLS verification on endpoint. | [optional] [default to false]
**bucketID** | **String** | The ID of the bucket to write to. | [optional] 
**name** | **String** | The name of the scraper target. | [optional] 
**orgID** | **String** | The organization ID. | [optional] 
**type** | **String** | The type of the metrics to be parsed. | [optional] 
**url** | **String** | The URL of the metrics endpoint. | [optional] 
**bucket** | **String** | The bucket name. | [optional] 
**id** | **String** |  | [optional] [readonly] 
**links** | [**ScraperTargetResponseAllOfLinks**](ScraperTargetResponseAllOfLinks.md) |  | [optional] 
**org** | **String** | The name of the organization. | [optional] 



## Enum: TypeEnum


* `prometheus` (value: `"prometheus"`)




