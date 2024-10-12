QT += network

HEADERS += \
# Models
    $${PWD}/OAISourceControlSyncJobStream.h \
    $${PWD}/OAISourceControlSyncJobStreamById.h \
    $${PWD}/OAISourceControlSyncJobStreamByIdProperties.h \
    $${PWD}/OAISourceControlSyncJobStreamProperties.h \
    $${PWD}/OAISourceControlSyncJobStreamsListBySyncJob.h \
    $${PWD}/OAISourceControlSyncJobStreams_ListBySyncJob_default_response.h \
# APIs
    $${PWD}/OAISourceControlSyncJobStreamsApi.h \
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
    $${PWD}/OAISourceControlSyncJobStream.cpp \
    $${PWD}/OAISourceControlSyncJobStreamById.cpp \
    $${PWD}/OAISourceControlSyncJobStreamByIdProperties.cpp \
    $${PWD}/OAISourceControlSyncJobStreamProperties.cpp \
    $${PWD}/OAISourceControlSyncJobStreamsListBySyncJob.cpp \
    $${PWD}/OAISourceControlSyncJobStreams_ListBySyncJob_default_response.cpp \
# APIs
    $${PWD}/OAISourceControlSyncJobStreamsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
