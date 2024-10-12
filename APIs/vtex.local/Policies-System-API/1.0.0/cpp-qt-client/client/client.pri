QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccount.h \
    $${PWD}/OAIAccountType.h \
    $${PWD}/OAICondition.h \
    $${PWD}/OAICondition_conditions_inner.h \
    $${PWD}/OAIEvaluatePolicyRequest.h \
    $${PWD}/OAIPolicyActionGetResponse.h \
    $${PWD}/OAIPolicyGetResponse.h \
    $${PWD}/OAIPolicySaveRequest.h \
    $${PWD}/OAIStatementGetResponse.h \
# APIs
    $${PWD}/OAIPolicyApi.h \
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
    $${PWD}/OAIAccount.cpp \
    $${PWD}/OAIAccountType.cpp \
    $${PWD}/OAICondition.cpp \
    $${PWD}/OAICondition_conditions_inner.cpp \
    $${PWD}/OAIEvaluatePolicyRequest.cpp \
    $${PWD}/OAIPolicyActionGetResponse.cpp \
    $${PWD}/OAIPolicyGetResponse.cpp \
    $${PWD}/OAIPolicySaveRequest.cpp \
    $${PWD}/OAIStatementGetResponse.cpp \
# APIs
    $${PWD}/OAIPolicyApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
