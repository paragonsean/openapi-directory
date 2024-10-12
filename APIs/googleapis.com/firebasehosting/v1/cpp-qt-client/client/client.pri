QT += network

HEADERS += \
# Models
    $${PWD}/OAICertVerification.h \
    $${PWD}/OAICustomDomainMetadata.h \
    $${PWD}/OAIDnsRecord.h \
    $${PWD}/OAIDnsRecordSet.h \
    $${PWD}/OAIDnsUpdates.h \
    $${PWD}/OAIHttpUpdate.h \
    $${PWD}/OAIListOperationsResponse.h \
    $${PWD}/OAILiveMigrationStep.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIStatus.h \
# APIs
    $${PWD}/OAIOperationsApi.h \
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
    $${PWD}/OAICertVerification.cpp \
    $${PWD}/OAICustomDomainMetadata.cpp \
    $${PWD}/OAIDnsRecord.cpp \
    $${PWD}/OAIDnsRecordSet.cpp \
    $${PWD}/OAIDnsUpdates.cpp \
    $${PWD}/OAIHttpUpdate.cpp \
    $${PWD}/OAIListOperationsResponse.cpp \
    $${PWD}/OAILiveMigrationStep.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIStatus.cpp \
# APIs
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
