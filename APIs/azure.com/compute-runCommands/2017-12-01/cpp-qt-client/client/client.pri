QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiError.h \
    $${PWD}/OAIApiErrorBase.h \
    $${PWD}/OAIInnerError.h \
    $${PWD}/OAIOperationStatusResponse.h \
    $${PWD}/OAIRunCommandDocument.h \
    $${PWD}/OAIRunCommandDocumentBase.h \
    $${PWD}/OAIRunCommandInput.h \
    $${PWD}/OAIRunCommandInputParameter.h \
    $${PWD}/OAIRunCommandListResult.h \
    $${PWD}/OAIRunCommandParameterDefinition.h \
    $${PWD}/OAIRunCommandResult.h \
    $${PWD}/OAIRunCommandResultProperties.h \
# APIs
    $${PWD}/OAIVirtualMachineRunCommandsApi.h \
    $${PWD}/OAIVirtualMachinesApi.h \
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
    $${PWD}/OAIApiError.cpp \
    $${PWD}/OAIApiErrorBase.cpp \
    $${PWD}/OAIInnerError.cpp \
    $${PWD}/OAIOperationStatusResponse.cpp \
    $${PWD}/OAIRunCommandDocument.cpp \
    $${PWD}/OAIRunCommandDocumentBase.cpp \
    $${PWD}/OAIRunCommandInput.cpp \
    $${PWD}/OAIRunCommandInputParameter.cpp \
    $${PWD}/OAIRunCommandListResult.cpp \
    $${PWD}/OAIRunCommandParameterDefinition.cpp \
    $${PWD}/OAIRunCommandResult.cpp \
    $${PWD}/OAIRunCommandResultProperties.cpp \
# APIs
    $${PWD}/OAIVirtualMachineRunCommandsApi.cpp \
    $${PWD}/OAIVirtualMachinesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
