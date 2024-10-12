# NetworkSecurityApi.UrlList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Time when the security policy was created. | [optional] [readonly] 
**description** | **String** | Optional. Free-text description of the resource. | [optional] 
**name** | **String** | Required. Name of the resource provided by the user. Name is of the form projects/{project}/locations/{location}/urlLists/{url_list} url_list should match the pattern:(^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$). | [optional] 
**updateTime** | **String** | Output only. Time when the security policy was updated. | [optional] [readonly] 
**values** | **[String]** | Required. FQDNs and URLs. | [optional] 


