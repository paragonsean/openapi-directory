QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAILookUpApi.h \
    $${PWD}/OAIMonitorApi.h \
    $${PWD}/OAIProductDetailsApi.h \
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
    $${PWD}/OAILookUpApi.cpp \
    $${PWD}/OAIMonitorApi.cpp \
    $${PWD}/OAIProductDetailsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
