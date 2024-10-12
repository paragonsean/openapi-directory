

# CertificateIdentityConstraints

Describes constraints on a Certificate's Subject and SubjectAltNames.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowSubjectAltNamesPassthrough** | **Boolean** | Required. If this is true, the SubjectAltNames extension may be copied from a certificate request into the signed certificate. Otherwise, the requested SubjectAltNames will be discarded. |  [optional] |
|**allowSubjectPassthrough** | **Boolean** | Required. If this is true, the Subject field may be copied from a certificate request into the signed certificate. Otherwise, the requested Subject will be discarded. |  [optional] |
|**celExpression** | [**Expr**](Expr.md) |  |  [optional] |



