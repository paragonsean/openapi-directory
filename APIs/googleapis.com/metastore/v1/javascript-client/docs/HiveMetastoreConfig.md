# DataprocMetastoreApi.HiveMetastoreConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auxiliaryVersions** | [**{String: AuxiliaryVersionConfig}**](AuxiliaryVersionConfig.md) | A mapping of Hive metastore version to the auxiliary version configuration. When specified, a secondary Hive metastore service is created along with the primary service. All auxiliary versions must be less than the service&#39;s primary version. The key is the auxiliary service name and it must match the regular expression a-z?. This means that the first character must be a lowercase letter, and all the following characters must be hyphens, lowercase letters, or digits, except the last character, which cannot be a hyphen. | [optional] 
**configOverrides** | **{String: String}** | A mapping of Hive metastore configuration key-value pairs to apply to the Hive metastore (configured in hive-site.xml). The mappings override system defaults (some keys cannot be overridden). These overrides are also applied to auxiliary versions and can be further customized in the auxiliary version&#39;s AuxiliaryVersionConfig. | [optional] 
**endpointProtocol** | **String** | The protocol to use for the metastore service endpoint. If unspecified, defaults to THRIFT. | [optional] 
**kerberosConfig** | [**KerberosConfig**](KerberosConfig.md) |  | [optional] 
**version** | **String** | Immutable. The Hive metastore schema version. | [optional] 



## Enum: EndpointProtocolEnum


* `ENDPOINT_PROTOCOL_UNSPECIFIED` (value: `"ENDPOINT_PROTOCOL_UNSPECIFIED"`)

* `THRIFT` (value: `"THRIFT"`)

* `GRPC` (value: `"GRPC"`)




