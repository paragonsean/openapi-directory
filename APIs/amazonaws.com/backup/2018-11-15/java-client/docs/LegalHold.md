

# LegalHold

A legal hold is an administrative tool that helps prevent backups from being deleted while under a hold. While the hold is in place, backups under a hold cannot be deleted and lifecycle policies that would alter the backup status (such as transition to cold storage) are delayed until the legal hold is removed. A backup can have more than one legal hold. Legal holds are applied to one or more backups (also known as recovery points). These backups can be filtered by resource types and by resource IDs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | [**String**](String.md) |  |  [optional] |
|**status** | [**LegalHoldStatus**](LegalHoldStatus.md) |  |  [optional] |
|**description** | [**String**](String.md) |  |  [optional] |
|**legalHoldId** | [**String**](String.md) |  |  [optional] |
|**legalHoldArn** | [**String**](String.md) |  |  [optional] |
|**creationDate** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**cancellationDate** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



