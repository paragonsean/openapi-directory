

# DestinyDefinitionsDestinyMaterialRequirement

Many actions relating to items require you to expend materials: - Activating a talent node - Inserting a plug into a socket The items will refer to material requirements by a materialRequirementsHash in these cases, and this is the definition for those requirements in terms of the item required, how much of it is required and other interesting info. This is one of the rare/strange times where a single contract class is used both in definitions *and* in live data response contracts. I'm not sure yet whether I regret that.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Integer** | The amount of the material required. |  [optional] |
|**countIsConstant** | **Boolean** | If true, the material requirement count value is constant. Since The Witch Queen expansion, some material requirement counts can be dynamic and will need to be returned with an API call. |  [optional] |
|**deleteOnAction** | **Boolean** | If True, the material will be removed from the character&#39;s inventory when the action is performed. |  [optional] |
|**itemHash** | **Integer** | The hash identifier of the material required. Use it to look up the material&#39;s DestinyInventoryItemDefinition. |  [optional] |
|**omitFromRequirements** | **Boolean** | If True, this requirement is \&quot;silent\&quot;: don&#39;t bother showing it in a material requirements display. I mean, I&#39;m not your mom: I&#39;m not going to tell you you *can&#39;t* show it. But we won&#39;t show it in our UI. |  [optional] |



