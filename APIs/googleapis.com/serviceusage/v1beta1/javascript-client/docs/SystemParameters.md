# ServiceUsageApi.SystemParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**[SystemParameterRule]**](SystemParameterRule.md) | Define system parameters. The parameters defined here will override the default parameters implemented by the system. If this field is missing from the service config, default system parameters will be used. Default system parameters and names is implementation-dependent. Example: define api key for all methods system_parameters rules: - selector: \&quot;*\&quot; parameters: - name: api_key url_query_parameter: api_key Example: define 2 api key names for a specific method. system_parameters rules: - selector: \&quot;/ListShelves\&quot; parameters: - name: api_key http_header: Api-Key1 - name: api_key http_header: Api-Key2 **NOTE:** All service configuration rules follow \&quot;last one wins\&quot; order. | [optional] 


