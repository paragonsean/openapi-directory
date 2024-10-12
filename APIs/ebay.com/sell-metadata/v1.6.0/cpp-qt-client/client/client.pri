QT += network

HEADERS += \
# Models
    $${PWD}/OAIAutomotivePartsCompatibilityPolicy.h \
    $${PWD}/OAIAutomotivePartsCompatibilityPolicyResponse.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorParameter.h \
    $${PWD}/OAIExtendedProducerResponsibility.h \
    $${PWD}/OAIExtendedProducerResponsibilityPolicy.h \
    $${PWD}/OAIExtendedProducerResponsibilityPolicyResponse.h \
    $${PWD}/OAIHazardStatement.h \
    $${PWD}/OAIHazardousMaterialDetailsResponse.h \
    $${PWD}/OAIItemCondition.h \
    $${PWD}/OAIItemConditionPolicy.h \
    $${PWD}/OAIItemConditionPolicyResponse.h \
    $${PWD}/OAIListingStructurePolicy.h \
    $${PWD}/OAIListingStructurePolicyResponse.h \
    $${PWD}/OAINegotiatedPricePolicy.h \
    $${PWD}/OAINegotiatedPricePolicyResponse.h \
    $${PWD}/OAIPictogram.h \
    $${PWD}/OAIReturnPolicy.h \
    $${PWD}/OAIReturnPolicyDetails.h \
    $${PWD}/OAIReturnPolicyResponse.h \
    $${PWD}/OAISalesTaxJurisdiction.h \
    $${PWD}/OAISalesTaxJurisdictions.h \
    $${PWD}/OAISignalWord.h \
    $${PWD}/OAITimeDuration.h \
# APIs
    $${PWD}/OAICountryApi.h \
    $${PWD}/OAIMarketplaceApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIAutomotivePartsCompatibilityPolicy.cpp \
    $${PWD}/OAIAutomotivePartsCompatibilityPolicyResponse.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorParameter.cpp \
    $${PWD}/OAIExtendedProducerResponsibility.cpp \
    $${PWD}/OAIExtendedProducerResponsibilityPolicy.cpp \
    $${PWD}/OAIExtendedProducerResponsibilityPolicyResponse.cpp \
    $${PWD}/OAIHazardStatement.cpp \
    $${PWD}/OAIHazardousMaterialDetailsResponse.cpp \
    $${PWD}/OAIItemCondition.cpp \
    $${PWD}/OAIItemConditionPolicy.cpp \
    $${PWD}/OAIItemConditionPolicyResponse.cpp \
    $${PWD}/OAIListingStructurePolicy.cpp \
    $${PWD}/OAIListingStructurePolicyResponse.cpp \
    $${PWD}/OAINegotiatedPricePolicy.cpp \
    $${PWD}/OAINegotiatedPricePolicyResponse.cpp \
    $${PWD}/OAIPictogram.cpp \
    $${PWD}/OAIReturnPolicy.cpp \
    $${PWD}/OAIReturnPolicyDetails.cpp \
    $${PWD}/OAIReturnPolicyResponse.cpp \
    $${PWD}/OAISalesTaxJurisdiction.cpp \
    $${PWD}/OAISalesTaxJurisdictions.cpp \
    $${PWD}/OAISignalWord.cpp \
    $${PWD}/OAITimeDuration.cpp \
# APIs
    $${PWD}/OAICountryApi.cpp \
    $${PWD}/OAIMarketplaceApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
