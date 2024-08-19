# CloudTestingApi.AndroidTestLoop

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appApk** | [**FileReference**](FileReference.md) |  | [optional] 
**appBundle** | [**AppBundle**](AppBundle.md) |  | [optional] 
**appPackageId** | **String** | The java package for the application under test. The default is determined by examining the application&#39;s manifest. | [optional] 
**scenarioLabels** | **[String]** | The list of scenario labels that should be run during the test. The scenario labels should map to labels defined in the application&#39;s manifest. For example, player_experience and com.google.test.loops.player_experience add all of the loops labeled in the manifest with the com.google.test.loops.player_experience name to the execution. Scenarios can also be specified in the scenarios field. | [optional] 
**scenarios** | **[Number]** | The list of scenarios that should be run during the test. The default is all test loops, derived from the application&#39;s manifest. | [optional] 


