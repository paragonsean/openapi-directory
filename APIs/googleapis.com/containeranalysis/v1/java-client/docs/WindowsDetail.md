

# WindowsDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cpeUri** | **String** | Required. The [CPE URI](https://cpe.mitre.org/specification/) this vulnerability affects. |  [optional] |
|**description** | **String** | The description of this vulnerability. |  [optional] |
|**fixingKbs** | [**List&lt;KnowledgeBase&gt;**](KnowledgeBase.md) | Required. The names of the KBs which have hotfixes to mitigate this vulnerability. Note that there may be multiple hotfixes (and thus multiple KBs) that mitigate a given vulnerability. Currently any listed KBs presence is considered a fix. |  [optional] |
|**name** | **String** | Required. The name of this vulnerability. |  [optional] |



