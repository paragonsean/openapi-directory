

# DataLakeStoreAccountPropertiesBasic

The basic account specific properties that are associated with an underlying Data Lake Store account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **UUID** | The unique identifier associated with this Data Lake Store account. |  [optional] [readonly] |
|**creationTime** | **OffsetDateTime** | The account creation time. |  [optional] [readonly] |
|**endpoint** | **String** | The full CName endpoint for this account. |  [optional] [readonly] |
|**lastModifiedTime** | **OffsetDateTime** | The account last modified time. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning status of the Data Lake Store account. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | The state of the Data Lake Store account. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| FAILED | &quot;Failed&quot; |
| CREATING | &quot;Creating&quot; |
| RUNNING | &quot;Running&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| PATCHING | &quot;Patching&quot; |
| SUSPENDING | &quot;Suspending&quot; |
| RESUMING | &quot;Resuming&quot; |
| DELETING | &quot;Deleting&quot; |
| DELETED | &quot;Deleted&quot; |
| UNDELETING | &quot;Undeleting&quot; |
| CANCELED | &quot;Canceled&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| SUSPENDED | &quot;Suspended&quot; |



