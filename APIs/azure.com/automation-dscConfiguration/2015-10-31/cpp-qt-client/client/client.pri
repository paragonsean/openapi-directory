QT += network

HEADERS += \
# Models
    $${PWD}/OAIContentHash.h \
    $${PWD}/OAIContentSource.h \
    $${PWD}/OAIDscConfiguration.h \
    $${PWD}/OAIDscConfigurationCreateOrUpdateParameters.h \
    $${PWD}/OAIDscConfigurationCreateOrUpdateProperties.h \
    $${PWD}/OAIDscConfigurationListResult.h \
    $${PWD}/OAIDscConfigurationParameter.h \
    $${PWD}/OAIDscConfigurationProperties.h \
    $${PWD}/OAIDscConfigurationUpdateParameters.h \
    $${PWD}/OAIDscConfiguration_ListByAutomationAccount_default_response.h \
# APIs
    $${PWD}/OAIDscConfigurationApi.h \
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
    $${PWD}/OAIContentHash.cpp \
    $${PWD}/OAIContentSource.cpp \
    $${PWD}/OAIDscConfiguration.cpp \
    $${PWD}/OAIDscConfigurationCreateOrUpdateParameters.cpp \
    $${PWD}/OAIDscConfigurationCreateOrUpdateProperties.cpp \
    $${PWD}/OAIDscConfigurationListResult.cpp \
    $${PWD}/OAIDscConfigurationParameter.cpp \
    $${PWD}/OAIDscConfigurationProperties.cpp \
    $${PWD}/OAIDscConfigurationUpdateParameters.cpp \
    $${PWD}/OAIDscConfiguration_ListByAutomationAccount_default_response.cpp \
# APIs
    $${PWD}/OAIDscConfigurationApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
