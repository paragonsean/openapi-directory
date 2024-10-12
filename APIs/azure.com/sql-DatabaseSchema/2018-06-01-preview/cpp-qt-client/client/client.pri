QT += network

HEADERS += \
# Models
    $${PWD}/OAIDatabaseColumn.h \
    $${PWD}/OAIDatabaseColumnListResult.h \
    $${PWD}/OAIDatabaseColumnProperties.h \
    $${PWD}/OAIDatabaseSchema.h \
    $${PWD}/OAIDatabaseSchemaListResult.h \
    $${PWD}/OAIDatabaseTable.h \
    $${PWD}/OAIDatabaseTableListResult.h \
    $${PWD}/OAIProxyResource.h \
    $${PWD}/OAIResource.h \
# APIs
    $${PWD}/OAIDatabaseColumnsApi.h \
    $${PWD}/OAIDatabaseSchemasApi.h \
    $${PWD}/OAIDatabaseTablesApi.h \
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
    $${PWD}/OAIDatabaseColumn.cpp \
    $${PWD}/OAIDatabaseColumnListResult.cpp \
    $${PWD}/OAIDatabaseColumnProperties.cpp \
    $${PWD}/OAIDatabaseSchema.cpp \
    $${PWD}/OAIDatabaseSchemaListResult.cpp \
    $${PWD}/OAIDatabaseTable.cpp \
    $${PWD}/OAIDatabaseTableListResult.cpp \
    $${PWD}/OAIProxyResource.cpp \
    $${PWD}/OAIResource.cpp \
# APIs
    $${PWD}/OAIDatabaseColumnsApi.cpp \
    $${PWD}/OAIDatabaseSchemasApi.cpp \
    $${PWD}/OAIDatabaseTablesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
