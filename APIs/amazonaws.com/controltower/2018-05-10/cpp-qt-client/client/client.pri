QT += network

HEADERS += \
# Models
    $${PWD}/OAIControlOperation.h \
    $${PWD}/OAIControlOperationStatus.h \
    $${PWD}/OAIControlOperationType.h \
    $${PWD}/OAIDisableControlInput.h \
    $${PWD}/OAIDisableControlOutput.h \
    $${PWD}/OAIDisableControl_request.h \
    $${PWD}/OAIEnableControlInput.h \
    $${PWD}/OAIEnableControlOutput.h \
    $${PWD}/OAIEnabledControlSummary.h \
    $${PWD}/OAIGetControlOperationInput.h \
    $${PWD}/OAIGetControlOperationOutput.h \
    $${PWD}/OAIGetControlOperationOutput_controlOperation.h \
    $${PWD}/OAIGetControlOperation_request.h \
    $${PWD}/OAIListEnabledControlsInput.h \
    $${PWD}/OAIListEnabledControlsOutput.h \
    $${PWD}/OAIListEnabledControls_request.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIControlOperation.cpp \
    $${PWD}/OAIControlOperationStatus.cpp \
    $${PWD}/OAIControlOperationType.cpp \
    $${PWD}/OAIDisableControlInput.cpp \
    $${PWD}/OAIDisableControlOutput.cpp \
    $${PWD}/OAIDisableControl_request.cpp \
    $${PWD}/OAIEnableControlInput.cpp \
    $${PWD}/OAIEnableControlOutput.cpp \
    $${PWD}/OAIEnabledControlSummary.cpp \
    $${PWD}/OAIGetControlOperationInput.cpp \
    $${PWD}/OAIGetControlOperationOutput.cpp \
    $${PWD}/OAIGetControlOperationOutput_controlOperation.cpp \
    $${PWD}/OAIGetControlOperation_request.cpp \
    $${PWD}/OAIListEnabledControlsInput.cpp \
    $${PWD}/OAIListEnabledControlsOutput.cpp \
    $${PWD}/OAIListEnabledControls_request.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
