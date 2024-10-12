QT += network

HEADERS += \
# Models
    $${PWD}/OAIActivity.h \
    $${PWD}/OAIActivityListResult.h \
    $${PWD}/OAIActivityOutputType.h \
    $${PWD}/OAIActivityParameter.h \
    $${PWD}/OAIActivityParameterSet.h \
    $${PWD}/OAIActivityParameterValidationSet.h \
    $${PWD}/OAIActivityProperties.h \
    $${PWD}/OAIContentHash.h \
    $${PWD}/OAIContentLink.h \
    $${PWD}/OAIModule.h \
    $${PWD}/OAIModuleCreateOrUpdateParameters.h \
    $${PWD}/OAIModuleCreateOrUpdateProperties.h \
    $${PWD}/OAIModuleErrorInfo.h \
    $${PWD}/OAIModuleListResult.h \
    $${PWD}/OAIModuleProperties.h \
    $${PWD}/OAIModuleUpdateParameters.h \
    $${PWD}/OAIModuleUpdateProperties.h \
    $${PWD}/OAIModule_ListByAutomationAccount_default_response.h \
    $${PWD}/OAITypeField.h \
    $${PWD}/OAITypeFieldListResult.h \
# APIs
    $${PWD}/OAIActivityApi.h \
    $${PWD}/OAIModuleApi.h \
    $${PWD}/OAIObjectDataTypesApi.h \
    $${PWD}/OAITypeFieldsApi.h \
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
    $${PWD}/OAIActivity.cpp \
    $${PWD}/OAIActivityListResult.cpp \
    $${PWD}/OAIActivityOutputType.cpp \
    $${PWD}/OAIActivityParameter.cpp \
    $${PWD}/OAIActivityParameterSet.cpp \
    $${PWD}/OAIActivityParameterValidationSet.cpp \
    $${PWD}/OAIActivityProperties.cpp \
    $${PWD}/OAIContentHash.cpp \
    $${PWD}/OAIContentLink.cpp \
    $${PWD}/OAIModule.cpp \
    $${PWD}/OAIModuleCreateOrUpdateParameters.cpp \
    $${PWD}/OAIModuleCreateOrUpdateProperties.cpp \
    $${PWD}/OAIModuleErrorInfo.cpp \
    $${PWD}/OAIModuleListResult.cpp \
    $${PWD}/OAIModuleProperties.cpp \
    $${PWD}/OAIModuleUpdateParameters.cpp \
    $${PWD}/OAIModuleUpdateProperties.cpp \
    $${PWD}/OAIModule_ListByAutomationAccount_default_response.cpp \
    $${PWD}/OAITypeField.cpp \
    $${PWD}/OAITypeFieldListResult.cpp \
# APIs
    $${PWD}/OAIActivityApi.cpp \
    $${PWD}/OAIModuleApi.cpp \
    $${PWD}/OAIObjectDataTypesApi.cpp \
    $${PWD}/OAITypeFieldsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
