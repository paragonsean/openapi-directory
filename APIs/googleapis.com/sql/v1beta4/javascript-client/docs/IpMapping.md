# CloudSqlAdminApi.IpMapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipAddress** | **String** | The IP address assigned. | [optional] 
**timeToRetire** | **String** | The due time for this IP to be retired in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. This field is only available when the IP is scheduled to be retired. | [optional] 
**type** | **String** | The type of this IP address. A &#x60;PRIMARY&#x60; address is a public address that can accept incoming connections. A &#x60;PRIVATE&#x60; address is a private address that can accept incoming connections. An &#x60;OUTGOING&#x60; address is the source address of connections originating from the instance, if supported. | [optional] 



## Enum: TypeEnum


* `SQL_IP_ADDRESS_TYPE_UNSPECIFIED` (value: `"SQL_IP_ADDRESS_TYPE_UNSPECIFIED"`)

* `PRIMARY` (value: `"PRIMARY"`)

* `OUTGOING` (value: `"OUTGOING"`)

* `PRIVATE` (value: `"PRIVATE"`)

* `MIGRATED_1ST_GEN` (value: `"MIGRATED_1ST_GEN"`)




