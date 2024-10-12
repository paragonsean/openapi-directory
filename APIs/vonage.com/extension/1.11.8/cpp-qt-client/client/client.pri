QT += network

HEADERS += \
# Models
    $${PWD}/OAIBasicUser.h \
    $${PWD}/OAIDID.h \
    $${PWD}/OAIDetailedInvalidParam.h \
    $${PWD}/OAIEndUserRoute.h \
    $${PWD}/OAIEndUserRouteEmbeddedObject.h \
    $${PWD}/OAIEndUserRouteHalResponse.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIFirstHref.h \
    $${PWD}/OAILastHref.h \
    $${PWD}/OAILine.h \
    $${PWD}/OAILinks.h \
    $${PWD}/OAINextHref.h \
    $${PWD}/OAIPrevHref.h \
    $${PWD}/OAISelfHref.h \
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
    $${PWD}/OAIBasicUser.cpp \
    $${PWD}/OAIDID.cpp \
    $${PWD}/OAIDetailedInvalidParam.cpp \
    $${PWD}/OAIEndUserRoute.cpp \
    $${PWD}/OAIEndUserRouteEmbeddedObject.cpp \
    $${PWD}/OAIEndUserRouteHalResponse.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIFirstHref.cpp \
    $${PWD}/OAILastHref.cpp \
    $${PWD}/OAILine.cpp \
    $${PWD}/OAILinks.cpp \
    $${PWD}/OAINextHref.cpp \
    $${PWD}/OAIPrevHref.cpp \
    $${PWD}/OAISelfHref.cpp \
    $${PWD}/OAIValidationErrorsResponse.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
