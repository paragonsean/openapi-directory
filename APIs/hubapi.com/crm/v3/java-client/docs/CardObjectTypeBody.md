

# CardObjectTypeBody


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**NameEnum**](#NameEnum) | A CRM object type where this card should be displayed. |  |
|**propertiesToSend** | **List&lt;String&gt;** | An array of properties that should be sent to this card&#39;s target URL when the data fetch request is made. Must be valid properties for the corresponding CRM object type. |  |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| CONTACTS | &quot;contacts&quot; |
| DEALS | &quot;deals&quot; |
| COMPANIES | &quot;companies&quot; |
| TICKETS | &quot;tickets&quot; |



