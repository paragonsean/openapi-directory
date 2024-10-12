

# PackageSearchDTO

The PackageSearchDTO Class. Contains relevant fields of PackageSearch DTO by masking actual Package entity's fields in application.                

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeStatus** | **Boolean** | Active Status  |  [optional] |
|**addonFee** | **BigDecimal** | sum of addon fees. incoming values for this filed will ignore.              |  [optional] |
|**applyForAllGyms** | **Boolean** | Boolean value to indicate wheather package is available in all the gyms.              |  [optional] |
|**bindingPeriod** | **Integer** | Range of period a member is bound to the contract if he/she choose this package.              |  [optional] |
|**createdDate** | **OffsetDateTime** | Package created DateTime.              |  [optional] |
|**createdUser** | **String** | Package created user.              |  [optional] |
|**description** | **String** | Common descriptions about package.If there are more instructions can be stored as comma separated values.              |  [optional] |
|**features** | **String** | What are the facilities, features available for package.ex:- wifi, ACm etc.Can be stored as comma seperated values.              |  [optional] |
|**freeMonths** | **Integer** | No of months gym member can come without payments.              |  [optional] |
|**memberCanRemoveAddOns** | **Boolean** | Boolean value to indicate member can remove already added addons if he choose this package.              |  [optional] |
|**modifiedDate** | **OffsetDateTime** | Package last modified DateTime.              |  [optional] |
|**modifiedUser** | **String** | Package last modified user.              |  [optional] |
|**monthlyFee** | **BigDecimal** | Monthly installment fee if package is not fixed visit. addition of the servicefee and addon fees divided by binding period.              |  [optional] |
|**numberOfVisits** | **Integer** | No of visits for fixed package  |  [optional] |
|**packageId** | **Integer** |  |  [optional] |
|**packageName** | **String** |  |  [optional] |
|**packageNumber** | **Integer** |  |  [optional] |
|**packageType** | **String** | Package type can be either fixed visit or unlimited.              |  [optional] |
|**registrationFee** | **BigDecimal** | Registartion fee for the package at a gym.              |  [optional] |
|**serviceFee** | **BigDecimal** | total Service charge of the package for entire period.              |  [optional] |
|**tags** | **String** | Comma separated string values in case of need of maintain some labels kind of stuff relevant to the package.              |  [optional] |
|**totalCount** | **Integer** | total number of recode for particular search  |  [optional] |
|**totalPrice** | **BigDecimal** | total price for the package including Addon fees, service fee and registration fee. incoming values for this field will ignore.              |  [optional] |



