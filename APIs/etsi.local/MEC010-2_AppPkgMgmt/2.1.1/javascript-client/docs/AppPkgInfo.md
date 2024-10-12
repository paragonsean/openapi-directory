# EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**AppPkgInfoLinks**](AppPkgInfoLinks.md) |  | 
**additionalArtifacts** | **Object** | Additional information of application package artifacts that are not application software images. Type is TBD | [optional] 
**appDId** | **String** | Identifier of this MEC application descriptor. This attribute shall be globally unique. | 
**appDVersion** | **String** | Identifies the version of the application descriptor. | 
**appName** | **String** | Name to identify the MEC application. | 
**appProvider** | **String** | Provider of the application and of the AppD. | [optional] 
**appSoftwareVersion** | **String** | Software version of the application. This is updated when there is any change to the software in the onboarded application package. | 
**checksum** | [**Checksum**](Checksum.md) |  | 
**id** | **String** | Identifier of the onboarded application package. | 
**onboardingState** | [**OnboardingState**](OnboardingState.md) |  | 
**operationalState** | [**AppPkgOperationalState**](AppPkgOperationalState.md) |  | 
**softwareImages** | **Object** | Information of application software image in application package. Type is TBD | 
**usageState** | [**UsageState**](UsageState.md) |  | 
**userDefinedData** | **{String: Object}** | &#39;This data type represents a list of key-value pairs. The order of the pairs in the list is not significant. In JSON, a set of key-value pairs is represented as an object. It shall comply with the provisions defined in clause 4 of IETF RFC 8259&#39; | [optional] 


