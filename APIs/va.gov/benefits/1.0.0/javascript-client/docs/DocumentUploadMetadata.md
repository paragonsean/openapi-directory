# BenefitsIntake.DocumentUploadMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**businessLine** | **String** | Optional parameter (can be missing or empty). The values are:&lt;br&gt;&lt;br&gt; CMP - Compensation requests such as those related to disability, unemployment, and pandemic claims&lt;br&gt;&lt;br&gt; PMC - Pension requests including survivor’s pension&lt;br&gt;&lt;br&gt; INS - Insurance such as life insurance, disability insurance, and other health insurance&lt;br&gt;&lt;br&gt; EDU - Education benefits, programs, and affiliations&lt;br&gt;&lt;br&gt; VRE - Veteran Readiness &amp; Employment such as employment questionnaires, employment discrimination, employment verification&lt;br&gt;&lt;br&gt; BVA - Board of Veteran Appeals&lt;br&gt;&lt;br&gt; FID - Fiduciary / financial appointee, including family member benefits&lt;br&gt;&lt;br&gt; NCA - National Cemetery Administration&lt;br&gt;&lt;br&gt; OTH - Other (this value if used, will be treated as CMP)&lt;br&gt;  | [optional] 
**docType** | **String** | VBA form number of the document | [optional] 
**fileNumber** | **String** | The Veteran&#39;s file number is exactly 9 digits with no alpha characters, hyphens, spaces or punctuation. In most cases, this is the Veteran&#39;s SSN but may also be an 8 digit BIRL number. If no file number has been established or if it is unknown, the application should use the Veteran&#39;s SSN and the file number will be associated with the submission later in the process. Incorrect file numbers can cause delays. | 
**source** | **String** | System, installation, or entity submitting the document | 
**veteranFirstName** | **String** | Veteran first name. Cannot be missing or empty or longer than 50 characters. Only upper/lower case letters, hyphens(-), spaces and forward-slash(/) allowed. | 
**veteranLastName** | **String** | Veteran last name. Cannot be missing or empty or longer than 50 characters. Only upper/lower case letters, hyphens(-), spaces and forward-slash(/) allowed. | 
**zipCode** | **String** | Veteran zip code. Either five digits (XXXXX) or five digits then four digits separated by a hyphen (XXXXX-XXXX). Use &#39;00000&#39; for Veterans with non-US addresses. | 



## Enum: BusinessLineEnum


* `CMP` (value: `"CMP"`)

* `PMC` (value: `"PMC"`)

* `INS` (value: `"INS"`)

* `EDU` (value: `"EDU"`)

* `VRE` (value: `"VRE"`)

* `BVA` (value: `"BVA"`)

* `FID` (value: `"FID"`)

* `NCA` (value: `"NCA"`)

* `OTH` (value: `"OTH"`)




