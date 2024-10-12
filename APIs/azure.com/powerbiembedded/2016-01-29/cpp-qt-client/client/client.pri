QT += network

HEADERS += \
# Models
    $${PWD}/OAIAzureSku.h \
    $${PWD}/OAICheckNameRequest.h \
    $${PWD}/OAICheckNameResponse.h \
    $${PWD}/OAICreateWorkspaceCollectionRequest.h \
    $${PWD}/OAIDisplay.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorDetail.h \
    $${PWD}/OAIMigrateWorkspaceCollectionRequest.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationList.h \
    $${PWD}/OAIUpdateWorkspaceCollectionRequest.h \
    $${PWD}/OAIWorkspace.h \
    $${PWD}/OAIWorkspaceCollection.h \
    $${PWD}/OAIWorkspaceCollectionAccessKey.h \
    $${PWD}/OAIWorkspaceCollectionAccessKeys.h \
    $${PWD}/OAIWorkspaceCollectionList.h \
    $${PWD}/OAIWorkspaceList.h \
# APIs
    $${PWD}/OAIOperationsApi.h \
    $${PWD}/OAIWorkspaceCollectionsApi.h \
    $${PWD}/OAIWorkspacesApi.h \
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
    $${PWD}/OAIAzureSku.cpp \
    $${PWD}/OAICheckNameRequest.cpp \
    $${PWD}/OAICheckNameResponse.cpp \
    $${PWD}/OAICreateWorkspaceCollectionRequest.cpp \
    $${PWD}/OAIDisplay.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorDetail.cpp \
    $${PWD}/OAIMigrateWorkspaceCollectionRequest.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationList.cpp \
    $${PWD}/OAIUpdateWorkspaceCollectionRequest.cpp \
    $${PWD}/OAIWorkspace.cpp \
    $${PWD}/OAIWorkspaceCollection.cpp \
    $${PWD}/OAIWorkspaceCollectionAccessKey.cpp \
    $${PWD}/OAIWorkspaceCollectionAccessKeys.cpp \
    $${PWD}/OAIWorkspaceCollectionList.cpp \
    $${PWD}/OAIWorkspaceList.cpp \
# APIs
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAIWorkspaceCollectionsApi.cpp \
    $${PWD}/OAIWorkspacesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
