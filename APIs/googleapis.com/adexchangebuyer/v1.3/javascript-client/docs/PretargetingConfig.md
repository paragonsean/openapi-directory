# AdExchangeBuyerApi.PretargetingConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingId** | **String** | The id for billing purposes, provided for reference. Leave this field blank for insert requests; the id will be generated automatically. | [optional] 
**configId** | **String** | The config id; generated automatically. Leave this field blank for insert requests. | [optional] 
**configName** | **String** | The name of the config. Must be unique. Required for all requests. | [optional] 
**creativeType** | **[String]** | List must contain exactly one of PRETARGETING_CREATIVE_TYPE_HTML or PRETARGETING_CREATIVE_TYPE_VIDEO. | [optional] 
**dimensions** | [**[PretargetingConfigDimensionsInner]**](PretargetingConfigDimensionsInner.md) | Requests which allow one of these (width, height) pairs will match. All pairs must be supported ad dimensions. | [optional] 
**excludedContentLabels** | **[String]** | Requests with any of these content labels will not match. Values are from content-labels.txt in the downloadable files section. | [optional] 
**excludedGeoCriteriaIds** | **[String]** | Requests containing any of these geo criteria ids will not match. | [optional] 
**excludedPlacements** | [**[PretargetingConfigExcludedPlacementsInner]**](PretargetingConfigExcludedPlacementsInner.md) | Requests containing any of these placements will not match. | [optional] 
**excludedUserLists** | **[String]** | Requests containing any of these users list ids will not match. | [optional] 
**excludedVerticals** | **[String]** | Requests containing any of these vertical ids will not match. Values are from the publisher-verticals.txt file in the downloadable files section. | [optional] 
**geoCriteriaIds** | **[String]** | Requests containing any of these geo criteria ids will match. | [optional] 
**isActive** | **Boolean** | Whether this config is active. Required for all requests. | [optional] 
**kind** | **String** | The kind of the resource, i.e. \&quot;adexchangebuyer#pretargetingConfig\&quot;. | [optional] [default to &#39;adexchangebuyer#pretargetingConfig&#39;]
**languages** | **[String]** | Request containing any of these language codes will match. | [optional] 
**maximumQps** | **String** | The maximum QPS allocated to this pretargeting configuration, used for pretargeting-level QPS limits. By default, this is not set, which indicates that there is no QPS limit at the configuration level (a global or account-level limit may still be imposed). | [optional] 
**mobileCarriers** | **[String]** | Requests containing any of these mobile carrier ids will match. Values are from mobile-carriers.csv in the downloadable files section. | [optional] 
**mobileDevices** | **[String]** | Requests containing any of these mobile device ids will match. Values are from mobile-devices.csv in the downloadable files section. | [optional] 
**mobileOperatingSystemVersions** | **[String]** | Requests containing any of these mobile operating system version ids will match. Values are from mobile-os.csv in the downloadable files section. | [optional] 
**placements** | [**[PretargetingConfigExcludedPlacementsInner]**](PretargetingConfigExcludedPlacementsInner.md) | Requests containing any of these placements will match. | [optional] 
**platforms** | **[String]** | Requests matching any of these platforms will match. Possible values are PRETARGETING_PLATFORM_MOBILE, PRETARGETING_PLATFORM_DESKTOP, and PRETARGETING_PLATFORM_TABLET. | [optional] 
**supportedCreativeAttributes** | **[String]** | Creative attributes should be declared here if all creatives corresponding to this pretargeting configuration have that creative attribute. Values are from pretargetable-creative-attributes.txt in the downloadable files section. | [optional] 
**userLists** | **[String]** | Requests containing any of these user list ids will match. | [optional] 
**vendorTypes** | **[String]** | Requests that allow any of these vendor ids will match. Values are from vendors.txt in the downloadable files section. | [optional] 
**verticals** | **[String]** | Requests containing any of these vertical ids will match. | [optional] 


