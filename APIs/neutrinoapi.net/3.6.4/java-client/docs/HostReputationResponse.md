

# HostReputationResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**host** | **String** | The IP address or host name |  |
|**isListed** | **Boolean** | Is this host blacklisted |  |
|**listCount** | **Integer** | The number of DNSBLs the host is listed on |  |
|**lists** | [**List&lt;Blacklist&gt;**](Blacklist.md) | Array of objects for each DNSBL checked |  |



