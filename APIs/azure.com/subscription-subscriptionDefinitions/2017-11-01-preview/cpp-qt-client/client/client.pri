QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAISubscriptionDefinition.h \
    $${PWD}/OAISubscriptionDefinitionList.h \
    $${PWD}/OAISubscriptionDefinitionProperties.h \
# APIs
    $${PWD}/OAISubscriptionDefinitionsApi.h \
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
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAISubscriptionDefinition.cpp \
    $${PWD}/OAISubscriptionDefinitionList.cpp \
    $${PWD}/OAISubscriptionDefinitionProperties.cpp \
# APIs
    $${PWD}/OAISubscriptionDefinitionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
