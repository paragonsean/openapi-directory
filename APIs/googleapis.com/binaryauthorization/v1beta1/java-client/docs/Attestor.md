

# Attestor

An attestor that attests to container image artifacts. An existing attestor cannot be modified except where indicated.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Optional. A descriptive comment. This field may be updated. The field may be displayed in chooser dialogs. |  [optional] |
|**etag** | **String** | Optional. A checksum, returned by the server, that can be sent on update requests to ensure the attestor has an up-to-date value before attempting to update it. See https://google.aip.dev/154. |  [optional] |
|**name** | **String** | Required. The resource name, in the format: &#x60;projects/_*_/attestors/_*&#x60;. This field may not be updated. |  [optional] |
|**updateTime** | **String** | Output only. Time when the attestor was last updated. |  [optional] [readonly] |
|**userOwnedDrydockNote** | [**UserOwnedDrydockNote**](UserOwnedDrydockNote.md) |  |  [optional] |



