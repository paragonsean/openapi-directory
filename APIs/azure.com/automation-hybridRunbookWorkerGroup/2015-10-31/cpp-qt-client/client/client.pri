QT += network

HEADERS += \
# Models
    $${PWD}/OAIHybridRunbookWorker.h \
    $${PWD}/OAIHybridRunbookWorkerGroup.h \
    $${PWD}/OAIHybridRunbookWorkerGroupUpdateParameters.h \
    $${PWD}/OAIHybridRunbookWorkerGroup_ListByAutomationAccount_default_response.h \
    $${PWD}/OAIHybridRunbookWorkerGroupsListResult.h \
    $${PWD}/OAIRunAsCredentialAssociationProperty.h \
# APIs
    $${PWD}/OAIHybridRunbookWorkerGroupApi.h \
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
    $${PWD}/OAIHybridRunbookWorker.cpp \
    $${PWD}/OAIHybridRunbookWorkerGroup.cpp \
    $${PWD}/OAIHybridRunbookWorkerGroupUpdateParameters.cpp \
    $${PWD}/OAIHybridRunbookWorkerGroup_ListByAutomationAccount_default_response.cpp \
    $${PWD}/OAIHybridRunbookWorkerGroupsListResult.cpp \
    $${PWD}/OAIRunAsCredentialAssociationProperty.cpp \
# APIs
    $${PWD}/OAIHybridRunbookWorkerGroupApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
