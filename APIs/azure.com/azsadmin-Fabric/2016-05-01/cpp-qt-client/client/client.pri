QT += network

HEADERS += \
# Models
    $${PWD}/OAIDisplay.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationList.h \
    $${PWD}/OAIProvisioningState.h \
    $${PWD}/OAIProvisioningStateProperties.h \
    $${PWD}/OAIResource.h \
# APIs
    $${PWD}/OAIFabricApi.h \
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
    $${PWD}/OAIDisplay.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationList.cpp \
    $${PWD}/OAIProvisioningState.cpp \
    $${PWD}/OAIProvisioningStateProperties.cpp \
    $${PWD}/OAIResource.cpp \
# APIs
    $${PWD}/OAIFabricApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
