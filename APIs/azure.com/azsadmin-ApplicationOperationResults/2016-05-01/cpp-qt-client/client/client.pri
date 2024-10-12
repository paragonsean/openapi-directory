QT += network

HEADERS += \
# Models
    $${PWD}/OAIApplicationOperationResult.h \
    $${PWD}/OAIApplicationOperationResultList.h \
    $${PWD}/OAIApplicationOperationResultModel.h \
# APIs
    $${PWD}/OAIApplicationOperationResultsApi.h \
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
    $${PWD}/OAIApplicationOperationResult.cpp \
    $${PWD}/OAIApplicationOperationResultList.cpp \
    $${PWD}/OAIApplicationOperationResultModel.cpp \
# APIs
    $${PWD}/OAIApplicationOperationResultsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
