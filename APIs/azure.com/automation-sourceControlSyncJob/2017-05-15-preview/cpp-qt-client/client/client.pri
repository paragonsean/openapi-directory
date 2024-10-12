QT += network

HEADERS += \
# Models
    $${PWD}/OAISourceControlSyncJob.h \
    $${PWD}/OAISourceControlSyncJobById.h \
    $${PWD}/OAISourceControlSyncJobByIdProperties.h \
    $${PWD}/OAISourceControlSyncJobCreateParameters.h \
    $${PWD}/OAISourceControlSyncJobCreateProperties.h \
    $${PWD}/OAISourceControlSyncJobListResult.h \
    $${PWD}/OAISourceControlSyncJobProperties.h \
    $${PWD}/OAISourceControlSyncJob_ListByAutomationAccount_default_response.h \
# APIs
    $${PWD}/OAISourceControlSyncJobApi.h \
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
    $${PWD}/OAISourceControlSyncJob.cpp \
    $${PWD}/OAISourceControlSyncJobById.cpp \
    $${PWD}/OAISourceControlSyncJobByIdProperties.cpp \
    $${PWD}/OAISourceControlSyncJobCreateParameters.cpp \
    $${PWD}/OAISourceControlSyncJobCreateProperties.cpp \
    $${PWD}/OAISourceControlSyncJobListResult.cpp \
    $${PWD}/OAISourceControlSyncJobProperties.cpp \
    $${PWD}/OAISourceControlSyncJob_ListByAutomationAccount_default_response.cpp \
# APIs
    $${PWD}/OAISourceControlSyncJobApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
