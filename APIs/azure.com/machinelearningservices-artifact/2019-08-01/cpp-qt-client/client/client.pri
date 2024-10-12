QT += network

HEADERS += \
# Models
    $${PWD}/OAIArtifact.h \
    $${PWD}/OAIArtifactContainerSas.h \
    $${PWD}/OAIArtifactContentInformation.h \
    $${PWD}/OAIArtifactIdList.h \
    $${PWD}/OAIArtifactPath.h \
    $${PWD}/OAIArtifactPathList.h \
    $${PWD}/OAIBatchArtifactContentInformationResult.h \
    $${PWD}/OAIDataPath.h \
    $${PWD}/OAIErrorDetails.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIInnerErrorResponse.h \
    $${PWD}/OAIPaginatedArtifactContentInformationList.h \
    $${PWD}/OAIPaginatedArtifactList.h \
    $${PWD}/OAIRootError.h \
    $${PWD}/OAISqlDataPath.h \
    $${PWD}/OAIStoredProcedureParameter.h \
# APIs
    $${PWD}/OAIArtifactApi.h \
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
    $${PWD}/OAIArtifact.cpp \
    $${PWD}/OAIArtifactContainerSas.cpp \
    $${PWD}/OAIArtifactContentInformation.cpp \
    $${PWD}/OAIArtifactIdList.cpp \
    $${PWD}/OAIArtifactPath.cpp \
    $${PWD}/OAIArtifactPathList.cpp \
    $${PWD}/OAIBatchArtifactContentInformationResult.cpp \
    $${PWD}/OAIDataPath.cpp \
    $${PWD}/OAIErrorDetails.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIInnerErrorResponse.cpp \
    $${PWD}/OAIPaginatedArtifactContentInformationList.cpp \
    $${PWD}/OAIPaginatedArtifactList.cpp \
    $${PWD}/OAIRootError.cpp \
    $${PWD}/OAISqlDataPath.cpp \
    $${PWD}/OAIStoredProcedureParameter.cpp \
# APIs
    $${PWD}/OAIArtifactApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
