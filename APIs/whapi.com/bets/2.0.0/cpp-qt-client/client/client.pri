QT += network

HEADERS += \
# Models
    $${PWD}/OAIBet.h \
    $${PWD}/OAIBetDelayed.h \
    $${PWD}/OAIBetHistoryResponse.h \
    $${PWD}/OAIBetPlaced.h \
    $${PWD}/OAIBetSlipRequest.h \
    $${PWD}/OAIBetSlipResponse.h \
    $${PWD}/OAIBetslipbet.h \
    $${PWD}/OAIBetslipleg.h \
    $${PWD}/OAIBetslippart.h \
    $${PWD}/OAICashInResponse.h \
    $${PWD}/OAIComplexBetRequestBody.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrors.h \
    $${PWD}/OAIFreeBetDetail.h \
    $${PWD}/OAILeg.h \
    $${PWD}/OAIPart.h \
    $${PWD}/OAIPlacedBet.h \
    $${PWD}/OAIPlacedBetLeg.h \
    $${PWD}/OAIPlacedBetPart.h \
    $${PWD}/OAIPriceFormatted.h \
    $${PWD}/OAISingleBetRequestBody.h \
    $${PWD}/OAISolution.h \
# APIs
    $${PWD}/OAIBetsApi.h \
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
    $${PWD}/OAIBet.cpp \
    $${PWD}/OAIBetDelayed.cpp \
    $${PWD}/OAIBetHistoryResponse.cpp \
    $${PWD}/OAIBetPlaced.cpp \
    $${PWD}/OAIBetSlipRequest.cpp \
    $${PWD}/OAIBetSlipResponse.cpp \
    $${PWD}/OAIBetslipbet.cpp \
    $${PWD}/OAIBetslipleg.cpp \
    $${PWD}/OAIBetslippart.cpp \
    $${PWD}/OAICashInResponse.cpp \
    $${PWD}/OAIComplexBetRequestBody.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrors.cpp \
    $${PWD}/OAIFreeBetDetail.cpp \
    $${PWD}/OAILeg.cpp \
    $${PWD}/OAIPart.cpp \
    $${PWD}/OAIPlacedBet.cpp \
    $${PWD}/OAIPlacedBetLeg.cpp \
    $${PWD}/OAIPlacedBetPart.cpp \
    $${PWD}/OAIPriceFormatted.cpp \
    $${PWD}/OAISingleBetRequestBody.cpp \
    $${PWD}/OAISolution.cpp \
# APIs
    $${PWD}/OAIBetsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
