QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIIdentity.h \
    $${PWD}/OAIPolicyAssignment.h \
    $${PWD}/OAIPolicyAssignmentListResult.h \
    $${PWD}/OAIPolicyAssignmentProperties.h \
    $${PWD}/OAIPolicySku.h \
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
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIIdentity.cpp \
    $${PWD}/OAIPolicyAssignment.cpp \
    $${PWD}/OAIPolicyAssignmentListResult.cpp \
    $${PWD}/OAIPolicyAssignmentProperties.cpp \
    $${PWD}/OAIPolicySku.cpp \
# APIs
    $${PWD}/OAIPolicyAssignmentsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
