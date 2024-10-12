QT += network

HEADERS += \
# Models
    $${PWD}/OAICollectInformation.h \
    $${PWD}/OAIErrorFieldType.h \
    $${PWD}/OAIErrorFieldTypeWrapper.h \
    $${PWD}/OAIFieldType.h \
    $${PWD}/OAIGetOnboardingUrlRequest.h \
    $${PWD}/OAIGetOnboardingUrlResponse.h \
    $${PWD}/OAIGetPciUrlRequest.h \
    $${PWD}/OAIGetPciUrlResponse.h \
    $${PWD}/OAIServiceError.h \
    $${PWD}/OAIShowPages.h \
# APIs
    $${PWD}/OAIHostedOnboardingPageApi.h \
    $${PWD}/OAIPCIComplianceQuestionnairePageApi.h \
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
    $${PWD}/OAICollectInformation.cpp \
    $${PWD}/OAIErrorFieldType.cpp \
    $${PWD}/OAIErrorFieldTypeWrapper.cpp \
    $${PWD}/OAIFieldType.cpp \
    $${PWD}/OAIGetOnboardingUrlRequest.cpp \
    $${PWD}/OAIGetOnboardingUrlResponse.cpp \
    $${PWD}/OAIGetPciUrlRequest.cpp \
    $${PWD}/OAIGetPciUrlResponse.cpp \
    $${PWD}/OAIServiceError.cpp \
    $${PWD}/OAIShowPages.cpp \
# APIs
    $${PWD}/OAIHostedOnboardingPageApi.cpp \
    $${PWD}/OAIPCIComplianceQuestionnairePageApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
