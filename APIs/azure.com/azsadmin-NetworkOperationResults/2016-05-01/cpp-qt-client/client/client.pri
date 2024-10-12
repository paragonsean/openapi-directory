QT += network

HEADERS += \
# Models
    $${PWD}/OAINetworkOperationResult.h \
    $${PWD}/OAINetworkOperationResultList.h \
    $${PWD}/OAINetworkOperationResultModel.h \
# APIs
    $${PWD}/OAINetworkOperationResultsApi.h \
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
    $${PWD}/OAINetworkOperationResult.cpp \
    $${PWD}/OAINetworkOperationResultList.cpp \
    $${PWD}/OAINetworkOperationResultModel.cpp \
# APIs
    $${PWD}/OAINetworkOperationResultsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
