# TrafficDirectorApi.ClientStatusRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excludeResourceContents** | **Boolean** | If true, the server will not include the resource contents in the response (i.e., the generic_xds_configs.xds_config field will not be populated). [#not-implemented-hide:] | [optional] 
**node** | [**Node**](Node.md) |  | [optional] 
**nodeMatchers** | [**[NodeMatcher]**](NodeMatcher.md) | Management server can use these match criteria to identify clients. The match follows OR semantics. | [optional] 


