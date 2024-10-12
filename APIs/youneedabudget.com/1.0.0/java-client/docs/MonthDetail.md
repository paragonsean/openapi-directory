

# MonthDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activity** | **Long** | The total amount of transactions in the month, excluding those categorized to &#39;Inflow: Ready to Assign&#39; |  |
|**ageOfMoney** | **Integer** | The Age of Money as of the month |  [optional] |
|**budgeted** | **Long** | The total amount budgeted in the month |  |
|**deleted** | **Boolean** | Whether or not the month has been deleted.  Deleted months will only be included in delta requests. |  |
|**income** | **Long** | The total amount of transactions categorized to &#39;Inflow: Ready to Assign&#39; in the month |  |
|**month** | **LocalDate** |  |  |
|**note** | **String** |  |  [optional] |
|**toBeBudgeted** | **Long** | The available amount for &#39;Ready to Assign&#39; |  |
|**categories** | [**List&lt;Category&gt;**](Category.md) | The budget month categories.  Amounts (budgeted, activity, balance, etc.) are specific to the {month} parameter specified. |  |



