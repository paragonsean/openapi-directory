QT += network

HEADERS += \
# Models
    $${PWD}/OAIContact.h \
    $${PWD}/OAIDID.h \
    $${PWD}/OAIDetailedInvalidParam.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIFirstHref.h \
    $${PWD}/OAILastHref.h \
    $${PWD}/OAILinks.h \
    $${PWD}/OAINextHref.h \
    $${PWD}/OAIPrevHref.h \
    $${PWD}/OAISelfHref.h \
    $${PWD}/OAIUser.h \
    $${PWD}/OAIUserEmbeddedObject.h \
    $${PWD}/OAIUserExtension.h \
    $${PWD}/OAIUserHalResponse.h \
    $${PWD}/OAIUsersEmbeddedObject.h \
    $${PWD}/OAIUsersHalResponse.h \
    $${PWD}/OAIValidationErrorsResponse.h \
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
    $${PWD}/OAIContact.cpp \
    $${PWD}/OAIDID.cpp \
    $${PWD}/OAIDetailedInvalidParam.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIFirstHref.cpp \
    $${PWD}/OAILastHref.cpp \
    $${PWD}/OAILinks.cpp \
    $${PWD}/OAINextHref.cpp \
    $${PWD}/OAIPrevHref.cpp \
    $${PWD}/OAISelfHref.cpp \
    $${PWD}/OAIUser.cpp \
    $${PWD}/OAIUserEmbeddedObject.cpp \
    $${PWD}/OAIUserExtension.cpp \
    $${PWD}/OAIUserHalResponse.cpp \
    $${PWD}/OAIUsersEmbeddedObject.cpp \
    $${PWD}/OAIUsersHalResponse.cpp \
    $${PWD}/OAIValidationErrorsResponse.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
