QT += network

HEADERS += \
# Models
    $${PWD}/OAIActionDescription.h \
    $${PWD}/OAIActionHelp.h \
    $${PWD}/OAIActionHelpResponse.h \
    $${PWD}/OAIDescribeActionResponse.h \
    $${PWD}/OAIDescribeServiceResponse.h \
    $${PWD}/OAIEntryPoint.h \
    $${PWD}/OAIEntryPointParameter.h \
    $${PWD}/OAIErrorModel.h \
    $${PWD}/OAIExecBody.h \
    $${PWD}/OAIListActionsResponse.h \
    $${PWD}/OAIListServicesResponse.h \
    $${PWD}/OAILoadService_200_response.h \
    $${PWD}/OAILoadService_request.h \
    $${PWD}/OAILoginResponse.h \
    $${PWD}/OAILoginResponse_response.h \
    $${PWD}/OAILogoutResponse.h \
    $${PWD}/OAILogoutResponse_response.h \
    $${PWD}/OAIServiceDescription.h \
# APIs
    $${PWD}/OAIOSDBApi.h \
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
    $${PWD}/OAIActionDescription.cpp \
    $${PWD}/OAIActionHelp.cpp \
    $${PWD}/OAIActionHelpResponse.cpp \
    $${PWD}/OAIDescribeActionResponse.cpp \
    $${PWD}/OAIDescribeServiceResponse.cpp \
    $${PWD}/OAIEntryPoint.cpp \
    $${PWD}/OAIEntryPointParameter.cpp \
    $${PWD}/OAIErrorModel.cpp \
    $${PWD}/OAIExecBody.cpp \
    $${PWD}/OAIListActionsResponse.cpp \
    $${PWD}/OAIListServicesResponse.cpp \
    $${PWD}/OAILoadService_200_response.cpp \
    $${PWD}/OAILoadService_request.cpp \
    $${PWD}/OAILoginResponse.cpp \
    $${PWD}/OAILoginResponse_response.cpp \
    $${PWD}/OAILogoutResponse.cpp \
    $${PWD}/OAILogoutResponse_response.cpp \
    $${PWD}/OAIServiceDescription.cpp \
# APIs
    $${PWD}/OAIOSDBApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
