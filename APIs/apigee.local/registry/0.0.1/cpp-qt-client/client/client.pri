QT += network

HEADERS += \
# Models
    $${PWD}/OAIApi.h \
    $${PWD}/OAIApiDeployment.h \
    $${PWD}/OAIApiSpec.h \
    $${PWD}/OAIApiVersion.h \
    $${PWD}/OAIArtifact.h \
    $${PWD}/OAIGoogleProtobufAny.h \
    $${PWD}/OAIListApiDeploymentRevisionsResponse.h \
    $${PWD}/OAIListApiDeploymentsResponse.h \
    $${PWD}/OAIListApiSpecRevisionsResponse.h \
    $${PWD}/OAIListApiSpecsResponse.h \
    $${PWD}/OAIListApiVersionsResponse.h \
    $${PWD}/OAIListApisResponse.h \
    $${PWD}/OAIListArtifactsResponse.h \
    $${PWD}/OAIRollbackApiDeploymentRequest.h \
    $${PWD}/OAIRollbackApiSpecRequest.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAITagApiDeploymentRevisionRequest.h \
    $${PWD}/OAITagApiSpecRevisionRequest.h \
# APIs
    $${PWD}/OAIRegistryApi.h \
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
    $${PWD}/OAIApi.cpp \
    $${PWD}/OAIApiDeployment.cpp \
    $${PWD}/OAIApiSpec.cpp \
    $${PWD}/OAIApiVersion.cpp \
    $${PWD}/OAIArtifact.cpp \
    $${PWD}/OAIGoogleProtobufAny.cpp \
    $${PWD}/OAIListApiDeploymentRevisionsResponse.cpp \
    $${PWD}/OAIListApiDeploymentsResponse.cpp \
    $${PWD}/OAIListApiSpecRevisionsResponse.cpp \
    $${PWD}/OAIListApiSpecsResponse.cpp \
    $${PWD}/OAIListApiVersionsResponse.cpp \
    $${PWD}/OAIListApisResponse.cpp \
    $${PWD}/OAIListArtifactsResponse.cpp \
    $${PWD}/OAIRollbackApiDeploymentRequest.cpp \
    $${PWD}/OAIRollbackApiSpecRequest.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAITagApiDeploymentRevisionRequest.cpp \
    $${PWD}/OAITagApiSpecRevisionRequest.cpp \
# APIs
    $${PWD}/OAIRegistryApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
