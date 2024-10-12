# ContentApiForShopping.AccountStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The ID of the account for which the status is reported. | [optional] 
**accountLevelIssues** | [**[AccountStatusAccountLevelIssue]**](AccountStatusAccountLevelIssue.md) | A list of account level issues. | [optional] 
**dataQualityIssues** | [**[AccountStatusDataQualityIssue]**](AccountStatusDataQualityIssue.md) | DEPRECATED - never populated. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;&#x60;content#accountStatus&#x60;\&quot; | [optional] 
**products** | [**[AccountStatusProducts]**](AccountStatusProducts.md) | List of product-related data by channel, destination, and country. Data in this field may be delayed by up to 30 minutes. | [optional] 
**websiteClaimed** | **Boolean** | Whether the account&#39;s website is claimed or not. | [optional] 


