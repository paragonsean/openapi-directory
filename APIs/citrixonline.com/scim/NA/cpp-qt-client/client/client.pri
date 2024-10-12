QT += network

HEADERS += \
# Models
    $${PWD}/OAIAuthenticationSchemes.h \
    $${PWD}/OAIBulk.h \
    $${PWD}/OAIChangePassword.h \
    $${PWD}/OAIEtag.h \
    $${PWD}/OAIFilter.h \
    $${PWD}/OAIGroup.h \
    $${PWD}/OAIGroupCollection.h \
    $${PWD}/OAIGroupDefinition.h \
    $${PWD}/OAIGroupMetadata.h \
    $${PWD}/OAIMember.h \
    $${PWD}/OAIPatch.h \
    $${PWD}/OAIResourceSchema.h \
    $${PWD}/OAISchemaAttribute.h \
    $${PWD}/OAISchemaSubAttribute.h \
    $${PWD}/OAIServiceProviderConfigs.h \
    $${PWD}/OAISort.h \
    $${PWD}/OAIUser.h \
    $${PWD}/OAIUserCollection.h \
    $${PWD}/OAIUserDefinition.h \
    $${PWD}/OAIUserFullName.h \
    $${PWD}/OAIUserMetadata.h \
    $${PWD}/OAIXmlDataFormat.h \
# APIs
    $${PWD}/OAIGroupsApi.h \
    $${PWD}/OAISchemasApi.h \
    $${PWD}/OAIUsersApi.h \
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
    $${PWD}/OAIAuthenticationSchemes.cpp \
    $${PWD}/OAIBulk.cpp \
    $${PWD}/OAIChangePassword.cpp \
    $${PWD}/OAIEtag.cpp \
    $${PWD}/OAIFilter.cpp \
    $${PWD}/OAIGroup.cpp \
    $${PWD}/OAIGroupCollection.cpp \
    $${PWD}/OAIGroupDefinition.cpp \
    $${PWD}/OAIGroupMetadata.cpp \
    $${PWD}/OAIMember.cpp \
    $${PWD}/OAIPatch.cpp \
    $${PWD}/OAIResourceSchema.cpp \
    $${PWD}/OAISchemaAttribute.cpp \
    $${PWD}/OAISchemaSubAttribute.cpp \
    $${PWD}/OAIServiceProviderConfigs.cpp \
    $${PWD}/OAISort.cpp \
    $${PWD}/OAIUser.cpp \
    $${PWD}/OAIUserCollection.cpp \
    $${PWD}/OAIUserDefinition.cpp \
    $${PWD}/OAIUserFullName.cpp \
    $${PWD}/OAIUserMetadata.cpp \
    $${PWD}/OAIXmlDataFormat.cpp \
# APIs
    $${PWD}/OAIGroupsApi.cpp \
    $${PWD}/OAISchemasApi.cpp \
    $${PWD}/OAIUsersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
