

# EndpointVerificationSpecificAttributes

Resource representing the [Endpoint Verification-specific attributes](https://cloud.google.com/endpoint-verification/docs/device-information) of a device.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalSignals** | **Map&lt;String, Object&gt;** | Additional signals reported by Endpoint Verification. It includes the following attributes: 1. Non-configurable attributes: hotfixes, av_installed, av_enabled, windows_domain_name, is_os_native_firewall_enabled, and is_secure_boot_enabled. 2. Configurable attributes: file_config, registry_config, and plist_config. |  [optional] |
|**browserAttributes** | [**List&lt;BrowserAttributes&gt;**](BrowserAttributes.md) | Details of browser profiles reported by Endpoint Verification. |  [optional] |
|**certificateAttributes** | [**List&lt;CertificateAttributes&gt;**](CertificateAttributes.md) | Details of certificates. |  [optional] |



