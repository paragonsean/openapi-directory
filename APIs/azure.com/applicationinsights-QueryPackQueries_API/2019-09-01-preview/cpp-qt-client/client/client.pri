QT += network

HEADERS += \
# Models
    $${PWD}/OAIAzureResourceProperties.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAILogAnalyticsQueryPackQuery.h \
    $${PWD}/OAILogAnalyticsQueryPackQueryListResult.h \
    $${PWD}/OAILogAnalyticsQueryPackQueryProperties.h \
    $${PWD}/OAILogAnalyticsQueryPackQuerySearchProperties.h \
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
    $${PWD}/OAIAzureResourceProperties.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAILogAnalyticsQueryPackQuery.cpp \
    $${PWD}/OAILogAnalyticsQueryPackQueryListResult.cpp \
    $${PWD}/OAILogAnalyticsQueryPackQueryProperties.cpp \
    $${PWD}/OAILogAnalyticsQueryPackQuerySearchProperties.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
