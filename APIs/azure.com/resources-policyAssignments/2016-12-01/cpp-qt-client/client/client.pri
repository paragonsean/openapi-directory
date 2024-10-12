QT += network

HEADERS += \
# Models
    $${PWD}/OAIPolicyAssignment.h \
    $${PWD}/OAIPolicyAssignmentListResult.h \
    $${PWD}/OAIPolicyAssignmentProperties.h \
# APIs
    $${PWD}/OAIPolicyAssignmentsApi.h \
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
    $${PWD}/OAIPolicyAssignment.cpp \
    $${PWD}/OAIPolicyAssignmentListResult.cpp \
    $${PWD}/OAIPolicyAssignmentProperties.cpp \
# APIs
    $${PWD}/OAIPolicyAssignmentsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
