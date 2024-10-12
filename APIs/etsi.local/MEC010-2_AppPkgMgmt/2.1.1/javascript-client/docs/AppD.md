# EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppD

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appDId** | **String** | Identifier of this MEC application descriptor. This attribute shall be globally unique. See note 1. | 
**appDNSRule** | [**[DNSRuleDescriptor]**](DNSRuleDescriptor.md) | Describes DNS rules the MEC application requires. | [optional] 
**appDVersion** | **String** | Identifies the version of the application descriptor. | 
**appDescription** | **String** | Human readable description of the MEC application. | 
**appExtCpd** | [**[AppExternalCpd]**](AppExternalCpd.md) | Describes external interface(s) exposed by this MEC application. | [optional] 
**appFeatureOptional** | [**[FeatureDependency]**](FeatureDependency.md) | Describes features a MEC application may use if available. | [optional] 
**appFeatureRequired** | [**[FeatureDependency]**](FeatureDependency.md) | Describes features a MEC application requires to run. | [optional] 
**appInfoName** | **String** | Human readable name for the MEC application. | [optional] 
**appLatency** | [**LatencyDescriptor**](LatencyDescriptor.md) |  | [optional] 
**appName** | **String** | Name to identify the MEC application. | 
**appProvider** | **String** | Provider of the application and of the AppD. | 
**appServiceOptional** | [**[ServiceDependency]**](ServiceDependency.md) | Describes services a MEC application may use if available. | [optional] 
**appServiceProduced** | [**[ServiceDescriptor]**](ServiceDescriptor.md) | Describes services a MEC application is able to produce to the platform or other MEC applications. Only relevant for service-producing apps. | [optional] 
**appServiceRequired** | [**[ServiceDependency]**](ServiceDependency.md) | Describes services a MEC application requires to run. | [optional] 
**appSoftVersion** | **String** | Identifies the version of software of the MEC application. | 
**appTrafficRule** | [**[TrafficRuleDescriptor]**](TrafficRuleDescriptor.md) | Describes traffic rules the MEC application requires. | [optional] 
**changeAppInstanceStateOpConfig** | **String** | NFV | [optional] 
**mecVersion** | **[String]** | Identifies version(s) of MEC system compatible with the MEC application described in this version of the AppD. | 
**swImageDescriptor** | **String** | Ref NFV | 
**terminateAppInstanceOpConfig** | **String** | NFV | [optional] 
**transportDependencies** | [**[TransportDependency]**](TransportDependency.md) | Transports, if any, that this application requires to be provided by the platform. These transports will be used by the application to deliver services provided by this application. Only relevant for service-producing apps. See note 2. | [optional] 
**virtualComputeDescriptor** | **String** | Ref NFV | 
**virtualStorageDescriptor** | **[String]** | Defines descriptors of virtual storage resources to be used by the MEC application. | [optional] 


