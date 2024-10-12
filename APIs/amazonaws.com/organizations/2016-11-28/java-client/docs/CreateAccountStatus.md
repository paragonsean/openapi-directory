

# CreateAccountStatus

Contains the status about a <a>CreateAccount</a> or <a>CreateGovCloudAccount</a> request to create an Amazon Web Services account or an Amazon Web Services GovCloud (US) account in an organization.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**String**](String.md) |  |  [optional] |
|**accountName** | [**String**](String.md) |  |  [optional] |
|**state** | [**CreateAccountState**](CreateAccountState.md) |  |  [optional] |
|**requestedTimestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**completedTimestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**accountId** | [**String**](String.md) |  |  [optional] |
|**govCloudAccountId** | [**String**](String.md) |  |  [optional] |
|**failureReason** | [**CreateAccountFailureReason**](CreateAccountFailureReason.md) |  |  [optional] |



