QT += network

HEADERS += \
# Models
    $${PWD}/OAIApproval.h \
    $${PWD}/OAIErrorAdditionalInfo.h \
    $${PWD}/OAIErrorAdditionalInfo_info.h \
    $${PWD}/OAIErrorBody.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAILockboxRequestResponse.h \
    $${PWD}/OAILockboxRequestResponseProperties.h \
    $${PWD}/OAILockboxRequestStatus.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIRequestListResult.h \
# APIs
    $${PWD}/OAIOperationsApi.h \
    $${PWD}/OAIRequestsApi.h \
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
    $${PWD}/OAIApproval.cpp \
    $${PWD}/OAIErrorAdditionalInfo.cpp \
    $${PWD}/OAIErrorAdditionalInfo_info.cpp \
    $${PWD}/OAIErrorBody.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAILockboxRequestResponse.cpp \
    $${PWD}/OAILockboxRequestResponseProperties.cpp \
    $${PWD}/OAILockboxRequestStatus.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIRequestListResult.cpp \
# APIs
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAIRequestsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
