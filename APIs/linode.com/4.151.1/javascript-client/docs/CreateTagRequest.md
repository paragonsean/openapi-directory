# LinodeApi.CreateTagRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **[Number]** | A list of Domain IDs to apply the new Tag to.  You must be allowed to &#x60;read_write&#x60; all of the requested Domains, or the Tag will not be created and an error will be returned.  | [optional] 
**label** | **String** | The new Tag.  | 
**linodes** | **[Number]** | A list of Linode IDs to apply the new Tag to.  You must be allowed to &#x60;read_write&#x60; all of the requested Linodes, or the Tag will not be created and an error will be returned.  | [optional] 
**nodebalancers** | **[Number]** | A list of NodeBalancer IDs to apply the new Tag to. You must be allowed to &#x60;read_write&#x60; all of the requested NodeBalancers, or the Tag will not be created and an error will be returned.  | [optional] 
**volumes** | **[Number]** | A list of Volume IDs to apply the new Tag to.  You must be allowed to &#x60;read_write&#x60; all of the requested Volumes, or the Tag will not be created and an error will be returned.  | [optional] 


