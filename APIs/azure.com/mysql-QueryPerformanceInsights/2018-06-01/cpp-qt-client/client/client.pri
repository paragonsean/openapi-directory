QT += network

HEADERS += \
# Models
    $${PWD}/OAIQueryStatistic.h \
    $${PWD}/OAIQueryStatisticProperties.h \
    $${PWD}/OAIQueryText.h \
    $${PWD}/OAIQueryTextProperties.h \
    $${PWD}/OAIQueryTextsResultList.h \
    $${PWD}/OAITopQueryStatisticsInput.h \
    $${PWD}/OAITopQueryStatisticsInputProperties.h \
    $${PWD}/OAITopQueryStatisticsResultList.h \
    $${PWD}/OAIWaitStatistic.h \
    $${PWD}/OAIWaitStatisticProperties.h \
    $${PWD}/OAIWaitStatisticsInput.h \
    $${PWD}/OAIWaitStatisticsInputProperties.h \
    $${PWD}/OAIWaitStatisticsResultList.h \
# APIs
    $${PWD}/OAIQueryTextsApi.h \
    $${PWD}/OAITopQueryStatisticsApi.h \
    $${PWD}/OAIWaitStatisticsApi.h \
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
    $${PWD}/OAIQueryStatistic.cpp \
    $${PWD}/OAIQueryStatisticProperties.cpp \
    $${PWD}/OAIQueryText.cpp \
    $${PWD}/OAIQueryTextProperties.cpp \
    $${PWD}/OAIQueryTextsResultList.cpp \
    $${PWD}/OAITopQueryStatisticsInput.cpp \
    $${PWD}/OAITopQueryStatisticsInputProperties.cpp \
    $${PWD}/OAITopQueryStatisticsResultList.cpp \
    $${PWD}/OAIWaitStatistic.cpp \
    $${PWD}/OAIWaitStatisticProperties.cpp \
    $${PWD}/OAIWaitStatisticsInput.cpp \
    $${PWD}/OAIWaitStatisticsInputProperties.cpp \
    $${PWD}/OAIWaitStatisticsResultList.cpp \
# APIs
    $${PWD}/OAIQueryTextsApi.cpp \
    $${PWD}/OAITopQueryStatisticsApi.cpp \
    $${PWD}/OAIWaitStatisticsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
