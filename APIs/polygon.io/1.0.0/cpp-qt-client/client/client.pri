QT += network

HEADERS += \
# Models
    $${PWD}/OAIAggregate.h \
    $${PWD}/OAICompany.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIForex.h \
    $${PWD}/OAILastForexQuote.h \
    $${PWD}/OAILastForexTrade.h \
    $${PWD}/OAILastQuote.h \
    $${PWD}/OAILastTrade.h \
    $${PWD}/OAIQuote.h \
    $${PWD}/OAITrade.h \
    $${PWD}/OAI_v1_historic_agg__size___symbol___date__get_200_response.h \
    $${PWD}/OAI_v1_historic_forex__from___to___date__get_200_response.h \
    $${PWD}/OAI_v1_historic_quotes__symbol___date__get_200_response.h \
    $${PWD}/OAI_v1_historic_trades__symbol___date__get_200_response.h \
    $${PWD}/OAI_v1_last_currencies__from___to__get_200_response.h \
    $${PWD}/OAI_v1_last_quote_currencies__from___to__get_200_response.h \
    $${PWD}/OAI_v1_last_quote_stocks__symbol__get_200_response.h \
    $${PWD}/OAI_v1_last_stocks__symbol__get_200_response.h \
# APIs
    $${PWD}/OAICurrenciesApi.h \
    $${PWD}/OAIStocksApi.h \
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
    $${PWD}/OAIAggregate.cpp \
    $${PWD}/OAICompany.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIForex.cpp \
    $${PWD}/OAILastForexQuote.cpp \
    $${PWD}/OAILastForexTrade.cpp \
    $${PWD}/OAILastQuote.cpp \
    $${PWD}/OAILastTrade.cpp \
    $${PWD}/OAIQuote.cpp \
    $${PWD}/OAITrade.cpp \
    $${PWD}/OAI_v1_historic_agg__size___symbol___date__get_200_response.cpp \
    $${PWD}/OAI_v1_historic_forex__from___to___date__get_200_response.cpp \
    $${PWD}/OAI_v1_historic_quotes__symbol___date__get_200_response.cpp \
    $${PWD}/OAI_v1_historic_trades__symbol___date__get_200_response.cpp \
    $${PWD}/OAI_v1_last_currencies__from___to__get_200_response.cpp \
    $${PWD}/OAI_v1_last_quote_currencies__from___to__get_200_response.cpp \
    $${PWD}/OAI_v1_last_quote_stocks__symbol__get_200_response.cpp \
    $${PWD}/OAI_v1_last_stocks__symbol__get_200_response.cpp \
# APIs
    $${PWD}/OAICurrenciesApi.cpp \
    $${PWD}/OAIStocksApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
