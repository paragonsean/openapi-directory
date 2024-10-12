QT += network

HEADERS += \
# Models
    $${PWD}/OAIInstanceViewStatus.h \
    $${PWD}/OAIRunCommandDocument.h \
    $${PWD}/OAIRunCommandDocumentBase.h \
    $${PWD}/OAIRunCommandInput.h \
    $${PWD}/OAIRunCommandInputParameter.h \
    $${PWD}/OAIRunCommandListResult.h \
    $${PWD}/OAIRunCommandParameterDefinition.h \
    $${PWD}/OAIRunCommandResult.h \
# APIs
    $${PWD}/OAIVirtualMachineRunCommandsApi.h \
    $${PWD}/OAIVirtualMachineScaleSetVMsApi.h \
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
    $${PWD}/OAIInstanceViewStatus.cpp \
    $${PWD}/OAIRunCommandDocument.cpp \
    $${PWD}/OAIRunCommandDocumentBase.cpp \
    $${PWD}/OAIRunCommandInput.cpp \
    $${PWD}/OAIRunCommandInputParameter.cpp \
    $${PWD}/OAIRunCommandListResult.cpp \
    $${PWD}/OAIRunCommandParameterDefinition.cpp \
    $${PWD}/OAIRunCommandResult.cpp \
# APIs
    $${PWD}/OAIVirtualMachineRunCommandsApi.cpp \
    $${PWD}/OAIVirtualMachineScaleSetVMsApi.cpp \
    $${PWD}/OAIVirtualMachinesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
