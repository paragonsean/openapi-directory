QT += network

HEADERS += \
# Models
    $${PWD}/OAIAPIKeyRequest.h \
    $${PWD}/OAIApplicationInsightsComponentAPIKey.h \
    $${PWD}/OAIApplicationInsightsComponentAPIKeyListResult.h \
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
    $${PWD}/OAIAPIKeyRequest.cpp \
    $${PWD}/OAIApplicationInsightsComponentAPIKey.cpp \
    $${PWD}/OAIApplicationInsightsComponentAPIKeyListResult.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
