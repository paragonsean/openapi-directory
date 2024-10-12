QT += network

HEADERS += \
# Models
    $${PWD}/OAIDenyAssignment.h \
    $${PWD}/OAIDenyAssignmentFilter.h \
    $${PWD}/OAIDenyAssignmentListResult.h \
    $${PWD}/OAIDenyAssignmentPermission.h \
    $${PWD}/OAIDenyAssignmentProperties.h \
    $${PWD}/OAIPrincipal.h \
# APIs
    $${PWD}/OAIDenyAssignmentsApi.h \
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
    $${PWD}/OAIDenyAssignment.cpp \
    $${PWD}/OAIDenyAssignmentFilter.cpp \
    $${PWD}/OAIDenyAssignmentListResult.cpp \
    $${PWD}/OAIDenyAssignmentPermission.cpp \
    $${PWD}/OAIDenyAssignmentProperties.cpp \
    $${PWD}/OAIPrincipal.cpp \
# APIs
    $${PWD}/OAIDenyAssignmentsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
