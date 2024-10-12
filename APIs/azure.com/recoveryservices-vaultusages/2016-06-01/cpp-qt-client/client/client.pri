QT += network

HEADERS += \
# Models
    $${PWD}/OAINameInfo.h \
    $${PWD}/OAIVaultUsage.h \
    $${PWD}/OAIVaultUsageList.h \
# APIs
    $${PWD}/OAIVaultUsagesApi.h \
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
    $${PWD}/OAINameInfo.cpp \
    $${PWD}/OAIVaultUsage.cpp \
    $${PWD}/OAIVaultUsageList.cpp \
# APIs
    $${PWD}/OAIVaultUsagesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
