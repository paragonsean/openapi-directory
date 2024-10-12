QT += network

HEADERS += \
# Models
    $${PWD}/OAICallback.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIException.h \
    $${PWD}/OAIExecution.h \
    $${PWD}/OAIExportDataResponse.h \
    $${PWD}/OAIListCallbacksResponse.h \
    $${PWD}/OAIListExecutionsResponse.h \
    $${PWD}/OAIListStepEntriesResponse.h \
    $${PWD}/OAINavigationInfo.h \
    $${PWD}/OAIPosition.h \
    $${PWD}/OAIPubsubMessage.h \
    $${PWD}/OAIStackTrace.h \
    $${PWD}/OAIStackTraceElement.h \
    $${PWD}/OAIStateError.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAIStep.h \
    $${PWD}/OAIStepEntry.h \
    $${PWD}/OAIStepEntryMetadata.h \
    $${PWD}/OAITriggerPubsubExecutionRequest.h \
# APIs
    $${PWD}/OAIProjectsApi.h \
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
    $${PWD}/OAICallback.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIException.cpp \
    $${PWD}/OAIExecution.cpp \
    $${PWD}/OAIExportDataResponse.cpp \
    $${PWD}/OAIListCallbacksResponse.cpp \
    $${PWD}/OAIListExecutionsResponse.cpp \
    $${PWD}/OAIListStepEntriesResponse.cpp \
    $${PWD}/OAINavigationInfo.cpp \
    $${PWD}/OAIPosition.cpp \
    $${PWD}/OAIPubsubMessage.cpp \
    $${PWD}/OAIStackTrace.cpp \
    $${PWD}/OAIStackTraceElement.cpp \
    $${PWD}/OAIStateError.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAIStep.cpp \
    $${PWD}/OAIStepEntry.cpp \
    $${PWD}/OAIStepEntryMetadata.cpp \
    $${PWD}/OAITriggerPubsubExecutionRequest.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
