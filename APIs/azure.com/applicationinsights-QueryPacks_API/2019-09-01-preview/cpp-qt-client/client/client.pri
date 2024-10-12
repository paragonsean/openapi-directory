QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAILogAnalyticsQueryPack.h \
    $${PWD}/OAILogAnalyticsQueryPackListResult.h \
    $${PWD}/OAILogAnalyticsQueryPackProperties.h \
    $${PWD}/OAIQueryPacksResource.h \
    $${PWD}/OAITagsResource.h \
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
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAILogAnalyticsQueryPack.cpp \
    $${PWD}/OAILogAnalyticsQueryPackListResult.cpp \
    $${PWD}/OAILogAnalyticsQueryPackProperties.cpp \
    $${PWD}/OAIQueryPacksResource.cpp \
    $${PWD}/OAITagsResource.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
