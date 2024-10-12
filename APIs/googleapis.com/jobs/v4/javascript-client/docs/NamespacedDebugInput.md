# CloudTalentSolutionApi.NamespacedDebugInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolutelyForcedExpNames** | **[String]** | Set of experiment names to be absolutely forced. These experiments will be forced without evaluating the conditions. | [optional] 
**absolutelyForcedExpTags** | **[String]** | Set of experiment tags to be absolutely forced. The experiments with these tags will be forced without evaluating the conditions. | [optional] 
**absolutelyForcedExps** | **[Number]** | Set of experiment ids to be absolutely forced. These ids will be forced without evaluating the conditions. | [optional] 
**conditionallyForcedExpNames** | **[String]** | Set of experiment names to be conditionally forced. These experiments will be forced only if their conditions and their parent domain&#39;s conditions are true. | [optional] 
**conditionallyForcedExpTags** | **[String]** | Set of experiment tags to be conditionally forced. The experiments with these tags will be forced only if their conditions and their parent domain&#39;s conditions are true. | [optional] 
**conditionallyForcedExps** | **[Number]** | Set of experiment ids to be conditionally forced. These ids will be forced only if their conditions and their parent domain&#39;s conditions are true. | [optional] 
**disableAutomaticEnrollmentSelection** | **Boolean** | If true, disable automatic enrollment selection (at all diversion points). Automatic enrollment selection means experiment selection process based on the experiment&#39;s automatic enrollment condition. This does not disable selection of forced experiments. Setting this field to false does not change anything in the experiment selection process. | [optional] 
**disableExpNames** | **[String]** | Set of experiment names to be disabled. If an experiment is disabled, it is never selected nor forced. If an aggregate experiment is disabled, its partitions are disabled together. If an experiment with an enrollment is disabled, the enrollment is disabled together. If a name corresponds to a domain, the domain itself and all descendant experiments and domains are disabled together. | [optional] 
**disableExpTags** | **[String]** | Set of experiment tags to be disabled. All experiments that are tagged with one or more of these tags are disabled. If an experiment is disabled, it is never selected nor forced. If an aggregate experiment is disabled, its partitions are disabled together. If an experiment with an enrollment is disabled, the enrollment is disabled together. | [optional] 
**disableExps** | **[Number]** | Set of experiment ids to be disabled. If an experiment is disabled, it is never selected nor forced. If an aggregate experiment is disabled, its partitions are disabled together. If an experiment with an enrollment is disabled, the enrollment is disabled together. If an ID corresponds to a domain, the domain itself and all descendant experiments and domains are disabled together. | [optional] 
**disableManualEnrollmentSelection** | **Boolean** | If true, disable manual enrollment selection (at all diversion points). Manual enrollment selection means experiment selection process based on the request&#39;s manual enrollment states (a.k.a. opt-in experiments). This does not disable selection of forced experiments. Setting this field to false does not change anything in the experiment selection process. | [optional] 
**disableOrganicSelection** | **Boolean** | If true, disable organic experiment selection (at all diversion points). Organic selection means experiment selection process based on traffic allocation and diversion condition evaluation. This does not disable selection of forced experiments. This is useful in cases when it is not known whether experiment selection behavior is responsible for a error or breakage. Disabling organic selection may help to isolate the cause of a given problem. Setting this field to false does not change anything in the experiment selection process. | [optional] 
**forcedFlags** | **{String: String}** | Flags to force in a particular experiment state. Map from flag name to flag value. | [optional] 
**forcedRollouts** | **{String: Boolean}** | Rollouts to force in a particular experiment state. Map from rollout name to rollout value. | [optional] 
**testingMode** | **String** | Sets different testing modes. See the documentation in the TestingMode message for more information. | [optional] 



## Enum: TestingModeEnum


* `UNSPECIFIED` (value: `"TESTING_MODE_UNSPECIFIED"`)

* `ALL_OFF` (value: `"TESTING_MODE_ALL_OFF"`)

* `ALL_ON` (value: `"TESTING_MODE_ALL_ON"`)




