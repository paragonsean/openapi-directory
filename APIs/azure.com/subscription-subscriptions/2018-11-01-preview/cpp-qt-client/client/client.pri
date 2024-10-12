QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdPrincipal.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIModernCspSubscriptionCreationParameters.h \
    $${PWD}/OAIModernSubscriptionCreationParameters.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAISubscriptionCreationResult.h \
    $${PWD}/OAISubscriptionOperation.h \
    $${PWD}/OAISubscriptionOperationListResult.h \
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
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIModernCspSubscriptionCreationParameters.cpp \
    $${PWD}/OAIModernSubscriptionCreationParameters.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAISubscriptionCreationResult.cpp \
    $${PWD}/OAISubscriptionOperation.cpp \
    $${PWD}/OAISubscriptionOperationListResult.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
