QT += network

HEADERS += \
# Models
    $${PWD}/OAIStorageOperationResult.h \
    $${PWD}/OAIStorageOperationResultList.h \
    $${PWD}/OAIStorageOperationResultModel.h \
# APIs
    $${PWD}/OAIStorageOperationResultsApi.h \
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
    $${PWD}/OAIStorageOperationResult.cpp \
    $${PWD}/OAIStorageOperationResultList.cpp \
    $${PWD}/OAIStorageOperationResultModel.cpp \
# APIs
    $${PWD}/OAIStorageOperationResultsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
