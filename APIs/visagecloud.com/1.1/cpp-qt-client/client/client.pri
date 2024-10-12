QT += network

HEADERS += \
# Models
    $${PWD}/OAIRestResponse.h \
# APIs
    $${PWD}/OAIAccountControllerApi.h \
    $${PWD}/OAIAnalysisApi.h \
    $${PWD}/OAIAnalyticsForPresenceAndAudienceApi.h \
    $${PWD}/OAIClassifierApi.h \
    $${PWD}/OAICollectionApi.h \
    $${PWD}/OAIProfileApi.h \
    $${PWD}/OAIStreamApi.h \
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
    $${PWD}/OAIRestResponse.cpp \
# APIs
    $${PWD}/OAIAccountControllerApi.cpp \
    $${PWD}/OAIAnalysisApi.cpp \
    $${PWD}/OAIAnalyticsForPresenceAndAudienceApi.cpp \
    $${PWD}/OAIClassifierApi.cpp \
    $${PWD}/OAICollectionApi.cpp \
    $${PWD}/OAIProfileApi.cpp \
    $${PWD}/OAIStreamApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
