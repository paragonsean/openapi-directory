QT += network

HEADERS += \
# Models
    $${PWD}/OAIElasticPool.h \
    $${PWD}/OAIElasticPoolListResult.h \
    $${PWD}/OAIElasticPoolPerDatabaseSettings.h \
    $${PWD}/OAIElasticPoolProperties.h \
    $${PWD}/OAIElasticPoolUpdate.h \
    $${PWD}/OAIElasticPoolUpdateProperties.h \
    $${PWD}/OAIElasticPoolUpdate_sku.h \
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
    $${PWD}/OAIElasticPool.cpp \
    $${PWD}/OAIElasticPoolListResult.cpp \
    $${PWD}/OAIElasticPoolPerDatabaseSettings.cpp \
    $${PWD}/OAIElasticPoolProperties.cpp \
    $${PWD}/OAIElasticPoolUpdate.cpp \
    $${PWD}/OAIElasticPoolUpdateProperties.cpp \
    $${PWD}/OAIElasticPoolUpdate_sku.cpp \
# APIs
    $${PWD}/OAIElasticPoolsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
