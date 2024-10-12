QT += network

HEADERS += \
# Models
    $${PWD}/OAIDisplay.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationList.h \
    $${PWD}/OAIResource.h \
# APIs
    $${PWD}/OAIUpdatesApi.h \
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
    $${PWD}/OAIDisplay.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationList.cpp \
    $${PWD}/OAIResource.cpp \
# APIs
    $${PWD}/OAIUpdatesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
