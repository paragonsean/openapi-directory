

# GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInner

Resource sharing request Object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalBarcode** | **List&lt;String&gt;** | List of additional barcodes. Note that the first one appears in the main barcode field. |  [optional] |
|**additionalPersonName** | **String** | The name of an additional contact. |  [optional] |
|**agreeToCopyrightTerms** | **Boolean** | Indication whether the requester has agreed to the copyright terms. Mandatory for borrowing requests. Currently not relevant for lending requests. |  [optional] |
|**allowOtherFormats** | **Boolean** | Indication whether other formats besides the value in format field are acceptable. Default is false. |  [optional] |
|**author** | **String** | Author of the requested resource. |  [optional] |
|**authorInitials** | **String** | Author initials of the requested resource. |  [optional] |
|**barcode** | **String** | Barcode of the requested resource. |  [optional] |
|**bibNote** | **String** | The note of the bibliographic record. |  [optional] |
|**callNumber** | **String** | The call number of the book. Indicates the library shelf on which the books are located. |  [optional] |
|**chapter** | **String** | The chapter number in the journal that contains the article. |  [optional] |
|**chapterAuthor** | **String** | For a book chapter, the author of this chapter. |  [optional] |
|**chapterTitle** | **String** | For a book chapter, the title of this chapter. |  [optional] |
|**citationType** | [**GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerCitationType**](GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerCitationType.md) |  |  [optional] |
|**copyrightStatus** | [**GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerCopyrightStatus**](GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerCopyrightStatus.md) |  |  [optional] |
|**createdDate** | **LocalDate** | The request creation date. |  [optional] |
|**createdTime** | **OffsetDateTime** | The request creation time. |  [optional] |
|**doi** | **String** | The doi of the requested resource. |  [optional] |
|**edition** | **String** | The edition of the requested resource. |  [optional] |
|**editor** | **String** | The editor of the book (typically used for books where chapters have different authors). |  [optional] |
|**endPage** | **String** | The end page of the requested resource. |  [optional] |
|**externalId** | **String** | External identifier of the resource sharing request. Mandatory when creating a lending request. |  [optional] |
|**format** | [**GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerFormat**](GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerFormat.md) |  |  [optional] |
|**fund** | [**GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerFund**](GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerFund.md) |  |  [optional] |
|**hasActiveNotes** | **Boolean** | Indication whether the request has active notes. Output parameter. |  [optional] |
|**isbn** | **String** | ISBN of the requested resource. |  [optional] |
|**issn** | **String** | ISSN of the requested resource. |  [optional] |
|**issue** | **String** | The issue of the requested resource. |  [optional] |
|**journalTitle** | **String** | The title of the journal. Relevant when an article is requested. |  [optional] |
|**lastInterestDate** | **LocalDate** | Last date the request is needed. Optional. |  [optional] |
|**lastModifiedDate** | **LocalDate** | Date by which the last change to the request was made. |  [optional] |
|**lastModifiedTime** | **OffsetDateTime** | Time by which the last change to the request was made. |  [optional] |
|**lccNumber** | **String** | The library of congress number of the book. |  [optional] |
|**levelOfService** | [**GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerLevelOfService**](GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerLevelOfService.md) |  |  [optional] |
|**lostDamagedFee** | **Object** |  |  [optional] |
|**maximumFee** | **Float** | Maximum fee the user is willing to pay for the request. Currently not relevant for lending requests. |  [optional] |
|**mmsId** | **String** | MMS ID of the requested resource. Borrowing request: this is relevant after physical material has arrived. Lending request: if supplied when creating a request, the request will be attached to this bib record. See [GET BIB API](https://developers.exlibrisgroup.com/alma/apis/bibs/GET/gwPcGly021om4RTvtjbPleCklCGxeYAf3JPdiJpJhUA&#x3D;/af2fb69d-64f4-42bc-bb05-d8a0ae56936e). |  [optional] |
|**needPatronInfo** | **Boolean** | Indication whether patron information is needed. Not relevant for lending requests. |  [optional] |
|**note** | **String** | General note. |  [optional] |
|**oclcNumber** | **String** | The oclc number of the book. |  [optional] |
|**otherStandardId** | **String** | The other standard id of the requested resource. |  [optional] |
|**owner** | **String** | The resource sharing library code. See [Get libraries API](https://developers.exlibrisgroup.com/alma/apis/conf/GET/gwPcGly021p29HpB7XTI4Dp4I8TKv6CAxBlD4LyRaVE&#x3D;/37088dc9-c685-4641-bc7f-60b5ca7cabed). Borrowing request: Optional. Used only when there are more than one resource sharing library defined for the user. Lending request: Mandatory. |  [optional] |
|**pages** | **String** | The relevant pages of the requested resource. |  [optional] |
|**part** | **String** | The part of the requested resource. |  [optional] |
|**partner** | [**GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerPartner**](GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerPartner.md) |  |  [optional] |
|**pickupLocation** | [**GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerPickupLocation**](GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerPickupLocation.md) |  |  [optional] |
|**pickupLocationType** | **String** | The pickup location type. The pickup location type. Possible values are: LIBRARY, CIRCULATION_DESK. |  [optional] |
|**placeOfPublication** | **String** | The publication place of the requested resource. |  [optional] |
|**pmid** | **String** | The pmid of the requested resource. |  [optional] |
|**preferredSendMethod** | [**GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerPreferredSendMethod**](GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerPreferredSendMethod.md) |  |  [optional] |
|**printed** | **Boolean** | Indication whether the request is printed. Output parameter. Relevant for lending requests. |  [optional] |
|**publisher** | **String** | Publisher of the requested resource. |  [optional] |
|**readingRoom** | [**GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerReadingRoom**](GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerReadingRoom.md) |  |  [optional] |
|**receiveCost** | **Object** |  |  [optional] |
|**remoteRecordId** | **String** | The remote record id of the requested resource. |  [optional] |
|**reported** | **Boolean** | Indication whether the request is reported. Output parameter. Relevant for lending requests. |  [optional] |
|**requestCost** | **Object** |  |  [optional] |
|**requestId** | **String** | Internal identifier of the resource sharing request in Alma, generated by Alma. Should be used in subsequent queries regarding the request. |  [optional] |
|**requestedLanguage** | [**GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerRequestedLanguage**](GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerRequestedLanguage.md) |  |  [optional] |
|**requestedMedia** | **String** | A description of the requested media. possible values are 1-7 (codes from request media code table), and the codes from &#39;AdditionalRequestedMedia&#39; [code table](https://developers.exlibrisgroup.com/blog/Working-with-the-code-tables-API). The valid values are according to the Requested media definition mapping table. |  [optional] |
|**requester** | [**GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerRequester**](GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerRequester.md) |  |  [optional] |
|**rsNote** | [**List&lt;GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerRsNoteInner&gt;**](GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerRsNoteInner.md) | List of related notes that appear in the Notes tab in the UI.. |  [optional] |
|**seriesTitleNumber** | **String** | The series title number of the requested resource. |  [optional] |
|**shippingCost** | [**GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerShippingCost**](GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerShippingCost.md) |  |  [optional] |
|**source** | **String** | The source of the requested resource. |  [optional] |
|**specificEdition** | **Boolean** | Indication whether edition is used in ISO Protocol and in Locate process. Default is true. Relevant when a book is requested. |  [optional] |
|**startPage** | **String** | The relevant start page of the requested resource. |  [optional] |
|**status** | [**GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerStatus**](GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerStatus.md) |  |  [optional] |
|**suppliedFormat** | [**GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerSuppliedFormat**](GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerSuppliedFormat.md) |  |  [optional] |
|**textEmail** | **String** | Borrowing request: In use with alternative_address only. In use when sending in digital format. Lending request: Requester&#39;s Email. |  [optional] |
|**textPostal1** | **String** | In use with alternative_address only. Not relevant for lending requests. |  [optional] |
|**textPostal2** | **String** | In use with alternative_address only. Not relevant for lending requests. |  [optional] |
|**textPostal3** | **String** | In use with alternative_address only. Not relevant for lending requests. |  [optional] |
|**textPostal4** | **String** | In use with alternative_address only. Not relevant for lending requests. |  [optional] |
|**title** | **String** | Title of the requested resource. Mandatory unless mms_id is supplied. |  [optional] |
|**useAlternativeAddress** | **Boolean** | An indication of whether the delivery should be to an alternative address. Default is false. Not relevant for lending requests. |  [optional] |
|**userRequest** | [**GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerUserRequest**](GetAlmawsV1TaskListsRsLendingRequests200ResponseUserResourceSharingRequestInnerUserRequest.md) |  |  [optional] |
|**volume** | **String** | The volume number of the journal that contains the article. |  [optional] |
|**willingToPay** | **Boolean** | Indication whether patron is willing to pay. Currently not relevant for lending requests. |  [optional] |
|**year** | **String** | Publication date of the requested resource. |  [optional] |



