

# AppD


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appDId** | **String** | Identifier of this MEC application descriptor. This attribute shall be globally unique. See note 1. |  |
|**appDNSRule** | [**List&lt;DNSRuleDescriptor&gt;**](DNSRuleDescriptor.md) | Describes DNS rules the MEC application requires. |  [optional] |
|**appDVersion** | **String** | Identifies the version of the application descriptor. |  |
|**appDescription** | **String** | Human readable description of the MEC application. |  |
|**appExtCpd** | [**List&lt;AppExternalCpd&gt;**](AppExternalCpd.md) | Describes external interface(s) exposed by this MEC application. |  [optional] |
|**appFeatureOptional** | [**List&lt;FeatureDependency&gt;**](FeatureDependency.md) | Describes features a MEC application may use if available. |  [optional] |
|**appFeatureRequired** | [**List&lt;FeatureDependency&gt;**](FeatureDependency.md) | Describes features a MEC application requires to run. |  [optional] |
|**appInfoName** | **String** | Human readable name for the MEC application. |  [optional] |
|**appLatency** | [**LatencyDescriptor**](LatencyDescriptor.md) |  |  [optional] |
|**appName** | **String** | Name to identify the MEC application. |  |
|**appProvider** | **String** | Provider of the application and of the AppD. |  |
|**appServiceOptional** | [**List&lt;ServiceDependency&gt;**](ServiceDependency.md) | Describes services a MEC application may use if available. |  [optional] |
|**appServiceProduced** | [**List&lt;ServiceDescriptor&gt;**](ServiceDescriptor.md) | Describes services a MEC application is able to produce to the platform or other MEC applications. Only relevant for service-producing apps. |  [optional] |
|**appServiceRequired** | [**List&lt;ServiceDependency&gt;**](ServiceDependency.md) | Describes services a MEC application requires to run. |  [optional] |
|**appSoftVersion** | **String** | Identifies the version of software of the MEC application. |  |
|**appTrafficRule** | [**List&lt;TrafficRuleDescriptor&gt;**](TrafficRuleDescriptor.md) | Describes traffic rules the MEC application requires. |  [optional] |
|**changeAppInstanceStateOpConfig** | **String** | NFV |  [optional] |
|**mecVersion** | **List&lt;String&gt;** | Identifies version(s) of MEC system compatible with the MEC application described in this version of the AppD. |  |
|**swImageDescriptor** | **String** | Ref NFV |  |
|**terminateAppInstanceOpConfig** | **String** | NFV |  [optional] |
|**transportDependencies** | [**List&lt;TransportDependency&gt;**](TransportDependency.md) | Transports, if any, that this application requires to be provided by the platform. These transports will be used by the application to deliver services provided by this application. Only relevant for service-producing apps. See note 2. |  [optional] |
|**virtualComputeDescriptor** | **String** | Ref NFV |  |
|**virtualStorageDescriptor** | **List&lt;String&gt;** | Defines descriptors of virtual storage resources to be used by the MEC application. |  [optional] |



