# WowzaStreamingCloudRestApiReferenceDocumentation.StreamSource1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupIpAddress** | **String** | If &lt;em&gt;location_method&lt;/em&gt; is &lt;strong&gt;ip_address&lt;/strong&gt;, specify the backup IP address of the source encoder. | [optional] 
**ipAddress** | **String** | If &lt;em&gt;location_method&lt;/em&gt; is &lt;strong&gt;ip_address&lt;/strong&gt;, specify the primary IP address of the source encoder. | [optional] 
**location** | **String** | If &lt;em&gt;location_method&lt;/em&gt; is &lt;strong&gt;region&lt;/strong&gt;, specify a location as close as possible to the source encoder. | [optional] 
**locationMethod** | **String** | The method used to determine the location of the stream source, either by &lt;strong&gt;region&lt;/strong&gt; or based on the source encoder&#39;s &lt;strong&gt;ip_address&lt;/strong&gt;. | 
**name** | **String** | A descriptive name for the stream source. Maximum 255 characters. | 



## Enum: LocationEnum


* `asia_pacific_australia` (value: `"asia_pacific_australia"`)

* `asia_pacific_japan` (value: `"asia_pacific_japan"`)

* `asia_pacific_singapore` (value: `"asia_pacific_singapore"`)

* `asia_pacific_taiwan` (value: `"asia_pacific_taiwan"`)

* `eu_belgium` (value: `"eu_belgium"`)

* `eu_germany` (value: `"eu_germany"`)

* `eu_ireland` (value: `"eu_ireland"`)

* `south_america_brazil` (value: `"south_america_brazil"`)

* `us_central_iowa` (value: `"us_central_iowa"`)

* `us_east_s_carolina` (value: `"us_east_s_carolina"`)

* `us_east_virginia` (value: `"us_east_virginia"`)

* `us_west_california` (value: `"us_west_california"`)

* `us_west_oregon` (value: `"us_west_oregon"`)





## Enum: LocationMethodEnum


* `region` (value: `"region"`)

* `ip_address` (value: `"ip_address"`)




