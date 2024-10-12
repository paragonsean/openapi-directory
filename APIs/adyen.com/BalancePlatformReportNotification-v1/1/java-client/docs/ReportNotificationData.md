

# ReportNotificationData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountHolder** | [**ResourceReference**](ResourceReference.md) | The account holder related to the report. |  [optional] |
|**balanceAccount** | [**ResourceReference**](ResourceReference.md) | The balance account related to the report. |  [optional] |
|**balancePlatform** | **String** | The unique identifier of the balance platform. |  [optional] |
|**creationDate** | **OffsetDateTime** | The date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**. |  [optional] |
|**downloadUrl** | **String** | The URL at which you can download the report. To download, you must authenticate your GET request with your [API credentials](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/overview). |  |
|**fileName** | **String** | The filename of the report. |  |
|**reportType** | **String** | Type of report. |  |



