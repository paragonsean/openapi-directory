QT += network

HEADERS += \
# Models
    $${PWD}/OAIAPIError.h \
    $${PWD}/OAIEntireDetectResponse.h \
    $${PWD}/OAILastDetectResponse.h \
    $${PWD}/OAIPoint.h \
    $${PWD}/OAIRequest.h \
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
    $${PWD}/OAIAPIError.cpp \
    $${PWD}/OAIEntireDetectResponse.cpp \
    $${PWD}/OAILastDetectResponse.cpp \
    $${PWD}/OAIPoint.cpp \
    $${PWD}/OAIRequest.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
