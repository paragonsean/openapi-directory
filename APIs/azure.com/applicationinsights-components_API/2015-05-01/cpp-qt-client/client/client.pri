QT += network

HEADERS += \
# Models
    $${PWD}/OAIApplicationInsightsComponent.h \
    $${PWD}/OAIApplicationInsightsComponentListResult.h \
    $${PWD}/OAIApplicationInsightsComponentProperties.h \
    $${PWD}/OAIComponentPurgeBody.h \
    $${PWD}/OAIComponentPurgeBodyFilters.h \
    $${PWD}/OAIComponentPurgeResponse.h \
    $${PWD}/OAIComponentPurgeStatusResponse.h \
    $${PWD}/OAIComponentsResource.h \
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
    $${PWD}/OAIApplicationInsightsComponent.cpp \
    $${PWD}/OAIApplicationInsightsComponentListResult.cpp \
    $${PWD}/OAIApplicationInsightsComponentProperties.cpp \
    $${PWD}/OAIComponentPurgeBody.cpp \
    $${PWD}/OAIComponentPurgeBodyFilters.cpp \
    $${PWD}/OAIComponentPurgeResponse.cpp \
    $${PWD}/OAIComponentPurgeStatusResponse.cpp \
    $${PWD}/OAIComponentsResource.cpp \
    $${PWD}/OAITagsResource.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
