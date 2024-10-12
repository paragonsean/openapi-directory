# AmazonRoute53.ResourceRecordSetsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** |  | 
**type** | [**RRType**](RRType.md) |  | 
**setIdentifier** | **String** |  | [optional] 
**weight** | **Number** |  | [optional] 
**region** | [**ResourceRecordSetRegion**](ResourceRecordSetRegion.md) |  | [optional] 
**geoLocation** | [**ResourceRecordSetGeoLocation**](ResourceRecordSetGeoLocation.md) |  | [optional] 
**failover** | [**ResourceRecordSetFailover**](ResourceRecordSetFailover.md) |  | [optional] 
**multiValueAnswer** | **Boolean** |  | [optional] 
**TTL** | **Number** |  | [optional] 
**resourceRecords** | **Array** |  | [optional] 
**aliasTarget** | [**ResourceRecordSetAliasTarget**](ResourceRecordSetAliasTarget.md) |  | [optional] 
**healthCheckId** | **String** |  | [optional] 
**trafficPolicyInstanceId** | **String** |  | [optional] 
**cidrRoutingConfig** | [**CidrRoutingConfig**](CidrRoutingConfig.md) |  | [optional] 


