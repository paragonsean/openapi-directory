# NeutrinoApi.Blacklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isListed** | **Boolean** | True if the host is currently black-listed | 
**listHost** | **String** | The hostname of the DNSBL | 
**listName** | **String** | The name of the DNSBL | 
**listRating** | **Number** | The list rating [1-3] with 1 being the best rating and 3 the lowest rating | 
**responseTime** | **Number** | The DNSBL server response time in milliseconds | 
**returnCode** | **String** | The specific return code for this listing (only set if listed) | 
**txtRecord** | **String** | The TXT record returned for this listing (only set if listed) | 


