QT += network

HEADERS += \
# Models
    $${PWD}/OAIDscCompilationJob.h \
    $${PWD}/OAIDscCompilationJobCreateParameters.h \
    $${PWD}/OAIDscCompilationJobCreateProperties.h \
    $${PWD}/OAIDscCompilationJobListResult.h \
    $${PWD}/OAIDscCompilationJobProperties.h \
    $${PWD}/OAIDscCompilationJobStream_ListByJob_200_response.h \
    $${PWD}/OAIDscCompilationJobStream_ListByJob_200_response_value_inner.h \
    $${PWD}/OAIDscCompilationJobStream_ListByJob_200_response_value_inner_properties.h \
    $${PWD}/OAIDscCompilationJob_ListByAutomationAccount_default_response.h \
    $${PWD}/OAIDscConfigurationAssociationProperty.h \
    $${PWD}/OAIJobProvisioningStateProperty.h \
# APIs
    $${PWD}/OAIDscCompilationJobApi.h \
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
    $${PWD}/OAIDscCompilationJob.cpp \
    $${PWD}/OAIDscCompilationJobCreateParameters.cpp \
    $${PWD}/OAIDscCompilationJobCreateProperties.cpp \
    $${PWD}/OAIDscCompilationJobListResult.cpp \
    $${PWD}/OAIDscCompilationJobProperties.cpp \
    $${PWD}/OAIDscCompilationJobStream_ListByJob_200_response.cpp \
    $${PWD}/OAIDscCompilationJobStream_ListByJob_200_response_value_inner.cpp \
    $${PWD}/OAIDscCompilationJobStream_ListByJob_200_response_value_inner_properties.cpp \
    $${PWD}/OAIDscCompilationJob_ListByAutomationAccount_default_response.cpp \
    $${PWD}/OAIDscConfigurationAssociationProperty.cpp \
    $${PWD}/OAIJobProvisioningStateProperty.cpp \
# APIs
    $${PWD}/OAIDscCompilationJobApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
