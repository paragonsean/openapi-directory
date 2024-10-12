

# GeneralName

Describes an ASN.1 X.400 <code>GeneralName</code> as defined in <a href=\"https://datatracker.ietf.org/doc/html/rfc5280\">RFC 5280</a>. Only one of the following naming options should be provided. Providing more than one option results in an <code>InvalidArgsException</code> error.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**otherName** | [**GeneralNameOtherName**](GeneralNameOtherName.md) |  |  [optional] |
|**rfc822Name** | [**String**](String.md) |  |  [optional] |
|**dnsName** | [**String**](String.md) |  |  [optional] |
|**directoryName** | [**ASN1Subject**](ASN1Subject.md) |  |  [optional] |
|**ediPartyName** | [**GeneralNameEdiPartyName**](GeneralNameEdiPartyName.md) |  |  [optional] |
|**uniformResourceIdentifier** | [**String**](String.md) |  |  [optional] |
|**ipAddress** | [**String**](String.md) |  |  [optional] |
|**registeredId** | [**String**](String.md) |  |  [optional] |



