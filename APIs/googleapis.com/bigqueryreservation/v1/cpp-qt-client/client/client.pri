QT += network

HEADERS += \
# Models
    $${PWD}/OAIAssignment.h \
    $${PWD}/OAIAutoscale.h \
    $${PWD}/OAIBiReservation.h \
    $${PWD}/OAICapacityCommitment.h \
    $${PWD}/OAIListAssignmentsResponse.h \
    $${PWD}/OAIListCapacityCommitmentsResponse.h \
    $${PWD}/OAIListReservationsResponse.h \
    $${PWD}/OAIMergeCapacityCommitmentsRequest.h \
    $${PWD}/OAIMoveAssignmentRequest.h \
    $${PWD}/OAIReservation.h \
    $${PWD}/OAISearchAllAssignmentsResponse.h \
    $${PWD}/OAISearchAssignmentsResponse.h \
    $${PWD}/OAISplitCapacityCommitmentRequest.h \
    $${PWD}/OAISplitCapacityCommitmentResponse.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAITableReference.h \
# APIs
    $${PWD}/OAIProjectsApi.h \
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
    $${PWD}/OAIAssignment.cpp \
    $${PWD}/OAIAutoscale.cpp \
    $${PWD}/OAIBiReservation.cpp \
    $${PWD}/OAICapacityCommitment.cpp \
    $${PWD}/OAIListAssignmentsResponse.cpp \
    $${PWD}/OAIListCapacityCommitmentsResponse.cpp \
    $${PWD}/OAIListReservationsResponse.cpp \
    $${PWD}/OAIMergeCapacityCommitmentsRequest.cpp \
    $${PWD}/OAIMoveAssignmentRequest.cpp \
    $${PWD}/OAIReservation.cpp \
    $${PWD}/OAISearchAllAssignmentsResponse.cpp \
    $${PWD}/OAISearchAssignmentsResponse.cpp \
    $${PWD}/OAISplitCapacityCommitmentRequest.cpp \
    $${PWD}/OAISplitCapacityCommitmentResponse.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAITableReference.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
