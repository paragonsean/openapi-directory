QT += network

HEADERS += \
# Models
    $${PWD}/OAIDownloadModelResponse.h \
    $${PWD}/OAIListModelsResponse.h \
    $${PWD}/OAIModel.h \
    $${PWD}/OAIModelOperationMetadata.h \
    $${PWD}/OAIModelState.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAITfLiteModel.h \
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
    $${PWD}/OAIDownloadModelResponse.cpp \
    $${PWD}/OAIListModelsResponse.cpp \
    $${PWD}/OAIModel.cpp \
    $${PWD}/OAIModelOperationMetadata.cpp \
    $${PWD}/OAIModelState.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAITfLiteModel.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
