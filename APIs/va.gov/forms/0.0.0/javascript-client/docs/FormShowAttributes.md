# VaForms.FormShowAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benefitCategories** | [**[FormShowAttributesBenefitCategoriesInner]**](FormShowAttributesBenefitCategoriesInner.md) | Listing of benefit categories and match | [optional] 
**createdAt** | **Date** | Internal field for VA.gov use | [optional] 
**deletedAt** | **Date** | The timestamp at which the form was deleted | [optional] 
**firstIssuedOn** | **Date** | The date the form first became available | [optional] 
**formDetailsUrl** | **String** | Location on www.va.gov of the info page for this form | [optional] 
**formName** | **String** | Name of the VA Form | [optional] 
**formToolIntro** | **String** | Introductory text describing the VA online tool for this form | [optional] 
**formToolUrl** | **String** | Location of the online tool for this form | [optional] 
**formType** | **String** | VA Type of the form | [optional] 
**formUsage** | **String** | A description of how the form is to be used | [optional] 
**language** | **String** | Language code of the form | [optional] 
**lastRevisionOn** | **Date** | The date the form was last updated | [optional] 
**pages** | **Number** | Number of pages contained in the form | [optional] 
**relatedForms** | **[String]** | A listing of other forms that relate to current form | [optional] 
**sha256** | **String** | A sha256 hash of the form contents | [optional] 
**title** | **String** | Title of the form as given by VA | [optional] 
**url** | **String** | Web location of the form | [optional] 
**vaFormAdministration** | **String** | The VA organization that administers the form | [optional] 
**validPdf** | **Boolean** | A flag indicating whether the form url was confirmed as a valid download | [optional] 
**versions** | [**[FormShowAttributesVersionsInner]**](FormShowAttributesVersionsInner.md) | The version history of revisions to the form | [optional] 


