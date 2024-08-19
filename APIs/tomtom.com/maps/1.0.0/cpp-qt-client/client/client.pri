QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAICopyrightsApi.h \
    $${PWD}/OAIRasterApi.h \
    $${PWD}/OAIVectorApi.h \
    $${PWD}/OAIWMSWMTSApi.h \
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
# APIs
    $${PWD}/OAICopyrightsApi.cpp \
    $${PWD}/OAIRasterApi.cpp \
    $${PWD}/OAIVectorApi.cpp \
    $${PWD}/OAIWMSWMTSApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
