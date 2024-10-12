# HostedOnboardingApi.GetOnboardingUrlRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountHolderCode** | **String** | The account holder code you provided when you created the account holder. | 
**collectInformation** | [**CollectInformation**](CollectInformation.md) | Contains indicators whether the page should only collect information for specific [KYC checks](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-checks). By default, the page collects information for all KYC checks that apply to the [legal entity type](https://docs.adyen.com/marketplaces-and-platforms/classic/account-holders-and-accounts#legal-entity-types). | [optional] 
**editMode** | **Boolean** | Indicates if editing checks is allowed even if all the checks have passed. | [optional] 
**mobileOAuthCallbackUrl** | **String** | The URL to which the account holder is redirected after completing an OAuth authentication with a bank through Trustly/PayMyBank. | [optional] 
**platformName** | **String** | The platform name which will show up in the welcome page. | [optional] 
**returnUrl** | **String** | The URL where the account holder will be redirected back to after they complete the onboarding, or if their session times out. Maximum length of 500 characters. If you don&#39;t provide this, the account holder will be redirected back to the default return URL configured in your platform account. | [optional] 
**shopperLocale** | **String** | The language to be used in the page, specified by a combination of a language and country code. For example, **pt-BR**.   If not specified in the request or if the language is not supported, the page uses the browser language. If the browser language is not supported, the page uses **en-US** by default.  For a list of supported languages, refer to [Change the page language](https://docs.adyen.com/marketplaces-and-platforms/classic/hosted-onboarding-page/customize-experience#change-page-language). | [optional] 
**showPages** | [**ShowPages**](ShowPages.md) | Contains indicators whether specific pages must be shown to the account holder. | [optional] 


