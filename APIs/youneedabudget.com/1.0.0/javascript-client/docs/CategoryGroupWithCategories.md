# YnabApiEndpoints.CategoryGroupWithCategories

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **Boolean** | Whether or not the category group has been deleted.  Deleted category groups will only be included in delta requests. | 
**hidden** | **Boolean** | Whether or not the category group is hidden | 
**id** | **String** |  | 
**name** | **String** |  | 
**categories** | [**[Category]**](Category.md) | Category group categories.  Amounts (budgeted, activity, balance, etc.) are specific to the current budget month (UTC). | 


