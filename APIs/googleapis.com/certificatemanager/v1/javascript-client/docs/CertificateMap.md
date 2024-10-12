# CertificateManagerApi.CertificateMap

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The creation timestamp of a Certificate Map. | [optional] [readonly] 
**description** | **String** | One or more paragraphs of text description of a certificate map. | [optional] 
**gclbTargets** | [**[GclbTarget]**](GclbTarget.md) | Output only. A list of GCLB targets that use this Certificate Map. A Target Proxy is only present on this list if it&#39;s attached to a Forwarding Rule. | [optional] [readonly] 
**labels** | **{String: String}** | Set of labels associated with a Certificate Map. | [optional] 
**name** | **String** | A user-defined name of the Certificate Map. Certificate Map names must be unique globally and match pattern &#x60;projects/_*_/locations/_*_/certificateMaps/_*&#x60;. | [optional] 
**updateTime** | **String** | Output only. The update timestamp of a Certificate Map. | [optional] [readonly] 


