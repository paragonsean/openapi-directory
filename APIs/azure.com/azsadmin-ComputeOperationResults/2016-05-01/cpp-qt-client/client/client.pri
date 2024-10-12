QT += network

HEADERS += \
# Models
    $${PWD}/OAIComputeOperationResult.h \
    $${PWD}/OAIComputeOperationResultList.h \
    $${PWD}/OAIComputeOperationResultModel.h \
# APIs
    $${PWD}/OAIComputeOperationResultsApi.h \
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
    $${PWD}/OAIComputeOperationResult.cpp \
    $${PWD}/OAIComputeOperationResultList.cpp \
    $${PWD}/OAIComputeOperationResultModel.cpp \
# APIs
    $${PWD}/OAIComputeOperationResultsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
