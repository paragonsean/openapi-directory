QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorDetail.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIIdentity.h \
    $${PWD}/OAIMachine.h \
    $${PWD}/OAIMachineListResult.h \
    $${PWD}/OAIMachineProperties.h \
    $${PWD}/OAIMachineReconnect.h \
    $${PWD}/OAIMachineReconnectProperties.h \
    $${PWD}/OAIMachineUpdate.h \
    $${PWD}/OAIMachineUpdateProperties.h \
    $${PWD}/OAIOSProfile.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperationValue.h \
    $${PWD}/OAIOperationValueDisplay.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIUpdateResource.h \
# APIs
    $${PWD}/OAIMachinesApi.h \
    $${PWD}/OAIOperationsApi.h \
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
    $${PWD}/OAIErrorDetail.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIIdentity.cpp \
    $${PWD}/OAIMachine.cpp \
    $${PWD}/OAIMachineListResult.cpp \
    $${PWD}/OAIMachineProperties.cpp \
    $${PWD}/OAIMachineReconnect.cpp \
    $${PWD}/OAIMachineReconnectProperties.cpp \
    $${PWD}/OAIMachineUpdate.cpp \
    $${PWD}/OAIMachineUpdateProperties.cpp \
    $${PWD}/OAIOSProfile.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperationValue.cpp \
    $${PWD}/OAIOperationValueDisplay.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIUpdateResource.cpp \
# APIs
    $${PWD}/OAIMachinesApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
