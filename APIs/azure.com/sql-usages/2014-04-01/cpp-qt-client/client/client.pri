QT += network

HEADERS += \
# Models
    $${PWD}/OAIDatabaseUsage.h \
    $${PWD}/OAIDatabaseUsageListResult.h \
    $${PWD}/OAIServerUsage.h \
    $${PWD}/OAIServerUsageListResult.h \
# APIs
    $${PWD}/OAIDatabasesApi.h \
    $${PWD}/OAIServersApi.h \
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
    $${PWD}/OAIDatabaseUsage.cpp \
    $${PWD}/OAIDatabaseUsageListResult.cpp \
    $${PWD}/OAIServerUsage.cpp \
    $${PWD}/OAIServerUsageListResult.cpp \
# APIs
    $${PWD}/OAIDatabasesApi.cpp \
    $${PWD}/OAIServersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
