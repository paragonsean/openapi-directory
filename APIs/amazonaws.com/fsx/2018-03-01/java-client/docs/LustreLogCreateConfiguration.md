

# LustreLogCreateConfiguration

<p>The Lustre logging configuration used when creating or updating an Amazon FSx for Lustre file system. An Amazon File Cache is created with Lustre logging enabled by default, with a setting of <code>WARN_ERROR</code> for the logging events. which can't be changed.</p> <p>Lustre logging writes the enabled logging events for your file system or cache to Amazon CloudWatch Logs.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**level** | [**LustreAccessAuditLogLevel**](LustreAccessAuditLogLevel.md) |  |  |
|**destination** | [**String**](String.md) |  |  [optional] |



