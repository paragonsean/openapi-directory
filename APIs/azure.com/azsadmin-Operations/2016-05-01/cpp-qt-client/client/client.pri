QT += network

HEADERS += \
# Models
    $${PWD}/OAIOperationStatus.h \
    $${PWD}/OAIProvisioningStateModel.h \
# APIs
    $${PWD}/OAIComputeFabricOperationsApi.h \
    $${PWD}/OAINetworkFabricOperationsApi.h \
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
    $${PWD}/OAIOperationStatus.cpp \
    $${PWD}/OAIProvisioningStateModel.cpp \
# APIs
    $${PWD}/OAIComputeFabricOperationsApi.cpp \
    $${PWD}/OAINetworkFabricOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
