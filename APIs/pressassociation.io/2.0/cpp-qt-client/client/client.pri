QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIAssetApi.h \
    $${PWD}/OAICatalogueApi.h \
    $${PWD}/OAIChannelApi.h \
    $${PWD}/OAIContributorApi.h \
    $${PWD}/OAIFeatureApi.h \
    $${PWD}/OAIPlatformApi.h \
    $${PWD}/OAIScheduleApi.h \
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
    $${PWD}/OAIAssetApi.cpp \
    $${PWD}/OAICatalogueApi.cpp \
    $${PWD}/OAIChannelApi.cpp \
    $${PWD}/OAIContributorApi.cpp \
    $${PWD}/OAIFeatureApi.cpp \
    $${PWD}/OAIPlatformApi.cpp \
    $${PWD}/OAIScheduleApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
