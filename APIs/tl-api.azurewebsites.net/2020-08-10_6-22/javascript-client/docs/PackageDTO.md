# Api.PackageDTO

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addOns** | [**[PackageItemDTO]**](PackageItemDTO.md) | Extra articles list added to the given package.              | [optional] 
**addonFee** | **Number** | sum of addon fees. incoming values for this filed will ignore.              | [optional] 
**applyForAllGyms** | **Boolean** | Boolean value to indicate wheather package is available in all the gyms.              | [optional] 
**availableGyms** | [**[GymDTO]**](GymDTO.md) | Gyms list where this package is available.              | [optional] 
**bindingPeriod** | **Number** | Range of period a member is bound to the contract if he/she choose this package.              | [optional] 
**createdDate** | **Date** | Package created DateTime.              | [optional] 
**createdUser** | **String** | Package created user.              | [optional] 
**description** | **String** | Common descriptions about package.If there are more instructions               can be stored as comma separated values.              | [optional] 
**endDate** | **Date** | End date of the package.After that package is not valid for use.              | [optional] 
**expireInMonths** | **Number** | No of months the fixed package is valid for sale              | [optional] 
**features** | **String** | What are the facilities, features available for package.ex:- wifi, ACm etc.Can be stored as comma seperated values.              | [optional] 
**freeMonths** | **Number** | No of months gym member can come without payments.              | [optional] 
**instructionsToGymUsers** | **String** | Instruction to the gym members relevant to the package.              If there are more instructions can be stored as comma seperated values.              | [optional] 
**instructionsToWebUsers** | **String** | Instruction to the MRM members relevant to the package.              If there are more instructions can be stored as comma seperated values.              | [optional] 
**isActive** | **Boolean** | Boolean value to indicate this package is still active or not.              | [optional] 
**isAtg** | **Boolean** | Boolean value to indicate ATG transaction from bank is applicable or not.              | [optional] 
**isAutoRenew** | **Boolean** | Boolean value to indicate the contract will auto renew after expiration               if this package would be chosen.              | [optional] 
**isFirstMonthFree** | **Boolean** | Boolean value to indicate if the first month charges is free.              | [optional] 
**isRegistrationFee** | **Boolean** | Boolean value to indicate this package has registration fee or not.              | [optional] 
**isRestAmount** | **Boolean** | Boolean value to indicate rest amount is applicable or not.              | [optional] 
**isShownInMobile** | **Boolean** | Boolean value to indicate package is visible in Mobile App or not.              | [optional] 
**isSponsorPackage** | **Boolean** | Boolean value to indicate package can be sponsored or not by other party.              | [optional] 
**maximumGiveAwayRestAmount** | **Number** | If a member join the gym middle of a month via this package,               what is the maximum amount of price can be neglected from payment from the member.              | [optional] 
**memberCanAddAddOns** | **Boolean** | Boolean value to indicate member can add extra addons he wish if he choose this package.              | [optional] 
**memberCanLeaveWithinFreePeriod** | **Boolean** | Boolean value to indicate if member can leave from contract within               free period if he/she choose this package.              | [optional] 
**memberCanRemoveAddOns** | **Boolean** | Boolean value to indicate member can remove already added addons if he choose this package.              | [optional] 
**modifiedDate** | **Date** | Package last modified DateTime.              | [optional] 
**modifiedUser** | **String** | Package last modified user.              | [optional] 
**monthlyFee** | **Number** | Monthly installment fee if package is not fixed visit. addition of the servicefee and addon fees divided by binding period.              read only              | [optional] 
**nextPackageNumber** | **Number** | Next Package the contract continue after the binding period of this package.              | [optional] 
**numberOfInstallments** | **Number** | Maximum Number of installment a member can divide the package price/cost to pay.              | [optional] 
**numberOfVisits** | **Number** | If package is fixed visit type, then how many visits are available for this package.              | [optional] 
**packageId** | **Number** |  | [optional] 
**packageName** | **String** |  | 
**packageNumber** | **String** |  | [optional] 
**packageType** | **String** | Package type can be either fixed visit or unlimited.              | 
**perVisitPrice** | **Number** | Cost/Price of the single visit to gym.              | [optional] 
**registrationFee** | **Number** | Registartion fee for the package at a gym.              read only              | 
**serviceFee** | **Number** | total Service charge of the package for entire period.              | 
**shownInWeb** | **Boolean** | Boolean value to show this package in MRM system or not.              | [optional] 
**startDate** | **Date** | Start date of the package.              | [optional] 
**tags** | **String** | Comma separated string values in case of need of maintain some labels kind of               stuff relevant to the package.              | [optional] 
**totalPrice** | **Number** | total price for the package including Addon fees, service fee and registration fee. incoming values for this field will ignore.              | [optional] 


