QT += network

HEADERS += \
# Models
    $${PWD}/OAIQuotaByCounterKeys_ListByService_default_response.h \
    $${PWD}/OAIQuotaByCounterKeys_ListByService_default_response_details_inner.h \
    $${PWD}/OAIQuotaCounterCollection.h \
    $${PWD}/OAIQuotaCounterContract.h \
    $${PWD}/OAIQuotaCounterValueContract.h \
# APIs
    $${PWD}/OAIQuotaByCounterKeysApi.h \
    $${PWD}/OAIQuotaByPeriodKeysApi.h \
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
    $${PWD}/OAIQuotaByCounterKeys_ListByService_default_response.cpp \
    $${PWD}/OAIQuotaByCounterKeys_ListByService_default_response_details_inner.cpp \
    $${PWD}/OAIQuotaCounterCollection.cpp \
    $${PWD}/OAIQuotaCounterContract.cpp \
    $${PWD}/OAIQuotaCounterValueContract.cpp \
# APIs
    $${PWD}/OAIQuotaByCounterKeysApi.cpp \
    $${PWD}/OAIQuotaByPeriodKeysApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
