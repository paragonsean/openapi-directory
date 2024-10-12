QT += network

HEADERS += \
# Models
    $${PWD}/OAICloudError.h \
    $${PWD}/OAICloudError_error.h \
    $${PWD}/OAICloudError_error_additionalInfo_inner.h \
    $${PWD}/OAIPolicyDefinitionGroup.h \
    $${PWD}/OAIPolicyDefinitionReference.h \
    $${PWD}/OAIPolicyDefinitionReference_parameters_value.h \
    $${PWD}/OAIPolicySetDefinition.h \
    $${PWD}/OAIPolicySetDefinitionListResult.h \
    $${PWD}/OAIPolicySetDefinitionProperties.h \
    $${PWD}/OAIPolicySetDefinitionProperties_parameters_value.h \
# APIs
    $${PWD}/OAIPolicySetDefinitionsApi.h \
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
    $${PWD}/OAICloudError.cpp \
    $${PWD}/OAICloudError_error.cpp \
    $${PWD}/OAICloudError_error_additionalInfo_inner.cpp \
    $${PWD}/OAIPolicyDefinitionGroup.cpp \
    $${PWD}/OAIPolicyDefinitionReference.cpp \
    $${PWD}/OAIPolicyDefinitionReference_parameters_value.cpp \
    $${PWD}/OAIPolicySetDefinition.cpp \
    $${PWD}/OAIPolicySetDefinitionListResult.cpp \
    $${PWD}/OAIPolicySetDefinitionProperties.cpp \
    $${PWD}/OAIPolicySetDefinitionProperties_parameters_value.cpp \
# APIs
    $${PWD}/OAIPolicySetDefinitionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
