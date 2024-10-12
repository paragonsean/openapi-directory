

# Feature

Feature represents the settings and status of any Hub Feature.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. When the Feature resource was created. |  [optional] [readonly] |
|**deleteTime** | **String** | Output only. When the Feature resource was deleted. |  [optional] [readonly] |
|**fleetDefaultMemberConfig** | [**CommonFleetDefaultMemberConfigSpec**](CommonFleetDefaultMemberConfigSpec.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels for this Feature. |  [optional] |
|**membershipSpecs** | [**Map&lt;String, MembershipFeatureSpec&gt;**](MembershipFeatureSpec.md) | Optional. Membership-specific configuration for this Feature. If this Feature does not support any per-Membership configuration, this field may be unused. The keys indicate which Membership the configuration is for, in the form: &#x60;projects/{p}/locations/{l}/memberships/{m}&#x60; Where {p} is the project, {l} is a valid location and {m} is a valid Membership in this project at that location. {p} WILL match the Feature&#39;s project. {p} will always be returned as the project number, but the project ID is also accepted during input. If the same Membership is specified in the map twice (using the project ID form, and the project number form), exactly ONE of the entries will be saved, with no guarantees as to which. For this reason, it is recommended the same format be used for all entries when mutating a Feature. |  [optional] |
|**membershipStates** | [**Map&lt;String, MembershipFeatureState&gt;**](MembershipFeatureState.md) | Output only. Membership-specific Feature status. If this Feature does report any per-Membership status, this field may be unused. The keys indicate which Membership the state is for, in the form: &#x60;projects/{p}/locations/{l}/memberships/{m}&#x60; Where {p} is the project number, {l} is a valid location and {m} is a valid Membership in this project at that location. {p} MUST match the Feature&#39;s project number. |  [optional] [readonly] |
|**name** | **String** | Output only. The full, unique name of this Feature resource in the format &#x60;projects/_*_/locations/_*_/features/_*&#x60;. |  [optional] [readonly] |
|**resourceState** | [**FeatureResourceState**](FeatureResourceState.md) |  |  [optional] |
|**scopeSpecs** | **Map&lt;String, Object&gt;** | Optional. Scope-specific configuration for this Feature. If this Feature does not support any per-Scope configuration, this field may be unused. The keys indicate which Scope the configuration is for, in the form: &#x60;projects/{p}/locations/global/scopes/{s}&#x60; Where {p} is the project, {s} is a valid Scope in this project. {p} WILL match the Feature&#39;s project. {p} will always be returned as the project number, but the project ID is also accepted during input. If the same Scope is specified in the map twice (using the project ID form, and the project number form), exactly ONE of the entries will be saved, with no guarantees as to which. For this reason, it is recommended the same format be used for all entries when mutating a Feature. |  [optional] |
|**scopeStates** | [**Map&lt;String, ScopeFeatureState&gt;**](ScopeFeatureState.md) | Output only. Scope-specific Feature status. If this Feature does report any per-Scope status, this field may be unused. The keys indicate which Scope the state is for, in the form: &#x60;projects/{p}/locations/global/scopes/{s}&#x60; Where {p} is the project, {s} is a valid Scope in this project. {p} WILL match the Feature&#39;s project. |  [optional] [readonly] |
|**spec** | [**CommonFeatureSpec**](CommonFeatureSpec.md) |  |  [optional] |
|**state** | [**CommonFeatureState**](CommonFeatureState.md) |  |  [optional] |
|**updateTime** | **String** | Output only. When the Feature resource was last updated. |  [optional] [readonly] |



