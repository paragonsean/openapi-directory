QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddress.h \
    $${PWD}/OAIContact.h \
    $${PWD}/OAIDomain.h \
    $${PWD}/OAIDomainAvailablilityCheckResult.h \
    $${PWD}/OAIDomainCollection.h \
    $${PWD}/OAIDomainControlCenterSsoRequest.h \
    $${PWD}/OAIDomainOwnershipIdentifier.h \
    $${PWD}/OAIDomainOwnershipIdentifierCollection.h \
    $${PWD}/OAIDomainPatchResource.h \
    $${PWD}/OAIDomainPurchaseConsent.h \
    $${PWD}/OAIDomainRecommendationSearchParameters.h \
    $${PWD}/OAIDomains_CheckAvailability_default_response.h \
    $${PWD}/OAIDomains_CheckAvailability_default_response_error.h \
    $${PWD}/OAIDomains_CheckAvailability_default_response_error_details_inner.h \
    $${PWD}/OAIDomains_CheckAvailability_request.h \
    $${PWD}/OAIHostName.h \
    $${PWD}/OAINameIdentifierCollection.h \
# APIs
    $${PWD}/OAIDomainsApi.h \
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
    $${PWD}/OAIAddress.cpp \
    $${PWD}/OAIContact.cpp \
    $${PWD}/OAIDomain.cpp \
    $${PWD}/OAIDomainAvailablilityCheckResult.cpp \
    $${PWD}/OAIDomainCollection.cpp \
    $${PWD}/OAIDomainControlCenterSsoRequest.cpp \
    $${PWD}/OAIDomainOwnershipIdentifier.cpp \
    $${PWD}/OAIDomainOwnershipIdentifierCollection.cpp \
    $${PWD}/OAIDomainPatchResource.cpp \
    $${PWD}/OAIDomainPurchaseConsent.cpp \
    $${PWD}/OAIDomainRecommendationSearchParameters.cpp \
    $${PWD}/OAIDomains_CheckAvailability_default_response.cpp \
    $${PWD}/OAIDomains_CheckAvailability_default_response_error.cpp \
    $${PWD}/OAIDomains_CheckAvailability_default_response_error_details_inner.cpp \
    $${PWD}/OAIDomains_CheckAvailability_request.cpp \
    $${PWD}/OAIHostName.cpp \
    $${PWD}/OAINameIdentifierCollection.cpp \
# APIs
    $${PWD}/OAIDomainsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
