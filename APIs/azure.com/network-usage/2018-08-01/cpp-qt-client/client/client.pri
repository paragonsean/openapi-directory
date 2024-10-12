QT += network

HEADERS += \
# Models
    $${PWD}/OAIUsage.h \
    $${PWD}/OAIUsageName.h \
    $${PWD}/OAIUsagesListResult.h \
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
    $${PWD}/OAIUsage.cpp \
    $${PWD}/OAIUsageName.cpp \
    $${PWD}/OAIUsagesListResult.cpp \
# APIs
    $${PWD}/OAIUsagesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
