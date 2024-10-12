

# PrismaConfig

Settings specific to the Mediaocean Prisma tool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**prismaCpeCode** | [**PrismaCpeCode**](PrismaCpeCode.md) |  |  [optional] |
|**prismaType** | [**PrismaTypeEnum**](#PrismaTypeEnum) | Required. The Prisma type. |  [optional] |
|**supplier** | **String** | Required. The entity allocated this budget (DSP, site, etc.). |  [optional] |



## Enum: PrismaTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PRISMA_TYPE_UNSPECIFIED&quot; |
| DISPLAY | &quot;PRISMA_TYPE_DISPLAY&quot; |
| SEARCH | &quot;PRISMA_TYPE_SEARCH&quot; |
| VIDEO | &quot;PRISMA_TYPE_VIDEO&quot; |
| AUDIO | &quot;PRISMA_TYPE_AUDIO&quot; |
| SOCIAL | &quot;PRISMA_TYPE_SOCIAL&quot; |
| FEE | &quot;PRISMA_TYPE_FEE&quot; |



