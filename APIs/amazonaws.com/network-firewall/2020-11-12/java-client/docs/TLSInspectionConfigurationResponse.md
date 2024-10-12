

# TLSInspectionConfigurationResponse

The high-level properties of a TLS inspection configuration. This, along with the <code>TLSInspectionConfiguration</code>, define the TLS inspection configuration. You can retrieve all objects for a TLS inspection configuration by calling <code>DescribeTLSInspectionConfiguration</code>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**tlSInspectionConfigurationArn** | [**String**](String.md) |  |  |
|**tlSInspectionConfigurationName** | [**String**](String.md) |  |  |
|**tlSInspectionConfigurationId** | [**String**](String.md) |  |  |
|**tlSInspectionConfigurationStatus** | [**ResourceStatus**](ResourceStatus.md) |  |  [optional] |
|**description** | [**String**](String.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**lastModifiedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**numberOfAssociations** | [**Integer**](Integer.md) |  |  [optional] |
|**encryptionConfiguration** | [**UpdateTLSInspectionConfigurationRequestEncryptionConfiguration**](UpdateTLSInspectionConfigurationRequestEncryptionConfiguration.md) |  |  [optional] |
|**certificates** | [**List**](List.md) |  |  [optional] |



