QT += network

HEADERS += \
# Models
    $${PWD}/OAIInterval.h \
    $${PWD}/OAIIntervalCollection.h \
    $${PWD}/OAIIntervalCollectionResponse.h \
    $${PWD}/OAIRate.h \
    $${PWD}/OAIRateResponse.h \
    $${PWD}/OAISummary.h \
    $${PWD}/OAISummaryResponse.h \
# APIs
    $${PWD}/OAICurrenciesApi.h \
    $${PWD}/OAIMetalsApi.h \
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
    $${PWD}/OAIInterval.cpp \
    $${PWD}/OAIIntervalCollection.cpp \
    $${PWD}/OAIIntervalCollectionResponse.cpp \
    $${PWD}/OAIRate.cpp \
    $${PWD}/OAIRateResponse.cpp \
    $${PWD}/OAISummary.cpp \
    $${PWD}/OAISummaryResponse.cpp \
# APIs
    $${PWD}/OAICurrenciesApi.cpp \
    $${PWD}/OAIMetalsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
