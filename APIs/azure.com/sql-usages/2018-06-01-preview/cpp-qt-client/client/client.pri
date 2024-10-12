QT += network

HEADERS += \
# Models
    $${PWD}/OAIName.h \
    $${PWD}/OAIUsage.h \
    $${PWD}/OAIUsageListResult.h \
# APIs
    $${PWD}/OAIUsagesApi.h \
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
    $${PWD}/OAIName.cpp \
    $${PWD}/OAIUsage.cpp \
    $${PWD}/OAIUsageListResult.cpp \
# APIs
    $${PWD}/OAIUsagesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
