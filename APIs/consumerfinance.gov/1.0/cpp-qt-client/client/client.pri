QT += network

HEADERS += \
# Models
    $${PWD}/OAIQueryResponse.h \
# APIs
    $${PWD}/OAIDataApi.h \
    $${PWD}/OAIHmdaApi.h \
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
    $${PWD}/OAIQueryResponse.cpp \
# APIs
    $${PWD}/OAIDataApi.cpp \
    $${PWD}/OAIHmdaApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
