

# PullDocRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**docDetails** | [**PullDocRequestDocDetails**](PullDocRequestDocDetails.md) |  |  |
|**format** | **String** | The certificate data in the response. Possible values of this attribute are:   xml: for certificate data in machine readable xml format   pdf: for certificate data in printable pdf format   both: for certificate data in both xml and pdf format. If the format attribute is not present in the request, then the API must return Base64 encoded PDF data in the response. Please see the response section below for more details. |  |
|**orgId** | **String** | Org Id is the user id provided to the Digital Locker application by the issuer application for accessing the API. |  |
|**ts** | **String** | A timestamp value. This will be used to decode the keyHash element described below. |  |
|**txn** | **String** | Transaction id. |  |
|**ver** | **String** | API version. |  |



