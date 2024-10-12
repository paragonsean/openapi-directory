QT += network

HEADERS += \
# Models
    $${PWD}/OAIAllRequestTypesExample.h \
    $${PWD}/OAIAllResponseTypesExample.h \
    $${PWD}/OAIAuthenticationMessage.h \
    $${PWD}/OAIConnectionMessage.h \
    $${PWD}/OAIHeartbeatMessage.h \
    $${PWD}/OAIKeyLineDefinition.h \
    $${PWD}/OAIKeyLineSelection.h \
    $${PWD}/OAIMarketChange.h \
    $${PWD}/OAIMarketChangeMessage.h \
    $${PWD}/OAIMarketDataFilter.h \
    $${PWD}/OAIMarketDefinition.h \
    $${PWD}/OAIMarketFilter.h \
    $${PWD}/OAIMarketSubscriptionMessage.h \
    $${PWD}/OAIOrder.h \
    $${PWD}/OAIOrderChangeMessage.h \
    $${PWD}/OAIOrderFilter.h \
    $${PWD}/OAIOrderMarketChange.h \
    $${PWD}/OAIOrderRunnerChange.h \
    $${PWD}/OAIOrderSubscriptionMessage.h \
    $${PWD}/OAIPriceLadderDefinition.h \
    $${PWD}/OAIRequestMessage.h \
    $${PWD}/OAIResponseMessage.h \
    $${PWD}/OAIRunnerChange.h \
    $${PWD}/OAIRunnerDefinition.h \
    $${PWD}/OAIStatusMessage.h \
    $${PWD}/OAIStrategyMatchChange.h \
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
    $${PWD}/OAIAllRequestTypesExample.cpp \
    $${PWD}/OAIAllResponseTypesExample.cpp \
    $${PWD}/OAIAuthenticationMessage.cpp \
    $${PWD}/OAIConnectionMessage.cpp \
    $${PWD}/OAIHeartbeatMessage.cpp \
    $${PWD}/OAIKeyLineDefinition.cpp \
    $${PWD}/OAIKeyLineSelection.cpp \
    $${PWD}/OAIMarketChange.cpp \
    $${PWD}/OAIMarketChangeMessage.cpp \
    $${PWD}/OAIMarketDataFilter.cpp \
    $${PWD}/OAIMarketDefinition.cpp \
    $${PWD}/OAIMarketFilter.cpp \
    $${PWD}/OAIMarketSubscriptionMessage.cpp \
    $${PWD}/OAIOrder.cpp \
    $${PWD}/OAIOrderChangeMessage.cpp \
    $${PWD}/OAIOrderFilter.cpp \
    $${PWD}/OAIOrderMarketChange.cpp \
    $${PWD}/OAIOrderRunnerChange.cpp \
    $${PWD}/OAIOrderSubscriptionMessage.cpp \
    $${PWD}/OAIPriceLadderDefinition.cpp \
    $${PWD}/OAIRequestMessage.cpp \
    $${PWD}/OAIResponseMessage.cpp \
    $${PWD}/OAIRunnerChange.cpp \
    $${PWD}/OAIRunnerDefinition.cpp \
    $${PWD}/OAIStatusMessage.cpp \
    $${PWD}/OAIStrategyMatchChange.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
