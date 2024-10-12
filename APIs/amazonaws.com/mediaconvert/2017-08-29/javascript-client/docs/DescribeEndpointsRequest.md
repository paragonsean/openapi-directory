# AwsElementalMediaConvert.DescribeEndpointsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxResults** | **Number** | Optional. Max number of endpoints, up to twenty, that will be returned at one time. | [optional] 
**mode** | **String** | Optional field, defaults to DEFAULT. Specify DEFAULT for this operation to return your endpoints if any exist, or to create an endpoint for you and return it if one doesn&#39;t already exist. Specify GET_ONLY to return your endpoints if any exist, or an empty list if none exist. | [optional] 
**nextToken** | **String** | Use this string, provided with the response to a previous request, to request the next batch of endpoints. | [optional] 



## Enum: ModeEnum


* `DEFAULT` (value: `"DEFAULT"`)

* `GET_ONLY` (value: `"GET_ONLY"`)




