

# CapabilityInformation

Subscription-level properties and limits for Data Lake Store.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountCount** | **Integer** | The current number of accounts under this subscription. |  [optional] [readonly] |
|**maxAccountCount** | **Integer** | The maximum supported number of accounts under this subscription. |  [optional] [readonly] |
|**migrationState** | **Boolean** | The Boolean value of true or false to indicate the maintenance state. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | The subscription state. |  [optional] [readonly] |
|**subscriptionId** | **UUID** | The subscription credentials that uniquely identifies the subscription. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| REGISTERED | &quot;Registered&quot; |
| SUSPENDED | &quot;Suspended&quot; |
| DELETED | &quot;Deleted&quot; |
| UNREGISTERED | &quot;Unregistered&quot; |
| WARNED | &quot;Warned&quot; |



