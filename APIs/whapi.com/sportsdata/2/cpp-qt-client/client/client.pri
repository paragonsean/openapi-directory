QT += network

HEADERS += \
# Models
    $${PWD}/OAIClass.h \
    $${PWD}/OAIClassesWrapper.h \
    $${PWD}/OAICompetition.h \
    $${PWD}/OAICompetitionsWrapper.h \
    $${PWD}/OAICompetitor.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorsWrapper.h \
    $${PWD}/OAIEvent.h \
    $${PWD}/OAIEventCompetitorsWrapper.h \
    $${PWD}/OAIEventsWrapper.h \
    $${PWD}/OAIMarket.h \
    $${PWD}/OAIMarketGroupsWrapper.h \
    $${PWD}/OAIMarketgroup.h \
    $${PWD}/OAIMarketsWrapper.h \
    $${PWD}/OAIPriceFormatted.h \
    $${PWD}/OAISelection.h \
    $${PWD}/OAISelectionsWrapper.h \
    $${PWD}/OAISport.h \
    $${PWD}/OAISportsWrapper.h \
    $${PWD}/OAITopBet.h \
    $${PWD}/OAITopBetsWrapper.h \
# APIs
    $${PWD}/OAICompetitorsApi.h \
    $${PWD}/OAISportsdataApi.h \
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
    $${PWD}/OAIClass.cpp \
    $${PWD}/OAIClassesWrapper.cpp \
    $${PWD}/OAICompetition.cpp \
    $${PWD}/OAICompetitionsWrapper.cpp \
    $${PWD}/OAICompetitor.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorsWrapper.cpp \
    $${PWD}/OAIEvent.cpp \
    $${PWD}/OAIEventCompetitorsWrapper.cpp \
    $${PWD}/OAIEventsWrapper.cpp \
    $${PWD}/OAIMarket.cpp \
    $${PWD}/OAIMarketGroupsWrapper.cpp \
    $${PWD}/OAIMarketgroup.cpp \
    $${PWD}/OAIMarketsWrapper.cpp \
    $${PWD}/OAIPriceFormatted.cpp \
    $${PWD}/OAISelection.cpp \
    $${PWD}/OAISelectionsWrapper.cpp \
    $${PWD}/OAISport.cpp \
    $${PWD}/OAISportsWrapper.cpp \
    $${PWD}/OAITopBet.cpp \
    $${PWD}/OAITopBetsWrapper.cpp \
# APIs
    $${PWD}/OAICompetitorsApi.cpp \
    $${PWD}/OAISportsdataApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
