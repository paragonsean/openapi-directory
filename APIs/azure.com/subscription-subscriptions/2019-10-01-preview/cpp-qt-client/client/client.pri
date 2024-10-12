QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdPrincipal.h \
    $${PWD}/OAICanceledSubscriptionId.h \
    $${PWD}/OAIEnabledSubscriptionId.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIModernCspSubscriptionCreationParameters.h \
    $${PWD}/OAIModernSubscriptionCreationParameters.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIRenamedSubscriptionId.h \
    $${PWD}/OAISubscriptionCreationParameters.h \
    $${PWD}/OAISubscriptionCreationResult.h \
    $${PWD}/OAISubscriptionName.h \
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
    $${PWD}/OAIAdPrincipal.cpp \
    $${PWD}/OAICanceledSubscriptionId.cpp \
    $${PWD}/OAIEnabledSubscriptionId.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIModernCspSubscriptionCreationParameters.cpp \
    $${PWD}/OAIModernSubscriptionCreationParameters.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIRenamedSubscriptionId.cpp \
    $${PWD}/OAISubscriptionCreationParameters.cpp \
    $${PWD}/OAISubscriptionCreationResult.cpp \
    $${PWD}/OAISubscriptionName.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
