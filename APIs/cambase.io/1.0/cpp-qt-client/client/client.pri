QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIModelsApi.h \
    $${PWD}/OAIRecordersApi.h \
    $${PWD}/OAIVendorsApi.h \
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
    $${PWD}/OAIModelsApi.cpp \
    $${PWD}/OAIRecordersApi.cpp \
    $${PWD}/OAIVendorsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
