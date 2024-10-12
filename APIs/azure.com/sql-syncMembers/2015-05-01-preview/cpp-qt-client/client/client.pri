QT += network

HEADERS += \
# Models
    $${PWD}/OAISyncFullSchemaProperties.h \
    $${PWD}/OAISyncFullSchemaPropertiesListResult.h \
    $${PWD}/OAISyncFullSchemaTable.h \
    $${PWD}/OAISyncFullSchemaTableColumn.h \
    $${PWD}/OAISyncMember.h \
    $${PWD}/OAISyncMemberListResult.h \
    $${PWD}/OAISyncMemberProperties.h \
# APIs
    $${PWD}/OAISyncMembersApi.h \
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
    $${PWD}/OAISyncFullSchemaProperties.cpp \
    $${PWD}/OAISyncFullSchemaPropertiesListResult.cpp \
    $${PWD}/OAISyncFullSchemaTable.cpp \
    $${PWD}/OAISyncFullSchemaTableColumn.cpp \
    $${PWD}/OAISyncMember.cpp \
    $${PWD}/OAISyncMemberListResult.cpp \
    $${PWD}/OAISyncMemberProperties.cpp \
# APIs
    $${PWD}/OAISyncMembersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
