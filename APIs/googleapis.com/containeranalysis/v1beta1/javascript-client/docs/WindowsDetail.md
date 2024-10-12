# ContainerAnalysisApi.WindowsDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpeUri** | **String** | Required. The CPE URI in [cpe format](https://cpe.mitre.org/specification/) in which the vulnerability manifests. Examples include distro or storage location for vulnerable jar. | [optional] 
**description** | **String** | The description of the vulnerability. | [optional] 
**fixingKbs** | [**[KnowledgeBase]**](KnowledgeBase.md) | Required. The names of the KBs which have hotfixes to mitigate this vulnerability. Note that there may be multiple hotfixes (and thus multiple KBs) that mitigate a given vulnerability. Currently any listed kb&#39;s presence is considered a fix. | [optional] 
**name** | **String** | Required. The name of the vulnerability. | [optional] 


