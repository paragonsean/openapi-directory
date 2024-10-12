QT += network

HEADERS += \
# Models
    $${PWD}/OAIRoleAssignment.h \
    $${PWD}/OAIRoleAssignmentCreateParameters.h \
    $${PWD}/OAIRoleAssignmentFilter.h \
    $${PWD}/OAIRoleAssignmentListResult.h \
    $${PWD}/OAIRoleAssignmentProperties.h \
    $${PWD}/OAIRoleAssignmentPropertiesWithScope.h \
# APIs
    $${PWD}/OAIRoleAssignmentsApi.h \
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
    $${PWD}/OAIRoleAssignment.cpp \
    $${PWD}/OAIRoleAssignmentCreateParameters.cpp \
    $${PWD}/OAIRoleAssignmentFilter.cpp \
    $${PWD}/OAIRoleAssignmentListResult.cpp \
    $${PWD}/OAIRoleAssignmentProperties.cpp \
    $${PWD}/OAIRoleAssignmentPropertiesWithScope.cpp \
# APIs
    $${PWD}/OAIRoleAssignmentsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
