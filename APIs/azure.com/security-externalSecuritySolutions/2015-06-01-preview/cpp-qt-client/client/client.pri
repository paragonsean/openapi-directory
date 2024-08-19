QT += network

HEADERS += \
# Models
    $${PWD}/OAIAadConnectivityState.h \
    $${PWD}/OAIAadExternalSecuritySolution.h \
    $${PWD}/OAIAadSolutionProperties.h \
    $${PWD}/OAIAtaExternalSecuritySolution.h \
    $${PWD}/OAIAtaSolutionProperties.h \
    $${PWD}/OAICefExternalSecuritySolution.h \
    $${PWD}/OAICefSolutionProperties.h \
    $${PWD}/OAIConnectedWorkspace.h \
    $${PWD}/OAIExternalSecuritySolution.h \
    $${PWD}/OAIExternalSecuritySolutionKind.h \
    $${PWD}/OAIExternalSecuritySolutionList.h \
    $${PWD}/OAIExternalSecuritySolutionProperties.h \
    $${PWD}/OAIExternalSecuritySolutions_List_default_response.h \
    $${PWD}/OAIExternalSecuritySolutions_List_default_response_error.h \
# APIs
    $${PWD}/OAIExternalSecuritySolutionsApi.h \
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
    $${PWD}/OAIAadConnectivityState.cpp \
    $${PWD}/OAIAadExternalSecuritySolution.cpp \
    $${PWD}/OAIAadSolutionProperties.cpp \
    $${PWD}/OAIAtaExternalSecuritySolution.cpp \
    $${PWD}/OAIAtaSolutionProperties.cpp \
    $${PWD}/OAICefExternalSecuritySolution.cpp \
    $${PWD}/OAICefSolutionProperties.cpp \
    $${PWD}/OAIConnectedWorkspace.cpp \
    $${PWD}/OAIExternalSecuritySolution.cpp \
    $${PWD}/OAIExternalSecuritySolutionKind.cpp \
    $${PWD}/OAIExternalSecuritySolutionList.cpp \
    $${PWD}/OAIExternalSecuritySolutionProperties.cpp \
    $${PWD}/OAIExternalSecuritySolutions_List_default_response.cpp \
    $${PWD}/OAIExternalSecuritySolutions_List_default_response_error.cpp \
# APIs
    $${PWD}/OAIExternalSecuritySolutionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
