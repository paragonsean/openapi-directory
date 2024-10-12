QT += network

HEADERS += \
# Models
    $${PWD}/OAIApplicationInsightsComponentProactiveDetectionConfiguration.h \
    $${PWD}/OAIApplicationInsightsComponentProactiveDetectionConfigurationProperties.h \
    $${PWD}/OAIApplicationInsightsComponentProactiveDetectionConfigurationProperties_RuleDefinitions.h \
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
    $${PWD}/OAIApplicationInsightsComponentProactiveDetectionConfiguration.cpp \
    $${PWD}/OAIApplicationInsightsComponentProactiveDetectionConfigurationProperties.cpp \
    $${PWD}/OAIApplicationInsightsComponentProactiveDetectionConfigurationProperties_RuleDefinitions.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
