QT += network

HEADERS += \
# Models
    $${PWD}/OAIAmount.h \
    $${PWD}/OAIServiceError.h \
    $${PWD}/OAIStoredValueBalanceCheckRequest.h \
    $${PWD}/OAIStoredValueBalanceCheckResponse.h \
    $${PWD}/OAIStoredValueBalanceMergeRequest.h \
    $${PWD}/OAIStoredValueBalanceMergeResponse.h \
    $${PWD}/OAIStoredValueIssueRequest.h \
    $${PWD}/OAIStoredValueIssueResponse.h \
    $${PWD}/OAIStoredValueLoadRequest.h \
    $${PWD}/OAIStoredValueLoadResponse.h \
    $${PWD}/OAIStoredValueStatusChangeRequest.h \
    $${PWD}/OAIStoredValueStatusChangeResponse.h \
    $${PWD}/OAIStoredValueVoidRequest.h \
    $${PWD}/OAIStoredValueVoidResponse.h \
# APIs
    $${PWD}/OAIGeneralApi.h \
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
    $${PWD}/OAIAmount.cpp \
    $${PWD}/OAIServiceError.cpp \
    $${PWD}/OAIStoredValueBalanceCheckRequest.cpp \
    $${PWD}/OAIStoredValueBalanceCheckResponse.cpp \
    $${PWD}/OAIStoredValueBalanceMergeRequest.cpp \
    $${PWD}/OAIStoredValueBalanceMergeResponse.cpp \
    $${PWD}/OAIStoredValueIssueRequest.cpp \
    $${PWD}/OAIStoredValueIssueResponse.cpp \
    $${PWD}/OAIStoredValueLoadRequest.cpp \
    $${PWD}/OAIStoredValueLoadResponse.cpp \
    $${PWD}/OAIStoredValueStatusChangeRequest.cpp \
    $${PWD}/OAIStoredValueStatusChangeResponse.cpp \
    $${PWD}/OAIStoredValueVoidRequest.cpp \
    $${PWD}/OAIStoredValueVoidResponse.cpp \
# APIs
    $${PWD}/OAIGeneralApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
