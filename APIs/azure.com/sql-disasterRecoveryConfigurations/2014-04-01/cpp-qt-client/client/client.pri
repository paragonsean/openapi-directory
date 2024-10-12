QT += network

HEADERS += \
# Models
    $${PWD}/OAIDisasterRecoveryConfiguration.h \
    $${PWD}/OAIDisasterRecoveryConfigurationListResult.h \
    $${PWD}/OAIDisasterRecoveryConfigurationProperties.h \
# APIs
    $${PWD}/OAIDisasterRecoveryConfigurationsApi.h \
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
    $${PWD}/OAIDisasterRecoveryConfiguration.cpp \
    $${PWD}/OAIDisasterRecoveryConfigurationListResult.cpp \
    $${PWD}/OAIDisasterRecoveryConfigurationProperties.cpp \
# APIs
    $${PWD}/OAIDisasterRecoveryConfigurationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
