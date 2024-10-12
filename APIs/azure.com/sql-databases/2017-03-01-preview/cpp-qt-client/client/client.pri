QT += network

HEADERS += \
# Models
    $${PWD}/OAIDatabase.h \
    $${PWD}/OAIDatabaseListResult.h \
    $${PWD}/OAIDatabaseProperties.h \
    $${PWD}/OAIDatabaseUpdate.h \
    $${PWD}/OAIDatabaseUpdate_sku.h \
    $${PWD}/OAIImportExportDatabaseDefinition.h \
    $${PWD}/OAIImportExportOperationResult.h \
    $${PWD}/OAIImportExportOperationResultProperties.h \
# APIs
    $${PWD}/OAIDatabasesApi.h \
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
    $${PWD}/OAIDatabase.cpp \
    $${PWD}/OAIDatabaseListResult.cpp \
    $${PWD}/OAIDatabaseProperties.cpp \
    $${PWD}/OAIDatabaseUpdate.cpp \
    $${PWD}/OAIDatabaseUpdate_sku.cpp \
    $${PWD}/OAIImportExportDatabaseDefinition.cpp \
    $${PWD}/OAIImportExportOperationResult.cpp \
    $${PWD}/OAIImportExportOperationResultProperties.cpp \
# APIs
    $${PWD}/OAIDatabasesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
