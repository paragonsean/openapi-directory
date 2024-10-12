QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccessApprovalServiceAccount.h \
    $${PWD}/OAIAccessApprovalSettings.h \
    $${PWD}/OAIAccessLocations.h \
    $${PWD}/OAIAccessReason.h \
    $${PWD}/OAIApprovalRequest.h \
    $${PWD}/OAIApproveApprovalRequestMessage.h \
    $${PWD}/OAIApproveDecision.h \
    $${PWD}/OAIDismissDecision.h \
    $${PWD}/OAIEnrolledService.h \
    $${PWD}/OAIListApprovalRequestsResponse.h \
    $${PWD}/OAIResourceProperties.h \
    $${PWD}/OAISignatureInfo.h \
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
    $${PWD}/OAIAccessApprovalServiceAccount.cpp \
    $${PWD}/OAIAccessApprovalSettings.cpp \
    $${PWD}/OAIAccessLocations.cpp \
    $${PWD}/OAIAccessReason.cpp \
    $${PWD}/OAIApprovalRequest.cpp \
    $${PWD}/OAIApproveApprovalRequestMessage.cpp \
    $${PWD}/OAIApproveDecision.cpp \
    $${PWD}/OAIDismissDecision.cpp \
    $${PWD}/OAIEnrolledService.cpp \
    $${PWD}/OAIListApprovalRequestsResponse.cpp \
    $${PWD}/OAIResourceProperties.cpp \
    $${PWD}/OAISignatureInfo.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
