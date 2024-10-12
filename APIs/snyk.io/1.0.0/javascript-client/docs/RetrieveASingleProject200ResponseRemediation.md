# SnykApi.RetrieveASingleProject200ResponseRemediation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch** | **Object** | Recommended patches to apply to the project  (object)    paths (array) - List of paths to the vulnerable dependency that can be patched | [optional] 
**pin** | **Object** | Recommended pins to apply to the project (Python only)  (object)     + upgradeTo (string, required) - &#x60;package@version&#x60; to upgrade to     + vulns (array[string], required) - List of vulnerability ids that will be fixed as part of this upgrade     + isTransitive (boolean) - Describes if the dependency to be pinned is a transitive dependency | [optional] 
**upgrade** | **Object** | Recommended upgrades to apply to the project  (object)     + upgradeTo (string, required) - &#x60;package@version&#x60; to upgrade to     + upgrades (array[string], required) -  List of &#x60;package@version&#x60; that will be upgraded as part of this upgrade     + vulns (array[string], required) - List of vulnerability ids that will be fixed as part of this upgrade | [optional] 


