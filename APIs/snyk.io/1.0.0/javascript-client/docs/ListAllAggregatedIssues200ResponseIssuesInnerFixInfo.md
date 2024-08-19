# SnykApi.ListAllAggregatedIssues200ResponseIssuesInnerFixInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixedIn** | **[Object]** | The set of versions in which this issue has been fixed. If the issue spanned multiple versions (i.e. &#x60;1.x&#x60; and &#x60;2.x&#x60;) then there will be multiple &#x60;fixedIn&#x60; entries | [optional] 
**isFixable** | **Boolean** | Whether all of the issue&#39;s paths are fixable. Paths that are already patched are not considered fixable unless they have an alternative remediation (e.g. pinning or upgrading). An upgrade path where the only changes are in transitive dependencies is only considered fixable if the package manager supports it. | [optional] 
**isPartiallyFixable** | **Boolean** | Whether any of the issue&#39;s paths can be fixed. Paths that are already patched are not considered fixable unless they have an alternative remediation (e.g. pinning or upgrading).  An upgrade path where the only changes are in transitive dependencies is only considered fixable if the package manager supports it. | [optional] 
**isPatchable** | **Boolean** | Whether all the of issue&#39;s paths are patchable | [optional] 
**isPinnable** | **Boolean** | Whether the issue can be fixed by pinning a transitive | [optional] 
**isUpgradable** | **Boolean** | Whether all of the issue&#39;s paths are upgradable | [optional] 
**nearestFixedInVersion** | **String** | Nearest version which includes a fix for the issue. This is populated for container projects only. | [optional] 


