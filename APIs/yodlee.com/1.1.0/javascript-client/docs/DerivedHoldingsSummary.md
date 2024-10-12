# YodleeCoreApis.DerivedHoldingsSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**[DerivedHoldingsAccount]**](DerivedHoldingsAccount.md) | Accounts that contribute to the classification. &lt;br&gt;&lt;b&gt;Required Feature Enablement&lt;/b&gt;: Asset classification feature.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] [readonly] 
**classificationType** | **String** | The classification type of the security. The supported asset classification type and the values are provided in the /holdings/assetClassificationList.&lt;br&gt;&lt;b&gt;Required Feature Enablement&lt;/b&gt;: Asset classification feature.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] [readonly] 
**classificationValue** | **String** | The classification value that corresponds to the classification type of the holding. The supported asset classification type and the values are provided in the /holdings/assetClassificationList.&lt;br&gt;&lt;b&gt;Required Feature Enablement&lt;/b&gt;: Asset classification feature.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] [readonly] 
**holding** | [**[DerivedHolding]**](DerivedHolding.md) | Securities that belong to the asset classification type and contributed to the summary value.&lt;br&gt;&lt;b&gt;Required Feature Enablement&lt;/b&gt;: Asset classification feature.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment, insurance&lt;br&gt; | [optional] [readonly] 
**value** | [**Money**](Money.md) |  | [optional] 


