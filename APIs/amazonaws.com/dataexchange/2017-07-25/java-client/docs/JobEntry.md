

# JobEntry

AWS Data Exchange Jobs are asynchronous import or export operations used to create or copy assets. A data set owner can both import and export as they see fit. Someone with an entitlement to a data set can only export. Jobs are deleted 90 days after they are created.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arn** | [**String**](String.md) |  |  |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**details** | [**JobEntryDetails**](JobEntryDetails.md) |  |  |
|**errors** | [**List**](List.md) |  |  [optional] |
|**id** | [**String**](String.md) |  |  |
|**state** | [**State**](State.md) |  |  |
|**type** | [**Type**](Type.md) |  |  |
|**updatedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |



