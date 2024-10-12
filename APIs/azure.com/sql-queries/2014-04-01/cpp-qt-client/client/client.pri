QT += network

HEADERS += \
# Models
    $${PWD}/OAIQueryInterval.h \
    $${PWD}/OAIQueryMetric.h \
    $${PWD}/OAIQueryStatistic.h \
    $${PWD}/OAIQueryStatisticListResult.h \
    $${PWD}/OAIQueryText.h \
    $${PWD}/OAIQueryTextListResult.h \
    $${PWD}/OAITopQueries.h \
    $${PWD}/OAITopQueriesListResult.h \
# APIs
    $${PWD}/OAIQueriesApi.h \
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
    $${PWD}/OAIQueryInterval.cpp \
    $${PWD}/OAIQueryMetric.cpp \
    $${PWD}/OAIQueryStatistic.cpp \
    $${PWD}/OAIQueryStatisticListResult.cpp \
    $${PWD}/OAIQueryText.cpp \
    $${PWD}/OAIQueryTextListResult.cpp \
    $${PWD}/OAITopQueries.cpp \
    $${PWD}/OAITopQueriesListResult.cpp \
# APIs
    $${PWD}/OAIQueriesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
