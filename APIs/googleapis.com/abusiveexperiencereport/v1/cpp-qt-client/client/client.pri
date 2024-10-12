QT += network

HEADERS += \
# Models
    $${PWD}/OAISiteSummaryResponse.h \
    $${PWD}/OAIViolatingSitesResponse.h \
# APIs
    $${PWD}/OAISitesApi.h \
    $${PWD}/OAIViolatingSitesApi.h \
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
    $${PWD}/OAISiteSummaryResponse.cpp \
    $${PWD}/OAIViolatingSitesResponse.cpp \
# APIs
    $${PWD}/OAISitesApi.cpp \
    $${PWD}/OAIViolatingSitesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
