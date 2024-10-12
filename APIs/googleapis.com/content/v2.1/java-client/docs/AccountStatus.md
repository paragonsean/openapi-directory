

# AccountStatus

The status of an account, that is, information about its products, which is computed offline and not returned immediately at insertion time.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The ID of the account for which the status is reported. |  [optional] |
|**accountLevelIssues** | [**List&lt;AccountStatusAccountLevelIssue&gt;**](AccountStatusAccountLevelIssue.md) | A list of account level issues. |  [optional] |
|**accountManagement** | **String** | How the account is managed. Acceptable values are: - \&quot;&#x60;manual&#x60;\&quot; - \&quot;&#x60;automatic&#x60;\&quot;  |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;&#x60;content#accountStatus&#x60;\&quot; |  [optional] |
|**products** | [**List&lt;AccountStatusProducts&gt;**](AccountStatusProducts.md) | List of product-related data by channel, destination, and country. Data in this field may be delayed by up to 30 minutes. |  [optional] |
|**websiteClaimed** | **Boolean** | Whether the account&#39;s website is claimed or not. |  [optional] |



