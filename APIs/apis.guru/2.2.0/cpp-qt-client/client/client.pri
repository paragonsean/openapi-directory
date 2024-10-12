QT += network

HEADERS += \
# Models
    $${PWD}/OAIAPI.h \
    $${PWD}/OAIApiVersion.h \
    $${PWD}/OAIGetProviders_200_response.h \
    $${PWD}/OAIGetServices_200_response.h \
    $${PWD}/OAIMetrics.h \
    $${PWD}/OAIMetrics_thisWeek.h \
# APIs
    $${PWD}/OAIAPIsApi.h \
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
    $${PWD}/OAIAPI.cpp \
    $${PWD}/OAIApiVersion.cpp \
    $${PWD}/OAIGetProviders_200_response.cpp \
    $${PWD}/OAIGetServices_200_response.cpp \
    $${PWD}/OAIMetrics.cpp \
    $${PWD}/OAIMetrics_thisWeek.cpp \
# APIs
    $${PWD}/OAIAPIsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
