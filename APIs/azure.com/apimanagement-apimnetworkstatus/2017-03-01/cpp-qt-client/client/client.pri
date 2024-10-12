QT += network

HEADERS += \
# Models
    $${PWD}/OAIConnectivityStatusContract.h \
    $${PWD}/OAINetworkStatusContract.h \
    $${PWD}/OAINetworkStatus_ListByLocation_default_response.h \
    $${PWD}/OAINetworkStatus_ListByLocation_default_response_details_inner.h \
# APIs
    $${PWD}/OAINetworkStatusApi.h \
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
    $${PWD}/OAIConnectivityStatusContract.cpp \
    $${PWD}/OAINetworkStatusContract.cpp \
    $${PWD}/OAINetworkStatus_ListByLocation_default_response.cpp \
    $${PWD}/OAINetworkStatus_ListByLocation_default_response_details_inner.cpp \
# APIs
    $${PWD}/OAINetworkStatusApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
