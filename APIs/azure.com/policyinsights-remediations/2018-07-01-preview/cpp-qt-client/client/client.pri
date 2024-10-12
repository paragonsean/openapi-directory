QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorDefinition.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIRemediation.h \
    $${PWD}/OAIRemediationDeployment.h \
    $${PWD}/OAIRemediationDeploymentSummary.h \
    $${PWD}/OAIRemediationDeploymentsListResult.h \
    $${PWD}/OAIRemediationFilters.h \
    $${PWD}/OAIRemediationListResult.h \
    $${PWD}/OAIRemediationProperties.h \
    $${PWD}/OAITypedErrorInfo.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIErrorDefinition.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIRemediation.cpp \
    $${PWD}/OAIRemediationDeployment.cpp \
    $${PWD}/OAIRemediationDeploymentSummary.cpp \
    $${PWD}/OAIRemediationDeploymentsListResult.cpp \
    $${PWD}/OAIRemediationFilters.cpp \
    $${PWD}/OAIRemediationListResult.cpp \
    $${PWD}/OAIRemediationProperties.cpp \
    $${PWD}/OAITypedErrorInfo.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
