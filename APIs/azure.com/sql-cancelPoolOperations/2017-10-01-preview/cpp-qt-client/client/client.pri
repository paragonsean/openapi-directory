QT += network

HEADERS += \
# Models
    $${PWD}/OAIElasticPoolOperation.h \
    $${PWD}/OAIElasticPoolOperationListResult.h \
    $${PWD}/OAIElasticPoolOperationProperties.h \
# APIs
    $${PWD}/OAIElasticPoolsApi.h \
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
    $${PWD}/OAIElasticPoolOperation.cpp \
    $${PWD}/OAIElasticPoolOperationListResult.cpp \
    $${PWD}/OAIElasticPoolOperationProperties.cpp \
# APIs
    $${PWD}/OAIElasticPoolsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
