QT += network

HEADERS += \
# Models
    $${PWD}/OAIDiscoveredSecuritySolution.h \
    $${PWD}/OAIDiscoveredSecuritySolutionList.h \
    $${PWD}/OAIDiscoveredSecuritySolutionProperties.h \
    $${PWD}/OAIDiscoveredSecuritySolutions_List_default_response.h \
    $${PWD}/OAIDiscoveredSecuritySolutions_List_default_response_error.h \
# APIs
    $${PWD}/OAIDiscoveredSecuritySolutionsApi.h \
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
    $${PWD}/OAIDiscoveredSecuritySolution.cpp \
    $${PWD}/OAIDiscoveredSecuritySolutionList.cpp \
    $${PWD}/OAIDiscoveredSecuritySolutionProperties.cpp \
    $${PWD}/OAIDiscoveredSecuritySolutions_List_default_response.cpp \
    $${PWD}/OAIDiscoveredSecuritySolutions_List_default_response_error.cpp \
# APIs
    $${PWD}/OAIDiscoveredSecuritySolutionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
