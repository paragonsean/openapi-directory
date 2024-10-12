

# TerminalAssignment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**companyId** | **String** | The unique identifier of the company account to which terminal is assigned. |  |
|**merchantId** | **String** | The unique identifier of the merchant account to which terminal is assigned. |  [optional] |
|**reassignmentTarget** | [**TerminalReassignmentTarget**](TerminalReassignmentTarget.md) | Indicates where the terminal is in the process of being reassigned to. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the reassignment. Possible values:   * &#x60;reassignmentInProgress&#x60;: the terminal was boarded and is now scheduled to remove the configuration. Wait for the terminal to synchronize with the Adyen platform.  * &#x60;deployed&#x60;: the terminal is deployed and reassigned.   * &#x60;inventory&#x60;: the terminal is in inventory and cannot process transactions.   * &#x60;boarded&#x60;: the terminal is boarded to a store, or a merchant account representing a store, and can process transactions.   |  |
|**storeId** | **String** | The unique identifier of the store to which terminal is assigned. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| BOARDED | &quot;boarded&quot; |
| DEPLOYED | &quot;deployed&quot; |
| INVENTORY | &quot;inventory&quot; |
| REASSIGNMENT_IN_PROGRESS | &quot;reassignmentInProgress&quot; |



