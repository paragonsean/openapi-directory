QT += network

HEADERS += \
# Models
    $${PWD}/OAICard.h \
    $${PWD}/OAICardResume.h \
    $${PWD}/OAICard_abilities_inner.h \
    $${PWD}/OAICard_attacks_inner.h \
    $${PWD}/OAICard_item.h \
    $${PWD}/OAICard_legal.h \
    $${PWD}/OAICard_variants.h \
    $${PWD}/OAISerie.h \
    $${PWD}/OAISerieResume.h \
    $${PWD}/OAISet.h \
    $${PWD}/OAISetResume.h \
    $${PWD}/OAISetResume_cardCount.h \
    $${PWD}/OAISet_cardCount.h \
    $${PWD}/OAIStringEndpoint.h \
    $${PWD}/OAIWeakRes_inner.h \
# APIs
    $${PWD}/OAICardsApi.h \
    $${PWD}/OAIFiltersApi.h \
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
    $${PWD}/OAICard.cpp \
    $${PWD}/OAICardResume.cpp \
    $${PWD}/OAICard_abilities_inner.cpp \
    $${PWD}/OAICard_attacks_inner.cpp \
    $${PWD}/OAICard_item.cpp \
    $${PWD}/OAICard_legal.cpp \
    $${PWD}/OAICard_variants.cpp \
    $${PWD}/OAISerie.cpp \
    $${PWD}/OAISerieResume.cpp \
    $${PWD}/OAISet.cpp \
    $${PWD}/OAISetResume.cpp \
    $${PWD}/OAISetResume_cardCount.cpp \
    $${PWD}/OAISet_cardCount.cpp \
    $${PWD}/OAIStringEndpoint.cpp \
    $${PWD}/OAIWeakRes_inner.cpp \
# APIs
    $${PWD}/OAICardsApi.cpp \
    $${PWD}/OAIFiltersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
