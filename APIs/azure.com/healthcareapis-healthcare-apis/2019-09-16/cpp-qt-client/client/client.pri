QT += network

HEADERS += \
# Models
    $${PWD}/OAICheckNameAvailabilityParameters.h \
    $${PWD}/OAIErrorDetails.h \
    $${PWD}/OAIErrorDetailsInternal.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationDisplay.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperationResultsDescription.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIServiceAccessPolicyEntry.h \
    $${PWD}/OAIServiceAuthenticationConfigurationInfo.h \
    $${PWD}/OAIServiceCorsConfigurationInfo.h \
    $${PWD}/OAIServiceCosmosDbConfigurationInfo.h \
    $${PWD}/OAIServicesDescription.h \
    $${PWD}/OAIServicesDescriptionListResult.h \
    $${PWD}/OAIServicesNameAvailabilityInfo.h \
    $${PWD}/OAIServicesPatchDescription.h \
    $${PWD}/OAIServicesProperties.h \
# APIs
    $${PWD}/OAICollectionApi.h \
    $${PWD}/OAIProxyApi.h \
    $${PWD}/OAIResourceApi.h \
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
    $${PWD}/OAICheckNameAvailabilityParameters.cpp \
    $${PWD}/OAIErrorDetails.cpp \
    $${PWD}/OAIErrorDetailsInternal.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationDisplay.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperationResultsDescription.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIServiceAccessPolicyEntry.cpp \
    $${PWD}/OAIServiceAuthenticationConfigurationInfo.cpp \
    $${PWD}/OAIServiceCorsConfigurationInfo.cpp \
    $${PWD}/OAIServiceCosmosDbConfigurationInfo.cpp \
    $${PWD}/OAIServicesDescription.cpp \
    $${PWD}/OAIServicesDescriptionListResult.cpp \
    $${PWD}/OAIServicesNameAvailabilityInfo.cpp \
    $${PWD}/OAIServicesPatchDescription.cpp \
    $${PWD}/OAIServicesProperties.cpp \
# APIs
    $${PWD}/OAICollectionApi.cpp \
    $${PWD}/OAIProxyApi.cpp \
    $${PWD}/OAIResourceApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
