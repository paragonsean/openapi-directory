QT += network

HEADERS += \
# Models
    $${PWD}/OAISyncDatabaseIdListResult.h \
    $${PWD}/OAISyncDatabaseIdProperties.h \
    $${PWD}/OAISyncFullSchemaProperties.h \
    $${PWD}/OAISyncFullSchemaPropertiesListResult.h \
    $${PWD}/OAISyncFullSchemaTable.h \
    $${PWD}/OAISyncFullSchemaTableColumn.h \
    $${PWD}/OAISyncGroup.h \
    $${PWD}/OAISyncGroupListResult.h \
    $${PWD}/OAISyncGroupLogListResult.h \
    $${PWD}/OAISyncGroupLogProperties.h \
    $${PWD}/OAISyncGroupProperties.h \
    $${PWD}/OAISyncGroupSchema.h \
    $${PWD}/OAISyncGroupSchemaTable.h \
    $${PWD}/OAISyncGroupSchemaTableColumn.h \
# APIs
    $${PWD}/OAISyncGroupsApi.h \
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
    $${PWD}/OAISyncDatabaseIdListResult.cpp \
    $${PWD}/OAISyncDatabaseIdProperties.cpp \
    $${PWD}/OAISyncFullSchemaProperties.cpp \
    $${PWD}/OAISyncFullSchemaPropertiesListResult.cpp \
    $${PWD}/OAISyncFullSchemaTable.cpp \
    $${PWD}/OAISyncFullSchemaTableColumn.cpp \
    $${PWD}/OAISyncGroup.cpp \
    $${PWD}/OAISyncGroupListResult.cpp \
    $${PWD}/OAISyncGroupLogListResult.cpp \
    $${PWD}/OAISyncGroupLogProperties.cpp \
    $${PWD}/OAISyncGroupProperties.cpp \
    $${PWD}/OAISyncGroupSchema.cpp \
    $${PWD}/OAISyncGroupSchemaTable.cpp \
    $${PWD}/OAISyncGroupSchemaTableColumn.cpp \
# APIs
    $${PWD}/OAISyncGroupsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
