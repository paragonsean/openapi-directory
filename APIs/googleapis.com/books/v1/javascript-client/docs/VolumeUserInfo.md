# BooksApi.VolumeUserInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquiredTime** | **String** | Timestamp when this volume was acquired by the user. (RFC 3339 UTC date-time format) Acquiring includes purchase, user upload, receiving family sharing, etc. | [optional] 
**acquisitionType** | **Number** | How this volume was acquired. | [optional] 
**copy** | [**VolumeUserInfoCopy**](VolumeUserInfoCopy.md) |  | [optional] 
**entitlementType** | **Number** | Whether this volume is purchased, sample, pd download etc. | [optional] 
**familySharing** | [**VolumeUserInfoFamilySharing**](VolumeUserInfoFamilySharing.md) |  | [optional] 
**isFamilySharedFromUser** | **Boolean** | Whether or not the user shared this volume with the family. | [optional] 
**isFamilySharedToUser** | **Boolean** | Whether or not the user received this volume through family sharing. | [optional] 
**isFamilySharingAllowed** | **Boolean** | Deprecated: Replaced by familySharing. | [optional] 
**isFamilySharingDisabledByFop** | **Boolean** | Deprecated: Replaced by familySharing. | [optional] 
**isInMyBooks** | **Boolean** | Whether or not this volume is currently in \&quot;my books.\&quot; | [optional] 
**isPreordered** | **Boolean** | Whether or not this volume was pre-ordered by the authenticated user making the request. (In LITE projection.) | [optional] 
**isPurchased** | **Boolean** | Whether or not this volume was purchased by the authenticated user making the request. (In LITE projection.) | [optional] 
**isUploaded** | **Boolean** | Whether or not this volume was user uploaded. | [optional] 
**readingPosition** | [**ReadingPosition**](ReadingPosition.md) |  | [optional] 
**rentalPeriod** | [**VolumeUserInfoRentalPeriod**](VolumeUserInfoRentalPeriod.md) |  | [optional] 
**rentalState** | **String** | Whether this book is an active or an expired rental. | [optional] 
**review** | [**Review**](Review.md) |  | [optional] 
**updated** | **String** | Timestamp when this volume was last modified by a user action, such as a reading position update, volume purchase or writing a review. (RFC 3339 UTC date-time format). | [optional] 
**userUploadedVolumeInfo** | [**VolumeUserInfoUserUploadedVolumeInfo**](VolumeUserInfoUserUploadedVolumeInfo.md) |  | [optional] 


