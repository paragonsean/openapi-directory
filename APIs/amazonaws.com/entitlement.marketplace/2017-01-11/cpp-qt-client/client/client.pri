QT += network

HEADERS += \
# Models
    $${PWD}/OAIEntitlement.h \
    $${PWD}/OAIEntitlementValue.h \
    $${PWD}/OAIEntitlement_Value.h \
    $${PWD}/OAIGetEntitlementFilterName.h \
    $${PWD}/OAIGetEntitlementsRequest.h \
    $${PWD}/OAIGetEntitlementsResult.h \
    $${PWD}/OAIInternalServiceErrorException.h \
    $${PWD}/OAIInvalidParameterException.h \
    $${PWD}/OAIThrottlingException.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIEntitlement.cpp \
    $${PWD}/OAIEntitlementValue.cpp \
    $${PWD}/OAIEntitlement_Value.cpp \
    $${PWD}/OAIGetEntitlementFilterName.cpp \
    $${PWD}/OAIGetEntitlementsRequest.cpp \
    $${PWD}/OAIGetEntitlementsResult.cpp \
    $${PWD}/OAIInternalServiceErrorException.cpp \
    $${PWD}/OAIInvalidParameterException.cpp \
    $${PWD}/OAIThrottlingException.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
