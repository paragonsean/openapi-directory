

# Adapter

Describes adapters supported by each mediation ad source. Adapters correspond to a specific SDK implementation of the ad source, and are each associated with a single platform and a list of supported ad unit formats. Adapters may also require setting some configurations to perform ad requests. Configurations can be specified in the AdUnitMapping by setting the [ad_unit_configurations](#AdUnitMapping.ad_unit_configurations) key/value pairs. For example, the ad_unit_configurations can be used to pass various IDs to the adapter's third-party SDK.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adapterConfigMetadata** | [**List&lt;AdapterAdapterConfigMetadata&gt;**](AdapterAdapterConfigMetadata.md) | Output only. Configuration metadata associated with this adapter. |  [optional] [readonly] |
|**adapterId** | **String** | Output only. ID of this adapter. It is used to set [adapter_id](#AdUnitMapping.adapter_id). |  [optional] [readonly] |
|**formats** | **List&lt;String&gt;** | Output only. Indicates the formats of the ad units supported by this adapter. |  [optional] [readonly] |
|**name** | **String** | Output only. Resource name of the adapter. Format is: accounts/{publisher_id}/adSources/{ad_source_id}/adapters/{adapter_id}. |  [optional] [readonly] |
|**platform** | **String** | Output only. Mobile application platform supported by this adapter. Supported values are: IOS, ANDROID, WINDOWS_PHONE |  [optional] [readonly] |
|**title** | **String** | Output only. The display name of this adapter. |  [optional] [readonly] |



