# YnabApiEndpoints.MonthDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | **Number** | The total amount of transactions in the month, excluding those categorized to &#39;Inflow: Ready to Assign&#39; | 
**ageOfMoney** | **Number** | The Age of Money as of the month | [optional] 
**budgeted** | **Number** | The total amount budgeted in the month | 
**deleted** | **Boolean** | Whether or not the month has been deleted.  Deleted months will only be included in delta requests. | 
**income** | **Number** | The total amount of transactions categorized to &#39;Inflow: Ready to Assign&#39; in the month | 
**month** | **Date** |  | 
**note** | **String** |  | [optional] 
**toBeBudgeted** | **Number** | The available amount for &#39;Ready to Assign&#39; | 
**categories** | [**[Category]**](Category.md) | The budget month categories.  Amounts (budgeted, activity, balance, etc.) are specific to the {month} parameter specified. | 


