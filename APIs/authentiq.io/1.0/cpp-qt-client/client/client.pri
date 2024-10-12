QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddress.h \
    $${PWD}/OAIClient.h \
    $${PWD}/OAIOAuth2Error.h \
    $${PWD}/OAIProblemDetail.h \
    $${PWD}/OAISession.h \
    $${PWD}/OAIToken.h \
    $${PWD}/OAIUserInfo.h \
    $${PWD}/OAIUserInfo_aq_location.h \
# APIs
    $${PWD}/OAIAuthenticationApi.h \
    $${PWD}/OAIClientManagementApi.h \
    $${PWD}/OAISessionManagementApi.h \
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
    $${PWD}/OAIClient.cpp \
    $${PWD}/OAIOAuth2Error.cpp \
    $${PWD}/OAIProblemDetail.cpp \
    $${PWD}/OAISession.cpp \
    $${PWD}/OAIToken.cpp \
    $${PWD}/OAIUserInfo.cpp \
    $${PWD}/OAIUserInfo_aq_location.cpp \
# APIs
    $${PWD}/OAIAuthenticationApi.cpp \
    $${PWD}/OAIClientManagementApi.cpp \
    $${PWD}/OAISessionManagementApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
