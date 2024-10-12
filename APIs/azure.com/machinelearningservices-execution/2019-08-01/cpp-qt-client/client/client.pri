QT += network

HEADERS += \
# Models
    $${PWD}/OAIContainerRegistry.h \
    $${PWD}/OAIDataReferenceConfiguration.h \
    $${PWD}/OAIDockerSection.h \
    $${PWD}/OAIEnvironmentDefinition.h \
    $${PWD}/OAIErrorDetails.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIHdiConfiguration.h \
    $${PWD}/OAIHistoryConfiguration.h \
    $${PWD}/OAIInnerErrorResponse.h \
    $${PWD}/OAIMpiConfiguration.h \
    $${PWD}/OAIPythonSection.h \
    $${PWD}/OAIRootError.h \
    $${PWD}/OAIRunConfiguration.h \
    $${PWD}/OAIRunDefinition.h \
    $${PWD}/OAISparkConfiguration.h \
    $${PWD}/OAISparkMavenPackage.h \
    $${PWD}/OAISparkSection.h \
    $${PWD}/OAIStartRunResult.h \
    $${PWD}/OAITensorflowConfiguration.h \
# APIs
    $${PWD}/OAIExecutionApi.h \
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
    $${PWD}/OAIContainerRegistry.cpp \
    $${PWD}/OAIDataReferenceConfiguration.cpp \
    $${PWD}/OAIDockerSection.cpp \
    $${PWD}/OAIEnvironmentDefinition.cpp \
    $${PWD}/OAIErrorDetails.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIHdiConfiguration.cpp \
    $${PWD}/OAIHistoryConfiguration.cpp \
    $${PWD}/OAIInnerErrorResponse.cpp \
    $${PWD}/OAIMpiConfiguration.cpp \
    $${PWD}/OAIPythonSection.cpp \
    $${PWD}/OAIRootError.cpp \
    $${PWD}/OAIRunConfiguration.cpp \
    $${PWD}/OAIRunDefinition.cpp \
    $${PWD}/OAISparkConfiguration.cpp \
    $${PWD}/OAISparkMavenPackage.cpp \
    $${PWD}/OAISparkSection.cpp \
    $${PWD}/OAIStartRunResult.cpp \
    $${PWD}/OAITensorflowConfiguration.cpp \
# APIs
    $${PWD}/OAIExecutionApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
